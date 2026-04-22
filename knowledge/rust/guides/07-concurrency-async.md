# Concurrency and Async Patterns

Patterns for concurrent and asynchronous Rust: synchronous threading (threads, mutexes, channels, atomics), async fundamentals (`Future`, `.await`, runtimes), the `Pin` type system (self-references, structural pinning, `pin-project`), structured concurrency and cancellation semantics, and Tokio idioms (`spawn`, `select!`, channels, shared state, async I/O, framing, streams). Concurrency in Rust is "fearless" because the type system encodes thread-safety via `Send`/`Sync` and address-stability via `Pin`/`Unpin`; most of this guide is about working with those encodings.


## Synchronous Concurrency

### CA-01: Spawn Threads with `thread::spawn` and Join Their Handles

**Strength**: SHOULD

**Summary**: `std::thread::spawn` returns a `JoinHandle<T>`; `.join()` waits for the thread, returns the closure's value, and surfaces panics as `Err`.

```rust
use std::thread;

// ✅ GOOD: join returns the closure's value; panic becomes Err
let handle = thread::spawn(|| {
    (1..=10).sum::<u64>()
});
let total: u64 = handle.join().expect("worker thread panicked");

// ✅ GOOD: closure takes ownership of captured state
let data = vec![1, 2, 3];
let handle = thread::spawn(move || data.len());
handle.join().unwrap();

// ❌ BAD: dropping the JoinHandle detaches the thread; errors silently lost
thread::spawn(|| do_important_work()); // no join, no error propagation
```

**Rationale**: A `JoinHandle` is the only safe way to observe completion and propagate panics from a worker. Dropping it does not cancel the thread (threads cannot be cancelled in safe Rust), but it does discard all error information.

**See also**: CA-03 for the `'static` bound that `thread::spawn` imposes, CA-09 for scoped threads that avoid it.

---

### CA-02: Use `move` to Transfer Ownership into a Thread

**Strength**: MUST

**Summary**: Spawned threads require `'static` closures; use `move` to force captured references into ownership transfers, or `Arc` to share.

```rust
use std::thread;

// ❌ BAD: by-reference capture fails the 'static bound
let v = vec![1, 2, 3];
// thread::spawn(|| println!("{:?}", v)); // ERROR: closure may outlive `v`

// ✅ GOOD: move transfers ownership
let v = vec![1, 2, 3];
thread::spawn(move || println!("{:?}", v)).join().unwrap();

// ✅ GOOD: Arc for shared read-only access
use std::sync::Arc;
let shared = Arc::new(vec![1, 2, 3]);
let a = Arc::clone(&shared);
thread::spawn(move || println!("{:?}", a));
```

**Rationale**: `thread::spawn`'s `'static` bound means the thread body cannot borrow from the spawner's stack because the main thread may exit first. `move` silences the "may outlive" error by giving the thread its own owned copy.

---

### CA-03: Prefer Scoped Threads for Fork-Join Workloads

**Strength**: SHOULD

**Summary**: `std::thread::scope` lets spawned threads borrow from the enclosing stack frame and joins all of them automatically on scope exit.

```rust
use std::thread;

fn sum_in_parallel(items: &[i64]) -> i64 {
    let mid = items.len() / 2;
    let (left, right) = items.split_at(mid);

    // ✅ GOOD: scope<'a> lets children borrow from the parent frame
    thread::scope(|s| {
        let l = s.spawn(|| left.iter().sum::<i64>());
        let r = s.spawn(|| right.iter().sum::<i64>());
        l.join().unwrap() + r.join().unwrap()
    })
}

// ❌ BAD: thread::spawn would require 'static data or Arc wrapping
// thread::spawn(|| left.iter().sum::<i64>()); // ERROR: borrow may outlive scope
```

**Rationale**: `thread::scope` is the synchronous analog of structured concurrency: every child thread must terminate before the scope returns, so borrows into the parent frame are statically sound. Prefer it whenever the fork and join happen in the same function.

**See also**: CA-36 (structured concurrency), CA-09 on scope lifetimes.

---

### CA-04: Protect Shared Mutable State with `Mutex`

**Strength**: MUST

**Summary**: `Mutex<T>` gives exclusive access via `lock()`; combine with `Arc<Mutex<T>>` to share across threads.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

// ✅ GOOD: Arc<Mutex<T>> is the canonical shared-mutable-state pattern
let counter = Arc::new(Mutex::new(0u64));
let mut handles = vec![];
for _ in 0..8 {
    let c = Arc::clone(&counter);
    handles.push(thread::spawn(move || {
        let mut guard = c.lock().unwrap();
        *guard += 1;
    }));
}
for h in handles { h.join().unwrap(); }
assert_eq!(*counter.lock().unwrap(), 8);

// ✅ GOOD: keep critical sections short; drop the guard explicitly
{
    let mut guard = counter.lock().unwrap();
    *guard += 1;
} // lock released here
heavy_non_locking_work();
```

**Rationale**: `Mutex` makes data-race-free mutation possible across threads. Critical sections should be as small as possible; holding a guard longer than necessary increases contention and risks deadlock.

---

### CA-05: Handle Mutex Poisoning Explicitly When It Matters

**Strength**: CONSIDER

**Summary**: A panic while holding a `Mutex` guard poisons it; `lock()` returns `PoisonError`. `.unwrap()` is usually fine; use `into_inner()` when you can recover.

```rust
use std::sync::Mutex;

let m = Mutex::new(Vec::<u32>::new());

// ✅ COMMON: unwrap on lock — propagates poisoning as a panic
let mut v = m.lock().unwrap();
v.push(1);

// ✅ RECOVERABLE: acknowledge and use the inner data anyway
let mut v = match m.lock() {
    Ok(guard) => guard,
    Err(poisoned) => poisoned.into_inner(), // take the data despite prior panic
};
v.push(2);
```

**Rationale**: Poisoning is a signal that the protected invariant may be broken. In most application code the right response is to propagate the panic. In resilient services (e.g., rebuilding cache state) you may deliberately recover.

---

### CA-06: Use `RwLock` for Read-Heavy Shared State

**Strength**: CONSIDER

**Summary**: `RwLock<T>` allows many concurrent readers or one writer; use it only when reads dominate writes.

```rust
use std::sync::RwLock;
use std::collections::HashMap;

struct Config { inner: RwLock<HashMap<String, String>> }

impl Config {
    fn get(&self, k: &str) -> Option<String> {
        // ✅ GOOD: many threads can read concurrently
        self.inner.read().unwrap().get(k).cloned()
    }
    fn set(&self, k: String, v: String) {
        // ✅ GOOD: exclusive access for writers
        self.inner.write().unwrap().insert(k, v);
    }
}
```

**Rationale**: `RwLock` costs more than `Mutex` per operation; its advantage only appears with highly read-biased workloads. Benchmark; do not use it reflexively.

---

### CA-07: Use `mpsc::channel` for Thread-to-Thread Message Passing

**Strength**: SHOULD

**Summary**: `std::sync::mpsc` gives you multi-producer single-consumer channels; prefer channels over shared state when communication is directional.

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel::<String>();

for i in 0..4 {
    let tx = tx.clone(); // ✅ producers clone the sender
    thread::spawn(move || tx.send(format!("hi from {i}")).unwrap());
}
drop(tx); // ✅ close the channel so the receiver terminates

for msg in rx {
    println!("{msg}");
}
```

**Rationale**: Channels enforce one-way data flow and make ownership transfers explicit. "Do not communicate by sharing memory; share memory by communicating." For higher performance or MPMC semantics, use the `crossbeam-channel` crate.

**See also**: CA-44 for async channels (`tokio::sync::mpsc`).

---

### CA-08: Use `Arc` to Share Ownership Across Threads

**Strength**: MUST

**Summary**: `Arc<T>` is an atomically reference-counted pointer; `Rc<T>` is not thread-safe and is `!Send`.

```rust
use std::sync::Arc;
use std::thread;

// ✅ GOOD: Arc allows shared ownership across threads
let shared = Arc::new(vec![1, 2, 3]);
let handles: Vec<_> = (0..4).map(|_| {
    let s = Arc::clone(&shared);
    thread::spawn(move || s.iter().sum::<i32>())
}).collect();

