---
concept: Ownership-Based Resource Management
slug: ownership-based-resource-management
category: unsafe-rust
subcategory: ownership
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "The Perils Of Ownership Based Resource Management (OBRM)"
chapter_number: 6
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "OBRM"
  - "RAII in Rust"
  - "constructors"
  - "destructors"
  - "Drop trait"
  - "resource leaking"
  - "mem::forget"
  - "leak amplification"
  - "destructor leaks"
prerequisites:
  - uninitialized-memory
extends: []
related:
  - unwinding-and-exception-safety
  - unsafe-concurrency
contrasts_with: []
answers_questions:
  - "How do constructors work in Rust compared to C++?"
  - "How does Rust's Drop trait implement destructors?"
  - "Why does Rust recursively drop struct fields?"
  - "Can you prevent recursive drop in Rust?"
  - "Is mem::forget safe and what are its implications?"
  - "What is leak amplification?"
  - "Why was thread::scoped::JoinGuard removed from std?"
  - "Can unsafe code rely on destructors being called?"
  - "How does Drain handle mem::forget safely?"
  - "What happens if you overflow Rc's reference count?"
---

# Quick Definition

Rust's ownership-based resource management (OBRM/RAII) acquires resources on construction and releases them on destruction. Rust has no built-in constructors beyond struct literal syntax, and the `Drop` trait provides automatic destructors that recursively drop all fields. Critically, safe code can prevent destructors from running (via `mem::forget` or reference cycles), so unsafe code must never rely on destructors for memory safety.

# Core Definition

"Roughly speaking the pattern is as follows: to acquire a resource, you create an object that manages it. To release the resource, you simply destroy the object, and it cleans up the resource for you." The most common resource is memory -- "`Box`, `Rc`, and basically everything in `std::collections` is a convenience to enable correctly managing memory." (Ch. 6, Introduction)

Constructors in Rust are minimal: "There is exactly one way to create an instance of a user-defined type: name it, and initialize all its fields at once." There are no copy, default, assignment, or move constructors as in C++. "Move constructors are meaningless in Rust because we don't enable types to 'care' about their location in memory. Every type must be ready for it to be blindly memcopied to somewhere else in memory." (Ch. 6, Constructors)

Destructors are provided by the `Drop` trait: "After `drop` is run, Rust will recursively try to drop all of the fields of `self`." This recursive behavior applies to all structs and enums regardless of whether they implement Drop. "There is no stable way to prevent this behavior in Rust 1.0." (Ch. 6, Destructors)

On leaking: "It is reasonable for safe code to assume that destructor leaks do not happen, as any program that leaks destructors is probably wrong. However *unsafe* code cannot rely on destructors to be run in order to be safe." `mem::forget` was once marked unsafe but is now safe, because "there are many ways to fail to call a destructor in safe code. The most famous example is creating a cycle of reference-counted pointers using interior mutability." (Ch. 6, Leaking)

# Prerequisites

- **uninitialized-memory** -- OBRM builds on understanding how initialization and deinitialization of memory works, including drop flags

# Key Properties

1. **One True Constructor**: Struct literal syntax is the only way to create a type instance; all other methods (e.g., `new()`) are ordinary functions that bottom out to it
2. **No move constructors**: Types cannot care about their memory location; they can be blindly memcopied, ruling out intrusive data structures in safe Rust
3. **Clone vs Copy**: `Clone` is Rust's moral equivalent of a copy constructor but is never implicit; `Copy` is a special case where the implementation is "just copy the bits"
4. **Default trait**: Rarely used in concrete contexts; types provide a static `new` method by convention instead
5. **Recursive drop**: After `drop(&mut self)` runs, Rust recursively drops all fields; types that contain Drop fields "need Drop" even without implementing it themselves
6. **Option pattern for destructors**: Using `Option<T>` and `.take()` in `drop` is the classic safe solution for moving out of self during destruction
7. **mem::forget is safe**: It consumes a value without running its destructor; reference cycles can also prevent destructors from running
8. **Unsafe code cannot rely on Drop**: Destructor leaks can happen in safe code, so safety invariants must not depend on destructors running
9. **Proxy type danger**: Types like `Drain`, `Rc`, and `JoinGuard` that manage access to distinct objects are most vulnerable to destructor leak bugs
10. **Leak amplification**: When `mem::forget` prevents a destructor from running, the safe response is to leak more (e.g., `Vec::drain` sets len to 0 before iteration)
11. **Rc overflow**: Forgetting enough Rcs can overflow the reference count, causing use-after-free; the standard library aborts in this case

# Construction / Recognition

## To Implement a Custom Destructor:
1. Implement the `Drop` trait with `fn drop(&mut self)`
2. Perform cleanup logic (deallocate memory, close handles, etc.)
3. Rust will automatically drop all fields recursively after your `drop` returns
4. Do not manually drop fields that Rust will drop for you (causes double-free)

## To Move a Field Out of Self During Drop:
1. Wrap the field in `Option<T>`
2. In `drop`, call `self.field.take().unwrap()` to move the value out
3. The `None` left behind prevents recursive drop of the moved-out field
4. Use `mem::forget` on the taken value if you've already cleaned up its resources

## To Design an API That Is Safe Against Destructor Leaks:
1. Do not place safety invariants in destructors -- assume the destructor may not run
2. For proxy types (iterators, guards), set the source to a trivially consistent state before yielding control
3. Example: `Vec::drain` sets the Vec's len to 0 at the start, so forgetting the Drain iterator leaks elements but does not cause use-after-free

# Context & Application

