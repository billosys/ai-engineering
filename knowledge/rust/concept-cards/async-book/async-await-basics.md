---
concept: Async/Await Basics
slug: async-await-basics
category: async-programming
subcategory: null
tier: foundational
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "02-async-and-await"
chapter_number: 2
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "async fn"
  - "await operator"
  - "async functions"
  - "futures are lazy"
prerequisites:
  - async-programming-overview
extends: []
related:
  - async-task-spawning
  - tokio-overview
  - tokio-runtime
  - future-trait-in-depth
contrasts_with: []
answers_questions:
  - "What does the async keyword do in Rust?"
  - "How does .await work?"
  - "Why do futures in Rust not execute until awaited?"
  - "What is an async runtime and why is it needed?"
  - "What are the components of an async runtime?"
  - "What is the relationship between futures and tasks?"
---

# Quick Definition

In Rust, `async fn` declares a function that returns a future instead of executing immediately. The `.await` operator drives a future to completion, either producing a result immediately or yielding control to the scheduler so another task can run. Futures in Rust are lazy -- they do no work until awaited or otherwise polled.

# Core Definition

"An async function is simply a function declared using the `async` keyword, and what that means is that it is a function which can be executed asynchronously, in other words the caller can choose not to wait for the function to complete before doing something else." (Ch. 2, "Async functions")

"In more mechanical terms, when an async function is called, the body is not executed as it would be for a regular function. Instead the function body and its arguments are packaged into a future which is returned in lieu of a real result." (Ch. 2, "Async functions")

On `.await`: "To get the result of that computation, we use the `await` keyword. If the result is ready immediately or can be computed without waiting, then `await` simply does that computation to produce the result. However, if the result is not ready, then `await` hands control over to the scheduler so that another task can execute." (Ch. 2, "await")

On laziness: "Calling an async function returns a future, it doesn't immediately execute the code in the function. Furthermore, a future does not do any work until it is awaited. This is in contrast to some other languages where an async function returns a future which begins executing immediately." (Ch. 2, "await")

The source defines the runtime's role: "Async tasks must be managed and scheduled. There are typically more tasks than cores available so they can't all be run at once." The runtime consists of a reactor/event loop (dispatches IO and timer events), a scheduler (determines when tasks execute and on which threads), and an executor (combines reactor and scheduler as the user-facing API). (Ch. 2, "The runtime")

# Prerequisites

The source builds directly on the concurrent programming concepts from Ch. 1 (cooperative multitasking, tasks, yield points). The concept of futures as deferred computations is introduced here for the first time.

# Key Properties

1. `async fn` transforms a function so that calling it returns a future rather than executing the body -- the body is packaged with its arguments into a future object
2. Futures are **lazy**: they do no work until driven by `.await` (or lower-level polling) -- this contrasts with languages like JavaScript where async functions begin executing immediately
3. `.await` is a postfix operator (`some_future.await`) that either produces a result immediately or yields control to the scheduler
4. `.await` can only be used inside an async context (currently async functions; later also async blocks and closures)
5. Within an async function, code executes sequentially as usual -- being async makes no difference to internal control flow
6. Synchronous functions can be called freely from async functions; async functions require `.await` to execute
7. The `?` error handling operator works with `.await` just as in synchronous Rust: `let data = read(...).await?`
8. A future is a regular Rust object (struct or enum) implementing the `Future` trait -- it represents a deferred computation
9. An async task is a future (usually a "big" future composed of many smaller ones) that is being executed by the runtime
10. Rust does not include an async runtime in the standard library -- you must choose an external runtime crate (Tokio being the most popular)
11. The runtime has three conceptual components: the **reactor** (IO/timer event dispatch), the **scheduler** (decides when/where tasks run), and the **executor** (user-facing API combining both)
12. `#[tokio::main]` is syntactic sugar that initializes the Tokio runtime and creates an initial async task for `main`

# Construction / Recognition

## Minimal Async Setup with Tokio (from Ch. 2)

1. Add Tokio dependency: `tokio = { version = "1", features = ["full"] }`
2. Annotate `main` with `#[tokio::main]` to make it an async entry point
3. Declare async functions with `async fn`
4. Call async functions and append `.await` to execute them

## Recognizing the Future/Task Distinction (from Ch. 2)

The source carefully distinguishes terminology:
- **Future**: A Rust object implementing `Future` -- represents a deferred computation
- **Task** (abstract): A logical sequence of concurrent execution, analogous to a thread
- **Runtime's task**: Whatever concept of task a specific runtime uses (e.g., a Tokio task)
- An async task is "just a future which is executed" -- but a future can be executed without being a runtime's task

## Combining Futures

"Async functions are one way to define a future, and `await` is one way to combine futures. Using `await` on a future combines that future into the future produced by the async function it's used inside." (Ch. 2, "await")

# Context & Application

This card captures the async-book's tutorial introduction to async/await mechanics. The source's unique contribution is its careful, beginner-oriented explanation of why futures are lazy and what that means practically -- calling an async function without `.await` produces a future that never executes (the compiler will warn).

The runtime discussion is distinctive in emphasizing that Rust deliberately does not bundle a runtime, unlike most languages with async support. The source introduces the reactor/scheduler/executor decomposition as common terminology rather than a strict requirement, noting that "there are no strong rules about how a runtime must be structured."

