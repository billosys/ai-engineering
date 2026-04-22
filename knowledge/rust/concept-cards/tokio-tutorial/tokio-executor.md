---
concept: Tokio Executor
slug: tokio-executor
category: async-internals
subcategory: null
tier: advanced
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Async in Depth"
chapter_number: 8
pdf_page: null
section: "Executors / Mini Tokio / Wakers / Updating Mini Tokio"
extraction_confidence: high
aliases:
  - "async executor"
  - "mini-tokio"
  - "task scheduler"
  - "waker system"
prerequisites:
  - future-trait-in-depth
  - tokio-runtime
extends:
  - future-trait-in-depth
related:
  - tokio-spawn
  - tokio-select
  - tokio-streams
contrasts_with: []
answers_questions:
  - "What calls poll on the outermost future?"
  - "How does a Tokio executor work?"
  - "What is a waker and how does it schedule tasks?"
  - "How does a task get re-polled when a resource becomes ready?"
  - "How do you build a minimal async executor?"
  - "What is the ArcWake trait?"
  - "What is tokio::sync::Notify?"
---

# Quick Definition

An executor is the component responsible for calling `Future::poll` on spawned tasks, driving asynchronous computations to completion. The executor uses a waker-based notification system: when a resource is not ready, it registers a `Waker`; when the resource becomes ready, it calls `wake()` to schedule the task for re-polling. This avoids busy-looping and enables efficient task scheduling.

# Core Definition

"Asynchronous Rust functions return futures. Futures must have `poll` called on them to advance their state. Futures are composed of other futures. So, the question is, what calls `poll` on the very most outer future?" (Tokio Tutorial, Ch. 8, "Executors")

"Recall from earlier, to run asynchronous functions, they must either be passed to `tokio::spawn` or be the main function annotated with `#[tokio::main]`. This results in submitting the generated outer future to the Tokio executor. The executor is responsible for calling `Future::poll` on the outer future, driving the asynchronous computation to completion." (Tokio Tutorial, Ch. 8, "Executors")

"Wakers are the missing piece. This is the system by which a resource is able to notify the waiting task that the resource has become ready to continue some operation." (Tokio Tutorial, Ch. 8, "Wakers")

# Prerequisites

- **future-trait-in-depth** -- the executor exists to drive futures; understanding poll, Pin, and the waker contract is essential
- **tokio-runtime** -- the Tokio runtime includes the executor as a core component

# Key Properties

1. The executor calls `Future::poll` on the outermost future, which cascades to inner futures
2. A naive executor that loops over all tasks and polls them is inefficient (busy-looping)
3. The `Context` argument to `poll` carries a `Waker` bound to the current task
4. Calling `waker.wake()` signals the executor to schedule the associated task for execution
5. Resources call `wake()` when they transition to a ready state
6. Wakers must be `Send` and `Sync` -- they can signal from any thread
7. Tasks are stored as `Pin<Box<dyn Future<Output = ()> + Send>>` for type-erasure
8. A channel-based executor receives wake notifications and only polls woken tasks
9. The `ArcWake` trait from the `futures` crate simplifies waker implementation
10. Spurious wake-ups are allowed, but polling a future that already returned `Ready` is not -- the executor must track completion state

# Construction / Recognition

## Mini-Tokio v1 -- Naive (Busy-Loop) Executor

```rust
use std::collections::VecDeque;
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use futures::task;

struct MiniTokio {
    tasks: VecDeque<Task>,
}

type Task = Pin<Box<dyn Future<Output = ()> + Send>>;

impl MiniTokio {
    fn new() -> MiniTokio {
        MiniTokio { tasks: VecDeque::new() }
    }

    fn spawn<F>(&mut self, future: F)
    where F: Future<Output = ()> + Send + 'static,
    {
        self.tasks.push_back(Box::pin(future));
    }

    fn run(&mut self) {
        let waker = task::noop_waker();
        let mut cx = Context::from_waker(&waker);

        while let Some(mut task) = self.tasks.pop_front() {
            if task.as_mut().poll(&mut cx).is_pending() {
                self.tasks.push_back(task);
            }
        }
    }
}
```

