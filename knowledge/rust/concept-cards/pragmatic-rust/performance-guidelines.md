---
concept: Performance Guidelines
slug: performance-guidelines
category: performance
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "06-performance"
chapter_number: 6
pdf_page: null
section: "Performance Guidelines"
extraction_confidence: high
aliases:
  - "hot path optimization"
  - "throughput optimization"
  - "yield points"
  - "async performance"
  - "COGS optimization"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - safety-guidelines
  - library-ux-guidelines
contrasts_with: []
answers_questions:
  - "How should I identify and optimize hot paths in Rust?"
  - "How do I optimize for throughput in a Rust library?"
  - "When should async tasks yield in Rust?"
  - "How often should yield points occur in CPU-bound async code?"
  - "What are common performance pitfalls in Rust?"
---

# Quick Definition

Performance guidelines covering three areas: identifying, profiling, and optimizing hot paths early with benchmarks (M-HOTPATH); optimizing for throughput measured in items-per-CPU-cycle rather than latency (M-THROUGHPUT); and inserting cooperative yield points in long-running async tasks to avoid starving other tasks (M-YIELD-POINTS).

# Core Definition

The performance guidelines provide a structured approach to writing high-performance Rust. M-HOTPATH requires early identification of whether a crate is performance or COGS relevant, followed by creating benchmarks around hot paths, regularly profiling CPU and allocation behavior, and documenting performance-sensitive areas. M-THROUGHPUT requires optimizing for items-per-CPU-cycle by partitioning work into chunks, letting threads work independently, sleeping/yielding when idle, designing batched APIs, and exploiting CPU cache locality. M-YIELD-POINTS requires that long-running CPU-bound async tasks cooperatively yield at regular intervals via `yield_now().await` to avoid starving concurrent operations in the runtime. (Ch. 6, "Performance Guidelines")

# Prerequisites

- **pragmatic-rust-overview** -- understanding the overall guideline framework provides context for when performance guidelines apply

# Key Properties

