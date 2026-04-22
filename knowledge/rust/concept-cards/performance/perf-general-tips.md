---
concept: General Performance Tips
slug: perf-general-tips
category: performance
subcategory: optimization-strategy
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Logging and Debugging / Wrapper Types / Machine Code / Parallelism / General Tips"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - "optimization principles"
  - "logging performance"
  - "wrapper type overhead"
  - "machine code inspection"
  - "rayon parallelism"
  - "lazy computation"
  - "special case optimization"
prerequisites: []
extends: []
related:
  - perf-iterators-and-bounds
  - perf-io
  - perf-compile-times
contrasts_with: []
answers_questions:
  - "What are the general principles for optimizing Rust code?"
  - "How can logging and debugging code slow down a program?"
  - "How should I group wrapper types like Mutex and RefCell for performance?"
  - "How do I inspect generated machine code in Rust?"
  - "What crates should I use for parallelism in Rust?"
  - "When is it worth optimizing for common special cases?"
---

# Quick Definition

A collection of smaller optimization topics: ensure logging/debugging code does no work when disabled; group co-accessed values under a single wrapper type (`Mutex`, `RefCell`) to reduce lock overhead; inspect hot code's machine output via Compiler Explorer or `cargo-show-asm`; use `rayon`/`crossbeam` for thread parallelism and SIMD for data parallelism; and follow general principles -- profile first, optimize algorithms before micro-optimizations, handle common cases fast, compute lazily, and document non-obvious optimizations.

# Core Definition

Chapters 13-17 of The Rust Performance Book cover five brief topics. **Logging and Debugging** (Ch. 13): logging/debugging code and its data-collection feeders can be surprisingly expensive; ensure no unnecessary work runs when logging is disabled, and use `debug_assert!` instead of `assert!` for hot assertions that are not safety-critical. **Wrapper Types** (Ch. 14): `RefCell`, `Mutex`, and similar wrappers have non-trivial access cost; when multiple wrapped values are typically accessed together, combining them under a single wrapper (e.g., `Arc<Mutex<(u32, u32)>>` instead of two `Arc<Mutex<u32>>` fields) can reduce overhead. **Machine Code** (Ch. 15): for very hot small code, inspect the generated assembly via Compiler Explorer (godbolt.org) or `cargo-show-asm`; the `core::arch` module provides architecture-specific intrinsics including SIMD instructions. **Parallelism** (Ch. 16): `rayon` and `crossbeam` are recommended for thread-based parallelism; SIMD/data parallelism is a separate topic with evolving Rust support. **General Tips** (Ch. 17): only optimize hot code; the biggest gains come from algorithms/data structures, not micro-optimization; minimize cache misses and branch mispredictions; accumulate small wins; use multiple profilers; make functions faster or call them less; eliminate silly slowdowns before adding clever speedups; compute lazily; optimize for common special cases (especially collections with 0-2 elements); use compact representations with fallback tables for repetitive data; handle the most common cases first; put small caches in front of data structures with high locality; and document non-obvious optimized code with comments referencing profiling data.

# Prerequisites

This is a foundational performance concept with no prerequisites within this source, though general Rust programming knowledge and profiling experience are assumed.

# Key Properties

1. Logging/debugging code and its data-collection feeders can cause measurable slowdowns even when the output is not displayed; guard them with conditional checks
2. `assert!` runs in all builds; `debug_assert!` only runs in dev builds -- use the latter for hot assertions that are not required for safety
3. Wrapper types (`RefCell`, `Mutex`) have non-trivial access cost; co-accessed values should be grouped under a single wrapper to reduce the number of lock/borrow operations
4. Compiler Explorer (godbolt.org) and `cargo-show-asm` let you inspect generated machine code for hot snippets
5. `core::arch` provides architecture-specific intrinsics including SIMD instructions
6. `rayon` and `crossbeam` are the recommended crates for thread-based parallelism; "Rust Atomics and Locks" by Mara Bos is recommended reading
7. Only optimize hot code -- optimized code is more complex and the effort is only worthwhile where it matters
8. The biggest performance gains come from algorithm and data structure changes, not low-level micro-optimization
9. Minimize cache misses and branch mispredictions where possible
10. Two strategies for speeding up a hot function: (a) make it faster, (b) call it less often
11. Eliminating "silly slowdowns" is often easier and more effective than introducing "clever speedups"
12. Lazy/on-demand computation avoids unnecessary work
13. Optimistically handle common special cases first; in particular, specially handling collections with 0, 1, or 2 elements is often a win when small sizes dominate
14. For repetitive data, use compact representation for common values with a fallback secondary table for unusual values
15. Put a small cache in front of data structures with high-locality access patterns
16. Comment non-obvious optimized code, referencing profiling data (e.g., "99% of the time this vector has 0 or 1 elements")

# Construction / Recognition

## To Apply These Optimization Principles:
1. Profile first to identify hot code; use multiple profilers for different perspectives
2. Check for algorithm/data-structure improvements before micro-optimization
3. Look for "silly slowdowns" -- unnecessary work, logging overhead, redundant computation
4. Measure case frequencies and handle the most common cases first
5. Consider lazy/on-demand computation for expensive values that may not always be needed
6. For collections, check if small-size special cases (0, 1, 2 elements) dominate

## To Audit Logging/Debugging Performance:
1. Identify all logging statements and their data-collection code
2. Ensure data collection is gated behind the same conditional as the logging output
3. Replace hot `assert!` calls with `debug_assert!` where the assertion is not safety-critical

## To Optimize Wrapper Types:
1. Identify fields that use separate `Mutex`/`RefCell`/`Arc` wrappers
2. Determine which fields are typically accessed together
3. Combine co-accessed fields under a single wrapper (e.g., `Arc<Mutex<(A, B)>>`)
4. Benchmark to confirm the change helps -- access patterns determine whether grouping is beneficial

