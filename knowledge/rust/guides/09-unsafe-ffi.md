# Unsafe and FFI Guidelines

Patterns for writing sound unsafe Rust and for crossing language boundaries. Covers the soundness contract (`unsafe` = UB risk, never "dangerous"), data representation for FFI (`repr(C)`, `repr(transparent)`, DSTs, ZSTs, niche optimization), raw pointers and uninitialized memory (`MaybeUninit`, `ptr::write/copy`, raw reference syntax), unsafe trait design (`Send`/`Sync`/variance/drop check), FFI declarations and strings, error and object-based FFI patterns, panic isolation, inline assembly, and `no_std` runtime contracts. Every unsafe block here carries a `// SAFETY:` comment; follow that convention in your own code.


## US-01: Unsafe Means UB Risk, Not "Dangerous"

**Strength**: MUST

**Summary**: The `unsafe` keyword marks a technical contract: misuse can cause undefined behavior. It is not a general "dangerous operation" annotation.

```rust
// ❌ BAD: dangerous but cannot cause UB — should not be unsafe
unsafe fn delete_database() {
    std::fs::remove_dir_all("/var/lib/db").unwrap();
}

// ✅ GOOD: same function — dangerous, but safe to call
fn delete_database() {
    std::fs::remove_dir_all("/var/lib/db").unwrap();
}

// ✅ GOOD: unsafe is correct here — misuse causes UB
/// Reads a value through a raw pointer.
///
/// # Safety
///
/// - `ptr` must be non-null, aligned, and dereferenceable for `T`
/// - `*ptr` must be a valid, initialized `T`
/// - No other access to `*ptr` may occur while this reference is alive
pub unsafe fn read_ptr<T>(ptr: *const T) -> T {
    // SAFETY: the caller upholds the four conditions documented above.
    unsafe { ptr.read() }
}
```

**Rationale**: Conflating "dangerous" with `unsafe` causes warning fatigue — readers stop taking the keyword seriously. Rust's safety guarantee is precisely that safe code cannot cause UB; `unsafe` is the gate where the compiler stops proving that for you and the author takes over.

**See also**: M-UNSAFE-IMPLIES-UB, US-02, US-03

---

## US-02: All Code Must Be Sound

**Strength**: MUST

**Summary**: Safe code must never cause undefined behavior, even for "weird" or adversarial inputs. Unsoundness has no exceptions.

```rust
// ❌ UNSOUND: a safe function that can trigger UB
pub fn as_u128_bad<T>(x: &T) -> &u128 {
    // SAFETY: ... there is none. Any T != 16 bytes is UB.
    unsafe { std::mem::transmute(x) }
}

// ❌ UNSOUND: blanket Send for anything — breaks data-race freedom
struct AlwaysSend<T>(T);
unsafe impl<T> Send for AlwaysSend<T> {}

// ❌ UNSOUND: safe API hands out unbounded index access
pub fn get(slice: &[u8], i: usize) -> u8 {
    // SAFETY: ... none; `i >= slice.len()` is UB.
    unsafe { *slice.get_unchecked(i) }
}

// ✅ SOUND: the type system enforces the precondition
pub fn as_u128(x: &[u8; 16]) -> u128 {
    // SAFETY: [u8; 16] and u128 have the same size and layout is trivial.
    unsafe { std::ptr::read_unaligned(x.as_ptr().cast()) }
}

// ✅ SOUND: invariants checked before the unsafe operation
pub fn get_checked(slice: &[u8], i: usize) -> Option<u8> {
    if i < slice.len() {
        // SAFETY: i < slice.len() verified on the line above.
        Some(unsafe { *slice.get_unchecked(i) })
    } else {
        None
    }
}
```

**Rationale**: If a safe caller can cause UB, the whole module is unsound — the boundary between trusted and untrusted code is broken. The Rust community treats unsoundness as a bug, even when the triggering code is contrived ("remote, theoretical possibility" is still UB). Soundness lives at the module boundary: safe functions may rely on invariants that other functions in the same module maintain.

**See also**: M-UNSOUND, US-01, US-12

---

## US-03: Document Safety Requirements and Each Unsafe Block

**Strength**: MUST

**Summary**: Every `unsafe fn` needs a `# Safety` section; every `unsafe { ... }` block needs a `// SAFETY:` comment explaining why the requirements hold here.

```rust
/// Writes `value` at `ptr` without running the destructor of the old value.
///
/// # Safety
///
/// - `ptr` must be valid for writes of `T`
/// - `ptr` must be properly aligned
/// - The existing value at `*ptr` (if any) must not need dropping, or it must
///   already have been taken/forgotten
pub unsafe fn write<T>(ptr: *mut T, value: T) {
    // SAFETY: contract is forwarded to the caller; std::ptr::write has the
    // same requirements we documented.
    unsafe { std::ptr::write(ptr, value) }
}

fn consume(data: &[u8], i: usize) -> Option<u8> {
    if i >= data.len() { return None; }
    let byte = unsafe {
        // SAFETY: we returned above when i was out of bounds, so i < data.len().
        *data.get_unchecked(i)
    };
    Some(byte)
}

/// A marker trait for types whose all-zero bit pattern is a valid value.
///
/// # Safety
///
/// Implementors must ensure that reading `size_of::<Self>()` zero bytes as
/// `Self` produces a valid, non-UB instance.
pub unsafe trait Zeroable {}

// SAFETY: every bit pattern is a valid u32.
unsafe impl Zeroable for u32 {}
```

**Rationale**: `# Safety` is the author's contract with callers; `// SAFETY:` is the author's proof that this particular site discharges that contract. Together they turn unsafe code into auditable code. The `clippy::undocumented_unsafe_blocks` and `clippy::missing_safety_doc` lints enforce the rule mechanically.

**See also**: M-UNSAFE, US-12

---

## US-04: Use `unsafe` Only for the Three Valid Reasons

**Strength**: MUST

**Summary**: Reach for `unsafe` only for (1) novel abstractions impossible to express safely, (2) performance validated by benchmarks, or (3) FFI / platform calls. Not to silence the borrow checker.

```rust
// ❌ BAD: shortcut — safe iterator is the right answer
fn sum_bad(xs: &[i32]) -> i32 {
    let mut total = 0;
    unsafe {
        for i in 0..xs.len() {
            // SAFETY: i < xs.len() — but there is no performance reason to do this
            total += *xs.get_unchecked(i);
        }
    }
    total
}

// ✅ GOOD
fn sum(xs: &[i32]) -> i32 { xs.iter().sum() }

// ❌ BAD: unsafe impl Send to fit into Tokio — this is unsound if T isn't Send
struct Bypass<T>(T);
unsafe impl<T> Send for Bypass<T> {}

// ❌ BAD: transmute to bypass lifetimes
fn extend_lifetime<'a>(s: &'a str) -> &'static str {
    // SAFETY: there is no safety — this is a memory-error time bomb.
    unsafe { std::mem::transmute(s) }
}

// ✅ GOOD: performance reason, documented and benchmarked
/// Computes the dot product of two slices.
///
/// # Safety
///
/// `a` and `b` must have the same length.
///
/// Using `get_unchecked` here is measured 18% faster than the iterator form
/// for length >= 1024 (see `benches/dot.rs`).
pub unsafe fn dot_unchecked(a: &[f64], b: &[f64]) -> f64 {
    let mut acc = 0.0;
    for i in 0..a.len() {
        // SAFETY: the caller guarantees a.len() == b.len(), and i < a.len().
        unsafe { acc += a.get_unchecked(i) * b.get_unchecked(i); }
    }
    acc
}
```

**Rationale**: Novel abstractions, proven-hot loops, and FFI are the cases where safe Rust genuinely can't express the required semantics. Everything else — including "I need to get this past the borrow checker" — has a safe alternative that is clearer, easier to review, and compiles to the same code under optimization.

**See also**: M-UNSAFE, US-03

---

## US-05: Contain Unsafety in Small Modules

**Strength**: SHOULD

**Summary**: Confine every unsafe invariant to a tiny module whose public API is safe. Auditing soundness then means auditing one short file.

```rust
// ✅ GOOD: the only unsafe in this module lives in ~30 lines
mod safe_buffer {
    use std::alloc::{alloc, dealloc, Layout};

    pub struct Buffer {
        ptr: *mut u8,
        len: usize,
    }

    // Module invariant:
    // - `ptr` is non-null, aligned for u8, points to an allocation of `len` bytes
    // - The allocation is owned by this Buffer (freed in Drop)

    impl Buffer {
        pub fn new(len: usize) -> Self {
            let layout = Layout::array::<u8>(len).expect("too large");
            // SAFETY: Layout is valid (non-zero size, checked above).
            let ptr = unsafe { alloc(layout) };
            assert!(!ptr.is_null(), "allocation failed");
            Self { ptr, len }
        }

        pub fn as_slice(&self) -> &[u8] {
            // SAFETY: module invariant — ptr points to len valid bytes.
            unsafe { std::slice::from_raw_parts(self.ptr, self.len) }
        }

        pub fn as_mut_slice(&mut self) -> &mut [u8] {
            // SAFETY: module invariant — &mut self guarantees exclusive access.
            unsafe { std::slice::from_raw_parts_mut(self.ptr, self.len) }
        }
    }

    impl Drop for Buffer {
        fn drop(&mut self) {
            let layout = Layout::array::<u8>(self.len).unwrap();
            // SAFETY: ptr came from `alloc(layout)` in new().
            unsafe { dealloc(self.ptr, layout); }
        }
    }

    // SAFETY: Buffer owns its allocation exclusively; sending the owning
    // handle between threads is fine.
    unsafe impl Send for Buffer {}
    // SAFETY: &Buffer hands out &[u8], which is already Sync.
    unsafe impl Sync for Buffer {}
}
```

