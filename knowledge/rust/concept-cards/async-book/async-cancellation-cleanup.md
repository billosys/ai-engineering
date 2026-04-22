---
concept: Async Cancellation and Cleanup
slug: async-cancellation-cleanup
category: async-programming
subcategory: null
tier: advanced
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "Destruction and clean-up"
chapter_number: 8
pdf_page: null
section: null
extraction_confidence: low
aliases:
  - "async destruction"
  - "async cleanup"
  - "cancellation cleanup patterns"
  - "async Drop problem"
prerequisites:
  - async-advanced-topics
  - async-concurrency-composition
extends:
  - async-advanced-topics
related:
  - async-programming-overview
  - async-io-model
  - cancellation-safety
  - async-cancellation
  - async-drop
  - cancellation-propagation
contrasts_with: []
answers_questions:
  - "How do I clean up resources in async Rust?"
  - "What happens when an async task is cancelled?"
  - "Why is there no async Drop in Rust?"
  - "How do panics interact with async tasks?"
  - "What patterns exist for async cleanup?"
  - "How does cancellation affect other futures and tasks?"
---

# Quick Definition

Async cancellation and cleanup addresses the challenge of properly releasing resources and handling state when async tasks are cancelled, panic, or complete. Rust lacks async Drop, meaning destructors cannot perform asynchronous cleanup. This forces programmers to use alternative patterns: avoiding cleanup needs, separating cleanup from destruction, or centralizing cleanup in dedicated tasks. Cancellation can happen at any await point via dropping, aborting, or `select`, and code must be designed to handle this gracefully.

# Core Definition

Chapter 8 outlines the core challenges of destruction and cleanup in async Rust. The chapter is organized as a structured outline rather than fully-written prose, but the topics it identifies represent critical concerns for production async code:

**Async cleanup challenges** (Ch. 8, introduction outline):
- "Might want to do stuff async during clean up, e.g., send a final message"
- "Might need to clean up stuff which is still being used async-ly"
- "Might want to clean up when an async task completes or cancels and there is no way to catch that"
- "State of the runtime during clean-up phase (esp if we're panicking or whatever)"
- "No async Drop" (with note: "WIP")

**Cancellation mechanisms** (Ch. 8, "Cancellation" outline):
- Drop a future
- Cancellation token
- Abort functions
The outline notes the need for "logging or monitoring cancellation" and understanding "how cancellation affects other futures tasks."

**Panicking and async** (Ch. 8, "Panicking and async" outline):
- "Propagation of panics across tasks (spawn result)"
- "Panics leaving data inconsistent (tokio mutexes)"
- "Calling async code when panicking (make sure you don't)"

**Cleanup patterns** (Ch. 8, "Patterns for clean-up" outline):
- "Avoid needing clean up (abort/restart)"
- "Don't use async for cleanup and don't worry too much"
- "async clean up method + dtor bomb (i.e., separate clean-up from destruction)"
- "centralise/out-source clean-up in a separate task or thread or supervisor object/process"

**Why no async Drop** (Ch. 8, "Why no async Drop (yet)" outline):
- Described as an "advanced section and not necessary to read"
- Identifies the problem: "Why async Drop is hard"
- Notes "Possible solutions and their issues" and "Current status"

These topics are complemented by the cancellation content introduced in Ch. 3 (see async-advanced-topics card), which provides the foundational explanation: cancellation means "stopping a future from executing" and can occur at any `.await` point. Ch. 3 warns: "the code might stop executing at any `await` and never start again. In order for your code to be correct (specifically to be *cancellation safe*), it must work correctly whether it completes normally or whether it terminates at any await point."

# Prerequisites

- **async-advanced-topics** -- cancellation basics (dropping futures, await as cancellation points) are introduced in Ch. 3 and are essential background
- **async-concurrency-composition** -- `select!` is "often the primary source of cancellation" and understanding it is critical for reasoning about cleanup

# Key Properties

