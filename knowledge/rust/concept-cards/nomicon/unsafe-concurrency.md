---
concept: Unsafe Concurrency
slug: unsafe-concurrency
category: unsafe-rust
subcategory: concurrency
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Concurrency and Parallelism"
chapter_number: 8
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Send and Sync"
  - "data races"
  - "race conditions"
  - "atomics"
  - "memory ordering"
  - "SeqCst"
  - "Acquire-Release"
  - "Relaxed ordering"
  - "C++ memory model"
  - "compiler reordering"
  - "hardware reordering"
prerequisites:
  - uninitialized-memory
  - ownership-based-resource-management
extends: []
related:
  - unwinding-and-exception-safety
contrasts_with: []
answers_questions:
  - "What is the difference between a data race and a race condition in Rust?"
  - "What are the Send and Sync traits?"
  - "Why are raw pointers neither Send nor Sync?"
  - "How do I implement Send and Sync for custom types?"
  - "What memory model does Rust use for atomics?"
  - "What is the difference between SeqCst, Acquire/Release, and Relaxed orderings?"
  - "What is compiler reordering and why does it matter for concurrency?"
  - "What is hardware reordering?"
  - "Why is Rc not Send or Sync?"
  - "When can a race condition violate memory safety?"
  - "What is a spinlock in Rust using atomics?"
---

# Quick Definition

Safe Rust guarantees the absence of *data races* (concurrent unsynchronized access where at least one is a write) but does not prevent general *race conditions*. The `Send` and `Sync` marker traits control which types can cross thread boundaries. Rust inherits C++20's atomics memory model, providing SeqCst, Acquire-Release, and Relaxed orderings to bridge the gap between program semantics, compiler optimizations, and hardware memory hierarchies.

# Core Definition

"Safe Rust guarantees an absence of data races, which are defined as: two or more threads concurrently accessing a location of memory; one or more of them is a write; one or more of them is unsynchronized." Data races cause Undefined Behavior and are prevented "mostly through Rust's ownership system alone: it's impossible to alias a mutable reference, so it's impossible to perform a data race." (Ch. 8, Data Races and Race Conditions)

"**However Rust does not prevent general race conditions.** This is mathematically impossible in situations where you do not control the scheduler." Race conditions alone cannot violate memory safety -- "only in conjunction with some other unsafe code can a race condition actually violate memory safety." (Ch. 8, Data Races and Race Conditions)

Send and Sync are the foundation of Rust's concurrency model: "A type is Send if it is safe to send it to another thread. A type is Sync if it is safe to share between threads (T is Sync if and only if `&T` is Send)." They are unsafe traits, automatically derived when all constituent types are Send/Sync, and incorrectly implementing them "can cause Undefined Behavior." (Ch. 8, Send and Sync)

For atomics, "Rust pretty blatantly just inherits the memory model for atomics from C++20. This is not due to this model being particularly excellent or easy to understand. Indeed, this model is quite complex and known to have several flaws. Rather, it is a pragmatic concession to the fact that *everyone* is pretty bad at modeling atomics." (Ch. 8, Atomics)

# Prerequisites

- **uninitialized-memory** -- understanding memory safety fundamentals
- **ownership-based-resource-management** -- Send/Sync interact with OBRM through guard types (MutexGuard is not Send)

# Key Properties

1. **Data race definition**: Concurrent access + at least one write + unsynchronized = Undefined Behavior; impossible in Safe Rust
2. **Race conditions are safe**: Deadlocks and logic errors from incorrect synchronization do not violate memory safety alone
3. **Race conditions + unsafe = danger**: A race condition can violate memory safety when combined with unsafe code (e.g., bounds-checking with an atomic then using `get_unchecked` with a stale value)
4. **Send**: Safe to transfer ownership to another thread; auto-derived when all fields are Send
5. **Sync**: Safe to share via `&T` between threads; T is Sync iff `&T` is Send; auto-derived when all fields are Sync
6. **Unsafe traits**: Send and Sync are unsafe to implement manually; other unsafe code may assume correct implementations
7. **Major non-Send/Sync types**: Raw pointers (lint), `UnsafeCell` (not Sync), `Rc` (neither -- unsynchronized refcount)
8. **Raw pointers as lint**: Raw pointers are marked non-Send/Sync not because dereferencing them is unsafe anyway, but to prevent types containing them from being automatically derived as thread-safe
9. **Negative impls**: Types can opt out of auto-derived Send/Sync using `impl !Send` / `impl !Sync` (requires `negative_impls` feature)
10. **MutexGuard is not Send**: The underlying library requires locks to be freed on the thread that acquired them; sending a MutexGuard to another thread would violate this
11. **C++20 memory model**: Rust's atomics inherit the C/C++ model; defined in terms of causality graphs and happens-before relationships
12. **Compiler reordering**: Compilers may eliminate dead stores and reorder independent operations; multi-threaded code may depend on ordering the compiler removes
13. **Hardware reordering**: CPUs with memory hierarchies may propagate writes to other threads in different orders; strongly-ordered (x86/64) vs weakly-ordered (ARM) platforms differ in default guarantees
14. **SeqCst**: Strongest ordering; all threads agree on a single global execution order; involves memory fences even on strongly-ordered platforms
15. **Acquire-Release**: Paired orderings for critical sections; release ensures all prior writes are visible to a subsequent acquire on the same location; no causality established across different locations or with uninvolved threads
16. **Relaxed**: Weakest ordering; operations are still atomic but can be freely reordered and establish no happens-before relationships; suitable for counters that don't synchronize other accesses
17. **No consume ordering**: Rust explicitly does not expose C++'s consume ordering

