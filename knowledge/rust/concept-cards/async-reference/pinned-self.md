---
concept: Pinned Self
slug: pinned-self
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinned self in methods"
extraction_confidence: high
aliases:
  - "Pin<&mut Self>"
  - "pinned self type"
  - "self: Pin<&mut Self>"
prerequisites:
  - pin-type
  - pinning
  - unpin-trait
extends:
  - pin-type
related:
  - pin-and-drop
  - structural-pinning
  - future-poll-signature
contrasts_with: []
answers_questions:
  - "How do I use Pin<&mut Self> in method signatures?"
  - "When should I use &mut self vs self: Pin<&mut Self>?"
  - "What is the phased model of pinning as it relates to method signatures?"
---

# Quick Definition

Methods on pinned types choose between `&mut self` (callable before pinning) and `self: Pin<&mut Self>` (callable after pinning), reflecting pinning's phased nature where objects start unpinned and become pinned at some point during their lifetime.

# Core Definition

"If the method does not need to mutate `self`, then you can still use `&self` since `Pin<...>` can dereference to a borrowed reference. However, if you need to mutate `self` (and your type is not `Unpin`) then you need to choose between `&mut self` and `self: Pin<&mut Self>`." (Ch. 2, "Pinned self in methods")

"Using `&mut self` makes the implementation easy, but means the method cannot be called on a pinned object. Using `self: Pin<&mut Self>` means considering pin projection (see the next section) and can only be called on a pinned object." (Ch. 2, "Pinned self in methods")

The source provides an intuitive framing: "pinning is a phased concept - objects start unpinned, and at some point undergo a phase change to become pinned. `&mut self` methods are ones which can be called in the first (unpinned) phase and `self: Pin<&mut Self>` methods are ones which can be called in the second (pinned) phase." (Ch. 2, "Pinned self in methods")

# Prerequisites

- **Pin type** — Must understand `Pin<Ptr>` to understand why `Pin<&mut Self>` restricts access
- **Pinning** — The phased nature of pinning drives the choice between self-types
- **Unpin trait** — For `Unpin` types, the choice between `&mut self` and `Pin<&mut Self>` is less consequential

# Key Properties

1. `&self` methods work on pinned types via `Deref` — no special consideration needed
2. For mutable methods on `!Unpin` types, the choice is between `&mut self` and `self: Pin<&mut Self>`
3. `&mut self` methods: easy to implement, callable only in the unpinned phase
4. `self: Pin<&mut Self>` methods: require pin projection for field access, callable only in the pinned phase
5. Pinned pointers cannot be implicitly coerced to `Pin<&mut Self>`, but can be converted via `Pin::as_mut`
6. `drop` takes `&mut self` due to a language limitation, even though it may be called in the pinned phase
7. The self-type choice represents a design decision about which lifecycle phase the method belongs to

# Construction / Recognition

## To Decide the Self-Type for a Method

1. If the method only reads from `self`: use `&self` (works in both phases via `Deref`)
2. If the method mutates `self` and is called before pinning (e.g., configuration): use `&mut self`
3. If the method mutates `self` and is called after pinning (e.g., polling): use `self: Pin<&mut Self>`
4. If the type is `Unpin`: the choice matters less since `Pin` has no practical effect

## To Call a Pinned Method

1. If you have `Pin<Box<T>>`, convert to `Pin<&mut T>` via `Pin::as_mut()`
2. Call the method on the resulting `Pin<&mut T>`
3. If calling the method multiple times, call `as_mut()` each time (no implicit reborrowing)

# Context & Application

The pinned self-type is encountered most commonly when implementing the `Future` trait, where `poll` takes `self: Pin<&mut Self>`. This design reflects that futures are polled after they have been pinned (placed in an executor). Any method that needs to operate on a future's internal state after pinning must use `Pin<&mut Self>` and work through pin projection to access fields.

The phased model helps reason about API design: methods for building or configuring an object before it is pinned use `&mut self`, while methods for operating on the object after it is pinned use `self: Pin<&mut Self>`.

# Examples

**Using `as_mut` for reborrowing** (Ch. 2, "Using pinned types"):
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

**The phase model** (Ch. 2, "Pinned self in methods"):
> "pinning is a phased concept - objects start unpinned, and at some point undergo a phase change to become pinned. `&mut self` methods are ones which can be called in the first (unpinned) phase and `self: Pin<&mut Self>` methods are ones which can be called in the second (pinned) phase."

# Relationships

## Builds Upon
- **Pin type** — `Pin<&mut Self>` is a specific instantiation of `Pin<Ptr>`

## Enables
- **Structural pinning** — Accessing fields from `Pin<&mut Self>` requires pin projection
- **Future poll signature** — `Future::poll` uses `self: Pin<&mut Self>`

## Related
- **Pin and drop** — `Drop::drop` takes `&mut self` even when logically operating in the pinned phase, a known language limitation

## Contrasts With
(none)

# Common Errors

- **Error**: Expecting `Pin<Box<T>>` to be implicitly coercible to `self: Pin<&mut Self>` in method calls.
  **Correction**: Use `Pin::as_mut()` to convert `Pin<Box<T>>` to `Pin<&mut T>` before calling the method.

- **Error**: Forgetting to call `as_mut()` when calling a pinned method multiple times.
  **Correction**: Each call to a method taking `self: Pin<&mut Self>` consumes the `Pin<&mut Self>`. Call `as_mut()` before each invocation to reborrow.

# Common Confusions

- **Confusion**: Thinking `&mut self` and `self: Pin<&mut Self>` are interchangeable for `!Unpin` types.
  **Clarification**: They represent different lifecycle phases. `&mut self` is for the unpinned phase; `self: Pin<&mut Self>` is for the pinned phase. Using the wrong one makes the method uncallable in the intended context.

- **Confusion**: Wondering why `drop` takes `&mut self` instead of `Pin<&mut Self>`.
  **Clarification**: This is a language limitation due to backwards compatibility. The `Drop` trait predates pinning. For `!Unpin` types, you must treat the `&mut self` in `drop` as if it were `Pin<&mut Self>`.

# Source Reference

Chapter 2: Pinning, sections "Pinned self in methods" and "Using pinned types."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pinned self in methods" section (lines 193-200 of source)
- Confidence rationale: HIGH — the source provides clear guidance on the choice between self-types with an intuitive phased model
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, unpin-trait) and co-extracted concepts (pin-type, pin-and-drop, structural-pinning, future-poll-signature)
