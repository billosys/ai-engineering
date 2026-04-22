---
concept: Async Concurrency Composition
slug: async-concurrency-composition
category: async-programming
subcategory: null
tier: intermediate
source: "Asynchronous Programming in Rust"
source_slug: async-book
authors: "The Rust Async Working Group"
chapter: "Composing futures concurrently"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "join and select"
  - "future composition"
  - "concurrent future combinators"
  - "async join"
  - "async select"
  - "async race"
prerequisites:
  - async-await-basics
  - async-advanced-topics
extends:
  - async-await-basics
related:
  - async-programming-overview
  - async-cancellation-cleanup
  - async-io-model
  - cancellation-safety
  - structured-concurrency
contrasts_with: []
answers_questions:
  - "What is the difference between join and select in async Rust?"
  - "How do I run multiple futures concurrently?"
  - "What is the difference between concurrency and parallelism with futures?"
  - "How does join! work in Tokio?"
  - "How does select! work in Tokio?"
  - "What is try_join! and when should I use it?"
  - "What are the cancellation risks with select?"
  - "Should I use join/select or spawn tasks?"
  - "What are async channels and locks?"
---

# Quick Definition

Async concurrency composition is the technique of running multiple futures concurrently within a single task using `join` (wait for all to complete) or `select`/`race` (wait for the first to complete, cancel the rest). Unlike spawning tasks, these combinators provide concurrency without parallelism -- futures take turns executing on the same thread, acting as "mini-executors" within a single async task. This card also covers async synchronization primitives (channels, locks) from Ch. 6 and async iterators (streams) from Ch. 12.

# Core Definition

"In this chapter we introduce two ways to compose futures concurrently without parallelism: `join` and `select`/`race`. In both cases, the futures run concurrently by time-slicing; each of the composed futures takes turns to execute then the next gets a turn. This is done *without involving the async runtime* (and therefore without multiple OS threads and without any potential for parallelism). The composing construct interleaves the futures locally. You can think of these constructs being like mini-executors which execute their component futures within a single async task." (Ch. 5, introduction)

"The fundamental difference between join and select/race is how they handle futures completing their work: a join finishes when all futures finish, a select/race finishes when one future finishes (all the others are cancelled)." (Ch. 5, introduction)

**Join**: "Tokio's `join` macro takes a list of futures and runs them all to completion concurrently (returning all the results as a tuple). It returns when all the futures have completed." `join!` "implicitly awaits its futures and produces a value. It does not create a future." For fail-fast behavior: "`try_join` works similarly to `join`, however, if any future returns an `Err`, then all the other futures are cancelled and `try_join` returns the error immediately." (Ch. 5, "Join")

**Select/Race**: "With race/select the futures are executed concurrently, but rather than waiting for all the futures to complete, we only wait for the first one to complete and then cancel the others." Tokio's `select!` "looks a bit like a `match` expression, but with `select`, all branches are run concurrently and the body of the branch which finishes first is executed with its result (the other branches are not executed and the futures are cancelled by `drop`ping)." (Ch. 5, "Race/select")

# Prerequisites

- **async-await-basics** -- understanding futures and await is essential since join/select compose futures
- **async-advanced-topics** -- understanding cancellation is critical because select intrinsically cancels futures

# Key Properties

1. `join!` runs all futures concurrently and returns when all complete; results returned as a tuple
2. `try_join!` cancels all remaining futures and returns immediately if any future returns `Err`
3. `select!` runs all futures concurrently and executes the branch of the first to complete; all others are cancelled by dropping
4. Join and select provide concurrency without parallelism -- all futures run on the same thread
5. These constructs act as "mini-executors" within a single task, not involving the async runtime scheduler
6. `join!` and `select!` implicitly await their futures; they produce values, not futures
7. If any future in a `join!` blocks the thread, none of the joined futures can make progress (risk of deadlock with mutexes)
8. `select!` supports pattern matching, `if` guards, and an `else` branch
9. `select!` is "often the primary source of cancellation in an async program"
10. Futures reused across `select!` loop iterations must be fused or guarded to prevent re-polling completed futures
11. References to futures in `select!` loops often require `pin!` because `&mut Future` requires `Unpin`
12. Spawning tasks is often simpler and more appropriate: "parallelism is often desirable, you're less likely to have bugs around cancellation or blocking, and resource allocation is usually fairer"

