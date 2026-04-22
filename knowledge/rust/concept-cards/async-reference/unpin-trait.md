---
concept: Unpin Trait
slug: unpin-trait
category: type-system
subcategory: marker-traits
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
  - "Unpin"
  - "!Unpin"
  - "std::marker::Unpin"
prerequisites:
  - place
  - move-semantics
  - address-sensitivity
  - pinning
extends: []
related:
  - pin-type
  - phantom-pinned
  - self-referential-type
contrasts_with: []
answers_questions:
  - "What is the Unpin trait?"
  - "How does Unpin relate to Pin?"
  - "What is the difference between Unpin and !Unpin types?"
---

# Quick Definition

`Unpin` is an auto-trait that indicates a type is not address-sensitive and can be safely moved even when pinned. Most types implement `Unpin` automatically; for such types, `Pin` has no practical effect.

# Core Definition

"`Unpin` is a trait which expresses whether objects are address-sensitive. If an object implements `Unpin`, then it is *not* address-sensitive. If an object is `!Unpin` then it is address-sensitive. Alternatively, if we think of pinning as the act of holding an object in its place, then `Unpin` means it is safe to undo that action and allow the object to be moved." (Async Reference, Ch. 2: Pinning, "Unpin" section)

"`Unpin` is an auto-trait and most types are `Unpin`. Only types which have an `!Unpin` field or which explicitly opt-out are not `Unpin`. You can opt-out by having a `PhantomPinned` field or (if you're using nightly) with `impl !Unpin for ... {}`." (Async Reference, Ch. 2: Pinning, "Unpin" section)

# Prerequisites

- **Place** — `Unpin` expresses whether a type depends on its place's address
- **Move semantics** — `Unpin` determines whether moves are safe for a type even under pinning
- **Address sensitivity** — `Unpin` is the type-level encoding of address sensitivity (or its absence)
- **Pinning** — `Unpin` only has meaning in the context of pinning; it determines whether `Pin` has practical effect

# Key Properties

1. `Unpin` is an auto-trait: the compiler automatically implements it for types where all fields are `Unpin`
2. Most types in Rust are `Unpin`
3. A type is `!Unpin` only if it has an `!Unpin` field or explicitly opts out
4. Opt-out mechanisms: include a `PhantomPinned` field, or (on nightly) use `impl !Unpin for T {}`
5. For `Unpin` types, `Pin` essentially does nothing — `Pin<Box<T>>` and `Pin<&mut T>` behave like `Box<T>` and `&mut T`
6. For `Unpin` types, pinned and regular pointers can be freely interconverted via `Pin::new` and `Pin::into_inner`
7. `Pin<...>` does NOT guarantee the pointee won't move — only that it won't move IF it is `!Unpin`
8. `Unpin` should not be understood as a standalone property — it only affects how an object interacts with `Pin`
9. Using an `Unpin` bound outside the pinning context has no effect on compiler behavior

# Construction / Recognition

## To Determine if a Type is Unpin

1. Check if all of its fields implement `Unpin` — if so, it is automatically `Unpin`
2. Check for `PhantomPinned` fields — these make the type `!Unpin`
3. Check for explicit `impl !Unpin` (nightly only)
4. Compiler-generated async futures are typically `!Unpin` when they contain self-referential state

## Practical Impact

1. If your type is `Unpin`: you can ignore all pinning complications. `Pin<&mut T>` works just like `&mut T`.
2. If your type is `!Unpin`: you must respect pinning guarantees. Getting `&mut T` from `Pin<&mut T>` requires unsafe code and careful reasoning.

# Context & Application

`Unpin` is the "escape hatch" that makes pinning ergonomic for the common case. Since most types are `Unpin`, most code does not need to worry about pinning at all. Only when working with `!Unpin` types (primarily async futures) do pinning's restrictions and requirements come into play.

**Typical contexts:**

