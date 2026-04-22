---
concept: "Implementing Arc: Atomic Reference Counting"
slug: implementing-arc
category: unsafe-rust
subcategory: concurrency-primitive
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "10-implementing-arc"
chapter_number: 10
pdf_page: null
section: "Layout, Base Code, Cloning, Dropping, Final Code"
extraction_confidence: high
aliases:
  - "Arc implementation"
  - "atomic reference counting"
  - "ArcInner"
  - "reference counting with atomics"
  - "Arc Clone and Drop"
prerequisites:
  - implementing-vec-fundamentals
extends: []
related:
  - implementing-vec-fundamentals
  - implementing-vec-iterators-zst
contrasts_with: []
answers_questions:
  - "How do I implement Arc from scratch?"
  - "Why does Arc use NonNull and PhantomData together?"
  - "What memory ordering does Arc::clone use and why?"
  - "Why does Arc::drop use Release ordering with an Acquire fence?"
  - "How does Arc prevent reference count overflow from mem::forget?"
  - "Why does Arc require T: Send + Sync for Send/Sync impls?"
  - "How does Arc use Box::into_raw and Box::from_raw for allocation?"
---

# Quick Definition

Implementing `Arc<T>` demonstrates atomic reference counting with correct memory orderings: `NonNull<ArcInner<T>>` + `PhantomData<ArcInner<T>>` for the layout, `Relaxed` ordering for clone (no synchronization needed for incrementing), `Release` ordering for the decrement in drop (ensures all uses happen-before deletion), and an `Acquire` fence before the final deallocation (synchronizes with all prior releases). The reference count is guarded against overflow from `mem::forget` by aborting at `isize::MAX`.

# Core Definition

"An `Arc<T>` provides thread-safe shared ownership of a value of type `T`, allocated in the heap." The reference count is "inherently shared mutable state, so Arc does need to think about synchronization. We could use a Mutex for this, but that's overkill. Instead, we'll use atomics." (Ch. 10, Layout) The inner structure pairs an `AtomicUsize` reference count with the data, and the outer Arc holds a `NonNull` pointer plus `PhantomData` for correct variance and drop-check behavior.

Clone uses `Relaxed` ordering: "We don't really have any code that will need atomic synchronization when cloning, as we do not modify the internal value while cloning." (Ch. 10, Cloning) Drop uses `Release` on `fetch_sub` and an `Acquire` fence before deallocation: "This fence is needed to prevent reordering of use of the data and deletion of the data. Because it is marked Release, the decreasing of the reference count synchronizes with this Acquire fence." (Ch. 10, Dropping)

# Prerequisites

- **implementing-vec-fundamentals** -- Understanding of `NonNull<T>` for variance, `PhantomData` for drop-check, and manual `Send`/`Sync` impls; the source explicitly references the Vec implementation

# Key Properties

1. **ArcInner<T>**: Contains `rc: AtomicUsize` (reference count) and `data: T`; heap-allocated via `Box::new` then extracted with `Box::into_raw`
2. **Arc<T> layout**: `NonNull<ArcInner<T>>` for covariance and non-null guarantee; `PhantomData<ArcInner<T>>` to tell the drop checker Arc has ownership of `ArcInner<T>`
3. **Construction**: `Box::new(ArcInner { rc: AtomicUsize::new(1), data })` then `NonNull::new(Box::into_raw(boxed)).unwrap()`
4. **Send/Sync bounds**: `unsafe impl<T: Sync + Send> Send for Arc<T> {}` and `unsafe impl<T: Sync + Send> Sync for Arc<T> {}` -- both bounds are required because without them, `Arc<Rc<u32>>` would be Send, allowing data races on the non-thread-safe Rc
5. **Deref**: Dereferences `NonNull` via `unsafe { self.ptr.as_ref() }` then returns `&inner.data`
6. **Clone ordering (Relaxed)**: No synchronization needed when incrementing the refcount -- "we do not modify the internal value while cloning"
7. **Overflow guard**: Aborts if `old_rc >= isize::MAX` -- defends against `mem::forget` causing unbounded refcount growth that would lead to use-after-free
8. **Drop ordering (Release)**: `fetch_sub(1, Ordering::Release)` ensures all accesses to the data happen-before the refcount decrement
9. **Drop fence (Acquire)**: `atomic::fence(Ordering::Acquire)` before deallocation synchronizes with all prior Release decrements, ensuring "use of the data happens before decreasing the reference count, which happens before this fence, which happens before the deletion of the data"
10. **Final deallocation**: `Box::from_raw(self.ptr.as_ptr())` reconstitutes the Box to drop the inner data and free the allocation