**Rationale**: Soundness boundaries equal module boundaries (per the Rust language team). Keep the module small so reviewers can verify that every safe entry point respects the module-wide invariants and no external code can violate them.

**See also**: US-02, US-14

---

## US-06: Choose `repr` Deliberately for FFI and Layout

**Strength**: MUST

**Summary**: Default Rust layout is unspecified. For FFI, raw byte access, or layout-sensitive code, pick `repr(C)`, `repr(transparent)`, `repr(packed)`, `repr(align(N))`, or `repr(uN)` explicitly.

```rust
use std::num::NonZeroU32;

// ✅ repr(C): stable, C-compatible field order and padding
#[repr(C)]
pub struct Header {
    pub magic: u32,
    pub version: u16,
    pub flags: u16,
}

// ✅ repr(transparent): same ABI and layout as the inner type, preserves niches
#[repr(transparent)]
pub struct Handle(NonZeroU32);
// size_of::<Option<Handle>>() == 4 (niche survives the wrapper)

// ✅ repr(u8): stable discriminant size for FFI enums
#[repr(u8)]
pub enum Opcode {
    Nop = 0x00,
    Ret = 0x01,
    Jmp = 0x02,
}

// ⚠️ repr(packed): no padding; taking references to fields may be unsound
#[repr(C, packed)]
pub struct Wire { kind: u8, value: u32 }

// Do NOT take &packed.value — use std::ptr::addr_of! instead
fn read_value(w: &Wire) -> u32 {
    let ptr = std::ptr::addr_of!(w.value);
    // SAFETY: addr_of! yields a (possibly misaligned) raw pointer; read_unaligned
    // handles the alignment.
    unsafe { ptr.read_unaligned() }
}

// ✅ repr(align(N)): stronger alignment (e.g., cache line)
#[repr(align(64))]
pub struct CacheLine([u8; 64]);

// ❌ BAD: default layout across FFI — reordering is allowed
pub struct BadPoint { x: f64, y: f64 }
extern "C" { fn process_point(p: *const BadPoint); } // UB potential
```

**Rationale**: `repr(C)` gives you the layout C expects. `repr(transparent)` is essential when a newtype must be ABI-compatible with its inner type — without it, `Option<Handle>` loses the `NonZeroU32` niche. `repr(packed)` is rarely correct outside FFI because unaligned references are UB. `repr(uN)` is required for FFI-safe enums with a known discriminant size.

**See also**: TD-21, US-18, nomicon "Data Representation"

---

## US-07: Understand Exotic Sizes — DSTs, ZSTs, and Empty Types

**Strength**: SHOULD

**Summary**: Most generic code assumes `Sized`. Dynamically sized types (`str`, `[T]`, `dyn Trait`) can only appear behind pointers; zero-sized types optimize to nothing; uninhabited types (`!`, `enum Void {}`) can never be produced.

```rust
// DST: wide pointer — pointer + length or pointer + vtable
let slice: &[u8] = b"hello";
assert_eq!(std::mem::size_of_val(slice), 5);
assert_eq!(std::mem::size_of::<&[u8]>(), 2 * std::mem::size_of::<usize>());

// ?Sized bound to accept DSTs through references
pub fn print_any<T: ?Sized + std::fmt::Debug>(x: &T) { println!("{x:?}"); }
print_any("hello");          // T = str
print_any(&42u32);           // T = u32

// ZST: zero bytes at runtime, still participates in types
struct Token;
assert_eq!(std::mem::size_of::<Token>(), 0);
// Vec<()> stores nothing — only the length matters
let v: Vec<()> = vec![(); 100];
assert_eq!(v.len(), 100);

// Empty type: no legitimate values
enum Never {}

// A function returning `Never` can never return normally.
// `Result<T, !>` is niche-optimized to T because `Err(!)` is unreachable.
fn always_ok() -> Result<i32, std::convert::Infallible> {
    Ok(42)
}
```

**Rationale**: DSTs require `?Sized` to be accepted as generic parameters. ZSTs matter for type-level tokens (TD-19) and for collections of unit types — but they require care in unsafe code because `ptr.add(1)` on a ZST doesn't advance the address. Empty types encode impossibility and let the compiler elide branches.

**See also**: TD-19, TD-22, nomicon "Exotic Sizes"

---

## US-08: Use `NonZero*` and Niche-Carrying Types for Size

**Strength**: SHOULD

**Summary**: `Option<NonZeroU32>` is 4 bytes; `Option<u32>` is 8. Use `NonZero*`, `&T`, `Box<T>`, and `NonNull<T>` so `Option<_>` stays compact.

```rust
use std::num::NonZeroU32;
use std::ptr::NonNull;

pub struct Handle(NonZeroU32);   // raw FFI handle, never zero

// Same size as u32 — the None case reuses the zero bit pattern
assert_eq!(std::mem::size_of::<Option<Handle>>(), std::mem::size_of::<u32>());

// NonNull<T>: non-null, covariant, for smart pointers
pub struct MyBox<T> {
    ptr: NonNull<T>,
    _owned: std::marker::PhantomData<T>,
}
assert_eq!(
    std::mem::size_of::<Option<MyBox<i32>>>(),
    std::mem::size_of::<*mut i32>()
);
```

**Rationale**: Niche optimization lets `Option<T>` reuse an invalid bit pattern of `T` as the `None` discriminant. This shrinks `Option<Handle>` to the size of `u32` and lets raw-pointer types in smart-pointer crates behave like nullable C pointers without paying for a separate discriminant byte.

**See also**: TD-20, US-06

---

## US-09: Pointer Aliasing, Validity, and Provenance

**Strength**: MUST

**Summary**: References and raw pointers have strict rules. `&T` promises the pointee is not mutated (except through `UnsafeCell`). `&mut T` promises exclusive access. Raw pointers carry provenance — casting through `usize` without care loses it and is UB.

```rust
// ❌ UB: two &mut to the same memory simultaneously
let mut x = 42;
let p = &mut x as *mut i32;
let a: &mut i32 = unsafe { &mut *p };
let b: &mut i32 = unsafe { &mut *p };    // ALIASING VIOLATION
*a = 1;
*b = 2;

// ❌ UB: dereferencing null, dangling, or misaligned
let null: *const i32 = std::ptr::null();
let v = unsafe { *null };                 // UB

// ❌ UB: writing via a reference whose target is read-only (e.g., const-promoted)
let s: &mut str = unsafe { &mut *(("hi".as_ptr() as *const u8) as *mut str) };

// ✅ valid: exclusive &mut lifetimes don't overlap
let mut x = 42;
{
    let a = &mut x;
    *a = 1;
}
let b = &mut x;
*b = 2;

// ✅ provenance-preserving raw pointer use
let mut v = vec![1u8, 2, 3, 4];
let base: *mut u8 = v.as_mut_ptr();
// SAFETY: offset is in-bounds (< v.len()), same allocation as `base`.
let third: *mut u8 = unsafe { base.add(2) };
// SAFETY: third is aligned (u8), dereferenceable, exclusively borrowed.
unsafe { *third = 99; }
```

Pointer validity rules in one place:

- Reads/writes require the pointer to be non-null, dereferenceable, and aligned for the pointed type.
- `&T` may only be created when the pointee is not mutated for the reference's lifetime (except through `UnsafeCell`).
- `&mut T` may only be created when no other reference or raw-pointer access occurs for its lifetime.
- `Box<T>` is treated like `&'static mut T` for aliasing.
- Reinterpreting `*mut T` via `as usize` then back through arithmetic is UB under the Strict Provenance model — use `ptr.wrapping_offset_from(base)` or the `core::ptr` intrinsics instead.

**Rationale**: The borrow checker enforces these rules for references; raw pointers let you bypass that proof, so you take on the obligation yourself. Miri can catch most violations under test — see US-22.

**See also**: US-02, US-22, nomicon "References and Pointers"

---

## US-10: Work With Uninitialized Memory via `MaybeUninit`

**Strength**: MUST

**Summary**: Never use `mem::uninitialized()` or `mem::zeroed()` on types where all-zeros is invalid. Use `MaybeUninit<T>` to hold uninitialized memory, initialize through raw pointers, and transition to `T` only once fully initialized.

```rust
use std::mem::{self, MaybeUninit};

// ❌ BAD: zeroed(): valid for u32, UB for Box/&T/NonZeroU32/enum discriminants
let _bad: Box<i32> = unsafe { mem::zeroed() };   // immediate UB (null Box)

// ✅ GOOD: build an array element-by-element
const N: usize = 4;
fn make_boxes() -> [Box<u32>; N] {
    let mut arr: [MaybeUninit<Box<u32>>; N] =
        [const { MaybeUninit::uninit() }; N];

    for (i, slot) in arr.iter_mut().enumerate() {
        slot.write(Box::new(i as u32));
    }

    // SAFETY: every element was written exactly once above.
    unsafe { mem::transmute::<[MaybeUninit<Box<u32>>; N], [Box<u32>; N]>(arr) }
}

// ✅ GOOD: initialize a struct field-by-field without creating references
// to uninitialized memory
pub struct Config { host: String, port: u16 }

fn make_config() -> Config {
    let mut uninit = MaybeUninit::<Config>::uninit();
    let ptr = uninit.as_mut_ptr();

    // SAFETY: addr_of_mut! on field projections of *mut T is allowed even
    // when the memory is uninitialized; we never form a &mut Config.
    unsafe {
        std::ptr::addr_of_mut!((*ptr).host).write(String::from("localhost"));
        std::ptr::addr_of_mut!((*ptr).port).write(8080);
    }

    // SAFETY: every field has been initialized with a valid value.
    unsafe { uninit.assume_init() }
}
```

