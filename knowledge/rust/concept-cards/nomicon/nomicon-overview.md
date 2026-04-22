---
concept: Nomicon Overview
slug: nomicon-overview
category: unsafe-rust
subcategory: null
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Introduction / Meet Safe and Unsafe"
chapter_number: 0
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "safe and unsafe Rust"
  - "unsafe Rust boundary"
  - "soundness property"
  - "undefined behavior in Rust"
  - "working with unsafe"
prerequisites: []
extends: []
related:
  - data-layout-repr
  - exotic-types
  - type-conversions
  - ownership-and-lifetimes
contrasts_with: []
answers_questions:
  - "What is the relationship between Safe Rust and Unsafe Rust?"
  - "What does the unsafe keyword actually allow you to do?"
  - "What constitutes undefined behavior in Rust?"
  - "What is the soundness property of Safe Rust?"
  - "How does module-level privacy relate to unsafe code correctness?"
  - "What is considered safe but undesirable behavior in Rust?"
---

# Quick Definition

Rust contains two languages: Safe Rust (which guarantees no undefined behavior) and Unsafe Rust (which permits five additional operations that can cause UB). The `unsafe` keyword controls the boundary between them, and soundness -- the guarantee that safe code cannot cause UB -- is Rust's fundamental safety property.

# Core Definition

Safe Rust guarantees that "no matter what, Safe Rust can't cause Undefined Behavior" -- this is the **soundness property** (Ch. 1, "How Safe and Unsafe Interact"). Unsafe Rust is "exactly like Safe Rust with all the same rules and semantics. It just lets you do some extra things that are Definitely Not Safe." The `unsafe` keyword serves dual purposes: it declares the existence of contracts the compiler cannot check (on functions and trait declarations), and it declares that a programmer has verified those contracts are upheld (on blocks and trait implementations).

The safe/unsafe split creates an **asymmetric trust relationship**: Safe Rust inherently trusts that any Unsafe Rust it touches has been written correctly, but Unsafe Rust cannot trust Safe Rust without care. Unsafe code must defend against incorrect (but safe-to-write) implementations of traits like `Ord`, since generic safe code may provide broken implementations. The `BTreeMap` example illustrates this: even with a sloppy `Ord` implementation, the unsafe internals must never cause UB, though the data structure may behave erratically.

The scope of unsafe code's soundness obligations extends beyond the `unsafe` block to the entire module. Privacy (module boundaries) is the primary mechanism for limiting the trust scope of unsafe code -- private fields and functions restrict which safe code can interfere with invariants that unsafe code relies upon.

# Prerequisites

This is a foundational concept within the Nomicon -- it establishes the framework for all subsequent chapters. General familiarity with Rust ownership, borrowing, and the type system is assumed.

# Key Properties

1. Unsafe Rust permits exactly five additional operations: dereference raw pointers, call unsafe functions, implement unsafe traits, access/modify mutable statics, and access union fields
2. The soundness property guarantees that safe code alone cannot cause undefined behavior
3. The `unsafe` keyword on functions/traits declares unchecked contracts; on blocks/impls it asserts contracts are upheld
4. Safe Rust trusts Unsafe Rust implicitly; Unsafe Rust must not trust generic Safe Rust
5. Unsafe code's soundness obligations are non-local -- a change in safe code (like `<` to `<=`) can make an unsafe block unsound
6. Module privacy is the primary tool for bounding the scope of unsafe code's trust
7. Unsafe traits (like `Send`, `Sync`, `GlobalAlloc`) exist to shift the burden of maintaining invariants to trait implementors
8. `Send` and `Sync` are automatically derived for types composed entirely of `Send`/`Sync` types
9. Things Rust considers "safe" but not desirable: deadlocks, race conditions, memory leaks, integer overflow, aborting, deleting the production database

# Construction / Recognition

## To Write Sound Unsafe Code

1. Identify the safety invariants your unsafe code depends on
2. Ensure those invariants cannot be violated by any safe code that can reach them
3. Use module privacy to restrict access to fields and functions that could violate invariants
4. Do not trust generic type parameters -- their implementations may be broken
5. Trust specific, well-known implementations (integers, slices) as a measured risk
6. Consider whether a trait should be marked `unsafe` if unsafe code cannot defend against broken implementations
7. Document the safety contracts on all `unsafe fn` declarations

## To Recognize Unsoundness

1. Check if any safe code modification could cause the unsafe block to exhibit UB
2. Verify that all private invariants are actually private (not accessible outside the module)
3. Confirm that generic trait implementations cannot violate assumed properties

# Context & Application

