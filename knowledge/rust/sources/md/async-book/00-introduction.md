NOTE: this guide is currently undergoing a rewrite after a long time without much work. It is work in progress, much is missing, and what exists is a bit rough.

# Introduction

This book is a guide to asynchronous programming in Rust. It is designed to help you take your first steps and to discover more about advanced topics. We don't assume any experience with asynchronous programming (in Rust or another language), but we do assume you're familiar with Rust already. If you want to learn about Rust, you could start with [The Rust Programming Language](https://doc.rust-lang.org/stable/book/).

This book has two main parts: [part one](part-guide/intro.md) is a beginners guide, it is designed to be read in-order and to take you from total beginner to intermediate level. Part two is a collection of stand-alone chapters on more advanced topics. It should be useful once you've worked through part one or if you already have some experience with async Rust.

You can navigate this book in multiple ways:

* You can read it front to back, in order. This is the recommend path for newcomers to async Rust, at least for [part one](part-guide/intro.md) of the book.
* There is a summary contents on the left-hand side of the webpage.
* If you want information about a broad topic, you could start with the topic index.
* If you want to find all discussion about a specific topic, you could start with the detailed index.
* You could see if your question is answered in the FAQs.


## What is Async Programming and why would you do it?

In concurrent programming, the program does multiple things at the same time (or at least appears to). Programming with threads is one form of concurrent programming. Code within a thread is written in sequential style and the operating system executes threads concurrently. With async programming, concurrency happens entirely within your program (the operating system is not involved). An async runtime (which is just another crate in Rust) manages async tasks in conjunction with the programmer explicitly yielding control by using the `await` keyword.

Because the operating system is not involved, *context switching* in the async world is very fast. Furthermore, async tasks have much lower memory overhead than operating system threads. This makes async programming a good fit for systems which need to handle very many concurrent tasks and where those tasks spend a lot of time waiting (for example, for client responses or for IO). It also makes async programming a good fit for microcontrollers with very limited amounts of memory and no operating system that provides threads.

Async programming also offers the programmer fine-grained control over how tasks are executed (levels of parallelism and concurrency, control flow, scheduling, and so forth). This means that async programming can be expressive as well as ergonomic for many uses. In particular, async programming in Rust has a powerful concept of cancellation and supports many different flavours of concurrency (expressed using constructs including `spawn` and its variations, `join`, `select`, `for_each_concurrent`, etc.). These allow composable and reusable implementations of concepts like timeouts, pausing, and throttling.


## Hello, world!

Just to give you a taste of what async Rust looks like, here is a 'hello, world' example. There is no concurrency, and it doesn't really take advantage of being async. It does define and use an async function, and it does print "hello, world!":

```rust,edition2021
{{#include ../examples/hello-world/src/main.rs}}
```

We'll explain everything in detail later. For now, note how we define an asynchronous function using `async fn` and call it using `.await` - an async function in Rust doesn't do anything unless it is `await`ed[^blocking].

Like all examples in this book, if you want to see the full example (including `Cargo.toml`, for example) or to run it yourself locally, you can find them in the book's GitHub repo: e.g., [examples/hello-world](https://github.com/rust-lang/async-book/tree/master/examples/hello-world).


## Development of Async Rust

The async features of Rust have been in development for a while, but it is not a 'finished' part of the language. Async Rust (at least the parts available in the stable compiler and standard libraries) is reliable and performant. It is used in production in some of the most demanding situations at the largest tech companies. However, there are some missing parts and rough edges (rough in the sense of ergonomics rather than reliability). You are likely to stumble upon some of these parts during your journey with async Rust. For most missing parts, there are workarounds and these are covered in this book.

Currently, working with async iterators (also known as streams) is where most users find some rough parts. Some uses of async in traits are not yet well-supported. There is not a good solution for async destruction.

Async Rust is being actively worked on. If you want to follow development, you can check out the Async Working Group's [home page](https://rust-lang.github.io/wg-async/meetings.html) which includes their [roadmap](https://rust-lang.github.io/wg-async/vision/roadmap.html). Or you could read the async [project goal](https://github.com/rust-lang/rust-project-goals/issues/105) within the Rust Project.

Rust is an open source project. If you'd like to contribute to development of async Rust, start at the [contributing docs](https://github.com/rust-lang/rust/blob/master/CONTRIBUTING.md) in the main Rust repo.


[^blocking]: This is actually a bad example because `println` is *blocking IO* and it is generally a bad idea to do blocking IO in async functions. We'll explain what blocking IO is in [chapter TODO]() and why you shouldn't do blocking IO in an async function in [chapter TODO]().


---

# Navigation

TODO Intro to navigation

- [By topic](topics.md)
- [FAQs]()
- [Index](index.md)


---

# Topic index

## Concurrency and parallelism

- [Introduction](../part-guide/concurrency.md#concurrency-and-parallelism)
- [Running async tasks in parallel using `spawn`](../part-guide/async-await.md#spawning-tasks)
- [Running futures concurrently using `join` and `select`](../part-guide/concurrency-primitives.md)
- [Mixing sync and async concurrency](../part-guide/io.md#other-blocking-operations)


## Correctness and safety

- Cancellation
  - [Introduction](../part-guide/more-async-await.md#cancellation)
  - [In `select` and `try_join`](../part-guide/concurrency-primitives.md)


## Performance

- Blocking
  - [Introduction](../part-guide/more-async-await.md#blocking-and-cancellation)
  - [Blocking and non-blocking IO](../part-guide/io.md)
  - [CPU-intensive code](../part-guide/io.md#other-blocking-operations)


## Testing

- [Unit test syntax](../part-guide/more-async-await.md#unit-tests)


---

# Index



- Async/`async`
  - [blocks](../part-guide/more-async-await.md#async-blocks)
  - [closures](../part-guide/more-async-await.md#async-closures)
  - [functions](../part-guide/async-await.md#async-functions)
  - [traits](../part-guide/more-async-await.md#async-traits)
  - [c.f., threads](../part-guide/concurrency.md#async-programming)
- [`await`](../part-guide/async-await.md#await)



- [Blocking](../part-guide/more-async-await.md#blocking-and-cancellation)
  - [IO](../part-guide/more-async-await.md#blocking-io)
  - [CPU-intensive tasks](../part-guide/io.md#other-blocking-operations)



- [Cancellation](../part-guide/more-async-await.md#cancellation)
  - [`CancellationToken`](../part-guide/more-async-await.md#cancellation)
  - [In `select`](../part-guide/concurrency-primitives.md#race-select)
- [Concurrency](../part-guide/concurrency.md)
  - [c.f., parallelism](../part-guide/concurrency.md#concurrency-and-parallelism)
  - [Primitives (`join`, `select`, etc.)](../part-guide/concurrency-primitives.md)
- [Cooperative scheduling](../part-guide/io.md#yielding)



- [Executor](../part-guide/async-await.md#the-runtime)



- [Futures](../part-guide/async-await.md#futures-and-tasks)
  - `Future` trait



- [IO](../part-guide/io.md)
  - [Blocking](../part-guide/more-async-await.md#blocking-io)



- [`join`](../part-guide/concurrency-primitives.md#join)
- [Joining tasks](../part-guide/async-await.md#joining-tasks)
- [`JoinHandle`](../part-guide/async-await.md#joinhandle)
  - [`abort`](../part-guide/more-async-await.md#cancellation)



- [Multiple runtimes](../part-guide/io.md#other-blocking-operations)
- Multitasking
  - [Cooperative](../part-guide/concurrency.md#async-programming), [yielding](../part-guide/io.md#yielding)
  - [Pre-emptive](../part-guide/concurrency.md#processes-and-threads)



- [Parallelism](../part-guide/concurrency.md#concurrency-and-parallelism)
  - [c.f., concurrency](../part-guide/concurrency.md#concurrency-and-parallelism)
- [Pinning, `Pin`](../part-reference/pinning.md)


- [`race`](../part-guide/concurrency-primitives.md#race-select)
- [Reactor](../part-guide/async-await.md#the-runtime)
- [Runtimes](../part-guide/async-await.md#the-runtime)



- [Scheduler](../part-guide/async-await.md#the-runtime)
- [`select`](../part-guide/concurrency-primitives.md#race-select)
- [Spawning tasks](../part-guide/async-await.md#spawning-tasks)



- [Tasks](../part-guide/async-await.md#futures-and-tasks)
  - [Spawning](../part-guide/async-await.md#spawning-tasks)
- Testing
  - [Unit tests](../part-guide/more-async-await.md#unit-tests)
- [Threads](../part-guide/concurrency.md#processes-and-threads)
- [Tokio](../part-guide/async-await.md#the-runtime)
- Traits
  - [async](../part-guide/more-async-await.md#async-traits)
  - `Future`
- [`try_join`](../part-guide/concurrency-primitives.md#join)



- [`Unpin`](../part-reference/pinning.md)



- [Waiting](../part-guide/io.md#other-blocking-operations)



- [Yielding](../part-guide/io.md#yielding)
- [`yield_now`](../part-guide/io.md#yielding)


---

# Part 1: A guide to asynchronous programming in Rust

This part of the book is a tutorial-style guide to async Rust. It is aimed at newcomers to async programming in Rust. It should be useful whether or not you've done async programming in other languages. If you have, you might skip the first section or skim it as a refresher. You might also want to read this [comparison to async in other languages]() sooner rather than later.

## Core concepts

We'll start by discussing different models of [concurrent programming](concurrency.md), using processes, threads, or async tasks. The first chapter will cover the essential parts of Rust's async model before we get into the nitty-gritty of async programming in the [second chapter](async-await.md) where we introduce the async and await programming paradigm. We cover some more async programming concepts in the [following chapter](more-async-await.md).

One of the main motivations for async programming is more performant IO, which we cover in the [next chapter](io.md). We also cover *blocking* in detail in the same chapter. Blocking is a major hazard in async programming where a thread is blocked from making progress by an operation (often IO) which synchronously waits.

Another motivation for async programming is that it facilitates new models for [abstraction and composition of concurrent code](concurrency-primitives.md). After covering that, we move on to [synchronization](sync.md) between concurrent tasks.

There is a chapter on [tools for async programming](tools.md).

The last few chapters cover some more specialised topics, starting with [async destruction and clean-up](dtors.md) (which is a common requirement, but since there is currently not a good built-in solution, is a bit of a specialist topic).

The next two chapters in the guide go into detail on [futures](futures.md) and [runtimes](runtimes.md), two fundamental building blocks for async programming.

Finally, we cover [timers and signal handling](timers-signals.md) and [async iterators](streams.md) (aka streams). The latter are how we program with sequences of async events (c.f., individual async events which are represented using futures or async functions). This is an area where the language is being actively developed and can be a little rough around the edges.
