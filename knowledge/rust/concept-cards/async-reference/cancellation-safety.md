---
concept: Cancellation Safety
slug: cancellation-safety
category: async-programming
subcategory: correctness
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Cancellation and cancellation safety"
chapter_number: 1
pdf_page: null
section: "Cancellation safety"
extraction_confidence: low
aliases:
  - "cancel safety"
  - "cancel-safe"
  - "halt safety"
prerequisites:
  - async-cancellation
extends: []
related:
  - structured-concurrency
  - cancellation-propagation
  - async-drop
contrasts_with:
  - async-cancellation
answers_questions:
  - "What is cancellation safety?"
  - "What is the difference between cancellation and cancellation safety?"
---

# Quick Definition

Cancellation safety is the property that an async operation can be cancelled (dropped before completion) without causing data loss or logic errors. It is not a memory safety issue or race condition, but concerns correctness of program logic.

# Core Definition

The source outline states that cancellation safety is "Not a memory safety issue or race condition" but involves "Data loss or other logic errors." The outline notes that there are "Different definitions/names" for the concept, including "tokio's definition," a "general definition/halt safety," and the idea of "applying a replicated future idea." Root causes identified in the outline include "Splitting state between the future and the context" and issues with "select or similar in loops." (Async Reference, Ch. 1: Cancellation and cancellation safety, "Cancellation safety" section — outline notes)

# Prerequisites

- **Async cancellation** — Cancellation safety is about handling cancellation correctly; understanding what cancellation is (drop = cancel, only at await points) is essential

# Key Properties

1. Cancellation safety is NOT a memory safety issue — it does not cause undefined behavior or data races
2. Cancellation safety concerns data loss and logic errors that occur when a future is cancelled
3. There are multiple definitions in the ecosystem (the outline mentions Tokio's definition, a general definition, and "halt safety")
4. A root cause of cancellation-unsafety is splitting state between the future and its calling context
5. The `select!` macro (or similar combinators) used in loops is a common source of cancellation-safety issues
6. "Simple data loss" is one category of cancellation-unsafety
7. "Resumption" is mentioned as a related concern (suggesting that re-polling a cancelled-and-recreated future may lose progress)

# Construction / Recognition

## To Recognize Cancellation-Safety Issues

1. Look for `select!` or similar combinators used in loops — if a future is re-created each iteration, work from the previous iteration's cancelled future may be lost
2. Look for state that is split between the future's internal state and external variables — if the future is cancelled, internal state is lost while external state remains
3. Look for futures that buffer data internally before writing it to an external destination — cancellation can lose the buffered data

## To Make an Operation Cancellation-Safe

1. Avoid splitting state between the future and the calling context
2. When using `select!` in a loop, store the future in a variable outside the loop and re-use it (don't re-create it each iteration)
3. Perform state mutations atomically at `.await` boundaries so partial progress is not lost

# Context & Application

Cancellation safety is a critical correctness concern in async Rust, particularly when using combinators like `select!` that cancel futures as part of their normal operation. Unlike memory safety (which the compiler enforces), cancellation safety must be reasoned about by the programmer. Different parts of the Rust async ecosystem have different definitions and expectations around cancellation safety.

**Typical contexts:**

- `select!` loops where one branch's future may be repeatedly cancelled and recreated
- Buffered I/O operations where internal buffers may be lost on cancellation
- Async APIs that document whether they are "cancel-safe" (e.g., Tokio's documentation)
- Graceful shutdown where in-progress work must not be lost

# Examples

The source (Ch. 1, "Cancellation safety" section) is an outline only and provides no worked examples. The bullet points listed are:
- "Not a memory safety issue or race condition"
- "Data loss or other logic errors"
- "Different definitions/names" (tokio's, general/halt safety, replicated future)
- "Simple data loss"
- "Resumption"
- "Issue with select or similar in loops"
- "Splitting state between the future and the context as a root cause"

No code examples, detailed scenarios, or formal definitions are provided in the source.

# Relationships

## Builds Upon

- **async-cancellation** — Cancellation safety is about handling cancellation correctly

## Enables

- (none explicitly stated in the outline)

## Related

- **structured-concurrency** — Structured concurrency can help ensure cancellation safety by providing well-defined cancellation boundaries
- **cancellation-propagation** — How cancellation flows affects where cancellation-safety concerns arise
- **async-drop** — Drop behavior during cancellation affects whether resources are properly cleaned up

## Contrasts With

- **async-cancellation** — Cancellation is the mechanism (dropping a future); cancellation safety is the correctness property (no data loss or logic errors from cancellation)

# Common Errors

- **Error**: Using `select!` in a loop and recreating a future each iteration, losing progress from the cancelled future.
  **Correction**: Store the future outside the loop and reuse it across iterations, or ensure that any progress is captured in external state before the future can be cancelled.

# Common Confusions

- **Confusion**: Thinking cancellation-unsafety causes memory unsafety or data races.
  **Clarification**: Cancellation safety concerns are about logic errors and data loss, not memory safety. The program remains memory-safe; it just may lose data or behave incorrectly.

- **Confusion**: Assuming there is a single universal definition of "cancellation safety."
  **Clarification**: The source outline notes "Different definitions/names" including Tokio's specific definition, a general definition (also called "halt safety"), and a "replicated future" framing. These definitions differ in scope and specifics.

- **Confusion**: Thinking cancellation safety is the same as cancellation.
  **Clarification**: Cancellation is the act of stopping a future. Cancellation safety is the property that this stopping does not cause data loss or logic errors.

# Source Reference

Chapter 1: Cancellation and cancellation safety, section "Cancellation safety." Note: this section is an unfinished outline consisting of bullet-point notes, not written prose.

# Verification Notes

- Definition source: Synthesized from bullet-point outline in Ch. 1, "Cancellation safety" section
- The source is an unfinished outline (~600 bytes total for the whole chapter) with NO written prose, definitions, or examples
- Key points ("not a memory safety issue," "data loss or logic errors," "splitting state," "select in loops") are directly from the outline bullets
- The multiple definitions point (Tokio's, general, halt safety) is directly from the outline
- Confidence: LOW — the source is rough outline material. All coherent definitions and explanations are synthesized from the outline's bullet points plus general async Rust knowledge. The final written chapter may define these concepts very differently.
- Cross-reference status: `async-cancellation` is a planned card in this batch; `structured-concurrency`, `cancellation-propagation`, `async-drop` are expected from Agent C
- Uncertainties: The outline is incomplete; "resumption" and "replicated future idea" are mentioned without explanation and their intended meaning is unclear. The distinction between Tokio's definition and the "general definition" is not elaborated.
