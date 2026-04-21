r[safety]
# Unsafety

r[safety.intro]
Unsafe operations are those that can potentially violate the memory-safety
guarantees of Rust's static semantics.

r[safety.unsafe-ops]
The following language level features cannot be used in the safe subset of
Rust:

r[safety.unsafe-deref]
- Dereferencing a [raw pointer].

r[safety.unsafe-static]
- Reading or writing a [mutable] or unsafe [external] static variable.

r[safety.unsafe-union-access]
- Accessing a field of a [`union`], other than to assign to it.

r[safety.unsafe-call]
- Calling an unsafe function.

r[safety.unsafe-target-feature-call]
- Calling a safe function marked with a [`target_feature`][attributes.codegen.target_feature] from a function that does not have a `target_feature` attribute enabling the same features (see [attributes.codegen.target_feature.safety-restrictions]).

r[safety.unsafe-impl]
- Implementing an [unsafe trait].

r[safety.unsafe-extern]
- Declaring an [`extern`] block[^extern-2024].

r[safety.unsafe-attribute]
- Applying an [unsafe attribute] to an item.

[^extern-2024]: Prior to the 2024 edition, extern blocks were allowed to be declared without `unsafe`.

[`extern`]: items/external-blocks.md
[`union`]: items/unions.md
[mutable]: items/static-items.md#mutable-statics
[external]: items/external-blocks.md
[raw pointer]: types/pointer.md
[unsafe trait]: items/traits.md#unsafe-traits
[unsafe attribute]: attributes.md


---

r[unsafe]
# The `unsafe` keyword

r[unsafe.intro]
The `unsafe` keyword is used to create or discharge the obligation to prove something safe. Specifically:

- It is used to mark code that *defines* extra safety conditions that must be upheld elsewhere.
  - This includes `unsafe fn`, `unsafe static`, and `unsafe trait`.
- It is used to mark code that the programmer *asserts* satisfies safety conditions defined elsewhere.
  - This includes `unsafe {}`, `unsafe impl`, `unsafe fn` without [`unsafe_op_in_unsafe_fn`], `unsafe extern`, and `#[unsafe(attr)]`.

The following discusses each of these cases.
See the [keyword documentation][keyword] for some illustrative examples.

r[unsafe.positions]
The `unsafe` keyword can occur in several different contexts:

- unsafe functions (`unsafe fn`)
- unsafe blocks (`unsafe {}`)
- unsafe traits (`unsafe trait`)
- unsafe trait implementations (`unsafe impl`)
- unsafe external blocks (`unsafe extern`)
- unsafe external statics (`unsafe static`)
- unsafe attributes (`#[unsafe(attr)]`)

r[unsafe.fn]
## Unsafe functions (`unsafe fn`)

r[unsafe.fn.intro]
Unsafe functions are functions that are not safe in all contexts and/or for all possible inputs.
We say they have *extra safety conditions*, which are requirements that must be upheld by all callers and that the compiler does not check.
For example, [`get_unchecked`] has the extra safety condition that the index must be in-bounds.
The unsafe function should come with documentation explaining what those extra safety conditions are.

r[unsafe.fn.safety]
Such a function must be prefixed with the keyword `unsafe` and can only be called from inside an `unsafe` block, or inside `unsafe fn` without the [`unsafe_op_in_unsafe_fn`] lint.

r[unsafe.block]
## Unsafe blocks (`unsafe {}`)

r[unsafe.block.intro]
A block of code can be prefixed with the `unsafe` keyword to permit using the unsafe actions as defined in the [Unsafety] chapter, such as calling other unsafe functions or dereferencing raw pointers.

r[unsafe.block.fn-body]
By default, the body of an unsafe function is also considered to be an unsafe block;
this can be changed by enabling the [`unsafe_op_in_unsafe_fn`] lint.

By putting operations into an unsafe block, the programmer states that they have taken care of satisfying the extra safety conditions of all operations inside that block.

Unsafe blocks are the logical dual to unsafe functions:
where unsafe functions define a proof obligation that callers must uphold, unsafe blocks state that all relevant proof obligations of functions or operations called inside the block have been discharged.
There are many ways to discharge proof obligations;
for example, there could be run-time checks or data structure invariants that guarantee that certain properties are definitely true, or the unsafe block could be inside an `unsafe fn`, in which case the block can use the proof obligations of that function to discharge the proof obligations arising inside the block.