# Construction / Recognition

## To Join Multiple Futures:
1. Pass future-producing expressions to `join!()`: `let (a, b) = join!(fut_a, fut_b);`
2. Do not `.await` inside `join!` -- the macro handles awaiting
3. Use `try_join!` instead if you want fail-fast error behavior
4. For dynamic sets of futures, use `JoinSet` or `FuturesUnordered` with streams

## To Select/Race Multiple Futures:
1. Write `select!` with branches in the form `result = future_expr => { body }`:
```rust
select! {
    result = do_work() => { handle(result) }
    _ = timeout() => { handle_timeout() }
}
```
2. All branches must evaluate to the same type (like `match`)
3. For loops with `select!`, create futures outside the loop and pass `&mut` references
4. Pin futures with `pin!()` if needed (when `&mut Future` does not implement `Future`)
5. Use fused futures or `if` guards to prevent re-polling completed futures

## To Choose Between Join/Select and Spawning:
1. Use `join!`/`select!` when you explicitly want single-threaded concurrency or need structured composition
2. Use `spawn` when parallelism is acceptable or desirable
3. Consider that `spawn` gives fairer scheduling (runtime-managed) while `join!` can starve futures
4. Consider that `select!` introduces cancellation hazards that spawning avoids

# Context & Application

The source emphasizes that while `join!` and `select!` are powerful, spawning tasks is often the better default: "If you want parallelism (or you don't explicitly not want parallelism), spawning tasks is often a simpler alternative. Spawning tasks is usually less error-prone, more general, and performance is more predictable. On the other hand, spawning is inherently less structured, which can make lifecycle and resource management harder to reason about." (Ch. 5, introduction)

A key performance subtlety: "If you spawn two tasks and join 99 futures on one of those tasks, then the scheduler will only know about two tasks and one task will get 50% of the time and the 99 futures will each get 0.5%." (Ch. 5, introduction)

The `select!` macro is a rich source of bugs: "Cancellation with `select` in a loop is a rich source of subtle bugs. These usually happen where a future contains some state involving some data but not the data itself. When the future is dropped by cancellation, that state is lost but the underlying data is not updated. This can lead to data being lost or processed multiple times." (Ch. 5, "Race/select")

This card also incorporates content from Ch. 6 (Channels, locking, and synchronization) and Ch. 12 (Async iterators/streams). Ch. 6 outlines async channels (oneshot, mpsc, bounded/unbounded), async locks (Mutex that can be held across await points, RwLock, Semaphore), and other synchronization primitives (Notify, Barrier, OnceCell). The chapter warns about deadlock with async mutexes held across await points, and advises using `std::sync::Mutex` when the lock does not span await points. Ch. 12 outlines async iterators (streams) as an asynchronous version of iterators, covering consumption patterns (`while let` with `next`, `for_each`, `for_each_concurrent`, `collect`), stream combinators, join/select/race with streams, implementing async iterators, and sinks.

# Examples

**Example 1 -- join!** (Ch. 5, "Join"):
```rust
async fn main() {
    let (result_1, result_2) = join!(do_a_thing(), do_a_thing());
    // Use `result_1` and `result_2`.
}
```
Both calls run concurrently on the same thread. No `.await` is needed -- `join!` handles it.

**Example 2 -- select! for timeout** (Ch. 5, "Race/select"):
```rust
async fn main() {
    select! {
        result = do_a_thing() => {
            println!("computation completed and returned {result}");
        }
        _ = timeout() => {
            println!("computation timed-out");
        }
    }
}
```
Whichever future completes first has its branch executed; the other is cancelled by dropping.

**Example 3 -- select! in a loop with a shared future** (Ch. 5, "Race/select"):
```rust
async fn main() {
    let mut stream = ...;
    let mut timeout = pin!(timeout());

    loop {
        select! {
            result = stream.next() => {
                match result {
                    Some(x) => println!("received: {x}"),
                    None => break,
                }
            }
            _ = &mut timeout => {
                println!("time out!");
                break;
            }
        }
    }
}
```
The `timeout` future is created once outside the loop and referenced with `&mut`. The `pin!` macro is needed because `&mut Future` requires `Unpin`. Without `break` or a fused future, re-polling `timeout` after it completes would be a bug.

