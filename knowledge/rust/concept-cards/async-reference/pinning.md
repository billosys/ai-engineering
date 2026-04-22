---
concept: Pinning
slug: pinning
category: memory-model
subcategory: safety-guarantees
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinning"
extraction_confidence: high
aliases:
  - "pinning (abstract concept)"
  - "pinned"
  - "being pinned"
prerequisites:
  - place
  - move-semantics
  - self-referential-type
  - address-sensitivity
extends: []
related:
  - pin-type
  - unpin-trait
  - phantom-pinned
  - pinning-values
  - structural-pinning
contrasts_with: []
answers_questions:
  - "What is pinning in Rust?"
  - "What must I understand before learning about Pin?"
  - "How does Unpin relate to Pin?"
---

# Quick Definition

Pinning is a guarantee that an object will not be moved or otherwise invalidated until it is dropped. Unlike borrowing (which temporarily prevents moves), pinning is permanent: once an object is pinned, it must remain pinned for the rest of its lifetime.

# Core Definition

"An object is pinned if it will not be moved or otherwise invalidated. As I explained above, this is not a new concept - borrowing an object prevents the object being moved for the duration of the borrow. Whether an object can be moved or not is not explicit in Rust's types, though it is known by the compiler (which is why you can get 'cannot move out of' error messages). As opposed to borrowing (and the temporary restriction on moves caused by borrowing), being pinned is permanent. An object can change from being not pinned to being pinned, but once it is pinned then it must remain pinned until it is dropped." (Async Reference, Ch. 2: Pinning, "Pinning" section)

The source emphasizes that this is an abstract concept: "I'm going to start by discussing an abstract concept of pinning, which is not exactly what is expressed by any particular type. We'll make the concept more concrete as we go on, and end up with precise definitions of what different types mean, but none of these types mean exactly the same as the pinning concept we'll start with." (Async Reference, Ch. 2: Pinning, "Pinning" section)

# Prerequisites

- **Place** — Pinning is a property of a value's place: the guarantee that the value will remain at that place
- **Move semantics** — Pinning exists because moves change addresses, which breaks address-sensitive types
- **Self-referential type** — Self-referential types are the primary motivation for pinning
- **Address sensitivity** — Pinning is a contract about validity for address-sensitive types; without understanding address sensitivity, pinning's purpose is unclear

# Key Properties

1. Pinning guarantees an object will not be moved or invalidated until dropped
2. Pinning is permanent: once pinned, always pinned (until drop)
3. Pinning is a one-way transition: unpinned -> pinned, but never pinned -> unpinned
4. Pinning is not built-in to the language or compiler; it works by restricting access to mutable references
5. Pinning is a property of the pointed-to place, not of the pointer itself
6. Pinning is orthogonal to mutability: an object can be mutable and pinned, mutable and not pinned, immutable and pinned, or immutable and not pinned
7. Pinning was not part of Rust until after 1.0; for backwards compatibility, there is no way to express whether an object is pinned — only that a reference points to a pinned object
8. Pinning is actually "a contract about validity, not about moving" — it guarantees address-sensitive objects maintain valid addresses
9. For `Unpin` types, pinning has no practical effect

# Construction / Recognition

## When Pinning Is Needed

1. When implementing or directly polling a `Future` (since `Future::poll` requires `Pin<&mut Self>`)
2. When using futures by reference with `select` or similar combinators
3. When manually calling `poll` on a future
4. When working with any `!Unpin` type that has address-sensitive invariants

## How Pinning Works (Conceptually)

1. An object starts unpinned and may be freely moved
2. A pinning pointer (e.g., `Pin<Box<T>>`, `Pin<&mut T>`) is created pointing to the object
3. The pinning pointer restricts access: it will not hand out `&mut T` that would allow moving the pointee
4. The object is now pinned and must remain at its current address until dropped
5. It is possible to break pinning in unsafe code, but the programmer bears responsibility for not doing so

# Context & Application

Pinning is key to the implementation of async programming in Rust. Async functions compile into self-referential state machines (futures), and pinning guarantees these futures won't be moved while their internal references are live. The `Future::poll` signature requires `Pin<&mut Self>` specifically to enforce this guarantee.

**Typical contexts:**