Rules of thumb:

- Dropping a `MaybeUninit<T>` is a no-op — it never calls `T::drop`. This is what makes element-by-element init safe even when earlier slots panic.
- Constructing a *reference* to uninitialized memory is UB. Use `std::ptr::addr_of!` / `addr_of_mut!` to get a raw pointer without a reference.
- `Container<MaybeUninit<T>>` and `Container<T>` are **not** layout-compatible in general — `Option<bool>` uses niche optimization that `Option<MaybeUninit<bool>>` breaks. Arrays are the main documented exception.
- `mem::uninitialized` is deprecated; always use `MaybeUninit`.

**Rationale**: Uninitialized memory is a normal tool for optimization, FFI out-parameters, and in-place construction. `MaybeUninit` is the type-level receipt that says "these bits may be invalid" — the compiler stops assuming the value is valid, which is exactly what you need to avoid UB on reads and drops.

**See also**: US-09, US-13, nomicon "Working With Uninitialized Memory"

---

## US-11: Raw Pointer Writes and Moves Without Drops

**Strength**: MUST

**Summary**: Assignment (`*ptr = value`) drops the old value. For uninitialized or not-yet-valid memory, use `ptr::write`, `ptr::copy`, `ptr::copy_nonoverlapping`, and `ptr::read` to move without running a destructor on garbage.

```rust
use std::ptr;

// ❌ BAD: assignment through a raw pointer to uninitialized memory
let mut uninit = std::mem::MaybeUninit::<String>::uninit();
let ptr = uninit.as_mut_ptr();
// *ptr = String::from("hi");   // drops uninitialized String → UB

// ✅ GOOD: ptr::write does not drop the old value
unsafe {
    // SAFETY: ptr is aligned, dereferenceable, and the slot is uninitialized.
    ptr::write(ptr, String::from("hi"));
}

// ✅ GOOD: ptr::read takes ownership out of a raw pointer
let owned: String = unsafe {
    // SAFETY: *ptr was just initialized, and we will never read *ptr again
    // (we conceptually moved it out).
    ptr::read(ptr)
};

// ✅ copy vs copy_nonoverlapping
let src = [1u8, 2, 3, 4];
let mut dst = [0u8; 4];
unsafe {
    // SAFETY: disjoint allocations, both valid for 4 bytes, aligned for u8.
    ptr::copy_nonoverlapping(src.as_ptr(), dst.as_mut_ptr(), 4);
}

// Use `copy` (memmove) when source and destination may overlap.
let mut buf = [1u8, 2, 3, 4, 0, 0];
unsafe {
    // SAFETY: overlapping is fine here; copy == memmove.
    ptr::copy(buf.as_ptr(), buf.as_mut_ptr().add(2), 4);
}
assert_eq!(buf, [1, 2, 1, 2, 3, 4]);
```

**Rationale**: Rust inserts `drop` calls at every assignment to owned memory. That behavior is wrong whenever the "old" contents are uninitialized, half-constructed, or already moved out. `ptr::write`/`ptr::read`/`ptr::copy*` give you move semantics without drop, which is the building block for `Vec::push`, `mem::swap`, and allocator-backed containers.

**See also**: US-10, US-13

---

## US-12: Minimize and Wrap Every Unsafe Block

**Strength**: MUST

**Summary**: Shrink `unsafe { ... }` to the exact UB-risking operations. Lift everything else out. Each block gets its own `// SAFETY:` comment.

```rust
// ❌ BAD: unsafe wraps the whole function
unsafe fn process(ptr: *const u8, len: usize) -> Vec<u8> {
    let mut out = Vec::with_capacity(len);
    for i in 0..len {
        let byte = *ptr.add(i);          // the only UB-risking operation
        out.push(byte);                  // safe — but inside unsafe {}
        validate(byte);                  // safe — but inside unsafe {}
    }
    out
}

// ✅ GOOD: construct a safe &[u8] once, then do the rest in safe code
pub fn process(ptr: *const u8, len: usize) -> Vec<u8> {
    // SAFETY: caller guarantees ptr is valid for `len` aligned bytes and
    // the memory is not mutated during this call.
    let slice = unsafe { std::slice::from_raw_parts(ptr, len) };

    let mut out = Vec::with_capacity(len);
    for &byte in slice {
        out.push(byte);
        validate(byte);
    }
    out
}

// Opt in to `unsafe_op_in_unsafe_fn` so unsafe fns still require explicit blocks.
#![deny(unsafe_op_in_unsafe_fn)]

/// # Safety
/// `ptr` is valid for reads of `len` bytes.
pub unsafe fn sum(ptr: *const u8, len: usize) -> u64 {
    // SAFETY: caller contract.
    let s: &[u8] = unsafe { std::slice::from_raw_parts(ptr, len) };
    s.iter().map(|&b| b as u64).sum()
}

fn validate(_: u8) {}
```

**Rationale**: The smaller the unsafe block, the smaller the audit surface. The `unsafe_op_in_unsafe_fn` lint (default in Edition 2024) forces the same discipline inside `unsafe fn` bodies — previously, those bodies were implicitly one giant unsafe block.

**See also**: US-03, US-05

---

## US-13: Exception Safety — Unwinding Through Unsafe Code

**Strength**: MUST

**Summary**: If a panic can propagate through a region that has temporarily broken an invariant, the invariant must be re-established before the panic escapes. Use guards, atomic updates, or `catch_unwind` at boundaries.

```rust
use std::ptr;

// ❌ BAD: if `clone()` panics, old values are leaked AND we've written into
// uninitialized slots inconsistently.
fn fill_bad<T: Clone>(buf: &mut [T], value: T) {
    for slot in buf.iter_mut() {
        *slot = value.clone();           // panic here → partial init
    }
}

// ✅ GOOD: Vec::extend_with pattern — guard ensures only the written
// elements are dropped on panic.
struct SetLenOnDrop<'a> { vec: &'a mut Vec<u8>, local_len: usize }
impl<'a> Drop for SetLenOnDrop<'a> {
    fn drop(&mut self) { self.vec.set_len(self.local_len); }
}

fn push_many(v: &mut Vec<u8>, source: impl IntoIterator<Item = u8>) {
    let mut guard = SetLenOnDrop { local_len: v.len(), vec: v };
    for b in source {
        // If `next()` panics here, `guard` Drop sets the vec's length to
        // the number we've actually written, dropping only those elements.
        guard.vec.reserve(1);
        let len = guard.local_len;
        let ptr = guard.vec.as_mut_ptr();
        unsafe {
            // SAFETY: we reserved one more slot; ptr.add(len) is in bounds.
            ptr::write(ptr.add(len), b);
        }
        guard.local_len += 1;
    }
    let final_len = guard.local_len;
    std::mem::forget(guard);
    unsafe {
        // SAFETY: we wrote `final_len - original_len` new elements above.
        v.set_len(final_len);
    }
}
```

Minimal vs maximal exception safety:

- **Minimal**: a panic does not cause UB. Leaks are acceptable. This is the bar for all unsafe code.
- **Maximal**: a panic leaves every observable value in a meaningful (usually original) state. Required for container APIs like `Vec::insert`, `HashMap::insert`.

**Rationale**: Rust's unwinding is real — even code that "can't panic" may (allocator OOM, `Debug` impl, user closure, integer overflow in debug). Unsafe code must assume any safe call inside it can unwind. Guard types with `Drop` that restore invariants are the standard pattern.

**See also**: US-10, US-20, nomicon "Unwinding" and "Exception Safety"

---

## US-14: Splitting Borrows Safely

**Strength**: SHOULD

**Summary**: When you need disjoint mutable access to parts of one value, prefer stdlib splitters (`split_at_mut`, `split_first_mut`, iterator adapters) or move the field out with `mem::take` / `Option::take` — reach for raw pointers only as a last resort.

```rust
// ❌ BAD: two overlapping &mut via raw pointers — UB if they alias in practice
fn split_bad<T>(s: &mut [T]) -> (&mut [T], &mut [T]) {
    let ptr = s.as_mut_ptr();
    let len = s.len();
    unsafe {
        // SAFETY: ??? split point is arbitrary — easy to make a mistake.
        let left = std::slice::from_raw_parts_mut(ptr, len / 2);
        let right = std::slice::from_raw_parts_mut(ptr.add(len / 2), len - len / 2);
        (left, right)
    }
}

// ✅ GOOD: stdlib enforces the disjointness invariant
fn split<T>(s: &mut [T]) -> (&mut [T], &mut [T]) {
    s.split_at_mut(s.len() / 2)
}

// ✅ GOOD: Option::take moves ownership without aliasing
struct Node { value: i32, next: Option<Box<Node>> }
impl Node {
    fn pop_next(&mut self) -> Option<Box<Node>> {
        self.next.take()     // now self.next == None, Box ownership is ours
    }
}

// ✅ GOOD: mem::take replaces with Default::default(); zero unsafe
fn drain_strings(v: &mut Vec<String>) -> Vec<String> {
    std::mem::take(v)
}
```

**Rationale**: The borrow checker rejects `let a = &mut s[0]; let b = &mut s[1];` because the lexical scope of `&mut s` is one call. Splitter methods encode the disjointness as a function signature the compiler understands. `Option::take` and `mem::take` avoid the problem by moving values rather than aliasing them.

