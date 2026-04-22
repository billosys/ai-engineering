---
concept: Unsafety (Reference)
slug: rust-unsafety-reference
category: unsafe-rust
subcategory: safety-model
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Unsafety"
chapter_number: 17
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "unsafe operations"
  - "unsafe keyword"
  - "undefined behavior in Rust"
  - "unsound code"
  - "sound code"
  - "invalid values"
  - "behavior not considered unsafe"
prerequisites: []
extends:
  - nomicon-overview
related:
  - rust-inline-assembly
  - rust-constant-evaluation
contrasts_with: []
answers_questions:
  - "What operations require unsafe in Rust?"
  - "What are all the positions where the unsafe keyword can appear?"
  - "What is the complete list of behavior considered undefined in Rust?"
  - "What constitutes an invalid value for each Rust type?"
  - "What is the relationship between unsafe functions and unsafe blocks?"
  - "What behaviors are explicitly not considered unsafe?"
  - "What are the pointer aliasing rules?"
---

# Quick Definition

Unsafe operations are those that can potentially violate Rust's memory-safety guarantees. The `unsafe` keyword serves dual roles: it defines extra safety conditions (on `fn`, `trait`, `static`, `extern`) and asserts that conditions are upheld (on blocks, `impl`, `extern`, attributes). The Reference provides the authoritative catalog of undefined behavior, invalid values, and the formal distinction between soundness and unsoundness.

# Core Definition

**Unsafe operations** (the things requiring `unsafe` contexts):
1. Dereferencing a raw pointer
2. Reading or writing a mutable or unsafe external static variable
3. Accessing a field of a `union` (other than assigning to it)
4. Calling an unsafe function
5. Calling a safe function marked with `target_feature` from a function lacking that feature
6. Implementing an unsafe trait
7. Declaring an `extern` block (required to be `unsafe extern` since Edition 2024)
8. Applying an unsafe attribute to an item

**The `unsafe` keyword** appears in seven positions:
- `unsafe fn` -- declares extra safety conditions callers must uphold
- `unsafe {}` -- asserts all safety conditions inside are discharged
- `unsafe trait` -- declares conditions implementations must uphold
- `unsafe impl` -- asserts trait safety conditions are met
- `unsafe extern` -- asserts extern block signatures are correct
- `unsafe static` -- marks a static with extra safety conditions
- `#[unsafe(attr)]` -- asserts unsafe attribute conditions are met

Unsafe blocks are the **logical dual** of unsafe functions: functions define proof obligations, blocks discharge them. By default, an unsafe function's body is also an unsafe block (changeable via the `unsafe_op_in_unsafe_fn` lint).

**Soundness**: unsafe code is *sound* if no safe code interacting with it can trigger undefined behavior; it is *unsound* if safe code can cause UB through it.

# Prerequisites

Understanding of Rust's ownership, borrowing, and type system. Familiarity with the concept of undefined behavior in systems programming.

# Key Properties

1. The `unsafe` keyword does not disable the borrow checker or type system -- it only permits the eight additional operations listed above
2. Unsafe blocks wrap foreign libraries, implement features not directly in the language, and optimize past the type system's conservative approximations
3. A doubly-linked list cannot be represented without reference counting in safe code; unsafe blocks with raw pointers eliminate this overhead
4. Data races are undefined behavior in Rust
5. Accessing (loading/storing) a dangling or misaligned pointer is UB; a zero-size pointer is trivially never dangling
6. Pointer aliasing rules: `&T` must not point to mutated memory (except inside `UnsafeCell<U>`); `&mut T` must point to memory not accessed by any other pointer; `Box<T>` is treated like `&'static mut T`
7. Mutating immutable bytes (const-promoted, static initializers, or data behind shared references) is UB
8. Producing an invalid value is immediate UB -- validity is checked for bool, char, fn pointers, `!`, integers, enums, structs, references, Box, and wide pointer metadata
9. `bool` must be 0 or 1; `char` must not be a surrogate and must be <= `char::MAX`; `fn` pointer must be non-null; `!` must never exist
10. References and `Box<T>` must be aligned, non-null, non-dangling, and point to valid values; slice metadata must be valid `usize` and total size <= `isize::MAX`
11. In const contexts, integer/float/bool/char values must not carry pointer provenance; pointer values must carry no provenance or consistent fragments of one original pointer

# Construction / Recognition

## Identifying Undefined Behavior

Check the authoritative list: data races; dangling/misaligned access; invalid place projections; aliasing violations; mutating immutable bytes; compiler intrinsic UB; executing unsupported target features; wrong call ABI or unwinding past non-unwinding frames; producing invalid values; incorrect inline assembly; violating runtime assumptions (stack deallocation without destructors, e.g. `longjmp`).

## Writing Sound Unsafe Code

1. Identify which of the eight unsafe operations your code uses
2. Wrap each in an `unsafe` block with clear justification
3. Ensure no safe caller can trigger UB through your interface
4. Document safety contracts on `unsafe fn` declarations
5. Use `unsafe_op_in_unsafe_fn` lint to require explicit `unsafe` blocks inside unsafe functions
6. Validate pointer alignment, bounds, and liveness before dereferencing raw pointers
7. Respect aliasing rules: never create `&mut T` and `&T` to the same memory simultaneously (unless behind `UnsafeCell`)

