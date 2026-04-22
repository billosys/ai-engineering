---
concept: Unsafe Rust
slug: rust-unsafe-code
category: unsafe-rust
subcategory: safety-model
tier: advanced
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Advanced Features"
chapter_number: 20
pdf_page: null
section: "Unsafe Rust"
extraction_confidence: high
aliases:
  - "unsafe superpowers"
  - "raw pointers"
  - "unsafe functions"
  - "mutable static variables"
  - "unsafe traits"
  - "FFI"
  - "foreign function interface"
  - "extern functions"
  - "Miri"
prerequisites: []
extends: []
related:
  - rust-unsafety-reference
  - nomicon-overview
contrasts_with: []
answers_questions:
  - "What five operations can you only perform in unsafe Rust?"
  - "Does unsafe disable the borrow checker?"
  - "How do raw pointers differ from references?"
  - "How do you create a safe abstraction over unsafe code?"
  - "How do you call C functions from Rust using extern?"
  - "How do you expose Rust functions to C?"
  - "Why is accessing mutable static variables unsafe?"
  - "What is an unsafe trait and when do you implement one?"
  - "What are union types and why is accessing their fields unsafe?"
  - "How does Miri help verify unsafe code?"
  - "What is the safe keyword in extern blocks?"
---

# Quick Definition

Unsafe Rust is a second language hidden within Rust that grants five additional capabilities (unsafe superpowers) not available in safe Rust: dereferencing raw pointers, calling unsafe functions, accessing/modifying mutable static variables, implementing unsafe traits, and accessing union fields. The `unsafe` keyword marks blocks and items where these operations are permitted. Critically, `unsafe` does not turn off the borrow checker or other safety checks -- it only unlocks these five specific operations. Unsafe code should be wrapped in safe abstractions whenever possible.

# Core Definition

**The five unsafe superpowers:**
1. **Dereference a raw pointer** -- `*const T` (immutable) and `*mut T` (mutable) raw pointers bypass borrowing rules, may be null, may be dangling, and have no automatic cleanup. Creating raw pointers is safe; dereferencing them requires `unsafe`.
2. **Call an unsafe function or method** -- functions marked `unsafe fn` have preconditions the compiler cannot verify. Callers must uphold those preconditions. Within an unsafe function body, unsafe operations still require explicit `unsafe` blocks.
3. **Access or modify a mutable static variable** -- global mutable state (`static mut`) is inherently unsafe because multiple threads could access it concurrently, creating data races. Reading or writing requires `unsafe`. The compiler denies creating references to mutable statics by default.
4. **Implement an unsafe trait** -- a trait is `unsafe` when it has invariants the compiler cannot verify (e.g., `Send`, `Sync`). Implementing it with `unsafe impl` is a promise that the invariants are upheld.
5. **Access fields of a union** -- unions (similar to C unions) store one value at a time but in the space of any variant. Accessing a field is unsafe because Rust cannot guarantee which variant is currently stored.

**Safe abstractions over unsafe code:**
The standard library's `split_at_mut` is the canonical example: the function contains `unsafe` internally (using raw pointers and `slice::from_raw_parts_mut`) but presents a safe API. The unsafe operations are sound because bounds are validated before the raw pointer operations. Wrapping unsafe code in safe functions is the idiomatic approach.

**Foreign Function Interface (FFI):**
- `unsafe extern "C" { fn abs(input: i32) -> i32; }` declares external C functions. The `"C"` specifies the ABI.
- Individual functions in extern blocks can be marked `safe` to indicate they have no memory safety concerns, allowing them to be called without `unsafe`.
- To expose Rust functions to C: `#[unsafe(no_mangle)] pub extern "C" fn call_from_c() { ... }`. The `no_mangle` attribute prevents name mangling.

**Miri** is an official Rust tool for dynamically detecting undefined behavior in unsafe code. Installed via `rustup +nightly component add miri`, run via `cargo +nightly miri run` or `cargo +nightly miri test`. Miri is dynamic (catches problems in executed code paths only), not a complete soundness checker, but extremely valuable for catching UB.