# Construction / Recognition

## To Implement Send and Sync for a Custom Type:
1. Verify the type's safety invariants hold when transferred to (Send) or shared across (Sync) threads
2. Add `unsafe impl<T> Send for MyType<T> where T: Send {}` if the type can be safely sent when its contents can be
3. Add `unsafe impl<T> Sync for MyType<T> where T: Sync {}` if shared references are safe when contents are Sync
4. Consider whether the type's destructor can safely run on a different thread than where it was created (relevant for Send)
5. When wrapping raw pointers, the encapsulating type should implement Send/Sync with appropriate bounds if the abstraction is thread-safe

## To Use Acquire-Release for a Spinlock:
1. Use an `AtomicBool` as the lock state
2. Acquire: loop with `compare_exchange(false, true, Ordering::Acquire, Ordering::Relaxed)`
3. Perform data accesses within the critical section
4. Release: `lock.store(false, Ordering::Release)`
5. The Acquire ensures all subsequent reads see data written before the Release on the locking thread

## To Choose an Atomic Ordering:
1. Start with `SeqCst` -- it is the safest default and "mechanically trivial to downgrade" later
2. Use Acquire-Release when protecting a critical section or establishing causality between a specific producer and consumer on the same memory location
3. Use Relaxed only for truly independent operations (e.g., a shared counter where you don't care about ordering relative to other data)
4. Test on weakly-ordered hardware (ARM) -- bugs may be hidden on strongly-ordered platforms (x86/64)

# Context & Application

The chapter establishes that Rust's concurrency safety comes from the type system (ownership + Send/Sync), not from runtime mechanisms. The language itself is agnostic about concurrency paradigms -- "message passing, green threads, and async APIs are all diverse enough that any abstraction over them tends to involve trade-offs." This design allows libraries to implement their own concurrency models.

The distinction between data races and race conditions is fundamental. Safe Rust eliminates data races (which are UB) but permits race conditions (which are logic errors). The key insight is that race conditions become dangerous only when combined with unsafe code -- the example of checking an atomic index against a Vec's length and then using `get_unchecked` with a re-loaded (potentially changed) value demonstrates exactly how this happens.

The atomics section is deliberately terse, acknowledging that "trying to fully explain the model in this book is fairly hopeless." The practical guidance is to start with SeqCst and downgrade only when you can prove correctness. The Acquire-Release spinlock example demonstrates the most common use case.

The Carton example (a simplified Box implementation) illustrates how to reason about Send and Sync for types that use raw pointers internally. The key insight is that standard library collections like Vec use raw pointers pervasively but are still Send and Sync because "they largely behave like an `&` or `&mut` into the collection."

# Examples

**Example 1** (Ch. 8, Race Condition + Unsafe): A race condition violating memory safety:
```rust
let data = vec![1, 2, 3, 4];
let idx = Arc::new(AtomicUsize::new(0));
let other_idx = idx.clone();
thread::spawn(move || {
    other_idx.fetch_add(10, Ordering::SeqCst);
});
if idx.load(Ordering::SeqCst) < data.len() {
    unsafe {
        // DANGEROUS: idx may have changed between the check and this load
        println!("{}", data.get_unchecked(idx.load(Ordering::SeqCst)));
    }
}
```

**Example 2** (Ch. 8, Implementing Send/Sync): A Carton type (simplified Box) with manual Send/Sync:
```rust
struct Carton<T>(ptr::NonNull<T>);

// Safety: No one besides us has the raw pointer, so we can safely
// transfer the Carton to another thread if T can be safely transferred.
unsafe impl<T> Send for Carton<T> where T: Send {}

// Safety: Carton does not use interior mutability; all mutations
// require &mut. It suffices that T be Sync for Carton<T> to be Sync.
unsafe impl<T> Sync for Carton<T> where T: Sync {}
```

**Example 3** (Ch. 8, Spinlock): Acquire-Release ordering for a basic spinlock:
```rust
let lock = Arc::new(AtomicBool::new(false));
// Acquire the lock
while lock.compare_exchange(false, true, Ordering::Acquire, Ordering::Relaxed).is_err() { }
// ... critical section ...
// Release the lock
lock.store(false, Ordering::Release);
```

**Example 4** (Ch. 8, Negative Impls): Opting out of auto-derived thread safety:
```rust
#![feature(negative_impls)]
struct SpecialThreadToken(u8);
impl !Send for SpecialThreadToken {}
impl !Sync for SpecialThreadToken {}
```

# Relationships

## Builds Upon
- Ownership and borrowing (data race prevention through aliasing rules)
- **ownership-based-resource-management** -- MutexGuard's Send restriction is tied to destructor behavior

## Enables
- Writing custom concurrent data structures with correct synchronization
- Implementing thread-safe wrappers around raw pointer-based types
- Building custom concurrency paradigms as libraries

## Related
- **unwinding-and-exception-safety** -- Mutex poisoning connects panics to concurrent state
- **uninitialized-memory** -- concurrent initialization requires synchronization beyond what MaybeUninit provides

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `get_unchecked` after a bounds check with an atomic that another thread could have modified.
  **Correction**: Load the atomic value once, store it locally, bounds-check the local copy, and use the same local copy for the access. Never re-load an atomic between a safety check and an unsafe operation.

- **Error**: Implementing Send or Sync for a type that contains unsynchronized shared mutable state.
  **Correction**: "Incorrectly implementing Send or Sync can cause Undefined Behavior." Only implement these traits when you can prove the type's invariants hold across thread boundaries.

- **Error**: Assuming Relaxed ordering establishes happens-before relationships with other data.
  **Correction**: "Relaxed operations are still atomic. That is, they don't count as data accesses and any read-modify-write operations done to them occur atomically." But they provide no ordering guarantees relative to other memory operations.

- **Error**: Testing concurrent code only on x86/64 and assuming correctness.
  **Correction**: "Asking for guarantees that are too weak on strongly-ordered hardware is more likely to *happen* to work, even though your program is strictly incorrect." Test on weakly-ordered hardware (ARM) when possible.

# Common Confusions

- **Confusion**: Thinking Safe Rust prevents all concurrency bugs.
  **Clarification**: Safe Rust prevents data races (Undefined Behavior) but not race conditions (logic errors). "It is considered 'safe' for Rust to get deadlocked or do something nonsensical with incorrect synchronization."

- **Confusion**: Thinking raw pointers are marked non-Send/Sync because they are inherently dangerous to use across threads.
  **Clarification**: Raw pointers are marked non-Send/Sync primarily as "more of a *lint*" to prevent types containing them from being automatically derived as thread-safe. "Doing anything useful with a raw pointer requires dereferencing it, which is already unsafe."

- **Confusion**: Thinking SeqCst is always necessary for correct concurrent code.
  **Clarification**: "In practice, sequential consistency is rarely necessary for program correctness." But it is the right default when you are not confident about weaker orderings. "Having your program run a bit slower than it needs to is certainly better than it running incorrectly!"

- **Confusion**: Thinking Acquire-Release establishes causality between all threads.
  **Clarification**: "No causality is established with any other threads. Similarly, no causality is established if A and B access *different* locations in memory." Acquire-Release only creates happens-before between a specific release and a subsequent acquire on the *same* location.

# Source Reference

Chapter 8: Concurrency and Parallelism -- all sections: Introduction (Rust's concurrency philosophy), Data Races and Race Conditions (definitions, data race vs race condition, unsafe interaction examples), Send and Sync (trait definitions, auto-derivation, major exceptions, raw pointers as lint, negative impls, Carton example, MutexGuard not Send), Atomics (C++20 memory model, compiler reordering, hardware reordering, data accesses vs atomic accesses, SeqCst, Acquire-Release with spinlock example, Relaxed, no consume ordering).

# Verification Notes

- Definition source: Direct quotations from Ch. 8 on data races, Send/Sync, and atomics
- Data race definition: Directly quoted three-part definition from Data Races section
- Send/Sync: Directly quoted definitions and major exceptions from Send and Sync section
- Carton example: Code directly from Send and Sync section with safety comments
- Atomics model: Directly from Atomics section including C++20 inheritance rationale
- Spinlock: Code directly from Acquire-Release subsection
- Hardware reordering: x86/64 vs ARM distinction directly from Hardware Reordering subsection
- Confidence rationale: HIGH -- the chapter provides clear definitions, concrete code examples, and explicit safety reasoning
- Uncertainties: The chapter contains TODO notes about negative vs positive reasoning and additional Send/Sync explanation, indicating the source itself considers the treatment incomplete in those areas