**See also**: US-09

---

## US-15: Casts, `as`, and `transmute` Rules

**Strength**: MUST

**Summary**: `as` is non-transitive and can silently truncate. `mem::transmute` requires equal-size, validity-preserving types. Never transmute `&T` to `&mut T`.

```rust
// `as` truncation / sign surprises
let x: i32 = -1;
let y: u8 = x as u8;                 // 255 (two's complement)
let big: u64 = 1_000_000_000_000;
let small: u32 = big as u32;          // truncates — no warning

// ❌ UB: transmute to a different size
let x: u32 = 42;
let y: u64 = unsafe { std::mem::transmute(x) };   // UB — size mismatch

// ❌ UB: &T → &mut T transmute (writes through what the compiler thinks is read-only)
fn bad_mut<T>(x: &T) -> &mut T {
    // SAFETY: none — this is never sound.
    unsafe { std::mem::transmute(x) }
}

// ✅ valid numeric conversion — explicit widening/narrowing
let y: u64 = x as u64;                // widening: always safe
let z: u32 = big.try_into().unwrap(); // checked narrowing

// ✅ transmute between types of equal size and compatible validity
#[repr(transparent)]
pub struct Millimeters(f32);

let m: Millimeters = unsafe { std::mem::transmute(1.5_f32) };
// — sound because of repr(transparent)

// ✅ prefer bytemuck/zerocopy over hand-rolled transmute
use bytemuck::{cast_slice, Pod, Zeroable};

#[derive(Copy, Clone, Pod, Zeroable)]
#[repr(C)]
struct Vertex { pos: [f32; 3], col: [f32; 4] }

fn to_bytes(v: &[Vertex]) -> &[u8] { cast_slice(v) }   // compile-time checked
```

**Rationale**: `as` is convenient but it's a Swiss-army knife that papers over semantic differences (int→int is a wrap; int→float is nearest; float→int is saturating since Rust 1.45; pointer→int loses provenance). `transmute` is strictly more powerful and strictly more dangerous — every rule of validity (US-10) must hold for both the source and destination types. Prefer checked conversions (`try_into`) and purpose-built crates (`bytemuck`, `zerocopy`) whenever possible.

**See also**: US-10, US-22, nomicon "Casts and Transmutes"

---

## US-16: Unsafe Traits — `Send`, `Sync`, and Custom Invariants

**Strength**: MUST

**Summary**: A trait is `unsafe` when implementations must uphold invariants the compiler can't check. `Send`, `Sync`, `GlobalAlloc`, and `PhantomPinned` are the canonical examples. Writing `unsafe impl Send for T {}` is a claim — you are responsible for making it true.

```rust
use std::cell::UnsafeCell;

// ❌ UNSOUND: the UnsafeCell itself is not thread-safe
struct Racy(UnsafeCell<u64>);
unsafe impl Sync for Racy {}     // WRONG — safe &Racy allows data races

// ✅ SOUND: a spinlock around the UnsafeCell
pub struct SpinLock<T> {
    locked: std::sync::atomic::AtomicBool,
    data: UnsafeCell<T>,
}

// SAFETY: SpinLock serializes access through the atomic flag, so &SpinLock<T>
// gives out &mut T only one thread at a time; T: Send is sufficient.
unsafe impl<T: Send> Sync for SpinLock<T> {}
unsafe impl<T: Send> Send for SpinLock<T> {}

// Custom unsafe trait — invariants callers and implementors must agree on
/// # Safety
///
/// Implementors must guarantee that the bit pattern of all zeros is a valid
/// instance of `Self`.
pub unsafe trait Zeroable: Sized {
    fn zeroed() -> Self {
        // SAFETY: the trait's contract says all-zeros is valid for Self.
        unsafe { std::mem::zeroed() }
    }
}

// SAFETY: every bit pattern is a valid u32.
unsafe impl Zeroable for u32 {}
// unsafe impl Zeroable for &u32 {}   // WOULD BE UNSOUND — null ref is UB
```

**Rationale**: The `unsafe` keyword on a trait says "misusing this trait — by implementing it for a type that doesn't satisfy the contract — causes UB in generic code that relies on the guarantee". `Send`/`Sync` are auto-derived for types whose fields are all `Send`/`Sync`; adding `unsafe impl` manually is a commitment that the auto-derive would have been wrong (usually because you hold raw pointers and know the access pattern is safe).

**See also**: US-03, US-21

---

## US-17: Variance, `PhantomData`, and Drop Check

**Strength**: SHOULD

**Summary**: Raw pointers let you forget lifetimes and type parameters — `PhantomData<T>` tells the compiler which variance to apply and whether `T` may be dropped when your type is dropped.

```rust
use std::marker::PhantomData;

// Shared-reference semantics: covariant in 'a and T, no drop responsibility
pub struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
    _marker: PhantomData<&'a T>,
}

// Owning wrapper: covariant in T, dropck knows T may be dropped
pub struct MyBox<T> {
    ptr: std::ptr::NonNull<T>,
    _owned: PhantomData<T>,          // "I own a T and will drop it"
}

// Invariant tag — type-level distinction without runtime cost
pub struct Id<Tag> {
    raw: u64,
    _tag: PhantomData<fn(Tag) -> Tag>,   // invariant in Tag
}

// Drop check relaxation via #[may_dangle] (nightly-style; Box/Vec use this)
// #[may_dangle] says "I don't touch T's fields during Drop", allowing the
// containee to hold dangling references at drop time. Requires PhantomData<T>
// so the compiler still tracks ownership for exchange/swap.
```

Variance cheat sheet — which marker to use:

| Marker                          | Variance in `T`               | Use                          |
|---------------------------------|-------------------------------|------------------------------|
| `PhantomData<T>`                | covariant, owns `T`           | `MyBox<T>`, `Vec<T>`         |
| `PhantomData<&'a T>`            | covariant in `T` and `'a`     | shared-reference wrappers    |
| `PhantomData<&'a mut T>`        | invariant in `T`, covariant `'a` | mutable-reference wrappers |
| `PhantomData<fn(T)>`            | contravariant in `T`          | callback/function-arg semantics |
| `PhantomData<fn() -> T>`        | covariant in `T`              | function-return semantics    |
| `PhantomData<fn(T) -> T>`       | invariant in `T`              | exchange-proof type tags     |
| `PhantomData<*mut T>`           | invariant in `T`              | interior-mutable raw handle  |

**Rationale**: Without `PhantomData`, unused type and lifetime parameters are compile errors and the compiler cannot compute correct variance. The wrong variance either rejects valid code or admits unsound coercions (e.g., covariant mutable references). When in doubt, pick invariant — `PhantomData<fn(T) -> T>` is almost always safe.

**See also**: TD-17, TD-18, nomicon "Subtyping and Variance"

---

## US-18: Ownership-Based Resource Management (OBRM)

**Strength**: MUST

**Summary**: Tie every resource — memory, file descriptors, mutex guards, FFI handles — to a Rust value with `Drop`. When the value is dropped, the resource is released. No leaks on the success path; bounded leaks on panic.

```rust
use std::os::raw::c_void;

extern "C" {
    fn lib_create() -> *mut c_void;
    fn lib_destroy(h: *mut c_void);
    fn lib_process(h: *mut c_void, v: i32) -> i32;
}

pub struct Handle {
    raw: *mut c_void,
}

impl Handle {
    pub fn new() -> Option<Self> {
        // SAFETY: lib_create returns a valid handle or null.
        let raw = unsafe { lib_create() };
        if raw.is_null() { None } else { Some(Self { raw }) }
    }

    pub fn process(&mut self, v: i32) -> i32 {
        // SAFETY: self.raw is a non-null handle from lib_create, not yet destroyed.
        unsafe { lib_process(self.raw, v) }
    }
}

impl Drop for Handle {
    fn drop(&mut self) {
        // SAFETY: self.raw is non-null and was produced by lib_create.
        unsafe { lib_destroy(self.raw) }
    }
}

// `mem::forget(handle)` is SAFE in Rust — it leaks the resource but doesn't
// cause UB. Unsafe code must not rely on Drop running.
```

Leak amplification is a real concern for types like `Rc`/`Arc` cycles and for `mem::forget` on guard types:

```rust
// `Vec::drain` returns an iterator with a Drop that shrinks the Vec.
// mem::forget on that iterator can leave the Vec in a logically-inconsistent
// but still sound state (old elements still there). Unsafe code must tolerate
// this ("leak amplification") — never assume Drop ran.
```

**Rationale**: OBRM is Rust's answer to try/finally, Go's defer, and C++'s RAII. It composes with unsafe code because `Drop` is called deterministically as values go out of scope. The caveat: `mem::forget`, `Rc` cycles, and `Box::leak` can skip `Drop` — unsafe invariants must be maintained at construction and use time, not relied on being re-established in `Drop`.

**See also**: US-13, US-20

---

## US-19: Declaring `extern` Blocks and Exporting Rust Functions

**Strength**: MUST

**Summary**: `extern "ABI"` blocks declare foreign functions; `extern "ABI" fn` with `#[no_mangle]` exports Rust functions. All types across the boundary must be FFI-safe. Since Edition 2024, `unsafe extern` is required.

