---
concept: PhantomPinned
slug: phantom-pinned
category: type-system
subcategory: marker-types
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Unpin"
extraction_confidence: medium
aliases:
  - "std::marker::PhantomPinned"
  - "PhantomPinned marker"
prerequisites:
  - unpin-trait
  - pinning
  - address-sensitivity
extends: []
related:
  - pin-type
  - self-referential-type
contrasts_with: []
answers_questions:
  - "What is PhantomPinned?"
  - "What is the difference between Unpin and !Unpin types?"
---

# Quick Definition

`PhantomPinned` is a zero-sized marker type from `std::marker` that, when included as a field, causes a struct to be `!Unpin`. This is the stable-Rust mechanism for declaring that a type is address-sensitive and should be subject to pinning's movement restrictions.

# Core Definition

"You can opt-out [of `Unpin`] by having a `PhantomPinned` field or (if you're using nightly) with `impl !Unpin for ... {}`." (Async Reference, Ch. 2: Pinning, "Unpin" section)

`PhantomPinned` is referenced as a field that makes a type `!Unpin`, linking to its documentation at `std::marker::PhantomPinned`. Since `Unpin` is an auto-trait, including a single `!Unpin` field (such as `PhantomPinned`) causes the entire containing type to become `!Unpin`.

# Prerequisites

- **Unpin trait** — `PhantomPinned` exists to opt a type out of `Unpin`; understanding what `Unpin` means is essential
- **Pinning** — `PhantomPinned` only has meaning in the context of pinning; it makes pinning "take effect" for a type
- **Address sensitivity** — `PhantomPinned` marks a type as address-sensitive (`!Unpin`)

# Key Properties

1. `PhantomPinned` is a zero-sized type (ZST) — it adds no runtime overhead
2. Including a `PhantomPinned` field in a struct makes the struct `!Unpin`
3. This is the stable-Rust mechanism for opting out of `Unpin` (the alternative, `impl !Unpin`, is nightly-only)
4. Because `Unpin` is an auto-trait, one `!Unpin` field is sufficient to make the whole type `!Unpin`
5. Located in `std::marker`, alongside other marker types like `PhantomData`
6. Only needed for types that require address stability — most types should remain `Unpin`

# Construction / Recognition

## To Use PhantomPinned

1. Import `std::marker::PhantomPinned`
2. Add a field of type `PhantomPinned` to your struct (conventionally named `_pin` or `_pinned`)
3. The struct is now `!Unpin` and will be subject to pinning's restrictions when accessed through `Pin`
4. You will now need unsafe code to create a `Pin` pointer to your type (using `Pin::new_unchecked` or `Box::pin`)

## To Recognize PhantomPinned Usage

1. Look for a field of type `PhantomPinned` or `std::marker::PhantomPinned` in a struct definition
2. This signals that the struct author intentionally marked the type as address-sensitive

# Context & Application

`PhantomPinned` is typically used when implementing types that need address stability on stable Rust — most commonly when implementing `Future` by hand or building data structures with self-referential invariants. It is a declaration of intent: by including `PhantomPinned`, the author signals that the type has address-sensitive invariants that `Pin` must protect.

**Typical contexts:**

- Hand-implemented futures that contain self-referential state
- Custom async primitives
- Types wrapping raw pointers that point back into the same allocation
- Any type where the programmer needs to enforce that users cannot move it out of a `Pin`

# Examples

**Example 1** (Ch. 2, "Unpin" section): The source mentions `PhantomPinned` as one of two opt-out mechanisms: "You can opt-out by having a [`PhantomPinned`](https://doc.rust-lang.org/std/marker/struct.PhantomPinned.html) field or (if you're using nightly) with `impl !Unpin for ... {}`."

**Example 2** (constructed from source description): A typical usage pattern:

```rust
use std::marker::PhantomPinned;

struct MyFuture {
    state: u64,
    // This field makes MyFuture !Unpin
    _pin: PhantomPinned,
}
```

Note: The source does not provide a complete code example of `PhantomPinned` usage; this example is constructed from the source's description. The source only mentions `PhantomPinned` in the context of explaining how to opt out of `Unpin`.

# Relationships

## Builds Upon

- **unpin-trait** — `PhantomPinned` is the mechanism to opt out of `Unpin`
- **address-sensitivity** — `PhantomPinned` declares address sensitivity at the type level

## Enables

- **pin-type** — Types with `PhantomPinned` are the ones for which `Pin` enforces its guarantees
- **self-referential-type** — `PhantomPinned` enables safe self-referential types when combined with pinning

## Related

- **pinning** — `PhantomPinned` activates pinning's guarantees for a type

## Contrasts With

- (none)

# Common Errors

- **Error**: Adding `PhantomPinned` to a type without understanding the consequences — the type now requires pinning to be used in contexts that expect `Unpin`.
  **Correction**: Only add `PhantomPinned` if your type genuinely has address-sensitive invariants. Adding it unnecessarily makes the type harder to work with.

# Common Confusions

- **Confusion**: Thinking `PhantomPinned` prevents movement by itself.
  **Clarification**: `PhantomPinned` only makes the type `!Unpin`. Movement is prevented only when the type is accessed through a `Pin` pointer. Without `Pin`, an `!Unpin` type can still be moved freely.

- **Confusion**: Thinking `PhantomPinned` is needed for compiler-generated async futures.
  **Clarification**: The compiler automatically generates `!Unpin` futures when needed. `PhantomPinned` is for manually-written types that need to be `!Unpin`.

# Source Reference

Chapter 2: Pinning, section "Unpin," paragraph 3. The concept is mentioned briefly in the context of explaining how types opt out of `Unpin`.

# Verification Notes

- Definition source: Brief mention in Ch. 2, "Unpin" section, paragraph 3
- The source provides only a single sentence about `PhantomPinned` — it is mentioned as one of two opt-out mechanisms for `Unpin`
- The constructed code example is not from the source but illustrates the described usage pattern
- Confidence: MEDIUM — the source mentions `PhantomPinned` clearly but does not provide a detailed explanation or examples. The definition is unambiguous, but the card's fuller exposition draws on general Rust knowledge beyond what the source explicitly states.
- Cross-reference status: `unpin-trait`, `pinning`, `address-sensitivity`, `pin-type`, `self-referential-type` are planned cards
- Uncertainties: The source does not elaborate on `PhantomPinned` beyond the single mention; fuller properties are synthesized from the linked std docs reference and general Rust knowledge