1. **M-HOTPATH**: Early in development, determine if a crate is performance or COGS relevant; if so, create benchmarks (criterion or divan), run profilers regularly, and document hot spots
2. Benchmarks should measure both elapsed wall time and CPU time across all threads (requires manual work beyond standard benchmark tools)
3. Enable debug symbols for benchmarks: `[profile.bench] debug = 1` in Cargo.toml
4. Common "language related" performance issues: frequent re-allocations, cloned/growing/format!-assembled strings, short-lived allocations, memory copy from cloning Strings and collections, repeated re-hashing, and using Rust's default hasher where collision resistance is not needed
5. Anecdotally, ~15% gains from addressing String problems on hot paths, up to ~50% in highly optimized versions
6. **M-THROUGHPUT**: Key metric is items per CPU cycle, not latency; partition work into chunks, let threads work independently, use batched APIs, exploit CPU cache locality
7. Do not: hot spin for individual items, process individual items when batching is possible, use work stealing to balance individual items
8. Shared state should only be used if sharing cost is less than re-computation cost
9. **M-YIELD-POINTS**: CPU-bound async tasks should yield at regular intervals; tasks with intermixed I/O naturally yield at `.await` points
10. Recommended yield frequency: 10-100 microseconds of CPU-bound work between yield points, balancing switching cost (~100's of ns) against starvation
11. For unpredictable operations, use runtime APIs like `has_budget_remaining()` to query available budget

# Construction / Recognition

## To Apply M-HOTPATH:
1. Assess if the crate is performance/COGS relevant early in development
2. Create benchmarks using criterion or divan around identified hot paths
3. Enable debug symbols for benchmarks in Cargo.toml
4. Run profilers (Intel VTune, Superluminal) regularly for CPU and allocation insights
5. Document or share performance-sensitive areas with the team

## To Apply M-THROUGHPUT:
1. Design APIs for batched operations rather than single-item processing
2. Partition work ahead of time for independent thread processing
3. Sleep or yield when no work is present rather than hot spinning
4. Measure items-per-CPU-cycle as the primary throughput metric

## To Apply M-YIELD-POINTS:
1. Identify CPU-bound async code without intermixed I/O
2. Insert `yield_now().await` at regular intervals (every 10-100 microseconds of work)
3. For unpredictable workloads, use `has_budget_remaining()` runtime APIs

# Context & Application

These guidelines target libraries running at scale where COGS (cost of goods sold) savings matter. The throughput focus reflects a server-side perspective where scaling for throughput is cheaper than reducing latency, and empty CPU cycles from hot spinning or single-item processing waste resources. The yield point guideline is specific to cooperative async runtimes (like Tokio) where long-running tasks block the executor thread. The 10-100 microsecond recommendation is derived from the assumption that task switching takes ~100ns plus cache miss overhead, so work between yields should be long enough that switching cost is less than 1%.

# Examples

**Example 1** (Ch. 6, M-HOTPATH -- Common issues): The source lists specific performance problems: "frequent re-allocations, esp. cloned, growing or `format!` assembled strings; short lived allocations over bump allocations; memory copy overhead from cloning Strings and collections; repeated re-hashing of equal data structures; use of Rust's default hasher where collision resistance wasn't an issue."

**Example 2** (Ch. 6, M-THROUGHPUT -- Do and Don't lists): Do: partition chunks, let threads work independently, sleep/yield when idle, design batched APIs, exploit CPU caches. Don't: hot spin for individual items, process individually when batching is possible, use work stealing to balance individual items.

**Example 3** (Ch. 6, M-YIELD-POINTS -- CPU-bound with yield): An async function decompresses items from a zip file in a loop: `for i in items { decompress(i); yield_now().await; }`. Without the yield, decompressing many items would starve other async tasks on the same executor thread.

**Example 4** (Ch. 6, M-YIELD-POINTS -- Natural preemption): An async function processing items with I/O: `for i in items { read_item(i).await; }`. The `.await` on I/O naturally provides preemption points, so no explicit yield is needed.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- the performance guidelines operate within the overall guideline severity framework

## Enables
- Cost-effective server-side Rust applications through throughput optimization
- Responsive async systems through cooperative yielding

## Related
- **safety-guidelines** -- performance is one of the three valid reasons for using `unsafe` code (M-UNSAFE)
- **library-ux-guidelines** -- batched API design connects to the UX guidelines' emphasis on ergonomic APIs

## Contrasts With
- Latency-first optimization strategies that accept empty cycles for faster individual response
- Preemptive threading models where yield points are unnecessary

# Common Errors

- **Error**: Hot spinning in a loop to receive individual items faster from a channel.
  **Correction**: Use batched receives or sleep/yield when no work is available. Hot spinning wastes CPU cycles that could process other tasks.

- **Error**: Writing CPU-bound async code that runs for milliseconds without yielding, causing other tasks to stall.
  **Correction**: Insert `yield_now().await` every 10-100 microseconds of CPU-bound work. For unpredictable durations, use `has_budget_remaining()`.

- **Error**: Optimizing code before profiling, leading to micro-optimizations in cold paths.
  **Correction**: Profile first to identify actual hot paths, then benchmark and optimize those specific areas.

# Common Confusions

- **Confusion**: Thinking yield points are needed in all async code.
  **Clarification**: Async code that performs I/O operations naturally yields at `.await` points. Explicit `yield_now().await` is only needed for CPU-bound computation without intermixed I/O.

- **Confusion**: Believing the default Rust hasher (SipHash) should always be replaced.
  **Clarification**: The default hasher provides collision resistance, which is important for preventing hash-flooding DoS attacks. It should only be replaced when collision resistance is not needed and hashing is on the hot path.

- **Confusion**: Thinking throughput and latency optimization are always at odds.
  **Clarification**: The source says "this does not mean to neglect latency -- after all you can scale for throughput, but not for latency." The guideline specifically targets avoiding empty cycles, not accepting worse latency.

# Source Reference

Chapter 6: Performance Guidelines. Contains three guidelines: M-HOTPATH (v0.1), M-THROUGHPUT (v0.1), M-YIELD-POINTS (v0.2). M-HOTPATH includes tool recommendations (criterion, divan, Intel VTune, Superluminal) and anecdotal performance gains. M-THROUGHPUT provides do/don't lists for throughput optimization. M-YIELD-POINTS includes code examples for both natural and explicit yielding, plus a detailed analysis of yield frequency. References: cheats.rs Performance Tips section.

# Verification Notes

- Definition source: Direct from section headings and `<why>` tags for each guideline
- Key Properties: Derived from do/don't lists, code examples, and quantitative recommendations
- Confidence rationale: HIGH -- all three guidelines have clear definitions, concrete recommendations, and code examples
- Uncertainties: The 10-100 microsecond yield interval is described as "a good starting point," not a hard rule
- Cross-reference status: pragmatic-rust-overview, safety-guidelines are from sibling extraction sets
