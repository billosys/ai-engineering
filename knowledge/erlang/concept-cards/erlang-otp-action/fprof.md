---
# === CORE IDENTIFICATION ===
concept: fprof (Execution-Time Profiler)
slug: fprof

# === CLASSIFICATION ===
category: performance
subcategory: profiling
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.2.2. Profiling execution time with fprof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fprof"
  - "execution-time profiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling
  - cprof
extends: []
related:
  - cprof
contrasts_with:
  - cprof

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is fprof?"
  - "How do you run an fprof profiling session?"
  - "How do you read fprof's output file?"
---

# Quick Definition

`fprof` is an Erlang/OTP profiler that measures execution time per function, producing a detailed text file showing call counts, accumulated time, and own time, plus suspension and garbage-collection time.

# Core Definition

The `fprof` profiler is perhaps the most valuable of the standard profiling tools: it gives a wealth of useful information in a digestible format and is one of the first tools to bring in when diagnosing performance issues. It supersedes the older, less efficient `eprof`. Both are built on Erlang's tracing functionality, so neither needs special compilation; but they have much higher overhead than `cprof` and can make code run up to 10 times slower. Running `fprof` involves tracing the code, turning the trace into raw profiling data, and analyzing that into a human-readable file. The analysis file reports, per function, the call count (CNT), accumulated time (ACC, total from start to end) and own time (OWN, time within the function alone), and treats process suspension and garbage collection like extra function calls (Chapter 14, Section 14.2.2).

# Prerequisites

- **Profiling** — `fprof` is a tool for the profiling step of performance tuning.
- **cprof** — The book introduces `cprof` first, then `fprof` for deeper detail.

# Key Properties

1. Measures execution time per function, far more detail than `cprof`.
2. Built on Erlang's tracing; needs no special compilation or debugging information.
3. High overhead — can make code run up to 10x slower; use with care in production.
4. Depends on `dbg` from the `runtime_tools` application; `fprof` itself is in the `tools` application.
5. Three stages: `fprof:trace(start)` ... `fprof:trace(stop)`, then `fprof:profile()`, then `fprof:analyse/1`.
6. The trace file (default `fprof.trace`) is binary; the analysis output is human-readable Erlang terms.
7. Output columns: CNT (call count), ACC (accumulated time), OWN (own time); time is wall-clock by default, switchable with the `cpu_time` option.
8. `ACC` is `undefined` for a process summary; suspension and garbage collection appear as pseudo-function paragraphs.

# Construction / Recognition

## To Construct/Create (an fprof session):
1. Start tracing: `fprof:trace(start)`.
2. Run the code: `profile_ex:run()`.
3. Stop tracing: `fprof:trace(stop)`.
4. Turn the trace into raw data: `fprof:profile()`.
5. Analyze to a file: `fprof:analyse([{dest, "profile.txt"}])`.

## To Identify/Recognize (reading the output):
1. The line in each paragraph ending with `%` is the function the paragraph concerns.
2. Lines above the `%` marker are callers; lines below are functions it called.
3. Start by checking suspension and garbage-collection times before the real functions.

# Context & Application

- **Typical contexts**: Detailed diagnosis of where execution time goes.
- **Common applications**: The book profiles `profile_ex`, accounting for the ~19 µs per fun call that makes `funner` slower than `looper`.
- **Historical/stylistic notes**: The output can be read back with `file:consult/1` since it is plain Erlang terms.

# Examples

**Example 1** (Section 14.2.2): The totals line `[{ totals, 5045, 78.976, 78.929}]` reports 5045 calls, 78.976 ms accumulated, 78.929 ms own time.

**Example 2** (Section 14.2.2): The `funner/2` paragraph shows it was called 1,001 times for 49.047 ms ACC and 20.717 ms OWN; suspension and garbage collection get their own paragraphs.

# Relationships

## Related
- **cprof** — The lighter call-counting profiler used before reaching for `fprof`.

## Contrasts With
- **cprof** — `cprof` only counts calls with ~10% overhead; `fprof` measures time with up to 10x overhead.

# Common Errors

- **Error**: Profiling large code over a long period.
  **Correction**: `fprof` accumulates trace data fast — it can generate gigabytes; limit scope.

- **Error**: Trying to account for every microsecond in the output.
  **Correction**: Wall-clock measurement and OS scheduling cause noise; look at the file as a whole and re-run if numbers look unreasonable.

# Common Confusions

- **Confusion**: Reading the trace file directly.
  **Clarification**: The default `fprof.trace` is binary; `fprof:profile()` and `fprof:analyse/1` produce the readable output.

# Source Reference

Chapter 14: Optimization and performance, Section 14.2.2 "Profiling execution time with fprof," including "Interpreting the output from fprof."

# Verification Notes

- Definition source: Direct adaptation of Section 14.2.2.
- Confidence rationale: HIGH — the tool, workflow, and output format are explicitly described.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