// ❌ BAD: Rc is !Send — won't compile in thread::spawn
// let rc = std::rc::Rc::new(vec![1]);
// thread::spawn(move || rc.len()); // ERROR: Rc<Vec<i32>> cannot be sent

for h in handles { h.join().unwrap(); }
```

**Rationale**: `Rc`'s reference-count increments are not atomic, so sharing an `Rc` across threads would be a data race. The compiler prevents this via `Send`. Use `Rc` in single-threaded code for the speed; use `Arc` whenever a value crosses threads.

**See also**: CA-12 for `Send`/`Sync`, TD-25 in `05-type-design.md`.

---

### CA-09: Use Atomics for Simple Counters and Flags

**Strength**: SHOULD

**Summary**: `AtomicUsize`, `AtomicBool`, etc. provide lock-free single-value concurrency; they are faster than `Mutex<T>` for scalar state.

```rust
use std::sync::atomic::{AtomicUsize, AtomicBool, Ordering};
use std::sync::Arc;
use std::thread;

// ✅ GOOD: atomic counter, no mutex needed
let counter = Arc::new(AtomicUsize::new(0));
let handles: Vec<_> = (0..8).map(|_| {
    let c = Arc::clone(&counter);
    thread::spawn(move || { c.fetch_add(1, Ordering::Relaxed); })
}).collect();
for h in handles { h.join().unwrap(); }
assert_eq!(counter.load(Ordering::Relaxed), 8);

// ✅ GOOD: shutdown flag
let running = Arc::new(AtomicBool::new(true));
let r = Arc::clone(&running);
let worker = thread::spawn(move || {
    while r.load(Ordering::Acquire) { /* do work */ }
});
running.store(false, Ordering::Release);
worker.join().unwrap();
```

**Rationale**: Atomics avoid the overhead of locking for simple state. For aggregated counters, `Relaxed` is usually correct; for flags that gate access to other memory, pair `Release` stores with `Acquire` loads.

---

### CA-10: Pick the Right Memory Ordering

**Strength**: SHOULD

**Summary**: Use `Relaxed` for independent counters, `Acquire`/`Release` for one-way synchronization, `AcqRel` for read-modify-write, and `SeqCst` only when you need a total order.

```rust
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};

let ready = AtomicBool::new(false);
let data  = AtomicUsize::new(0);

// Producer
data.store(42, Ordering::Relaxed);
ready.store(true, Ordering::Release); // ✅ publishes prior writes

// Consumer
if ready.load(Ordering::Acquire) {     // ✅ sees prior writes once true
    assert_eq!(data.load(Ordering::Relaxed), 42);
}

// ✅ Relaxed for independent counters (no cross-atomic ordering needed)
let counter = AtomicUsize::new(0);
counter.fetch_add(1, Ordering::Relaxed);

// ✅ AcqRel for compare_exchange that both reads and writes
let _ = counter.compare_exchange(0, 1, Ordering::AcqRel, Ordering::Acquire);

// Use SeqCst only when you need a single global ordering across many atomics.
```

**Rationale**: Orderings are about visibility of other memory. Weaker orderings are cheaper on modern CPUs; stronger orderings are not "safer" — they are correct when you actually rely on a total order. Start by reasoning about which writes must be visible after which reads.

---

### CA-11: Prefer `Rc`/`RefCell` Single-Threaded, `Arc`/`Mutex` Multi-Threaded

**Strength**: SHOULD

**Summary**: Pick the cheapest tool that matches the threading model. Do not reach for `Arc<Mutex<T>>` when single-threaded ownership suffices.

```rust
use std::cell::RefCell;
use std::rc::Rc;
use std::sync::{Arc, Mutex};

// ✅ Single-threaded: Rc<RefCell<T>> is fast (no atomics, no locks)
let local: Rc<RefCell<Vec<i32>>> = Rc::new(RefCell::new(vec![]));
local.borrow_mut().push(1);

// ✅ Multi-threaded: Arc<Mutex<T>> is required
let shared: Arc<Mutex<Vec<i32>>> = Arc::new(Mutex::new(vec![]));
shared.lock().unwrap().push(1);
```

**Rationale**: `Arc` uses atomic refcounts; `Mutex` uses OS locking primitives. Both have real overhead you do not need in single-threaded code. The compiler tells you when you need to upgrade (via `Send`/`Sync` errors).

---

### CA-12: Understand `Send` and `Sync`

**Strength**: MUST

**Summary**: `T: Send` means a value can be transferred to another thread. `T: Sync` means `&T` can be shared across threads (equivalent to `&T: Send`). Most types are both; most breakage comes from `Rc`, `Cell`, `RefCell`, and raw pointers.

```rust
use std::cell::{Cell, RefCell};
use std::rc::Rc;
use std::sync::{Arc, Mutex};
use std::thread;

// ✅ Send + Sync: primitives, String, Vec<T: Send+Sync>, Arc, Mutex
fn move_and_share<T: Send + Sync + 'static>(_: T) {}
move_and_share(Arc::new(Mutex::new(0u64)));

// ✅ Send, not Sync: Cell, RefCell, mpsc::Sender (mostly)
// ❌ Neither: Rc<T>, raw pointers (*const T, *mut T)

fn requires_send<T: Send>(_: T) {}
let rc = Rc::new(0);
// requires_send(rc); // ERROR: Rc is !Send

// ✅ A future's Send-ness is computed from what it holds across .await
async fn ok()  { let s = String::from("hi"); yield_point().await; drop(s); }
async fn bad() { let r = Rc::new(0); yield_point().await; drop(r); } // future: !Send
async fn yield_point() {}
```

**Rationale**: Most async runtimes (Tokio's multi-threaded scheduler included) require `Send` futures. Any `!Send` type held across an `.await` poisons the whole future's `Send`-ness. The fix is almost always `Arc` over `Rc` and `Mutex` over `RefCell`.

**See also**: CA-14, CA-41, M-TYPES-SEND.


---

## Async Fundamentals

### CA-13: Async Provides Concurrency, Not Parallelism

**Strength**: SHOULD

**Summary**: `async` enables many tasks to make progress on few threads by yielding at `.await`. It is orthogonal to parallelism (which may or may not also apply).

```rust
// Concurrency: one task at a time, interleaved at .await
// Parallelism: multiple threads running simultaneously
// Tokio's multi-threaded runtime gives both; its current-thread gives only concurrency.

async fn handle(conn: Connection) { /* ... */ }

#[tokio::main]
async fn main() {
    let listener = /* ... */;
    loop {
        let conn = listener.accept().await.unwrap();
        // ✅ concurrent: accept loop continues immediately
        tokio::spawn(async move { handle(conn).await });
    }
}
```

**Rationale**: Async shines for I/O-bound workloads that spend most time waiting. A single thread can handle thousands of concurrent connections by yielding during I/O. Parallelism via multi-threaded runtimes adds hardware utilization on top; it does not replace concurrency.

---

### CA-14: `async fn` Is Lazy and Returns a Future

**Strength**: MUST

**Summary**: Calling `async fn` does not execute it; it returns a `Future` that must be `.await`ed or polled by an executor. No runtime, no progress.

```rust
async fn work() -> u32 { 42 }

#[tokio::main]
async fn main() {
    // ❌ BAD: calling but not awaiting — the future is dropped, no work happens
    let _ = work();

    // ✅ GOOD: .await drives it to completion
    let v = work().await;

    // ✅ Pattern: store-then-await so you can select over it, etc.
    let fut = work();
    let v = fut.await;
    let _ = v;
}
```

**Rationale**: Rust's futures are "pull-based" and lazy — nothing happens until polled. This is the foundation of zero-cost cancellation (drop the future to cancel) and fine-grained executor control, but it is also the most common beginner trap.

---

### CA-15: `.await` Yields Control; Sequential Awaits Are Not Concurrent

**Strength**: SHOULD

**Summary**: Back-to-back `.await`s run sequentially. To run them concurrently, use `tokio::join!`, `select!`, or `tokio::spawn`.

```rust
// ❌ SEQUENTIAL: total time = a + b
async fn seq() {
    let a = fetch_a().await; // wait for a
    let b = fetch_b().await; // then wait for b
}

