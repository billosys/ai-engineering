---
concept: Manual Pinning
slug: manual-pinning
category: async-programming
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Manual pinning"
extraction_confidence: high
aliases:
  - "explicit pinning"
  - "pinning leaking through async/await"
prerequisites:
  - pin-type
  - pinning-values
  - future-poll-signature
  - pin-and-async
extends:
  - pin-and-async
  - future-poll-signature
related:
  - structural-pinning
  - pinned-self
contrasts_with: []
answers_questions:
  - "When does pinning leak through the async/await abstraction?"
  - "When do I need to manually pin a future?"
  - "Why does select! sometimes require pinning?"
---

# Quick Definition

Manual pinning is required when pinning "leaks through" the async/await abstraction, typically when polling futures directly, using boxed futures, implementing custom futures, combining futures by reference (e.g., in `select!` loops), or working with streams.

# Core Definition

"There are some places where pinning leaks through the abstraction of async/await. At its root, this is due to the `Pin` in the signature of `Future::poll` and `Stream::poll_next`. When using futures and streams directly (rather than through async/await), we might need to consider pinning to make things work." (Ch. 2, "Manual pinning")

The source enumerates five common situations requiring manual pinning:

1. "Polling a future or stream - either in application code or when implementing your own future."
2. "Using boxed futures. If you're using boxed futures (or streams) and therefore writing out future types rather than using async functions, you'll likely see a lot of `Pin<...>` in those types and need to use `Box::pin` to create the futures."
3. "Implementing a future - inside `poll`, `self` is pinned and therefore you need to work with pin projection and/or unsafe code to get mutable access to fields of `self`."
4. "Combining futures or streams. ... if you need to take a reference to a future and then poll it (e.g., defining a future outside a loop and using it in `select!` inside the loop), then you will need to pin the reference to the future in order to use the reference like a future."
5. "Working with streams - there is currently less abstraction in Rust around streams than futures, so you're more likely to use combinator methods ... or even `poll` manually than when working with futures."

# Prerequisites

- **Pin type** — Must understand `Pin<Ptr>` to work with pinned pointers manually
- **Pinning values** — Must know how to create `Pin<Box<T>>` and `Pin<&mut T>` using `Box::pin` and `pin!`
- **Future poll signature** — The `Pin` in `Future::poll` is the root cause of manual pinning
- **Pin and async** — Must understand why async futures require pinning

# Key Properties

1. Manual pinning is needed when the async/await abstraction is insufficient
2. The root cause is always the `Pin` in `Future::poll` or `Stream::poll_next`
3. Polling a future manually requires pinning it first
4. Boxed futures (`Pin<Box<dyn Future>>`) require `Box::pin` to create
5. Implementing `Future::poll` means working with `Pin<&mut Self>` and pin projection
6. Using `select!` with a future reference defined outside the loop requires pinning the reference
7. Streams require manual pinning more often than futures due to less abstraction in the ecosystem

# Construction / Recognition

## To Recognize When Manual Pinning Is Needed

1. Compiler error mentioning `Unpin` bound or `Pin` requirement
2. Working with `dyn Future` or boxed future types
3. Using `select!` with a future defined outside the select expression
4. Implementing `Future` or `Stream` traits manually
5. Calling `.poll()` directly on a future or stream

## To Apply Manual Pinning

1. For a future you want to poll: `let pinned = pin!(my_future);` (stack) or `let pinned = Box::pin(my_future);` (heap)
2. For a future reference in `select!`: pin the reference before the loop
3. For boxed futures: use `Box::pin(async { ... })` when creating them
4. Inside `Future::poll`: use `pin-project` or unsafe pin projection to access fields

# Context & Application

Manual pinning is the "escape hatch" aspect of Rust's async design. The source opens this section with an optimistic note: "Hopefully, you can do all you ever want to do with async Rust and never worry about pinning." (Ch. 2, "Pinning and async programming")

In practice, manual pinning is most commonly encountered in two scenarios:
1. The `select!` macro in a loop, where a future is defined before the loop and used by reference inside it — the reference must be pinned.
2. Type-erased futures using `Pin<Box<dyn Future<Output = T>>>`, which are common in framework and library code.

The stream case is notable: "there is currently less abstraction in Rust around streams than futures, so you're more likely to use combinator methods or even `poll` manually than when working with futures." (Ch. 2, "Manual pinning")

# Examples

**Polling a future** (Ch. 2, "Manual pinning"):
> "Polling a future or stream - either in application code or when implementing your own future."

**Boxed futures** (Ch. 2, "Manual pinning"):
> "If you're using boxed futures (or streams) and therefore writing out future types rather than using async functions, you'll likely see a lot of `Pin<...>` in those types and need to use `Box::pin` to create the futures."

**Select with references** (Ch. 2, "Manual pinning"):
> "if you need to take a reference to a future and then poll it (e.g., defining a future outside a loop and using it in `select!` inside the loop), then you will need to pin the reference to the future in order to use the reference like a future."

**Implementing a future** (Ch. 2, "Manual pinning"):
> "Implementing a future - inside `poll`, `self` is pinned and therefore you need to work with pin projection and/or unsafe code to get mutable access to fields of `self`."

# Relationships

## Builds Upon
- **Pin and async** — Manual pinning arises when the automatic pinning of async/await is insufficient
- **Future poll signature** — The `Pin<&mut Self>` in `Future::poll` is the root cause

## Enables
(none specific — manual pinning is itself the resolution of the leaky abstraction)

## Related
- **Structural pinning** — Inside `poll` implementations, accessing fields requires pin projection
- **Pinned self** — Manual future implementations must work with `self: Pin<&mut Self>`
- **Pinning values** — `Box::pin` and `pin!` are the primary tools for manual pinning

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to use a future reference in `select!` without pinning it first.
  **Correction**: Pin the reference before the select loop: `let future = pin!(my_future);`, then use `&mut future` in `select!`.

- **Error**: Forgetting to use `Box::pin` when creating boxed futures.
  **Correction**: When the type requires `Pin<Box<dyn Future>>`, create the future with `Box::pin(async { ... })`.

# Common Confusions

- **Confusion**: Believing manual pinning is always needed when working with async code.
  **Clarification**: "Hopefully, you can do all you ever want to do with async Rust and never worry about pinning." Manual pinning is only needed when stepping outside the async/await abstraction.

- **Confusion**: Thinking streams and futures require the same amount of manual pinning.
  **Clarification**: Streams currently require more manual pinning because "there is currently less abstraction in Rust around streams than futures."

# Source Reference

Chapter 2: Pinning, section "Manual pinning."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Manual pinning" section (lines 275-284 of source)
- Confidence rationale: HIGH — the source provides an exhaustive enumeration of manual pinning scenarios with clear explanations
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning) and co-extracted concepts (pin-type, pinning-values, future-poll-signature, pin-and-async, structural-pinning, pinned-self)
