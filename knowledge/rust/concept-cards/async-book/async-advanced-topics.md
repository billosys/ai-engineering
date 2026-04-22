---
concept: Advanced Async/Await Topics
slug: async-advanced-topics
category: async-programming
subcategory: null
tier: intermediate
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "More async/await topics"
chapter_number: 3
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - "async blocks and closures"
  - "async unit testing"
  - "async Send and static"
  - "async traits"
prerequisites:
  - async-await-basics
extends:
  - async-await-basics
related:
  - async-programming-overview
  - async-cancellation-cleanup
  - async-concurrency-composition
  - cancellation-safety
contrasts_with: []
answers_questions:
  - "How do I unit test async code in Rust?"
  - "What is blocking in async Rust and why is it dangerous?"
  - "What are async blocks and how do they differ from async functions?"
  - "What are the Send + 'static bounds on futures and why do they exist?"
  - "How do async traits work in Rust?"
  - "Can async functions be recursive?"
  - "What is cancellation in async Rust?"
---

# Quick Definition

Chapter 3 of the Async Book covers essential intermediate topics for working with async/await: unit testing async code, understanding blocking and cancellation, async blocks and closures, lifetime and borrowing issues, `Send + 'static` bounds, async traits, and recursion. These topics go beyond basic async/await syntax to address the practical subtleties of writing correct async Rust.

# Core Definition

The chapter covers several interconnected topics that arise once a programmer moves beyond basic async/await usage:

**Unit testing**: "How to unit test async code? The issue is that you can only await from inside an async context, and unit tests in Rust are not async. Luckily, most runtimes provide a convenience attribute for tests similar to the one for `async main`." The Tokio example uses `#[tokio::test]` on an `async fn`. (Ch. 3, "Unit tests")

**Blocking**: "We say a thread is blocked when it can't make any progress. That's usually because it is waiting for the OS to complete a task on its behalf. [...] in an async program, there are other tasks which should be scheduled on the same OS thread, but the OS doesn't know about those and keeps the whole thread waiting. This means that rather than the single task waiting for its I/O to complete (which is fine), many tasks have to wait (which is not fine)." Blocking computation has a similar effect: "If you have a long-running computation without yielding control to the runtime, then that task will never give the runtime's scheduler a chance to schedule other tasks." (Ch. 3, "Blocking and cancellation")

**Cancellation**: "Cancellation means stopping a future (or task) from executing. Since in Rust futures must be driven forward by an external force, if a future is no longer driven forward then it will not execute any more. If a future is dropped, then it can never make any more progress and is canceled." Cancellation can occur by dropping a future, calling `abort` on a `JoinHandle`, via a `CancellationToken`, or implicitly via `select`. "From the perspective of writing async code, the code might stop executing at any `await` and never start again." (Ch. 3, "Blocking and cancellation")

**Async blocks**: "An async block is a deferred version of a regular block. An async block scopes code and names together, but at runtime it is not immediately executed and evaluates to a future. To execute the block and obtain the result, it must be `await`ed." An async block is "the simplest way to start an async context and create a future." A function returning an async block is roughly equivalent to an async function: "`async fn foo() -> Foo` becomes `fn foo() -> impl Future<Output = Foo>`." (Ch. 3, "Async blocks")

The sections on async closures, lifetimes/borrowing, `Send + 'static` bounds, async traits, and recursion are outlined but not yet fully written. Their bullet points indicate important topics: async closures are a new language feature; borrowing across await points and `Future + '_` bounds present lifetime challenges; `Send + 'static` bounds are required by multi-threaded runtimes and can be avoided with `spawn_local`; async traits now have native syntax but have issues around `Send + 'static` and object safety; and async recursion requires explicit boxing.

# Prerequisites

- **async-await-basics** -- understanding basic async/await syntax and the concept of futures is necessary before tackling these intermediate topics

# Key Properties

1. Async unit tests require runtime-provided test attributes (e.g., `#[tokio::test]`) because standard Rust tests are not async
2. Blocking an OS thread in an async context starves all tasks on that thread, not just the blocking task
3. Blocking computation (CPU-intensive work without yielding) has a similar effect to blocking IO
4. Cancellation occurs at await points: "the code might stop executing at any `await` and never start again"
5. Cancellation can happen by dropping a future, aborting a task, via a cancellation token, or implicitly via `select`
6. Cancellation safety requires code to work correctly whether it completes normally or terminates at any await point
7. Async blocks evaluate to futures rather than executing immediately; they are the simplest way to create a future
8. Async blocks have function-like control flow: `break`/`continue` cannot cross async block boundaries; `return` exits the block, not the surrounding function
9. The `?` operator inside an async block exits only the block, requiring a second `?` after `.await` to propagate to the enclosing function
10. `async fn foo() -> T` is roughly equivalent to `fn foo() -> impl Future<Output = T> { async { ... } }`

# Construction / Recognition

## To Unit Test Async Code:
1. Add the runtime's test attribute (e.g., `#[tokio::test]`) to the test function
2. Declare the test function as `async fn`
3. Use `.await` freely within the test body

## To Identify Blocking in Async Code:
1. Look for standard library IO operations (e.g., `std::fs`, `std::net`) used inside async tasks
2. Look for long-running computations without any `.await` points
3. Look for non-async synchronization primitives (e.g., `std::sync::Mutex`)
4. If none of these appear between await points, the code is not blocking

## To Use Async Blocks:
1. Write `async { ... }` to create a future from a block of code
2. Use `.await` on the result to execute it
3. Remember that `return` inside the block returns from the block (like a function), not from the enclosing function
4. Use `Ok::<_, MyError>(())` turbofishing to help the compiler infer the block's return type when using `?`

# Context & Application

