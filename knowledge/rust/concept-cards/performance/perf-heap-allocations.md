---
concept: Heap Allocation Optimization
slug: perf-heap-allocations
category: performance
subcategory: memory
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Heap Allocations"
chapter_number: 7
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "allocation optimization"
  - "reducing allocations"
  - "SmallVec"
  - "ArrayVec"
  - "Cow"
  - "clone-on-write"
  - "clone_from"
  - "reusing collections"
  - "smartstring"
prerequisites:
  - perf-profiling
extends: []
related:
  - perf-build-configuration
  - perf-type-sizes
  - perf-hashing
  - perf-stdlib-types
contrasts_with: []
answers_questions:
  - "How do I reduce heap allocations in Rust?"
  - "When should I use SmallVec vs Vec?"
  - "How does Cow reduce allocations?"
  - "What is clone_from and why is it faster than clone?"
  - "How do I avoid allocations when reading lines from a file?"
  - "How do I profile heap allocations in Rust?"
  - "What is smartstring and when should I use it?"
  - "How do I reuse collections to avoid repeated allocations?"
---

# Quick Definition

Heap allocations are moderately expensive in Rust (involving global locks, data structure manipulation, and possibly system calls). Key optimization strategies include using `SmallVec`/`ArrayVec` for short vectors, `Cow` for mixed borrowed/owned data, `clone_from` instead of `clone`, reserving capacity with `Vec::with_capacity`, reusing collections, and using `smartstring` for short strings.

# Core Definition

"Heap allocations are moderately expensive. The exact details depend on which allocator is in use, but each allocation (and deallocation) typically involves acquiring a global lock, doing some non-trivial data structure manipulation, and possibly executing a system call. Small allocations are not necessarily cheaper than large allocations. It is worth understanding which Rust data structures and operations cause allocations, because avoiding them can greatly improve performance." (Ch. 7, Heap Allocations introduction)

The chapter covers the allocation behavior of core types (`Box`, `Rc`/`Arc`, `Vec`, `String`, hash tables), operations that trigger allocations (`clone`, `to_owned`, `format!`), and techniques to reduce allocation rates (`SmallVec`, `ArrayVec`, capacity pre-allocation, `Cow`, collection reuse, `clone_from`). DHAT profiling is recommended for identifying hot allocation sites, with experience from rustc showing that "reducing allocation rates by 10 allocations per million instructions executed can have measurable performance improvements (e.g. ~1%)." (Ch. 7, Profiling)

# Prerequisites

- **perf-profiling** -- DHAT is specifically recommended for identifying hot allocation sites before optimizing

# Key Properties

1. **Vec internals**: Contains three words (length, capacity, pointer); elements are always heap-allocated if present and nonzero-sized; growth strategy is quasi-doubling: 0, 4, 8, 16, 32, 64...
2. **SmallVec<[T; N]>**: Stores up to N elements inline, then falls back to heap allocation; slightly slower than `Vec` for normal operations due to the inline/heap check; available from the `smallvec` crate
3. **ArrayVec**: From the `arrayvec` crate; like SmallVec but never falls back to heap allocation, making it faster when the maximum length is known precisely
4. **Vec capacity**: `Vec::with_capacity`, `Vec::reserve`, and `Vec::reserve_exact` avoid multiple reallocations when the size is known; `Vec::shrink_to_fit` reclaims excess capacity
5. **String**: Behaves like `Vec<u8>` for allocation purposes; `smartstring` avoids heap allocation for strings <= 23 ASCII characters (on 64-bit); `format!` always allocates
6. **Cow**: Holds either borrowed or owned data; avoids unnecessary allocations when data is usually borrowed but occasionally needs to be owned; supports clone-on-write via `Cow::to_mut`
7. **clone_from**: `a.clone_from(&b)` may reuse `a`'s existing allocation, unlike `a = b.clone()` which always allocates fresh
8. **Rc/Arc**: `clone` does not allocate (just increments reference count), but overuse can increase allocation rates by heap-allocating values that could otherwise be stack-allocated
9. **Collection reuse**: Declaring a "workhorse" collection outside a loop and clearing it each iteration avoids repeated allocations
10. **BufRead::read_line**: Reusing a single `String` with `read_line` + `clear` is far more efficient than `BufRead::lines` which allocates for every line
11. **dhat-rs**: Provides heap usage testing to write tests that verify allocation counts, preventing allocation regressions

