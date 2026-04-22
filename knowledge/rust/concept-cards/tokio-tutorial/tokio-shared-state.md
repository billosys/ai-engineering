---
concept: Tokio Shared State
slug: tokio-shared-state
category: async-runtime
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Shared state"
chapter_number: 4
pdf_page: null
section: "Strategies"
extraction_confidence: high
aliases:
  - "shared state in tokio"
  - "async mutex"
  - "arc mutex pattern"
  - "mutex sharding"
prerequisites:
  - tokio-spawn
extends:
  - tokio-spawn
related:
  - tokio-channels
  - tokio-executor
contrasts_with: []
answers_questions:
  - "How do I share state between Tokio tasks?"
  - "Should I use std::sync::Mutex or tokio::sync::Mutex in async code?"
  - "Why can't I hold a MutexGuard across an .await?"
  - "What is mutex sharding and when should I use it?"
  - "How do I avoid deadlocks with mutexes in async Rust?"
---

# Quick Definition

Tokio provides two primary strategies for sharing state across tasks: guarding shared data with `Arc<Mutex<_>>` (using `std::sync::Mutex` for short critical sections) or spawning a dedicated task to manage the state via message passing. The choice between `std::sync::Mutex` and `tokio::sync::Mutex` is critical -- the synchronous mutex is preferred when contention is low and locks are not held across `.await` points.

# Core Definition

Shared state in Tokio wraps data in `Arc<Mutex<_>>` for concurrent access across tasks. The `Arc` enables reference-counted ownership shared across multiple tasks (potentially on multiple threads), while `Mutex` ensures exclusive access. The tutorial defines the canonical pattern:

```rust
type Db = Arc<Mutex<HashMap<String, Bytes>>>;
```

The key design decision is which mutex to use. "A common error is to unconditionally use `tokio::sync::Mutex` from within async code. An async mutex is a mutex that is locked across calls to `.await`." The rule of thumb: "using a synchronous mutex from within asynchronous code is fine as long as contention remains low and the lock is not held across calls to `.await`." (Ch. 4, "On using `std::sync::Mutex` and `tokio::sync::Mutex`")

# Prerequisites

- **tokio-spawn** -- understanding task spawning is required because shared state is passed to spawned tasks via `Arc::clone`, and the `Send` bound on spawned futures constrains which mutex guards can be held across `.await`

# Key Properties

1. `Arc<Mutex<_>>` is the standard pattern for sharing simple data (like a `HashMap`) across Tokio tasks
2. `Arc::clone()` creates a new handle (incrementing the reference count) that is moved into each spawned task
3. `std::sync::Mutex` blocks the current thread when waiting for the lock, which also blocks other tasks scheduled on that thread
4. `tokio::sync::Mutex` yields control back to the executor when waiting, but uses a synchronous mutex internally so performance is not necessarily better
5. `std::sync::MutexGuard` is not `Send`, so holding it across an `.await` produces a compile error ("future cannot be sent between threads safely")
6. Even if a MutexGuard implements `Send` (some crate implementations do), holding it across `.await` can cause deadlocks
7. The compiler calculates `Send`-ness based on scope, not explicit `drop()` calls -- you must use a block scope `{ }` to release the guard before `.await`
8. When contention becomes a problem, consider: message passing via a dedicated task, mutex sharding, or restructuring code to avoid the mutex

# Construction / Recognition

## To Use Arc<Mutex<_>> for Shared State:
1. Define the shared data type (e.g., `HashMap<String, Bytes>`)
2. Wrap it in `Arc::new(Mutex::new(data))` before the accept loop
3. Clone the `Arc` handle for each spawned task: `let db = db.clone()`
4. Move the cloned handle into the spawned async block
5. Lock the mutex within short, synchronous scopes: `let mut db = db.lock().unwrap()`
6. Ensure the `MutexGuard` is dropped before any `.await` point

## To Avoid Holding MutexGuard Across .await:
1. Wrap mutex operations in a non-async method on a struct that owns the mutex
2. Or use an explicit block scope `{ let mut lock = mutex.lock().unwrap(); *lock += 1; }` before the `.await`
3. Do NOT rely on `drop(lock)` before `.await` -- the compiler ignores explicit drops for `Send` analysis

# Context & Application

The `Bytes` type from the `bytes` crate is used instead of `Vec<u8>` because it provides shallow (reference-counted) cloning, making it efficient to clone values out of the shared `HashMap`. The term "handle" is used throughout Tokio to reference a value that provides access to some shared state -- `Arc` is the canonical handle type.

