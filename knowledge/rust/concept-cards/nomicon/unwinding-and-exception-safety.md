---
concept: Unwinding and Exception Safety
slug: unwinding-and-exception-safety
category: unsafe-rust
subcategory: error-handling
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Unwinding"
chapter_number: 7
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "exception safety"
  - "panic safety"
  - "unwinding"
  - "catch_unwind"
  - "poisoning"
  - "minimal exception safety"
  - "maximal exception safety"
  - "panic in unsafe code"
prerequisites:
  - uninitialized-memory
  - ownership-based-resource-management
extends: []
related:
  - unsafe-concurrency
contrasts_with: []
answers_questions:
  - "What is Rust's error handling hierarchy?"
  - "What happens when a Rust thread panics?"
  - "What is catch_unwind and when should I use it?"
  - "What is exception safety in Rust?"
  - "What is the difference between minimal and maximal exception safety?"
  - "How do I write exception-safe unsafe code?"
  - "What is poisoning and why does Mutex use it?"
  - "Can a panic cross FFI boundaries?"
  - "How do I handle panics in unsafe code that works with uninitialized memory?"
---

# Quick Definition

Rust's panic mechanism unwinds the stack, calling destructors as if every function instantly returned. Unsafe code must be *minimally* exception safe (never violate memory safety on panic); safe code should aim for *maximal* exception safety (program remains correct). The guard pattern -- storing cleanup logic in a struct's destructor -- ensures invariants are restored whether code panics or not. Types that survive panics (like `Mutex`) may choose to *poison* themselves to prevent use of potentially inconsistent state.

# Core Definition

Rust has a tiered error-handling scheme: "If something might reasonably be absent, Option is used. If something goes wrong and can reasonably be handled, Result is used. If something goes wrong and cannot reasonably be handled, the thread panics. If something catastrophic happens, the program aborts." (Ch. 7, Introduction)

"Panics cause the thread to halt normal execution and unwind its stack, calling destructors as if every function instantly returned." The `catch_unwind` API enables catching panics without spawning a thread, but "Rust's current unwinding implementation is heavily optimized for the 'doesn't unwind' case. If a program doesn't unwind, there should be no runtime cost for the program being *ready* to unwind. As a consequence, actually unwinding will be more expensive than in e.g. Java." (Ch. 7, Introduction)

Exception safety has two levels: "In unsafe code, we *must* be exception safe to the point of not violating memory safety. We'll call this *minimal* exception safety. In safe code, it is *good* to be exception safe to the point of your program doing the right thing. We'll call this *maximal* exception safety." (Ch. 7, Exception Safety)

Poisoning provides a runtime safety mechanism: "These types may choose to explicitly *poison* themselves if they witness a panic. Poisoning doesn't entail anything in particular. Generally it just means preventing normal usage from proceeding." The standard library's Mutex is the most notable example. (Ch. 7, Poisoning)

# Prerequisites

- **uninitialized-memory** -- panicking through code with uninitialized memory causes double-frees or leaks
- **ownership-based-resource-management** -- unwinding triggers destructors, connecting directly to OBRM

# Key Properties

1. **Tiered error handling**: Option for absence, Result for recoverable errors, panic for unrecoverable errors, abort for catastrophic failure
2. **Stack unwinding**: Panic unwinds the stack, calling destructors in reverse order as if every function returned immediately
3. **catch_unwind**: Catches panics without spawning a new thread; should be used sparingly because unwinding is expensive compared to the no-unwind case
4. **FFI boundary requirement**: "Rust's unwinding strategy is not specified to be fundamentally compatible with any other language's unwinding." Panics must be caught at FFI boundaries or the result is Undefined Behavior
5. **Minimal exception safety**: Required for all unsafe code -- never violate memory safety on panic
6. **Maximal exception safety**: Desired for safe code -- the program should continue to do the right thing after a panic
7. **Unsafe code with caller code**: Unsafe code that invokes user-provided closures (e.g., Clone::clone, Ord::cmp) must assume those calls can panic
8. **Guard pattern**: Store algorithm state in a separate struct with a destructor that restores invariants, acting as a "finally" block
9. **Poisoning**: Types that survive across panic boundaries (e.g., Mutex) can mark themselves as poisoned; future operations return Err or panic
10. **Mutex poisoning rationale**: Not for memory safety ("it must be minimally exception-safe") but to prevent use of data that "was likely in the middle of being modified, and as such may be in an inconsistent or incomplete state"

# Construction / Recognition

## To Make Unsafe Code Exception-Safe:
1. Identify all points where user-provided or non-trivial code can panic (Clone, Ord comparisons, closures, arithmetic on debug builds)
2. Ensure the program is in a safe (not necessarily consistent) state at every point where a panic could occur
3. Either: run all potentially panicking code before modifying state, or use a guard struct

## To Use the Guard Pattern:
1. Create a struct that holds a mutable reference to the data being modified plus temporary state
2. Implement `Drop` on the guard to restore invariants (write the temporary value back, fix lengths, etc.)
3. Perform the potentially-panicking operations while the guard is alive
4. The guard's destructor runs whether the code panics or completes normally

## To Handle the Vec::push_all Problem:
1. Do NOT set the Vec's length before cloning all elements -- `clone()` can panic
2. Either set the length after the loop (prevents observing uninitialized memory) or update the length each iteration (ensures already-cloned values are dropped)

## To Handle the BinaryHeap::sift_up Problem:
1. Option A: Separate user-defined code (comparisons) from unsafe code (moves) into two phases
2. Option B: Use a `Hole` guard struct that holds the removed element and writes it back in its destructor

# Context & Application