// ✅ CONCURRENT: total time = max(a, b)
async fn conc() {
    let (a, b) = tokio::join!(fetch_a(), fetch_b());
}

// ✅ CONCURRENT with early exit: select races them
async fn race() {
    tokio::select! {
        a = fetch_a() => handle_a(a),
        b = fetch_b() => handle_b(b),
    }
}

async fn fetch_a() -> u32 { 1 }
async fn fetch_b() -> u32 { 2 }
fn handle_a(_: u32) {} fn handle_b(_: u32) {}
```

**Rationale**: `.await` suspends the current task until that one future completes. Beginners often assume multiple `.await`s in a function run concurrently — they do not. Use explicit combinators.

---

### CA-16: The `Future` Trait

**Strength**: CONSIDER

**Summary**: A `Future` is a state machine with one method, `poll`, which returns `Poll::Ready(output)` or `Poll::Pending`. The executor polls futures; pending futures arrange to wake the executor later via a `Waker`.

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

// The trait:
// pub trait Future {
//     type Output;
//     fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
// }

// A trivial future: already ready.
struct Ready<T>(Option<T>);
impl<T: Unpin> Future for Ready<T> {
    type Output = T;
    fn poll(mut self: Pin<&mut Self>, _: &mut Context<'_>) -> Poll<T> {
        Poll::Ready(self.0.take().expect("polled after completion"))
    }
}

// Rule: when returning Poll::Pending, arrange for cx.waker() to be called later.
```

**Rationale**: You rarely write `poll` by hand; the compiler generates it from `async fn`. But understanding the poll/waker contract explains cancellation, why futures must be pinned, and why leaking a waker without waking it stalls a task forever.

---

### CA-17: `async fn` Desugars to a State Machine

**Strength**: CONSIDER

**Summary**: An `async fn`'s body is compiled into an anonymous struct that holds local variables across `.await` points; each `.await` is a state transition. This is why held variables affect `Send`-ness.

```rust
// Conceptual desugaring:
async fn greet(name: String) -> String {
    let greeting = format!("Hello, {name}");
    tokio::task::yield_now().await; // ← suspension point
    greeting                        // ← local persisted across yield
}

// The compiler generates (roughly):
// enum GreetState {
//     Start { name: String },
//     AfterYield { greeting: String, yield_fut: YieldNow },
//     Done,
// }
// impl Future for GreetState { ... }
```

**Rationale**: This desugaring explains: why locals held across `.await` must be `Send` for `Send` futures; why the state machine's size equals "largest stack across all suspension points"; why self-referential locals need `Pin` (see CA-24, CA-26).

---

### CA-18: Async Trait Methods — Native vs `#[async_trait]`

**Strength**: SHOULD

**Summary**: Rust 1.75+ supports `async fn` in traits natively (AFIT/RPITIT). Use native async for static dispatch; use `#[async_trait]` when you need `dyn Trait`.

```rust
// ✅ GOOD: native async trait (Rust 1.75+). Static dispatch only.
trait Store {
    async fn get(&self, k: &str) -> Option<String>;
}

impl Store for InMemoryStore {
    async fn get(&self, k: &str) -> Option<String> { self.map.get(k).cloned() }
}

// ❌ LIMITATION: `dyn Store` is awkward (the returned future type is hidden)

// ✅ GOOD: use #[async_trait] when you need trait objects
use async_trait::async_trait;
#[async_trait]
trait DynStore: Send + Sync {
    async fn get(&self, k: &str) -> Option<String>;
}
fn take_dyn(_: &dyn DynStore) {}

struct InMemoryStore { map: std::collections::HashMap<String, String> }
```

**Rationale**: Native async traits compile to zero-overhead static dispatch. `#[async_trait]` boxes the returned future (`Pin<Box<dyn Future + Send>>`) to make the trait object-safe at the cost of a heap allocation per call. Pick static dispatch unless you genuinely need heterogeneous trait objects.

---

### CA-19: I/O Provides Natural Yield Points; CPU Work Does Not

**Strength**: SHOULD

**Summary**: Every async I/O operation `.await`s, which yields. A tight CPU loop in an `async fn` yields nowhere and can starve every other task on that thread.

```rust
// ✅ GOOD: I/O yields naturally
async fn handle(conn: &mut Conn) {
    loop {
        let req = conn.read_request().await;  // yields while waiting
        let resp = serve(req);                // fast — no yield needed
        conn.write_response(resp).await;      // yields while writing
    }
}

// ❌ BAD: CPU-bound loop with no yields starves other tasks
async fn sum_big(v: &[u64]) -> u64 {
    let mut s = 0;
    for x in v { s += compute(*x); } // never yields
    s
}

// ✅ GOOD: yield periodically in CPU-heavy sections
async fn sum_big_ok(v: &[u64]) -> u64 {
    let mut s = 0;
    for (i, x) in v.iter().enumerate() {
        s += compute(*x);
        if i % 1024 == 0 { tokio::task::yield_now().await; }
    }
    s
}
fn compute(x: u64) -> u64 { x }
```

**Rationale**: Cooperative schedulers depend on tasks yielding. A loop without `.await` monopolises the worker thread. `yield_now().await` is the minimal cooperative signal; for heavier CPU work, use `spawn_blocking` instead (CA-41).

**See also**: M-YIELD-POINTS.

---

### CA-20: Never Block the Async Runtime

**Strength**: MUST

**Summary**: Synchronous I/O, `std::thread::sleep`, blocking mutexes, and long CPU work all block a runtime thread. Use async equivalents or `spawn_blocking`.

```rust
use std::time::Duration;

// ❌ BAD: synchronous file I/O blocks the entire runtime thread
async fn read_config_bad() -> String {
    std::fs::read_to_string("config.toml").unwrap()
}

// ✅ GOOD: async file I/O
async fn read_config_ok() -> std::io::Result<String> {
    tokio::fs::read_to_string("config.toml").await
}

// ❌ BAD: thread::sleep blocks
async fn wait_bad() { std::thread::sleep(Duration::from_secs(1)); }

// ✅ GOOD: async sleep
async fn wait_ok()  { tokio::time::sleep(Duration::from_secs(1)).await; }

// ✅ GOOD: synchronous hashing offloaded
async fn hash(data: Vec<u8>) -> [u8; 32] {
    tokio::task::spawn_blocking(move || hash_sync(&data)).await.unwrap()
}
fn hash_sync(_: &[u8]) -> [u8; 32] { [0; 32] }
```

**Rationale**: A blocked runtime thread cannot poll any other task. On a 4-thread runtime, 4 blocked tasks halt the entire process. This is the single most common production outage in async Rust.

**See also**: See `11-anti-patterns.md` for more on blocking-in-async.


---

## Pin and Self-References

### CA-21: Values Can Move — and That Breaks Self-References

**Strength**: CONSIDER

**Summary**: In Rust, ownership transfers are moves: the value's bytes are copied to a new address. Types that contain pointers into themselves break when moved because the pointers still reference the old location.

```rust
// ✅ Moves are legal and common for most types:
let s = String::from("hi");
let t = s;            // s moved into t
// println!("{s}");   // ERROR: s is gone

// Conceptually broken self-reference (will not compile, shown for intuition):
// struct SelfRef { s: String, p: *const u8 } // p into s.as_ptr()
// let mut a = SelfRef { s: String::from("hi"), p: /* &a.s.as_ptr()[0] */ };
// let b = a; // b.p now points into the old location of a.s — dangling.
```

**Rationale**: Move semantics assume a value's address is not meaningful. Self-referential types violate that assumption; they need a guarantee that the value will not move. That guarantee is `Pin`.

**See also**: TD-23 / TD-24 / TD-25 in `05-type-design.md`, CA-22, CA-24.

---

### CA-22: `Pin<Ptr<T>>` Guarantees the Value Will Not Move

**Strength**: CONSIDER

