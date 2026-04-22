---
concept: Rust Async and Await
slug: rust-async-await
category: language-semantics
subcategory: concurrency
tier: intermediate
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Async and Await"
chapter_number: 17
pdf_page: null
section: "Futures, Async Syntax, Concurrency with Async, Streams, Future Trait, Pin and Unpin, Tasks and Threads"
extraction_confidence: high
aliases:
  - "async"
  - "await"
  - "futures"
  - "async/await"
  - "streams"
  - "Future trait"
  - "Poll"
  - "Pin"
  - "Unpin"
  - "async runtime"
  - "tasks"
  - "cooperative multitasking"
  - "spawn_task"
prerequisites:
  - rust-concurrency
extends: []
related:
  - rust-concurrency
  - rust-smart-pointers
contrasts_with:
  - rust-concurrency
answers_questions:
  - "What is async/await in Rust?"
  - "What is a Future in Rust?"
  - "How do I run async code in Rust?"
  - "What is an async runtime and why does Rust need one?"
  - "How do futures differ from threads?"
  - "What is the difference between parallelism and concurrency?"
  - "How do I run multiple futures concurrently?"
  - "What are streams in async Rust?"
  - "What is Pin and Unpin?"
  - "How does the Future trait work (poll, Poll::Ready, Poll::Pending)?"
  - "When should I use threads vs. async?"
  - "What is cooperative multitasking in Rust?"
---

# Quick Definition

Rust's async/await system provides cooperative, non-blocking concurrency through futures -- values that represent computations that may not be ready yet. The `async` keyword transforms blocks and functions into state machines that implement the `Future` trait, and `await` yields control to the runtime at suspension points. Unlike threads, futures are lazy (they do nothing until polled), and a runtime is required to drive them to completion. Streams extend futures to represent asynchronous sequences of values.

# Core Definition

**Futures**: "A future is a value that may not be ready now but will become ready at some point in the future." Rust's `Future` trait is the building block: "Each future holds its own information about the progress that has been made and what 'ready' means." Futures in Rust are _lazy_: "they don't do anything until you ask them to with the `await` keyword."

**`async` and `await` Syntax**: "You can apply the `async` keyword to blocks and functions to specify that they can be interrupted and resumed. Within an async block or async function, you can use the `await` keyword to await a future." Rust's `await` is a _postfix_ keyword (`response.text().await`), unlike most other languages, which makes method chaining natural. "When Rust sees a block marked with the `async` keyword, it compiles it into a unique, anonymous data type that implements the `Future` trait." An `async fn` is equivalent to a function returning `impl Future<Output = T>`.

**State Machines**: "Each await point represents a place where control is handed back to the runtime. Rust needs to keep track of the state involved in the async block so that the runtime could kick off some other work and then come back when it's ready to try advancing the first one again. This is an invisible state machine."

**Runtimes**: "Async code needs a runtime: a Rust crate that manages the details of executing asynchronous code." Rust does not bundle a runtime -- "there are many different async runtimes available, each of which makes different tradeoffs." The `main` function cannot be `async`; instead, call a runtime function like `trpl::block_on` (wrapping Tokio) to bridge synchronous and asynchronous code. Some runtimes provide macros (e.g., `#[tokio::main]`) that rewrite `async fn main` into a regular `fn main`.

**Concurrency with Futures**: Use `join` to await two futures concurrently (both must complete). Use `select` to race futures (returns whichever finishes first). The `join!` macro handles a fixed number of futures; `join_all` handles a dynamic collection. `trpl::spawn_task` creates a new async task (similar to `thread::spawn` but for futures). The `async move` block transfers ownership of captured variables, important for ensuring channels close properly.

**Yielding Control**: "Rust only pauses async blocks and hands control back to a runtime at an await point. Everything between await points is synchronous." Long-running synchronous code between await points "starves" other futures. Use `yield_now` to cooperatively hand control back to the runtime without sleeping. "This is a form of cooperative multitasking, where each future has the power to determine when it hands over control via await points."

**Streams**: "A stream is like an asynchronous form of iteration." The `Stream` trait combines `Iterator` and `Future`: its `poll_next` method returns `Poll<Option<Self::Item>>`. Use `StreamExt` (an extension trait) for higher-level APIs like `next()`. "Stream and StreamExt are not yet part of Rust's standard library."

