---
concept: Tokio Task Spawning
slug: tokio-spawn
category: async-runtime
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "03-spawning"
chapter_number: 3
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "tokio::spawn"
  - "Tokio tasks"
  - "async green threads"
  - "task spawning"
  - "JoinHandle"
prerequisites:
  - tokio-runtime
extends:
  - tokio-runtime
related:
  - tokio-shared-state
  - tokio-channels
  - tokio-select
  - tokio-executor
contrasts_with: []
answers_questions:
  - "How do I run tasks concurrently in Tokio?"
  - "What is tokio::spawn?"
  - "What is a Tokio task?"
  - "Why must spawned tasks be 'static?"
  - "Why must spawned tasks be Send?"
  - "How much memory does a Tokio task use?"
  - "What is the difference between concurrency and parallelism in Tokio?"
---

# Quick Definition

`tokio::spawn` creates a new asynchronous task (a lightweight green thread) that runs concurrently with other tasks on the Tokio runtime. Each task is an independent unit of execution managed by the scheduler, requiring only 64 bytes of memory. Spawned tasks must satisfy two bounds: `'static` (no borrowed references to external data) and `Send` (safe to move between threads).

# Core Definition

"A Tokio task is an asynchronous green thread. They are created by passing an `async` block to `tokio::spawn`. The `tokio::spawn` function returns a `JoinHandle`, which the caller may use to interact with the spawned task. The `async` block may have a return value. The caller may obtain the return value using `.await` on the `JoinHandle`." (Ch. 3, "Tasks")

"Tasks are the unit of execution managed by the scheduler. Spawning the task submits it to the Tokio scheduler, which then ensures that the task executes when it has work to do. The spawned task may be executed on the same thread as where it was spawned, or it may execute on a different runtime thread. The task can also be moved between threads after being spawned." (Ch. 3, "Tasks")

"Tasks in Tokio are very lightweight. Under the hood, they require only a single allocation and 64 bytes of memory. Applications should feel free to spawn thousands, if not millions of tasks." (Ch. 3, "Tasks")

# Prerequisites

- **tokio-runtime** -- understanding the Tokio runtime, `#[tokio::main]`, and async/await is necessary before spawning tasks onto that runtime

# Key Properties