# Context & Application

Chapter 17 provides the formal, authoritative specification of unsafe operations and undefined behavior that the Nomicon's practical guidance is built upon. The UB list is explicitly described as non-exhaustive and may grow or shrink; there is no formal model of Rust's semantics yet. The aliasing rules are not fully determined but outlined in general principles. The chapter also clarifies what Rust considers safe but undesirable: deadlocks, memory leaks, exiting without destructors, pointer address leaks, integer overflow (wrapping in release, panicking in debug), and logic errors (violating `Hash`/`Eq` consistency, mutating `BTreeMap` keys).

The invalid-values specification is particularly important for `transmute`, `MaybeUninit`, and union access -- any of these that produce a value violating the rules is immediate UB, not just "potentially problematic."

# Examples

**Example 1** (Unsafe block discharging a proof obligation):
```rust
fn index(idx: usize, arr: &[u8]) -> Option<u8> {
    if idx < arr.len() {
        // Safety: idx is bounds-checked above
        unsafe { Some(*arr.get_unchecked(idx)) }
    } else {
        None
    }
}
```

**Example 2** (Misaligned pointer -- UB even if field type is u8):
```rust
// If ptr: *const S where S has alignment 8,
// then (*ptr).f is "based on a misaligned pointer" if ptr is not 8-aligned,
// even if f has type u8 (alignment 1).
// &raw const/&raw mut on such a place is allowed, but load/store is UB.
```

**Example 3** (Behaviors explicitly NOT considered unsafe):
```rust
// These are safe (not UB) but undesirable:
// - Deadlocks
// - Memory leaks
// - Integer overflow (wraps in release, panics in debug)
// - Exiting without calling destructors
// - Violating Hash/Eq consistency (logic error, not UB)
```

# Relationships

## Builds Upon
(none -- this is the authoritative specification)

## Enables
- **rust-inline-assembly** -- incorrect inline assembly is listed as a source of UB; assembly rules reference this chapter
- **rust-constant-evaluation** -- const contexts have additional provenance-related validity requirements

## Related
- **nomicon-overview** -- the Nomicon's practical treatment of safe/unsafe builds on this formal specification
- **rust-abi-and-runtime** -- wrong call ABI and unwinding violations are forms of UB defined here

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming `union` field access only requires unsafe for reading, not for pattern matching.
  **Correction**: Accessing a union field (reading it, matching on it) requires unsafe. Only assigning to a union field is safe. This is because reading may produce an invalid value for the field's type.

- **Error**: Creating a reference to a packed struct field, which may be misaligned.
  **Correction**: Taking `&packed_struct.field` where the field might be misaligned is a compiler error for `repr(packed)` types. Use `&raw const packed_struct.field` (raw pointer) instead, then read with `read_unaligned`.

- **Error**: Transmuting a pointer with provenance to an integer in a const context.
  **Correction**: In const evaluation, pointer-to-integer reinterpretation is UB if the pointer had provenance. Integer types must not carry provenance in const contexts.

# Common Confusions

- **Confusion**: Believing the UB list is exhaustive and stable.
  **Clarification**: The list explicitly states it "is not exhaustive; it may grow or shrink." There is no formal model of Rust's semantics. Some listed items may become defined in future versions, and new UB may be added.

- **Confusion**: Thinking integer overflow is undefined behavior.
  **Clarification**: Integer overflow is explicitly safe (not UB). In debug builds it panics; in release builds it wraps using two's complement. The `Wrapping<T>` type and methods like `i32::wrapping_add` make wrapping explicit. It is erroneous but not a safety violation.

- **Confusion**: Assuming `unsafe fn` bodies automatically require `unsafe` blocks for unsafe operations.
  **Clarification**: By default, an unsafe function's body is itself an unsafe block. The `unsafe_op_in_unsafe_fn` lint changes this behavior, requiring explicit `unsafe` blocks. The lint is recommended for clearer safety documentation.

# Source Reference

Chapter 17 (Unsafety, 486 lines): Three sections -- "Unsafety" (8 unsafe operations), "The unsafe keyword" (7 positions, detailed semantics of each), "Behavior considered undefined" (full UB catalog with pointed-to bytes, misaligned places, dangling pointers, invalid values for all types including const-context provenance rules), "Behavior not considered unsafe" (deadlocks, leaks, integer overflow, logic errors).

# Verification Notes

- Definition source: Direct extraction from Chapter 17 (486 lines), covering all three major sections
- Key Properties: Items 1-11 drawn directly from source text with minimal synthesis
- Confidence rationale: HIGH -- the source is the authoritative language specification with explicit, detailed rules
- Uncertainties: Aliasing rules "are not determined yet" (source verbatim); union validity "not decided yet"; whether wide reference must point to valid value "remains a subject of some debate"
- Cross-reference status: All slugs reference cards in the reference and nomicon extraction sets
