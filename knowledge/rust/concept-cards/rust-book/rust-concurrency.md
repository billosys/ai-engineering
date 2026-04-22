---
concept: Rust Concurrency
slug: rust-concurrency
category: language-semantics
subcategory: concurrency
tier: intermediate
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Fearless Concurrency"
chapter_number: 16
pdf_page: null
section: "Threads, Message Passing, Shared State, Send and Sync"
extraction_confidence: high
aliases:
  - "fearless concurrency"
  - "threads"
  - "message passing"
  - "channels"
  - "mpsc"
  - "shared state"
  - "Mutex"
  - "Arc"
  - "Send trait"
  - "Sync trait"
  - "thread safety"
prerequisites:
  - rust-smart-pointers
extends: []
related:
  - rust-async-await
  - rust-smart-pointers
contrasts_with:
  - rust-async-await
answers_questions:
  - "What is fearless concurrency in Rust?"
  - "How do I create threads in Rust?"
  - "How do I use move closures with threads?"
  - "What are channels and how do I use message passing?"
  - "What is mpsc and how does it work?"
  - "How do I share state between threads with Mutex<T>?"
  - "What is Arc<T> and why can't I use Rc<T> across threads?"
  - "What are the Send and Sync traits?"
  - "What is the difference between Mutex<T>/Arc<T> and RefCell<T>/Rc<T>?"
  - "How does Rust prevent data races at compile time?"
---

# Quick Definition

Rust's concurrency model, called "fearless concurrency," leverages the ownership and type systems to catch many concurrency errors at compile time rather than runtime. The standard library provides OS-level threads (1:1 model), channels for message passing (`mpsc`), mutexes for shared-state concurrency (`Mutex<T>` with `Arc<T>`), and the marker traits `Send` and `Sync` that extend safety guarantees to user-defined types.

# Core Definition

**Fearless Concurrency**: "By leveraging ownership and type checking, many concurrency errors are compile-time errors in Rust rather than runtime errors." The ownership and type systems help manage both memory safety and concurrency problems, so "incorrect code will refuse to compile and present an error explaining the problem."

**Threads**: "The Rust standard library uses a 1:1 model of thread implementation, whereby a program uses one operating system thread per one language thread." Create threads with `thread::spawn`, passing a closure. The return type is `JoinHandle<T>` -- call `join()` to block until the thread completes. "When the main thread of a Rust program completes, all spawned threads are shut down." Use `move` closures to transfer ownership of captured values into the spawned thread: "By adding the `move` keyword before the closure, we force the closure to take ownership of the values it's using."

**Message Passing via Channels**: Rust provides `mpsc::channel` -- "multiple producer, single consumer." A channel "has two halves: a transmitter and a receiver." The transmitter's `send` method "takes ownership of its parameter, and when the value is moved the receiver takes ownership of it." This prevents using a value after sending it. The receiver offers `recv` (blocking) and `try_recv` (non-blocking). The receiver can be used as an iterator in a `for` loop. Create multiple producers by cloning the transmitter with `tx.clone()`.

**Shared-State Concurrency with `Mutex<T>`**: "Mutex is an abbreviation for mutual exclusion, as in a mutex allows only one thread to access some data at any given time." Call `lock()` to acquire the lock, which returns a `MutexGuard` wrapped in a `LockResult`. `MutexGuard` implements `Deref` to access inner data and `Drop` to release the lock automatically. "The type system ensures that we acquire a lock before using the value." `Mutex<T>` provides interior mutability like `RefCell<T>`.

**`Arc<T>` for Thread-Safe Reference Counting**: "`Arc<T>` is a type like `Rc<T>` that is safe to use in concurrent situations. The a stands for atomic, meaning it's an atomically reference-counted type." `Rc<T>` cannot implement `Send` because its reference count updates are not atomic. "`Arc<T>` and `Rc<T>` have the same API" -- the only difference is thread safety, which comes with "a performance penalty that you only want to pay when you really need to."