"Our implementation so far has a major **flaw**. Our executor never goes to sleep. The executor continuously loops **all** spawned futures and polls them. Most of the time, the futures will not be ready to perform more work and will return `Poll::Pending` again. The process will burn CPU cycles." (Tokio Tutorial, Ch. 8, "Mini Tokio")

## Mini-Tokio v2 -- Waker-Based Executor

The improved design uses a channel to receive wake notifications:

```rust
use std::sync::{mpsc, Arc, Mutex};
use std::task::{Context, Poll};
use futures::task::{self, ArcWake};

struct MiniTokio {
    scheduled: mpsc::Receiver<Arc<Task>>,
    sender: mpsc::Sender<Arc<Task>>,
}

struct TaskFuture {
    future: Pin<Box<dyn Future<Output = ()> + Send>>,
    poll: Poll<()>,
}

struct Task {
    task_future: Mutex<TaskFuture>,
    executor: mpsc::Sender<Arc<Task>>,
}

impl Task {
    fn schedule(self: &Arc<Self>) {
        self.executor.send(self.clone());
    }

    fn poll(self: Arc<Self>) {
        let waker = task::waker(self.clone());
        let mut cx = Context::from_waker(&waker);
        let mut task_future = self.task_future.try_lock().unwrap();
        task_future.poll(&mut cx);
    }
}

impl ArcWake for Task {
    fn wake_by_ref(arc_self: &Arc<Self>) {
        arc_self.schedule();
    }
}

impl MiniTokio {
    fn run(&self) {
        while let Ok(task) = self.scheduled.recv() {
            task.poll();
        }
    }

    fn spawn<F>(&self, future: F)
    where F: Future<Output = ()> + Send + 'static,
    {
        Task::spawn(future, &self.sender);
    }
}
```

The `TaskFuture::poll` method guards against spurious wakes:
```rust
impl TaskFuture {
    fn poll(&mut self, cx: &mut Context<'_>) {
        // Spurious wake-ups are allowed, even after a future has
        // returned `Ready`. However, polling a future which has
        // already returned `Ready` is *not* allowed.
        if self.poll.is_pending() {
            self.poll = self.future.as_mut().poll(cx);
        }
    }
}
```

# Context & Application

The executor-waker model is the fundamental mechanism of async Rust. The chapter builds a complete mini-Tokio from scratch to demonstrate:

1. **Why executors exist**: Futures are inert values; something must call `poll`
2. **Why wakers exist**: Without them, the executor must busy-loop over all tasks
3. **How the system achieves efficiency**: Resources signal readiness via wakers, and the executor only polls tasks that can make progress

The full async Rust execution cycle:
- "Asynchronous Rust operations are lazy and require a caller to poll them."
- "Wakers are passed to futures to link a future to the task calling it."
- "When a resource is **not** ready to complete an operation, `Poll::Pending` is returned and the task's waker is recorded."
- "When the resource becomes ready, the task's waker is notified."
- "The executor receives the notification and schedules the task to execute."
- "The task is polled again, this time the resource is ready and the task makes progress."

For cases where manual waker management is too low-level, Tokio provides `tokio::sync::Notify` -- a utility that handles waker details and allows implementing delays with `async/await`:

```rust
use tokio::sync::Notify;
use std::sync::Arc;
use std::time::{Duration, Instant};
use std::thread;

async fn delay(dur: Duration) {
    let when = Instant::now() + dur;
    let notify = Arc::new(Notify::new());
    let notify_clone = notify.clone();

    thread::spawn(move || {
        let now = Instant::now();
        if now < when {
            thread::sleep(when - now);
        }
        notify_clone.notify_one();
    });

    notify.notified().await;
}
```

# Examples