```rust
use std::os::raw::{c_char, c_int, c_void};

// ✅ FFI-safe primitives from std::os::raw or core::ffi
unsafe extern "C" {
    fn compute(input: c_int) -> c_int;
    fn write_buf(ptr: *const u8, len: usize) -> isize;
    fn puts(s: *const c_char) -> c_int;
    fn printf(fmt: *const c_char, ...) -> c_int;       // variadic
}

// ✅ Opaque C type — zero-sized marker struct, only accessed via *mut
#[repr(C)]
pub struct Opaque { _private: [u8; 0] }

unsafe extern "C" {
    fn opaque_create() -> *mut Opaque;
    fn opaque_destroy(h: *mut Opaque);
}

// ✅ FFI-safe struct
#[repr(C)]
pub struct Point { pub x: f64, pub y: f64 }

// ✅ Exporting a Rust function to C
#[no_mangle]
pub extern "C" fn rust_add(a: c_int, b: c_int) -> c_int {
    a.wrapping_add(b)
}

// ❌ BAD: passing Rust types across FFI without repr(C)
pub struct BadConfig { timeout: u64, retries: u32 }   // layout is undefined
// extern "C" { fn configure(cfg: BadConfig); }        // UB

// ❌ BAD: Rust generics/lifetimes don't cross the boundary
// extern "C" { fn with_slice(s: &[u8]); }   // wide pointer is not C-ABI
```

FFI-safe types (no `#[repr(C)]` needed for the built-ins):

- `bool`, integer types (`i8`..=`i64`, `u8`..=`u64`, `isize`, `usize`), `f32`, `f64`
- Raw pointers: `*const T`, `*mut T`
- Function pointers: `extern "C" fn(...) -> ...`
- `Option<&T>` and `Option<NonNull<T>>` are FFI-safe (nullable-pointer optimization)
- Any type marked `#[repr(C)]`, `#[repr(transparent)]`, or (for enums) `#[repr(uN)]`/`#[repr(iN)]`

**Rationale**: C doesn't know about Rust's ownership, lifetimes, or `Vec`/`String`/`&[T]` layouts. You must pick an explicit representation. The `unsafe extern` syntax (Edition 2024) makes the unsafety of declaring external function signatures explicit — the declaration is itself a claim about what the other side expects.

**See also**: US-06, US-20, US-23

---

## US-20: Don't Unwind Across FFI Boundaries

**Strength**: MUST

**Summary**: A panic unwinding through `extern "C"` is UB. Catch panics at the boundary with `std::panic::catch_unwind`, or use `extern "C-unwind"` if the other side is Rust/Itanium-EH compatible.

```rust
use std::panic::{catch_unwind, AssertUnwindSafe};
use std::os::raw::c_int;

const OK: c_int = 0;
const ERR_PANIC: c_int = -99;
const ERR_BAD_ARG: c_int = -1;

// ❌ BAD: panic crosses C ABI — undefined behavior
#[no_mangle]
pub extern "C" fn rust_bad(n: c_int) -> c_int {
    assert!(n >= 0);             // panic on n < 0 is UB here
    n * 2
}

// ✅ GOOD: catch_unwind at the boundary
#[no_mangle]
pub extern "C" fn rust_safe(n: c_int) -> c_int {
    let result = catch_unwind(AssertUnwindSafe(|| {
        if n < 0 { return Err(ERR_BAD_ARG); }
        Ok(n * 2)
    }));
    match result {
        Ok(Ok(v))  => v,
        Ok(Err(e)) => e,
        Err(_panic) => ERR_PANIC,
    }
}

// ✅ Alternative: panic = "abort" in Cargo.toml — no unwinding at all.
// [profile.release]
// panic = "abort"

// ✅ If the caller is Rust (or supports Itanium C++ EH), use "C-unwind"
#[no_mangle]
pub extern "C-unwind" fn rust_may_unwind() {
    panic!("this is fine — caller opted into unwinding");
}
```

`catch_unwind` only catches unwinding panics — with `panic = "abort"`, the whole process terminates, which is safe across FFI but may be surprising. Pick one strategy per crate.

**Rationale**: The C ABI has no concept of stack unwinding. A Rust panic crossing into C corrupts the stack and skips C++ destructors. `catch_unwind` converts the panic into a normal return at the Rust side; `extern "C-unwind"` is the explicit opt-in for when both sides agree.

**See also**: US-13, US-19

---

## US-21: FFI String Conversions

**Strength**: MUST

**Summary**: Rust `&str`/`String` are not null-terminated; C strings are. Use `CString` to pass Rust strings to C; `CStr::from_ptr` to borrow incoming strings; check for null; be explicit about ownership transfer.

```rust
use std::ffi::{CStr, CString};
use std::os::raw::c_char;

unsafe extern "C" {
    fn puts(s: *const c_char) -> i32;
    fn c_store(s: *const c_char);           // C holds onto the pointer
    fn c_return_string() -> *mut c_char;    // C allocates; we must free
    fn free_c_string(p: *mut c_char);
}

// ✅ Short-lived pass to C — keep the CString alive for the call
pub fn print_line(s: &str) -> std::io::Result<()> {
    let cstr = CString::new(s)
        .map_err(|_| std::io::Error::other("embedded null"))?;
    // SAFETY: cstr.as_ptr() is a valid NUL-terminated C string; lives until
    // end of statement where `puts` returns.
    unsafe { puts(cstr.as_ptr()); }
    Ok(())
}

// ❌ BAD: dangling pointer — CString drops at end of expression
pub fn bad(s: &str) {
    unsafe { puts(CString::new(s).unwrap().as_ptr()); }
    //                                   ^^^^^^^^^^^ dangles after `;`
}

// ✅ Receive a C string — caller guarantees NUL-termination
/// # Safety
/// `p` must be non-null and point to a NUL-terminated sequence.
pub unsafe fn from_c(p: *const c_char) -> String {
    // SAFETY: forwarded from the caller.
    let cstr = unsafe { CStr::from_ptr(p) };
    cstr.to_string_lossy().into_owned()
}

// ✅ Transfer ownership TO C (C frees with free_c_string presumably)
pub fn hand_off(s: String) {
    let cstr = CString::new(s).unwrap();
    let raw = cstr.into_raw();              // leak intentionally
    // SAFETY: we handed the allocation to C; we must not touch it again.
    unsafe { c_store(raw); }
}

// ✅ Reclaim ownership FROM C (must be a pointer we originally gave out)
pub fn take_back(raw: *mut c_char) -> String {
    // SAFETY: raw was produced by CString::into_raw() above; not freed since.
    let cstr = unsafe { CString::from_raw(raw) };
    cstr.into_string().unwrap_or_default()
}
```

**Rationale**: `CString::new` allocates a NUL-terminated buffer; `.as_ptr()` borrows it. Drop ordering matters — the `CString` must outlive the FFI call. `into_raw`/`from_raw` make ownership transfer explicit and pair the two sides of the allocation.

**See also**: US-18, US-19, US-24

---

## US-22: Error Propagation Across FFI

**Strength**: SHOULD

**Summary**: Translate Rust `Result` to integer codes (or out-parameters) at the boundary. Use a thread-local for detailed last-error messages. Keep the exported function signatures tight.

```rust
use std::cell::RefCell;
use std::os::raw::c_int;

const OK: c_int = 0;
const ERR_INVALID: c_int = -1;
const ERR_IO: c_int = -2;
const ERR_PANIC: c_int = -99;

#[derive(Debug)]
enum Error {
    Invalid(&'static str),
    Io(std::io::Error),
}

impl Error {
    fn code(&self) -> c_int {
        match self {
            Error::Invalid(_) => ERR_INVALID,
            Error::Io(_) => ERR_IO,
        }
    }
}

thread_local! {
    static LAST_ERROR: RefCell<Option<Error>> = RefCell::new(None);
}

fn record(err: Error) {
    LAST_ERROR.with(|slot| *slot.borrow_mut() = Some(err));
}

// ✅ Main entry: integer code, detail available via get_last_error_message
#[no_mangle]
pub extern "C" fn my_op(n: c_int) -> c_int {
    match std::panic::catch_unwind(|| do_op(n)) {
        Ok(Ok(())) => OK,
        Ok(Err(e)) => { let code = e.code(); record(e); code }
        Err(_) => ERR_PANIC,
    }
}

fn do_op(n: c_int) -> Result<(), Error> {
    if n < 0 { return Err(Error::Invalid("negative input")); }
    Ok(())
}

// ✅ Allow the caller to fetch the most recent error as a C string
#[no_mangle]
pub extern "C" fn my_last_error_message(
    out: *mut u8, out_len: usize,
) -> c_int {
    LAST_ERROR.with(|slot| {
        let Some(err) = slot.borrow().as_ref().map(|e| format!("{e:?}")) else {
            return 0;
        };
        let bytes = err.as_bytes();
        let n = bytes.len().min(out_len.saturating_sub(1));
        // SAFETY: caller guarantees `out` is valid for `out_len` writes.
        unsafe {
            std::ptr::copy_nonoverlapping(bytes.as_ptr(), out, n);
            *out.add(n) = 0;                 // NUL terminator
        }
        n as c_int
    })
}
```

**Rationale**: C programs expect error codes, not panics. Keeping the detail on the Rust side (thread-local, opaque handle, or out-parameter) lets you present rich errors without blowing up the C ABI. The `errno` pattern — integer + thread-local detail — is widely understood.

**See also**: US-20, US-24

---

## US-23: Object-Based FFI APIs

**Strength**: SHOULD

**Summary**: When exposing a non-trivial Rust type to C, pass opaque handles (`*mut Handle`) produced by a `create` function and released by a `destroy` function. Never expose the struct's layout.