**Summary**: `Pin<Ptr<T>>` is a wrapper around a pointer that promises the pointee's address is stable for the rest of its lifetime (unless `T: Unpin`). `Pin::new`, `Box::pin`, and `std::pin::pin!` are the usual constructors.

```rust
use std::pin::Pin;

// ✅ GOOD: heap-pinned future, standard for dyn Future
let fut: Pin<Box<dyn Future<Output = u32> + Send>> = Box::pin(async { 1 });

// ✅ GOOD: stack-pinned via the pin! macro
let fut = std::pin::pin!(async { 2 });
let _ = fut; // fut is Pin<&mut _>

// ✅ GOOD: explicit pin for safe Unpin-able types
let mut n = 7u32;
let pinned: Pin<&mut u32> = Pin::new(&mut n); // u32: Unpin, always safe

use std::future::Future;
```

**Rationale**: `Pin` is the type-system encoding of "this value's address must be stable." Futures generated by `async fn` are `!Unpin` (they may be self-referential) and therefore must be pinned before `poll`. `Future::poll`'s signature takes `self: Pin<&mut Self>` for exactly this reason.

---

### CA-23: `Unpin` Means "Safe to Move Even While Pinned"

**Strength**: CONSIDER

**Summary**: `Unpin` is an auto trait implemented for any type that does not rely on address stability. Most concrete types are `Unpin`; only `async fn`-generated futures and explicitly opted-out types are `!Unpin`.

```rust
use std::marker::PhantomPinned;

// ✅ All of these are Unpin:
fn needs_unpin<T: Unpin>() {}
needs_unpin::<u32>();
needs_unpin::<String>();
needs_unpin::<Vec<u8>>();

// ❌ Opt out of Unpin by embedding PhantomPinned
struct AddrSensitive {
    _pin: PhantomPinned,
    // ...fields that require address stability
}
// needs_unpin::<AddrSensitive>(); // ERROR: not Unpin
```

**Rationale**: `Unpin` is a negative guarantee read in reverse: "pinning me is a no-op because my address does not matter." The distinction matters because `Pin<&mut T>` permits `get_mut` to extract `&mut T` if `T: Unpin`, which in turn allows unrestricted movement. `PhantomPinned` is the stable-Rust way to opt a type out.

**See also**: TD-24 in `05-type-design.md`.

---

### CA-24: `PhantomPinned` Opts a Type Out of `Unpin`

**Strength**: SHOULD

**Summary**: Add a `PhantomPinned` field to mark a type as `!Unpin`. This is the correct signal that the type is address-sensitive.

```rust
use std::marker::PhantomPinned;
use std::pin::Pin;

struct SelfRef {
    data: String,
    slice: *const str, // points into data
    _pin: PhantomPinned, // ✅ makes SelfRef !Unpin
}

impl SelfRef {
    // Constructor must return a Pin<Box<Self>> so address is fixed before link-up
    fn new(data: String) -> Pin<Box<Self>> {
        let mut boxed = Box::pin(SelfRef {
            data,
            slice: std::ptr::null(),
            _pin: PhantomPinned,
        });
        let slice: *const str = &boxed.data[..];
        // SAFETY: we do not move the data field; we only update a raw pointer
        unsafe {
            let mut_ref: Pin<&mut Self> = boxed.as_mut();
            Pin::get_unchecked_mut(mut_ref).slice = slice;
        }
        boxed
    }
}
```

**Rationale**: Without `PhantomPinned`, the auto-derived `Unpin` impl lets callers move the value through `Pin::get_mut`, invalidating the self-reference. `PhantomPinned` is how stable Rust communicates "this is `!Unpin`."

---

### CA-25: Structural vs Non-Structural Pinning

**Strength**: CONSIDER

**Summary**: A field is "structurally pinned" if pinning the outer value implies pinning the field. You must choose per-field and stay consistent: structural fields require `unsafe` projection and must never be moved; non-structural fields may use `Pin::get_mut`.

```rust
use std::pin::Pin;
use std::marker::PhantomPinned;

struct Conn {
    // structural: inner future is pinned when Conn is pinned
    inner: SomeFuture,
    // non-structural: a counter; moving it is fine even when Conn is pinned
    bytes_in: u64,
    _pin: PhantomPinned,
}

impl Conn {
    // Structural projection — unsafe and hand-written
    fn inner(self: Pin<&mut Self>) -> Pin<&mut SomeFuture> {
        unsafe { self.map_unchecked_mut(|s| &mut s.inner) }
    }
    // Non-structural projection — safe
    fn bytes_in(self: Pin<&mut Self>) -> &mut u64 {
        unsafe { &mut self.get_unchecked_mut().bytes_in }
    }
}
struct SomeFuture;
```

**Rationale**: Pin projection is subtle: if `inner` is structurally pinned you must never offer an API that moves out of it; if it is not structurally pinned you must never rely on its address. Mixing the two is unsound. Prefer `pin-project` (CA-26) to handle this correctly.

---

### CA-26: Use `pin-project` Instead of Hand-Rolling Pin Projections

**Strength**: SHOULD

**Summary**: The `pin-project` (or `pin-project-lite`) crate generates correct, safe pin projections from attributes — no `unsafe` required.

```rust
use pin_project_lite::pin_project;
use std::pin::Pin;
use std::future::Future;
use std::task::{Context, Poll};

pin_project! {
    pub struct Timeout<F> {
        #[pin] future: F,           // structural: pinned with Timeout
        deadline: tokio::time::Instant, // non-structural: plain &mut
    }
}

impl<F: Future> Future for Timeout<F> {
    type Output = F::Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<F::Output> {
        let this = self.project();        // ✅ safe projection
        this.future.poll(cx)              // `this.future` is Pin<&mut F>
    }
}
```

**Rationale**: Pin-projection soundness conditions are tricky enough that the crate was written to encode them as attribute rules (`#[pin]` means structural, bare means non-structural). Using the crate avoids entire categories of soundness bugs and removes all `unsafe` from the caller's code.

---

### CA-27: Future `poll` Takes `Pin<&mut Self>` for a Reason

**Strength**: CONSIDER

**Summary**: `Future::poll`'s pinned receiver encodes the guarantee that futures which may be self-referential (all `async fn` outputs) are never moved between polls.

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