**`Send` and `Sync` Marker Traits**: "The `Send` marker trait indicates that ownership of values of the type implementing `Send` can be transferred between threads." Almost all types implement `Send` except `Rc<T>`. "The `Sync` marker trait indicates that it is safe for the type implementing `Sync` to be referenced from multiple threads. In other words, any type `T` implements `Sync` if `&T` (an immutable reference to `T`) implements `Send`." `RefCell<T>` does not implement `Sync` because its runtime borrow checking is not thread-safe. "Types composed entirely of other types that implement the `Send` and `Sync` traits also automatically implement `Send` and `Sync`." Manually implementing these traits requires unsafe code.

# Prerequisites

- **rust-smart-pointers** -- understanding `Rc<T>`, `RefCell<T>`, `Deref`, and `Drop` is essential for grasping `Arc<T>`, `Mutex<T>`, and why `Rc<T>` is not thread-safe

# Key Properties

1. Rust uses a 1:1 thread model (one OS thread per language thread)
2. `thread::spawn` takes a closure; returns `JoinHandle<T>` for joining
3. `move` closures transfer ownership of captured values into spawned threads
4. `mpsc::channel` returns `(Sender<T>, Receiver<T>)` -- multiple producers, single consumer
5. `send()` takes ownership of its argument, preventing use-after-send
6. `Receiver` implements `Iterator`, enabling `for msg in rx` loops
7. `Mutex::lock()` returns `MutexGuard` which auto-releases the lock when dropped
8. `Mutex<T>` provides interior mutability (like `RefCell<T>` but thread-safe)
9. `Arc<T>` is the atomic (thread-safe) version of `Rc<T>` -- same API, performance penalty
10. `Rc<T>` does not implement `Send`; use `Arc<T>` for cross-thread shared ownership
11. `Send` means ownership can transfer between threads; `Sync` means references can be shared
12. `RefCell<T>` does not implement `Sync`; use `Mutex<T>` for thread-safe interior mutability
13. Deadlocks remain possible with `Mutex<T>` -- Rust prevents data races, not all logic errors
14. Types composed entirely of `Send`/`Sync` types are automatically `Send`/`Sync`

# Construction / Recognition

## Thread-Safe vs. Single-Threaded Equivalents

| Single-Threaded | Thread-Safe | Purpose |
|-----------------|-------------|---------|
| `Rc<T>` | `Arc<T>` | Shared ownership |
| `RefCell<T>` | `Mutex<T>` | Interior mutability |
| `Rc<RefCell<T>>` | `Arc<Mutex<T>>` | Shared mutable data |
| `Cell<T>` | `AtomicT` types | Simple value mutation |

## Thread Spawning with Move Closure

```rust
use std::thread;
let v = vec![1, 2, 3];
let handle = thread::spawn(move || {
    println!("vector: {v:?}");
});
handle.join().unwrap();
```

## Channel Message Passing

```rust
use std::sync::mpsc;
use std::thread;
let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    tx.send(String::from("hello")).unwrap();
});
let received = rx.recv().unwrap();
```

## Shared Counter with Arc<Mutex<T>>

```rust
use std::sync::{Arc, Mutex};
use std::thread;
let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];
for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}
for handle in handles {
    handle.join().unwrap();
}
println!("Result: {}", *counter.lock().unwrap());
```

# Context & Application

- **Typical contexts**: CPU-bound parallelism, background processing, concurrent data access, producer-consumer patterns.
- **Common applications**: Web servers handling multiple connections; parallel data processing; background tasks with progress reporting via channels; shared caches protected by `Arc<Mutex<T>>`.
- **Design guidelines**: Use message passing (channels) when transferring ownership between threads. Use shared state (`Arc<Mutex<T>>`) when multiple threads need to read and write the same data. Prefer `Arc<T>` without `Mutex<T>` when data is read-only after creation. For simple numeric operations, consider `std::sync::atomic` types instead of `Mutex<T>`.
- **When to use threads vs. async**: Threads are best for CPU-bound parallelism; async (Chapter 17) is better for I/O-bound concurrency with many tasks.

# Examples

**Example 1** -- Thread with `move` closure (Ch. 16, "Using move Closures with Threads"):
```rust
use std::thread;
let v = vec![1, 2, 3];
let handle = thread::spawn(move || {
    println!("Here's a vector: {v:?}");
});
handle.join().unwrap();
// v is no longer usable here -- ownership was moved
```