# Construction / Recognition

## To Identify Allocation Hot Spots:
1. Run a general-purpose profiler; if `malloc`/`free` are hot, allocation optimization is worthwhile
2. Use DHAT (or dhat-rs) to identify exact hot allocation sites and their rates
3. Use `eprintln!` at hot `Vec::push` sites to understand length distributions

## To Optimize Short Vectors:
1. If many short vectors exist, replace `Vec<T>` with `SmallVec<[T; N]>` from the `smallvec` crate
2. If the maximum length is known precisely, use `ArrayVec` from the `arrayvec` crate instead
3. Benchmark: SmallVec is slightly slower for normal operations and may be larger than Vec if N is high or T is large

## To Optimize Longer Vectors:
1. Use `Vec::with_capacity(n)` when the minimum or exact size is known
2. Use `Vec::shrink_to_fit()` to reclaim excess capacity (note: may reallocate)

## To Avoid String Allocations:
1. Use string literals instead of `format!` when possible
2. Use `smartstring::String` for strings that are often short (<=23 ASCII chars)
3. Use `std::format_args` or the `lazy_format` crate to defer formatting

## To Use Cow for Mixed Borrowed/Owned Data:
1. Replace `Vec<String>` with `Vec<Cow<'static, str>>` when mixing string literals and formatted strings
2. Use `Cow::Borrowed(x)` for borrowed data and `Cow::Owned(y)` or `.into()` for owned data
3. Use `Cow::to_mut()` for clone-on-write semantics when data is mostly read but occasionally mutated

## To Reuse Collections:
1. Declare the collection outside the loop
2. Use it within the loop body
3. Call `.clear()` at the end of each iteration (empties without affecting capacity)
4. For functions called repeatedly, accept `&mut Vec<T>` instead of returning `Vec<T>`

# Context & Application

Heap allocation optimization is one of the most impactful categories of Rust performance work. The chapter provides a systematic taxonomy of allocation sources and mitigation strategies, grounded in extensive experience optimizing the Rust compiler itself.

The `Cow` type is highlighted as particularly valuable but "fiddly to get working." It bridges the gap between the zero-cost borrowed case and the owned case, supporting both `&str`/`String`, `&[T]`/`Vec<T>`, and `&Path`/`PathBuf` pairings. The clone-on-write semantics via `Cow::to_mut` are useful for data that is "mostly read-only but occasionally needs to be modified."

The distinction between `clone` and `clone_from` is subtle but important: `clone_from` can reuse existing allocations, making `a.clone_from(&b)` potentially much cheaper than `a = b.clone()`. The example shows a Vec with capacity 99 retaining that capacity after `clone_from`.

Collection reuse trades code clarity for performance: declaring a workhorse Vec outside a loop "obscures the fact that each iteration's usage of the Vec is unrelated to the others." This is a conscious trade-off.

# Examples

**Example 1** (Ch. 7, Vec Growth): Vec's growth strategy skips directly from capacity 0 to 4, avoiding many allocations in practice. Knowing the likely length allows using `Vec::with_capacity` to avoid multiple reallocations -- "if you know a vector will grow to have at least 20 elements, these functions can immediately provide a vector with a capacity of at least 20 using a single allocation, whereas pushing the items one at a time would result in four allocations (for capacities of 4, 8, 16, and 32)."

**Example 2** (Ch. 7, Cow): Using Cow to avoid allocations with mixed static/dynamic strings:
```rust
use std::borrow::Cow;
let mut errors: Vec<Cow<'static, str>> = vec![];
errors.push(Cow::Borrowed("something went wrong"));
errors.push(Cow::Owned(format!("something went wrong on line {}", 100)));
errors.push(Cow::from("something else went wrong"));
errors.push(format!("something else went wrong on line {}", 101).into());
```