Unsafe blocks are used to wrap foreign libraries, make direct use of hardware or implement features not directly present in the language.
For example, Rust provides the language features necessary to implement memory-safe concurrency in the language but the implementation of threads and message passing in the standard library uses unsafe blocks.

Rust's type system is a conservative approximation of the dynamic safety requirements, so in some cases there is a performance cost to using safe code.
For example, a doubly-linked list is not a tree structure and can only be represented with reference-counted pointers in safe code.
By using `unsafe` blocks to represent the reverse links as raw pointers, it can be implemented without reference counting.
(See ["Learn Rust With Entirely Too Many Linked Lists"](https://rust-unofficial.github.io/too-many-lists/) for a more in-depth exploration of this particular example.)

[Unsafety]: unsafety.md

r[unsafe.trait]
## Unsafe traits (`unsafe trait`)

r[unsafe.trait.intro]
An unsafe trait is a trait that comes with extra safety conditions that must be upheld by *implementations* of the trait.
The unsafe trait should come with documentation explaining what those extra safety conditions are.

r[unsafe.trait.safety]
Such a trait must be prefixed with the keyword `unsafe` and can only be implemented by `unsafe impl` blocks.

r[unsafe.impl]
## Unsafe trait implementations (`unsafe impl`)

When implementing an unsafe trait, the implementation needs to be prefixed with the `unsafe` keyword.
By writing `unsafe impl`, the programmer states that they have taken care of satisfying the extra safety conditions required by the trait.

Unsafe trait implementations are the logical dual to unsafe traits: where unsafe traits define a proof obligation that implementations must uphold, unsafe implementations state that all relevant proof obligations have been discharged.

[keyword]: ../std/keyword.unsafe.html
[`get_unchecked`]: slice::get_unchecked
[`unsafe_op_in_unsafe_fn`]: ../rustc/lints/listing/allowed-by-default.html#unsafe-op-in-unsafe-fn

r[unsafe.extern]
## Unsafe external blocks (`unsafe extern`)

The programmer who declares an [external block] must assure that the signatures of the items contained within are correct. Failing to do so may lead to undefined behavior.  That this obligation has been met is indicated by writing `unsafe extern`.

r[unsafe.extern.edition2024]
> [!EDITION-2024]
> Prior to edition 2024, `extern` blocks were allowed without being qualified as `unsafe`.

[external block]: items/external-blocks.md

r[unsafe.attribute]
## Unsafe attributes (`#[unsafe(attr)]`)

An [unsafe attribute] is one that has extra safety conditions that must be upheld when using the attribute. The compiler cannot check whether these conditions have been upheld.  To assert that they have been, these attributes must be wrapped in `unsafe(..)`, e.g. `#[unsafe(no_mangle)]`.

[unsafe attribute]: attributes.md


---

r[undefined]
# Behavior considered undefined

r[undefined.intro]
Rust code is incorrect if it exhibits any of the behaviors in the following
list. This includes code within `unsafe` blocks and `unsafe` functions.
`unsafe` only means that avoiding undefined behavior is on the programmer; it
does not change anything about the fact that Rust programs must never cause
undefined behavior.

r[undefined.soundness]
It is the programmer's responsibility when writing `unsafe` code to ensure that
any safe code interacting with the `unsafe` code cannot trigger these
behaviors. `unsafe` code that satisfies this property for any safe client is
called *sound*; if `unsafe` code can be misused by safe code to exhibit
undefined behavior, it is *unsound*.

> [!WARNING]
> The following list is not exhaustive; it may grow or shrink. There is no formal model of Rust's semantics for what is and is not allowed in unsafe code, so there may be more behavior considered unsafe. We also reserve the right to make some of the behavior in that list defined in the future. In other words, this list does not say that anything will *definitely* always be undefined in all future Rust versions (but we might make such commitments for some list items in the future).
>
> Please read the [Rustonomicon] before writing unsafe code.

r[undefined.race]
* Data races.

r[undefined.pointer-access]
* Accessing (loading from or storing to) a place that is [dangling] or [based on
  a misaligned pointer].

r[undefined.place-projection]
* Performing a place projection that violates the requirements of [in-bounds
  pointer arithmetic](pointer#method.offset). A place projection is a [field
  expression][project-field], a [tuple index expression][project-tuple], or an
  [array/slice index expression][project-slice].

r[undefined.alias]
* Breaking the pointer aliasing rules. The exact aliasing rules are not determined yet, but here is an outline of the general principles:
  `&T` must point to memory that is not mutated while they are live (except for data inside an [`UnsafeCell<U>`]),
  and `&mut T` must point to memory that is not read or written by any pointer not derived from the reference and that no other reference points to while they are live.
  `Box<T>` is treated similar to `&'static mut T` for the purpose of these rules.
  The exact liveness duration is not specified, but some bounds exist:
  * For references, the liveness duration is upper-bounded by the syntactic
    lifetime assigned by the borrow checker; it cannot be live any *longer* than that lifetime.
  * Each time a reference or box is dereferenced or reborrowed, it is considered live.
  * Each time a reference or box is passed to or returned from a function, it is considered live.
  * When a reference (but not a `Box`!) is passed to a function, it is live at least as long as that function call, again except if the `&T` contains an [`UnsafeCell<U>`].

  All this also applies when values of these types are passed in a (nested) field of a compound type, but not behind pointer indirections.

r[undefined.immutable]
* Mutating immutable bytes.
  All bytes reachable through a [const-promoted] expression are immutable, as well as bytes reachable through borrows in `static` and `const` initializers that have been [lifetime-extended] to `'static`.
  The bytes owned by an immutable binding or immutable `static` are immutable, unless those bytes are part of an [`UnsafeCell<U>`].

  Moreover, the bytes [pointed to] by a shared reference, including transitively through other references (both shared and mutable) and `Box`es, are immutable; transitivity includes those references stored in fields of compound types.

  A mutation is any write of more than 0 bytes which overlaps with any of the relevant bytes (even if that write does not change the memory contents).

r[undefined.intrinsic]
* Invoking undefined behavior via compiler intrinsics.

r[undefined.target-feature]
* Executing code compiled with platform features that the current platform
  does not support (see [`target_feature`]), *except* if the platform explicitly documents this to be safe.

r[undefined.call]
* Calling a function with the wrong [call ABI][abi], or unwinding past a stack frame that does not allow unwinding (e.g. by calling a `"C-unwind"` function imported or transmuted as a `"C"` function or function pointer).

r[undefined.invalid]
* Producing an [invalid value][invalid-values]. "Producing" a
  value happens any time a value is assigned to or read from a place, passed to
  a function/primitive operation or returned from a function/primitive
  operation.

r[undefined.asm]
* Incorrect use of inline assembly. For more details, refer to the [rules] to
  follow when writing code that uses inline assembly.

r[undefined.runtime]
* Violating assumptions of the Rust runtime. Most assumptions of the Rust runtime are currently not explicitly documented.
  * For assumptions specifically related to unwinding, see the [panic documentation][unwinding-ffi].
  * The runtime assumes that a Rust stack frame is not deallocated without executing destructors for local variables owned by the stack frame. This assumption can be violated by C functions like `longjmp`.

> [!NOTE]
> Undefined behavior affects the entire program. For example, calling a function in C that exhibits undefined behavior of C means your entire program contains undefined behaviour that can also affect the Rust code. And vice versa, undefined behavior in Rust can cause adverse affects on code executed by any FFI calls to other languages.

r[undefined.pointed-to]
## Pointed-to bytes

The span of bytes a pointer or reference "points to" is determined by the pointer value and the size of the pointee type (using `size_of_val`).

r[undefined.misaligned]
## Places based on misaligned pointers
[based on a misaligned pointer]: #places-based-on-misaligned-pointers

r[undefined.misaligned.ptr]
A place is said to be "based on a misaligned pointer" if the last `*` projection
during place computation was performed on a pointer that was not aligned for its
type. (If there is no `*` projection in the place expression, then this is
accessing the field of a local or `static` and rustc will guarantee proper alignment. If
there are multiple `*` projections, then each of them incurs a load of the
pointer-to-be-dereferenced itself from memory, and each of these loads is
subject to the alignment constraint. Note that some `*` projections can be
omitted in surface Rust syntax due to automatic dereferencing; we are
considering the fully expanded place expression here.)

For instance, if `ptr` has type `*const S` where `S` has an alignment of 8, then
`ptr` must be 8-aligned or else `(*ptr).f` is "based on an misaligned pointer".
This is true even if the type of the field `f` is `u8` (i.e., a type with
alignment 1). In other words, the alignment requirement derives from the type of
the pointer that was dereferenced, *not* the type of the field that is being
accessed.

r[undefined.misaligned.load-store]
Note that a place based on a misaligned pointer only leads to undefined behavior
when it is loaded from or stored to.

r[undefined.misaligned.raw]
`&raw const`/`&raw mut` on such a place is allowed.

r[undefined.misaligned.reference]
`&`/`&mut` on a place requires the alignment of the field type (or
else the program would be "producing an invalid value"), which generally is a
less restrictive requirement than being based on an aligned pointer.

r[undefined.misaligned.packed]
Taking a reference will lead to a compiler error in cases where the field type might be
more aligned than the type that contains it, i.e., `repr(packed)`. This means
that being based on an aligned pointer is always sufficient to ensure that the
new reference is aligned, but it is not always necessary.

r[undefined.dangling]
## Dangling pointers
[dangling]: #dangling-pointers

r[undefined.dangling.def]
A reference/pointer is "dangling" if not all of the bytes it
[points to] are part of the same live allocation (so in particular they all have to be
part of *some* allocation).

r[undefined.dangling.zero-size]
If the size is 0, then the pointer is trivially never "dangling"
(even if it is a null pointer).

r[undefined.dangling.dynamic-size]
Note that dynamically sized types (such as slices and strings) point to their
entire range, so it is important that the length metadata is never too large.

r[undefined.dangling.alloc-limit]
In particular, the dynamic size of a Rust value (as determined by `size_of_val`)
must never exceed `isize::MAX`, since it is impossible for a single allocation
to be larger than `isize::MAX`.

r[undefined.validity]
## Invalid values
[invalid-values]: #invalid-values

r[undefined.validity.def]
The Rust compiler assumes that all values produced during program execution are
"valid", and producing an invalid value is hence immediate UB.

Whether a value is valid depends on the type:

r[undefined.validity.bool]
* A [`bool`] value must be `false` (`0`) or `true` (`1`).

r[undefined.validity.fn-pointer]
* A `fn` pointer value must be non-null.

r[undefined.validity.char]
* A `char` value must not be a surrogate (i.e., must not be in the range `0xD800..=0xDFFF`) and must be equal to or less than `char::MAX`.

r[undefined.validity.never]
* A `!` value must never exist.

r[undefined.validity.scalar]
* An integer (`i*`/`u*`), floating point value (`f*`), or raw pointer must be
  initialized, i.e., must not be obtained from uninitialized memory.

r[undefined.validity.str]
* A `str` value is treated like `[u8]`, i.e. it must be initialized.

r[undefined.validity.enum]
* An `enum` must have a valid discriminant, and all fields of the variant indicated by that discriminant must be valid at their respective type.

r[undefined.validity.struct]
* A `struct`, tuple, and array requires all fields/elements to be valid at their respective type.

r[undefined.validity.union]
* For a `union`, the exact validity requirements are not decided yet.
  Obviously, all values that can be created entirely in safe code are valid.
  If the union has a zero-sized field, then every possible value is valid.
  Further details are [still being debated](https://github.com/rust-lang/unsafe-code-guidelines/issues/438).

r[undefined.validity.reference-box]
* A reference or [`Box<T>`] must be aligned and non-null, it cannot be [dangling], and it must point to a valid value
  (in case of dynamically sized types, using the actual dynamic type of the
  pointee as determined by the metadata).
  Note that the last point (about pointing to a valid value) remains a subject of some debate.

r[undefined.validity.wide]
* The metadata of a wide reference, [`Box<T>`], or raw pointer must match
  the type of the unsized tail:
  * `dyn Trait` metadata must be a pointer to a compiler-generated vtable for `Trait`.
    (For raw pointers, this requirement remains a subject of some debate.)
  * Slice (`[T]`) metadata must be a valid `usize`.
    Furthermore, for wide references and [`Box<T>`], slice metadata is invalid
    if it makes the total size of the pointed-to value bigger than `isize::MAX`.

r[undefined.validity.valid-range]
* If a type has a custom range of a valid values, then a valid value must be in that range.
  In the standard library, this affects [`NonNull<T>`] and [`NonZero<T>`].

  > [!NOTE]
  > `rustc` achieves this with the unstable `rustc_layout_scalar_valid_range_*` attributes.

r[undefined.validity.const-provenance]
* **In [const contexts]**: In addition to what is described above, further provenance-related requirements apply during const evaluation. Any value that holds pure integer data (the `i*`/`u*`/`f*` types as well as `bool` and `char`, enum discriminants, and slice metadata) must not carry any provenance. Any value that holds pointer data (references, raw pointers, function pointers, and `dyn Trait` metadata) must either carry no provenance, or all bytes must be fragments of the same original pointer value in the correct order.

  This implies that transmuting or otherwise reinterpreting a pointer (reference, raw pointer, or function pointer) into a non-pointer type (such as integers) is undefined behavior if the pointer had provenance.

  > [!EXAMPLE]
  > All of the following are UB:
  >
  > ```rust,compile_fail
  > # use core::mem::MaybeUninit;
  > # use core::ptr;
  > // We cannot reinterpret a pointer with provenance as an integer,
  > // as then the bytes of the integer will have provenance.
  > const _: usize = {
  >     let ptr = &0;
  >     unsafe { (&raw const ptr as *const usize).read() }
  > };
  >
  > // We cannot rearrange the bytes of a pointer with provenance and
  > // then interpret them as a reference, as then a value holding
  > // pointer data will have pointer fragments in the wrong order.
  > const _: &i32 = {
  >     let mut ptr = &0;
  >     let ptr_bytes = &raw mut ptr as *mut MaybeUninit::<u8>;
  >     unsafe { ptr::swap(ptr_bytes.add(1), ptr_bytes.add(2)) };
  >     ptr
  > };
  > ```

r[undefined.validity.undef]
**Note:** Uninitialized memory is also implicitly invalid for any type that has
a restricted set of valid values. In other words, the only cases in which
reading uninitialized memory is permitted are inside `union`s and in "padding"
(the gaps between the fields of a type).

[`bool`]: types/boolean.md
[`const`]: items/constant-items.md
[abi]: items/external-blocks.md#abi
[const contexts]: const-eval.const-context
[`target_feature`]: attributes/codegen.md#the-target_feature-attribute
[`UnsafeCell<U>`]: std::cell::UnsafeCell
[Rustonomicon]: ../nomicon/index.html
[`NonNull<T>`]: core::ptr::NonNull
[`NonZero<T>`]: core::num::NonZero
[place expression context]: expressions.md#place-expressions-and-value-expressions
[rules]: inline-assembly.md#rules-for-inline-assembly
[points to]: #pointed-to-bytes
[pointed to]: #pointed-to-bytes
[project-field]: expressions/field-expr.md
[project-tuple]: expressions/tuple-expr.md#tuple-indexing-expressions
[project-slice]: expressions/array-expr.md#array-and-slice-indexing-expressions
[unwinding-ffi]: panic.md#unwinding-across-ffi-boundaries
[const-promoted]: destructors.md#constant-promotion
[lifetime-extended]: destructors.md#temporary-lifetime-extension


---

# Behavior not considered `unsafe`

The Rust compiler does not consider the following behaviors _unsafe_,
though a programmer may (should) find them undesirable, unexpected,
or erroneous.

- Deadlocks
- Leaks of memory and other resources
- Exiting without calling destructors
- Exposing randomized base addresses through pointer leaks

## Integer overflow

If a program contains arithmetic overflow, the programmer has made an
error. In the following discussion, we maintain a distinction between
arithmetic overflow and wrapping arithmetic. The first is erroneous,
while the second is intentional.

When the programmer has enabled `debug_assert!` assertions (for
example, by enabling a non-optimized build), implementations must
insert dynamic checks that `panic` on overflow. Other kinds of builds
may result in `panics` or silently wrapped values on overflow, at the
implementation's discretion.

In the case of implicitly-wrapped overflow, implementations must
provide well-defined (even if still considered erroneous) results by
using two's complement overflow conventions.

The integral types provide inherent methods to allow programmers
explicitly to perform wrapping arithmetic. For example,
`i32::wrapping_add` provides two's complement, wrapping addition.

The standard library also provides a `Wrapping<T>` newtype which
ensures all standard arithmetic operations for `T` have wrapping
semantics.

See [RFC 560] for error conditions, rationale, and more details about
integer overflow.

## Logic errors

Safe code may impose extra logical constraints that can be checked
at neither compile-time nor runtime. If a program breaks such
a constraint, the behavior may be unspecified but will not result in
undefined behavior. This could include panics, incorrect results,
aborts, and non-termination. The behavior may also differ between
runs, builds, or kinds of build.

For example, implementing both `Hash` and `Eq` requires that values
considered equal have equal hashes. Another example are data structures
like `BinaryHeap`, `BTreeMap`, `BTreeSet`, `HashMap` and `HashSet`
which describe constraints on the modification of their keys while
they are in the data structure. Violating such constraints is not
considered unsafe, yet the program is considered erroneous and
its behavior unpredictable.

[RFC 560]: https://github.com/rust-lang/rfcs/blob/master/text/0560-integer-overflow.md