- Async/await implementation: futures are pinned when polled
- The `pin!` macro for stack-pinning references to futures
- `Box::pin` for heap-pinning objects
- Any API that works with `!Unpin` types

**Important design context:** "pinning is a low-level building block designed specifically for the implementation of async Rust. Although it is not directly tied to async Rust and can be used for other purposes, it was not designed to be a general-purpose mechanism." (Ch. 2, footnote 1)

# Examples

**Example 1** (Ch. 2, "Pinning" section): Pinning is reflected in pointer types: "`Pin<Box<T>>` is a pointer to an owned, pinned object and `Pin<&mut T>` is a pointer to a uniquely borrowed, mutable, pinned object (c.f., `&mut T` which is a pointer to a uniquely borrowed, mutable, object which may or may not be pinned)."

**Example 2** (Ch. 2, "Pinning" section): Pinning is orthogonal to mutability. The source lists four combinations:
- `Pin<&mut T>`: mutable and pinned
- `&mut T`: mutable and not pinned
- `Pin<&T>`: immutable and pinned
- `&T`: immutable and not pinned (but NOT pinned — its immovability from borrowing is only temporary)

**Example 3** (Ch. 2, "TL;DR" section): "`Pin` marks a pointer as pointing to an object which will not move until it is dropped. Pinning is not built-in to the language or compiler; it works by simply restricting access to mutable references to the pointee."

# Relationships

## Builds Upon

- **place** — Pinning is a guarantee about a value's place
- **move-semantics** — Pinning prevents the problematic effects of moves
- **self-referential-type** — The primary motivation for pinning
- **address-sensitivity** — Pinning protects address-sensitive types

## Enables

- **pin-type** — The concrete `Pin<P>` wrapper that implements the pinning guarantee
- **pinning-values** — Practical mechanisms for pinning objects (stack vs heap pinning)
- **structural-pinning** — Rules for accessing fields of pinned objects

## Related

- **unpin-trait** — Determines whether pinning has practical effect on a type
- **phantom-pinned** — Marker type to opt types out of `Unpin`
- **pin-and-async** — How pinning integrates with async programming

## Contrasts With

- (none — borrowing provides temporary immobility, but is not extracted as a separate card here)

# Common Errors

- **Error**: Attempting to get `&mut T` from `Pin<&mut T>` for an `!Unpin` type to move the value.
  **Correction**: `Pin` deliberately restricts access to `&mut T` for `!Unpin` types. Use pin-projection methods to access individual fields safely.

# Common Confusions

- **Confusion**: Thinking that pinning prevents ALL movement, including for `Unpin` types.
  **Clarification**: Pinning only prevents movement for `!Unpin` (address-sensitive) types. For `Unpin` types, `Pin` has no practical effect and pinned/unpinned pointers can be freely interconverted.

- **Confusion**: Thinking that `&T` (shared reference) means the object is pinned because it can't be moved.
  **Clarification**: `&T` prevents movement only temporarily (for the duration of the borrow). Pinning is permanent — once pinned, an object stays pinned until drop. Temporary immobility from borrowing is not pinning.

- **Confusion**: Thinking pinning is a built-in language feature.
  **Clarification**: Pinning is implemented entirely in the type system via the `Pin` wrapper and the `Unpin` trait. It is not a compiler built-in; it works by restricting access to mutable references.

# Source Reference

Chapter 2: Pinning, sections "TL;DR" (full), "Pinning" (full), and "Unpin" (paragraphs 1-2 for the validity vs. movement clarification). Also footnotes on permanence and design intent.

# Verification Notes

- Definition source: Direct quotation from Ch. 2, "Pinning" section, paragraph 2
- Abstract concept note: Direct quotation from Ch. 2, "Pinning" section, paragraph 1
- Orthogonality with mutability: Directly from source, paragraph 5 of "Pinning" section
- Validity vs. movement: Directly from "Unpin" section
- Confidence: HIGH — the source devotes an entire section to carefully defining the abstract concept of pinning with extensive explanation
- Cross-reference status: `place`, `move-semantics`, `self-referential-type`, `address-sensitivity`, `pin-type`, `unpin-trait`, `phantom-pinned`, `pinning-values`, `structural-pinning`, `pin-and-async` are planned or expected cards
- Uncertainties: None