The source's treatment of the future/task distinction is notably precise. It acknowledges the terminology is confusing ("different runtimes have slightly different concepts of tasks") and commits to specific definitions for the rest of the book. This level of care reflects the async-book's pedagogical approach versus the async-reference's more formal treatment or the tokio-tutorial's practical focus.

Sequential `.await` chains (`foo().await; bar().await;`) do NOT introduce concurrency -- they are strictly sequential. Concurrency requires spawning tasks (covered in `async-task-spawning`) or using concurrency primitives like `join`/`select` (covered in later chapters).

# Examples

**Example 1** (Ch. 2, `add` and `wait_to_add`):
```rust
async fn add(a: u32, b: u32) -> u32 {
    a + b
}

async fn wait_to_add(a: u32, b: u32) -> u32 {
    sleep(1000).await;
    a + b
}
```
Calling `add(15, 3).await` returns `18` immediately. Calling `wait_to_add(15, 3).await` eventually returns `18`, but while sleeping another task can run. Calling either without `.await` returns a future that produces no result.

**Example 2** (Ch. 2, Mini-Redis client):
```rust
#[tokio::main]
async fn main() -> Result<()> {
    let mut client = client::connect("127.0.0.1:6379").await?;
    client.set("hello", "world".into()).await?;
    let result = client.get("hello").await?;
    println!("got value from the server; result={:?}", result);
    Ok(())
}
```
Sequential async calls with error handling via `?`. The source notes: "For all the talk so far about concurrency, parallelism, and asynchrony, both these examples are 100% sequential."

**Example 3** (Ch. 2, hello-world-sleep): The source demonstrates that sleeping for one second between printing "hello" and "world" produces strictly sequential output -- the task sleeps, then continues. "That is because executing a single task is purely sequential. If we had some concurrency, then that one second nap would be an excellent opportunity to get some other work done."

# Relationships

## Builds Upon

- **async-programming-overview** -- the conceptual foundation of cooperative multitasking, tasks, and yield points

## Enables

- **async-task-spawning** -- using `spawn` to create concurrent tasks (covered in later sections of Ch. 2)
- Async blocks and closures (covered in later chapters)
- Concurrency primitives like `join` and `select` (covered in later chapters)

## Related

- **tokio-overview** -- Tokio-specific perspective on runtime selection and configuration
- **tokio-runtime** -- deeper coverage of `#[tokio::main]` and runtime configuration
- **future-trait-in-depth** -- the `Future` trait mechanics that underlie `.await`

## Contrasts With

- (none -- this is the foundational async/await card for this source)

# Common Errors

- **Error**: Calling an async function without `.await` and expecting it to execute.
  **Correction**: Futures in Rust are lazy. `say_hello()` returns an unexecuted future. You must write `say_hello().await` to actually run it. The compiler will warn about unused futures.

- **Error**: Using `std::thread::sleep` instead of `tokio::time::sleep` in async code.
  **Correction**: `std::thread::sleep` blocks the entire OS thread, preventing the async scheduler from running other tasks. Use the async sleep provided by the runtime. The source's footnote explicitly warns: "if we were to use `sleep` from std we'd put the whole thread to sleep."

- **Error**: Expecting `.await` to introduce concurrency.
  **Correction**: `foo().await; bar().await;` is strictly sequential -- `foo` completes entirely before `bar` begins. Concurrency requires `spawn`, `join`, or `select`.

# Common Confusions

- **Confusion**: Thinking Rust's async model works like JavaScript's (where calling an async function starts execution immediately).
  **Clarification**: "A future does not do any work until it is awaited. This is in contrast to some other languages where an async function returns a future which begins executing immediately." In Rust, the future is an inert object until driven.

- **Confusion**: Conflating futures and tasks.
  **Clarification**: A future is any Rust object implementing `Future`. A task is a future that is being executed by a runtime. Not all futures are tasks -- a future can be awaited as part of another future without being a separate runtime task.

- **Confusion**: Thinking `.await` always blocks or always yields.
  **Clarification**: `.await` checks if the future's result is ready. If ready, it returns immediately with no yielding. If not ready, it yields control to the scheduler. The behavior depends entirely on the state of the awaited future.

# Source Reference

Chapter 2: Async and Await -- sections "Rust async concepts" (The runtime, Futures and tasks), "Async functions", "await", and "Some async/await examples". The Futures-rs subsection is omitted as it contains only TODO placeholders.

# Verification Notes

- Definition source: Direct quotations from Ch. 2 "Async functions" and "await" sections
- Runtime decomposition (reactor/scheduler/executor): Direct from Ch. 2 "The runtime" with specific terms quoted
- Future laziness: Explicitly stated and contrasted with other languages in Ch. 2
- Confidence: HIGH -- Ch. 2 provides extensive, well-written prose with clear definitions and examples
- Uncertainties: The Futures-rs subsection is marked TODO in the source, so ecosystem context is incomplete
- Cross-reference status: `async-task-spawning` is a card in this batch; `tokio-overview` and `tokio-runtime` exist in tokio-tutorial; `future-trait-in-depth` exists in tokio-tutorial