struct MyFut;
impl Future for MyFut {
    type Output = ();
    // Pin<&mut Self> = "I won't be moved between polls"
    fn poll(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<()> {
        Poll::Ready(())
    }
}

// To call poll yourself, you need a pinned pointer:
async fn driver() {
    let mut fut = std::pin::pin!(async { 1 });
    // fut.as_mut() gives Pin<&mut _>
    let _ = futures::future::poll_fn(|cx| fut.as_mut().poll(cx)).await;
}
```

**Rationale**: The pinned receiver is the compile-time contract that lets the compiler generate self-referential state machines for `async fn`. Without `Pin`, async Rust would require heap allocation for every future (or runtime verification).

**See also**: CA-16, CA-22.

---

### CA-28: Avoid Self-Referential Types in Safe Code

**Strength**: AVOID

**Summary**: Hand-written self-referential types almost always reach for `unsafe` and are rife with soundness pitfalls. Use indices/IDs, `Rc`/`Arc`, or helper crates (`ouroboros`, `self_cell`) instead.

```rust
// ❌ AVOID: raw self-reference via pointer
struct SelfRefBad {
    data: String,
    view: *const u8, // into data
}
// Soundness requires: never move SelfRefBad, never drop data early, no aliasing.

// ✅ GOOD: indices instead of pointers
struct Graph {
    nodes: Vec<Node>,
    edges: Vec<(usize, usize)>, // indices into nodes
}
struct Node { name: String }

// ✅ GOOD: self_cell for the rare case you truly need a borrow-inside-owner
// use self_cell::self_cell;
// self_cell!( struct OwnerAndView { owner: String, dependent: /*...*/ } );
```

**Rationale**: Indices trade the pointer-chasing of self-references for array lookups; they are almost always fast enough and always sound. Reach for `Pin` + `PhantomPinned` only when writing runtime internals.

**See also**: TD-25 in `05-type-design.md`.


---

## Structured Concurrency and Cancellation

### CA-29: Dropping a Future Cancels It

**Strength**: MUST

**Summary**: In async Rust, cancellation is not a method call — it is dropping the future. Once dropped, the future will never be polled again and all its state is freed.

```rust
use tokio::time::{timeout, Duration};

async fn fetch() -> String { "data".into() }

// ✅ timeout drops `fetch()` on deadline, which cancels it.
async fn with_deadline() {
    match timeout(Duration::from_millis(100), fetch()).await {
        Ok(s)  => println!("{s}"),
        Err(_) => println!("cancelled"), // fetch() was dropped
    }
}

// ✅ select drops all other branches when one completes
async fn race(a: impl Future<Output=()>, b: impl Future<Output=()>) {
    tokio::select! {
        _ = a => {}, // b is dropped here
        _ = b => {}, // a is dropped here
    }
}
use std::future::Future;
```

**Rationale**: Cancellation is free and infallible: just stop polling. This is a major feature of Rust's lazy futures — no cancellation token plumbing required. But it means `drop` is your cleanup hook, and any mid-operation state is simply discarded.

---

### CA-30: Cancellation Safety Means "Partial Progress Is OK"

**Strength**: MUST

**Summary**: A future is cancellation-safe if dropping it at any `.await` point does not corrupt observable state or lose data. This is about application semantics, not memory safety.

```rust
use tokio::sync::mpsc;

// ❌ CANCEL-UNSAFE: items consumed from `rx` may be lost if the future is dropped
async fn drain_unsafe(rx: &mut mpsc::Receiver<String>) {
    while let Some(item) = rx.recv().await {
        process(item).await; // ⚠ if dropped here, item is already taken
    }
}

// ✅ CANCEL-SAFE: consume then act atomically, or hold item until processed
async fn handle_one(rx: &mut mpsc::Receiver<String>) {
    if let Some(item) = rx.recv().await {
        process(item).await;
        // if dropped here, item is processed-or-unrecoverable, not straddling recv
    }
}
async fn process(_: String) {}
```

**Rationale**: Most futures in practice are cancellation-safe because `.await` points bracket state. The danger zone is code that has taken ownership of something (pulled from a queue, withdrawn from an account) and has not yet acted on it. Either reorder operations or use a transaction.

---

### CA-31: `select!` in Loops — Cancellation-Safe Branches Only

**Strength**: MUST

**Summary**: Every iteration of a `select!` in a loop drops all losing branches. If a branch takes work that it then hands off through the handler, that work could be lost on the next iteration.

```rust
use tokio::sync::mpsc;

async fn loop_safe(mut a: mpsc::Receiver<u32>, mut b: mpsc::Receiver<u32>) {
    loop {
        // ✅ recv() is cancellation-safe: dropping it leaves the item in the channel
        tokio::select! {
            Some(x) = a.recv() => handle(x).await,
            Some(y) = b.recv() => handle(y).await,
            else => break,
        }
    }
}

// ❌ NOT safe: read_exact() is not cancellation-safe; partial read may be lost
// Instead, wrap it in a spawned task or a buffered reader that persists state.
async fn handle(_: u32) {}
```

**Rationale**: Tokio documents cancellation-safety per-method. `tokio::sync::mpsc::Receiver::recv` is safe; `tokio::io::AsyncReadExt::read_exact` is not. When in doubt, check the docs for the phrase "cancellation safe."

---

### CA-32: Structured Concurrency — Tasks Live Within a Scope

**Strength**: SHOULD

**Summary**: Prefer concurrency patterns where child tasks cannot outlive the scope that spawned them. This mirrors synchronous call-stack discipline and makes cleanup correct by construction.

```rust
use tokio::task::JoinSet;

// ✅ Structured: JoinSet joins all tasks before the function returns
async fn gather(urls: Vec<String>) -> Vec<Result<String, reqwest::Error>> {
    let mut set = JoinSet::new();
    for url in urls {
        set.spawn(async move { reqwest::get(url).await?.text().await });
    }
    let mut out = Vec::new();
    while let Some(res) = set.join_next().await {
        out.push(res.unwrap());
    }
    out // all spawned tasks are complete before returning
}

// ❌ Unstructured: tokio::spawn without join is fire-and-forget
async fn leaky(urls: Vec<String>) {
    for url in urls { tokio::spawn(async move { reqwest::get(url).await.ok(); }); }
    // tasks may outlive this function indefinitely
}
```

**Rationale**: Structured concurrency (popularized by Trio) gives tasks a temporal scope: if the scope returns, all children are done. Errors and cancellations propagate predictably. Unstructured `tokio::spawn` is sometimes correct for long-lived background work, but default to structured patterns.

---

### CA-33: Cancellation Propagates Through the Task Tree

**Strength**: SHOULD

**Summary**: When a parent task is cancelled, its children should be cancelled too. Use `JoinSet::abort_all`, cancellation tokens, or structured scopes to enforce this.

```rust
use tokio::sync::CancellationToken;
use tokio::task::JoinSet;

async fn root(token: CancellationToken) {
    let mut set = JoinSet::new();
    for i in 0..4 {
        let t = token.child_token();
        set.spawn(async move { worker(i, t).await });
    }

    // ✅ When we exit this scope, cancel all children
    tokio::select! {
        _ = token.cancelled() => { set.abort_all(); }
        _ = async { while set.join_next().await.is_some() {} } => {}
    }
}

async fn worker(id: u32, t: CancellationToken) {
    tokio::select! {
        _ = t.cancelled() => println!("worker {id} cancelled"),
        _ = async { /* real work */ } => {}
    }
}
```

**Rationale**: Without cancellation propagation, a cancelled parent leaks zombie children. `tokio-util`'s `CancellationToken` is the standard way to spread a cancellation signal; `JoinSet::abort_all` is the brute-force version.

---

### CA-34: Async Has No `Drop` Equivalent for `.await`

**Strength**: CONSIDER

**Summary**: `Drop` is synchronous. If cleanup requires `.await` (flushing a connection, sending a farewell message), model it as an explicit `close()` / `shutdown()` method, not in `Drop`.

```rust
pub struct Session { /* ... */ }

impl Session {
    // ✅ Explicit async shutdown; callers must remember to call it
    pub async fn shutdown(self) -> Result<(), Error> {
        self.flush().await?;
        self.send_goodbye().await?;
        Ok(())
    }

