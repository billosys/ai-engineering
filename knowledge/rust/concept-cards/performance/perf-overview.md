---
concept: Performance Overview
slug: perf-overview
category: performance
subcategory: methodology
tier: foundational
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Introduction, Benchmarking, Linting"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Rust performance basics"
  - "benchmarking Rust"
  - "Clippy perf lints"
  - "performance linting"
prerequisites: []
extends: []
related:
  - perf-build-configuration
  - perf-profiling
  - perf-heap-allocations
  - perf-type-sizes
contrasts_with: []
answers_questions:
  - "What does The Rust Performance Book cover?"
  - "How do I benchmark a Rust program?"
  - "Which benchmarking tools are available for Rust?"
  - "How can Clippy help with performance?"
  - "How do I disallow slow standard library types with Clippy?"
---

# Quick Definition

The Rust Performance Book covers practical techniques for improving runtime speed, memory usage, and binary size of Rust programs. Effective optimization begins with benchmarking to measure changes and linting with Clippy to catch performance anti-patterns automatically.

# Core Definition

"Performance is important for many Rust programs. This book contains techniques that can improve the performance-related characteristics of Rust programs, such as runtime speed, memory usage, and binary size." The book focuses on "techniques that are practical and proven: many are accompanied by links to pull requests or other resources that show how the technique was used on a real-world Rust program." It is aimed at intermediate and advanced Rust users. (Ch. 0, Introduction)

Benchmarking is the foundation of optimization: "Good benchmarking is hard. Having said that, do not stress too much about having a perfect benchmarking setup, particularly when you start optimizing a program. Mediocre benchmarking is far better than no benchmarking." (Ch. 1, Benchmarking)

Clippy provides automated performance detection: "It is an excellent tool to run on Rust code in general. It can also help with performance, because a number of the lints relate to code patterns that can cause sub-optimal performance." The book explicitly defers to Clippy for problems it can detect automatically: "the rest of this book will not mention performance problems that Clippy detects by default." (Ch. 3, Linting)

# Prerequisites

This is a foundational concept with no prerequisites within this source. The book assumes intermediate-to-advanced Rust knowledge.

# Key Properties

1. The book covers runtime speed, memory usage, binary size, and compile times
2. Some techniques require only build configuration changes; many require code changes
3. Benchmarking requires representative workloads -- real-world inputs are best, microbenchmarks and stress tests are useful in moderation
4. Wall-time is the obvious metric but suffers high variance; instruction counts or cycles may provide lower-variance alternatives
5. Benchmarking tools: Rust's built-in benchmark tests (nightly only), Criterion, Divan, Hyperfine (general-purpose), Bencher (CI), and custom harnesses like rustc-perf
6. Clippy's perf lint group catches sub-optimal performance patterns automatically
7. Non-performance lints (e.g., `ptr_arg`) can also improve performance by reducing indirection
8. Clippy's `disallowed_types` lint prevents accidental use of slow standard library types after switching to faster alternatives

# Construction / Recognition

## To Start Optimizing a Rust Program:
1. Establish benchmarks using realistic workloads and appropriate tools (Criterion, Divan, or Hyperfine)
2. Choose metrics appropriate to your program type -- wall-time for batch programs, but consider lower-variance alternatives like instruction counts
3. Run `cargo clippy` and address all perf lints first -- these are the easiest wins
4. If switching to alternative types (e.g., FxHashMap), add `disallowed_types` to `clippy.toml` to prevent accidental reuse of the slow types
5. Profile to identify hot spots before making code changes (see perf-profiling)
6. Benchmark each change individually to verify it has the expected effect

## To Configure Clippy for Performance Enforcement:
1. Run `cargo clippy` to see all default lints including perf lints
2. Visit the Clippy lint list and filter by the "Perf" group to see all performance lints
3. To disallow specific types, create a `clippy.toml` with entries like:
   ```toml
   disallowed-types = ["std::collections::HashMap", "std::collections::HashSet"]
   ```

# Context & Application

The Rust Performance Book fills a specific niche: practical, proven Rust optimization techniques backed by real-world evidence. It is not a general-purpose profiling guide, and it acknowledges its bias toward compiler development. The book is deliberately terse, favoring breadth over depth, linking to external resources for deeper treatment.

The emphasis on benchmarking-before-and-after is a recurring theme throughout the book. Tiny changes in memory layout can cause ephemeral performance fluctuations, so metrics with lower variance (instruction counts, cycles) may be more reliable than wall-time.

Clippy serves as the automated first pass -- any pattern Clippy can detect is excluded from the book's manual guidance, making the book complementary to the tool rather than redundant.

# Examples

**Example 1** (Ch. 1, Benchmarking): The book lists concrete benchmarking tools: Criterion and Divan as sophisticated alternatives to built-in bench tests, Hyperfine as a general-purpose tool, Bencher for CI integration, and rustc-perf as an example custom harness.

**Example 2** (Ch. 3, Linting): "The `ptr_arg` style lint suggests changing various container arguments to slices, such as changing `&mut Vec<T>` arguments to `&mut [T]`. The primary motivation here is that a slice gives a more flexible API, but it may also result in faster code due to less indirection."

**Example 3** (Ch. 3, Disallowing Types): To prevent accidental use of standard HashMap/HashSet after switching to FxHashMap:
```toml
disallowed-types = ["std::collections::HashMap", "std::collections::HashSet"]
```

# Relationships

## Builds Upon
- General Rust knowledge (the book targets intermediate/advanced users)

## Enables
- **perf-build-configuration** -- build-level optimizations (the next chapter)
- **perf-profiling** -- identifying hot spots to optimize
- **perf-heap-allocations** -- reducing allocation overhead
- **perf-type-sizes** -- shrinking hot types

## Related
- **perf-hashing** -- one of the types Clippy's `disallowed_types` can enforce
- **perf-stdlib-types** -- additional `disallowed_types` use cases (parking_lot)

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Optimizing code without first establishing benchmarks.
  **Correction**: Always benchmark before and after changes. "Mediocre benchmarking is far better than no benchmarking."

- **Error**: Ignoring Clippy's non-performance lints when optimizing.
  **Correction**: Some non-perf lints (like `ptr_arg`) can improve performance. Review all Clippy suggestions, not just the "Perf" category.

- **Error**: Switching to alternative types (e.g., FxHashMap) but accidentally using standard types in some locations.
  **Correction**: Use Clippy's `disallowed_types` in `clippy.toml` to catch accidental use of the types you've replaced.

# Common Confusions

- **Confusion**: Thinking wall-time is always the best metric for benchmarking.
  **Clarification**: Wall-time suffers from high variance; "tiny changes in memory layout can cause significant but ephemeral performance fluctuations." Instruction counts or cycle counts may provide more stable measurements.

- **Confusion**: Believing that if Clippy passes, there are no performance issues.
  **Clarification**: Clippy catches common patterns automatically, but the majority of performance optimization requires manual profiling, analysis, and code changes. The entire rest of the book covers what Clippy cannot detect.

# Source Reference

Chapter 0: Introduction (book scope, audience, philosophy). Chapter 1: Benchmarking (workloads, tools, metrics, summarization). Chapter 3: Linting (Clippy perf lints, `ptr_arg`, `disallowed_types`).

# Verification Notes

- Definition source: Direct quotations from Ch. 0 (Introduction) and Ch. 3 (Linting)
- Benchmarking tools: Enumerated directly from Ch. 1
- Clippy guidance: Directly from Ch. 3 including `disallowed_types` configuration
- Confidence rationale: HIGH -- all three chapters provide explicit, clear guidance with minimal ambiguity
- Uncertainties: None
