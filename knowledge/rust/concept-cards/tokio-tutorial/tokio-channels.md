---
concept: Tokio Channels
slug: tokio-channels
category: async-runtime
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Channels"
chapter_number: 5
pdf_page: null
section: "Tokio's channel primitives"
extraction_confidence: high
aliases:
  - "message passing in tokio"
  - "tokio mpsc"
  - "tokio oneshot"
  - "channel primitives"
prerequisites:
  - tokio-spawn
  - tokio-shared-state
extends:
  - tokio-shared-state
related:
  - tokio-select
  - tokio-streams
contrasts_with: []
answers_questions:
  - "What channel types does Tokio provide?"
  - "When should I use message passing instead of a mutex?"
  - "How do I send a response back through a channel?"
  - "What is the mpsc + oneshot pattern for request/response?"
  - "How does backpressure work with Tokio channels?"
---

# Quick Definition

Tokio provides four channel primitives for message passing between tasks: `mpsc` (multi-producer, single-consumer, many values), `oneshot` (single-producer, single-consumer, one value), `broadcast` (multi-producer, multi-consumer, every receiver sees every value), and `watch` (multi-producer, multi-consumer, receivers see only the most recent value). The `mpsc` + `oneshot` combination is the primary pattern for request/response communication with a resource-managing task.

# Core Definition

Message passing is the alternative to shared-state concurrency in Tokio. "The pattern involves spawning a dedicated task to manage the `client` resource. Any task that wishes to issue a request sends a message to the `client` task. The `client` task issues the request on behalf of the sender, and the response is sent back to the sender." (Ch. 5, "Message passing")

The four channel types in `tokio::sync`:

- **mpsc**: Multi-producer, single-consumer. Many values can be sent. Created with a capacity for backpressure. Senders are cloneable; receiver is not.
- **oneshot**: Single-producer, single-consumer. A single value can be sent. No capacity needed. Neither handle is cloneable. `send` completes immediately (no `.await`).
- **broadcast**: Multi-producer, multi-consumer. Many values can be sent. Each receiver sees every value.
- **watch**: Multi-producer, multi-consumer. Many values can be sent, but no history is kept. Receivers only see the most recent value.

# Prerequisites

- **tokio-spawn** -- channels are used to communicate between spawned tasks
- **tokio-shared-state** -- understanding the mutex approach helps motivate when message passing is the better alternative

# Key Properties

1. `mpsc::channel(capacity)` creates a bounded channel; when full, `send().await` suspends until space is available
2. Cloning the `mpsc::Sender` creates additional producers; all senders share the same channel to the single receiver
3. When all `Sender` handles are dropped, the channel closes and `recv()` returns `None`
4. `oneshot::channel()` always has capacity of one; neither handle can be cloned
5. `oneshot::Sender::send()` does NOT require `.await` -- it completes immediately, returning `Err` if the receiver was dropped
6. The `mpsc` + `oneshot` pattern: embed a `oneshot::Sender` in each command message so the manager task can send responses back
7. Bounded channels provide backpressure; lazy futures in Rust prevent implicit unbounded queuing
8. For multi-producer multi-consumer where only one consumer sees each message, use the `async-channel` crate (not in `tokio::sync`)
9. `std::sync::mpsc` and `crossbeam::channel` block the thread and must not be used in async code

# Construction / Recognition

## To Set Up mpsc + oneshot Request/Response:
1. Define a `Command` enum with variants for each operation, each containing a `oneshot::Sender` for the response
2. Create the `mpsc::channel` with an appropriate capacity bound
3. Clone the `mpsc::Sender` for each task that needs to send commands
4. Spawn a manager task that owns the resource and loops on `rx.recv().await`
5. In each requesting task: create a `oneshot::channel`, embed the sender in the command, send via `mpsc`, await the `oneshot` receiver

## To Choose the Right Channel Type:
- Need many-to-one command dispatch? Use `mpsc`
- Need a single response back? Use `oneshot`
- Need all receivers to see every message? Use `broadcast`
- Need receivers to see only the latest state? Use `watch`

# Context & Application

The message-passing pattern is preferred over mutexes when the shared resource requires asynchronous work (like I/O). A dedicated manager task owns the resource exclusively, avoiding the need for locks entirely. The channel acts as a buffer, allowing tasks to enqueue requests while the manager is busy, potentially improving throughput.

The `oneshot` channel is specifically optimized for sending a single value. Its `send` method is synchronous (no `.await`), which makes it efficient for response delivery. When the receiver drops their half, `send` returns `Err`, indicating the requester is no longer interested -- this is a form of cancellation.

