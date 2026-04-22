---
concept: Tokio Streams
slug: tokio-streams
category: async-runtime
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Streams"
chapter_number: 10
pdf_page: null
section: "Iteration / Adapters / Implementing Stream"
extraction_confidence: high
aliases:
  - "async streams"
  - "Stream trait"
  - "tokio-stream"
  - "async iteration"
prerequisites:
  - future-trait-in-depth
  - tokio-channels
extends:
  - future-trait-in-depth
related:
  - tokio-executor
  - tokio-select
  - tokio-async-io
contrasts_with: []
answers_questions:
  - "What is a Stream in async Rust?"
  - "How do I iterate over a stream?"
  - "What stream adapters does Tokio provide?"
  - "How do I implement the Stream trait?"
  - "Why do streams need to be pinned?"
  - "What is the async-stream crate?"
  - "What is the relationship between Stream and Future?"
---

# Quick Definition

A `Stream` is the asynchronous equivalent of `std::iter::Iterator` -- it yields a series of values asynchronously. The `Stream` trait provides `poll_next`, which mirrors `Future::poll` but returns `Poll<Option<Self::Item>>` to signal either a next value, pending state, or end of stream. Tokio provides stream support through the `tokio-stream` crate and the `StreamExt` trait for adapters.

# Core Definition

"A stream is an asynchronous series of values. It is the asynchronous equivalent to Rust's `std::iter::Iterator` and is represented by the `Stream` trait. Streams can be iterated in `async` functions. They can also be transformed using adapters. Tokio provides a number of common adapters on the `StreamExt` trait." (Tokio Tutorial, Ch. 10, introduction)

The `Stream` trait definition:

```rust
use std::pin::Pin;
use std::task::{Context, Poll};

pub trait Stream {
    type Item;

    fn poll_next(
        self: Pin<&mut Self>,
        cx: &mut Context<'_>
    ) -> Poll<Option<Self::Item>>;

    fn size_hint(&self) -> (usize, Option<usize>) {
        (0, None)
    }
}
```

"The `Stream::poll_next()` function is much like `Future::poll`, except it can be called repeatedly to receive many values from the stream. Just as we saw in Async in depth, when a stream is **not** ready to return a value, `Poll::Pending` is returned instead. The task's waker is registered. Once the stream should be polled again, the waker is notified." (Tokio Tutorial, Ch. 10, "Implementing Stream")

# Prerequisites

- **future-trait-in-depth** -- the `Stream` trait is modeled directly on `Future`; `poll_next` follows the same poll/waker contract
- **tokio-channels** -- channels are a common source of streams, and the broadcast example uses pub/sub channels

# Key Properties

1. `poll_next` returns `Poll::Ready(Some(item))` for the next value
2. `poll_next` returns `Poll::Ready(None)` to signal end of stream
3. `poll_next` returns `Poll::Pending` when no value is available yet (same waker contract as `Future::poll`)
4. `size_hint()` works the same way as with iterators
5. Streams are iterated with `while let Some(v) = stream.next().await` (no async `for` loops in Rust yet)
6. Calling `next()` requires the stream to be **pinned** -- use `tokio::pin!` for non-`Unpin` streams
7. Tokio provides stream support in the separate `tokio-stream` crate (not in `tokio` itself, pending `Stream` trait stabilization)
8. The `StreamExt` trait provides adapters: `map`, `filter`, `take`, `filter_map`, and more
9. Adapter ordering matters: `filter` then `take` differs from `take` then `filter`
10. Manual `Stream` implementations typically compose inner futures and other streams

# Construction / Recognition

## Iterating a Stream

```rust
use tokio_stream::StreamExt;

#[tokio::main]
async fn main() {
    let mut stream = tokio_stream::iter(&[1, 2, 3]);

    while let Some(v) = stream.next().await {
        println!("GOT = {:?}", v);
    }
}
```

"Like iterators, the `next()` method returns `Option<T>` where `T` is the stream's value type. Receiving `None` indicates that stream iteration is terminated." (Tokio Tutorial, Ch. 10, "Iteration")

## Using Adapters

```rust
let messages = subscriber
    .into_stream()
    .filter(|msg| match msg {
        Ok(msg) if msg.content.len() == 1 => true,
        _ => false,
    })
    .map(|msg| msg.unwrap().content)
    .take(3);
```

"Note that the order in which adapters are applied matters. Calling `filter` first then `take` is different than calling `take` then `filter`." (Tokio Tutorial, Ch. 10, "Adapters")

## Implementing Stream Manually

An `Interval` stream that yields `()` three times at 10ms intervals:

```rust
use tokio_stream::Stream;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::Duration;

struct Interval {
    rem: usize,
    delay: Delay,
}

impl Stream for Interval {
    type Item = ();

    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>)
        -> Poll<Option<()>>
    {
        if self.rem == 0 {
            return Poll::Ready(None);
        }

        match Pin::new(&mut self.delay).poll(cx) {
            Poll::Ready(_) => {
                let when = self.delay.when + Duration::from_millis(10);
                self.delay = Delay { when };
                self.rem -= 1;
                Poll::Ready(Some(()))
            }
            Poll::Pending => Poll::Pending,
        }
    }
}
```

## Using async-stream Crate

The `async-stream` crate provides a `stream!` macro as an ergonomic alternative to manual implementation:

```rust
use async_stream::stream;
use std::time::{Duration, Instant};

let s = stream! {
    let mut when = Instant::now();
    for _ in 0..3 {
        let delay = Delay { when };
        delay.await;
        yield ();
        when += Duration::from_millis(10);
    }
};
```