## To Inspect Machine Code:
1. Isolate the hot function or snippet
2. Paste it into Compiler Explorer (godbolt.org) to view assembly
3. For full projects, use `cargo-show-asm` to view assembly of specific functions
4. Look for removable bounds checks, missed vectorization, or unexpected branches

# Context & Application

These chapters are largely stubs pointing to external resources rather than providing deep treatment. The general tips chapter (Ch. 17) is the most substantive of the group and reflects hard-won optimization wisdom from the Rust compiler's own development -- many of the linked examples are from rust-lang/rust PRs. The principles are universal (not Rust-specific) but particularly relevant in Rust because Rust's zero-cost abstractions make it tempting to skip profiling and optimize prematurely.

The wrapper types guidance is especially relevant for concurrent Rust code, where reducing the number of mutex acquisitions directly reduces contention. The logging advice applies to any production system where tracing/logging is enabled in release builds.

# Examples

**Example 1** (Ch. 13, "Logging and Debugging"): Rust compiler PRs (#50246, #75133, #147293) showed measurable slowdowns from data collection code that ran even when logging was disabled.

**Example 2** (Ch. 13): Replacing `assert!` with `debug_assert!` in hot paths within the Rust compiler (PRs #58210, #90746) improved performance by skipping non-safety-critical assertions in release builds.

**Example 3** (Ch. 14, "Wrapper Types"): Restructuring a struct from two separate `Arc<Mutex<u32>>` fields to a single `Arc<Mutex<(u32, u32)>>` reduced lock acquisition overhead in the Rust compiler (PR #68694).

**Example 4** (Ch. 17, "General Tips"): Algorithm changes in the Rust compiler (PRs #53383, #54318) produced larger speedups than any micro-optimization.

**Example 5** (Ch. 17): Lazy computation in the Rust compiler (PRs #36592, #50339) avoided unnecessary work. Special-casing small collections (PRs #50932, #64627, #64949) was effective because small sizes dominated.

# Relationships

## Builds Upon
- General programming optimization knowledge (profiling, algorithm design) -- assumed prerequisite

## Enables
- Informed optimization decisions in Rust projects
- Performance-aware wrapper type design

## Related
- **perf-iterators-and-bounds** -- iterator optimization is one specific application of the "make it faster or call it less" principle
- **perf-io** -- I/O buffering is an instance of batching to reduce syscall overhead
- **perf-compile-times** -- compile-time optimization is a related but distinct performance domain

## Contrasts With
- None explicitly stated in the source

# Common Errors

- **Error**: Running expensive data-collection code for logging even when logging is disabled.
  **Correction**: Gate data collection behind the same conditional check as the logging output so no work is done when logging is off.

- **Error**: Using `assert!` for a hot invariant check that is not required for memory safety.
  **Correction**: Use `debug_assert!` so the check only runs in dev/debug builds, not in release.

- **Error**: Wrapping each field in its own `Mutex` when the fields are always accessed together.
  **Correction**: Group co-accessed fields under a single `Mutex` to reduce lock acquisitions.

- **Error**: Micro-optimizing cold code without profiling first.
  **Correction**: Profile to identify hot code, then optimize only what matters. Most optimizations to cold code are wasted effort.

# Common Confusions

- **Confusion**: Thinking all optimizations should focus on making code run faster.
  **Clarification**: The source identifies two strategies: (a) make the function faster, and (b) avoid calling it as much. Strategy (b) is often easier and more impactful.

- **Confusion**: Believing one profiler gives a complete picture.
  **Clarification**: "Different profilers have different strengths. It is good to use more than one."

- **Confusion**: Thinking Rust code needs extensive optimization because it is a systems language.
  **Clarification**: The source notes that "as long as the obvious pitfalls are avoided (e.g., using non-release builds), Rust code generally is fast and uses little memory."

- **Confusion**: Assuming wrapper type grouping always helps.
  **Clarification**: "Whether or not this helps performance will depend on the exact access patterns of the values." Benchmark to confirm.

# Source Reference

Chapter 13: Logging and Debugging (18 lines). Covers logging/debugging overhead and `assert!` vs `debug_assert!`. Links to Rust compiler PRs #50246, #75133, #147293, #58210, #90746. Chapter 14: Wrapper Types (28 lines). Covers grouping `RefCell`/`Mutex` wrappers. Links to Rust compiler PR #68694. Chapter 15: Machine Code (16 lines). Covers Compiler Explorer, `cargo-show-asm`, and `core::arch`. Chapter 16: Parallelism (23 lines). References `rayon`, `crossbeam`, "Rust Atomics and Locks," and SIMD blog post. Chapter 17: General Tips (70 lines). Covers optimization philosophy, algorithms vs micro-optimization, lazy computation, special-case handling, compact representations, caching, and documentation. Links to numerous Rust compiler PRs.

# Verification Notes

- Definition source: Synthesized from five brief chapters (Ch. 13-17), most of which are stubs or short collections of tips
- Key Properties: All properties are explicit in the source text, though many are stated briefly without elaboration
- Confidence rationale: MEDIUM -- the individual chapters (13, 14, 15, 16) are very brief stubs with minimal detail; Ch. 17 has more substance but is a collection of tips rather than a structured treatment; grouping five chapters into one card necessarily compresses the content
- Uncertainties: Chapters 13-16 are near-stubs that primarily point to external resources; the depth of coverage is intentionally shallow
- Cross-reference status: perf-iterators-and-bounds, perf-io, perf-compile-times are sibling cards from this extraction set
