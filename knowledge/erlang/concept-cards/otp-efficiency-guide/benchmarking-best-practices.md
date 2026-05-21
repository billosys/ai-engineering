---
# === CORE IDENTIFICATION ===
concept: Benchmarking Best Practices
slug: benchmarking-best-practices

# === CLASSIFICATION ===
category: performance
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Benchmarking"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "benchmarking methodology"
  - "performance benchmarking"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - profiling-strategy
  - profiling-analysis
  - erlperf
  - wall-clock-vs-cpu-time
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I benchmark two implementations to determine which is faster?"
  - "What pitfalls should I avoid when benchmarking Erlang code?"
---

# Quick Definition

Benchmarking best practices in Erlang encompass the methodology for comparing implementation performance, including accounting for OS background tasks, cache effects, multi-core variability, process isolation, measurement granularity, and architecture-specific results.

# Core Definition

The Erlang Efficiency Guide defines the purpose of benchmarking: "The main purpose of benchmarking is to find out which implementation of a given algorithm or function is the fastest." The guide then immediately tempers expectations: "Benchmarking is far from an exact science. Today's operating systems generally run background tasks that are difficult to turn off. Caches and multiple CPU cores do not facilitate benchmarking. It would be best to run UNIX computers in single-user mode when benchmarking, but that is inconvenient to say the least for casual testing."

The guide provides three specific pieces of advice:
1. "The granularity of both measurement types can be high. Therefore, ensure that each individual measurement lasts for at least several seconds."
2. "To make the test fair, each new test run is to run in its own, newly created Erlang process. Otherwise, if all tests run in the same process, the later tests start out with larger heap sizes and therefore probably do fewer garbage collections. Also consider restarting the Erlang emulator between each test."
3. "Do not assume that the fastest implementation of a given algorithm on computer architecture X is also the fastest on computer architecture Y."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Purpose: determine which implementation of a given algorithm is fastest.
2. Not an exact science -- OS background tasks, caches, and multi-core effects introduce variability.
3. Each measurement must last at least several seconds to overcome granularity issues.
4. Each test must run in its own newly created Erlang process for fairness.
5. Running tests in the same process is unfair because later tests have larger heaps and fewer GCs.
6. Consider restarting the Erlang emulator between tests.
7. Results are architecture-specific -- do not assume portability across CPU architectures.
8. Wall-clock time and CPU time are both useful but measure different things.
9. Use the shortest measured time as the best-case result for wall-clock measurements.

# Construction / Recognition

## To Benchmark Correctly:
1. Identify the implementations to compare.
2. Design each test to run for at least several seconds.
3. Run each test in its own newly created Erlang process.
4. Consider restarting the emulator between tests.
5. Measure both wall-clock time (`timer:tc/3`) and CPU time (`statistics(runtime)`).
6. Run multiple iterations and note the shortest wall-clock time.
7. Do not generalize results across different CPU architectures.
8. Use tools like `erlperf` for convenient comparison.

## To Recognize Invalid Benchmarks:
1. Tests run for only milliseconds (granularity issues).
2. Multiple tests run in the same process (heap size contamination).
3. Results assumed to hold across different hardware.
4. Only one measurement type used (wall-clock or CPU time but not both).

# Context & Application

Benchmarking connects directly to the profiling workflow: after profiling identifies bottlenecks and analysis produces optimization hypotheses, benchmarking validates whether the proposed changes actually improve performance. The Profiling chapter explicitly says "Some benchmarks might be needed to back up your theory and to avoid making things slower if your theory is wrong."

The guide's emphasis on process isolation reflects Erlang-specific concerns: the BEAM virtual machine's per-process garbage collection means that heap size accumulates across test runs within a single process, creating an unfair advantage for later tests (they do fewer garbage collections). This is an Erlang-specific pitfall that generic benchmarking advice would not cover.

# Examples

**Example 1** (benchmarking.md, "Some final advice"): The source explains the process isolation requirement: "To make the test fair, each new test run is to run in its own, newly created Erlang process. Otherwise, if all tests run in the same process, the later tests start out with larger heap sizes and therefore probably do fewer garbage collections."

**Example 2** (benchmarking.md, "Some final advice"): The source warns about architecture specificity: "Do not assume that the fastest implementation of a given algorithm on computer architecture X is also the fastest on computer architecture Y."

# Relationships

## Builds Upon
- No prerequisites -- this is a foundational methodology concept.

## Enables
- Validation of optimization hypotheses from profiling analysis.
- Informed decision-making about which implementation to use.

## Related
- **profiling-strategy** -- profiling identifies what to benchmark
- **profiling-analysis** -- analysis produces hypotheses that benchmarking validates
- **erlperf** -- a tool that implements many benchmarking best practices automatically
- **wall-clock-vs-cpu-time** -- the two measurement types used in benchmarking

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Running all benchmark tests in a single Erlang process.
  **Correction**: Create a new process for each test run. Later tests in the same process benefit from larger heaps and fewer garbage collections, skewing results.

- **Error**: Running benchmarks that complete in milliseconds.
  **Correction**: Ensure each measurement lasts at least several seconds to overcome measurement granularity.

- **Error**: Assuming benchmark results from one CPU architecture apply to another.
  **Correction**: The fastest implementation on architecture X may not be fastest on architecture Y. Re-benchmark on the target architecture.

# Common Confusions

- **Confusion**: Thinking benchmarking produces exact, reproducible results.
  **Clarification**: The source explicitly states "Benchmarking is far from an exact science" due to OS background tasks, caches, and multi-core effects.

- **Confusion**: Believing that wall-clock time is always the best metric.
  **Clarification**: Both wall-clock time and CPU time are useful. Wall-clock includes I/O and OS activity; CPU time is more consistent but misses I/O. The guide recommends doing both.

# Source Reference

Erlang Efficiency Guide, "Benchmarking" chapter, introductory text and "Some final advice" section.

# Verification Notes

- Definition: Directly quoted from the opening of the Benchmarking chapter.
- Key Properties: All three pieces of "final advice" directly quoted from source.
- Confidence: HIGH -- the source provides explicit, structured guidance.
- Cross-references: All related slugs correspond to cards in this extraction.
- Uncertainties: None.
