---
concept: Pinning Values
slug: pinning-values
category: type-system
subcategory: type-wrappers
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinning values"
extraction_confidence: high
aliases:
  - "creating pinned pointers"
  - "Box::pin"
  - "pin! macro"
  - "Pin::new_unchecked"
  - "stack pinning"
  - "heap pinning"
prerequisites:
  - pin-type
  - pinning
  - unpin-trait
extends:
  - pin-type
related:
  - pin-and-async
  - manual-pinning
contrasts_with: []
answers_questions:
  - "How do I pin a value on the heap?"
  - "How do I pin a value on the stack?"
  - "What are the different ways to create a pinned pointer?"
---

# Quick Definition

Pinning values is the act of creating `Pin<Ptr>` pointers to objects, done via `Box::pin` for heap pinning, the `pin!` macro for stack pinning, or the unsafe `Pin::new_unchecked` for custom pointer types.

# Core Definition

"Objects are not created pinned. An object starts unpinned (and may be freely moved), it becomes pinned when a pinning pointer is created which points to the object. If the object is `Unpin`, then this is trivial using `Pin::new`, however, if the object is not `Unpin`, then pinning it must ensure that it cannot be moved or invalidated via an alias." (Ch. 2, "Pinning values")

The source describes three primary mechanisms for creating pinned values:

1. **Heap pinning**: "`Box::pin`... or convert an existing `Box` into a pinning `Box` using `Box::into_pin`" (Ch. 2, "Pinning values")
2. **Stack pinning**: "To pin an object on the stack, you can use the `pin` macro to create and pin a mutable reference (`Pin<&mut T>`)" (Ch. 2, "Pinning values")
3. **Unsafe pinning**: "For pointers which don't [have safe mechanisms], or for your own pointer types, you'll need to use `Pin::new_unchecked` to create a pinned pointer" (Ch. 2, "Pinning values")

# Prerequisites

- **Pin type** — Must understand what `Pin<Ptr>` represents before learning how to create instances
- **Pinning** — Must understand the abstract concept of pinning to know what guarantees are being established
- **Unpin trait** — Whether a type is `Unpin` determines which pinning mechanisms are safe to use

# Key Properties

1. Objects start unpinned and become pinned when a pinning pointer is created
2. `Box::pin(value)` creates `Pin<Box<T>>` — the value is pinned on the heap
3. `Box::into_pin(boxed)` converts an existing `Box<T>` into `Pin<Box<T>>`
4. The `pin!` macro creates `Pin<&mut T>` — the value is pinned on the stack (or the async pseudo-stack in async functions)
5. `Pin::new_unchecked` is unsafe and requires the programmer to uphold pinning invariants manually
6. `Pin::new` is safe but only works for `Unpin` types (where pinning is trivial)
7. `Arc` and `Rc` have similar safe pinning mechanisms to `Box`
8. `Pin::static_ref` and `Pin::static_mut` can pin static references
9. There is no special compiler treatment for `Box` — it uses `Pin`'s unsafe API internally

# Construction / Recognition

## To Pin a Value on the Heap

1. Call `Box::pin(value)` to create a `Pin<Box<T>>` directly
2. Or create a `Box<T>` first, then convert with `Box::into_pin(boxed_value)`
3. The result is a `Pin<Box<T>>` — the value lives on the heap at a stable address

## To Pin a Value on the Stack

1. Use the `std::pin::pin!` macro: `let pinned = pin!(value);`
2. The result is a `Pin<&mut T>` binding
3. In async functions, this pins to the async pseudo-stack (likely on the heap as part of the future)

## To Pin with a Custom Pointer Type

1. Use `unsafe { Pin::new_unchecked(ptr) }` where `ptr` is your custom pointer
2. You must ensure: the pointee will remain valid at its address until dropped
3. You must ensure: `Deref`/`DerefMut` implementations don't move out of the pointee
4. You must ensure: the pointer's `Drop` doesn't invalidate the pointee

# Context & Application

Pinning values is the practical entry point for working with the pinning system. Most async programmers encounter pinning values when they need to poll a future directly, use `select!` with a reference to a future, or box a future for type erasure.

Heap pinning via `Box::pin` is the most common and ergonomic approach, especially for boxed futures (`Pin<Box<dyn Future>>`). Stack pinning via `pin!` is used when a temporary pinned reference is needed, such as inside a loop body that uses `select!`.

**Historical note**: The Tokio crate provides its own `pin!` macro with additional syntax for assigning into a variable. The older `pin_mut!` macro from futures-rs and pin-utils is deprecated in favor of the std macro.

# Examples

**Heap pinning** (Ch. 2, "Pinning values"):
> "To pin an object on the heap, you can create a new pinning `Box` by using `Box::pin`, or convert an existing `Box` into a pinning `Box` using `Box::into_pin`. In either case, you'll end up with `Pin<Box<T>>`."

**Stack pinning** (Ch. 2, "Pinning values"):
> "`Box::pin` pins an object to a place in the heap. To pin an object on the stack, you can use the `pin` macro to create and pin a mutable reference (`Pin<&mut T>`)."

**Footnote on async stack pinning** (Ch. 2, footnote):
> "This is only strictly pinning to the stack in non-async functions. In an async function, all locals are allocated in the async pseudo-stack, so the place being pinned is likely to be stored on the heap as part of the future underlying the async function."

# Relationships

## Builds Upon
- **Pin type** — Pinning values creates `Pin<Ptr>` instances
- **Pinning** — Pinning values is the concrete realization of the abstract pinning concept

## Enables
- **Pin and async** — Creating pinned futures is necessary for polling them
- **Manual pinning** — Understanding pinning values is prerequisite to manual pinning scenarios

## Related
- **Pin project crate** — Macro crates simplify working with pinned values in practice
- **Future poll signature** — `Future::poll` requires `Pin<&mut Self>`, which must be created via pinning

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to use `Pin::new` to pin a `!Unpin` type.
  **Correction**: `Pin::new` only works for `Unpin` types. For `!Unpin` types, use `Box::pin` (heap) or the `pin!` macro (stack), or `Pin::new_unchecked` (unsafe).

- **Error**: Assuming `Pin::new_unchecked` is safe to call on any pointer.
  **Correction**: `Pin::new_unchecked` is unsafe. The programmer must ensure the pointee remains valid at its address until dropped, including that no `&mut` can be obtained after pinning.

# Common Confusions

- **Confusion**: Believing that `pin!` always pins to the literal stack.
  **Clarification**: In async functions, locals live in the async pseudo-stack (typically on the heap as part of the future struct). The `pin!` macro pins to whatever place the local occupies.

- **Confusion**: Thinking `Box` has special compiler support for pinning.
  **Clarification**: "There is no special treatment for `Box` (or the other std pointers) either in the pinning implementation or the compiler. `Box` uses the unsafe functions in `Pin`'s API to implement `Box::pin`." (Ch. 2, footnote)

# Source Reference

Chapter 2: Pinning, section "Pinning values." Footnotes on `Box::pin` implementation and async pseudo-stack.

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pinning values" section (lines 96-110 of source)
- Confidence rationale: HIGH — the source explicitly enumerates all mechanisms for creating pinned values with clear distinctions
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, unpin-trait) and co-extracted concepts (pin-type, pin-and-async, manual-pinning)
