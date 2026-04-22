---
concept: Future Trait In Depth
slug: future-trait-in-depth
category: async-internals
subcategory: null
tier: advanced
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Async in Depth"
chapter_number: 8
pdf_page: null
section: "Futures / Implementing Future / Async fn as a Future"
extraction_confidence: high
aliases:
  - "Future poll model"
  - "std::future::Future"
  - "manual Future implementation"
  - "async state machine"
prerequisites:
  - tokio-overview
  - tokio-spawn
extends: []
related:
  - tokio-executor
  - tokio-select
  - tokio-streams
contrasts_with: []
answers_questions:
  - "What is the Future trait in Rust?"
  - "How does polling work in async Rust?"
  - "What does Pin<&mut Self> mean in the Future trait?"
  - "How do I implement Future manually?"
  - "What state machine does the compiler generate for async fn?"
  - "Why are Rust futures lazy?"
  - "What is the difference between Rust futures and futures in other languages?"
---

# Quick Definition

The `std::future::Future` trait is the foundation of async Rust. A future is a value representing an in-progress computation that is advanced by polling. Unlike futures in other languages, a Rust future **is** the computation itself -- not a handle to a background computation. The owner drives it forward by calling `Future::poll`, which returns either `Poll::Ready(output)` or `Poll::Pending`.

# Core Definition

"The value returned by `my_async_fn()` is a future. A future is a value that implements the `std::future::Future` trait provided by the standard library. They are values that contain the in-progress asynchronous computation." (Tokio Tutorial, Ch. 8, "Futures")

The trait definition:

```rust
use std::pin::Pin;
use std::task::{Context, Poll};

pub trait Future {
    type Output;

    fn poll(self: Pin<&mut Self>, cx: &mut Context)
        -> Poll<Self::Output>;
}
```

"Unlike how futures are implemented in other languages, a Rust future does not represent a computation happening in the background, rather the Rust future **is** the computation itself. The owner of the future is responsible for advancing the computation by polling the future." (Tokio Tutorial, Ch. 8, "Futures")

# Prerequisites

- **tokio-overview** -- understanding the Tokio runtime and async/await syntax is needed before diving into the underlying trait mechanics
- **tokio-spawn** -- knowing how tasks are spawned provides context for why futures need executors to drive them

# Key Properties

1. The `Output` associated type is the type the future produces once it completes
2. `poll` takes `self: Pin<&mut Self>` -- `Pin` enables Rust to support borrows across `.await` points in async functions
3. `poll` takes `cx: &mut Context` -- the `Context` carries a `Waker` used to signal readiness
4. `poll` returns `Poll::Ready(value)` when the computation is complete
5. `poll` returns `Poll::Pending` when the computation cannot yet complete (waiting on a resource)
6. Rust futures are lazy -- calling an async function returns a future but does nothing until it is polled
7. Futures compose: polling an outer future results in polling inner futures
8. When a future returns `Poll::Pending`, it **must** ensure the waker is signalled at some point -- forgetting this causes the task to hang indefinitely
9. Each call to `poll` **could** supply a different `Waker` instance -- implementations must update any previously recorded waker with the new one

# Construction / Recognition

## Implementing Future Manually

A simple `Delay` future that waits until a specific instant:

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::{Duration, Instant};

struct Delay {
    when: Instant,
}

impl Future for Delay {
    type Output = &'static str;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>)
        -> Poll<&'static str>
    {
        if Instant::now() >= self.when {
            println!("Hello world");
            Poll::Ready("done")
        } else {
            // Ensure waker is signalled (required contract)
            cx.waker().wake_by_ref();
            Poll::Pending
        }
    }
}
```

## Async fn as a State Machine

The compiler transforms an `async fn` into an enum-based state machine that implements `Future`. For example, this async main:

```rust
async fn main() {
    let when = Instant::now() + Duration::from_millis(10);
    let future = Delay { when };
    let out = future.await;
    assert_eq!(out, "done");
}
```

Generates roughly:

```rust
enum MainFuture {
    State0,            // Initialized, never polled
    State1(Delay),     // Waiting on `Delay`
    Terminated,        // Future has completed
}

