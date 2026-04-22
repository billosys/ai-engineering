---
concept: Iterator and Bounds Check Performance
slug: perf-iterators-and-bounds
category: performance
subcategory: runtime-optimization
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Iterators / Bounds Checks"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "iterator performance"
  - "collect vs extend"
  - "bounds check elimination"
  - "chunks_exact"
  - "iter copied"
prerequisites: []
extends: []
related:
  - perf-general-tips
  - perf-io
contrasts_with: []
answers_questions:
  - "How do I avoid unnecessary allocations when using iterators?"
  - "When should I use collect vs extend vs returning an iterator?"
  - "How do I eliminate bounds checks in Rust for better performance?"
  - "What is the performance difference between chunks and chunks_exact?"
  - "When should I use iter().copied() instead of iter()?"
---

# Quick Definition

Iterator performance in Rust hinges on avoiding unnecessary allocations (prefer returning `impl Iterator` over `Vec`, use `extend` over `collect`+`append`, prefer `chunks_exact` over `chunks`), while bounds check elimination requires structuring code so the compiler can prove indices are in range -- through iteration, slicing before loops, or range assertions.

# Core Definition

The Rust Performance Book covers iterator optimization across four areas: (1) avoiding needless `collect` calls that allocate when an iterator would suffice, using `extend` instead of `collect`+`append`, and implementing `size_hint`/`ExactSizeIterator` so collection operations pre-allocate correctly; (2) preferring `filter_map` over `filter`+`map` chains and avoiding `chain` on hot iterators; (3) using `chunks_exact` instead of `chunks` for better codegen when the chunk size divides the slice length; (4) using `iter().copied()` on small `Copy` types so consumers receive values rather than references, which can produce better LLVM output. Separately, bounds checks on slice/vector accesses can be eliminated safely by iterating instead of indexing, slicing a `Vec` before a loop, or adding assertions on index ranges. As a last resort, `get_unchecked`/`get_unchecked_mut` can bypass bounds checks unsafely. (Ch. 10: Iterators; Ch. 11: Bounds Checks)

# Prerequisites

This is a foundational performance concept with no prerequisites within this source, though familiarity with Rust iterators, slices, and the `Iterator` trait is assumed.

# Key Properties

1. `Iterator::collect` requires an allocation; avoid it if the collection is only iterated over again
2. Returning `impl Iterator<Item=T>` from a function avoids the allocation that returning `Vec<T>` would require (may need additional lifetime annotations)
3. `extend` on an existing collection is more efficient than `collect` into a new `Vec` followed by `append`
4. Implementing `Iterator::size_hint` or `ExactSizeIterator::len` lets `collect`/`extend` pre-allocate, reducing the number of allocations
5. `chain` can be slower than a single iterator on hot paths
6. `filter_map` may be faster than `filter` followed by `map`
7. `chunks_exact` is faster than `chunks` because the compiler knows each chunk is exactly the specified size, enabling better optimization; handle remainders via `ChunksExact::remainder`
8. The `chunks_exact` advantage applies equally to `rchunks_exact`, `chunks_exact_mut`, and `rchunks_exact_mut`
9. `iter().copied()` on small `Copy` types (e.g., integers) yields values instead of references, and LLVM may generate better code in that case
10. Bounds checks on slice/vector indexing can be eliminated safely by: (a) using iteration, (b) slicing a `Vec` before the loop and indexing the slice, (c) adding `assert!` on index ranges
11. The unsafe `get_unchecked`/`get_unchecked_mut` methods bypass bounds checks entirely but should be a last resort
12. Bounds check elimination is tricky; the Bounds Check Cookbook provides detailed guidance

# Construction / Recognition

## To Optimize Iterator Usage:
1. Identify any `collect` call where the resulting collection is only iterated -- replace with returning `impl Iterator`
2. When extending an existing collection, call `extend(iter)` directly instead of `let v: Vec<_> = iter.collect(); existing.append(&mut v);`
3. For custom iterators, implement `size_hint` (or `ExactSizeIterator`) to help downstream `collect`/`extend` pre-allocate
4. On hot paths, replace `filter().map()` chains with `filter_map` and consider avoiding `chain`
5. Replace `chunks(n)` with `chunks_exact(n)` and handle the remainder separately

## To Eliminate Bounds Checks:
1. Replace indexed loops (`for i in 0..v.len() { v[i] }`) with iterators (`for x in &v`)
2. When indexing is necessary, slice the `Vec` before the loop: `let s = &v[start..end]; for i in 0..s.len() { s[i] }`
3. Add assertions before the loop body: `assert!(idx < v.len())` so the compiler can elide later checks
4. As a last resort, use `unsafe { v.get_unchecked(i) }`

