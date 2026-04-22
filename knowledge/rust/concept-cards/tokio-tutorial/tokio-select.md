---
concept: Tokio Select
slug: tokio-select
category: async-runtime
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Select"
chapter_number: 9
pdf_page: null
section: "tokio::select! / Cancellation / Syntax / Loops"
extraction_confidence: high
aliases:
  - "select! macro"
  - "tokio::select!"
  - "async multiplexing"
  - "branch selection"
prerequisites:
  - future-trait-in-depth
  - tokio-spawn
  - tokio-channels
extends: []
related:
  - tokio-executor
  - tokio-streams
  - tokio-async-io
contrasts_with:
  - tokio-spawn
answers_questions:
  - "How do I wait on multiple async operations simultaneously?"
  - "How does select! handle cancellation?"
  - "What is the difference between select! and tokio::spawn for concurrency?"
  - "How do I use select! in a loop?"
  - "How do I resume an async operation across multiple select! iterations?"
  - "What is a select! branch precondition?"
  - "Can select! branches borrow data?"
---

# Quick Definition

The `tokio::select!` macro waits on multiple async computations concurrently and returns when a **single** computation completes. All other branches are dropped (cancelled). Unlike `tokio::spawn`, all branches run on the **same task** and never execute simultaneously -- `select!` multiplexes async operations within a single task.

# Core Definition

"The `tokio::select!` macro allows waiting on multiple async computations and returns when a **single** computation completes." (Tokio Tutorial, Ch. 9, "tokio::select!")

"With asynchronous Rust, cancellation is performed by dropping a future. Recall from 'Async in depth', async Rust operations are implemented using futures and futures are lazy. The operation only proceeds when the future is polled. If the future is dropped, the operation cannot proceed because all associated state has been dropped." (Tokio Tutorial, Ch. 9, "Cancellation")

Branch syntax:
```text
<pattern> = <async expression> => <handler>,
```

"When the `select` macro is evaluated, all the `<async expression>`s are aggregated and executed concurrently. When an expression completes, the result is matched against `<pattern>`. If the result matches the pattern, then all remaining async expressions are dropped and `<handler>` is executed." (Tokio Tutorial, Ch. 9, "Syntax")

# Prerequisites

- **future-trait-in-depth** -- `select!` is implemented as a future that polls multiple inner futures; understanding poll semantics explains cancellation
- **tokio-spawn** -- `select!` is an alternative to `spawn` for concurrency; understanding both clarifies when to use each
- **tokio-channels** -- many `select!` patterns involve receiving from channels

# Key Properties

1. Waits on up to 64 branches concurrently
2. Returns when the **first** branch completes and matches its pattern
3. All remaining branches are dropped (cancelled) when one completes
4. Cancellation works by dropping the future -- no explicit cancellation token needed
5. The macro randomly selects which branch to poll first, preventing starvation
6. All branches run on the **same task** -- they never run simultaneously
7. Branch async expressions may **borrow** data (unlike `tokio::spawn` which requires `'static`)
8. Multiple branches may immutably borrow the same data concurrently
9. Only one handler runs, so handlers may mutably borrow the same data
10. The return type of all handlers must be the same
11. If a pattern does not match, the branch is disabled and remaining branches continue
12. An `else` branch handles the case where no patterns match
13. Branch preconditions (`, if <condition>`) disable branches before polling

# Construction / Recognition

## Basic Usage

```rust
use tokio::sync::oneshot;

#[tokio::main]
async fn main() {
    let (tx1, rx1) = oneshot::channel();
    let (tx2, rx2) = oneshot::channel();

    tokio::spawn(async { let _ = tx1.send("one"); });
    tokio::spawn(async { let _ = tx2.send("two"); });

    tokio::select! {
        val = rx1 => {
            println!("rx1 completed first with {:?}", val);
        }
        val = rx2 => {
            println!("rx2 completed first with {:?}", val);
        }
    }
}
```

## Future Implementation (Simplified)

The source shows `select!` is conceptually a single future that polls branches in sequence:

```rust
struct MySelect {
    rx1: oneshot::Receiver<&'static str>,
    rx2: oneshot::Receiver<&'static str>,
}

impl Future for MySelect {
    type Output = ();

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<()> {
        if let Poll::Ready(val) = Pin::new(&mut self.rx1).poll(cx) {
            println!("rx1 completed first with {:?}", val);
            return Poll::Ready(());
        }

        if let Poll::Ready(val) = Pin::new(&mut self.rx2).poll(cx) {
            println!("rx2 completed first with {:?}", val);
            return Poll::Ready(());
        }

        Poll::Pending
    }
}
```

"After `.await` receives the output from a future, the future is dropped. This results in the futures for both branches to be dropped. As one branch did not complete, the operation is effectively cancelled." (Tokio Tutorial, Ch. 9, "The Future implementation")

## Cooperative Cancellation

```rust
tokio::spawn(async {
    tokio::select! {
        val = some_operation() => {
            let _ = tx1.send(val);
        }
        _ = tx1.closed() => {
            // `some_operation()` is canceled, the
            // task completes and `tx1` is dropped.
        }
    }
});
```

# Context & Application

`select!` is Tokio's primary tool for **per-task concurrency** -- multiplexing multiple async operations within a single task. The distinction from `tokio::spawn` is fundamental:

"The `tokio::spawn` function takes an asynchronous operation and spawns a new task to run it. A task is the object that the Tokio runtime schedules. Two different tasks are scheduled independently by Tokio. They may run simultaneously on different operating system threads. Because of this, a spawned task has the same restriction as a spawned thread: no borrowing." (Tokio Tutorial, Ch. 9, "Per-task concurrency")