# Prerequisites

Understanding of Rust's ownership, borrowing, and lifetime systems, plus basic knowledge of references and smart pointers.

# Key Properties

1. `unsafe` does NOT disable the borrow checker, type system, or any other safety checks -- it only unlocks the five specific superpowers
2. Raw pointers can be created in safe code; only dereferencing them requires `unsafe`
3. Raw pointers can have both `*const T` and `*mut T` to the same location simultaneously -- unlike references, they are not subject to borrowing rules
4. Raw pointers differ from references in four ways: they can ignore borrowing rules, can be null, can be dangling, and have no automatic cleanup
5. Safe abstractions over unsafe code are the primary pattern: the outer function is safe, internal unsafe operations are bounded and validated
6. Within an `unsafe fn` body, unsafe operations still require explicit `unsafe` blocks (the compiler warns if you forget)
7. Static variables have fixed memory addresses (unlike constants, which may be duplicated); mutable statics are unsafe to access
8. The `safe` keyword in `unsafe extern` blocks lets you mark specific foreign functions as safe to call without an `unsafe` block
9. `#[unsafe(no_mangle)]` is required to export Rust functions with their original names for C interop
10. Miri catches undefined behavior at runtime but cannot guarantee absence of UB in untested code paths

# Construction / Recognition

## To use raw pointers safely:
1. Create raw pointers using raw borrow operators: `&raw const x` or `&raw mut x`
2. Alternatively cast from references: `let p = &x as *const i32;`
3. Validate pointers (bounds, alignment, liveness) before dereferencing
4. Dereference only within `unsafe` blocks: `unsafe { *p }`
5. Wrap the unsafe operations in a safe function with proper validation

## To create a safe abstraction:
1. Validate all preconditions in safe code (bounds checks, null checks)
2. Perform raw pointer operations in a minimal `unsafe` block
3. Do not mark the outer function as `unsafe` -- it is safe by construction
4. Document why the unsafe operations are sound

## To call foreign (C) functions:
1. Declare them in `unsafe extern "C" { ... }`
2. Mark inherently safe functions with `safe` keyword
3. Call unsafe foreign functions within `unsafe` blocks
4. Use `SAFETY` comments to document why the call is correct

# Context & Application

The Unsafe Rust section of Chapter 20 serves as the book's introduction to going beyond the compiler's safety guarantees. It is deliberately structured to emphasize that `unsafe` is a scalpel, not a sledgehammer: only five operations are unlocked, and the rest of Rust's safety machinery remains active.

The chapter teaches the crucial pattern of building safe abstractions over unsafe internals, using `split_at_mut` as its primary example. This pattern is how much of the standard library works: `Vec`, `String`, `HashMap`, and other types use unsafe internally but expose safe APIs.

The FFI section covers both directions (Rust calling C, C calling Rust) and introduces the Edition 2024 requirement that extern blocks be marked `unsafe extern`. The `safe` keyword for individual extern functions is a newer feature that reduces unnecessary `unsafe` blocks.

The chapter also introduces Miri as a practical tool, not just a theoretical concept, with concrete usage instructions and realistic examples of catching undefined behavior.

# Examples

**Example 1** (Ch. 20, "Dereferencing Raw Pointers"):
```rust
let mut num = 5;
let r1 = &raw const num;   // *const i32 -- safe to create
let r2 = &raw mut num;     // *mut i32 -- safe to create
unsafe {
    println!("r1 is: {}", *r1);  // dereferencing requires unsafe
    println!("r2 is: {}", *r2);
}
```