**Example 4 -- select! returning a value** (Ch. 5, "Race/select"):
```rust
let result = select! {
    result = do_a_thing() => { Some(result) }
    _ = timeout() => { None }
};
```
All branches must have the same type, like `match`.

# Relationships

## Builds Upon
- **async-await-basics** -- join/select compose futures, which are the core async/await abstraction
- **async-advanced-topics** -- cancellation semantics (from Ch. 3) are essential for understanding select

## Enables
- **async-cancellation-cleanup** -- select is "often the primary source of cancellation" requiring cleanup strategies

## Related
- **async-programming-overview** -- concurrent composition is a core capability of async programming
- **async-io-model** -- async IO operations are the typical futures composed with join/select
- **cancellation-safety** -- the formal property needed for futures used with select
- **structured-concurrency** -- join provides more structured composition than spawning

## Contrasts With
- None explicitly stated, though the source repeatedly contrasts join/select with spawning tasks

# Common Errors

- **Error**: Using a mutex within `join!` where one future holds the lock while another waits for it.
  **Correction**: "Because all the futures are executed on the same thread, if any future blocks the thread, then none of them can make progress. If using a mutex or other lock, this can easily lead to deadlock."

- **Error**: Re-polling a completed future in a `select!` loop without fusing or guarding it.
  **Correction**: Use a fused future (`future.fuse()`) or an `if` guard to prevent re-polling. "Depending on how the future is written, this might cause a panic, a logic error, or some kind of crash."

- **Error**: Moving a future into `select!` inside a loop instead of referencing it.
  **Correction**: Create the future outside the loop and use `&mut future` (with `pin!` if needed) inside the `select!`. Moving the future into `select!` would drop it on each iteration.

- **Error**: Assuming data processed by a cancelled future is safely handled.
  **Correction**: "When the future is dropped by cancellation, that state is lost but the underlying data is not updated. This can lead to data being lost or processed multiple times." Design futures to be cancellation-safe.

# Common Confusions

- **Confusion**: Thinking `join!` creates a future.
  **Clarification**: `join!` "implicitly awaits its futures and produces a value. It does not create a future." It must be used within an async context.

- **Confusion**: Thinking join/select provide parallelism.
  **Clarification**: "This is done without involving the async runtime (and therefore without multiple OS threads and without any potential for parallelism)." For parallelism, spawn tasks instead.

- **Confusion**: Thinking `select!` notifies cancelled futures or triggers cancellation tokens.
  **Clarification**: "`select` cancels futures by simply dropping them. This will not notify the future being dropped or trigger any cancellation tokens." For cooperative cancellation, use explicit cancellation tokens and spawn tasks instead.

- **Confusion**: Thinking Tokio's `select!` and futures-rs `select!` behave identically.
  **Clarification**: In futures-rs, futures must always be fused (enforced by type-checking), there is no `if` guard support, and `default`/`complete` branches replace `else`.

# Source Reference

Chapter 5: "Composing futures concurrently" -- all sections. The introduction, "Join" section (including "Alternatives"), "Race/select" section (including "Alternatives"), and "Final words" are fully written with detailed prose and examples. This card also incorporates outline content from Ch. 6: "Channels, locking, and synchronization" (41 lines, entirely bullet-point outline covering channels, async Mutex, RwLock, Semaphore, and other sync primitives) and Ch. 12: "Async iterators" (52 lines, outline covering stream consumption, combinators, implementing async iterators, and sinks).

# Verification Notes

- Definition source: Direct quotations from Ch. 5 introduction, "Join" section, and "Race/select" section
- Key Properties: All from explicit statements in Ch. 5's fully-written prose
- Confidence rationale: HIGH -- Ch. 5 is the most thoroughly written of all the chapters in scope, with detailed prose, code examples, and nuanced discussion of tradeoffs. The folded-in content from Ch. 6 and Ch. 12 is outline-only and contributes supplementary context, not core claims.
- Uncertainties: Ch. 6 (sync primitives) and Ch. 12 (streams/async iterators) are entirely outlines; their eventual full content may warrant separate cards. The stream-related content in Ch. 5 references a "[streams chapter](streams.md)" that maps to Ch. 12's outline.
- Cross-reference status: `async-await-basics` and `async-programming-overview` are from Agent A's Ch. 1-2 extraction; `cancellation-safety` and `structured-concurrency` exist in async-reference; other slugs are in this extraction set