These topics form the practical knowledge needed to write non-trivial async Rust programs. The blocking rules are particularly important: "It is very important to only use non-blocking I/O from an async task, never blocking I/O (which is the only kind provided in Rust's standard library)."

Cancellation is ubiquitous in async Rust programs, primarily through `select` macros and future dropping. The source warns that cancellation can cause data loss: "if an async function reads data into an internal buffer, then awaits the next datum. If reading the data is destructive and the async function is canceled, then the internal buffer will be dropped, and the data in it will be lost."

Async blocks are commonly used to create small one-off futures and to wrap code that needs to run in an async context. The equivalence between async functions and functions returning async blocks is important for API design, as "from the caller's perspective they are equivalent, and changing from one form to the other is not a breaking change."

The source also folds in content from Ch. 9 (Futures) and Ch. 10 (Runtimes). Ch. 9 notes the importance of the `Future` trait (with `Output` associated type), `IntoFuture` for the async builder pattern, and boxing futures (which "used to be common and necessary but mostly isn't now, except for recursion"). Ch. 10 covers runtime startup patterns (explicit startup vs async main, `block_on`), the distinction between threads and tasks (work-stealing multi-threaded by default, `spawn_local` and `spawn_blocking`), and configuration options (thread pool size, single-threaded modes).

# Examples

**Example 1 -- Unit test** (Ch. 3, "Unit tests"):
```rust
#[tokio::test]
async fn test_something() {
    // Write a test here, including all the `await`s you like.
}
```

**Example 2 -- Async block vs regular block** (Ch. 3, "Async blocks"):
```rust
let s1 = {
    let a = 42;
    format!("The answer is {a}")
};

let s2 = async {
    let q = question().await;
    format!("The question is {q}")
};
```
`s1` is a string; `s2` is a future. `question()` has not been called until `s2.await` is executed.

**Example 3 -- Error handling in async blocks** (Ch. 3, "Async blocks"):
```rust
async {
    let x = foo()?;   // This `?` only exits the async block.
    consume(x);
    Ok(())
}.await?             // Second `?` propagates to the surrounding function.
```

**Example 4 -- Cancellation points** (Ch. 3, "Cancellation"):
```rust
async fn some_function(input: Option<Input>) {
    let Some(input) = input else { return; };
    let x = foo(input)?;
    let y = bar(x).await;  // Might be cancelled here.
    // ...
}
```
The function might terminate at any `return`, `?`, `.await`, or implicit return, but cancellation specifically can only occur at `.await` points.

# Relationships

## Builds Upon
- **async-await-basics** -- these topics extend the basic async/await model with practical considerations

## Enables
- **async-concurrency-composition** -- understanding blocking and cancellation is essential for using join/select correctly
- **async-cancellation-cleanup** -- cancellation introduced here is explored in depth in destruction/cleanup

## Related
- **async-programming-overview** -- broader context for why async exists
- **cancellation-safety** -- the formal property that code works correctly when cancelled at any await point

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using standard library blocking IO (e.g., `std::fs::read`) inside async tasks.
  **Correction**: Use the runtime's async IO equivalents (e.g., `tokio::fs::read`). If blocking IO is unavoidable, use `spawn_blocking` to run it on a dedicated thread pool.

- **Error**: Assuming code after an `.await` will always execute.
  **Correction**: Any `.await` is a potential cancellation point. Design code to be correct whether it completes normally or is cancelled at any await. Avoid holding destructive intermediate state across await points.

- **Error**: Using `break` or `continue` inside an async block to control an outer loop.
  **Correction**: Use `return` to exit the async block, or use `ControlFlow` as the block's return value to signal the loop.

# Common Confusions

- **Confusion**: Thinking `?` inside an async block propagates to the enclosing function.
  **Clarification**: `?` inside an async block only exits the block. You need a second `?` after `.await` to propagate to the enclosing function: `async { foo()? }.await?`.

- **Confusion**: Thinking cancellation only happens when explicitly requested.
  **Clarification**: Cancellation can happen implicitly. The `select` macro cancels all non-winning branches automatically. Any code that drops a future cancels it. "From the perspective of writing async code, the code might stop executing at any `await` and never start again."

- **Confusion**: Thinking an async block executes when defined.
  **Clarification**: An async block creates a future that is not executed until awaited. In the example, `let s2 = async { question().await; };` does not call `question()` until `s2.await`.

# Source Reference

Chapter 3: "More async/await topics" -- all sections. The unit tests, blocking/cancellation, and async blocks sections are fully written. The sections on async closures, lifetimes, `Send + 'static`, async traits, and recursion are outlines/stubs with bullet points indicating planned content. Supplementary content drawn from Ch. 9 ("Futures" -- outlined topics on Future/IntoFuture traits, polling, futures-rs, futures-concurrency) and Ch. 10 ("Runtimes" -- outlined topics on running async code, threads vs tasks, configuration, alternate runtimes).

# Verification Notes

- Definition source: Direct quotations from Ch. 3 sections on unit tests, blocking, cancellation, and async blocks
- Key Properties: Items 1-10 derived from explicit source statements in fully-written sections
- Confidence rationale: MEDIUM -- the unit tests, blocking, cancellation, and async blocks sections are fully written and well-sourced (high confidence individually), but approximately half the chapter (async closures, lifetimes, Send+'static, async traits, recursion) consists of bullet-point outlines only. Ch. 9 and Ch. 10 are also outlines. Overall confidence is medium because the card covers both well-developed and stub content.
- Uncertainties: The outline-only sections may be substantially expanded; the bullet points indicate topics but not final treatment. Ch. 9 and Ch. 10 are entirely outlines.
- Cross-reference status: `async-await-basics` and `async-programming-overview` are from Agent A's Ch. 1-2 extraction; `cancellation-safety` exists in async-reference; other slugs are in this extraction set