# Context & Application

Iterator performance matters most in tight inner loops and data-processing pipelines where even small per-element costs multiply. The `collect`-vs-iterator guidance is particularly relevant when designing function APIs -- returning `impl Iterator` instead of `Vec` allows callers to compose without intermediate allocations. The `chunks_exact` optimization is important for SIMD-friendly processing of byte buffers and numeric arrays.

Bounds checks are typically not a bottleneck ("less often than you might expect"), but in verified hot loops they can measurably slow execution. The safe elimination techniques (iteration, pre-slicing, assertions) should be tried before resorting to `unsafe`. The `iter().copied()` technique is an advanced optimization that may require inspecting generated machine code to confirm its effect.

# Examples

**Example 1** (Ch. 10, "collect and extend"): A function returning `Vec<T>` that forces allocation can be changed to return `impl Iterator<Item=T>`, avoiding the allocation when the caller only iterates the result.

**Example 2** (Ch. 10, "Chunks"): Using `chunks_exact` instead of `chunks` in the `exrs` crate showed measurable improvement. When chunk size does not divide evenly, `chunks_exact` combined with `ChunksExact::remainder` is still faster than `chunks`.

**Example 3** (Ch. 10, "copied"): Iterating over a collection of integers with `iter().copied()` instead of `iter()` allowed LLVM to generate better machine code in Rust compiler internals.

**Example 4** (Ch. 11, "Bounds Checks"): Adding assertions on index variable ranges (e.g., in `rand` and `jpeg-decoder` crates) allowed the compiler to optimize away bounds checks within loops.

# Relationships

## Builds Upon
- General Rust iterator and slice knowledge (assumed prerequisite, not from this source)

## Enables
- Writing zero-allocation iterator pipelines for data processing
- Safe bounds-check-free inner loops for numerical and byte processing

## Related
- **perf-general-tips** -- the general optimization philosophy of profiling before optimizing and handling common cases applies to iterator optimization decisions
- **perf-io** -- I/O buffering works alongside iterator patterns when processing streamed data

## Contrasts With
- None explicitly stated in the source

# Common Errors

- **Error**: Calling `collect` into a `Vec` only to iterate over it once more (e.g., `let v: Vec<_> = iter.collect(); for x in &v { ... }`).
  **Correction**: Consume the iterator directly or return `impl Iterator` from the function.

- **Error**: Using `chunks(n)` when the chunk size is known to divide the length evenly.
  **Correction**: Use `chunks_exact(n)` for better compiler optimization; handle any remainder via `ChunksExact::remainder`.

- **Error**: Using `unsafe { get_unchecked(i) }` as the first approach to eliminating bounds checks.
  **Correction**: Try safe techniques first: iterate instead of indexing, pre-slice the container, or add assertions on index ranges.

# Common Confusions

- **Confusion**: Thinking bounds checks are always a significant performance bottleneck.
  **Clarification**: The source notes that bounds checks affect performance "less often than you might expect." Profile first to confirm they are actually hot before attempting elimination.

- **Confusion**: Believing `iter().copied()` always produces faster code than `iter()`.
  **Clarification**: The benefit depends on LLVM's optimization of the specific usage. The source calls this "an advanced technique" and recommends checking generated machine code to verify the effect.

- **Confusion**: Thinking `chain` is always a free abstraction.
  **Clarification**: `chain` introduces per-element overhead to track which of the two underlying iterators is active. On hot paths, a single iterator may be measurably faster.

# Source Reference

Chapter 10: Iterators. Sections on `collect` and `extend`, chaining, chunks, and `copied`. Includes links to pull requests in the Rust compiler (rust-lang/rust#77990, #64801), exrs crate (#173, #175), and Rust issues (#106539, #113789) as examples. Chapter 11: Bounds Checks. Brief chapter covering safe techniques (iteration, pre-slicing, assertions) and unsafe `get_unchecked`/`get_unchecked_mut`. References the Bounds Check Cookbook and pull requests in `rand` (#960) and `jpeg-decoder` (#167).

# Verification Notes

- Definition source: Directly from Ch. 10 and Ch. 11 prose and examples
- Key Properties: All 12 properties are explicit in the source text
- Confidence rationale: HIGH -- Ch. 10 provides detailed guidance with concrete examples and links to real-world PRs; Ch. 11 is brief but explicit
- Uncertainties: The `copied()` technique's effectiveness is described as requiring machine code inspection, making it situational
- Cross-reference status: perf-general-tips and perf-io are sibling cards from this extraction set
