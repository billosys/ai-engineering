---
concept: Tokio Runtime and Async Entry Point
slug: tokio-runtime
category: async-runtime
subcategory: null
tier: foundational
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "02-hello-tokio"
chapter_number: 2
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "#[tokio::main]"
  - "tokio::main macro"
  - "Tokio runtime"
  - "async main"
  - "tokio::runtime::Runtime"
prerequisites:
  - tokio-overview
extends: []
related:
  - tokio-spawn
  - future-trait-in-depth
  - tokio-executor
contrasts_with: []
answers_questions:
  - "How do I start a Tokio application?"
  - "What does #[tokio::main] do?"
  - "What is the Tokio runtime?"
  - "How does async/await work in Rust?"
  - "Why are Rust's async operations lazy?"
  - "What is compile-time green threading?"
---

# Quick Definition

The Tokio runtime is the executor that drives async code to completion. It is bootstrapped by the `#[tokio::main]` macro, which transforms an `async fn main()` into a synchronous `fn main()` that creates a runtime and blocks on the async entry point. Async functions in Rust are lazy -- calling them returns a `Future` that does nothing until `.await`ed.

# Core Definition

"The main function used to launch the application differs from the usual one found in most of Rust's crates. (1) It is an `async fn`. (2) It is annotated with `#[tokio::main]`." The macro is then explained: "The `#[tokio::main]` function is a macro. It transforms the `async fn main()` into a synchronous `fn main()` that initializes a runtime instance and executes the async main function." (Ch. 2, "Async `main` function")

The runtime's role is made explicit: "An `async fn` is used as we want to enter an asynchronous context. However, asynchronous functions must be executed by a runtime. The runtime contains the asynchronous task scheduler, provides evented I/O, timers, etc. The runtime does not automatically start, so the main function needs to start it." (Ch. 2, "Async `main` function")

On async/await semantics: "Async functions are called like any other Rust function. However, calling these functions does not result in the function body executing. Instead, calling an `async fn` returns a value representing the operation. This is conceptually analogous to a zero-argument closure. To actually run the operation, you should use the `.await` operator on the return value." (Ch. 2, "Using `async/await`")

# Prerequisites

- **tokio-overview** -- understanding what Tokio is and why an async runtime is needed before learning how to start one

# Key Properties

1. `#[tokio::main]` is a proc macro that transforms `async fn main()` into a synchronous entry point that creates and runs a `tokio::runtime::Runtime`
2. The macro expansion creates a `Runtime`, then calls `rt.block_on(async { ... })` to drive the top-level future
3. Async functions are **lazy** in Rust: calling an `async fn` does not execute its body; it returns an anonymous type implementing `Future`
4. The `.await` operator is what drives a future to completion -- without `.await`, the async function's body never runs
5. The return value of `async fn` implements the `Future` trait (specifically, it is an anonymous compiler-generated type)
6. `.await` yields control back to the thread, allowing other work to proceed while the operation completes in the background
7. Rust's async/await is described as "compile-time green threading" -- the compiler transforms async code into state machines at compile time
8. Rust's lazy async semantics differ from other languages (like JavaScript or C#) where async operations begin executing immediately upon being called

# Construction / Recognition

## The `#[tokio::main]` Macro Transformation:

The annotated code:
```rust
#[tokio::main]
async fn main() {
    println!("hello");
}
```

Is transformed by the macro into:
```rust
fn main() {
    let mut rt = tokio::runtime::Runtime::new().unwrap();
    rt.block_on(async {
        println!("hello");
    })
}
```

## Key Patterns:
1. Every Tokio application starts with `#[tokio::main]` on an `async fn main()`
2. Async operations are invoked with `.await` -- this is the only indication that an operation is asynchronous
3. Async code looks synchronous except for the `.await` points
4. Dependencies are declared with feature flags: `tokio = { version = "1", features = ["full"] }`

# Context & Application

The Tokio runtime is the bridge between Rust's async/await language features and actual execution. Rust deliberately separates the async language primitives from runtime implementation -- `async`/`await` produce `Future` values, but something must poll those futures to drive them forward. The Tokio runtime provides:

- An asynchronous task scheduler (single-threaded or multi-threaded work-stealing)
- Evented I/O (backed by epoll/kqueue/IOCP)
- Timers
- Synchronization primitives

