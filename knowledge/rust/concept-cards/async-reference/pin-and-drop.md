---
concept: Pin and Drop
slug: pin-and-drop
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinning and Drop"
extraction_confidence: high
aliases:
  - "pinning drop guarantee"
  - "drop guarantee"
  - "Pin Drop interaction"
prerequisites:
  - pin-type
  - pinning
  - unpin-trait
extends:
  - pin-type
related:
  - pinned-self
  - structural-pinning
  - async-drop
contrasts_with: []
answers_questions:
  - "How does Drop interact with pinning?"
  - "How do I implement Drop for a pinned type?"
  - "What is the drop guarantee for pinned types?"
---

# Quick Definition

The pinning contract holds until the pinned object's `drop` method returns. For `!Unpin` types, the `Drop` implementation must treat `&mut self` as if it were `Pin<&mut Self>`, maintaining the object's validity throughout the drop process.

# Core Definition

"The pinning contract applies until the pinned object is dropped (technically, that means when its `drop` method returns, not when it is called)." (Ch. 2, "Pinning and Drop")

"If you are implementing an address-sensitive type (i.e., one that is `!Unpin`), then you must take extra care with the `Drop` implementation. Even though the self-type in `drop` is `&mut Self`, you must treat the self-type as `Pin<&mut Self>`. In other words, you must ensure the object remains valid until the `drop` function returns." (Ch. 2, "Pinning and Drop")

For manual lifecycle management: "If you have an object which is (or might be) pinned and that object is not `Unpin`, then you must call its `drop` method (using `drop_in_place`) before deallocating or reusing the object's memory or address." (Ch. 2, "Pinning and Drop")

# Prerequisites

- **Pin type** — Must understand `Pin<Ptr>` to understand what guarantees it provides through drop
- **Pinning** — The pinning contract is what defines the scope of the drop guarantee
- **Unpin trait** — The drop guarantee only has practical implications for `!Unpin` types

# Key Properties

1. The pinning contract holds from the moment of pinning until the `drop` method **returns** (not when it is called)
2. `Drop::drop` takes `&mut self`, not `Pin<&mut Self>` — this is a language limitation for backwards compatibility
3. For `!Unpin` types, the `Drop` implementation must treat `&mut self` as though it were `Pin<&mut Self>`
4. The object must remain valid at its address throughout the entire `drop` execution
5. Memory must not be deallocated or reused before `drop` has been called (when managing lifecycles manually)
6. `drop_in_place` must be used before deallocating memory of a potentially pinned `!Unpin` object
7. The drop guarantee requires special compiler treatment because `Drop::drop` predates pinning

# Construction / Recognition

## To Implement Drop for a !Unpin Type

1. Implement `Drop` for your type as usual with `fn drop(&mut self)`
2. Inside `drop`, wrap `self` in a `Pin` using `unsafe { Pin::new_unchecked(self) }`
3. Delegate to an inner function that takes `Pin<&mut Self>` to make the pinned contract explicit
4. Ensure no code in the drop path moves any structurally pinned fields
5. Ensure the object remains valid at its address until `drop` returns

## Recommended Idiom

```rust
impl Drop for Type {
    fn drop(&mut self) {
        // `new_unchecked` is okay because we know this value is never used
        // again after being dropped.
        inner_drop(unsafe { Pin::new_unchecked(self)});

        fn inner_drop(this: Pin<&mut Self>) {
            // Actual drop code goes here.
        }
    }
}
```

# Context & Application

The interaction between `Pin` and `Drop` is one of the subtlest aspects of the pinning system. It arises because `Drop` was designed before pinning existed, so its signature uses `&mut self` rather than `Pin<&mut Self>`. This creates a soundness gap that must be closed by the programmer when implementing `Drop` for `!Unpin` types.

This is particularly relevant when implementing custom futures (which are typically `!Unpin` due to self-references), intrusive data structures, or any type that relies on address stability. The source notes that "ensuring correctness here is likely to be interesting!" — particularly when multiple pinned objects interact (e.g., intrusive linked lists).

# Examples

**The recommended Drop idiom** (Ch. 2, "Pinning and Drop"):
```rust
impl Drop for Type {
    fn drop(&mut self) {
        inner_drop(unsafe { Pin::new_unchecked(self)});

        fn inner_drop(this: Pin<&mut Self>) {
            // Actual drop code goes here.
        }
    }
}
```

**Manual lifecycle management** (Ch. 2, "Pinning and Drop"):
> "If you have an object which is (or might be) pinned and that object is not `Unpin`, then you must call its `drop` method (using `drop_in_place`) before deallocating or reusing the object's memory or address."

# Relationships

## Builds Upon
- **Pin type** — The drop guarantee is part of Pin's contract
- **Pinning** — Drop terminates the pinning contract

## Enables
- **Structural pinning** — Structurally pinned fields must be dropped before they are moved, even during panics
- **Async drop** — Understanding Pin-and-Drop is prerequisite to understanding async drop challenges

## Related
- **Pinned self** — Drop's `&mut self` vs the logical `Pin<&mut Self>` is directly related to method self-type choices
- **Self-referential type** — Self-referential types are the primary motivation for careful `Drop` with pinning

## Contrasts With
(none)

# Common Errors

- **Error**: Moving a structurally pinned field inside `Drop::drop`.
  **Correction**: Even though `drop` receives `&mut self`, you must not move pinned fields. Wrap `self` in `Pin` and respect the pinning contract.

- **Error**: Deallocating memory of a pinned `!Unpin` object without calling `drop_in_place` first.
  **Correction**: The pinning contract requires the object's destructor to run before its memory is reclaimed or reused. Always call `drop_in_place` before deallocation.

# Common Confusions

- **Confusion**: Believing the pinning contract ends when `drop` is called.
  **Clarification**: The contract holds until `drop` **returns**. The object must remain valid at its address throughout the entire drop execution.

- **Confusion**: Thinking that `&mut self` in `Drop::drop` means you have full `&mut` freedoms for a pinned type.
  **Clarification**: For `!Unpin` types, `drop` receives `&mut self` only due to a language limitation. You must treat it as `Pin<&mut Self>` and must not violate pinning invariants.

# Source Reference

Chapter 2: Pinning, section "Pinning and Drop." See the std docs reference for the drop guarantee.

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pinning and Drop" section (lines 171-191 of source)
- Confidence rationale: HIGH — the source provides explicit rules, a recommended code idiom, and clear safety requirements
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, unpin-trait) and Agent C concepts (async-drop)
