---
concept: Pin Type
slug: pin-type
category: type-system
subcategory: type-wrappers
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pin"
extraction_confidence: high
aliases:
  - "Pin<Ptr>"
  - "Pin wrapper"
  - "Pin struct"
  - "std::pin::Pin"
prerequisites:
  - pinning
  - place
  - move-semantics
  - unpin-trait
extends:
  - pinning
related:
  - pinning-values
  - pin-and-async
  - phantom-pinned
contrasts_with:
  - unpin-trait
answers_questions:
  - "What is the Pin type?"
  - "What is the difference between Pin<Box<T>> and Box<T>?"
  - "Does Pin add a runtime indirection?"
---

# Quick Definition

`Pin<Ptr>` is a compile-time marker wrapper around pointer types (like `Box` or `&mut`) that guarantees the pointee will remain valid at its address until dropped. It is compiled away entirely and has no runtime cost.

# Core Definition

"`Pin` is a marker type, it is important for type checking, but is compiled away and does not exist at runtime (`Pin<Ptr>` is guaranteed to have the same memory layout and ABI as `Ptr`). It is a wrapper of pointers (such as `Box`), so it behaves like a pointer type, but it does not add an indirection, `Box<Foo>` and `Pin<Box<Foo>>` are the same when a program is run. It is better to think of `Pin` as a modifier to the pointer rather than a pointer itself." (Ch. 2, "Pin" section)

"`Pin<Ptr>` means that the pointee of `Ptr` (not `Ptr` itself) is pinned. That is, `Pin` guarantees that the pointee (not the pointer) will remain valid with respect to its address until the pointee is dropped. If the pointee is address-sensitive (i.e., is `!Unpin`), then the pointee will not be moved." (Ch. 2, "Pin" section)

# Prerequisites

- **Pinning** — `Pin` is the concrete type that expresses the abstract concept of pinning in Rust's type system
- **Place** — Understanding that `Pin` concerns the pointee's place in memory, not the pointer itself
- **Move semantics** — `Pin` exists to restrict moves; understanding what moves are and why they can be problematic is essential
- **Unpin trait** — `Pin` only constrains types that are `!Unpin`; for `Unpin` types it has essentially no effect

# Key Properties

1. `Pin<Ptr>` is a newtype wrapper over pointer types; it has the same memory layout and ABI as the inner pointer
2. `Pin` applies to the pointee, not the pointer itself — the pointer can still be moved
3. For immutable pointers (e.g., `&T`), `Pin` has no effect since the pointee cannot be mutated or replaced
4. For mutable pointers, `Pin` withholds `DerefMut` unless the pointee is `Unpin`
5. `Pin` implements `Deref` unconditionally, so immutable access is always available
6. For `Unpin` types, `Pin<Box<T>>` and `Box<T>` are effectively interchangeable via `Pin::new` and `Pin::into_inner`
7. `Pin` is purely a compile-time construct — it is erased during compilation

# Construction / Recognition

## To Recognize Pin Usage

1. Look for `Pin<Box<T>>`, `Pin<&T>`, or `Pin<&mut T>` in type signatures
2. The presence of `Pin` indicates the API intends the pointee to remain at a stable address
3. If the inner type is `Unpin`, `Pin` is effectively a no-op

## To Work With Pin

1. Use `Deref` (or explicit `deref()`) for immutable access — this always works
2. Use `as_ref()` to get `Pin<&T>` from a pinned pointer
3. Use `as_mut()` to reborrow `Pin<&mut T>` (needed because `Pin` does not support implicit reborrowing)
4. For unsafe escape hatches, use `into_inner_unchecked` or `get_unchecked_mut`

# Context & Application

`Pin` is the mechanism by which Rust expresses address stability in its type system without language-level support. It was introduced after Rust 1.0 specifically to support async/await, where compiler-generated futures can contain self-references between fields. The most visible use of `Pin` for application programmers is in the signature of `Future::poll`, where `self` is `Pin<&mut Self>`.

For most async code using `async`/`await`, `Pin` is handled automatically by the compiler. It becomes relevant when working with futures directly, implementing custom futures, or using combinators like `select!`.

# Examples

**Immutable access through deref** (Ch. 2, "Using pinned types"):
> "Using a pinned pointer as an immutably borrowed reference is trivial because of `Pin`'s implementation of `Deref`. You can mostly just treat `Pin<Ptr<T>>` as `&T`, using an explicit `deref()` if necessary."

**Reborrowing with `as_mut`** (Ch. 2, "Using pinned types"):
```rust
impl Type {
    fn method(self: Pin<&mut Self>) {
        // do something
    }

    fn call_method_twice(mut self: Pin<&mut Self>) {
        // `method` consumes `self`, so reborrow the `Pin<&mut Self>` via `as_mut`.
        self.as_mut().method();
        self.as_mut().method();
    }
}
```

# Relationships

## Builds Upon
- **Pinning** — `Pin` is the type-level encoding of the pinning concept
- **Move semantics** — `Pin` restricts the move semantics that Rust normally allows

## Enables
- **Pinning values** — `Pin` is the wrapper; pinning values is the act of creating `Pin<Ptr>` instances
- **Pin and async** — `Pin` appears in `Future::poll` to ensure futures with self-references remain valid
- **Structural pinning** — projecting pin guarantees to fields requires understanding `Pin`

## Related
- **Phantom pinned** — `PhantomPinned` is used to make types `!Unpin`, which is when `Pin` has meaningful effect

## Contrasts With
- **Unpin trait** — `Unpin` types make `Pin` a no-op; `!Unpin` types are where `Pin` actually constrains behavior

# Common Errors

- **Error**: Assuming `Pin<Ptr>` pins the pointer itself.
  **Correction**: `Pin` pins the pointee (the data the pointer points to), not the pointer. The pointer can still be moved freely.

- **Error**: Trying to get `&mut T` from `Pin<&mut T>` for a `!Unpin` type using safe code.
  **Correction**: `Pin` deliberately withholds `DerefMut` for `!Unpin` types. Use the unsafe `get_unchecked_mut` only if you can uphold the pinning invariants.

# Common Confusions

- **Confusion**: Believing `Pin` prevents all moves of the pointee.
  **Clarification**: `Pin` only prevents moves of `!Unpin` types. For `Unpin` types, `Pin` has essentially no effect and the data can still be moved.

- **Confusion**: Thinking `Pin` adds a runtime indirection or overhead like a smart pointer.
  **Clarification**: `Pin<Ptr>` has the same memory layout and ABI as `Ptr`. It is a compile-time-only wrapper that is completely erased during compilation.

- **Confusion**: Thinking `Pin` is about validity of the pointer.
  **Clarification**: `Pin` is about validity of the pointee at its address. The pointer itself is not pinned and can be moved, copied, or dropped normally.

# Source Reference

Chapter 2: Pinning, sections "Pin," "How pinning works," and "Pinning pointer types."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pin" section (lines 89-93 of source)
- Confidence rationale: HIGH — the source provides an explicit, detailed definition of `Pin` with clear explanation of its properties and guarantees
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, place, move-semantics, unpin-trait, phantom-pinned)