**Example 2** (Ch. 20, "Safe Abstraction over Unsafe"): Implementing `split_at_mut`:
```rust
use std::slice;
fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = values.len();
    let ptr = values.as_mut_ptr();
    assert!(mid <= len);
    unsafe {
        (
            slice::from_raw_parts_mut(ptr, mid),
            slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

**Example 3** (Ch. 20, "FFI with safe marking"):
```rust
unsafe extern "C" {
    safe fn abs(input: i32) -> i32;  // marked safe -- no unsafe block needed
}
fn main() {
    println!("abs(-3) = {}", abs(-3));  // called without unsafe
}
```

**Example 4** (Ch. 20, "Mutable Static Variable"):
```rust
static mut COUNTER: u32 = 0;
/// SAFETY: Must only be called from a single thread.
unsafe fn add_to_count(inc: u32) {
    unsafe { COUNTER += inc; }
}
fn main() {
    unsafe { add_to_count(3); }
    // Accessing COUNTER also requires unsafe
}
```

# Relationships

## Builds Upon
(none -- this is the book's introduction to unsafe concepts)

## Enables
- **rust-advanced-traits-and-types** -- understanding unsafe is needed for unsafe traits like `Send`/`Sync` and for understanding the newtype pattern's zero-cost guarantees

## Related
- **rust-unsafety-reference** -- The Rust Reference's formal specification of undefined behavior and unsafe operations
- **nomicon-overview** -- The Rustonomicon provides deep practical guidance on writing correct unsafe code

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming that `unsafe` turns off all of Rust's safety checks, leading to writing carelessly within `unsafe` blocks.
  **Correction**: `unsafe` only unlocks the five specific superpowers. The borrow checker, type system, and lifetime checks all remain active within `unsafe` blocks.

- **Error**: Using `while let` instead of `let` + `recv()` in a mutex-guarded channel loop (as in Ch 21's thread pool), causing the mutex lock to be held for the entire loop body.
  **Correction**: Use `let job = receiver.lock().unwrap().recv().unwrap();` so the `MutexGuard` is dropped immediately after `recv()`, not held during job execution.

- **Error**: Creating raw pointers to arbitrary addresses and dereferencing them: `let p = 0x012345 as *const i32; unsafe { *p }`.
  **Correction**: Only dereference raw pointers that are known to be valid. Use Miri to detect such undefined behavior.

# Common Confusions

- **Confusion**: Thinking raw pointers are always unsafe to work with.
  **Clarification**: Creating raw pointers is safe. Only dereferencing them (reading/writing through them) requires `unsafe`. You can create, store, and pass around raw pointers in safe code.

- **Confusion**: Believing that `unsafe fn` bodies are automatically unsafe blocks where any unsafe operation is allowed without annotation.
  **Clarification**: As of recent Rust editions, the compiler warns if you perform unsafe operations inside an `unsafe fn` without an explicit `unsafe` block. The `unsafe_op_in_unsafe_fn` lint encourages explicit blocks for clarity.

- **Confusion**: Conflating type aliases (like `type Kilometers = i32`) with newtypes (like `struct Millimeters(u32)`) -- relevant because the safe abstraction discussion references both.
  **Clarification**: Type aliases do NOT create distinct types; values are interchangeable. Newtypes create genuinely new types that prevent accidental mixing and enable orphan-rule workarounds.

# Source Reference

Chapter 20 of The Rust Programming Language, section "Unsafe Rust" (~600 lines). Covers: the five unsafe superpowers, raw pointers (creation vs dereferencing), unsafe functions and safe abstractions (split_at_mut example), extern functions and FFI (unsafe extern, safe keyword, no_mangle, ABI), mutable static variables, unsafe traits (Send/Sync), unions, and Miri for detecting undefined behavior.

# Verification Notes

- Definition source: Directly extracted from Chapter 20 "Unsafe Rust" section of The Rust Programming Language
- Key Properties: All derived from explicit statements and code examples in the source text
- Confidence rationale: HIGH -- authoritative book by the Rust team with comprehensive examples
- Uncertainties: The `safe` keyword in extern blocks and `unsafe extern` requirement are Edition 2024 features that may see refinement
- Cross-reference status: rust-unsafety-reference and nomicon-overview cover the same domain from reference and advanced perspectives respectively
