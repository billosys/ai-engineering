---
concept: "Implementing Vec: IntoIter, Drain, RawVec, and Zero-Sized Types"
slug: implementing-vec-iterators-zst
category: unsafe-rust
subcategory: data-structure-implementation
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "09-implementing-vec"
chapter_number: 9
pdf_page: null
section: "IntoIter, RawVec, Drain, Handling Zero-Sized Types"
extraction_confidence: high
aliases:
  - "Vec IntoIter implementation"
  - "RawVec abstraction"
  - "Vec Drain implementation"
  - "zero-sized types in collections"
  - "ZST Vec handling"
  - "RawValIter"
prerequisites:
  - implementing-vec-fundamentals
extends:
  - implementing-vec-fundamentals
related:
  - implementing-arc
contrasts_with: []
answers_questions:
  - "How does IntoIter consume a Vec by value?"
  - "How do you implement a double-ended iterator over raw memory?"
  - "What is RawVec and why extract it from Vec?"
  - "How does Drain borrow a Vec while iterating its elements by value?"
  - "Why are zero-sized types special in unsafe collection code?"
  - "How do you iterate zero-sized types with raw pointers?"
  - "Why must ZST pointers be treated as counters, not real pointers?"
  - "What is ManuallyDrop and when do you use it with iterators?"
---

# Quick Definition

The second half of the Vec implementation covers consuming iterators (IntoIter, Drain), the RawVec abstraction for shared allocation logic, and the special handling required for zero-sized types (ZSTs). IntoIter uses a two-pointer (start/end) C-style iteration idiom with `ptr::read`. RawVec extracts the `(ptr, cap)` pair with allocation/growth/deallocation logic, shared between Vec and IntoIter. ZSTs require three specific guards: never allocating, setting capacity to `usize::MAX`, and using pointer-as-integer arithmetic for iteration since pointer offsets are no-ops for zero-sized types.

# Core Definition

IntoIter "consumes the Vec by-value, and can consequently yield its elements by-value" using two pointers: "one that points to the start of the array, and one that points to one-element past the end. When we want an element from one end, we'll read out the value pointed to at that end and move the pointer over by one. When the two pointers are equal, we know we're done." (Ch. 9, IntoIter) It must take ownership of the Vec's allocation to free it on drop.

RawVec exists because "we've duplicated the logic for specifying a buffer and freeing its memory in Vec and IntoIter" -- it abstracts the `(ptr, cap)` pair with allocation, growth, and deallocation logic. (Ch. 9, RawVec) Drain "is largely the same as IntoIter, except that instead of consuming the Vec, it borrows the Vec and leaves its allocation untouched." (Ch. 9, Drain) A further `RawValIter` abstraction factors out the two-pointer iteration logic shared between IntoIter and Drain.

For zero-sized types: "The raw allocator API has undefined behavior if you pass in 0 for an allocation size" and "raw pointer offsets are no-ops for zero-sized types, which will break our C-style pointer iterator." (Ch. 9, Handling Zero-Sized Types) ZSTs set `cap = usize::MAX` and use integer arithmetic on cast pointers to simulate iteration.

# Prerequisites

- **implementing-vec-fundamentals** -- Requires understanding of the Vec layout, allocation strategy, and ptr::write/ptr::read patterns established in the first half

# Key Properties