Backpressure is a central concern. "Whenever concurrency or queuing is introduced, it is important to ensure that the queuing is bounded and the system will gracefully handle the load." Tokio's lazy futures help: an async operation not `.await`-ed does not execute, preventing implicit unbounded queuing that plagues callback-based or eager-future systems.

# Examples

**Example 1** (Ch. 5, "Define the message type"): A command enum with oneshot response channels:
```rust
#[derive(Debug)]
enum Command {
    Get {
        key: String,
        resp: oneshot::Sender<mini_redis::Result<Option<Bytes>>>,
    },
    Set {
        key: String,
        val: Bytes,
        resp: oneshot::Sender<mini_redis::Result<()>>,
    },
}
```

**Example 2** (Ch. 5, "Spawn manager task"): The manager task receives commands and operates on the client:
```rust
let manager = tokio::spawn(async move {
    let mut client = client::connect("127.0.0.1:6379").await.unwrap();
    while let Some(cmd) = rx.recv().await {
        match cmd {
            Command::Get { key, resp } => {
                let res = client.get(&key).await;
                let _ = resp.send(res);
            }
            Command::Set { key, val, resp } => {
                let res = client.set(&key, val).await;
                let _ = resp.send(res);
            }
        }
    }
});
```

**Example 3** (Ch. 5, "Receive responses"): A requesting task creates a oneshot and awaits the response:
```rust
let t1 = tokio::spawn(async move {
    let (resp_tx, resp_rx) = oneshot::channel();
    let cmd = Command::Get {
        key: "foo".to_string(),
        resp: resp_tx,
    };
    tx.send(cmd).await.unwrap();
    let res = resp_rx.await;
    println!("GOT = {:?}", res);
});
```

# Relationships

## Builds Upon
- **tokio-shared-state** -- message passing is the alternative to the mutex-based approach introduced in Ch. 4
- **tokio-spawn** -- tasks are the endpoints of channel communication

## Enables
- **tokio-select** -- `select!` can multiplex across multiple channel receivers
- **tokio-streams** -- channels can be used as stream sources

## Related
- None explicitly beyond the above

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `std::sync::mpsc` or `crossbeam::channel` in async code.
  **Correction**: These block the thread, which is not allowed in async code. Use `tokio::sync::mpsc` instead.

- **Error**: Forgetting to clone the `mpsc::Sender` before moving it into a spawned task.
  **Correction**: Clone the sender for each additional task: `let tx2 = tx.clone()`. Moving the original sender means only one task can send.

- **Error**: Using an unbounded queue for command dispatch without considering memory.
  **Correction**: Always use bounded channels (`mpsc::channel(capacity)`) and choose a manageable capacity. "Unbounded queues will eventually fill up all available memory."

# Common Confusions

- **Confusion**: Thinking `oneshot::send()` needs to be `.await`-ed.
  **Clarification**: "Calling `send` on `oneshot::Sender` completes immediately and does not require an `.await`. This is because `send` on a `oneshot` channel will always fail or succeed immediately without any form of waiting."

- **Confusion**: Thinking you need to handle the `Err` from `resp.send(res)`.
  **Clarification**: The `Err` indicates the receiver dropped (cancelled the request). In many scenarios this is acceptable: "the receiver cancelling interest is an acceptable event." Using `let _ = resp.send(res)` is idiomatic.

- **Confusion**: Thinking lazy futures cause implicit queuing like callbacks do.
  **Clarification**: In Rust's async model, `async_op()` without `.await` does nothing. This is a feature: "with Tokio and asynchronous Rust, the above snippet will not result in `async_op` running at all."

# Source Reference

Chapter 5: Channels. Covers message passing motivation, the four channel primitives (mpsc, oneshot, broadcast, watch), command enum pattern, mpsc + oneshot request/response, and backpressure in bounded channels. The channel primitives overview is in "Tokio's channel primitives" section; the mpsc + oneshot pattern runs through the remainder of the chapter.

# Verification Notes

- Definition source: Directly from Ch. 5 "Message passing" and "Tokio's channel primitives" sections
- Key Properties: All from explicit statements in the chapter
- Confidence rationale: HIGH -- the source provides complete working examples with detailed explanations
- Uncertainties: broadcast and watch channels are described briefly (covered in later sections per the tutorial); mpsc and oneshot are fully worked through
- Cross-reference status: tokio-spawn from Agent A; tokio-select and tokio-streams from Agent C
