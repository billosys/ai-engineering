---
concept: Async Task Spawning
slug: async-task-spawning
category: async-programming
subcategory: null
tier: foundational
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "02-async-and-await"
chapter_number: 2
pdf_page: null
section: "Spawning tasks, Joining tasks, JoinHandle"
extraction_confidence: high
aliases:
  - "tokio::spawn"
  - "spawning async tasks"
  - "JoinHandle"
  - "joining tasks"
prerequisites:
  - async-await-basics
extends: []
related:
  - async-programming-overview
  - tokio-spawn
  - tokio-overview
  - async-cancellation
contrasts_with:
  - tokio-spawn
answers_questions:
  - "How do you introduce concurrency in async Rust?"
  - "What does tokio::spawn do?"
  - "How do you get the result of a spawned async task?"
  - "What is a JoinHandle?"
  - "What is the difference between awaiting a function and spawning it?"
---

# Quick Definition

`tokio::spawn` creates a new async task that runs concurrently (and potentially in parallel) with the spawning task. It returns a `JoinHandle` that can be `.await`ed to retrieve the spawned task's result. Spawning is how concurrency is introduced in async Rust -- sequential `.await` chains alone are strictly sequential.

# Core Definition

"Just like we use `std::thread::spawn` to spawn a new task, we can use `tokio::spawn` to spawn a new async task. Note that `spawn` is a function of Tokio, the runtime, not from Rust's standard library, because tasks are purely a runtime concept." (Ch. 2, "Spawning tasks")

"There are three concepts in play: futures, tasks, and threads. The `spawn` function takes a future (which remember can be made up of many smaller futures) and runs it as a new Tokio task. Tasks are the concept which the Tokio runtime schedules and manages (not individual futures). Tokio (in its default configuration) is a multi-threaded runtime which means that when we spawn a new task, that task may be run on a different OS thread from the task it was spawned from." (Ch. 2, "Spawning tasks")

On joining: "If we want to get the result of executing a spawned task, then the spawning task can wait for it to finish and use the result, this is called joining the tasks (analogous to joining threads, and the APIs for joining are similar)." (Ch. 2, "Joining tasks")

On the critical distinction between sequential and concurrent code: "When we write two statements following each other in Rust, they are executed sequentially (whether in async code or not). When we write `await`, that does not change the concurrency of sequential statements. E.g., `foo(); bar();` is strictly sequential ... `foo().await; bar().await;` is also strictly sequential ... If we use either `thread::spawn` or `tokio::spawn` we introduce concurrency and potentially parallelism." (Ch. 2, "Spawning tasks")

# Prerequisites

This concept requires understanding of async functions, `.await`, and futures from `async-await-basics`. The source builds directly on the examples from earlier in Ch. 2.

# Key Properties

1. `tokio::spawn` takes a future and runs it as a new Tokio task, returning a `JoinHandle`
2. `spawn` is a regular (non-async) function -- it does real work (scheduling) before returning, unlike async functions that are inert until awaited
3. Spawned tasks run **concurrently** with the spawning task and any other tasks; on a multi-threaded runtime they may also run **in parallel** on different OS threads
4. A spawned task may start on one thread and be moved to another during execution
5. Dropping a `JoinHandle` does **not** cancel the spawned task -- the task continues running independently
6. `.await`ing a `JoinHandle` waits for the spawned task to complete and returns a `Result` -- `Ok(value)` on success, `Err(JoinError)` on panic or abort
7. `JoinHandle` is itself a future -- it is generic over the return type of the spawned task (e.g., `JoinHandle<String>`)
8. Immediately awaiting a spawn (`spawn(foo()).await`) defeats the purpose -- it introduces no concurrency because the spawning task blocks waiting
9. Sequential `.await` is strictly sequential even in async code -- `spawn` (or concurrency primitives like `join`/`select`) is required to introduce concurrency
10. The source also mentions that async Rust supports "concurrency but not parallelism" via constructs like `join` and `select`, independent of the runtime (covered in later chapters)

# Construction / Recognition

## Introducing Concurrency via Spawn

1. Call `tokio::spawn(some_future)` to create a new concurrent task
2. Save the returned `JoinHandle` if you need the result later
3. Do other work concurrently
4. `.await` the `JoinHandle` when you need the result (joining)

## Pattern: Fire-and-Forget vs Join

- **Fire-and-forget**: Discard the `JoinHandle` -- the task runs to completion independently
- **Join**: Save the `JoinHandle` and `.await` it later to get the result and synchronize

## Anti-Pattern: Immediate Await

Writing `spawn(foo()).await` spawns a task then immediately waits for it. The source explicitly warns: "there is no possible concurrency! You almost never want to do this (because why bother with the spawn? Just write the sequential code)."

# Context & Application

This card captures the async-book's pedagogical introduction to spawning, which carefully builds up from the observation that sequential `.await` introduces zero concurrency. The source uses a progression of hello-world variants to demonstrate this: first a purely sequential version, then a version with `sleep` showing sequential behavior, then a spawned version showing concurrent (nondeterministic) output, and finally a joined version showing controlled synchronization.