Exception safety is one of the most subtle aspects of unsafe Rust programming. The chapter emphasizes that "unless you are very careful and tightly control what code runs, pretty much everything can unwind, and you need to be ready for it." Even arithmetic can panic on debug builds due to overflow checks.

The two worked examples (Vec::push_all and BinaryHeap::sift_up) demonstrate increasing complexity. Vec::push_all has a simple fix: delay `set_len` until after the loop. BinaryHeap::sift_up requires the more sophisticated guard pattern because the data structure has a "hole" (a logically uninitialized slot) throughout the operation.

The Hole struct is a practical implementation of the guard pattern, functioning as Rust's equivalent of try/finally. The guard holds the removed element and writes it back into the hole in its destructor, ensuring the heap never contains uninitialized memory regardless of panics.

Poisoning is an optional, complementary strategy for types that persist across panic boundaries. It does not prevent memory unsafety (that is guaranteed by minimal exception safety) but prevents logic errors from using data in an inconsistent state. The Mutex exposes a method to access poisoned data for users who are "double-plus-sure" they can handle it.

# Examples

**Example 1** (Ch. 7, Vec::push_all Bug): Setting length before cloning creates an exception safety hole:
```rust
impl<T: Clone> Vec<T> {
    fn push_all(&mut self, to_push: &[T]) {
        self.reserve(to_push.len());
        unsafe {
            let end_ptr = self.as_mut_ptr().add(self.len());
            // BUG: length set too early -- if clone() panics,
            // uninitialized memory will be read on drop
            self.set_len(self.len() + to_push.len());
            for (i, x) in to_push.iter().enumerate() {
                end_ptr.add(i).write(x.clone()); // clone can panic!
            }
        }
    }
}
```
Fix: move `set_len` after the loop, or update it each iteration.

**Example 2** (Ch. 7, Guard Pattern): The Hole struct acts as a "finally" block for BinaryHeap::sift_up:
```rust
struct Hole<'a, T: 'a> {
    data: &'a mut [T],
    elt: Option<T>,
    pos: usize,
}

impl<'a, T> Drop for Hole<'a, T> {
    fn drop(&mut self) {
        unsafe {
            let pos = self.pos;
            ptr::write(&mut self.data[pos], self.elt.take().unwrap());
        }
    }
}
```
The destructor fills the hole whether the comparison panics or not.

**Example 3** (Ch. 7, Poisoning): Mutex poisons itself when a MutexGuard is dropped during a panic:
"Any future attempts to lock the Mutex will return an `Err` or panic." The data may be in an inconsistent state -- e.g., a BinaryHeap that no longer has the heap property. The lock can still be obtained via `into_inner()` for users who can handle potentially inconsistent data.

# Relationships

## Builds Upon
- **uninitialized-memory** -- panicking through uninitialized memory causes UB
- **ownership-based-resource-management** -- unwinding triggers destructors; understanding recursive drop is essential

## Enables
- Writing correct unsafe data structure implementations (Vec, BinaryHeap, etc.)
- Safe FFI wrappers that catch panics at the boundary

## Related
- **unsafe-concurrency** -- Mutex poisoning connects exception safety to concurrent programming

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Setting a collection's length before fully initializing all elements, when the initialization can panic.
  **Correction**: In `Vec::push_all`, `set_len` must come after the loop (or be updated each iteration), not before. "Clone is completely out of our control, and is totally free to panic."

- **Error**: Allowing panics to cross FFI boundaries.
  **Correction**: "You must *absolutely* catch any panics at the FFI boundary!" Unwinding into or from another language is Undefined Behavior. Use `catch_unwind` at FFI entry points.

- **Error**: Assuming unsafe code only needs to handle code it controls.
  **Correction**: "It is not uncommon for Unsafe code to work with arrays of temporarily uninitialized data while repeatedly invoking caller-provided code. Such code needs to be careful and consider exception safety."

# Common Confusions

- **Confusion**: Thinking minimal exception safety means the program state must be fully consistent after a panic.
  **Clarification**: Minimal exception safety only requires memory safety. "We need only guarantee that it's a *safe* state" -- the data may be logically inconsistent but must not cause undefined behavior.

- **Confusion**: Thinking poisoning is about memory safety.
  **Clarification**: "Mutex poisons not for true safety in the sense that Rust normally cares about. It poisons as a safety-guard against blindly using the data." Poisoning prevents logic errors, not UB. The data behind a poisoned Mutex can still be accessed safely.

- **Confusion**: Thinking `catch_unwind` is Rust's equivalent of try/catch for routine error handling.
  **Clarification**: "Don't build your programs to unwind under normal circumstances. Ideally, you should only panic for programming errors or *extreme* problems." The unwinding implementation is optimized for the no-panic case, making actual unwinding expensive.

# Source Reference

Chapter 7: Unwinding -- all sections: Introduction (tiered error handling, stack unwinding, catch_unwind, FFI boundary requirement), Exception Safety (minimal vs maximal, Vec::push_all bug and fix, BinaryHeap::sift_up with Hole guard pattern), Poisoning (Mutex poisoning rationale, safe access to poisoned data).

# Verification Notes

- Definition source: Direct quotations from Ch. 7 Introduction, Exception Safety, and Poisoning sections
- Tiered error handling: Directly quoted from Introduction
- Minimal/maximal exception safety: Directly quoted definitions from Exception Safety
- Vec::push_all: Code and analysis directly from Exception Safety section
- Hole guard pattern: Code directly from BinaryHeap::sift_up subsection
- Poisoning: Directly from Poisoning section with Mutex explanation
- Confidence rationale: HIGH -- the chapter provides clear definitions, detailed code examples, and thorough explanations of each concept
- Uncertainties: None
