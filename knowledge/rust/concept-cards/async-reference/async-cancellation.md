---
concept: Async Cancellation
slug: async-cancellation
category: async-programming
subcategory: lifecycle
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Cancellation and cancellation safety"
chapter_number: 1
pdf_page: null
section: null
extraction_confidence: low
aliases:
  - "cancellation"
  - "future cancellation"
  - "async task cancellation"
  - "drop as cancel"
prerequisites: []
extends: []
related:
  - cancellation-safety
  - async-drop
  - cancellation-propagation
  - structured-concurrency
contrasts_with:
  - cancellation-safety
answers_questions:
  - "What is async cancellation?"
  - "What is the difference between cancellation and cancellation safety?"
---

# Quick Definition

Async cancellation is the act of stopping a future before it completes. In Rust's async model, dropping a future is the primary cancellation mechanism: `drop = cancel`. Cancellation can only occur at `.await` points.

# Core Definition

The source outlines async cancellation as a key concept distinguishing async from threaded concurrency. The outline states: "drop = cancel," "only at await points," and notes that cancellation is a "useful feature" that is "still somewhat abrupt and surprising." The source also distinguishes between internal and external cancellation, and between cancellation of threads versus futures. (Async Reference, Ch. 1: Cancellation and cancellation safety — outline notes)

The source additionally mentions alternative cancellation mechanisms beyond drop: "abort" and "cancellation tokens."

# Prerequisites

This concept is presented as a standalone topic in the source outline. General familiarity with async/await and futures is assumed but not explicitly listed as a prerequisite in the outline.

# Key Properties

1. In Rust async, dropping a future cancels it (`drop = cancel`)
2. Cancellation can only occur at `.await` points (futures are not interrupted mid-execution)
3. Cancellation is a useful feature of async Rust, not merely a hazard
4. Cancellation is "still somewhat abrupt and surprising" — it requires care
5. There is a distinction between internal cancellation (the future decides to stop) and external cancellation (something outside drops the future)
6. Threads and futures have different cancellation semantics
7. Alternative cancellation mechanisms exist: abort (forceful termination) and cancellation tokens (cooperative signaling)

# Construction / Recognition

## To Recognize Cancellation

1. A future is dropped before returning `Poll::Ready` — this is cancellation
2. A `select!` macro picks one branch and drops the other futures — the dropped futures are cancelled
3. A timeout wrapper drops the inner future when time expires — the inner future is cancelled
4. An explicit `.abort()` call on a task handle

## Alternative Cancellation Mechanisms (from outline)

1. **Drop**: The default and most common — dropping a future cancels it
2. **Abort**: Forceful termination (e.g., `JoinHandle::abort` in Tokio)
3. **Cancellation tokens**: Cooperative mechanism where the future checks a token and exits voluntarily

# Context & Application

Async cancellation is fundamental to resource management in async Rust. Because futures can be cancelled at any `.await` point by being dropped, async code must be designed with the awareness that it may not run to completion. This has implications for resource cleanup, data consistency, and the design of async APIs.

**Typical contexts:**

- `select!` macros that race multiple futures and cancel the losers
- Timeout wrappers that cancel operations that take too long
- Task management where spawned tasks may be aborted
- Graceful shutdown sequences that cancel pending work

# Examples

The source (Ch. 1) is an outline only and provides no worked examples. The bullet points listed are:
- "drop = cancel"
- "only at await points"
- "useful feature"
- "still somewhat abrupt and surprising"
- "abort" and "cancellation tokens" as other mechanisms

No code examples or detailed scenarios are provided in the source.

# Relationships

## Builds Upon

- (none explicitly stated in the outline)

## Enables

- **cancellation-safety** — Cancellation safety is about handling cancellation correctly
- **cancellation-propagation** — How cancellation flows through async call trees
- **async-drop** — Drop behavior during cancellation

## Related

- **structured-concurrency** — Structured concurrency provides guarantees about when cancellation occurs

## Contrasts With

- **cancellation-safety** — Cancellation is the mechanism; cancellation safety is the property of handling it correctly without data loss or logic errors

# Common Errors

- **Error**: Assuming a future will always run to completion.
  **Correction**: Any future can be cancelled at any `.await` point by being dropped. Design async code to handle partial execution.

# Common Confusions

- **Confusion**: Thinking cancellation is the same as cancellation safety.
  **Clarification**: Cancellation is the act of stopping a future (e.g., by dropping it). Cancellation safety is the property that no data loss or logic errors occur when a future is cancelled. A future can be cancelled without the operation being cancellation-safe.

- **Confusion**: Thinking futures can be cancelled at any point during execution (like thread signals).
  **Clarification**: Futures can only be cancelled at `.await` points. Between `.await` points, execution runs synchronously to the next yield point.

# Source Reference

Chapter 1: Cancellation and cancellation safety, full chapter. Note: this chapter is an unfinished outline consisting of bullet-point notes, not written prose.

# Verification Notes

- Definition source: Synthesized from bullet-point outline in Ch. 1
- The source is an unfinished outline (~600 bytes of bullet points), NOT written prose
- Key points "drop = cancel" and "only at await points" are directly from the outline
- The distinction between internal/external cancellation and the list of alternative mechanisms (abort, cancellation tokens) are directly from the outline
- No examples, code, or detailed explanations exist in the source
- Confidence: LOW — the source is rough outline material with no definitions, examples, or prose. All properties beyond the bullet points are synthesized from general async Rust knowledge.
- Cross-reference status: `cancellation-safety` is a planned card in this batch; `async-drop`, `cancellation-propagation`, `structured-concurrency` are expected from Agent C
- Uncertainties: The outline is incomplete and the final chapter may define these concepts differently. The distinction between internal/external cancellation and threads/futures is mentioned but not elaborated.