**The `Future` Trait**: Defined as:
```rust
pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}
```
`Poll::Ready(T)` indicates the future has completed; `Poll::Pending` indicates more work remains. The runtime polls futures and puts them back to sleep when pending.

**`Pin` and `Unpin`**: Futures compiled from async blocks may contain self-references between await points. `Pin` wraps a pointer to prevent the pointed-to value from moving in memory, which would invalidate self-references. `Unpin` is a marker trait indicating a type is safe to move even when pinned. Most types implement `Unpin` automatically. Use `Box::pin` or the `pin!` macro when working with trait objects like `Vec<Pin<Box<dyn Future>>>`.

**Tasks vs. Threads**: "Threads act as a boundary for sets of synchronous operations; concurrency is possible between threads. Tasks act as a boundary for sets of asynchronous operations; concurrency is possible both between and within tasks." Tasks are managed by the runtime, not the OS. Many runtimes use _work stealing_ to move tasks between OS threads.

# Prerequisites

- **rust-concurrency** -- understanding threads, `Send`/`Sync`, and the motivation for concurrency is essential context for async

# Key Properties

1. Futures are lazy -- they do nothing until polled (via `await` or a runtime)
2. `async fn` desugars to a function returning `impl Future<Output = T>`
3. `await` is postfix in Rust (`expr.await`), enabling method chaining
4. Every `await` point is a potential suspension/resumption point in the state machine
5. Rust does not include a built-in async runtime; third-party crates (Tokio, async-std) provide them
6. `main` cannot be `async`; use `block_on` or a runtime macro to bridge sync/async
7. `join` runs futures concurrently and waits for all to complete; `select` returns whichever finishes first
8. Code between `await` points executes synchronously -- long-running work starves other futures
9. `yield_now` explicitly yields control to the runtime without sleeping
10. Streams are asynchronous iterators; `poll_next` returns `Poll<Option<Item>>`
11. `Stream`/`StreamExt` are not yet in the standard library but are widely used via the `futures` crate
12. `Pin` prevents self-referential futures from being moved in memory; `Unpin` opts out of this restriction
13. `Box::pin` or `pin!` macro required when storing futures as trait objects in collections
14. Tasks are lightweight, runtime-managed units of work; threads are OS-managed

# Construction / Recognition

## Async Function Equivalence

```rust
// This async function:
async fn page_title(url: &str) -> Option<String> { /* ... */ }

// Is equivalent to:
fn page_title(url: &str) -> impl Future<Output = Option<String>> {
    async move { /* ... */ }
}
```

## Concurrency Combinators

| Combinator | Behavior | Use Case |
|------------|----------|----------|
| `join` / `join!` | Waits for all futures | Run N futures concurrently, need all results |
| `join_all` | Waits for dynamic collection | Unknown number of futures at compile time |
| `select` | Returns first to finish | Racing, timeouts |
| `spawn_task` | Runs future as a separate task | Fire-and-forget or join later |

## Thread vs. Task vs. Future Hierarchy

- **Thread** (OS-managed) -> contains one or more **Tasks** (runtime-managed) -> each task manages one or more **Futures** (most granular unit)

## Building a Timeout with Async Combinators

```rust
async fn timeout<F: Future>(future_to_try: F, max_time: Duration)
    -> Result<F::Output, Duration>
{
    match trpl::select(future_to_try, trpl::sleep(max_time)).await {
        Either::Left(output) => Ok(output),
        Either::Right(_) => Err(max_time),
    }
}
```

## Pin for Dynamic Future Collections

```rust
let futures: Vec<Pin<Box<dyn Future<Output = ()>>>> = vec![
    Box::pin(async { /* task 1 */ }),
    Box::pin(async { /* task 2 */ }),
];
trpl::join_all(futures).await;
```

# Context & Application

- **Typical contexts**: I/O-bound operations (network requests, file I/O, database queries), web servers, concurrent API calls, event-driven systems.
- **Common applications**: Fetching multiple web pages concurrently; implementing timeouts around slow operations; processing streams of events (WebSocket messages, database cursors); building non-blocking servers with Tokio or async-std.
- **When to use threads vs. async**: "If the work is very parallelizable (CPU-bound), threads are a better choice. If the work is very concurrent (I/O-bound), async is a better choice." The two can be combined -- use threads for compute-heavy work and async channels for coordination.
- **Async move blocks**: Use `async move { }` when the async block needs to own captured variables, particularly important for ensuring channel senders are dropped to signal completion.

# Examples

