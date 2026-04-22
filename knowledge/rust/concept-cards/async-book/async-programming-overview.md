---
concept: Async Programming Overview
slug: async-programming-overview
category: async-programming
subcategory: null
tier: foundational
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "00-introduction, 01-concurrent-programming"
chapter_number: 0
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "async concurrency"
  - "async vs threads"
  - "concurrent programming models"
prerequisites: []
extends: []
related:
  - async-await-basics
  - async-task-spawning
  - tokio-overview
  - structured-concurrency
contrasts_with:
  - tokio-overview
answers_questions:
  - "What is async programming and why would you use it?"
  - "How does async concurrency differ from thread-based concurrency?"
  - "What is the difference between concurrency and parallelism?"
  - "What is cooperative vs preemptive multitasking?"
  - "Why is async programming more efficient than threads?"
---

# Quick Definition

Async programming is a form of concurrent programming where tasks are managed entirely within the program (not by the OS), using cooperative multitasking. Tasks voluntarily yield control at explicit points, enabling very low context-switching overhead and memory usage compared to OS threads.

# Core Definition

"In concurrent programming, the program does multiple things at the same time (or at least appears to). Programming with threads is one form of concurrent programming. Code within a thread is written in sequential style and the operating system executes threads concurrently. With async programming, concurrency happens entirely within your program (the operating system is not involved). An async runtime (which is just another crate in Rust) manages async tasks in conjunction with the programmer explicitly yielding control by using the `await` keyword." (Ch. 0, "What is Async Programming and why would you do it?")

"Async programming is a kind of concurrency with the same high-level goals as concurrency with threads (do many things at the same time), but a different implementation. The two big differences between async concurrency and concurrency with threads, is that async concurrency is managed entirely within the program with no help from the OS, and that multitasking is cooperative rather than pre-emptive." (Ch. 1, "Async programming")

The source frames concurrency and parallelism as distinct concepts: "Concurrency is about ordering of computations and parallelism is about the mode of execution." Another framing offered is that "concurrency is a way of organizing code and parallelism is a resource." (Ch. 1, "Concurrency and Parallelism")

# Prerequisites

This is a foundational overview concept. The source assumes familiarity with Rust but not with async programming: "We don't assume any experience with asynchronous programming (in Rust or another language), but we do assume you're familiar with Rust already." (Ch. 0, Introduction)

# Key Properties

1. Async concurrency is managed entirely within the program, with no OS involvement for scheduling or task management
2. Multitasking is **cooperative** -- tasks must voluntarily yield control -- as opposed to the **preemptive** multitasking used by OS threads
3. Between yield points, code executes sequentially and cannot be unexpectedly paused by the scheduler
4. If a task takes too long between yield points (blocking IO or long computation), other tasks cannot make progress
5. Async context switching is much cheaper than thread context switching -- no OS involvement, no register/TLB/cache flushing
6. Async tasks have much lower memory overhead than OS threads, enabling orders of magnitude more concurrent tasks
7. Concurrency is about ordering of computations (concurrent operations have no observable ordering); parallelism is about literal simultaneous execution on multiple processors
8. Parallelism is a resource -- only the number of processor cores matters, not how code is organized with respect to concurrency
9. Both threaded and async systems can offer both concurrency and parallelism; the difference is in overhead and control granularity
10. Threads and async are not mutually exclusive -- many programs use both, and async runtimes typically execute tasks across multiple OS threads

# Construction / Recognition

## Sequential vs Concurrent vs Parallel Execution (from Ch. 1)

1. **Sequential**: Subtasks execute one after another in order; no concurrency
2. **Concurrent (interleaved)**: Subtasks from different tasks are interleaved on a single processor; from each task's perspective, its own subtasks still execute sequentially
3. **Parallel**: Subtasks from different tasks execute literally at the same time on different processors; this is also concurrent

## When Async Is a Good Fit

1. Systems with very many concurrent tasks that spend a lot of time waiting (e.g., for client responses or IO)
2. Microcontrollers with limited memory and no OS-provided threads
3. Applications requiring fine-grained control over task scheduling, cancellation, and composition

## Thread-Based vs Async IO (from Ch. 1)

- **Threads**: Thread requests IO from OS, OS pauses thread, other threads work, OS wakes thread on completion
- **Async**: Task requests IO from runtime, runtime requests IO from OS (non-blocking), runtime pauses task and schedules others, runtime wakes task on completion

# Context & Application

The source presents async programming as the third major execution model after sequential execution and threads/processes. The key insight is that async concurrency trades the simplicity of OS-managed preemptive scheduling for dramatically lower overhead, making it practical to handle thousands or millions of concurrent tasks.

The cooperative multitasking model has important implications: code between yield points runs atomically from the scheduler's perspective (you will never be "unexpectedly paused"), but this places responsibility on the programmer to yield regularly. A task that performs blocking IO or long computation without yielding will starve all other tasks on that thread.