"The `select!` macro runs all branches concurrently **on the same task**. Because all branches of the `select!` macro are executed on the same task, they will never run **simultaneously**. The `select!` macro multiplexes asynchronous operations on a single task." (Tokio Tutorial, Ch. 9, "Per-task concurrency")

Key design patterns:

**select! in a loop with multiple channels** -- drain messages from several channels, using the `else` branch to break when all are closed:
```rust
loop {
    let msg = tokio::select! {
        Some(msg) = rx1.recv() => msg,
        Some(msg) = rx2.recv() => msg,
        Some(msg) = rx3.recv() => msg,
        else => { break }
    };
    println!("Got {:?}", msg);
}
```

The random branch selection prevents starvation: "If `select!` **did not** randomly pick a branch to check first, on each iteration of the loop, `rx1` would be checked first. If `rx1` always contained a new message, the remaining channels would never be checked."

**Resuming an operation across iterations** -- pin the future outside the loop and pass `&mut` references:
```rust
let operation = action();
tokio::pin!(operation);

loop {
    tokio::select! {
        _ = &mut operation => break,
        Some(v) = rx.recv() => {
            if v % 2 == 0 { break; }
        }
    }
}
```

**Branch preconditions** -- disable branches dynamically:
```rust
tokio::select! {
    res = &mut operation, if !done => {
        done = true;
        // handle result
    }
    Some(v) = rx.recv() => {
        if v % 2 == 0 {
            operation.set(action(Some(v)));
            done = false;
        }
    }
}
```

# Examples

**Example 1** (Ch. 9, "Pattern matching"): Using `Some(v)` patterns with an `else` branch:
```rust
tokio::select! {
    Some(v) = rx1.recv() => {
        println!("Got {:?} from rx1", v);
    }
    Some(v) = rx2.recv() => {
        println!("Got {:?} from rx2", v);
    }
    else => {
        println!("Both channels closed");
    }
}
```
When `recv()` returns `None` (channel closed), the `Some(v)` pattern does not match, disabling that branch. When all branches are disabled, the `else` branch executes.

**Example 2** (Ch. 9, "Errors"): The `?` operator behaves differently in async expressions vs handlers:
```rust
tokio::select! {
    res = async {
        loop {
            let (socket, _) = listener.accept().await?;
            tokio::spawn(async move { process(socket) });
        }
        Ok::<_, io::Error>(())
    } => {
        res?;  // propagates error out of select!
    }
    _ = rx => {
        println!("terminating accept loop");
    }
}
```
Using `?` in the async expression propagates to the `res` binding. Using `?` in the handler propagates out of the `select!` expression.

# Relationships

## Builds Upon
- **future-trait-in-depth** -- `select!` is implemented as a composite future that polls branches
- **tokio-channels** -- channels are the most common resource used in `select!` branches

## Enables
- Graceful shutdown patterns (select on work + shutdown signal)
- Timeout patterns (select on operation + `tokio::time::sleep`)
- Request racing (select on multiple sources, use first to respond)

## Related
- **tokio-executor** -- `select!` runs within the executor's polling model
- **tokio-streams** -- streams can be used in `select!` branches via `StreamExt::next()`
- **tokio-async-io** -- I/O operations are common `select!` branch expressions

## Contrasts With
- **tokio-spawn** -- `spawn` creates independent tasks on potentially different OS threads; `select!` multiplexes within one task. `spawn` requires `'static + Send`; `select!` allows borrowing.

# Common Errors

- **Error**: Polling a completed future by using `&mut operation` in a loop without a precondition.
  **Correction**: Use a `done` flag with a branch precondition: `res = &mut operation, if !done => { done = true; ... }`. Reset `done` and use `operation.set(...)` when restarting.

- **Error**: Forgetting `tokio::pin!` when using `&mut operation` in `select!`.
  **Correction**: To `.await` a reference, the value must be pinned or implement `Unpin`. Call `tokio::pin!(operation)` before the loop. The error message mentions "no method named `poll` found."

- **Error**: Expecting `select!` branches to run simultaneously (like separate threads).
  **Correction**: "All branches of the `select!` macro are executed on the same task, they will never run **simultaneously**." For true parallelism, use `tokio::spawn`.

# Common Confusions

- **Confusion**: Thinking cancelled branches lose data from channels.
  **Clarification**: "Only one channel has a value popped. All other channels remain untouched, and their messages stay in those channels until the next loop iteration. No messages are lost." Only the winning branch's value is consumed.

- **Confusion**: Thinking `select!` always picks the first ready branch.
  **Clarification**: "The `select!` macro randomly picks branches to check first for readiness." This prevents starvation when multiple branches are always ready.

- **Confusion**: Thinking branch async expressions are re-evaluated each loop iteration.
  **Clarification**: When resuming an operation across loop iterations, define the future *outside* the loop and pass `&mut` references. If defined inside `select!`, it restarts from scratch each iteration.

# Source Reference

Chapter 9: "Select," all sections. Lines 1-741 of `09-select.md`.

# Verification Notes

- Definition source: Direct quotations from "tokio::select!", "Cancellation", "Syntax", and "Per-task concurrency" sections
- Key Properties: Derived from explicit statements about branch limits, randomization, borrowing rules, and pattern matching
- Confidence rationale: HIGH -- the source provides thorough coverage with examples for every feature, including the underlying Future implementation
- Uncertainties: None for the core semantics
- Cross-reference status: All slugs reference cards from this extraction set or from Agents A/B