"The `async-stream` crate is available as a temporary solution. This crate provides a `stream!` macro that transforms the input into a stream." (Tokio Tutorial, Ch. 10, "async-stream")

# Context & Application

Streams are the natural abstraction for any source of multiple asynchronous values: network message channels, pub/sub subscriptions, file chunks, database result sets, timer intervals, etc.

The Mini-Redis broadcast example demonstrates a real use case: subscribing to a pub/sub channel returns a `Subscriber`, which is converted to a stream via `into_stream()`. The stream must be pinned before iteration:

```rust
let client = client::connect("127.0.0.1:6379").await?;
let subscriber = client.subscribe(vec!["numbers".to_string()]).await?;
let messages = subscriber.into_stream();

tokio::pin!(messages);

while let Some(msg) = messages.next().await {
    println!("got = {:?}", msg);
}
```

"Calling `next()` on a stream requires the stream to be pinned. The `into_stream()` function returns a stream that is *not* pinned, we must explicitly pin it in order to iterate it." (Tokio Tutorial, Ch. 10, "Mini-Redis broadcast")

On pinning: "A Rust value is 'pinned' when it can no longer be moved in memory. A key property of a pinned value is that pointers can be taken to the pinned data and the caller can be confident the pointer stays valid. This feature is used by `async/await` to support borrowing data across `.await` points." (Tokio Tutorial, Ch. 10)

The `Stream` trait is currently in `futures-core`, not the standard library. Once stabilized in `std`, Tokio's stream utilities will move from `tokio-stream` into the `tokio` crate.

# Examples

**Example 1** (Ch. 10, "Adapters"): Chaining filter, map, and take to process only single-digit numbers from a subscription:
```rust
let messages = subscriber
    .into_stream()
    .filter(|msg| match msg {
        Ok(msg) if msg.content.len() == 1 => true,
        _ => false,
    })
    .map(|msg| msg.unwrap().content)
    .take(3);
```
Output: `b"1"`, `b"3"`, `b"6"` -- only single-byte messages, stopping after three.

**Example 2** (Ch. 10, "Implementing Stream"): The `Interval` stream composes a `Delay` future. Each `poll_next` polls the inner delay. When the delay completes, it creates a new delay 10ms later, decrements the counter, and yields `()`. When the counter reaches zero, it returns `None` to end the stream. This demonstrates how streams compose futures.

# Relationships

## Builds Upon
- **future-trait-in-depth** -- `poll_next` follows the same `Pin<&mut Self>`, `Context`, `Poll` pattern as `Future::poll`
- **tokio-channels** -- channel receivers are natural stream sources

## Enables
- Reactive data processing pipelines with adapter chains
- Integration with `select!` via `StreamExt::next()` in select branches

## Related
- **tokio-executor** -- streams are polled by the same executor machinery as futures
- **tokio-select** -- streams can be used as `select!` branches via `next()`
- **tokio-async-io** -- buffered I/O readers can produce streams of lines
- **tokio-framing** -- codec-based framing produces streams of decoded messages

## Contrasts With
- None explicitly -- the analogy is Stream:Iterator as Future:synchronous-value

# Common Errors

- **Error**: Attempting to iterate a stream without pinning it first.
  **Correction**: Call `tokio::pin!(stream)` before the `while let` loop, or use `Box::pin(stream)` for heap pinning. The error message mentions `Unpin` not being implemented.

- **Error**: Applying adapters in the wrong order, expecting `take(3).filter(...)` to filter first.
  **Correction**: Adapter order matters. `filter(...).take(3)` filters then takes 3 matching items. `take(3).filter(...)` takes 3 items then filters, potentially yielding fewer than 3.

- **Error**: Expecting a stream subscription to receive all published messages.
  **Correction**: "Some early messages may be dropped as there is a race between subscribing and publishing." Subscribe before publishing starts to avoid lost messages.

# Common Confusions

- **Confusion**: Expecting Rust to support `async for` loops over streams.
  **Clarification**: "Currently, the Rust programming language does not support async `for` loops. Instead, iterating streams is done using a `while let` loop paired with `StreamExt::next()`." This may change in a future Rust edition.

- **Confusion**: Looking for the `Stream` trait in `tokio` or `std`.
  **Clarification**: The `Stream` trait lives in `futures-core`. Tokio's stream utilities and adapters are in the separate `tokio-stream` crate. "Once the `Stream` trait is stabilized in the Rust standard library, Tokio's stream utilities will be moved into the `tokio` crate."

- **Confusion**: Thinking `poll_next` returning `Poll::Ready(None)` is the same as `Poll::Pending`.
  **Clarification**: `Poll::Ready(None)` means the stream is **finished** -- no more values will ever come. `Poll::Pending` means no value is available **yet** but more may arrive later.

# Source Reference

Chapter 10: "Streams," all sections. Lines 1-418 of `10-streams.md`.

# Verification Notes

- Definition source: Direct quotations from the introduction and "Implementing Stream" section
- Key Properties: Derived from the trait definition, explicit statements about iteration patterns, pinning, and adapter behavior
- Confidence rationale: HIGH -- the source provides the complete trait definition, multiple adapter examples, a manual implementation, and the `async-stream` alternative
- Uncertainties: The `Stream` trait stabilization timeline is noted as pending
- Cross-reference status: All slugs reference cards from this extraction set or from Agents A/B