The source emphasizes that concurrency and parallelism are orthogonal concerns. Adding concurrency without parallelism never makes a system faster (though it can improve responsiveness). In async Rust, Tokio's default multi-threaded runtime provides both concurrency and parallelism, similar to threads. However, async Rust also offers constructs for concurrency without parallelism (e.g., `join` and `select`), which have no thread-based equivalent.

This card captures the async-book's unique tutorial-style presentation of these concepts. The tokio-tutorial's `tokio-overview` card covers similar ground but from Tokio's specific perspective; the async-reference cards cover formal semantics.

# Examples

**Example 1** (Ch. 0, "Hello, world!"): The source provides a minimal async hello-world that defines and calls an async function using `.await`. The key observation: "an async function in Rust doesn't do anything unless it is `await`ed." The example deliberately uses `println` (blocking IO) and the source notes in a footnote that this is "actually a bad example because `println` is blocking IO and it is generally a bad idea to do blocking IO in async functions."

**Example 2** (Ch. 1, cooperative multitasking implications): The source lists three consequences of cooperative multitasking:
- Between yield points, execution is guaranteed sequential -- "you'll never be unexpectedly paused"
- Long-running code between yield points starves other tasks
- Scheduler implementation is simpler with fewer context-switching overheads

**Example 3** (Ch. 1, concurrency vs parallelism pseudocode): The source uses a pseudocode model of tasks with 100 subtasks each to illustrate sequential execution (all of task 1 then task 2), concurrent interleaved execution (alternating subtasks on one processor), and parallel execution (different processors handling different tasks simultaneously). The key observation: "no matter how much concurrency we add, the whole job takes the same amount of time to complete" -- only parallelism reduces total time.

# Relationships

## Builds Upon

- Sequential programming and basic Rust familiarity (explicitly stated as the only prerequisite)

## Enables

- **async-await-basics** -- the practical syntax and mechanics of async programming in Rust
- **async-task-spawning** -- creating concurrent tasks using `spawn`

## Related

- **tokio-overview** -- Tokio's perspective on async runtime selection and when to use async
- **structured-concurrency** -- advanced concurrency patterns built on async primitives

## Contrasts With

- **tokio-overview** -- this card covers the general async programming model; tokio-overview covers Tokio's specific runtime and ecosystem

# Common Errors

- **Error**: Performing blocking IO or long computation in an async task without yielding.
  **Correction**: In cooperative multitasking, a task that doesn't yield starves all other tasks on its thread. Use async IO operations or `spawn_blocking` for blocking work.

- **Error**: Assuming more concurrency will make a program faster.
  **Correction**: Concurrency is about code organization, not speed. "Increasing the concurrency of a system without increasing parallelism can never make it faster" -- only parallelism (more CPU cores doing work) reduces total execution time.

# Common Confusions

- **Confusion**: Using "concurrency" and "parallelism" interchangeably.
  **Clarification**: Concurrency means operations have no observable ordering (they could be interleaved on one core). Parallelism means operations literally happen at the same time on different cores. Concurrent execution on a single core takes the same total time as sequential; parallel execution reduces total time.

- **Confusion**: Thinking async replaces threads entirely.
  **Clarification**: "Threads and async are not mutually exclusive: many programs use both." A database server might use async for network IO but OS threads for computation. Async runtimes themselves typically execute tasks across multiple OS threads for parallelism.

- **Confusion**: Thinking that async tasks are like green threads with preemptive scheduling.
  **Clarification**: Rust's async tasks use cooperative multitasking -- they yield control explicitly via `await`. The source notes that Go uses preemptive user-space scheduling (green threads) but Rust deliberately chose cooperative scheduling because it avoids the need for a heavyweight runtime and simplifies interop with other languages and the OS.

# Source Reference

Chapter 0: Introduction (all sections -- "What is Async Programming and why would you do it?", "Hello, world!", "Development of Async Rust") and Chapter 1: Concurrent programming (all sections -- "Sequential execution", "Processes and threads", "Async programming", "Concurrency and Parallelism", "Summary").

# Verification Notes

- Definition source: Direct quotations from Ch. 0 introduction and Ch. 1 "Async programming" section
- Key Properties: Synthesized from Ch. 0 motivation and Ch. 1's detailed comparison of execution models
- Concurrency vs parallelism framing: Direct from Ch. 1, including the Aaron Turon attribution in footnote
- Confidence: HIGH -- the source provides extensive, well-written prose covering these concepts thoroughly
- Uncertainties: The source notes it is "currently undergoing a rewrite" and is "work in progress, much is missing." However, Chapters 0-1 appear complete with full prose.
- Cross-reference status: `async-await-basics` and `async-task-spawning` are cards in this batch; `tokio-overview` exists in tokio-tutorial; `structured-concurrency` exists in async-reference
