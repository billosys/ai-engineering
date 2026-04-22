---
concept: Address Sensitivity
slug: address-sensitivity
category: memory-model
subcategory: type-properties
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Unpin"
extraction_confidence: high
aliases:
  - "address-sensitive"
  - "address-sensitive type"
  - "!Unpin"
prerequisites:
  - place
  - move-semantics
  - self-referential-type
extends: []
related:
  - pinning
  - unpin-trait
  - phantom-pinned
  - pin-type
contrasts_with: []
answers_questions:
  - "What is address sensitivity?"
  - "What is the difference between Unpin and !Unpin types?"
  - "How does Unpin relate to Pin?"
---

# Quick Definition

An object is address-sensitive if its correctness depends on its memory address not changing. Self-referential types are the primary example: their internal pointers encode absolute addresses that become invalid if the object moves. In Rust, `!Unpin` types are address-sensitive.

# Core Definition

"Pinning is actually a contract about validity, not about moving. It guarantees that *if an object is address-sensitive, then* its address will not change (and thus addresses derived from it, such as the addresses of its fields, will not change either). Most data in Rust is not address-sensitive. It can be moved around and everything will be ok. `Pin` guarantees that the pointee will be valid with respect to it's address. If the pointee is address-sensitive, then it can't be moved; if it's not address-sensitive, then it doesn't matter whether it is moved." (Async Reference, Ch. 2: Pinning, "Unpin" section)

"`Unpin` is a trait which expresses whether objects are address-sensitive. If an object implements `Unpin`, then it is *not* address-sensitive. If an object is `!Unpin` then it is address-sensitive." (Async Reference, Ch. 2: Pinning, "Unpin" section)

# Prerequisites

- **Place** — Address sensitivity is about whether an object depends on the address of its place
- **Move semantics** — Moves change the address of an object, which is what makes address sensitivity a problem
- **Self-referential type** — Self-referential types are the primary example of address-sensitive types, since their internal references encode absolute addresses

# Key Properties

1. An address-sensitive object's correctness depends on its memory address remaining stable
2. Moving an address-sensitive object invalidates it (internal pointers become dangling)
3. Most types in Rust are NOT address-sensitive — they can be freely moved
4. Address sensitivity is expressed in Rust's type system via the `Unpin` trait: `!Unpin` means address-sensitive, `Unpin` means not address-sensitive
5. `Pin` only has practical effect on address-sensitive (`!Unpin`) types — for `Unpin` types, `Pin` does nothing
6. Addresses derived from an address-sensitive object (such as field addresses) must also remain stable

# Construction / Recognition

## To Recognize an Address-Sensitive Type

1. Check if the type is `!Unpin` — this is the type-level marker for address sensitivity
2. Look for internal self-references or raw pointers to the type's own fields
3. Compiler-generated async futures are typically `!Unpin` when they contain cross-references between local variables
4. Types containing a `PhantomPinned` field are `!Unpin` by design

## What Makes a Type Address-Sensitive

1. The type contains self-referential pointers (raw pointers from one field to another)
2. The type has been explicitly marked `!Unpin` via `PhantomPinned` or `impl !Unpin`
3. The type contains a field that is itself `!Unpin` (the `!Unpin` property propagates)

# Context & Application

Address sensitivity is the conceptual bridge between the problem (self-referential types are broken by moves) and the solution (pinning). Pinning guarantees that address-sensitive objects will not be moved. The `Unpin`/`!Unpin` distinction tells the pinning system which types actually need this guarantee and which can safely ignore it.

**Typical contexts:**

- Understanding what `Pin` actually guarantees (validity with respect to address, not immobility per se)
- Determining whether a type needs pinning (only if it is `!Unpin` / address-sensitive)
- Understanding why `Pin` has no practical effect on `Unpin` types

# Examples

**Example 1** (Ch. 2, "Unpin" section): Most data in Rust is not address-sensitive — "It can be moved around and everything will be ok." For these types, `Pin` has no practical effect.

**Example 2** (Ch. 2, "Unpin" section): An address-sensitive type (one that is `!Unpin`) cannot be moved when pinned: "`Pin` guarantees that the pointee will be valid with respect to it's address. If the pointee is address-sensitive, then it can't be moved."

**Example 3** (Ch. 2, "Unpin" section): For `Unpin` types, `Pin` is transparent: "`Pin<Box<T>>` and `Pin<&mut T>` can be used just like `Box<T>` and `&mut T>`." The pinned and regular pointers "can be freely-interconverted using `Pin::new` and `Pin::into_inner`."

# Relationships

## Builds Upon

- **place** — Address sensitivity concerns whether the place's address matters
- **move-semantics** — Moves are what change addresses and thus break address-sensitive types
- **self-referential-type** — Self-referential types are the primary example of address-sensitive types

## Enables

- **pinning** — Pinning exists to protect address-sensitive types
- **unpin-trait** — `Unpin` is the type-level expression of whether a type is address-sensitive

## Related

- **phantom-pinned** — A marker type used to make types address-sensitive (`!Unpin`)
- **pin-type** — The wrapper type that enforces the address-stability guarantee

## Contrasts With

- (none)

# Common Errors

- **Error**: Assuming that `Pin` prevents all movement of the pointee.
  **Correction**: `Pin` only prevents movement of `!Unpin` (address-sensitive) types. `Unpin` types can be freely moved even when behind a `Pin`.

# Common Confusions

- **Confusion**: Thinking that pinning is about immobility rather than validity.
  **Clarification**: "Pinning is actually a contract about validity, not about moving." It guarantees that if an object is address-sensitive, its address will not change. For non-address-sensitive types, pinning imposes no movement restriction.

- **Confusion**: Conflating address sensitivity with immutability.
  **Clarification**: Address sensitivity is orthogonal to mutability. An address-sensitive object can still be mutated (its fields changed); what must not change is its memory address (the place where it lives).

# Source Reference

Chapter 2: Pinning, section "Unpin," paragraphs 1-3.

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Unpin" section, paragraphs 2-3
- The relationship between `Unpin` and address sensitivity: Directly quoted from source
- Confidence: HIGH — the source explicitly defines address sensitivity and its relationship to `Unpin` and `Pin`
- Cross-reference status: `place`, `move-semantics`, `self-referential-type`, `pinning`, `unpin-trait`, `phantom-pinned`, `pin-type` are planned cards
- Uncertainties: None
