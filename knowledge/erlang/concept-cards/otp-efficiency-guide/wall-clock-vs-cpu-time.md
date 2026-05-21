---
# === CORE IDENTIFICATION ===
concept: Wall-Clock vs CPU Time Measurement
slug: wall-clock-vs-cpu-time

# === CLASSIFICATION ===
category: performance
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Benchmarking"
chapter_number: null
pdf_page: null
section: "Benchmarking using Erlang/OTP functionality"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "wall-clock time vs CPU time"
  - "timer:tc vs statistics(runtime)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - benchmarking-best-practices
extends: []
related:
  - erlperf
  - dbg-profiling
  - profiling-strategy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does wall-clock time measurement relate to CPU time measurement?"
  - "How do I benchmark two implementations to determine which is faster?"
  - "When should I use timer:tc vs statistics(runtime)?"
---

# Quick Definition

Erlang provides two built-in approaches to benchmarking time measurement: `timer:tc/3` for wall-clock time (includes I/O, swapping, and OS activity) and `statistics(runtime)` for CPU time spent in the Erlang VM (more consistent but excludes OS kernel time). The guide recommends using both.

# Core Definition

The Erlang Efficiency Guide distinguishes two measurement types:

**Wall-clock time** (`timer:tc/3`): "The advantage with wall-clock time is that I/O, swapping, and other activities in the operating system kernel are included in the measurements. The disadvantage is that the measurements often vary a lot. Usually it is best to run the benchmark several times and note the shortest time, which is the minimum time that is possible to achieve under the best of circumstances."

**CPU time** (`statistics(runtime)`): "The advantage with CPU time is that the results are more consistent from run to run. The disadvantage is that the time spent in the operating system kernel (such as swapping and I/O) is not included. Therefore, measuring CPU time is misleading if any I/O (file or socket) is involved."

The guide concludes: "It is probably a good idea to do both wall-clock measurements and CPU time measurements."

# Prerequisites

- **Benchmarking Best Practices** -- Understanding the overall benchmarking methodology and its pitfalls.

# Key Properties

1. **Wall-clock time (`timer:tc/3`):**
   - Includes I/O, swapping, and OS kernel activities.
   - Measurements vary a lot between runs.
   - Use the shortest measured time as the best-case result.
   - Best for measuring real-world end-to-end performance.

2. **CPU time (`statistics(runtime)`):**
   - Measures CPU time spent in the Erlang virtual machine.
   - Results are more consistent from run to run.
   - Does not include time in OS kernel (swapping, I/O).
   - Misleading if any I/O (file or socket) is involved.

3. Both measurement types should be used together.
4. Both measurement types can have high granularity, so measurements must last at least several seconds.

# Construction / Recognition

## To Measure Wall-Clock Time:
1. Use `timer:tc(Module, Function, Args)` to time a function call.
2. Run the benchmark multiple times.
3. Record the shortest time as the best achievable result.
4. This is appropriate when I/O or OS activity is part of what you are measuring.

## To Measure CPU Time:
1. Call `statistics(runtime)` before the benchmark to get the starting CPU time.
2. Run the benchmark.
3. Call `statistics(runtime)` after the benchmark.
4. Compute the difference for CPU time consumed.
5. This is appropriate for pure computation without I/O.

## To Choose Between Them:
1. If the code involves I/O (file, socket): wall-clock time is essential; CPU time will be misleading.
2. If the code is pure computation: CPU time gives more consistent results.
3. When in doubt: measure both.

# Context & Application

The distinction between wall-clock time and CPU time is fundamental to benchmarking any system, but the Erlang Efficiency Guide's advice is specifically tailored to the BEAM VM. CPU time as measured by `statistics(runtime)` reflects time spent in the Erlang virtual machine specifically, not just any CPU activity. This makes it a precise measure of computation but blind to external interactions.

The recommendation to use the shortest wall-clock time as the result is a common benchmarking technique: the shortest time represents the run with the least interference from background OS activity, giving the closest approximation to the true execution time.

This concept also connects to `dbg` profiling, where the choice between `timestamp` and `cpu_timestamp` options reflects the same wall-clock vs. CPU time distinction.

# Examples

**Example 1** (benchmarking.md, "Benchmarking using Erlang/OTP functionality"): The source contrasts the two approaches directly:
- `timer:tc/3`: "I/O, swapping, and other activities in the operating system kernel are included in the measurements" but "measurements often vary a lot."
- `statistics(runtime)`: "results are more consistent from run to run" but "measuring CPU time is misleading if any I/O (file or socket) is involved."

**Example 2** (benchmarking.md, "Benchmarking using Erlang/OTP functionality"): For wall-clock measurements, the source recommends: "Usually it is best to run the benchmark several times and note the shortest time, which is the minimum time that is possible to achieve under the best of circumstances."

# Relationships

## Builds Upon
- **benchmarking-best-practices** -- these are the two measurement mechanisms used within the benchmarking methodology

## Enables
- Accurate benchmarking of both I/O-bound and CPU-bound code

## Related
- **erlperf** -- erlperf performs its own time measurements; understanding measurement types helps interpret its results
- **dbg-profiling** -- dbg's `timestamp` vs `cpu_timestamp` options mirror this same distinction
- **profiling-strategy** -- measurement type choice affects profiling tool selection

## Contrasts With
- Wall-clock time and CPU time contrast with each other as described in the card. They are complementary rather than competing with external concepts.

# Common Errors

- **Error**: Using only `statistics(runtime)` (CPU time) when benchmarking code that involves file or socket I/O.
  **Correction**: CPU time is misleading for I/O-bound code because time in the OS kernel is excluded. Use `timer:tc/3` for wall-clock time, or measure both.

- **Error**: Reporting the average wall-clock time instead of the minimum.
  **Correction**: The source recommends noting "the shortest time, which is the minimum time that is possible to achieve under the best of circumstances." Averages include OS interference.

- **Error**: Running benchmarks that complete in sub-second times.
  **Correction**: "The granularity of both measurement types can be high. Therefore, ensure that each individual measurement lasts for at least several seconds."

# Common Confusions

- **Confusion**: Thinking wall-clock time and CPU time should be similar for all code.
  **Clarification**: They diverge significantly when I/O, swapping, or OS scheduling is involved. CPU time excludes all OS kernel activity; wall-clock time includes everything.

- **Confusion**: Believing CPU time is always the better metric because it is more consistent.
  **Clarification**: Consistency does not mean accuracy. If your code involves I/O, CPU time measurements are misleading because they miss the actual time spent waiting for I/O operations.

# Source Reference

Erlang Efficiency Guide, "Benchmarking" chapter, "Benchmarking using Erlang/OTP functionality" section. Describes `timer:tc/3` for wall-clock time and `statistics(runtime)` for CPU time.

# Verification Notes

- Definition: Directly quoted from source for both measurement types.
- Key Properties: All advantages and disadvantages quoted from source.
- Recommendation to use both: Directly quoted from source.
- Confidence: HIGH -- the source provides explicit, detailed descriptions of both measurement types with clear guidance.
- Cross-references: All related slugs correspond to cards in this extraction.
- Uncertainties: None.
