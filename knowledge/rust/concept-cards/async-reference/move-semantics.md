---
concept: Move Semantics
slug: move-semantics
category: memory-model
subcategory: ownership
tier: foundational
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Move semantics"
extraction_confidence: high
aliases:
  - "move"
  - "moving data"
  - "Rust moves"
prerequisites:
  - place
extends: []
related:
  - self-referential-type
  - pinning
  - address-sensitivity
contrasts_with: []
answers_questions:
  - "What is move semantics in Rust?"
  - "How does move semantics relate to self-referential types?"
  - "What must I understand before learning about Pin?"
---

# Quick Definition

Assignment in Rust moves data from one place to another, transferring the value's memory location so it exists only at the destination. After a move, pointers to the original location become invalid, which is why borrowed references prevent moves.

# Core Definition

"Assignment in Rust *moves* data (mostly, some simple data has copy semantics, but that doesn't matter too much). When we write `let b = a;`, the data that was in memory at a place identified by `a` is moved to the place identified by `b`. That means that after the assignment, the data exists at `b` but no longer exists at `a`. Or in other words, the address of the object is changed by the assignment." (Async Reference, Ch. 2: Pinning, "Move semantics" section)

"Abstractly, a move is implemented by copying the bits from the origin to the destination and then erasing the origin bits. However, the compiler can optimise this is many ways." (Async Reference, Ch. 2: Pinning, footnote)

# Prerequisites

- **Place** — Moves are defined as data transferring between places; understanding what a place is (a chunk of memory with an address) is essential to understanding what it means for data to move.

# Key Properties

1. Assignment (`let b = a;`) moves data from the source place to the destination place
2. After a move, the data no longer exists at the source place
3. The address of the moved object changes as a result of the move
4. If pointers existed to the source place, they become invalid after the move
5. Borrowed references prevent moving: `let r = &a; let b = a;` is illegal because `r` points at `a`'s place
6. Types implementing `Copy` have copy semantics instead of move semantics (but this is a minor exception)
7. Moving is not limited to variable assignment — data can be moved out of `Box` (heap to stack) and via `std::mem::take`, `replace`, and `swap` (out of `&mut T`)
8. Moving out of a `Box` leaves the pointed-to place invalid; moving out of a mutable reference leaves the place valid but containing different data

# Construction / Recognition

## To Recognize a Move

1. Look for assignment between non-`Copy` types: `let b = a;`
2. Look for passing a value to a function: `foo(a)` moves `a` into the function parameter
3. Look for returning a value from a function
4. Look for dereferencing a `Box` to move heap data to the stack
5. Look for `std::mem::take`, `std::mem::replace`, or `std::mem::swap` — these move data out of mutable references

## To Understand Why a Move Is Blocked

1. Check if there are any active borrows of the source value
2. The compiler prevents moves when references to the source place exist
3. The compiler only tracks references from outside an object — internal (self-referential) references are invisible to the compiler

# Context & Application

Move semantics are central to Rust's ownership model and are the key motivation for pinning. Because moves change the address of an object, any internal pointers (self-references) within the object would become dangling after a move. The compiler cannot detect or prevent this because self-references are invisible to the borrow checker. This is why pinning was introduced: to guarantee that certain objects will not be moved, making self-referential structures (like async futures) safe.

**Typical contexts:**

- Ownership transfer between variables, function arguments, and return values
- Understanding why self-referential types are unsound without pinning
- Understanding the motivation for `Pin<P>` in async Rust

# Examples

**Example 1** (Ch. 2, "Move semantics" section): `let b = a;` — data moves from `a`'s place to `b`'s place. After this, `a` is no longer valid.

**Example 2** (Ch. 2, "Move semantics" section): `let r = &a; let b = a;` — this is illegal. The existence of `r` (a reference to `a`'s place) prevents `a` from being moved.

**Example 3** (Ch. 2, "Move semantics" section): The hypothetical `Bad` struct illustrates why moves are dangerous for self-referential types:

```rust,norun
struct Bad {
    field: u64,
    r: &'self u64,
}
```

If `b.r` points to `b.field` and we move `b` to `a` with `let a = b;`, then `a.r` would still point to the old location of `b.field` — now invalid memory.

**Example 4** (Ch. 2, "Move semantics" section): `std::mem::take`, `replace`, and `swap` move data out of a mutable reference (`&mut T`), showing that moves are not limited to variable assignment.

# Relationships

## Builds Upon

- **place** — Moves are defined as transferring data between places

## Enables

- **self-referential-type** — Understanding why self-referential types are broken by moves
- **pinning** — Pinning exists to prevent moves for address-sensitive types
- **address-sensitivity** — The concept that some types break when their address changes

## Related

- **pinning** — Pinning is the solution to the problem that moves create for self-referential types
- **self-referential-type** — The primary example of types that are broken by moves

## Contrasts With

- (none — copy semantics is the exception but not extracted as a separate card here)

# Common Errors

- **Error**: Attempting to use a value after it has been moved (e.g., using `a` after `let b = a;`).
  **Correction**: After a move, the source is no longer valid. The compiler will reject this with a "use of moved value" error.

- **Error**: Assuming that moving a self-referential struct is safe because the internal reference "moves with it."
  **Correction**: Internal references store absolute addresses, not relative offsets. After a move, the internal reference still points to the old memory location, which is now invalid.

# Common Confusions

- **Confusion**: Thinking that a move is the same as a copy.
  **Clarification**: A move transfers ownership — the source becomes invalid. A copy (for `Copy` types) duplicates the data, leaving both source and destination valid.

- **Confusion**: Believing the compiler can detect and fix internal (self-referential) pointers during moves.
  **Clarification**: The compiler only knows about references from outside an object into it. Self-references within an object are invisible to the compiler, which is why they are unsound without pinning.

# Source Reference

Chapter 2: Pinning, section "Move semantics," full section including footnotes.

# Verification Notes

- Definition source: Direct quotation from Ch. 2, "Move semantics" section, paragraph 4
- Implementation detail: Direct quotation from footnote at end of "Move semantics" section
- The `Bad` struct example: Directly from source, lines 36-40
- Confidence: HIGH — the source provides a thorough, explicitly structured explanation of move semantics
- Cross-reference status: `place`, `self-referential-type`, `pinning`, `address-sensitivity` are planned cards in this batch
- Uncertainties: None