- Generic async code using `Unpin` bounds to ensure ease of use (e.g., `T: Future + Unpin`)
- Determining whether a type can be used with `pin!` or must be heap-pinned
- Understanding why some futures require pinning and others don't

**Key insight from source:** "The only reason to use `Unpin` is in conjunction with pinning, or to propagate the bound to where it is used with pinning." (Ch. 2, "Unpin" section)

# Examples

**Example 1** (Ch. 2, "Unpin" section): For `Unpin` types, `Pin` is transparent: "For types which implement `Unpin`, `Pin` essentially does nothing. `Pin<Box<T>>` and `Pin<&mut T>` can be used just like `Box<T>` and `&mut T`. In fact, for `Unpin` types, the `Pin`ed and regular pointers can be freely-interconverted using `Pin::new` and `Pin::into_inner`."

**Example 2** (Ch. 2, "Unpin" section): Opting out of `Unpin`: "You can opt-out by having a `PhantomPinned` field or (if you're using nightly) with `impl !Unpin for ... {}`."

**Example 3** (Ch. 2, "Unpin" section): The practical implication: "working with `Unpin` types and pinning is much easier than with types which are not `Unpin`, in fact the `Pin` marker has basically no effect on `Unpin` types and pointers to `Unpin` types, and you can basically ignore all the pinning guarantees and requirements."

# Relationships

## Builds Upon

- **pinning** — `Unpin` exists solely in the context of pinning
- **address-sensitivity** — `Unpin` is the type-level encoding of "not address-sensitive"

## Enables

- **pin-type** — `Unpin` determines whether `Pin` has practical restrictions on a type
- **phantom-pinned** — `PhantomPinned` is the mechanism to opt out of `Unpin`

## Related

- **self-referential-type** — Self-referential types are typically `!Unpin`
- **pin-type** — `Unpin` determines whether `Pin` behaves like a regular pointer wrapper or enforces pinning

## Contrasts With

- (none — `!Unpin` is the negation but not a separate trait)

# Common Errors

- **Error**: Adding an `Unpin` bound to a generic parameter outside of any pinning context, expecting it to have some effect.
  **Correction**: `Unpin` only changes behavior in conjunction with `Pin`. Outside pinning contexts, it has no effect on compilation or runtime behavior.

- **Error**: Assuming a type is `!Unpin` because it "shouldn't be moved."
  **Correction**: `Unpin` is automatically implemented based on fields. A type is `!Unpin` only if it contains an `!Unpin` field or explicitly opts out. Most custom types are `Unpin`.

# Common Confusions

- **Confusion**: Thinking `Unpin` means "can be unpinned" (i.e., a pinned object can transition back to unpinned).
  **Clarification**: `Unpin` means "address-insensitive." For `Unpin` types, `Pin` has no effect, so the concept of "unpinning" doesn't apply — they were never meaningfully pinned. The name is misleading; think of it as "pinning doesn't matter for this type."

- **Confusion**: Thinking `Pin` guarantees no movement for all types.
  **Clarification**: `Pin<...>` only guarantees non-movement for `!Unpin` types. For `Unpin` types, the pointee can be moved freely even through a `Pin` pointer.

- **Confusion**: Thinking `Unpin` is a general-purpose trait with meaning outside of pinning.
  **Clarification**: "`Unpin` should not be understood as a property of an object alone; the only thing `Unpin` changes is how an object interacts with `Pin`."

# Source Reference

Chapter 2: Pinning, section "Unpin," full section (paragraphs 1-5).

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Unpin" section, paragraphs 2-3
- Auto-trait and opt-out mechanisms: Directly quoted from paragraph 3
- Practical implications: Directly quoted from paragraphs 4-5
- Confidence: HIGH — the source provides an explicit, multi-paragraph definition of `Unpin` with practical guidance
- Cross-reference status: `place`, `move-semantics`, `address-sensitivity`, `pinning`, `pin-type`, `phantom-pinned`, `self-referential-type` are planned or expected cards
- Uncertainties: None