The laziness of Rust's futures is a critical distinction from other async ecosystems. In JavaScript, `fetch()` starts the HTTP request immediately. In Rust, calling an `async fn` produces a future that does absolutely nothing until polled. This has important implications: futures can be composed, stored, and conditionally executed without triggering side effects.

The tutorial demonstrates these concepts through a Mini-Redis client that connects to a server, sets a key-value pair, and reads it back -- all using `.await` to drive each async operation.

# Examples

**Example 1** (Ch. 2, Lazy futures -- execution ordering):
```rust
async fn say_world() {
    println!("world");
}

#[tokio::main]
async fn main() {
    let op = say_world();    // Does NOT execute say_world's body
    println!("hello");        // Prints first
    op.await;                 // NOW say_world executes, prints "world"
}
```
Output: `hello` then `world`. This demonstrates that calling `say_world()` returns a future without executing it. Only `.await` triggers execution.

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
Each `.await` suspends the current task while the I/O operation completes. The code reads sequentially but executes asynchronously.

**Example 3** (Ch. 2, Compile-time green threading): "Rust transforms the `async fn` at compile time into a routine that operates asynchronously. Any calls to `.await` within the `async fn` yield control back to the thread. The thread may do other work while the operation processes in the background."

# Relationships

## Builds Upon
- **tokio-overview** -- understanding Tokio's role and when to use it

## Enables
- **tokio-spawn** -- once a runtime exists, tasks can be spawned onto it for concurrent execution
- **tokio-async-io** -- the runtime's evented I/O subsystem powers async network and file operations
- **tokio-select** -- the `select!` macro operates within the runtime context

## Related
- **future-trait-in-depth** -- the `Future` trait that async functions return is the foundation of the entire system
- **tokio-executor** -- deeper exploration of how the runtime schedules and polls tasks

## Contrasts With
- Synchronous `fn main()` -- does not require a runtime; blocking calls proceed sequentially on the OS thread
- Other async runtimes (async-std, smol) -- provide the same role but with different implementations and trade-offs

# Common Errors

- **Error**: Calling an async function without `.await` and expecting it to execute.
  **Correction**: Async functions in Rust are lazy. The call returns a `Future` that does nothing until `.await`ed. The compiler will emit a warning: "unused implementer of `Future` that must be used."

- **Error**: Trying to use `.await` outside an async context (e.g., in a regular `fn`).
  **Correction**: `.await` can only be used inside `async fn` or `async` blocks. The outermost entry point must use `#[tokio::main]` (or manually create a runtime) to bridge from synchronous to asynchronous code.

- **Error**: Using blocking standard library APIs (e.g., `std::thread::sleep`, `std::net::TcpStream`) inside async functions.
  **Correction**: Blocking calls occupy the runtime thread and prevent other tasks from progressing. Use Tokio's async equivalents (`tokio::time::sleep`, `tokio::net::TcpStream`) or offload blocking work with `tokio::task::spawn_blocking`.

# Common Confusions

- **Confusion**: Thinking `#[tokio::main]` does something magical beyond creating a runtime.
  **Clarification**: The macro simply creates a `tokio::runtime::Runtime`, calls `block_on` with the async main body, and returns. It is syntactic sugar for a well-defined transformation.

- **Confusion**: Expecting Rust's async functions to begin executing immediately (as in JavaScript or C#).
  **Clarification**: "Although other languages implement async/await too, Rust takes a unique approach. Primarily, Rust's async operations are lazy." Calling an `async fn` produces a future; only `.await` (or explicit polling) drives execution.

- **Confusion**: Thinking `.await` blocks the thread.
  **Clarification**: `.await` suspends the current task (not the thread) and yields control back to the runtime scheduler. The thread is free to execute other tasks while the awaited operation completes.

# Source Reference

Chapter 2: Hello Tokio, all sections -- "Breaking it down," "What is asynchronous programming?," "Compile-time green-threading," "Using `async/await`," "Async `main` function," and "Cargo features."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, sections "Async `main` function" and "Using `async/await`"
- Macro transformation: Exact code example from Ch. 2 showing the before/after expansion
- Lazy semantics: Explicitly stated in Ch. 2 with the `say_world` example demonstrating execution order
- Confidence rationale: HIGH -- the source provides explicit definitions, code examples, and the exact macro transformation
- Uncertainties: None
- Cross-reference status: Agent B slugs (tokio-async-io) and Agent C slugs (future-trait-in-depth, tokio-executor, tokio-select) referenced per assignment