The pattern of wrapping mutex access in non-async methods is the safest approach: "The safest way to handle a mutex is to wrap it in a struct, and lock the mutex only inside non-async methods on that struct." This guarantees no `Send` errors and protects against deadlocks even with `MutexGuard` types that implement `Send`.

When the shared resource requires async operations (like I/O), the message-passing approach (covered in `tokio-channels`) is preferred over mutexes.

# Examples

**Example 1** (Ch. 4, "Initialize the HashMap"): The canonical pattern clones an `Arc` handle for each connection:
```rust
let db = Arc::new(Mutex::new(HashMap::new()));
loop {
    let (socket, _) = listener.accept().await.unwrap();
    let db = db.clone();
    tokio::spawn(async move {
        process(socket, db).await;
    });
}
```

**Example 2** (Ch. 4, "Holding a MutexGuard across an .await"): Using a block scope to release the guard before `.await`:
```rust
async fn increment_and_do_stuff(mutex: &Mutex<i32>) {
    {
        let mut lock: MutexGuard<i32> = mutex.lock().unwrap();
        *lock += 1;
    } // lock goes out of scope here
    do_something_async().await;
}
```

**Example 3** (Ch. 4, "Mutex sharding"): Splitting a single mutex into N shards to reduce contention:
```rust
type ShardedDb = Arc<Vec<Mutex<HashMap<String, Vec<u8>>>>>;
// Finding a key: hash to select shard, then lock only that shard
let shard = db[hash(key) % db.len()].lock().unwrap();
shard.insert(key, value);
```

# Relationships

## Builds Upon
- **tokio-spawn** -- shared state must be moved into spawned tasks, and the `Send` bound on `tokio::spawn` constrains mutex usage

## Enables
- **tokio-channels** -- message passing is the alternative strategy for shared state when async operations are needed

## Related
- **tokio-executor** -- the multi-threaded scheduler can move tasks between threads at `.await` points, which is why `MutexGuard` must not be held across `.await`

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `tokio::sync::Mutex` everywhere in async code because "it's async so I need an async mutex."
  **Correction**: Use `std::sync::Mutex` for short, synchronous critical sections. Only use `tokio::sync::Mutex` when you genuinely need to hold the lock across an `.await`.

- **Error**: Calling `drop(lock)` before `.await` and expecting it to satisfy the `Send` bound.
  **Correction**: The compiler uses scope-based analysis. Wrap the lock usage in an explicit block `{ }` so the guard's scope ends before the `.await`.

- **Error**: Spawning a task with `spawn_local` or similar to avoid the `Send` requirement, then locking a mutex that other tasks on the same thread also use.
  **Correction**: This causes deadlocks. If Tokio suspends the lock-holding task at an `.await`, another task on the same thread may try to lock the same mutex, deadlocking because the holding task cannot resume.

# Common Confusions

- **Confusion**: Thinking `tokio::sync::Mutex` is faster or better than `std::sync::Mutex` in async contexts.
  **Clarification**: "An asynchronous mutex is more expensive than an ordinary mutex, and it is typically better to use one of the two other approaches." The async mutex internally uses a synchronous mutex; its benefit is supporting locks held across `.await`, not better performance.

- **Confusion**: Thinking mutex sharding requires a specific crate or complex implementation.
  **Clarification**: The basic pattern is simply `Arc<Vec<Mutex<HashMap<_, _>>>>` with a hash function to select the shard. For production use, crates like `dashmap`, `leapfrog`, or `flurry` provide more sophisticated implementations.

# Source Reference

Chapter 4: Shared state. Covers strategies for sharing state (mutex vs. message passing), `std::sync::Mutex` vs. `tokio::sync::Mutex`, holding `MutexGuard` across `.await`, restructuring code, tasks/threads/contention, and mutex sharding. Key insight from "On using `std::sync::Mutex` and `tokio::sync::Mutex`" section.

# Verification Notes

- Definition source: Directly from Ch. 4 "Strategies" and "On using std::sync::Mutex and tokio::sync::Mutex" sections
- Key Properties: Derived from explicit statements throughout the chapter
- Confidence rationale: HIGH -- the source provides detailed, explicit guidance with code examples and error messages
- Uncertainties: None for the core content
- Cross-reference status: tokio-spawn and tokio-channels reference cards from other agents; tokio-executor from Agent C
