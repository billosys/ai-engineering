---
concept: "Implementing Vec: Layout, Allocation, and Core Operations"
slug: implementing-vec-fundamentals
category: unsafe-rust
subcategory: data-structure-implementation
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "09-implementing-vec"
chapter_number: 9
pdf_page: null
section: "Layout, Allocating Memory, Push and Pop, Deallocating, Deref, Insert and Remove"
extraction_confidence: high
aliases:
  - "Vec implementation"
  - "raw allocator Vec"
  - "NonNull Vec layout"
  - "ptr::write and ptr::read"
  - "custom Vec from scratch"
prerequisites:
  - contain-unsafety
extends: []
related:
  - implementing-vec-iterators-zst
  - implementing-arc
  - perf-heap-allocations
contrasts_with: []
answers_questions:
  - "How do I implement Vec from scratch in Rust?"
  - "Why does Vec use NonNull instead of *mut T?"
  - "How does Vec handle memory allocation and growth?"
  - "Why does an empty Vec not allocate?"
  - "How do push and pop use ptr::write and ptr::read?"
  - "Why must allocations be limited to isize::MAX bytes?"
  - "How does Deref make Vec behave like a slice?"
  - "How do insert and remove use ptr::copy (memmove)?"
---

# Quick Definition

Implementing `Vec<T>` from scratch demonstrates core unsafe Rust patterns: using `NonNull<T>` for correct variance and null-pointer optimization, the global allocator API (`alloc`/`realloc`/`dealloc` with `Layout`), `ptr::write`/`ptr::read` for moving values without evaluating uninitialized memory, and `Deref<Target=[T]>` to inherit all slice functionality. The struct is `(NonNull<T>, cap, len)` with `NonNull::dangling()` as the sentinel for zero-capacity state.

# Core Definition

A Vec has three parts: "a pointer to the allocation, the size of the allocation, and the number of elements that have been initialized." (Ch. 9, Layout) Using a raw `*mut T` "would be too strict" because "the compiler will give us too strict variance. So a `&Vec<&'static str>` couldn't be used where a `&Vec<&'a str>` was expected." (Ch. 9, Layout) The solution is `NonNull<T>`, which provides covariance over T and a non-null guarantee enabling null-pointer optimization on `Option<Vec<T>>`. Manual `unsafe impl Send/Sync` is required since `NonNull` does not auto-implement them.

For allocation, "creating an empty Vec doesn't actually allocate at all" -- the pointer is set to `NonNull::dangling()` and `cap == 0` serves as the sentinel for "no allocation." Growth follows a doubling strategy (0 -> 1 -> 2 -> 4 -> ...) using `alloc::alloc` for initial allocation and `alloc::realloc` for growth, with `alloc::handle_alloc_error` to abort on OOM. All allocations are limited to `isize::MAX` bytes because `ptr::offset` uses LLVM's GEP inbounds, which takes a signed integer.

# Prerequisites

- **contain-unsafety** -- The Vec implementation is the canonical example of containing unsafe code behind a safe API, requiring understanding of soundness invariants and safe wrapper design

# Key Properties