1. Async tasks can be cancelled at any `.await` point by dropping the future, aborting via JoinHandle, or implicitly via `select!`
2. Cancelled futures receive no notification and no opportunity to clean up (besides their synchronous destructor)
3. Rust has no async Drop -- destructors cannot perform asynchronous operations
4. Panics in spawned tasks are caught by the runtime and surfaced through the JoinHandle result
5. Panics can leave data protected by Tokio mutexes in an inconsistent state (Tokio mutexes do not poison)
6. Async code should never be called during a panic
7. The simplest cleanup strategy is to avoid needing cleanup entirely (design for abort/restart)
8. The "dtor bomb" pattern separates async cleanup from destruction: call an explicit async cleanup method, panic in Drop if it was not called
9. Cleanup can be centralized in a dedicated supervisor task or thread
10. CancellationToken provides cooperative cancellation where the future can observe and respond to cancellation requests

# Construction / Recognition

## To Design for Cancellation Safety:
1. Identify all `.await` points in your async function -- each is a potential termination point
2. Ensure no critical state is lost if execution stops at any await point
3. Avoid holding intermediate state (e.g., partially-read buffers) across await points unless that state can be safely discarded or recovered
4. If using `select!` in a loop, ensure futures are cancellation-safe or use fusing/guards

## To Implement Async Cleanup:
1. **Simplest approach**: Design operations to be idempotent so they can be safely retried after cancellation; avoid needing cleanup
2. **Synchronous cleanup**: Use standard `Drop` for cleanup that does not require async operations
3. **Explicit cleanup method**: Provide an `async fn cleanup()` method that must be called before dropping; optionally panic in `Drop` if it was not called ("dtor bomb")
4. **Supervisor pattern**: Centralize resource management in a dedicated task that handles cleanup on behalf of worker tasks
5. **Shutdown coordination**: Use channels or cancellation tokens to signal shutdown and allow tasks to clean up cooperatively (see Tokio shutdown guidance)

## To Handle Panics in Async Code:
1. Check `JoinHandle` results for panics from spawned tasks
2. Do not call async code from within a panic handler or `Drop` implementation
3. Be aware that Tokio mutexes do not poison on panic -- data may be inconsistent

# Context & Application

Cancellation and cleanup is one of the most challenging aspects of async Rust programming. The difficulty stems from a fundamental tension: async operations need async cleanup, but Rust's destruction mechanism (`Drop`) is synchronous. The source explicitly identifies this as an area of ongoing language development ("WIP").

The practical impact is significant. In production async services, resources such as network connections, database transactions, file handles, and in-flight messages all need proper cleanup. When a `select!` macro cancels a future that is mid-transaction, the programmer must reason about what happens to the partially-completed operation.

The source's list of cleanup patterns (from most to least simple) provides a practical decision framework: start by trying to avoid cleanup needs, then use synchronous Drop if possible, then explicit async methods, and finally supervisor patterns for complex cases. The Tokio documentation on [shutdown](https://tokio.rs/tokio/topics/shutdown) is referenced as additional guidance.

The interaction between cancellation and the broader async-reference concepts is important: the async-reference's `cancellation-safety` card addresses the formal property of being safe under cancellation, while the async-reference's `async-drop` card discusses the language-level feature gap. This card bridges those concepts with practical patterns from the Async Book.

# Examples

**Example 1 -- Cancellation at await points** (synthesized from Ch. 3 and Ch. 8):
A future reading data into an internal buffer that awaits the next datum illustrates the cleanup problem. If cancelled, the internal buffer is dropped and any destructively-read data is lost. This is the canonical example of why cancellation safety matters: the state split between the future (buffer) and the external source (data already consumed) cannot be reconciled after cancellation.

**Example 2 -- Cleanup patterns** (Ch. 8, "Patterns for clean-up" outline):
The source outlines four patterns in order of complexity:
1. Avoid needing cleanup (design for abort/restart)
2. Don't use async for cleanup (use synchronous Drop, accept limitations)
3. Explicit async cleanup method + dtor bomb (separate cleanup from destruction)
4. Centralize cleanup in a supervisor task or thread