OBRM is central to Rust's design philosophy, but the Rustonomicon reveals its sharp edges. The chapter's title -- "The *Perils* Of Ownership Based Resource Management" -- signals that while OBRM works beautifully in practice, it introduces subtle theoretical problems.

The key insight is that `mem::forget` being safe changes what unsafe code can assume. Before this was settled, APIs like `thread::scoped::JoinGuard` relied on destructors for safety. The JoinGuard API intended to guarantee that parent threads would join child threads before shared data went out of scope, but `mem::forget` could bypass the join, enabling use-after-free. This API was removed from the standard library.

The leak amplification strategy (used by `Vec::drain`) is the pragmatic resolution: design APIs so that forgetting the guard/proxy type causes additional leaks rather than undefined behavior. "Since we've accepted that mem::forget is safe, this is definitely safe."

The Rc overflow case demonstrates an extreme consequence: if `mem::forget` is used to leak enough Rcs, the reference count overflows, eventually reaching 0 with outstanding references. The standard library aborts rather than permitting use-after-free.

# Examples

**Example 1** (Ch. 6, Constructors): Rust's one true constructor is struct literal syntax:
```rust
struct Foo { a: u8, b: u32, c: bool }
let foo = Foo { a: 0, b: 1, c: false };
```
Every other way of creating a Foo calls a function that bottoms out to this.

**Example 2** (Ch. 6, Destructors): A custom Box using Option to safely move out during drop:
```rust
struct SuperBox<T> { my_box: Option<Box<T>> }

impl<T> Drop for SuperBox<T> {
    fn drop(&mut self) {
        unsafe {
            let my_box = self.my_box.take().unwrap();
            let c: NonNull<T> = my_box.ptr.into();
            Global.deallocate(c.cast(), Layout::new::<T>());
            mem::forget(my_box);
        }
    }
}
```

**Example 3** (Ch. 6, Drain Leak): Forgetting a Drain iterator causes use-after-free if the Vec's len is not pre-set to 0:
```rust
let mut vec = vec![Box::new(0); 4];
{
    let mut drainer = vec.drain(..);
    drainer.next();
    drainer.next();
    mem::forget(drainer);
}
// If Vec len wasn't zeroed, vec[0] reads freed memory!
```
The fix: set Vec's len to 0 when starting iteration, restoring it only in the destructor.

**Example 4** (Ch. 6, JoinGuard): The removed `thread::scoped` API relied on destructors for safety:
```rust
let mut data = Box::new(0);
{
    let guard = thread::scoped(|| { *data += 1; });
    mem::forget(guard); // Expires the loan without blocking
}
// Box dropped while scoped thread may still be accessing it
```

# Relationships

## Builds Upon
- **uninitialized-memory** -- drop flags, MaybeUninit, and initialization state are prerequisites for understanding OBRM

## Enables
- **unwinding-and-exception-safety** -- exception safety depends on OBRM and understanding when destructors run
- Safe abstraction over system resources (files, sockets, threads, locks)

## Related
- **unsafe-concurrency** -- Send/Sync interact with OBRM through types like MutexGuard
- **unwinding-and-exception-safety** -- panics trigger destructors, connecting unwinding to OBRM

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Deallocating a field in a custom destructor without preventing recursive drop.
  **Correction**: "After we deallocate the `box`'s ptr in SuperBox's destructor, Rust will happily proceed to tell the box to Drop itself and everything will blow up with use-after-frees and double-frees." Use the Option pattern to take the field before manual cleanup.

- **Error**: Designing unsafe APIs that rely on destructors running for memory safety.
  **Correction**: `mem::forget` is safe, and reference cycles can also prevent destructors. "Unsafe code cannot rely on destructors to be run in order to be safe."

- **Error**: Assuming `Rc`'s reference count cannot overflow.
  **Correction**: Using `mem::forget` repeatedly on `Rc` clones can overflow the reference count to 0, causing use-after-free. The standard library aborts in this case.

# Common Confusions

- **Confusion**: Thinking Rust has special constructor mechanisms like C++.
  **Clarification**: "Unlike C++, Rust does not come with a slew of built-in kinds of constructor." There are no copy, default, assignment, or move constructors. The `new()` convention is an ordinary associated function with no special language meaning.

- **Confusion**: Thinking `mem::forget` is unsafe or should never be used.
  **Clarification**: `mem::forget` was once marked unsafe as a lint, but "this was generally determined to be an untenable stance to take: there are many ways to fail to call a destructor in safe code." It is now safe.

- **Confusion**: Believing OBRM eliminates all resource leaks.
  **Clarification**: "Many people like to believe that Rust eliminates resource leaks. In practice, this is basically true." But theoretically, infinite loops, `mem::forget`, and reference cycles can all prevent destructors from running.

# Source Reference

Chapter 6: The Perils Of Ownership Based Resource Management (OBRM) -- all sections: Introduction (RAII pattern), Constructors (One True Constructor, no move constructors, Copy/Clone, Default, `new` convention), Destructors (Drop trait, recursive drop, Option pattern), Leaking (mem::forget safety, proxy types, Drain and leak amplification, Rc overflow, thread::scoped::JoinGuard removal).

# Verification Notes

- Definition source: Direct quotations from Ch. 6 Introduction, Constructors, Destructors, and Leaking sections
- Constructor philosophy: Directly from Constructors section including C++ comparison
- Recursive drop: Directly from Destructors section with SuperBox example
- mem::forget safety: Directly from Leaking section with rationale
- Leak amplification: Directly from Drain subsection
- JoinGuard: Directly from thread::scoped::JoinGuard subsection with note about removal from std
- Confidence rationale: HIGH -- the chapter provides detailed code examples and thorough explanations of each concept
- Uncertainties: None