1. **Layout**: `NonNull<T>` + `cap: usize` + `len: usize`; `NonNull` provides covariance and non-null guarantee; manual `Send`/`Sync` impls required
2. **Empty Vec**: Uses `NonNull::dangling()` as pointer, `cap == 0` as sentinel; no actual allocation occurs; `dangling()` provides a properly aligned non-null pointer
3. **Growth strategy**: If `cap == 0`, allocate for 1 element; otherwise double capacity; uses `Layout::array::<T>(new_cap)` to compute allocation layout
4. **Allocation limit**: All allocations must not exceed `isize::MAX` bytes due to `ptr::offset` semantics (LLVM GEP inbounds takes signed integer)
5. **Push**: Uses `ptr::write` to blindly overwrite the target address -- "No evaluation involved"; cannot use indexing because that would evaluate (and try to drop) possibly uninitialized memory
6. **Pop**: Uses `ptr::read` to copy out the bits and interpret them as T, leaving memory "logically uninitialized, even though there is in fact a perfectly good instance of T there"
7. **Drop**: Calls `pop` until empty to drop elements, then deallocates with `alloc::dealloc`; must not dealloc when `cap == 0`
8. **Deref**: `Deref<Target=[T]>` via `slice::from_raw_parts` gives Vec all slice functionality (len, first, last, indexing, sorting, iter, iter_mut)
9. **Insert**: Uses `ptr::copy` (C's `memmove`) to shift `[i..len]` to `[i+1..len+1]`, then `ptr::write` at index
10. **Remove**: Uses `ptr::read` at index, then `ptr::copy` to shift `[i+1..len]` to `[i..len-1]`
11. **OOM handling**: Uses `alloc::handle_alloc_error` which aborts rather than panics, because "unwinding can cause allocations to happen"

# Construction / Recognition

## To Implement Vec Layout:
1. Use `NonNull<T>` (not `*mut T`) for the pointer field to get correct covariance and null-pointer optimization
2. Add `cap: usize` and `len: usize` fields
3. Implement `unsafe impl<T: Send> Send for Vec<T> {}` and `unsafe impl<T: Sync> Sync for Vec<T> {}`
4. Initialize with `NonNull::dangling()`, `cap: 0`, `len: 0`

## To Implement Allocation Growth:
1. Check if `cap == 0` -- if so, allocate for 1 element with `alloc::alloc`
2. Otherwise, double capacity and use `alloc::realloc` with the old layout
3. Use `Layout::array::<T>(new_cap)` to compute layouts
4. Assert `new_layout.size() <= isize::MAX` to guard against GEP overflow
5. On null return from allocator, call `alloc::handle_alloc_error`

## To Implement Push/Pop Safely:
1. Push: grow if `len == cap`, then `ptr::write(ptr.add(len), elem)`, then increment len
2. Pop: if `len == 0` return None, else decrement len and `ptr::read(ptr.add(len))`
3. Never index into the allocation directly -- this evaluates memory and triggers drops

# Context & Application

This is the first half of a complete Vec implementation walkthrough in The Rustonomicon. It establishes the foundational patterns for unsafe data structure implementation: using `NonNull` for proper type-system integration, the raw allocator API for manual memory management, and `ptr::write`/`ptr::read` for bypassing Rust's move semantics on raw memory.

The choice of `NonNull::dangling()` for empty Vecs is a recurring pattern: "we already have `cap == 0` as our sentinel for no allocation. We don't even need to handle it specially in almost any code because we usually need to check if `cap > len` or `len > 0` anyway." This avoids the undefined behavior of allocating zero-sized blocks through the global allocator.

The GEP inbounds constraint (limiting allocations to `isize::MAX` bytes) is a consequence of how LLVM reasons about pointer offsets for alias analysis. It is "super important to an optimizing compiler to be able to reason about data dependencies and aliasing."

The `Deref<Target=[T]>` implementation is a key design insight: rather than implementing all slice operations manually, Vec derives them automatically by coercing to a slice reference.

# Examples

**Example 1** (Ch. 9, Layout): Vec layout using NonNull for correct variance:
```rust
use std::ptr::NonNull;
pub struct Vec<T> {
    ptr: NonNull<T>,
    cap: usize,
    len: usize,
}
unsafe impl<T: Send> Send for Vec<T> {}
unsafe impl<T: Sync> Sync for Vec<T> {}
```

**Example 2** (Ch. 9, Push): Writing to uninitialized memory with ptr::write:
```rust
pub fn push(&mut self, elem: T) {
    if self.len == self.cap { self.grow(); }
    unsafe { ptr::write(self.ptr.as_ptr().add(self.len), elem); }
    self.len += 1;
}
```

**Example 3** (Ch. 9, Pop): Reading from initialized memory without evaluation:
```rust
pub fn pop(&mut self) -> Option<T> {
    if self.len == 0 { None }
    else {
        self.len -= 1;
        unsafe { Some(ptr::read(self.ptr.as_ptr().add(self.len))) }
    }
}
```

**Example 4** (Ch. 9, Insert): Shifting elements with ptr::copy (memmove):
```rust
pub fn insert(&mut self, index: usize, elem: T) {
    assert!(index <= self.len, "index out of bounds");
    if self.len == self.cap { self.grow(); }
    unsafe {
        ptr::copy(self.ptr.as_ptr().add(index),
                  self.ptr.as_ptr().add(index + 1),
                  self.len - index);
        ptr::write(self.ptr.as_ptr().add(index), elem);
    }
    self.len += 1;
}
```

# Relationships

## Builds Upon
- Rust's `unsafe` system, raw pointer operations (`ptr::write`, `ptr::read`, `ptr::copy`)
- The global allocator API (`std::alloc`)
- `NonNull<T>` wrapper for variance and null-pointer optimization
- `Deref`/`DerefMut` traits for automatic coercion

## Enables
- **implementing-vec-iterators-zst** -- IntoIter, Drain, RawVec, and ZST handling build on this foundation

## Related
- **implementing-arc** -- uses the same `NonNull`/`PhantomData` layout patterns for a different data structure
- **perf-heap-allocations** -- understanding Vec internals (growth strategy, capacity) is essential for allocation optimization
- **contain-unsafety** -- Vec is the canonical example of containing unsafety behind a safe API

## Contrasts With
- Using `*mut T` directly (loses variance, null-pointer optimization)
- Using `Box` or other safe abstractions (do not allow custom growth/layout strategies)

# Common Errors

- **Error**: Using `*mut T` instead of `NonNull<T>` for the pointer field.
  **Correction**: `*mut T` is invariant over T, so `&Vec<&'static str>` cannot be used where `&Vec<&'a str>` is expected. `NonNull<T>` is covariant and enables null-pointer optimization on `Option<Vec<T>>`.

- **Error**: Indexing into the allocation (`buf[idx] = x`) instead of using `ptr::write`.
  **Correction**: Indexing evaluates the memory as a valid T and calls `drop` on the old value. For uninitialized memory, use `ptr::write` which "just blindly overwrites the target address with the bits of the value."

- **Error**: Calling `alloc::dealloc` when `cap == 0`.
  **Correction**: When cap is 0, no allocation was made; the pointer is `NonNull::dangling()`. Deallocating it is undefined behavior.

- **Error**: Panicking on OOM instead of aborting.
  **Correction**: "Unwinding can cause allocations to happen, and that seems like a bad thing to do when your allocator just came back with 'hey I don't have any more memory'." Use `alloc::handle_alloc_error` to abort.

# Common Confusions

- **Confusion**: Thinking `NonNull::dangling()` is the same as a null pointer.
  **Clarification**: `dangling()` returns a well-aligned non-null pointer (specifically `mem::align_of::<T>()` cast to a pointer). It is valid as a placeholder because `cap == 0` prevents any actual access through it.

- **Confusion**: Thinking `ptr::read` destroys the source value.
  **Clarification**: `ptr::read` copies out the bits and interprets them as T. The source memory is left physically unchanged but is now "logically uninitialized" -- the caller must ensure no second read or drop occurs.

- **Confusion**: Thinking the `isize::MAX` allocation limit is a Rust limitation.
  **Clarification**: It is an LLVM constraint. `ptr::offset` maps to LLVM's GEP inbounds instruction, which takes a signed integer. Unsigned indices greater than `isize::MAX` would overflow GEP and "actually go in the wrong direction."

# Source Reference

Chapter 9: Example: Implementing Vec -- sections: Layout (NonNull, variance, Send/Sync), Allocating Memory (grow strategy, GEP inbounds, isize::MAX, OOM), Push and Pop (ptr::write, ptr::read), Deallocating (Drop impl), Deref (slice::from_raw_parts), Insert and Remove (ptr::copy / memmove).

# Verification Notes

- Definition source: Direct quotations from Ch. 9 Layout and Allocating Memory sections
- Key Properties: Derived from code examples and explanatory text
- Confidence rationale: HIGH -- the source is a complete implementation walkthrough with detailed code and explanation at each step
- Uncertainties: None
- Cross-reference status: `implementing-vec-iterators-zst` is in this extraction set; `implementing-arc` is in this extraction set
