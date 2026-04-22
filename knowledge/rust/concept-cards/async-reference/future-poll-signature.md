---
concept: Future Poll Signature
slug: future-poll-signature
category: async-programming
subcategory: null
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinning and async programming"
extraction_confidence: high
aliases:
  - "Future::poll"
  - "poll method"
  - "Pin in Future::poll"
prerequisites:
  - pin-type
  - pin-and-async
  - pinned-self
extends:
  - pin-and-async
related:
  - manual-pinning
  - structural-pinning
contrasts_with: []
answers_questions:
  - "Why does Future::poll require Pin<&mut Self>?"
  - "What is the signature of Future::poll?"
  - "How does Pin appear in the Future trait?"
---

# Quick Definition

`Future::poll` takes `self: Pin<&mut Self>` because compiler-generated futures may be self-referential, and pinning guarantees the future remains at a stable address so internal references stay valid across poll calls.

# Core Definition

"We see this requirement in the signature of `Future::poll`, where the type of `self` (the future) is `Pin<&mut Self>`. Mostly, when using async/await, the compiler takes care of pinning and unpinning, and as a programmer you don't need to worry about it." (Ch. 2, "Pinning and async programming")

The `Pin<&mut Self>` in `Future::poll` is the primary point where the pinning system connects to async programming. It reflects the fact that between poll calls, a future's internal state may contain self-references (variables that reference other variables stored as fields of the future struct). The pin guarantee ensures these references remain valid.

# Prerequisites

- **Pin type** — Must understand `Pin<&mut Self>` as a type that restricts access to the pointee
- **Pin and async** — Must understand why async futures need pinning (self-referential fields)
- **Pinned self** — Must understand what `self: Pin<&mut Self>` means in method signatures

# Key Properties

1. `Future::poll` takes `self: Pin<&mut Self>` — the future must be pinned before it can be polled
2. This requirement exists because futures may contain self-references after being polled
3. The compiler handles pinning automatically when using `async`/`await`
4. When polling manually, the caller must ensure the future is pinned (via `Box::pin`, `pin!`, etc.)
5. `Stream::poll_next` has the same `Pin<&mut Self>` requirement for the same reasons
6. The `Pin` in the signature is what makes manual pinning necessary in certain edge cases

# Construction / Recognition

## To Poll a Future Manually

1. Create or obtain the future
2. Pin it using `Box::pin(future)` or `pin!(future)` to get `Pin<&mut Future>`
3. Create a `Context` (typically from a `Waker`)
4. Call `future.poll(cx)` on the pinned future
5. If calling `poll` multiple times, reborrow with `as_mut()` each time

## To Implement Future::poll

1. Define `fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>`
2. Use pin projection to access fields (via `pin-project` or unsafe code)
3. Structurally pinned sub-futures can be polled by projecting to `Pin<&mut SubFuture>`
4. Non-structurally pinned fields can be accessed as `&mut Field`

# Context & Application

The `Pin<&mut Self>` in `Future::poll` is the single most visible consequence of the pinning system for async Rust programmers. It is the reason pinning "leaks through" the async/await abstraction in certain situations. The source identifies several common scenarios where the pinned poll signature becomes relevant:

- Polling a future or stream manually (in application code or when implementing a custom future)
- Using boxed futures where types are written out rather than inferred from async functions
- Implementing a future where you need mutable access to fields of `self`
- Combining futures where a reference to a future needs to be polled (e.g., `select!` in a loop)

Most async Rust code never directly encounters `Future::poll` because `async`/`await` handles it. The signature matters when the abstraction is insufficient.

# Examples

**The signature's origin** (Ch. 2, "Pinning and async programming"):
> "We see this requirement in the signature of `Future::poll`, where the type of `self` (the future) is `Pin<&mut Self>`."

**Why it exists — self-referential futures** (Ch. 2, "Pinning and async programming"):
> Async function `foo` where `b = &a` across an await point generates a self-referential future. Moving this future would invalidate the reference, so `poll` requires the future to be pinned.

**When it leaks through** (Ch. 2, "Manual pinning"):
> "At its root, this is due to the `Pin` in the signature of `Future::poll` and `Stream::poll_next`. When using futures and streams directly (rather than through async/await), we might need to consider pinning to make things work."

# Relationships

## Builds Upon
- **Pin and async** — The poll signature is the concrete manifestation of pinning's role in async
- **Pinned self** — `Future::poll` is the canonical example of `self: Pin<&mut Self>` in a method

## Enables
- **Manual pinning** — The pinned poll signature is what forces manual pinning in certain situations

## Related
- **Structural pinning** — Inside `poll`, accessing sub-futures requires pin projection

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to poll a future without pinning it first.
  **Correction**: The future must be pinned before calling `poll`. Use `Box::pin(future)` or `pin!(future)` to create a pinned reference.

- **Error**: Moving a future between poll calls.
  **Correction**: Once pinned and polled, a future must not be moved. The `Pin` wrapper prevents this in safe code, but care is needed in unsafe contexts.

# Common Confusions

- **Confusion**: Thinking every future is self-referential and *requires* pinning for correctness.
  **Clarification**: Many futures are `Unpin` and do not actually contain self-references. The `Pin` in `Future::poll` is a universal requirement of the trait signature, but for `Unpin` futures it has no practical effect.

- **Confusion**: Believing `async`/`await` always requires the programmer to handle pinning.
  **Clarification**: "Mostly, when using async/await, the compiler takes care of pinning and unpinning, and as a programmer you don't need to worry about it." Pinning only becomes visible when working with futures directly.

# Source Reference

Chapter 2: Pinning, sections "Pinning and async programming" and "Manual pinning."

# Verification Notes

- Definition source: Direct quotation from Ch. 2, "Pinning and async programming" section (line 272 of source)
- Confidence rationale: HIGH — the source explicitly connects the `Pin` in `Future::poll` to the self-referential nature of async futures
- Uncertainties: None
- Cross-reference status: Slugs verified against co-extracted concepts (pin-type, pin-and-async, pinned-self, manual-pinning, structural-pinning)