1. `tokio::spawn` accepts an `async` block (or any `Future`) and submits it to the Tokio scheduler as an independent task
2. Returns a `JoinHandle` that can be `.await`ed to get the task's return value (wrapped in `Result` to handle panics)
3. Awaiting a `JoinHandle` returns `Err` if the task panicked or was forcefully cancelled by runtime shutdown
4. Tasks require only a single allocation and 64 bytes of memory -- spawning thousands or millions is expected
5. Tasks may execute on any runtime thread and may be moved between threads during execution
6. **`'static` bound**: The spawned task must not contain references to data owned outside the task; use `move` to transfer ownership into the async block, or `Arc` to share data
7. **`Send` bound**: All data held across `.await` points must be `Send`, because the task can be moved between threads at any `.await`
8. Data that is dropped before an `.await` point does not need to be `Send` (it is not persisted in the task's state)
9. Concurrency (interleaving work on one or more threads) is distinct from parallelism (simultaneous execution on multiple threads); Tokio can run many tasks concurrently even on a single thread

# Construction / Recognition

## Sequential Processing (No Concurrency):
```rust
loop {
    let (socket, _) = listener.accept().await.unwrap();
    process(socket).await;  // Blocks the loop until this connection finishes
}
```
Each connection is fully processed before the next is accepted.

## Concurrent Processing with `tokio::spawn`:
```rust
loop {
    let (socket, _) = listener.accept().await.unwrap();
    tokio::spawn(async move {
        process(socket).await;  // Runs independently, loop continues immediately
    });
}
```
Each connection is processed in its own task. The accept loop continues immediately, enabling concurrent handling of many connections.

## Satisfying the `'static` Bound:
- Use `async move { ... }` to transfer ownership of captured variables into the task
- For shared data, wrap in `Arc` and clone before moving into the task

## Satisfying the `Send` Bound:
- Ensure all data held across `.await` points implements `Send`
- Non-`Send` types (like `Rc`) can be used if they are dropped before any `.await`
- Scope non-`Send` values in a block so they are dropped before yielding

# Context & Application

The spawning chapter marks the transition from sequential async code to concurrent async code in the tutorial. The Mini-Redis server begins by accepting TCP connections in a loop and processing each one sequentially -- which means only one client can be served at a time. By introducing `tokio::spawn`, each connection gets its own task, enabling the server to handle many clients concurrently.

The `'static` and `Send` bounds are the two key constraints that Rust's type system imposes on spawned tasks, and understanding them is essential for practical Tokio programming:

- The `'static` bound exists because the scheduler cannot know how long a task will live. Since a spawned task runs independently of its parent, it might outlive the scope that created it. Therefore, it must own all its data (or share via `Arc`).

- The `Send` bound exists because the multi-threaded runtime can move tasks between OS threads at any `.await` point. All state that persists across a yield point must be safe to transfer between threads.

The chapter also introduces the per-connection `HashMap` pattern for storing state. Each task has its own `HashMap`, which means data is not shared between connections -- a limitation addressed in the next chapter (shared state).

# Examples

**Example 1** (Ch. 3, JoinHandle usage):
```rust
#[tokio::main]
async fn main() {
    let handle = tokio::spawn(async {
        "return value"
    });
    let out = handle.await.unwrap();
    println!("GOT {}", out);
}
```
The spawned task returns a value. `.await` on the `JoinHandle` retrieves it, with `unwrap()` handling the potential panic case.

**Example 2** (Ch. 3, `'static` bound -- compile error and fix):
```rust
// This FAILS: v is borrowed, not moved
let v = vec![1, 2, 3];
task::spawn(async {
    println!("Here's a vec: {:?}", v);  // borrows v
});

// This WORKS: async move transfers ownership
let v = vec![1, 2, 3];
task::spawn(async move {
    println!("Here's a vec: {:?}", v);  // owns v
});
```
The `'static` bound means the task cannot borrow from its parent scope. The `move` keyword transfers ownership into the task.

**Example 3** (Ch. 3, `Send` bound -- `Rc` across `.await`):
```rust
// This WORKS: rc is dropped before .await
tokio::spawn(async {
    {
        let rc = Rc::new("hello");
        println!("{}", rc);
    }
    // rc is dropped here, not held across yield
    yield_now().await;
});

// This FAILS: rc is held across .await
tokio::spawn(async {
    let rc = Rc::new("hello");
    yield_now().await;       // rc persists across this yield
    println!("{}", rc);      // rc used after .await
});
```
`Rc` is not `Send`. It can exist within a task as long as it is not held across an `.await` point.

**Example 4** (Ch. 3, Concurrency vs. parallelism): "Concurrency and parallelism are not the same thing. If you alternate between two tasks, then you are working on both tasks concurrently, but not in parallel. For it to qualify as parallel, you would need two people, one dedicated to each task. One of the advantages of using Tokio is that asynchronous code allows you to work on many tasks concurrently, without having to work on them in parallel using ordinary threads. In fact, Tokio can run many tasks concurrently on a single thread!"

# Relationships

## Builds Upon
- **tokio-runtime** -- tasks are spawned onto the runtime; the scheduler provided by the runtime manages their execution

## Enables
- **tokio-shared-state** -- once tasks run concurrently, they need mechanisms (Mutex, RwLock, Arc) to share state safely
- **tokio-channels** -- message passing provides an alternative to shared state for inter-task communication

## Related
- **tokio-executor** -- the scheduler internals that determine how spawned tasks are polled and moved between threads
- **tokio-select** -- an alternative concurrency model that multiplexes futures within a single task rather than spawning separate tasks

## Contrasts With
- Sequential `.await` within a single task (no concurrency -- each operation completes before the next begins)
- `std::thread::spawn` (OS threads are heavier: ~8KB stack per thread vs. 64 bytes per Tokio task; OS-scheduled rather than cooperatively scheduled)

# Common Errors

- **Error**: Forgetting `async move` when the spawned task uses variables from the parent scope.
  **Correction**: Without `move`, variables are borrowed rather than owned, violating the `'static` bound. Use `async move { ... }` to transfer ownership. If data must be shared, clone an `Arc` and move the clone into the task.

- **Error**: Holding a non-`Send` type (like `Rc`, `MutexGuard` from `std::sync::Mutex`) across an `.await` point in a spawned task.
  **Correction**: Either drop the non-`Send` value before the `.await` (using a scoping block), or replace it with a `Send` alternative (e.g., `Arc` instead of `Rc`, `tokio::sync::Mutex` instead of `std::sync::Mutex`).

- **Error**: Ignoring the `JoinHandle` returned by `tokio::spawn`, losing the ability to detect task panics.
  **Correction**: If the task's result matters (or panics should be detected), store and `.await` the `JoinHandle`. The `JoinHandle` returns `Err` if the task panicked.

# Common Confusions

- **Confusion**: Thinking `'static` means the value must live for the entire program duration.
  **Clarification**: "'static" as a bound means the type contains no non-static references -- it owns all its data. The value itself can be created and destroyed at any time. "Just because a value is `'static` does not mean that you have a memory leak."

- **Confusion**: Thinking all data in a spawned task must be `Send`.
  **Clarification**: Only data held across `.await` points must be `Send`. Non-`Send` types can be used freely within a task as long as they are dropped before any `.await`. The compiler tracks this precisely.

- **Confusion**: Conflating concurrency with parallelism in Tokio.
  **Clarification**: Tokio provides concurrency (interleaved execution of many tasks). With a multi-threaded runtime, some of that concurrency may also be parallel. With a single-threaded runtime, tasks are concurrent but never parallel. The key benefit is handling many I/O-bound operations without needing one OS thread per operation.

# Source Reference

Chapter 3: Spawning, all sections -- "Accepting sockets," "Concurrency," "Tasks," "`'static` bound," "`Send` bound," and "Store values." The chapter progresses from a sequential accept loop to concurrent per-connection tasks, explaining the task model and its constraints along the way.

# Verification Notes

- Definition source: Direct quotations from Ch. 3, "Tasks" section
- `'static` bound: Explained with compile error example and the clarification that `'static` does not mean "lives forever"
- `Send` bound: Demonstrated with `Rc` examples showing both the passing and failing cases
- Memory cost (64 bytes): Directly stated in Ch. 3, "Tasks"
- Confidence rationale: HIGH -- the source provides explicit definitions, compiler error messages, and multiple code examples for each constraint
- Uncertainties: None
- Cross-reference status: Agent B slugs (tokio-shared-state, tokio-channels) and Agent C slugs (tokio-executor, tokio-select) referenced per assignment
