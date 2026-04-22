---
concept: Async Drop
slug: async-drop
category: language-features
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Async drop and scoped tasks"
extraction_confidence: medium
aliases:
  - "async destructors"
  - "asynchronous drop"
  - "async destructor"
prerequisites:
  - structured-concurrency
  - cancellation-propagation
extends: []
related:
  - pin-and-drop
  - temporal-scope
  - scoped-threads
  - nursery-pattern
contrasts_with: []
answers_questions:
  - "What is async drop?"
  - "Why is async drop important for structured concurrency?"
---

# Quick Definition

Async drop is the currently-missing Rust language feature that would allow destructors to perform asynchronous cleanup operations. Its absence is a key barrier to fully implementing structured concurrency in async Rust, because synchronous `drop` cannot await child task cancellation or perform async resource cleanup.

# Core Definition

"In Rust, destructors (`drop`) are used to ensure resources are cleaned up when an object's lifetime ends. Since futures are just objects, their destructor would be an obvious place to ensure cancellation of child futures. However, in an async program it is very often desirable for cleanup actions to be asynchronous (not doing so can block other tasks). Unfortunately Rust does not currently support asynchronous destructors (async drop). There is ongoing work to support them, but it is difficult for a number of reasons, including that an object with an async destructor might be dropped from non-async context, and that since calling `drop` is implicit, there is nowhere to write an explicit `await`." (Async Reference, Ch. 3: Structured Concurrency, "Async drop and scoped tasks")

# Prerequisites

- **Structured concurrency** -- async drop is motivated by the need to enforce structured concurrency principles in async code
- **Cancellation propagation** -- async drop would enable proper cancellation propagation through the task tree via destructors

# Key Properties

1. Rust does not currently support async drop (as of the source's writing)
2. There is ongoing work to add async drop to the language
3. Key difficulty: an object with an async destructor might be dropped from non-async context
4. Key difficulty: `drop` is called implicitly, so there is nowhere to write an explicit `await`
5. Without async drop, cleanup in async programs may block other tasks
6. Futures are "just objects," so their destructor is the natural place for cancellation of child futures
7. The absence of async drop is why there are no "scoped tasks" for async (analogous to scoped threads)

# Construction / Recognition

## Workaround in the Absence of Async Drop:
1. Use an explicit async shutdown method rather than relying on `drop`
2. The shutdown method can await child task cancellation and async resource cleanup
3. Call the shutdown method before allowing the object to be dropped
4. The source recommends: "use an explicit shutdown method rather than dropping the component, so that the shutdown function can wait for child tasks to terminate or cancel them (since `drop` cannot be async)"

## To Recognize Where Async Drop Would Help:
1. Look for `drop` implementations that need to perform I/O (closing network connections, flushing buffers)
2. Look for cases where dropping a future should cancel spawned child tasks and wait for them
3. Look for explicit shutdown methods that exist because `drop` cannot be async

# Context & Application

The absence of async drop is a fundamental gap in Rust's async ecosystem that the source connects directly to structured concurrency. Without async drop:

- A future's destructor cannot properly propagate cancellation to spawned child tasks (it cannot await their termination)
- Resource cleanup in async contexts may block the executor thread
- There is no "scoped tasks" construct for async (the synchronous analog, scoped threads, works well)

The source's recommended workaround is explicit shutdown: "use an explicit shutdown method rather than dropping the component, so that the shutdown function can wait for child tasks to terminate or cancel them (since `drop` cannot be async)." (Ch. 3, "Structured and unstructured idioms")

The source also connects async drop to the question of scoped tasks: "Given how useful scoped threads are (both in general and for structured concurrency), another good question is why there is no similar construct for async programming ('scoped tasks')?" This is left as a TODO.

# Examples

**Example 1** (Ch. 3, "Async drop and scoped tasks"): The core problem: "Since futures are just objects, their destructor would be an obvious place to ensure cancellation of child futures. However, in an async program it is very often desirable for cleanup actions to be asynchronous (not doing so can block other tasks)."

**Example 2** (Ch. 3, "Async drop and scoped tasks"): The technical difficulties: "it is difficult for a number of reasons, including that an object with an async destructor might be dropped from non-async context, and that since calling `drop` is implicit, there is nowhere to write an explicit `await`."

**Example 3** (Ch. 3, "Structured and unstructured idioms"): The practical workaround: "To handle shutting down a program (or component), use an explicit shutdown method rather than dropping the component, so that the shutdown function can wait for child tasks to terminate or cancel them (since `drop` cannot be async)."

# Relationships

## Builds Upon
- **structured-concurrency** -- async drop is needed to fully implement structured concurrency in async Rust
- **cancellation-propagation** -- async drop would be the mechanism for propagating cancellation through destructors

## Enables
- Scoped tasks (the async analog of scoped threads) -- currently blocked on async drop
- Automatic async resource cleanup in destructors
- Full structured concurrency enforcement in async Rust

## Related
- **pin-and-drop** -- pin interacts with drop semantics in async contexts (Ch. 2)
- **temporal-scope** -- async drop would enforce temporal scope at the destructor level
- **scoped-threads** -- scoped threads work in synchronous Rust; the async equivalent is blocked on async drop
- **nursery-pattern** -- nurseries partially work around the lack of async drop

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Attempting to do async work (I/O, awaiting futures) inside a synchronous `drop` implementation.
  **Correction**: Synchronous `drop` cannot await. Use an explicit async shutdown method, or use a runtime's `block_on` as a last resort (which may panic if called from within an async context).

- **Error**: Assuming that dropping a future struct automatically cancels all tasks it spawned.
  **Correction**: Dropping a future only drops owned child futures (which are cancelled). Spawned tasks (via `tokio::spawn` etc.) are not affected by the parent's drop. Use join handles or cancellation tokens.

# Common Confusions

- **Confusion**: Thinking async drop exists in Rust today.
  **Clarification**: As of the source's writing, Rust does not support async drop. "There is ongoing work to support them," but it remains a difficult unsolved problem.

- **Confusion**: Thinking the explicit shutdown workaround is equivalent to async drop.
  **Clarification**: Explicit shutdown methods are a workaround, not a replacement. They require the caller to remember to call shutdown before drop, and they do not compose with the language's automatic cleanup mechanisms (scope exit, panic unwinding, etc.).

# Source Reference

Chapter 3: Structured Concurrency, "Async drop and scoped tasks" section under "Related topics." The shutdown workaround is discussed in "Structured and unstructured idioms." The concept is also referenced in Chapter 2 (Pinning) in the context of pin and drop interactions.

# Verification Notes

- Definition source: Direct quotation from "Async drop and scoped tasks" section
- Key Properties: Extracted from the explicit discussion in the section; the difficulties are directly stated
- Confidence rationale: MEDIUM -- the source clearly describes the problem and its significance, but the section contains a TODO for the scoped tasks answer, and async drop is described as ongoing work with uncertain resolution. The concept itself is well-defined but its future status is uncertain.
- Uncertainties: The source marks "TODO answer this" for why there are no scoped tasks; the current state of async drop work may have progressed since the source was written
- Cross-reference status: pin-and-drop references Ch. 2 cards; other slugs are in this extraction set