impl Future for MainFuture {
    type Output = ();

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>)
        -> Poll<()>
    {
        use MainFuture::*;
        loop {
            match *self {
                State0 => {
                    let when = Instant::now() +
                        Duration::from_millis(10);
                    let future = Delay { when };
                    *self = State1(future);
                }
                State1(ref mut my_future) => {
                    match Pin::new(my_future).poll(cx) {
                        Poll::Ready(out) => {
                            assert_eq!(out, "done");
                            *self = Terminated;
                            return Poll::Ready(());
                        }
                        Poll::Pending => {
                            return Poll::Pending;
                        }
                    }
                }
                Terminated => {
                    panic!("future polled after completion")
                }
            }
        }
    }
}
```

"Rust futures are **state machines**. Here, `MainFuture` is represented as an `enum` of the future's possible states." (Tokio Tutorial, Ch. 8, "Async fn as a Future")

# Context & Application

The Future trait is THE core abstraction of async Rust. Every `async fn`, every `.await`, every `tokio::spawn` call ultimately works through this trait. Understanding poll semantics is essential for:

- Implementing custom futures (timers, combinators, protocol state machines)
- Debugging async code that hangs (usually a missing waker signal)
- Understanding why async Rust has zero-cost abstractions (state machines, not heap-allocated callbacks)
- Working with `Pin` and `Unpin` (required for self-referential futures)

The waker contract is critical: "When a future returns `Poll::Pending`, it **must** ensure that the waker is signalled at some point. Forgetting to do this results in the task hanging indefinitely." This is described as "a common source of bugs."

A future can migrate across tasks between polls, so each `poll` call could supply a different `Waker`. Implementations that cache the waker must check with `will_wake()` and update if changed.

# Examples

**Example 1** (Ch. 8, "Futures"): Calling an async function returns a future without executing anything:
```rust
let what_is_this = my_async_fn();
// Nothing has been printed yet.
what_is_this.await;
// Text has been printed and socket has been
// established and closed.
```

**Example 2** (Ch. 8, "A few loose ends"): A robust `Delay` implementation that correctly handles waker updates when the future migrates between tasks:
```rust
struct Delay {
    when: Instant,
    waker: Option<Arc<Mutex<Waker>>>,
}

impl Future for Delay {
    type Output = ();

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<()> {
        if Instant::now() >= self.when {
            return Poll::Ready(());
        }

        if let Some(waker) = &self.waker {
            let mut waker = waker.lock().unwrap();
            if !waker.will_wake(cx.waker()) {
                *waker = cx.waker().clone();
            }
        } else {
            let when = self.when;
            let waker = Arc::new(Mutex::new(cx.waker().clone()));
            self.waker = Some(waker.clone());
            thread::spawn(move || {
                let now = Instant::now();
                if now < when {
                    thread::sleep(when - now);
                }
                let waker = waker.lock().unwrap();
                waker.wake_by_ref();
            });
        }

        Poll::Pending
    }
}
```

# Relationships

## Builds Upon
- **tokio-overview** -- the Future trait underlies the async/await syntax introduced there
- **tokio-spawn** -- spawned tasks are futures submitted to the executor

## Enables
- **tokio-executor** -- executors exist to call `Future::poll` on the outermost future
- **tokio-streams** -- the `Stream` trait is modeled directly on `Future` with `poll_next`
- **tokio-select** -- `select!` is implemented by polling multiple futures

## Related
- **tokio-async-io** -- async I/O resources implement the poll/waker pattern for readiness
- **tokio-channels** -- channels are often used inside futures as waker-driven notification mechanisms

## Contrasts With
- None explicitly -- the contrast is with callback-based or background-thread models in other languages

# Common Errors

- **Error**: Returning `Poll::Pending` without ensuring the waker will be signalled.
  **Correction**: "When a future returns `Poll::Pending`, it **must** ensure that the waker is signalled at some point." Always arrange for `waker.wake()` to be called when the resource becomes ready. This is the single most common source of async bugs.

- **Error**: Not updating the stored waker when a future migrates between tasks.
  **Correction**: "Each call to `poll` **could** supply a different `Waker` instance. The poll function must update any previously recorded waker with the new one." Use `will_wake()` to check and update if needed.

- **Error**: Polling a future after it has returned `Poll::Ready`.
  **Correction**: Once a future completes, it must not be polled again. The generated state machine panics with "future polled after completion" if this happens.

# Common Confusions

- **Confusion**: Thinking calling an async function starts executing the computation.
  **Clarification**: "Asynchronous Rust operations are lazy and require a caller to poll them." Calling `my_async_fn()` returns a future value; nothing executes until `.await` or an executor polls it.

- **Confusion**: Thinking a Rust future represents work happening in the background (like JavaScript Promises).
  **Clarification**: "A Rust future does not represent a computation happening in the background, rather the Rust future **is** the computation itself." No work happens unless something polls the future.

- **Confusion**: Thinking `cx.waker().wake_by_ref()` is a harmless no-op.
  **Clarification**: Calling `wake_by_ref()` immediately before returning `Poll::Pending` (without arranging a real readiness signal) results in a busy loop. It satisfies the contract but wastes CPU cycles because the executor will immediately re-poll.

# Source Reference

Chapter 8: "Async in Depth," sections "Futures," "Implementing Future," "Async fn as a Future," and "A few loose ends." Lines 1-847 of `08-async-in-depth.md`.

# Verification Notes

- Definition source: Direct quotations from the "Futures" section
- Key Properties: Derived from the trait definition, explicit statements about laziness, waker contract, and waker update requirements
- Confidence rationale: HIGH -- the source provides the complete trait definition, multiple implementations, and explicit rules about the poll/waker contract
- Uncertainties: None for the core definitions; the source is authoritative
- Cross-reference status: All slugs reference cards from this extraction set or from Agents A/B
