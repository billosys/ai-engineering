---
# === CORE IDENTIFICATION ===
concept: Profiling
slug: profiling

# === CLASSIFICATION ===
category: performance
subcategory: profiling
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.2. Profiling Erlang code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "profiling"
  - "code profiling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - performance-baseline
extends: []
related:
  - cprof
  - fprof
  - performance-tuning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is profiling?"
  - "What is the difference between CPU time and wall-clock time?"
  - "What kinds of statistics can profilers gather?"
---

# Quick Definition

Profiling is gathering statistics about code as it runs and associating that data with points in the code, most often to find where the most time is spent.

# Core Definition

In the general sense, profiling means gathering statistics about code as it is running and associating the data with corresponding points in the code. The most typical form measures where the most time is being spent — those are the main bottlenecks. Time can be measured as CPU time (how much real work the program does) or wall-clock time (how long you wait for it to finish): high wall-clock with low CPU time means the code is mostly waiting (usually on I/O), while high CPU time may indicate a bad algorithm. Some simple profilers only count how many times each function is called or each line executed, as an approximation of CPU time. Profilers may also measure memory usage, I/O usage, and the number of processes ready to run (Chapter 14, Section 14.2).

# Prerequisites

- **Establishing a baseline** — Profiling follows baselining when measurements show goals are unmet.

# Key Properties

1. Profiling associates runtime statistics with specific points in the code.
2. The most common measurement is where time is spent — i.e. bottlenecks.
3. CPU time reflects real work done; wall-clock time reflects elapsed waiting.
4. High wall-clock + low CPU time → the code is waiting (often on disk or network I/O).
5. High CPU time → possibly a bad algorithm (quadratic or exponential behaviour).
6. Simple profilers count calls or executed lines as a CPU-time approximation.
7. Erlang/OTP profiling tools include `cprof`, `fprof`, `cover` (coverage), `instrument` (memory), and `percept` (concurrency).

# Construction / Recognition

## To Identify/Recognize:
1. A point where few or no other processes are ready to run can be a synchronization bottleneck limiting parallelism.
2. Compare CPU vs. wall-clock time to tell "working" from "waiting".

## To Construct/Create (a profiling session):
1. Choose a tool fitting the metric you need (`cprof` for call counts, `fprof` for execution time).
2. Start the tool, run the code, stop the tool, analyze the results.

# Context & Application

- **Typical contexts**: Step 3 of the performance-tuning loop, locating bottlenecks.
- **Common applications**: The book uses the standard-library `cprof` and `fprof` tools to profile a `profile_ex` module.
- **Historical/stylistic notes**: With practice some pitfalls can be spotted by reading code, but tracking down real bottlenecks usually still requires profiling.

# Examples

**Example 1** (Section 14.2): The book lists `cover` for code coverage, `instrument` for memory-usage analysis, and `percept` for concurrency profiling alongside the two time profilers.

**Example 2** (Section 14.2): A program point where few other processes are ready to execute is identified as a possible synchronization bottleneck.

# Relationships

## Related
- **cprof** — A standard-library profiler that counts function calls.
- **fprof** — A standard-library profiler that measures execution time.
- **Performance tuning methodology** — Profiling is the locating step of the tuning loop.

# Common Errors

- **Error**: Profiling huge chunks of code for a long time with a heavy profiler.
  **Correction**: Limit scope; `fprof` in particular can accumulate gigabytes of trace data.

# Common Confusions

- **Confusion**: Treating wall-clock time and CPU time as the same thing.
  **Clarification**: Wall-clock includes time spent waiting; CPU time counts only active computation.

# Source Reference

Chapter 14: Optimization and performance, Section 14.2 "Profiling Erlang code."

# Verification Notes

- Definition source: Direct adaptation of the Section 14.2 introduction.
- Confidence rationale: HIGH — profiling is explicitly defined and discussed.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