    async fn flush(&self) -> Result<(), Error> { Ok(()) }
    async fn send_goodbye(&self) -> Result<(), Error> { Ok(()) }
}

impl Drop for Session {
    fn drop(&mut self) {
        // ❌ Cannot .await here. Best-effort, sync-only, often a log warning.
        eprintln!("Session dropped without shutdown (ok in tests, bug in prod)");
    }
}
struct Error;
```

**Rationale**: Rust has no async-drop yet. The standard workaround is an explicit async destructor method; some codebases pair this with a `Drop` impl that loudly warns. Document the shutdown requirement in the type's `Debug`/doc comments.


---

## Tokio Idioms

### CA-35: `tokio::spawn` for Independent Tasks; Understand the Bounds

**Strength**: MUST

**Summary**: `tokio::spawn` takes a `Future: Send + 'static` and returns a `JoinHandle<T>`. Tasks are ~64 bytes; spawn thousands freely. Use `move` to satisfy `'static`; hold no `!Send` types across `.await`.

```rust
use std::sync::Arc;
use tokio::sync::Mutex;

// ✅ GOOD: 'static via move, Send via Arc
async fn server(state: Arc<Mutex<State>>, listener: Listener) {
    loop {
        let conn = listener.accept().await;
        let state = Arc::clone(&state);
        tokio::spawn(async move {
            handle(conn, state).await;
        });
    }
}

// ❌ BAD: borrows from caller — fails 'static bound
// tokio::spawn(async { use_shared(&state).await; });

async fn handle(_: Connection, _: Arc<Mutex<State>>) {}
struct State; struct Listener; struct Connection;
impl Listener { async fn accept(&self) -> Connection { Connection } }
```

**Rationale**: Spawned tasks run on the Tokio scheduler and may migrate between threads at any `.await`. The `'static` and `Send` bounds encode those freedoms. "`'static` does not mean forever" — it means "contains no non-`'static` references."

---

### CA-36: Use `spawn_blocking` for CPU-Bound or Blocking Work

**Strength**: MUST

**Summary**: `tokio::task::spawn_blocking` runs a synchronous closure on a dedicated blocking pool, leaving the async workers free to serve tasks.

```rust
use tokio::task;

// ✅ Blocking/CPU work lives on the blocking pool
async fn hash_file(path: std::path::PathBuf) -> std::io::Result<[u8; 32]> {
    task::spawn_blocking(move || {
        let bytes = std::fs::read(&path)?;
        Ok(compute_hash(&bytes))
    })
    .await?
}
fn compute_hash(_: &[u8]) -> [u8; 32] { [0; 32] }
```

**Rationale**: The blocking pool (default 512 threads) is designed to absorb synchronous work. Async worker threads must never block, or the whole runtime stalls. `spawn_blocking` is the bridge.

---

### CA-37: `tokio::select!` for Per-Task Multiplexing

**Strength**: SHOULD

**Summary**: `select!` polls multiple futures concurrently on one task and completes with the first ready branch; losing branches are dropped (cancelled). Prefer it over spawning when branches share state or are short-lived.

```rust
use tokio::sync::mpsc;
use tokio::time::{sleep, Duration};

async fn watcher(mut rx: mpsc::Receiver<u32>) {
    loop {
        tokio::select! {
            // branches may borrow local state — unlike tokio::spawn
            Some(msg) = rx.recv()                       => handle(msg),
            _         = sleep(Duration::from_secs(30))  => heartbeat(),
            else                                        => break,
        }
    }
}
fn handle(_: u32) {}
fn heartbeat() {}
```

**Rationale**: `select!` stays on one task (no spawn, no `'static`, no `Send`), so branches can borrow. It also provides random branch selection, preventing starvation. Use it for timeouts, graceful shutdown signals, and channel merging.

---

### CA-38: `select!` — Resume Long Operations Across Iterations

**Strength**: SHOULD

**Summary**: To continue one operation across many `select!` loop iterations, define the future outside the loop, pin it, and pass `&mut` references; combine with a precondition to avoid polling a completed future.

```rust
use tokio::pin;
use tokio::sync::mpsc;

async fn run(mut rx: mpsc::Receiver<u32>) {
    let op = do_work();
    pin!(op);
    let mut done = false;

    loop {
        tokio::select! {
            res = &mut op, if !done => { done = true; use_result(res); }
            Some(v) = rx.recv()      => println!("msg {v}"),
            else => break,
        }
    }
}
async fn do_work() -> u32 { 42 }
fn use_result(_: u32) {}
```

**Rationale**: Defining the future inside `select!` restarts it each iteration. Pinning once and passing `&mut` resumes the same state machine. The `if !done` precondition prevents the "poll after completion" panic.

---

### CA-39: `tokio::sync::mpsc` for Async Multi-Producer Work Queues

**Strength**: SHOULD

**Summary**: Bounded `mpsc` channels provide backpressure: producers wait when the queue is full. Use `channel(n)` with a deliberate bound, not `unbounded_channel`.

```rust
use tokio::sync::mpsc;

async fn pipeline() {
    let (tx, mut rx) = mpsc::channel::<String>(128); // ✅ bounded → backpressure

    // producers
    for i in 0..10 {
        let tx = tx.clone();
        tokio::spawn(async move { tx.send(format!("job {i}")).await.unwrap(); });
    }
    drop(tx); // ✅ drop the extra sender so rx terminates

    // consumer
    while let Some(job) = rx.recv().await { handle(job).await; }
}
async fn handle(_: String) {}
```

**Rationale**: Unbounded channels can grow without limit, turning a slow consumer into an OOM. Bounded channels make the system self-regulating. A producer awaiting `send` is exactly the signal you want when downstream is overloaded.

---

### CA-40: `oneshot`, `broadcast`, and `watch` for Specific Patterns

**Strength**: SHOULD

**Summary**: Pick the channel matching your communication shape: `oneshot` for request/response, `broadcast` for fan-out of every message, `watch` for latest-value notifications.

```rust
use tokio::sync::{oneshot, broadcast, watch};

// ✅ oneshot: single reply. Non-async send — cannot deadlock.
async fn rpc() {
    let (tx, rx) = oneshot::channel::<u32>();
    tokio::spawn(async move { let _ = tx.send(42); });
    let v = rx.await.unwrap();
    let _ = v;
}

// ✅ broadcast: every receiver gets every message; slow receivers lag
async fn pubsub() {
    let (tx, _) = broadcast::channel::<String>(64);
    let mut r1 = tx.subscribe();
    let mut r2 = tx.subscribe();
    let _ = tx.send("event".into());
    let _ = r1.recv().await; let _ = r2.recv().await;
}

// ✅ watch: latest value only; readers always see the freshest
async fn config_reload() {
    let (tx, mut rx) = watch::channel::<u32>(0);
    tokio::spawn(async move {
        while rx.changed().await.is_ok() { apply(*rx.borrow()); }
    });
    tx.send(7).unwrap();
}
fn apply(_: u32) {}
```

**Rationale**: Using the wrong channel leads to pain: `mpsc` for broadcast doesn't fan out; `broadcast` for request/response lags or drops. Matching the pattern keeps the code idiomatic and the semantics clear.

---

### CA-41: Prefer `std::sync::Mutex` in Async; Use `tokio::sync::Mutex` Only Across `.await`

**Strength**: MUST

**Summary**: A synchronous mutex is fine in async code as long as the guard is not held across an `.await`. Use `tokio::sync::Mutex` only when you genuinely need the lock across an await point.

```rust
use std::sync::Mutex as StdMutex;
use std::sync::Arc;

// ✅ GOOD: short sync critical section, scoped so the guard drops before .await
struct Svc { state: StdMutex<u64> }
impl Svc {
    async fn tick(&self) {
        let val = {
            let mut g = self.state.lock().unwrap();
            *g += 1;
            *g
        }; // ← guard dropped here
        persist(val).await; // now safe to .await
    }
}

// ❌ BAD: MutexGuard (std) is !Send, but even if it were, holding it across
//        .await can deadlock other tasks on the same thread.
// let g = self.state.lock().unwrap();
// persist(*g).await;      // held across .await → bad

async fn persist(_: u64) {}
```

**Rationale**: `std::sync::Mutex` is faster than `tokio::sync::Mutex` and usually sufficient. The async mutex exists for cases where you legitimately need to await while locked (rare, typically pipelined I/O). Explicit `drop(guard)` before `.await` does *not* satisfy the compiler's `Send` analysis — use a block scope instead.

---

### CA-42: Shard a Hot `Mutex` Instead of Wrapping Everything in a Global

**Strength**: CONSIDER

**Summary**: When a single `Mutex<HashMap<...>>` becomes a bottleneck, partition by hash into N shards, each with its own mutex.

```rust
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

type Shard = Mutex<HashMap<String, Vec<u8>>>;
type Db = Arc<Vec<Shard>>;

fn make_db(shards: usize) -> Db {
    Arc::new((0..shards).map(|_| Mutex::new(HashMap::new())).collect())
}
fn shard_for<'a>(db: &'a Db, key: &str) -> &'a Shard {
    let mut h = std::collections::hash_map::DefaultHasher::new();
    std::hash::Hash::hash(key, &mut h);
    let i = (std::hash::Hasher::finish(&h) as usize) % db.len();
    &db[i]
}

fn put(db: &Db, k: String, v: Vec<u8>) { shard_for(db, &k).lock().unwrap().insert(k, v); }
fn get(db: &Db, k: &str) -> Option<Vec<u8>> { shard_for(db, k).lock().unwrap().get(k).cloned() }
```

**Rationale**: N shards reduce contention by up to Nx. For production, reach for `dashmap`, `flurry`, or `leapfrog` instead of rolling your own. Sharding is a classic answer to "my mutex is the bottleneck."

---

### CA-43: Service Types Implement Cheap `Clone` via `Arc<Inner>`

**Strength**: SHOULD

**Summary**: Clients, pools, and service handles should be cheaply `Clone` by wrapping their state in `Arc<Inner>`. Callers then share them across tasks without wrapping at every use site.

```rust
use std::sync::Arc;

#[derive(Clone)]
pub struct HttpClient { inner: Arc<ClientInner> }

struct ClientInner { /* pool, config, ... */ }

impl HttpClient {
    pub fn new() -> Self { Self { inner: Arc::new(ClientInner { }) } }
    pub async fn get(&self, _url: &str) -> Result<Vec<u8>, ()> { Ok(vec![]) }
}

// ✅ Effortless sharing across tasks
async fn demo(client: HttpClient) {
    let c = client.clone();
    tokio::spawn(async move { let _ = c.get("https://example.com").await; });
}
```

**Rationale**: `Clone` that takes a lock, copies state, or performs I/O is a footgun. An `Arc<Inner>` clone is an atomic increment — predictable, cheap, correct. This is how `reqwest::Client`, `tokio::runtime::Handle`, and most production clients are built.

**See also**: M-SERVICES-CLONE.

---

### CA-44: `AsyncRead` / `AsyncWrite` and Splitting Streams

**Strength**: SHOULD

**Summary**: Tokio's byte streams implement `AsyncRead` / `AsyncWrite`. Use `tokio::io::split` or `TcpStream::into_split` when a reader and writer need to live on different tasks.

```rust
use tokio::net::TcpStream;
use tokio::io::{AsyncReadExt, AsyncWriteExt};

async fn echo(stream: TcpStream) -> std::io::Result<()> {
    // ✅ into_split produces owned halves suitable for tokio::spawn
    let (mut rd, mut wr) = stream.into_split();
    let mut buf = vec![0u8; 4096];

    let reader = tokio::spawn(async move {
        loop {
            let n = rd.read(&mut buf).await?;
            if n == 0 { return Ok::<(), std::io::Error>(()); }
            // process...
        }
    });

    wr.write_all(b"hello\n").await?;
    reader.await.unwrap()
}
```

**Rationale**: Many protocols need concurrent reads and writes. `into_split` yields `OwnedReadHalf`/`OwnedWriteHalf` that are `Send + 'static`, which fit `tokio::spawn`. The borrowing `split` method is lighter-weight but constrains lifetimes.

---

### CA-45: Frame Byte Streams with a Read Buffer and `BufWriter`

**Strength**: SHOULD

**Summary**: For frame-oriented protocols, pair a `BufWriter<W>` for writes with a `BytesMut` read buffer; decode frames incrementally, returning `None` when more bytes are needed.

```rust
use bytes::{Buf, BytesMut};
use tokio::io::{AsyncReadExt, AsyncWriteExt, BufWriter};
use tokio::net::TcpStream;

pub struct Connection {
    stream: BufWriter<TcpStream>,
    buffer: BytesMut,
}

impl Connection {
    pub fn new(socket: TcpStream) -> Self {
        Self { stream: BufWriter::new(socket), buffer: BytesMut::with_capacity(8 * 1024) }
    }

    pub async fn read_frame(&mut self) -> std::io::Result<Option<Frame>> {
        loop {
            if let Some(frame) = try_parse(&mut self.buffer)? { return Ok(Some(frame)); }
            if self.stream.read_buf(&mut self.buffer).await? == 0 {
                return Ok(if self.buffer.is_empty() { None } else {
                    Err(std::io::ErrorKind::ConnectionReset.into())?
                });
            }
        }
    }

    pub async fn write_frame(&mut self, frame: &Frame) -> std::io::Result<()> {
        encode(&mut self.stream, frame).await?;
        self.stream.flush().await
    }
}

pub struct Frame;
fn try_parse(_b: &mut BytesMut) -> std::io::Result<Option<Frame>> { Ok(None) }
async fn encode<W: AsyncWriteExt + Unpin>(_w: &mut W, _f: &Frame) -> std::io::Result<()> { Ok(()) }
```

**Rationale**: This is Tokio's canonical framing pattern. `BufWriter` coalesces small writes; `BytesMut` accumulates inbound bytes. The two-phase "parse-or-read-more" loop handles partial frames correctly. For common framings (length-delimited, line-delimited), prefer `tokio_util::codec`.

---

### CA-46: Use `tokio_util::codec` for Standard Framings

**Strength**: CONSIDER

**Summary**: For length-delimited, line-delimited, or custom codecs, wrap an `AsyncRead`/`AsyncWrite` in `Framed<T, Codec>` to get a `Stream`/`Sink` of frames for free.

```rust
use futures::{SinkExt, StreamExt};
use tokio::net::TcpStream;
use tokio_util::codec::{Framed, LengthDelimitedCodec};

async fn proto(stream: TcpStream) -> std::io::Result<()> {
    // ✅ length-prefixed frames
    let mut framed = Framed::new(stream, LengthDelimitedCodec::new());
    while let Some(frame) = framed.next().await {
        let frame = frame?;
        framed.send(frame.freeze()).await?;
    }
    Ok(())
}
```

**Rationale**: Rolling your own codec is easy to get subtly wrong (off-by-one on lengths, incorrect buffering of partial frames). `tokio_util::codec` gives well-tested building blocks and composes with `Stream`/`Sink` adapters.

---

### CA-47: `Stream` Is the Async `Iterator`; Iterate with `while let` + `next`

**Strength**: SHOULD

**Summary**: `Stream`s yield a sequence of values asynchronously. No `async for` yet; use `while let Some(v) = stream.next().await`. Pin the stream first.

```rust
use tokio_stream::{self as stream, StreamExt};

async fn demo() {
    let mut s = stream::iter(vec![1, 2, 3]);
    while let Some(v) = s.next().await { println!("{v}"); }
}

// For non-Unpin streams (e.g., Subscriber::into_stream), pin before iterating:
async fn iter_owned<S>(s: S) where S: tokio_stream::Stream<Item = u32> {
    tokio::pin!(s);
    while let Some(v) = s.next().await { println!("{v}"); }
}
```

**Rationale**: `Stream`'s `poll_next` mirrors `Future::poll`; iteration uses `StreamExt::next()` which returns a `Future<Option<Item>>`. Pinning is required because many streams are `!Unpin`. `tokio_stream` is the crate until `Stream` lands in `std`.

---

### CA-48: Compose Streams with Adapters; Order Matters

**Strength**: SHOULD

**Summary**: `StreamExt` provides `map`, `filter`, `take`, `filter_map`, etc. Adapter order changes semantics — e.g., `filter.take(3)` differs from `take(3).filter`.

```rust
use tokio_stream::{self as stream, StreamExt};

async fn demo() {
    let s = stream::iter(1..=10)
        .filter(|n| n % 2 == 0) // evens
        .map(|n| n * n)         // 4, 16, 36, ...
        .take(3);               // first 3 squares of evens
    tokio::pin!(s);
    while let Some(v) = s.next().await { println!("{v}"); }
}
```

**Rationale**: Adapters are lazy: each one wraps the previous. `filter(pred).take(n)` filters then takes; `take(n).filter(pred)` takes first, which may produce fewer results. Think pipelines, not imperative loops.

---

### CA-49: Assert Your Public Futures Are `Send`

**Strength**: SHOULD

**Summary**: Add a compile-time assertion that your public `async fn`s return `Send` futures — an accidental `Rc` across `.await` will fail the test, not only the first user.

```rust
pub async fn fetch(id: u64) -> Result<String, ()> { let _ = id; Ok("".into()) }

#[cfg(test)]
mod send_tests {
    use super::*;
    fn assert_send<T: Send>(_: T) {}

    #[test]
    fn fetch_is_send() {
        assert_send(fetch(1));
    }
}
```

**Rationale**: `Send`-ness is computed structurally from what the future holds. A single `RefCell` or `Rc` across an `.await` — possibly added years after the function was first written — makes the future `!Send` and breaks every downstream `tokio::spawn`. Catch it in CI.

**See also**: CA-12, M-TYPES-SEND.

---

### CA-50: Return `Pin<Box<dyn Future ... + Send>>` from Trait Objects

**Strength**: CONSIDER

**Summary**: For `dyn Trait` where methods are async, either use `#[async_trait]` (which inserts `Pin<Box<dyn Future>>`) or do it manually; the receiver is a pinned boxed future.

```rust
use std::future::Future;
use std::pin::Pin;

// ✅ Manual pattern — no macro required
trait Handler: Send + Sync {
    fn handle(&self, req: u32) -> Pin<Box<dyn Future<Output = u32> + Send + '_>>;
}

struct Adder;
impl Handler for Adder {
    fn handle(&self, req: u32) -> Pin<Box<dyn Future<Output = u32> + Send + '_>> {
        Box::pin(async move { req + 1 })
    }
}

async fn use_handler(h: &dyn Handler) -> u32 { h.handle(1).await }
```

**Rationale**: Trait objects require a concrete return type. Boxing the future gives a uniform `Pin<Box<dyn Future>>` at the cost of a heap allocation per call. `#[async_trait]` is the sugar; knowing the desugaring helps debug obscure `Send`/lifetime errors.


---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| CA-01 Spawn with `thread::spawn` and join | SHOULD | `JoinHandle::join` surfaces panics |
| CA-02 `move` into threads | MUST | `'static` bound requires ownership |
| CA-03 Prefer `thread::scope` | SHOULD | Scoped threads borrow from parent |
| CA-04 `Mutex` for shared mutation | MUST | `Arc<Mutex<T>>` is the canonical pattern |
| CA-05 Handle mutex poisoning | CONSIDER | `into_inner()` recovers; `unwrap()` propagates |
| CA-06 `RwLock` for read-heavy | CONSIDER | Costlier than `Mutex`; benchmark |
| CA-07 `mpsc::channel` for messaging | SHOULD | Share by communicating |
| CA-08 `Arc` across threads, `Rc` within | MUST | `Rc` is `!Send` |
| CA-09 Atomics for counters/flags | SHOULD | Lock-free scalar concurrency |
| CA-10 Pick the right memory ordering | SHOULD | Relaxed / Acquire-Release / AcqRel / SeqCst |
| CA-11 Single- vs multi-threaded primitives | SHOULD | Do not over-synchronize |
| CA-12 `Send`/`Sync` | MUST | `!Send` across `.await` poisons the future |
| CA-13 Concurrency ≠ parallelism | SHOULD | Async gives the former, maybe the latter |
| CA-14 `async fn` is lazy | MUST | Must be `.await`ed or spawned |
| CA-15 Sequential `.await`s are sequential | SHOULD | Use `join!` / `select!` for concurrency |
| CA-16 `Future` trait | CONSIDER | Poll-based state machine + Waker |
| CA-17 `async fn` is a state machine | CONSIDER | Held locals shape `Send`-ness and size |
| CA-18 Async trait methods | SHOULD | Native AFIT for static, `#[async_trait]` for dyn |
| CA-19 I/O yields, CPU does not | SHOULD | `yield_now().await` in CPU loops |
| CA-20 Never block in async | MUST | Use async APIs or `spawn_blocking` |
| CA-21 Moves invalidate self-references | CONSIDER | Why `Pin` exists |
| CA-22 `Pin<Ptr<T>>` | CONSIDER | Address-stability guarantee |
| CA-23 `Unpin` | CONSIDER | "Pinning me is a no-op" |
| CA-24 `PhantomPinned` | SHOULD | Stable-Rust way to opt out of `Unpin` |
| CA-25 Structural pin projection | CONSIDER | Per-field choice, kept consistent |
| CA-26 Use `pin-project` | SHOULD | Safe pin projection without `unsafe` |
| CA-27 `Future::poll` takes `Pin<&mut Self>` | CONSIDER | Enables self-referential state machines |
| CA-28 Avoid self-referential types | AVOID | Use indices or helper crates |
| CA-29 Drop cancels a future | MUST | Cancellation is infallible and free |
| CA-30 Cancellation safety | MUST | About data loss, not memory safety |
| CA-31 `select!` loops need cancel-safe branches | MUST | Check docs; `recv` yes, `read_exact` no |
| CA-32 Structured concurrency | SHOULD | `JoinSet` over fire-and-forget `spawn` |
| CA-33 Propagate cancellation | SHOULD | `CancellationToken` or `abort_all` |
| CA-34 No async drop | CONSIDER | Explicit `shutdown().await` method |
| CA-35 `tokio::spawn` bounds | MUST | `Future: Send + 'static` |
| CA-36 `spawn_blocking` for CPU/blocking | MUST | Keeps async workers unblocked |
| CA-37 `tokio::select!` | SHOULD | Per-task multiplexing; branches may borrow |
| CA-38 Resume a future across iterations | SHOULD | Pin outside, `&mut`, use preconditions |
| CA-39 Bounded `mpsc` for backpressure | SHOULD | `channel(n)` over `unbounded_channel` |
| CA-40 `oneshot` / `broadcast` / `watch` | SHOULD | Match channel to pattern |
| CA-41 `std::sync::Mutex` in async | MUST | Only use `tokio::sync::Mutex` across `.await` |
| CA-42 Shard hot mutexes | CONSIDER | N shards → Nx contention drop |
| CA-43 `Arc<Inner>` for Service clone | SHOULD | Cheap, idiomatic sharing |
| CA-44 `AsyncRead`/`AsyncWrite` + split | SHOULD | `into_split` for spawned halves |
| CA-45 `BufWriter` + `BytesMut` framing | SHOULD | Parse-or-read-more loop |
| CA-46 `tokio_util::codec` for standard framings | CONSIDER | Battle-tested codecs |
| CA-47 `Stream` iteration | SHOULD | `while let Some(v) = s.next().await`; pin first |
| CA-48 `StreamExt` adapters | SHOULD | Order matters |
| CA-49 Assert public futures are `Send` | SHOULD | Catch `!Send` regressions in CI |
| CA-50 `Pin<Box<dyn Future>>` for trait objects | CONSIDER | Manual desugaring of `#[async_trait]` |


## Related Guidelines

- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for the ownership rules that underpin `Send`/`Sync` and scoped threads (CA-02, CA-03).
- **Type Design**: See `05-type-design.md` — TD-23 (`Pin<Ptr<T>>` for address-sensitive types), TD-24 (`PhantomPinned` on `!Unpin` types), TD-25 (avoid self-referential types). Directly supports CA-21 through CA-28.
- **Traits**: See `06-traits.md` for trait-object constraints and the lifetime shape of `#[async_trait]` (CA-18, CA-50).
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for the soundness obligations of hand-rolled pin projection (CA-25) and self-referential types (CA-28).
- **Anti-Patterns**: See `11-anti-patterns.md` for deep dives on blocking-in-async, unbounded channels, and `Arc<Mutex<T>>` overuse (CA-20, CA-39, CA-41, CA-42).


## External References

- [The Rust Book — Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) (Ch. 16) — threads, channels, `Mutex`, `Send`/`Sync`.
- [The Rust Book — Async and Await](https://doc.rust-lang.org/book/ch17-00-async-await.html) (Ch. 17) — futures, runtimes, `async`/`.await` fundamentals.
- [Asynchronous Programming in Rust (async-book)](https://rust-lang.github.io/async-book/) — the `Future` trait, executors, pinning, and async ecosystem.
- [Async: What We Got, What We Want (async-reference)](https://rust-lang.github.io/wg-async/vision/) — `Pin`/`Unpin` model, cancellation and structured concurrency vision, async drop.
- [Tokio Tutorial](https://tokio.rs/tokio/tutorial) — `tokio::spawn`, `select!`, channels, shared state, async I/O, framing, streams.
- [`std::pin`](https://doc.rust-lang.org/std/pin/index.html), [`PhantomPinned`](https://doc.rust-lang.org/std/marker/struct.PhantomPinned.html), [`pin-project-lite`](https://docs.rs/pin-project-lite), [`tokio-util::codec`](https://docs.rs/tokio-util/latest/tokio_util/codec/).
- Pragmatic Rust Guidelines: M-TYPES-SEND, M-YIELD-POINTS, M-SERVICES-CLONE.