The Rustonomicon exists as a companion to The Reference, focusing on how language features interact in unsafe contexts and the practical problems that arise. It covers: the meaning of (un)safety, unsafe primitives, safe abstractions over unsafe code, subtyping and variance, exception safety, uninitialized memory, type punning, concurrency, FFI, and optimization. The book assumes "considerable prior knowledge" of systems programming and Rust.

The safe/unsafe boundary is the central design insight of Rust: by concentrating danger in `unsafe` blocks and requiring the rest of the language to be sound, Rust achieves C-level control without C-level pervasive unsafety. The five unsafe operations are carefully chosen as the minimal set that cannot be statically verified -- everything else remains under the compiler's guarantee.

# Examples

**Example 1** (Ch. 1, "Working with Unsafe"): A correct unsafe function that checks bounds before unchecked indexing:
```rust
fn index(idx: usize, arr: &[u8]) -> Option<u8> {
    if idx < arr.len() {
        unsafe { Some(*arr.get_unchecked(idx)) }
    } else {
        None
    }
}
```
Changing `<` to `<=` in the safe code makes the function unsound -- demonstrating the non-locality of safety.

**Example 2** (Ch. 1, "Working with Unsafe"): A `Vec` implementation where a private `make_room` method that merely increments `cap` would be 100% safe code but completely unsound, because it violates the invariant that `cap` reflects allocated space. However, because `make_room` is private, only code within the module can call it, preserving soundness.

**Example 3** (Ch. 1, "How Safe and Unsafe Interact"): The hypothetical `UnsafeOrd` trait shows how marking a trait `unsafe` shifts correctness responsibility to implementors, allowing `BTreeMap` internals to trust the ordering implementation.

# Relationships

## Builds Upon
(none -- this is the foundational framing for all Nomicon content)

## Enables
- **data-layout-repr** -- understanding safe/unsafe boundary is needed to reason about repr guarantees
- **ownership-and-lifetimes** -- lifetime rules are the safe language's mechanism; unsafe code must uphold them manually
- **type-conversions** -- transmute and casts are unsafe operations requiring understanding of soundness

## Related
- **exotic-types** -- ZSTs, DSTs, and empty types have special unsafe considerations
- **drop-check-and-phantom-data** -- drop checking is part of the compiler's soundness enforcement

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming the scope of unsafe is limited to the `unsafe` block itself.
  **Correction**: Unsafe code's soundness depends on all code that can affect its invariants, which extends to the entire module (bounded by privacy). A safe function that modifies private struct fields can make an unsafe block in another function unsound.

- **Error**: Trusting generic type parameters in unsafe code (e.g., trusting that a generic `Ord` implementation is correct).
  **Correction**: Unsafe code must defend against broken generic implementations. Only trust specific, well-known types or use `unsafe` traits to shift the correctness burden to implementors.

# Common Confusions

- **Confusion**: Believing `unsafe` disables the borrow checker or type system.
  **Clarification**: Unsafe Rust has the same rules and semantics as Safe Rust -- it only unlocks five additional operations. The borrow checker, type system, and all other checks remain fully active.

- **Confusion**: Thinking memory leaks, deadlocks, or integer overflow are undefined behavior.
  **Clarification**: Rust explicitly considers these "safe" -- they cannot be caused by `unsafe` code alone and are not classified as UB. They are undesirable but not safety violations.

- **Confusion**: Thinking `unsafe` means "this code is dangerous."
  **Clarification**: On a block, `unsafe` means "I, the programmer, have verified the safety contracts." On a function or trait, it means "callers/implementors must verify contracts." It's a trust declaration, not a danger warning.

# Source Reference

Chapter 0: Introduction -- scope of the Nomicon, relationship to The Reference. Chapter 1: Meet Safe and Unsafe -- the safe/unsafe boundary, soundness property, what unsafe allows, UB catalog, unsafe traits (`Send`, `Sync`, `GlobalAlloc`), working with unsafe (soundness, non-locality, module privacy).

# Verification Notes

- Definition source: Direct synthesis from Ch. 0 (45 lines) and Ch. 1 (459 lines), with key quotations from "How Safe and Unsafe Interact" and "What Unsafe Rust Can Do" sections
- Key Properties: Items 1-2 are verbatim from source; items 3-9 are synthesized from explicit discussion
- Confidence rationale: HIGH -- the source provides explicit, detailed definitions of all concepts with concrete examples
- Uncertainties: The source notes Rust's aliasing model is not yet fully defined; the UB list may evolve
- Cross-reference status: All slugs reference cards in the nomicon extraction set
