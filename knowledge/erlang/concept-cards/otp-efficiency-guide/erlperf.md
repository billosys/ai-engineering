---
# === CORE IDENTIFICATION ===
concept: erlperf
slug: erlperf

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Benchmarking"
chapter_number: null
pdf_page: null
section: "Using erlperf"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - benchmarking-best-practices
extends: []
related:
  - wall-clock-vs-cpu-time
  - profiling-strategy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is erlperf?"
  - "How do I benchmark two implementations to determine which is faster?"
---

# Quick Definition

`erlperf` is an open-source benchmarking tool for Erlang that makes it simple to compare the performance of different code implementations by reporting queries per second (QPS), average execution time, and relative performance.

# Core Definition

The Erlang Efficiency Guide describes erlperf: "A useful tool for benchmarking is erlperf. It makes it simple to find out which code is faster." The tool is an external package available at `https://github.com/max-au/erlperf` with documentation at `https://hexdocs.pm/erlperf/erlperf.html`.

erlperf produces output with three key columns:
- **Time** -- average execution time per call
- **QPS** -- queries per second (how many calls can be made in one second)
- **Rel** -- relative performance, with 100% indicating the fastest code

# Prerequisites

- **Benchmarking Best Practices** -- Understanding benchmarking methodology and its limitations.

# Key Properties

1. Open-source tool (not part of Erlang/OTP core).
2. Command-line interface for quick comparisons.
3. Reports average execution time per call (Time column).
4. Reports queries per second (QPS column).
5. Reports relative performance with 100% = fastest (Rel column).
6. Supports comparing multiple implementations side by side.
7. Accepts Erlang expressions as command-line arguments.
8. Available on GitHub (max-au/erlperf) and Hex (hexdocs.pm/erlperf).

# Construction / Recognition

## To Use erlperf:
1. Install erlperf from Hex or GitHub.
2. Pass Erlang expressions as command-line arguments, each terminated with a period.
3. Read the output table comparing Time, QPS, and Rel for each expression.
4. The expression with Rel = 100% is the fastest.

## To Interpret Results:
1. **Time**: Lower is faster (average nanoseconds per call).
2. **QPS**: Higher is faster (more calls per second).
3. **Rel**: 100% is the fastest; other percentages show relative speed.

# Context & Application

`erlperf` is the only benchmarking tool explicitly recommended by the Erlang Efficiency Guide. It automates many of the best practices from the benchmarking methodology (process isolation, sufficient duration, multiple runs) and presents results in an immediately interpretable format.

The guide uses erlperf to demonstrate a practical benchmarking investigation: comparing `rand:bytes/1` vs. `crypto:strong_rand_bytes/1` at different byte counts (2, 100, 1000). This example shows how relative performance can change depending on parameters -- `rand:bytes/1` is faster for small byte counts but `crypto:strong_rand_bytes/1` becomes faster at 1000 bytes.

# Examples

**Example 1** (benchmarking.md, "Using erlperf"): Comparing two random byte generators for 2 bytes:
```
% erlperf 'rand:bytes(2).' 'crypto:strong_rand_bytes(2).'
Code                                 ||        QPS       Time   Rel
rand:bytes(2).                        1    7784 Ki     128 ns  100%
crypto:strong_rand_bytes(2).          1    2286 Ki     437 ns   29%
```
`rand:bytes(2)` executes in 128 nanoseconds (7,784,000 calls/second), more than 3x faster than `crypto:strong_rand_bytes(2)` at 437 nanoseconds.

**Example 2** (benchmarking.md, "Using erlperf"): The same comparison at 100 bytes:
```
% erlperf 'rand:bytes(100).' 'crypto:strong_rand_bytes(100).'
Code                                   ||        QPS       Time   Rel
rand:bytes(100).                        1    2124 Ki     470 ns  100%
crypto:strong_rand_bytes(100).          1    1915 Ki     522 ns   90%
```
The gap narrows -- `crypto:strong_rand_bytes/1` is now at 90% relative performance.

**Example 3** (benchmarking.md, "Using erlperf"): At 1000 bytes, the results reverse:
```
% erlperf 'rand:bytes(1000).' 'crypto:strong_rand_bytes(1000).'
Code                                    ||        QPS       Time   Rel
crypto:strong_rand_bytes(1000).          1    1518 Ki     658 ns  100%
rand:bytes(1000).                        1     284 Ki    3521 ns   19%
```
`crypto:strong_rand_bytes(1000)` is now the fastest, demonstrating that performance comparisons are parameter-dependent.

# Relationships

## Builds Upon
- **benchmarking-best-practices** -- erlperf implements benchmarking best practices in a convenient tool

## Enables
- Quick performance comparison of alternative implementations

## Related
- **wall-clock-vs-cpu-time** -- erlperf's Time column represents a specific measurement type
- **profiling-strategy** -- benchmarking with erlperf can validate optimization hypotheses from profiling

## Contrasts With
- No direct contrasts in source. erlperf is the only dedicated benchmarking tool mentioned.

# Common Errors

- **Error**: Drawing conclusions from a single erlperf run with a single parameter value.
  **Correction**: The source's example shows that relative performance can change dramatically with different parameters (2 bytes vs. 1000 bytes). Test across the parameter range relevant to your use case.

- **Error**: Assuming erlperf's Rel percentage means one function is always that much faster.
  **Correction**: Relative performance depends on the specific inputs, system load, and hardware. The benchmarking chapter warns that results are not portable across architectures.

# Common Confusions

- **Confusion**: Thinking erlperf is part of Erlang/OTP core.
  **Clarification**: erlperf is an external open-source tool available on GitHub and Hex. It is recommended by the official documentation but must be installed separately.

- **Confusion**: Thinking the `||` column in erlperf output is related to results.
  **Clarification**: The `||` column shows the number of parallel processes (concurrency level) used for the benchmark, defaulting to 1.

# Source Reference

Erlang Efficiency Guide, "Benchmarking" chapter, "Using erlperf" section. Three worked examples comparing `rand:bytes/1` and `crypto:strong_rand_bytes/1` at different byte counts.

# Verification Notes

- Definition: Directly quoted from source.
- Examples: All three examples are directly from the source with exact output.
- Key Properties: Derived from source description and example output.
- Confidence: HIGH -- the source provides detailed examples with exact command-line usage and output.
- Cross-references: benchmarking-best-practices, wall-clock-vs-cpu-time slugs correspond to cards in this extraction.
- Uncertainties: None.