**Example 3** (Ch. 7, Reading Lines): Replacing `BufRead::lines()` (allocates per line) with `read_line` reusing a single String:
```rust
let mut lock = io::stdin().lock();
let mut line = String::new();
while lock.read_line(&mut line)? != 0 {
    process(&line);
    line.clear();
}
```
This reduces allocations to at most a handful (depending on line length distribution).

**Example 4** (Ch. 7, clone_from): Reusing allocation with `clone_from`:
```rust
let mut v1: Vec<u32> = Vec::with_capacity(99);
let v2: Vec<u32> = vec![1, 2, 3];
v1.clone_from(&v2); // v1's allocation is reused
assert_eq!(v1.capacity(), 99);
```

# Relationships

## Builds Upon
- **perf-profiling** -- DHAT profiling is explicitly required to identify hot allocation sites

## Enables
- More efficient memory usage and reduced allocation overhead across the entire program

## Related
- **perf-build-configuration** -- alternative allocators (jemalloc, mimalloc) are a complementary approach to reducing allocation cost
- **perf-type-sizes** -- shrinking types reduces allocation sizes and memory traffic
- **perf-hashing** -- hash tables have similar allocation patterns to Vec
- **perf-stdlib-types** -- covers additional standard library type optimizations

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `SmallVec` with a large N or large T, making the SmallVec itself larger than a Vec.
  **Correction**: "If `N` is high or `T` is large, then the `SmallVec<[T; N]>` itself can be larger than `Vec<T>`, and copying of `SmallVec` values will be slower." Benchmark to confirm the optimization is effective.

- **Error**: Using `BufRead::lines()` for performance-sensitive file reading.
  **Correction**: `lines()` allocates a new `String` for every line. Use `read_line` with a reusable `String` buffer and `clear()` to reduce allocations to a handful.

- **Error**: Using `a = b.clone()` when `a`'s existing allocation could be reused.
  **Correction**: Use `a.clone_from(&b)` instead, which reuses `a`'s heap allocation when possible.

- **Error**: Using `Rc`/`Arc` for values that are rarely shared.
  **Correction**: "If used for values that are rarely shared, they can increase allocation rates by heap allocating values that might otherwise not be heap-allocated." Only use Rc/Arc when sharing actually occurs.

# Common Confusions

- **Confusion**: Thinking SmallVec is always faster than Vec.
  **Clarification**: "It is slightly slower than `Vec` for normal operations because it must always check if the elements are heap-allocated or not." SmallVec wins by reducing allocation counts, but the per-operation overhead means it must be benchmarked for the specific use case.

- **Confusion**: Thinking `format!` is free because it returns a stack value.
  **Clarification**: `format!` produces a `String`, which involves a heap allocation. If a string literal can be used instead, it avoids this allocation entirely.

- **Confusion**: Thinking `Cow` only avoids allocations for borrowed data.
  **Clarification**: `Cow` also provides clone-on-write semantics via `Cow::to_mut` -- if the data is borrowed and needs mutation, it clones to owned at that point. This is useful for data that is "mostly read-only but occasionally needs to be modified."

# Source Reference

Chapter 7: Heap Allocations -- all sections: Profiling (DHAT), Box, Rc/Arc, Vec (Growth, Short Vecs, Longer Vecs), String, Hash Tables, clone, to_owned, Cow (clone-on-write), Reusing Collections, Reading Lines from a File, Using an Alternative Allocator, Avoiding Regressions (dhat-rs heap usage testing).

# Verification Notes

- Definition source: Direct quotation from Ch. 7 introduction
- Vec internals: Directly from the Vec section including growth strategy
- SmallVec/ArrayVec: Directly from Short Vecs section with trade-offs
- Cow: Directly from Cow section with code examples
- clone_from: Directly from clone section with code example
- Confidence rationale: HIGH -- the longest and most detailed chapter in the book, with extensive code examples and links to real-world rustc PRs
- Uncertainties: None