```rust
use std::os::raw::c_int;

// Internal type — full Rust, non-FFI-safe layout
pub struct Database { /* Vec<Row>, HashMap, ... */ }

impl Database {
    pub fn open(_path: &str) -> Result<Self, std::io::Error> {
        Ok(Self {})
    }
    pub fn insert(&mut self, _row: &[u8]) -> Result<(), std::io::Error> {
        Ok(())
    }
}

// ✅ FFI wrappers — caller holds a *mut Database, never sees fields
#[no_mangle]
pub extern "C" fn db_open(path: *const u8, len: usize) -> *mut Database {
    if path.is_null() { return std::ptr::null_mut(); }
    // SAFETY: caller guarantees path/len describe a valid UTF-8 slice.
    let slice = unsafe { std::slice::from_raw_parts(path, len) };
    let Ok(s) = std::str::from_utf8(slice) else { return std::ptr::null_mut(); };
    match Database::open(s) {
        Ok(db) => Box::into_raw(Box::new(db)),
        Err(_) => std::ptr::null_mut(),
    }
}

#[no_mangle]
pub extern "C" fn db_insert(
    db: *mut Database, row: *const u8, len: usize,
) -> c_int {
    if db.is_null() || row.is_null() { return -1; }
    // SAFETY: db was produced by db_open and not destroyed; caller guarantees
    // row/len describe a valid byte buffer.
    let db = unsafe { &mut *db };
    let slice = unsafe { std::slice::from_raw_parts(row, len) };
    match db.insert(slice) { Ok(()) => 0, Err(_) => -1 }
}

#[no_mangle]
pub extern "C" fn db_close(db: *mut Database) {
    if db.is_null() { return; }
    // SAFETY: db came from Box::into_raw in db_open; this retakes ownership.
    unsafe { drop(Box::from_raw(db)); }
}
```

**Rationale**: Opaque handles hide the Rust layout, let the struct grow fields across versions, and keep unsafety contained in a handful of wrapper functions. This is how databases, ML runtimes, and crypto libraries expose themselves to C, Python, Swift, and so on.

**See also**: US-18, US-24

---

## US-24: Isolate DLL State and Consolidate FFI Types

**Strength**: MUST

**Summary**: When multiple Rust shared libraries load into the same process, only share `repr(C)`-compatible, stateless types between them. Consolidate FFI types in a single crate so every consumer agrees on the layout.

```rust
// ❌ BAD: sharing a Rust-layout Vec across two dynamic libraries
pub struct Message { items: Vec<u8> }    // Vec layout depends on stdlib version

#[no_mangle]
pub extern "C" fn send(msg: Message) { /* UB if crates disagree */ }

// ✅ GOOD: FFI-safe wire format
#[repr(C)]
pub struct MessageC {
    ptr: *const u8,
    len: usize,
}

#[no_mangle]
pub extern "C" fn send_c(msg: MessageC) {
    // SAFETY: caller owns the bytes for the duration of the call.
    let _data = unsafe { std::slice::from_raw_parts(msg.ptr, msg.len) };
}

// ✅ GOOD: single `my-crate-types` crate that every consumer depends on
// shared-types/src/lib.rs:
// #[repr(C)]
// pub struct Message { pub ptr: *const u8, pub len: usize }
//
// producer-lib/Cargo.toml: my-crate-types = "1"
// consumer-lib/Cargo.toml: my-crate-types = "1"
// Both see the same layout; one semver break changes it everywhere.
```

**Rationale**: Rust does not guarantee ABI stability across compiler versions, stdlib versions, or even between builds of the same code with different features. Two DLLs built independently cannot safely exchange `Vec<T>` or `String`. Consolidating FFI types in a versioned shared crate forces every consumer to agree on a single layout.

**See also**: M-ISOLATE-DLL-STATE, US-06, US-19

---

## US-25: Provide Native Escape Hatches (`from_raw`, `into_raw`, `as_raw`)

**Strength**: SHOULD

**Summary**: A type wrapping a native handle should expose `unsafe fn from_raw`, `fn into_raw`, and `fn as_raw` so users can interoperate with other libraries speaking the same native API.

```rust
use std::os::raw::c_void;

pub struct Handle(*mut c_void);

impl Handle {
    /// Safely create a handle through the high-level API.
    pub fn new() -> Result<Self, Error> { todo!() }

    /// Wrap an existing raw handle obtained from the native library.
    ///
    /// # Safety
    ///
    /// - `raw` must be a valid, still-open handle from the native API
    /// - After calling, the caller must not use `raw` directly anywhere else
    pub unsafe fn from_raw(raw: *mut c_void) -> Self { Self(raw) }

    /// Consume this wrapper and return the raw handle. The caller is now
    /// responsible for closing it (drop is suppressed via `mem::forget`).
    pub fn into_raw(self) -> *mut c_void {
        let raw = self.0;
        std::mem::forget(self);
        raw
    }

    /// Borrow the raw handle without taking ownership.
    pub fn as_raw(&self) -> *mut c_void { self.0 }
}

impl Drop for Handle {
    fn drop(&mut self) {
        // SAFETY: Handle invariant — self.0 is a valid handle we own.
        unsafe { /* native_close(self.0) */ }
    }
}

pub struct Error;
```

**Rationale**: Without escape hatches, your wrapper becomes a silo — users can't pass your handles to other libraries that speak the same native API (Windows `HANDLE`, POSIX fd, `sqlite3*`, OpenGL textures, etc.). The `from_raw`/`into_raw`/`as_raw` triad is the idiomatic way to interoperate: unsafe where ownership changes, safe for borrowing.

**See also**: M-ESCAPE-HATCHES, US-18, US-23

---

## US-26: Arc-Like Reference Counting — A Worked Case Study

**Strength**: CONSIDER

**Summary**: Reference-counted smart pointers illustrate every concern at once: `NonNull` for niche, `PhantomData` for drop check, atomic ordering for clone/drop, and the fence that makes `Drop` observe writes from the final `Release` decrement.

```rust
use std::marker::PhantomData;
use std::ptr::NonNull;
use std::sync::atomic::{AtomicUsize, Ordering, fence};

struct ArcInner<T> {
    count: AtomicUsize,
    data: T,
}

pub struct MyArc<T> {
    ptr: NonNull<ArcInner<T>>,
    _owned: PhantomData<ArcInner<T>>,
}

// SAFETY: MyArc is Send/Sync iff T is Sync (shared data crosses threads).
unsafe impl<T: Sync + Send> Send for MyArc<T> {}
unsafe impl<T: Sync + Send> Sync for MyArc<T> {}

impl<T> MyArc<T> {
    pub fn new(data: T) -> Self {
        let boxed = Box::new(ArcInner { count: AtomicUsize::new(1), data });
        Self {
            ptr: NonNull::from(Box::leak(boxed)),
            _owned: PhantomData,
        }
    }

    fn inner(&self) -> &ArcInner<T> {
        // SAFETY: self.ptr is valid for the lifetime of every live MyArc.
        unsafe { self.ptr.as_ref() }
    }
}

impl<T> Clone for MyArc<T> {
    fn clone(&self) -> Self {
        // Relaxed: we only need atomicity, not ordering — nobody else reads
        // the count to decide visibility.
        let old = self.inner().count.fetch_add(1, Ordering::Relaxed);
        assert!(old < isize::MAX as usize, "ref count overflow");
        Self { ptr: self.ptr, _owned: PhantomData }
    }
}

impl<T> Drop for MyArc<T> {
    fn drop(&mut self) {
        // Release: synchronizes the data writes we did into ArcInner with
        // the thread that observes count == 0.
        if self.inner().count.fetch_sub(1, Ordering::Release) != 1 {
            return;
        }
        // Acquire fence: pairs with the final Release above so this thread
        // sees every write that happened-before the last decrement.
        fence(Ordering::Acquire);
        // SAFETY: count reached 0, so we are the last owner; reclaim the box.
        unsafe { drop(Box::from_raw(self.ptr.as_ptr())); }
    }
}

impl<T> std::ops::Deref for MyArc<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.inner().data }
}
```

**Rationale**: Reference counting looks simple but is easy to get wrong. The ordering pattern — `Relaxed` for clone, `Release` for drop, `Acquire` fence before reclamation — is the minimum required for correctness on weakly-ordered architectures (ARM, PowerPC). Miri and `loom` test this style of code; both are essential.

**See also**: US-10, US-27, nomicon "Implementing Arc and Mutex"

---

## US-27: Atomics, Data Races, and Race Conditions

**Strength**: SHOULD

**Summary**: A data race (unsynchronized write and read/write to the same location) is UB. A race condition (logically wrong ordering of well-synchronized operations) is a correctness bug but not UB. Pick atomic orderings deliberately; default to `SeqCst` when you're unsure.

```rust
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::thread;

// ❌ DATA RACE → UB
// let mut x = 0u32;
// let p = &x as *const u32 as *mut u32;
// thread::spawn(move || unsafe { *p = 1 });
// let _ = x;         // reading while another thread writes — UB

// ✅ Synchronized via atomic — well-defined
let counter = std::sync::Arc::new(AtomicUsize::new(0));
let handles: Vec<_> = (0..4).map(|_| {
    let c = counter.clone();
    thread::spawn(move || {
        for _ in 0..1000 { c.fetch_add(1, Ordering::Relaxed); }
    })
}).collect();
for h in handles { h.join().unwrap(); }
assert_eq!(counter.load(Ordering::SeqCst), 4000);

// ✅ Release/Acquire — classic flag-and-data handoff
static READY: AtomicBool = AtomicBool::new(false);
static mut DATA: u64 = 0;

fn producer() {
    // SAFETY: only the producer writes DATA, and only before the Release
    // store signals readiness.
    unsafe { DATA = 42; }
    READY.store(true, Ordering::Release);    // publishes DATA
}

fn consumer() {
    while !READY.load(Ordering::Acquire) {   // observes DATA once Acquire sees true
        std::hint::spin_loop();
    }
    // SAFETY: READY == true and Acquire synchronizes with the Release above.
    unsafe { assert_eq!(DATA, 42); }
}
```