The source's key insight for beginners is that `async`/`await` alone do not create concurrency. The `.await` operator is about driving futures to completion, not about introducing parallelism. Concurrency requires an explicit action: spawning a task, or using concurrency primitives. This is a critical mental model correction for programmers coming from other async ecosystems.

The distinction between `spawn` (a runtime function, not a language feature) and `thread::spawn` (a standard library function) reinforces that async tasks are a runtime concept, not a language-level concept. Different runtimes may have different spawning semantics.

This card focuses on the async-book's tutorial-style introduction. The `tokio-spawn` card in the tokio-tutorial covers Tokio-specific details like `Send` bounds, `'static` requirements, and `spawn_blocking` in greater depth.

# Examples

**Example 1** (Ch. 2, hello-world-spawn): Two functions printing "hello" and "world!" are spawned as separate tasks. "If you run the program a few times you should see the strings printing in both orders - sometimes 'hello' first, sometimes 'world!' first. A classic concurrent race!" The spawned tasks run concurrently and the nondeterministic ordering proves it.

**Example 2** (Ch. 2, hello-world-join): The same spawned tasks, but now the `JoinHandle`s are saved and later awaited:
```rust
let handle1 = tokio::spawn(say_hello());
let handle2 = tokio::spawn(say_world());
// ... other work ...
let _ = handle1.await;
let _ = handle2.await;
println!("!");
```
The two spawned tasks still run concurrently (both orderings are possible), but the exclamation mark always prints last because the main task waits for both handles before continuing. The source notes that `let _ = ...` avoids a warning about the unused `Result`.

**Example 3** (Ch. 2, JoinHandle error handling): "If the spawned task completed successfully, then the task's result will be in the `Ok` variant. If the task panicked or was aborted (a form of cancellation), then the result will be an `Err` containing a `JoinError`." The source advises that `unwrap`ing the `JoinHandle` result is reasonable if you're not using `abort`-based cancellation, as it effectively propagates panics.

# Relationships

## Builds Upon

- **async-await-basics** -- understanding of async functions, `.await`, and futures is required before spawning makes sense

## Enables

- Concurrency primitives (`join`, `select`) covered in later async-book chapters
- Cancellation patterns (aborting spawned tasks via `JoinHandle`)

## Related

- **async-programming-overview** -- the conceptual foundation explaining why spawning introduces concurrency
- **tokio-spawn** -- Tokio-tutorial's deeper coverage of spawn semantics, `Send` bounds, and `spawn_blocking`
- **tokio-overview** -- broader context of the Tokio runtime that provides `spawn`
- **async-cancellation** -- cancellation via `JoinHandle::abort`

## Contrasts With

- **tokio-spawn** -- this card provides the async-book's beginner-oriented introduction; tokio-spawn covers Tokio-specific details and constraints in depth

# Common Errors

- **Error**: Expecting sequential `.await` to run tasks concurrently.
  **Correction**: `foo().await; bar().await;` is strictly sequential. Use `tokio::spawn` to introduce concurrency, or `join!`/`select!` for structured concurrency without spawning.

- **Error**: Immediately awaiting a spawned task: `spawn(foo()).await`.
  **Correction**: This spawns a task then immediately blocks waiting for it -- there is no concurrency. Either save the `JoinHandle` and await it later, or just call `foo().await` directly without spawning.

- **Error**: Assuming a dropped `JoinHandle` cancels the task.
  **Correction**: "Dropping the `JoinHandle` does not affect the spawned task" -- it continues running. To cancel a task, use `JoinHandle::abort()`.

# Common Confusions

- **Confusion**: Thinking `async`/`await` inherently provides concurrency.
  **Clarification**: `async`/`await` provides the ability to yield control and resume later, but sequential `.await` calls are strictly sequential. Concurrency must be explicitly introduced via `spawn`, `join!`, `select!`, or similar constructs.

- **Confusion**: Thinking spawned tasks run on a fixed thread.
  **Clarification**: In Tokio's default multi-threaded runtime, "when we spawn a new task, that task may be run on a different OS thread from the task it was spawned from (it may be run on the same thread, or it may start on one thread and then be moved to another later on)."

- **Confusion**: Conflating `JoinHandle.await` returning `Result` with the task's own `Result`.
  **Clarification**: `JoinHandle.await` returns `Result<T, JoinError>` where the `Err` case means the task panicked or was aborted -- not a regular application error. The inner `T` is the task's return value, which may itself be a `Result`.

# Source Reference

Chapter 2: Async and Await -- sections "Spawning tasks", "Joining tasks", and "JoinHandle". These are the final three sections of the chapter.

# Verification Notes

- Definition source: Direct quotations from Ch. 2 "Spawning tasks" and "Joining tasks" sections
- Sequential-vs-concurrent distinction: Directly quoted summary from the source
- JoinHandle behavior (drop, await, Result): Directly from Ch. 2 "JoinHandle" section
- Confidence: HIGH -- the source provides clear prose with worked examples demonstrating each concept
- Uncertainties: None for this section -- it is well-written and complete
- Cross-reference status: `async-await-basics` and `async-programming-overview` are cards in this batch; `tokio-spawn` exists in tokio-tutorial; `async-cancellation` exists in async-reference