**Example 1** (Ch. 8, "Updating Delay"): A `Delay` future using wakers properly -- spawns a timer thread that calls `wake()` when the duration elapses:
```rust
impl Future for Delay {
    type Output = &'static str;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>)
        -> Poll<&'static str>
    {
        if Instant::now() >= self.when {
            Poll::Ready("done")
        } else {
            let waker = cx.waker().clone();
            let when = self.when;
            thread::spawn(move || {
                let now = Instant::now();
                if now < when {
                    thread::sleep(when - now);
                }
                waker.wake();
            });
            Poll::Pending
        }
    }
}
```

**Example 2** (Ch. 8, "Updating Mini Tokio"): The `ArcWake` implementation connects the waker system to the channel-based scheduler. When `waker.wake()` is called from the timer thread, it triggers `Task::schedule`, which clones the `Arc<Task>` and sends it through the channel. The executor's `run()` loop receives it and calls `task.poll()`.

# Relationships

## Builds Upon
- **future-trait-in-depth** -- the executor's purpose is to drive futures via `poll`
- **tokio-runtime** -- the real Tokio runtime embeds a production-grade version of this executor

## Enables
- **tokio-spawn** -- `tokio::spawn` submits futures to the executor
- **tokio-select** -- `select!` works within the executor's polling model
- **tokio-streams** -- streams are polled by the same executor machinery

## Related
- **tokio-channels** -- the mini-tokio executor uses `mpsc` channels for task scheduling
- **tokio-shared-state** -- `Mutex<TaskFuture>` is used to make `Task` implement `Sync`

## Contrasts With
- None explicitly -- the source contrasts this waker-based model with the naive busy-loop approach

# Common Errors

- **Error**: Building an executor that busy-loops by polling all tasks continuously.
  **Correction**: Use a waker-based notification system. Only poll tasks when they are signalled as ready via `waker.wake()`. The source builds the naive version first specifically to show this flaw.

- **Error**: Polling a future after it returned `Poll::Ready`.
  **Correction**: "Spurious wake-ups are allowed, even after a future has returned `Ready`. However, polling a future which has already returned `Ready` is *not* allowed." Track the poll state and skip completed futures.

- **Error**: Creating a waker that is not `Send + Sync`.
  **Correction**: Wakers must be `Send` and `Sync` because resources may call `wake()` from any thread (e.g., a timer thread). Use `Arc`-based waker implementations.

# Common Confusions

- **Confusion**: Thinking the executor is part of the standard library.
  **Clarification**: The standard library provides only the `Future` trait, `Context`, `Waker`, and `Poll`. The executor is provided by the runtime (Tokio, async-std, etc.). This is why `async fn` alone does nothing -- you need a runtime.

- **Confusion**: Thinking `ArcWake` is the only way to create wakers.
  **Clarification**: The standard library provides `RawWakerVTable` for manual vtable construction. `ArcWake` from the `futures` crate is a convenience that avoids unsafe boilerplate. Real Tokio uses its own optimized waker implementation.

- **Confusion**: Thinking `Notify` is just for timers.
  **Clarification**: `tokio::sync::Notify` is a general-purpose task notification mechanism that handles waker details. It can replace manual waker management in many scenarios, not just delays.

# Source Reference

Chapter 8: "Async in Depth," sections "Executors," "Mini Tokio," "Wakers," "Updating Delay," "Updating Mini Tokio," "Notify utility," and "Summary." Lines 194-847 of `08-async-in-depth.md`.

# Verification Notes

- Definition source: Direct quotations from "Executors," "Wakers," and "Summary" sections
- Key Properties: Derived from the progressive mini-tokio implementation and explicit statements about waker requirements
- Confidence rationale: HIGH -- the source builds a complete executor from scratch with detailed commentary on every design decision
- Uncertainties: None for the core concepts; the mini-tokio is pedagogical (real Tokio is more complex)
- Cross-reference status: All slugs reference cards from this extraction set or from Agents A/B