Ordering cheatsheet:

- **Relaxed**: atomicity only — use for counters where ordering doesn't matter.
- **Release (store) / Acquire (load)**: one-to-one handoff; everything before the Release is visible after the paired Acquire.
- **AcqRel**: `fetch_*` operations that both observe a previous value and publish a new one.
- **SeqCst**: a single global total order across all `SeqCst` operations. Slower, simpler to reason about.

**Rationale**: C/C++/Rust share the same memory model. On x86, Acquire/Release is free; on ARM/POWER it's not. Writing `Relaxed` everywhere is a common bug — the counter still counts, but the surrounding code may reorder in ways that break higher-level invariants. Tools: Miri (single-threaded UB) and `loom` (multi-thread interleavings).

**See also**: US-16, US-26, nomicon "Concurrency"

---

## US-28: Vec-Like Container — Capacity, Growth, and ZSTs

**Strength**: CONSIDER

**Summary**: A hand-rolled `Vec` illustrates `NonNull::dangling` for the zero-cap case, `ptr::write`/`ptr::read` for moves, the `isize::MAX` allocation limit, and ZST-aware growth.

```rust
use std::alloc::{alloc, dealloc, realloc, handle_alloc_error, Layout};
use std::marker::PhantomData;
use std::mem;
use std::ptr::{self, NonNull};

pub struct MyVec<T> {
    ptr: NonNull<T>,
    cap: usize,
    len: usize,
    _marker: PhantomData<T>,
}

// SAFETY: MyVec owns a T-allocation and behaves like Vec<T>.
unsafe impl<T: Send> Send for MyVec<T> {}
unsafe impl<T: Sync> Sync for MyVec<T> {}

impl<T> MyVec<T> {
    pub fn new() -> Self {
        assert!(mem::size_of::<T>() != 0 || cfg!(feature = "zst_support"),
                "ZST support omitted for brevity");
        // dangling() gives a well-aligned non-null pointer that we must not
        // dereference (cap == 0 → nothing to dereference).
        Self {
            ptr: NonNull::dangling(),
            cap: 0,
            len: 0,
            _marker: PhantomData,
        }
    }

    fn grow(&mut self) {
        let (new_cap, new_layout) = if self.cap == 0 {
            (1, Layout::array::<T>(1).unwrap())
        } else {
            let new_cap = self.cap * 2;
            let new_layout = Layout::array::<T>(new_cap).unwrap();
            // Per nomicon: total allocation must be <= isize::MAX bytes.
            assert!(new_layout.size() <= isize::MAX as usize, "allocation too large");
            (new_cap, new_layout)
        };

        let new_ptr = if self.cap == 0 {
            // SAFETY: new_layout is non-zero size.
            unsafe { alloc(new_layout) }
        } else {
            let old_layout = Layout::array::<T>(self.cap).unwrap();
            // SAFETY: self.ptr came from alloc(old_layout); new_layout same align.
            unsafe { realloc(self.ptr.as_ptr().cast(), old_layout, new_layout.size()) }
        };

        self.ptr = NonNull::new(new_ptr.cast())
            .unwrap_or_else(|| handle_alloc_error(new_layout));
        self.cap = new_cap;
    }

    pub fn push(&mut self, item: T) {
        if self.len == self.cap { self.grow(); }
        // SAFETY: self.ptr.add(self.len) is in-bounds after grow().
        unsafe { ptr::write(self.ptr.as_ptr().add(self.len), item); }
        self.len += 1;
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.len == 0 { return None; }
        self.len -= 1;
        // SAFETY: self.len points at an initialized slot; we decrement first
        // so the logical length excludes the slot we read from.
        Some(unsafe { ptr::read(self.ptr.as_ptr().add(self.len)) })
    }
}

impl<T> Drop for MyVec<T> {
    fn drop(&mut self) {
        while self.pop().is_some() {}   // drop each element in place
        if self.cap != 0 {
            let layout = Layout::array::<T>(self.cap).unwrap();
            // SAFETY: self.ptr came from alloc/realloc with this layout.
            unsafe { dealloc(self.ptr.as_ptr().cast(), layout); }
        }
    }
}
```

Take-aways the nomicon hammers on:

- `NonNull::dangling()` lets you hold "no allocation yet" without a null check on every access — combine with `cap == 0` gate.
- `isize::MAX` (not `usize::MAX`) is the maximum allocation size. Exceeding it is UB.
- `ptr::write` / `ptr::read` move in and out of the buffer without running `drop` on uninitialized slots.
- ZSTs (`size_of::<T>() == 0`) need special handling: allocate nothing, and `ptr.add(n)` is a no-op at the address level.

**See also**: US-07, US-10, US-11, nomicon "Implementing Vec"

---

## US-29: `no_std` and the Runtime Contract

**Strength**: CONSIDER

**Summary**: `no_std` crates replace `std` with `core` plus optional `alloc`. The binary must provide a `#[panic_handler]`, and — on unwinding targets — an `eh_personality` lang item. Pick `panic = "abort"` unless you genuinely need unwinding.

```rust
// lib.rs
#![no_std]

extern crate alloc;                  // opt in to Box/Vec/String via a global allocator

use alloc::vec::Vec;

pub fn collect(iter: impl Iterator<Item = u8>) -> Vec<u8> {
    iter.collect()
}

// In a binary crate (#![no_main] or custom entrypoint) you also need:
#[cfg(not(test))]
#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    loop {}                          // or `cortex_m::asm::udf()`, etc.
}

// With panic = "abort" in Cargo.toml (profile.release.panic = "abort"),
// eh_personality is not required. Without it, you may need:
// #[lang = "eh_personality"] extern fn eh_personality() {}
```

Cargo.toml hints:

```toml
[profile.release]
panic = "abort"        # avoid needing eh_personality and unwinding

[dependencies]
# For production no_std panic handlers, pick one of:
# panic-halt  = "0.2"     # loop {}
# panic-abort = "0.3"     # core::intrinsics::abort()
# panic-probe = "0.3"     # forwards to defmt / RTT
```

`alloc` vs no allocator:

- `#![no_std]` alone: `core` only, no heap. `Box`, `Vec`, `String` unavailable.
- `#![no_std]` + `extern crate alloc`: requires a `#[global_allocator]` somewhere in the binary.
- `extern crate alloc` + `#[global_allocator]` = `linked_list_allocator`, `embedded-alloc`, etc.

**Rationale**: Embedded, kernel, and WASM targets don't have `std` — there's no file system, thread library, or process model. `no_std` lets the same crate compile for both environments. The runtime contract — panic handler, allocator if you use `alloc`, and EH personality if you unwind — has to come from the final binary.

**See also**: US-13, US-20

---

## US-30: Inline Assembly with `asm!`

**Strength**: CONSIDER

**Summary**: Use `asm!` for intrinsics the compiler doesn't expose, CPU-feature flags, context switches, and hot loops. Every operand and clobbered register must be declared. All `asm!` blocks are `unsafe`.

```rust
use core::arch::asm;

// Multiply by 6 on x86-64 with explicit operand classes
pub fn mul6(x: u64) -> u64 {
    let mut x = x;
    unsafe {
        // SAFETY: the template respects its declared operands; no memory/flag
        // access beyond what's stated; we restore all non-output registers.
        asm!(
            "mov {tmp}, {x}",
            "shl {tmp}, 1",
            "shl {x}, 2",
            "add {x}, {tmp}",
            x = inout(reg) x,
            tmp = out(reg) _,
            options(pure, nomem, preserves_flags),  // pure + no memory side effects
        );
    }
    x
}

// Calling a C function from asm with clobber_abi
extern "C" fn helper() -> i32 { 17 }

pub fn call_helper() -> i32 {
    let r: i32;
    unsafe {
        // SAFETY: clobber_abi("C") declares that all caller-saved registers
        // of the C ABI may be clobbered; output register is explicit.
        asm!(
            "call {f}",
            f = sym helper,
            out("rax") r,
            clobber_abi("C"),
        );
    }
    r
}

// ❌ BAD: forgetting to declare a clobbered register
// asm!("mov rbx, 1");          // rbx is callee-saved in SysV — UB without clobber
```

Operand types, options, and rules:

- Operand kinds: `in`, `out`, `lateout`, `inout`, `inlateout`, `sym`, `const`, `label { ... }`.
- Options: `pure`, `nomem`, `readonly`, `preserves_flags`, `noreturn`, `nostack`, `att_syntax`, `raw`.
- `pure` requires `nomem` or `readonly` and at least one non-discarded output.
- Every non-output register must be restored to its entry value — use `clobber_abi("C")` for shortcut on function calls.
- Adjacent `asm!` blocks make no guarantee about adjacency in the output — each is its own atomic unit.

`global_asm!` places code outside any function (boot vectors, interrupt tables). `naked_asm!` is the entire body of a `#[naked]` function — only `sym` and `const` operands are allowed.

**Rationale**: Inline assembly is the escape hatch for instructions Rust has no intrinsic for (CPU-feature probes, system call instructions like `syscall`/`sysenter`/`svc`, ring transitions, atomic primitives on niche targets). Since the compiler cannot see inside the template, the operand declarations are the only information it has about what registers and memory you touch.

**See also**: US-19, US-29, reference "Inline Assembly"

---

## US-31: Test Unsafe Code with Miri and `loom`