# Construction / Recognition

## To Implement Arc Layout:
1. Define `ArcInner<T>` with `rc: AtomicUsize` and `data: T`
2. Define `Arc<T>` with `ptr: NonNull<ArcInner<T>>` and `phantom: PhantomData<ArcInner<T>>`
3. `NonNull` provides covariance and non-null guarantee; `PhantomData` provides correct drop-check ownership info
4. Implement `unsafe impl<T: Sync + Send> Send/Sync for Arc<T>`

## To Implement Arc::new:
1. Box the ArcInner with refcount initialized to 1
2. Convert to raw pointer with `Box::into_raw`
3. Wrap in `NonNull::new(...).unwrap()` -- guaranteed non-null from Box

## To Implement Clone:
1. Load inner via `unsafe { self.ptr.as_ref() }`
2. `fetch_add(1, Ordering::Relaxed)` -- Relaxed is sufficient for incrementing
3. Check `old_rc >= isize::MAX` and abort to guard against mem::forget overflow
4. Return new Arc copying the pointer and PhantomData

## To Implement Drop:
1. `fetch_sub(1, Ordering::Release)` -- Release ensures prior accesses happen-before
2. If the old value was not 1, return (other references remain)
3. `atomic::fence(Ordering::Acquire)` -- synchronizes with all prior Release decrements
4. `Box::from_raw(self.ptr.as_ptr())` -- drops data and frees allocation

# Context & Application

This implementation is "loosely based on the standard library's implementation (technically taken from `alloc::sync` in 1.49)" but simplified by omitting weak references. It demonstrates how atomics and memory orderings work together to create a correct concurrent data structure.

The memory ordering choices are carefully justified. Clone uses Relaxed because incrementing the count has no data dependency -- if a thread has an Arc reference, the data is already visible to it. Drop uses Release on the decrement so that any mutations to interior-mutable data (like through a `Mutex<T>` inside the Arc) are visible to whichever thread performs the final deallocation. The Acquire fence before deallocation completes the synchronization: "Since a Mutex is not acquired when it is deleted, we can't rely on its synchronization logic to make writes in thread A visible to a destructor running in thread B."

The overflow guard against `mem::forget` is defensive: the standard library aborts at `isize::MAX` "on the assumption that there are probably not about 2 billion threads (or about 9 quintillion on some 64-bit machines) incrementing the reference count at once."

# Examples

**Example 1** (Ch. 10, Layout): Arc with correct variance and drop-check:
```rust
use std::marker::PhantomData;
use std::ptr::NonNull;
use std::sync::atomic::AtomicUsize;

pub struct Arc<T> {
    ptr: NonNull<ArcInner<T>>,
    phantom: PhantomData<ArcInner<T>>,
}
pub struct ArcInner<T> {
    rc: AtomicUsize,
    data: T,
}
```

**Example 2** (Ch. 10, Clone): Relaxed increment with overflow guard:
```rust
impl<T> Clone for Arc<T> {
    fn clone(&self) -> Arc<T> {
        let inner = unsafe { self.ptr.as_ref() };
        let old_rc = inner.rc.fetch_add(1, Ordering::Relaxed);
        if old_rc >= isize::MAX as usize {
            std::process::abort();
        }
        Self { ptr: self.ptr, phantom: PhantomData }
    }
}
```