1. **IntoIter struct**: Holds `buf: NonNull<T>`, `cap: usize` (for deallocation), `start: *const T`, `end: *const T`; uses `ManuallyDrop` (or `mem::forget`) on the source Vec to prevent double-free
2. **Two-pointer iteration**: `next()` reads from `start` and advances it forward; `next_back()` retreats `end` and reads from it; order differs because `end` always points past the element it wants to read next
3. **IntoIter Drop**: Drains remaining elements (via `for _ in &mut *self {}`), then deallocates the buffer
4. **RawVec**: Struct of `(NonNull<T>, cap)` with `new()`, `grow()`, and `Drop` -- extracts allocation logic shared by Vec and IntoIter
5. **Simplified Vec with RawVec**: Vec becomes `(RawVec<T>, len)`, Drop only pops elements (deallocation handled by RawVec's Drop)
6. **Simplified IntoIter with RawVec**: Holds `_buf: RawVec<T>` (just needs it to live for deallocation) plus iteration pointers; Drop only drains elements
7. **RawValIter**: Factors out the `(start, end)` pointer iteration from IntoIter and Drain into a shared internal iterator
8. **Drain**: Uses `PhantomData<&'a mut Vec<T>>` for lifetime binding; borrows Vec semantically but iterates elements by value; sets `vec.len = 0` on creation as a mem::forget safety measure
9. **ZST allocation**: Sets `cap = usize::MAX` (never allocates); `NonNull::dangling()` serves as both "unallocated" and "zero-sized allocation"; `grow()` asserts `size_of::<T>() != 0`
10. **ZST iteration**: Pointer offsets are no-ops for ZSTs, so pointers are cast to `usize`, incremented/decremented by 1, and cast back; `ptr::read` uses `NonNull::dangling()` instead of the counter-pointer to maintain alignment
11. **ZST deallocation**: Drop must check `self.cap != 0 && elem_size != 0` -- never deallocate for ZSTs since nothing was allocated

# Construction / Recognition

## To Implement IntoIter:
1. Create struct with allocation info (buf, cap) and iteration pointers (start, end)
2. In `into_iter`, wrap the Vec in `ManuallyDrop` to prevent its Drop from running
3. Set `start = ptr.as_ptr()` and `end = ptr.as_ptr().add(len)` (but if `cap == 0`, set `end = start`)
4. Implement `Iterator::next` with `ptr::read(start)` then advance start
5. Implement `DoubleEndedIterator::next_back` by retreating end then `ptr::read(end)`
6. In Drop, drain remaining elements, then deallocate buffer

## To Extract RawVec:
1. Move `(NonNull<T>, cap)` plus `new()`, `grow()`, and `Drop` into a separate struct
2. Replace Vec's fields with `(RawVec<T>, len)` -- add helper methods `ptr()` and `cap()`
3. Vec's Drop now only pops elements; RawVec's Drop handles deallocation
4. IntoIter holds `_buf: RawVec<T>` (kept alive for deallocation) plus `RawValIter<T>`

## To Handle Zero-Sized Types:
1. In `RawVec::new`: if `size_of::<T>() == 0`, set `cap = usize::MAX`
2. In `RawVec::grow`: assert `size_of::<T>() != 0` -- ZSTs should never need growth
3. In `RawVec::drop`: check `self.cap != 0 && elem_size != 0` before deallocating
4. In `RawValIter::new`: for ZSTs, compute `end` as `(start as usize + len) as *const _`
5. In iteration: advance pointers via integer arithmetic, read from `NonNull::dangling()` not the counter-pointer

# Context & Application

The Vec implementation chapter demonstrates progressive refactoring driven by actual code duplication. The initial IntoIter duplicated allocation management from Vec, motivating the extraction of RawVec. Similarly, Drain duplicated iteration logic from IntoIter, motivating the extraction of RawValIter. This incremental approach mirrors real-world unsafe code development.

The Drain type introduces an important mem::forget safety consideration: setting `self.len = 0` on creation means that if the Drain is forgotten (via `mem::forget`), "we just leak the whole Vec's contents" rather than causing a use-after-free. This defensive approach is part of the broader "leaking is safe" philosophy.

The ZST handling reveals subtle pitfalls in unsafe code. The initial ZST iteration code had a "bug" that went unnoticed for years: "abusing the iterator pointers to be counters makes them unaligned! Our one job when using ZSTs is to keep pointers aligned!" The fix is to read from `NonNull::dangling()` instead of the counter-pointer when calling `ptr::read`, since `ptr::read` is a no-op for ZSTs anyway.

# Examples

**Example 1** (Ch. 9, IntoIter): Two-pointer iteration consuming elements by value:
```rust
impl<T> Iterator for IntoIter<T> {
    type Item = T;
    fn next(&mut self) -> Option<T> {
        if self.start == self.end { None }
        else { unsafe {
            let result = ptr::read(self.start);
            self.start = self.start.offset(1);
            Some(result)
        }}
    }
}
```

**Example 2** (Ch. 9, RawVec): Extracted allocation abstraction simplifying Vec:
```rust
pub struct Vec<T> {
    buf: RawVec<T>,
    len: usize,
}
impl<T> Drop for Vec<T> {
    fn drop(&mut self) {
        while let Some(_) = self.pop() {}
        // deallocation is handled by RawVec
    }
}
```

**Example 3** (Ch. 9, ZST iteration): Using integer arithmetic for ZST pointer advancement:
```rust
fn next(&mut self) -> Option<T> {
    if self.start == self.end { None }
    else { unsafe {
        if mem::size_of::<T>() == 0 {
            self.start = (self.start as usize + 1) as *const _;
            Some(ptr::read(NonNull::<T>::dangling().as_ptr()))
        } else {
            let old_ptr = self.start;
            self.start = self.start.offset(1);
            Some(ptr::read(old_ptr))
        }
    }}
}
```

**Example 4** (Ch. 9, Drain): Borrowing Vec while yielding elements by value:
```rust
pub fn drain(&mut self) -> Drain<T> {
    let iter = unsafe { RawValIter::new(&self) };
    // mem::forget safety: if Drain is forgotten, we leak contents
    self.len = 0;
    Drain { iter, vec: PhantomData }
}
```

# Relationships

## Builds Upon
- **implementing-vec-fundamentals** -- IntoIter, Drain, and ZST handling extend the core Vec established there

## Enables
- Understanding of how standard library collection iterators work internally
- Knowledge of the RawVec pattern used throughout the standard library

## Related
- **implementing-arc** -- uses similar NonNull/PhantomData layout patterns with different ownership semantics

## Contrasts With
- Safe iterator implementations that rely on slice references rather than raw pointer manipulation
- Iterators for non-ZST types only, which do not need the integer-arithmetic pointer trick

# Common Errors

- **Error**: Forgetting to prevent Vec's Drop from running when creating IntoIter.
  **Correction**: Use `ManuallyDrop::new(self)` or `mem::forget(self)` after extracting the buffer and length. Otherwise, Vec's destructor would deallocate the buffer that IntoIter still needs.

- **Error**: Setting `end = ptr.as_ptr().add(len)` when `cap == 0`.
  **Correction**: When cap is 0, the pointer is `NonNull::dangling()` and no allocation exists. Offsetting it is invalid. Set `end = ptr.as_ptr()` (equal to start) to signal an empty iterator.

- **Error**: Deallocating ZST allocations (passing `NonNull::dangling()` to `dealloc`).
  **Correction**: Check `self.cap != 0 && mem::size_of::<T>() != 0` before deallocating. ZSTs never allocate, so there is nothing to deallocate.

- **Error**: Using the counter-pointer directly with `ptr::read` for ZST iteration.
  **Correction**: Counter-pointers are unaligned integers cast to pointers. Read from `NonNull::<T>::dangling().as_ptr()` instead, which is properly aligned. The read is a no-op for ZSTs anyway.

# Common Confusions

- **Confusion**: Thinking `next` and `next_back` have symmetric read-then-advance logic.
  **Clarification**: "The order of read and offset are reversed for `next` and `next_back`." For `next`, read then advance start. For `next_back`, retreat end then read. This is because `end` always points past the next element, while `start` points at it.

- **Confusion**: Thinking RawVec is a standard library type that users should use.
  **Clarification**: RawVec is an internal implementation detail extracted to share allocation logic between Vec and IntoIter. It is not part of the public API. The real standard library has a similar internal `RawVec`.

- **Confusion**: Thinking ZSTs with `cap = usize::MAX` could overflow on push.
  **Clarification**: Setting cap to `usize::MAX` means `self.len == self.cap()` can only be true after `usize::MAX` pushes, at which point `grow()` is called and immediately panics with "capacity overflow." This guards against actually overflowing.

# Source Reference

Chapter 9: Example: Implementing Vec -- sections: IntoIter (two-pointer idiom, ManuallyDrop, DoubleEndedIterator, Drop), RawVec (extraction of allocation logic, simplified Vec/IntoIter), Drain (PhantomData lifetime, mem::forget safety), Handling Zero-Sized Types (allocation guards, iteration via integer arithmetic, alignment concerns). Includes complete final code with tests.

# Verification Notes

- Definition source: Direct quotations from Ch. 9 IntoIter, RawVec, Drain, and ZST sections
- Key Properties: Derived from code examples and explanatory text
- ZST alignment bug: Explicitly discussed in source -- "The original author only noticed the problem when linking to this page years later"
- Confidence rationale: HIGH -- the source is a complete implementation walkthrough with step-by-step code evolution
- Uncertainties: None
- Cross-reference status: `implementing-vec-fundamentals` is in this extraction set; `implementing-arc` is in this extraction set