**Strength**: SHOULD

**Summary**: Miri catches undefined behavior in single-threaded execution (aliasing, uninitialized reads, OOB, UB transmutes). `loom` exhaustively explores thread interleavings for atomics and synchronization.

```rust
// #[cfg(miri)] gates allow skipping tests that hit unsupported FFI,
// very long runtimes, or known-limitations features.
#[test]
fn pop_from_empty_is_none() {
    let mut v: MyVec<u32> = MyVec::new();
    assert!(v.pop().is_none());
}

#[cfg(not(miri))]       // FFI not supported under Miri
#[test]
fn ffi_roundtrip() { /* ... */ }

// Run: cargo +nightly miri test

// loom test — explores all thread schedulings of a Release/Acquire pair
#[cfg(loom)]
#[test]
fn atomic_handshake() {
    use loom::sync::atomic::{AtomicBool, Ordering};
    use loom::thread;
    loom::model(|| {
        static READY: AtomicBool = AtomicBool::new(false);
        static mut DATA: u32 = 0;
        let t = thread::spawn(|| {
            // SAFETY: only producer writes DATA before Release.
            unsafe { DATA = 1; }
            READY.store(true, Ordering::Release);
        });
        while !READY.load(Ordering::Acquire) {}
        // SAFETY: Acquire pairs with Release; DATA is stable.
        unsafe { assert_eq!(DATA, 1); }
        t.join().unwrap();
    });
}
```

**Rationale**: Miri is essentially a Rust interpreter that tracks provenance, uninitialized memory, and aliasing (Stacked Borrows / Tree Borrows) in real time — it's the standard tool for validating unsafe code. `loom` complements it by simulating every legal memory-model interleaving for multi-threaded code. Both are cheap to add to CI and catch classes of bugs that sanitizers miss.

**See also**: US-09, US-26, US-27

---

## US-32: Prefer Safe Abstractions — `bytemuck`, `zerocopy`, `pin-project`

**Strength**: SHOULD

**Summary**: Before writing your own `unsafe`, check whether an audited crate already provides it safely.

```rust
// ✅ bytemuck: safe transmutation for Pod types
use bytemuck::{Pod, Zeroable, cast_slice};

#[derive(Copy, Clone, Pod, Zeroable)]
#[repr(C)]
struct Pixel { r: u8, g: u8, b: u8, a: u8 }

let pixels: &[Pixel] = &[Pixel { r: 0, g: 0, b: 0, a: 255 }; 10];
let bytes: &[u8] = cast_slice(pixels);   // no unsafe, checked at compile time

// ✅ zerocopy: safe slice-of-bytes → slice-of-T and vice versa with validation
// ✅ pin-project: derive safe pinned field access without writing unsafe yourself

// Other useful ones in the same vein:
// - crossbeam: lock-free data structures reviewed by concurrency specialists
// - parking_lot: faster Mutex / RwLock than std, well-tested unsafe
// - memoffset: safe offset_of! for computing field offsets in repr(C) structs
```

**Rationale**: The Rust ecosystem has mature crates whose entire job is to encapsulate a slice of unsafe correctly. Reuse beats reinvention — these crates have more review, more tests, more Miri runs, and more fuzz than you can reasonably give your own implementation.

**See also**: US-05, US-18


## Safety Checklist

Before shipping any code containing `unsafe`:

```rust
// 1. Is `unsafe` the only way to express this? (US-04)
//    ✅ Novel abstraction, FFI, proven-hot loop
//    ❌ "Avoiding the borrow checker", "simpler"

// 2. Does every unsafe fn have a `# Safety` section? (US-03)
/// # Safety
/// - precondition 1
/// - precondition 2

// 3. Does every `unsafe { ... }` block have a `// SAFETY:` comment? (US-03, US-12)
unsafe {
    // SAFETY: explain which preconditions from the caller or this module
    //         make this operation sound right here.
}

// 4. Can any safe caller trigger UB through my public API? (US-02)
//    If yes → unsound → fix immediately. No exceptions.

// 5. Are unsafe invariants contained in the smallest possible module? (US-05)

// 6. Does unsafe code survive panics? (US-13)
//    - Guard types that restore invariants in Drop
//    - `mem::forget` is safe — never rely on Drop running
//    - Account for `clone()`, `Debug` impls, user closures panicking

// 7. FFI: any panic caught, any handle owned by a Drop-ing type? (US-18, US-20)

// 8. Layout: `repr(C)` / `repr(transparent)` where crossing FFI? (US-06)

// 9. Tests under Miri (`cargo +nightly miri test`)? (US-31)
//    Tests under `loom` for atomics? (US-27, US-31)

// 10. Could an existing crate (bytemuck, zerocopy, pin-project) replace
//     my hand-rolled unsafe? (US-32)
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| US-01 Unsafe means UB risk, not dangerous | MUST | `unsafe` is the UB contract, not a warning |
| US-02 All code must be sound | MUST | Safe callers can never trigger UB |
| US-03 Document safety and every block | MUST | `# Safety` + `// SAFETY:` everywhere |
| US-04 Three valid reasons for unsafe | MUST | Novel abstraction, performance, FFI |
| US-05 Contain unsafety in small modules | SHOULD | Soundness boundary = module boundary |
| US-06 Choose `repr` deliberately | MUST | `repr(C)`, `repr(transparent)` for FFI |
| US-07 Understand DSTs, ZSTs, empty types | SHOULD | `?Sized`, niche optimization, `!` |
| US-08 Use NonZero* and niche types | SHOULD | `Option<NonZeroU32>` is 4 bytes |
| US-09 Pointer aliasing and provenance | MUST | `&mut` exclusive; no `usize` round-trip |
| US-10 `MaybeUninit` for uninitialized | MUST | `mem::zeroed` is UB for many types |
| US-11 `ptr::write/read/copy` (no drop) | MUST | Assignment drops; raw write does not |
| US-12 Minimize unsafe scope | MUST | One unsafe op per block |
| US-13 Exception safety in unsafe code | MUST | Guard types; unwind can't break invariants |
| US-14 Split borrows with stdlib | SHOULD | `split_at_mut`, `Option::take` |
| US-15 Cast and transmute rules | MUST | `as` truncates; `transmute` requires equal size |
| US-16 Unsafe traits (Send/Sync) | MUST | `unsafe impl` is a correctness claim |
| US-17 Variance and PhantomData | SHOULD | Raw-pointer wrappers need PhantomData |
| US-18 Ownership-based resource mgmt | MUST | Tie resources to `Drop` |
| US-19 `extern` blocks and exports | MUST | `repr(C)` types; no Rust generics |
| US-20 No unwind across FFI | MUST | `catch_unwind` or `panic = "abort"` |
| US-21 FFI string conversions | MUST | `CString` to C; `CStr::from_ptr` from C |
| US-22 Error propagation across FFI | SHOULD | Integer code + thread-local detail |
| US-23 Object-based FFI APIs | SHOULD | Opaque handles + create/destroy |
| US-24 Isolate DLL state and types | MUST | Only FFI-safe types cross DLL edges |
| US-25 Native escape hatches | SHOULD | `from_raw`/`into_raw`/`as_raw` |
| US-26 Arc case study | CONSIDER | Relaxed clone, Release drop, Acquire fence |
| US-27 Atomics, data races, races | SHOULD | Pick ordering deliberately |
| US-28 Vec case study | CONSIDER | `NonNull::dangling`, isize::MAX limit |
| US-29 `no_std` runtime contract | CONSIDER | `#[panic_handler]`, `eh_personality` |
| US-30 Inline assembly | CONSIDER | Declare every operand and clobber |
| US-31 Test with Miri and loom | SHOULD | Single-thread UB + multi-thread orderings |
| US-32 Prefer safe-abstraction crates | SHOULD | bytemuck, zerocopy, pin-project |


## Related Guidelines

- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for how borrowing rules underpin the pointer-aliasing rules exploited here (US-09).
- **Type Design**: See `05-type-design.md` for `repr`, `PhantomData`, variance, `Pin`/`PhantomPinned`, and niche-bearing types (US-06, US-07, US-08, US-17).
- **Concurrency and Async**: See `07-concurrency-async.md` for `Send`/`Sync` design, `Arc`, mutexes, and async ownership — all of which inform the unsafe impls and atomics discussed here (US-16, US-26, US-27).
- **Error Handling**: See `08-error-handling.md` for how `Result` interacts with panic safety at FFI boundaries (US-13, US-20, US-22).
- **Anti-Patterns**: See `11-anti-patterns.md` for the catalog of `unsafe` misuse and unsound patterns to recognize and reject.


## External References

- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) — definitive guide to unsafe Rust
- [The Rust Reference — Unsafety](https://doc.rust-lang.org/reference/unsafety.html)
- [The Rust Reference — Behavior Considered Undefined](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)
- [The Rust Reference — Inline Assembly](https://doc.rust-lang.org/reference/inline-assembly.html)
- [Unsafe Code Guidelines Reference](https://rust-lang.github.io/unsafe-code-guidelines/)
- [Miri](https://github.com/rust-lang/miri) — interpreter that detects UB
- [`loom`](https://github.com/tokio-rs/loom) — permutation testing for concurrent code
- [`bytemuck`](https://docs.rs/bytemuck), [`zerocopy`](https://docs.rs/zerocopy), [`pin-project`](https://docs.rs/pin-project) — audited safe abstractions
- Pragmatic Rust Guidelines: M-UNSAFE-IMPLIES-UB, M-UNSAFE, M-UNSOUND, M-ISOLATE-DLL-STATE, M-ESCAPE-HATCHES