**Example 3** (Ch. 10, Drop): Release decrement with Acquire fence:
```rust
impl<T> Drop for Arc<T> {
    fn drop(&mut self) {
        let inner = unsafe { self.ptr.as_ref() };
        if inner.rc.fetch_sub(1, Ordering::Release) != 1 {
            return;
        }
        atomic::fence(Ordering::Acquire);
        unsafe { Box::from_raw(self.ptr.as_ptr()); }
    }
}
```

# Relationships

## Builds Upon
- Atomic operations and memory orderings (`Relaxed`, `Release`, `Acquire`)
- `NonNull<T>` and `PhantomData` for type-system correctness (same patterns as Vec)
- `Box::into_raw` / `Box::from_raw` for manual heap management

## Enables
- Understanding of how production-quality concurrent data structures handle memory ordering
- Foundation for understanding weak references and more complex reference-counting schemes

## Related
- **implementing-vec-fundamentals** -- uses identical `NonNull`/`PhantomData` layout patterns; explicitly referenced by the source
- **implementing-vec-iterators-zst** -- shares the pattern of manual allocation management with Box::into_raw

## Contrasts With
- `Rc<T>` -- single-threaded reference counting, no atomics needed, no Send/Sync
- Using a `Mutex` for the reference count -- correct but "overkill" compared to atomics

# Common Errors

- **Error**: Using `Acquire` or `SeqCst` ordering for clone's `fetch_add`.
  **Correction**: `Relaxed` is sufficient. No data synchronization is needed when incrementing because the cloning thread already has access to the data through its existing Arc reference.

- **Error**: Using `Relaxed` ordering for drop's `fetch_sub`.
  **Correction**: `Release` ordering is required so that all prior accesses to the data (including writes through interior mutability like `Mutex<T>`) happen-before the decrement, making them visible to the thread that performs final deallocation.

- **Error**: Omitting the `Acquire` fence before deallocation.
  **Correction**: Without the fence, the dropping thread might not see writes made through interior-mutable types by other threads before they released their references. The Acquire fence synchronizes with all prior Release decrements.

- **Error**: Implementing `Send`/`Sync` for Arc without requiring `T: Send + Sync`.
  **Correction**: Without these bounds, `Arc<Rc<u32>>` would be `Sync`, allowing cloning of the non-thread-safe `Rc` across threads, causing data races.

# Common Confusions

- **Confusion**: Thinking the `Acquire` fence could be replaced with `Acquire` on the `fetch_sub`.
  **Clarification**: The source notes that "the Acquire fence here could probably be replaced with an Acquire load, which could improve performance in highly-contended situations." However, using `AcqRel` on `fetch_sub` would also work but would add unnecessary Acquire synchronization on every decrement, not just the final one.

- **Confusion**: Thinking `PhantomData<ArcInner<T>>` is only about variance.
  **Clarification**: It serves two purposes. `NonNull` already provides covariance. `PhantomData` additionally tells the drop checker that Arc owns an `ArcInner<T>`, which "will give incorrect ownership information to the drop checker" if omitted, since "at some point there will be an instance of this structure that entirely owns its data."

- **Confusion**: Thinking `Box::from_raw` just frees memory.
  **Clarification**: It reconstitutes the Box, which then runs Drop for `ArcInner<T>` (dropping the data T) and frees the heap allocation. It is a full ownership transfer back to Box.

# Source Reference

Chapter 10: Implementing Arc -- all sections: Layout (ArcInner, NonNull, PhantomData, variance, drop check), Base Code (construction via Box::into_raw, Send/Sync bounds, Deref), Cloning (Relaxed ordering, overflow guard, mem::forget defense), Dropping (Release ordering, Acquire fence, Box::from_raw deallocation), Final Code (complete implementation).

# Verification Notes

- Definition source: Direct quotations from Ch. 10 Layout, Cloning, and Dropping sections
- Memory ordering justification: Extended quotation from the Boost documentation via the standard library source, included verbatim in the source text
- Confidence rationale: HIGH -- complete walkthrough with detailed reasoning for each design choice, especially memory orderings
- Uncertainties: The chapter notes it is "very work-in-progress" and does not cover weak references or Mutex implementation (marked TODO)
- Cross-reference status: `implementing-vec-fundamentals` is in this extraction set
