---
concept: Async IO Model
slug: async-io-model
category: async-programming
subcategory: null
tier: foundational
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "IO and issues with blocking"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - "non-blocking IO"
  - "async IO"
  - "asynchronous IO in Rust"
prerequisites:
  - async-await-basics
  - async-advanced-topics
extends: []
related:
  - async-programming-overview
  - async-concurrency-composition
  - async-cancellation-cleanup
contrasts_with: []
answers_questions:
  - "What is the difference between blocking and non-blocking IO in async Rust?"
  - "Why does blocking IO break async programs?"
  - "How do I use async IO in Rust?"
  - "How should I handle CPU-intensive work in an async program?"
  - "What is spawn_blocking and when should I use it?"
  - "What is yielding in async Rust?"
---

# Quick Definition

Async IO is the model of performing input/output operations without blocking the OS thread, allowing the async runtime to schedule other tasks while IO completes. In Rust, the standard library provides only blocking IO; async IO requires runtime-specific libraries (e.g., Tokio's `io` module). Mixing blocking IO with async tasks is the primary source of performance problems in async programs.

# Core Definition

"Efficiently handling IO is one of the primary motivators for async programming and most async programs do lots of IO. At its root, the issue with IO is that it takes orders of magnitude more time than computation, therefore just waiting for IO to complete rather than getting on with other work is incredibly inefficient." (Ch. 4, introduction)

"IO can be either synchronous or asynchronous (aka blocking and non-blocking, respectively). Synchronous IO means that the program (or at least the thread) waits (aka blocks) while the IO takes place and doesn't start processing until the IO is complete. Asynchronous IO means that the program can continue to make progress while the IO takes place and can pick up the result later." (Ch. 4, "Blocking and non-blocking IO")

"Asynchronous IO and asynchronous programming are not intrinsically linked. However, async programming facilitates ergonomic and performant async IO, and that is a major motivation for async programming." (Ch. 4, "Blocking and non-blocking IO")

"Rust's standard library includes functions and traits for blocking IO. For non-blocking IO, you must use specialized libraries, which are often part of the async runtime, e.g., Tokio's `io` module." (Ch. 4, "Blocking and non-blocking IO")

The consequences of using blocking IO in async context are severe: "if we used a write function from the standard library, the async scheduler would not be involved and the OS would pause the whole thread while the IO completes, meaning that not only is the current task paused but no other task can be executed using that thread. If this happens to all threads in the runtime's thread pool (which in some circumstances can be just one thread), then the whole program stops and cannot make progress. This is called blocking the thread and is very bad for performance." (Ch. 4, "Blocking and non-blocking IO")

# Prerequisites

- **async-await-basics** -- understanding async/await syntax and futures is needed to use async IO operations
- **async-advanced-topics** -- the concept of blocking introduced in Ch. 3 is central to understanding why async IO matters

# Key Properties

1. IO takes orders of magnitude longer than computation, making it the primary motivator for async programming
2. Blocking IO pauses the entire OS thread, starving all async tasks on that thread
3. Non-blocking IO only pauses the current task while the runtime schedules other tasks
4. Rust's standard library provides only blocking IO; async IO requires runtime libraries
5. If all threads in the runtime's thread pool block, the entire program stops
6. Blocking can also be caused by long-running computation, non-async synchronization primitives, or busy-waiting
7. CPU-intensive work prevents the scheduler from running other tasks (cooperative multitasking)
8. Three solutions for long-running/blocking work: `spawn_blocking`, separate thread, or separate runtime
9. `spawn_blocking` runs synchronous code on a separate thread pool optimized for blocking tasks
10. Long-running async tasks should yield periodically (every 10-100 microseconds) to allow other tasks to run

# Construction / Recognition

## To Use Async IO Correctly:
1. Use the runtime's IO modules (e.g., `tokio::io`, `tokio::net`, `tokio::fs`) instead of `std::io`, `std::net`, `std::fs`
2. Await all IO operations to allow the runtime to schedule other tasks during waits
3. Never call blocking IO functions from within an async task without wrapping them

## To Handle Blocking/CPU-Intensive Work:
1. For blocking IO that cannot be avoided, use `spawn_blocking` to offload to a blocking-aware thread pool
2. For CPU-intensive work, use a separate thread pool (e.g., Rayon) or a second runtime instance
3. For long-lived blocking threads, use `std::thread::spawn` directly rather than consuming a pool thread
4. For long-running async code, use a separate runtime configured for that workload
5. Insert `yield_now().await` calls in CPU-intensive loops to give the scheduler opportunities to run other tasks

## To Choose Between Solutions for Blocking Work:
1. Blocking IO -> `spawn_blocking` (required for optimal performance)
2. Permanent thread -> `std::thread::spawn` (avoids tying up pool threads)
3. Lots of CPU work -> thread pool (Rayon) or second async runtime
4. Long-running async code -> second runtime (only option that supports async tasks)
5. Simple cases -> `spawn_blocking` or dedicated thread for ease, even if not theoretically optimal

# Context & Application

The chapter emphasizes that the blocking/non-blocking distinction is the most practically important concept in async Rust performance. Async IO is not inherently tied to async programming, but async programming makes async IO ergonomic.

The source details how async IO works mechanically: "write_all is an async IO method which writes data to stream. This might complete immediately, but more likely this will take some time to complete, so stream.write_all(...).await will cause the current task to be paused while it waits for the OS to handle the write. The scheduler will run other tasks and when the write is complete, it will wake up the task and schedule it to continue working." (Ch. 4, "Blocking and non-blocking IO")

For CPU-intensive work, the source provides nuanced guidance: "There is a meme that you should simply not use async Rust for CPU-intensive work, but that is an over-simplification. What is correct is that you cannot mix IO- and CPU-bound tasks without some special handling and expect to have a good time." (Ch. 4, "CPU-intensive work")

When using multiple runtimes or mixed sync/async contexts, synchronization requires care: "you need to take care that you are using the correct combinations of sync and async primitives and the correct (blocking or non-blocking) methods on those primitives." Tokio channels can be used across contexts with blocking methods, but each runtime "is its own little universe of tasks and the schedulers are totally independent." (Ch. 4, "Other blocking operations")

On yielding: "Calling `yield_now` won't yield to the scheduler if the current future is being run inside a `select` or `join`." A rule of thumb: "code should not run for more than 10-100 microseconds without hitting a potential yield point." (Ch. 4, "Yielding")

# Examples

**Example 1 -- Async IO with Tokio** (Ch. 4, "Blocking and non-blocking IO"):
```rust
use tokio::{io::AsyncWriteExt, net::TcpStream};

async fn write_hello() -> Result<(), Box<dyn std::error::Error>> {
    let mut stream = TcpStream::connect("127.0.0.1:8080").await?;
    stream.write_all(b"hello world!").await?;
    Ok(())
}
```
The `write_all` call pauses only the current task; the runtime schedules other tasks while the OS handles the write. Using `std::io::Write` instead would block the entire thread.

**Example 2 -- Decision guide for blocking work** (Ch. 4, "Other blocking operations"):
The source provides explicit guidance:
- "If you're doing blocking IO, you should probably use `spawn_blocking`."
- "If you have a thread that will run forever, you should use `std::thread::spawn`."
- "If you're doing lots of CPU work, then you should use a thread pool, either a specialised one or a second async runtime."
- "If you need to run long-running async code, then you should use a second runtime."

# Relationships

## Builds Upon
- **async-await-basics** -- async IO uses the async/await model for ergonomic non-blocking operations
- **async-advanced-topics** -- extends the blocking concepts introduced in Ch. 3

## Enables
- **async-concurrency-composition** -- async IO operations are the primary futures composed with join/select

## Related
- **async-programming-overview** -- IO efficiency is the primary motivation for async programming
- **async-cancellation-cleanup** -- IO operations may need cleanup when cancelled

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `std::fs::read_to_string` or `std::net::TcpStream` inside an async task.
  **Correction**: Use `tokio::fs::read_to_string` or `tokio::net::TcpStream` (or equivalent from your runtime). If you must use blocking IO, wrap it in `spawn_blocking`.

- **Error**: Running CPU-intensive loops without yielding inside async tasks.
  **Correction**: Insert `tokio::task::yield_now().await` periodically, or offload the work to `spawn_blocking` or a dedicated thread pool. The rule of thumb is to yield every 10-100 microseconds.

- **Error**: Using `std::thread::sleep` instead of `tokio::time::sleep` in async code.
  **Correction**: Always use the runtime's sleep function. `std::thread::sleep` blocks the OS thread, starving other tasks.

- **Error**: Using `std::sync::Mutex` where it might be held across an await point.
  **Correction**: Use an async mutex (e.g., `tokio::sync::Mutex`) when the lock must be held across await points. Use `std::sync::Mutex` only when the lock is not held across await points and contention is low.

# Common Confusions

- **Confusion**: Thinking async IO and async programming are the same thing.
  **Clarification**: "Asynchronous IO and asynchronous programming are not intrinsically linked." Async programming is a broader paradigm; async IO is one (important) application of it.

- **Confusion**: Thinking `spawn_blocking` runs async code.
  **Clarification**: "`spawn_blocking` runs regular synchronous code, not an async task. That means that the task can't be cancelled (even though its `JoinHandle` has an `abort` method)."

- **Confusion**: Thinking any `.await` will yield to the scheduler.
  **Clarification**: "await doesn't automatically yield to the scheduler. That only happens if the leaf future being awaited is pending (not ready) or there is an explicit yield somewhere in the call stack."

# Source Reference

Chapter 4: "IO and issues with blocking" -- all sections. The "Blocking and non-blocking IO" section and "Other blocking operations" section (including "CPU-intensive work" and "Yielding" subsections) are fully written. The "Reading and writing," "Memory management," "Advanced topics on IO," and "OS view of IO" sections are TODO stubs with bullet-point outlines.

# Verification Notes

- Definition source: Direct quotations from Ch. 4 "Blocking and non-blocking IO" and "Other blocking operations" sections
- Key Properties: All from explicit statements in fully-written sections
- Confidence rationale: MEDIUM -- the blocking vs non-blocking distinction and the solutions for blocking work are thoroughly developed with clear prose and examples; however, the "Reading and writing," "Memory management," "Advanced topics on IO," and "OS view of IO" sections are TODO stubs. The fully-written portions (which are the most important parts) are high confidence; overall medium due to incomplete sections.
- Uncertainties: The stub sections on async Read/Write traits, memory management (zero-copy, buffer management), and OS-level IO mechanisms (io_uring, mio, completion IO) will likely add significant content when completed
- Cross-reference status: `async-await-basics` and `async-programming-overview` are from Agent A's Ch. 1-2 extraction; other slugs are in this extraction set