**Example 2** -- Multiple producers via cloned transmitter (Ch. 16, "Creating Multiple Producers"):
```rust
use std::sync::mpsc;
use std::thread;
let (tx, rx) = mpsc::channel();
let tx1 = tx.clone();
thread::spawn(move || { tx1.send("from thread 1").unwrap(); });
thread::spawn(move || { tx.send("from thread 2").unwrap(); });
for received in rx {
    println!("Got: {received}");
}
```

**Example 3** -- `MutexGuard` auto-release (Ch. 16, "The API of Mutex<T>"):
```rust
use std::sync::Mutex;
let m = Mutex::new(5);
{
    let mut num = m.lock().unwrap();
    *num = 6;
} // MutexGuard dropped here, lock released
println!("m = {:?}", m);
```

**Example 4** -- Compile-time safety: `Rc<T>` rejected for threads (Ch. 16, "Multiple Ownership with Multiple Threads"):

Attempting to use `Rc<Mutex<i32>>` with `thread::spawn` produces: `` `Rc<Mutex<i32>>` cannot be sent between threads safely `` because `` the trait `Send` is not implemented for `Rc<Mutex<i32>>` ``. Switching to `Arc<Mutex<i32>>` resolves the error.

# Relationships

## Builds Upon
- **rust-smart-pointers** -- `Rc<T>` and `RefCell<T>` are the single-threaded predecessors of `Arc<T>` and `Mutex<T>`

## Enables
- **rust-async-await** -- async runtimes often use threads under the hood; `Send`/`Sync` bounds are critical for async tasks

## Related
- **rust-async-await** -- presents an alternative concurrency model using futures and tasks instead of threads
- **rust-smart-pointers** -- `Arc<T>` is the thread-safe version of `Rc<T>`; `Mutex<T>` is the thread-safe version of `RefCell<T>`

## Contrasts With
- **rust-async-await** -- threads are 1:1 OS threads for parallelism; async uses cooperative multitasking for I/O-bound concurrency

# Common Errors

- **Error**: Spawning a thread with a closure that borrows from the main thread, getting "closure may outlive the current function."
  **Correction**: Add the `move` keyword to the closure to transfer ownership into the spawned thread.

- **Error**: Using `Rc<T>` across threads, getting `` `Rc<T>` cannot be sent between threads safely ``.
  **Correction**: Replace `Rc<T>` with `Arc<T>`. They have the same API but `Arc<T>` uses atomic operations for thread safety.

- **Error**: `Mutex::lock()` panics because "another thread holding the lock panicked" (poisoned mutex).
  **Correction**: Handle the `PoisonError` from `lock()` rather than calling `unwrap()`. Use `into_inner()` on the error to recover the data if appropriate.

# Common Confusions

- **Confusion**: Rust prevents all concurrency bugs, including deadlocks.
  **Clarification**: Rust prevents data races at compile time, but "Mutex<T> comes with the risk of creating deadlocks." Deadlocks are logic errors that the type system cannot catch.

- **Confusion**: `Arc<T>` should always be used instead of `Rc<T>` for safety.
  **Clarification**: "Thread safety comes with a performance penalty that you only want to pay when you really need to." Use `Rc<T>` in single-threaded contexts and `Arc<T>` only when sharing across threads.

- **Confusion**: Channels can only have one sender.
  **Clarification**: `mpsc` stands for "multiple producer, single consumer." Clone the transmitter to create multiple senders. However, there can only be one receiver.

# Source Reference

The Rust Programming Language, Chapter 16: Fearless Concurrency -- Threads, Message Passing, Shared-State Concurrency, and the Send and Sync Traits.

# Verification Notes

- Definition source: Direct from Chapter 16 of The Rust Programming Language
- Confidence rationale: High -- concurrency primitives are stable standard library types with clear documentation
- Uncertainties: None significant; all concepts are well-established
- Cross-reference status: Related cards verified against planned card slugs (rust-smart-pointers, rust-async-await)