**Example 1** -- Basic async function with `block_on` (Ch. 17, "Executing an Async Function with a Runtime"):
```rust
fn main() {
    trpl::block_on(async {
        let url = "https://www.rust-lang.org";
        match page_title(url).await {
            Some(title) => println!("Title: {title}"),
            None => println!("No title found"),
        }
    });
}
```

**Example 2** -- Racing two futures with `select` (Ch. 17, "Racing Two URLs"):
```rust
let title_fut_1 = page_title(&args[1]);
let title_fut_2 = page_title(&args[2]);
let (url, maybe_title) = match trpl::select(title_fut_1, title_fut_2).await {
    Either::Left(left) => left,
    Either::Right(right) => right,
};
```

**Example 3** -- Async message passing (Ch. 17, "Sending Data Between Two Tasks"):
```rust
let (tx, mut rx) = trpl::channel();
let tx_fut = async move {
    for val in ["hi", "from", "the", "future"] {
        tx.send(val).unwrap();
        trpl::sleep(Duration::from_millis(500)).await;
    }
};
let rx_fut = async {
    while let Some(value) = rx.recv().await {
        println!("received '{value}'");
    }
};
trpl::join(tx_fut, rx_fut).await;
```

**Example 4** -- Mixing threads and async (Ch. 17, "Putting It All Together"):
```rust
let (tx, mut rx) = trpl::channel();
// Blocking work on a dedicated thread
thread::spawn(move || {
    for i in 1..=10 {
        tx.send(i).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});
// Async processing of results
trpl::block_on(async {
    while let Some(msg) = rx.recv().await {
        println!("{msg}");
    }
});
```

# Relationships

## Builds Upon
- **rust-concurrency** -- threads, `Send`/`Sync`, and the motivation for concurrency provide the foundation

## Enables
No directly enabled cards within this batch.

## Related
- **rust-concurrency** -- threads and async are complementary concurrency approaches
- **rust-smart-pointers** -- `Pin` works with smart pointers (`Box`, `Rc`, `Arc`); async trait objects use `Box<dyn Future>`

## Contrasts With
- **rust-concurrency** -- threads use OS scheduling (preemptive); async uses cooperative multitasking with explicit await points

# Common Errors

- **Error**: Marking `main` as `async fn`, getting "main function is not allowed to be async."
  **Correction**: Use `trpl::block_on(async { ... })` or a runtime macro like `#[tokio::main]` to set up the runtime within a normal `main`.

- **Error**: Putting all async operations in a single async block and expecting them to run concurrently.
  **Correction**: "Within a given async block, the order in which await keywords appear in the code is also the order in which they're executed." Separate independent operations into their own async blocks and use `join` or `join!` to run them concurrently.

- **Error**: Storing futures of different async blocks in a `Vec` without pinning, getting "`dyn Future<Output = ()>` cannot be unpinned."
  **Correction**: Use `Box::pin(async { ... })` to create `Pin<Box<dyn Future>>` values that can be collected and passed to `join_all`.

# Common Confusions

- **Confusion**: Futures start executing as soon as they are created, like threads.
  **Clarification**: "Futures in Rust are lazy: they don't do anything until you ask them to with the await keyword." This is different from `thread::spawn`, where the closure runs immediately.

- **Confusion**: `async` and `await` are a complete concurrency solution without any additional runtime.
  **Clarification**: "Async code needs a runtime" -- Rust deliberately does not bundle one. You must use a third-party runtime like Tokio, async-std, or smol. The `async`/`await` syntax only generates state machines; the runtime drives them.

- **Confusion**: Async is always faster than threads.
  **Clarification**: For CPU-bound work, threads are often better. Async excels at I/O-bound concurrency where many tasks spend most of their time waiting. "If the work is very parallelizable, threads are a better choice."

# Source Reference

The Rust Programming Language, Chapter 17: Async and Await -- Futures, Async Syntax, Concurrency with Async, Streams, the Future Trait, Pin and Unpin, Tasks and Threads.

# Verification Notes

- Definition source: Direct from Chapter 17 of The Rust Programming Language
- Confidence rationale: High -- this is the newest chapter in TRPL, covering stable async/await syntax and ecosystem patterns
- Uncertainties: `Stream` and `StreamExt` are not yet in the standard library (ecosystem trait from `futures` crate); the exact trait definition may evolve
- Cross-reference status: Related cards verified against planned card slugs (rust-concurrency, rust-smart-pointers)