**Example 3 -- Cancellation via select** (from Ch. 5, relevant to Ch. 8):
```rust
select! {
    result = do_work() => { process(result) }
    _ = cancellation_signal() => { /* do_work is dropped here */ }
}
```
When `cancellation_signal` completes first, the `do_work` future is dropped with no notification. Any intermediate state held by `do_work` is lost.

# Relationships

## Builds Upon
- **async-advanced-topics** -- cancellation basics (dropping futures, await as cancellation points) from Ch. 3
- **async-concurrency-composition** -- `select!` is the primary source of implicit cancellation

## Enables
- None explicitly -- this is an advanced topic addressing consequences of earlier concepts

## Related
- **async-programming-overview** -- cleanup challenges are a core aspect of the async programming model
- **async-io-model** -- IO operations are frequently the resources requiring cleanup
- **cancellation-safety** -- the formal correctness property for code that may be cancelled
- **async-cancellation** -- the async-reference's treatment of cancellation mechanisms
- **async-drop** -- the async-reference's treatment of the missing async Drop feature
- **cancellation-propagation** -- structured concurrency's approach to propagating cancellation through task trees

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Assuming a future will always run to completion.
  **Correction**: Any `.await` is a potential cancellation point. Design for the case where execution stops at any await, especially when using `select!` or when futures may be dropped.

- **Error**: Attempting to perform async operations in a `Drop` implementation.
  **Correction**: Rust does not support async Drop. Use an explicit async cleanup method, a supervisor task, or design operations to not need async cleanup.

- **Error**: Ignoring JoinHandle results from spawned tasks.
  **Correction**: Spawned tasks may panic, and the panic is caught by the runtime. Always check JoinHandle results to detect and handle panics.

# Common Confusions

- **Confusion**: Thinking `CancellationToken` prevents all forms of cancellation.
  **Clarification**: A future with a cancellation token can still be cancelled by dropping it or aborting its task. The cancellation token only provides *cooperative* cancellation -- the future must check the token and decide to stop.

- **Confusion**: Thinking Tokio mutexes poison on panic like `std::sync::Mutex`.
  **Clarification**: Tokio mutexes do not poison. A panic while holding a Tokio mutex leaves the protected data in a potentially inconsistent state with no automatic detection.

- **Confusion**: Thinking cancellation is rare or only happens on shutdown.
  **Clarification**: Cancellation is pervasive in async Rust. Every use of `select!` implicitly cancels futures. The source describes `select` as "often the primary source of cancellation in an async program."

# Source Reference

Chapter 8: "Destruction and clean-up" -- all sections. The entire chapter is a structured outline with section headings and bullet points, not fully-written prose. Sections: introduction (async cleanup challenges, no async Drop), "Cancellation" (mechanisms, monitoring, effects), "Panicking and async" (propagation, inconsistent state, calling async when panicking), "Patterns for clean-up" (four patterns from simple to complex), "Why no async Drop (yet)" (noted as advanced). Supplementary cancellation content drawn from Ch. 3's fully-written "Blocking and cancellation" section.

# Verification Notes

- Definition source: Bullet-point outlines from Ch. 8 sections, supplemented by direct quotations from Ch. 3's "Cancellation" subsection
- Key Properties: Items 1-3 and 10 derived from Ch. 3's fully-written text; items 4-9 derived from Ch. 8's outline bullet points
- Confidence rationale: LOW -- Ch. 8 is entirely a structured outline with no fully-written prose. The topics identified are clearly important and the organizational structure is sound, but the actual treatment is preliminary. The cancellation content from Ch. 3 (which is fully written) provides a solid foundation, but the cleanup patterns, panicking behavior, and async Drop discussion are all outline-only. The chapter explicitly marks its content as "WIP" areas.
- Uncertainties: All Ch. 8 sections may change substantially when fully written. The cleanup patterns are listed but not explained. The async Drop discussion is noted as having "possible solutions and their issues" that are not yet documented. The interaction between panicking and async mutexes needs more detail.
- Cross-reference status: `async-await-basics` and `async-programming-overview` from Agent A; `cancellation-safety`, `async-cancellation`, `async-drop`, `cancellation-propagation` from async-reference cards; other slugs in this extraction set
