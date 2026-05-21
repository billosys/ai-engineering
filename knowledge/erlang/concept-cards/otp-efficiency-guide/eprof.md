---
# === CORE IDENTIFICATION ===
concept: eprof
slug: eprof

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Profiling"
chapter_number: null
pdf_page: null
section: "eprof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - fprof
  - cprof
  - tprof
  - profiling-analysis
contrasts_with:
  - fprof
  - cprof

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does fprof compare to eprof and cprof?"
  - "How do I profile an Erlang application to find performance bottlenecks?"
---

# Quick Definition

`eprof` is an Erlang/OTP profiling tool based on `trace_info` BIFs that shows how much time each process uses and in which function calls that time is spent. It displays time as both percentage of total and absolute values, with a small performance impact.

# Core Definition

The Erlang Efficiency Guide describes eprof: "`eprof` is based on the Erlang `trace_info` BIFs. `eprof` shows how much time has been used by each process, and in which function calls this time has been spent. Time is shown as a percentage of total time and absolute time."

# Prerequisites

- **Profiling Strategy** -- Understanding the profiling approach and when to use eprof vs. other tools.

# Key Properties

1. Based on the Erlang `trace_info` BIFs.
2. Shows time used by each process.
3. Shows time spent in each function call.
4. Displays time as both percentage of total and absolute time.
5. Results displayed per process/function to screen/file.
6. Produces medium-sized result sets.
7. Causes small slowdown of the profiled program.
8. Records number of calls: Yes.
9. Records only total execution time (not own time separately).
10. Does not record "called by" relationships.
11. Does not record garbage collection information.

# Construction / Recognition

## To Use eprof:
1. Start eprof profiling (see `m:eprof` manual page in Tools).
2. Run the code to be profiled.
3. Stop profiling and analyze results.
4. Examine the per-process and per-function time breakdown.

## To Recognize When eprof Is Appropriate:
1. You need to know which processes and functions consume the most time.
2. You want percentage breakdowns of time usage.
3. You need lower overhead than fprof provides.
4. You do not need caller-callee relationships or garbage collection details.

# Context & Application

`eprof` sits between `fprof` and `cprof` in terms of detail vs. overhead. It provides timing information (unlike `cprof`) without the significant slowdown of `fprof`. The percentage-based output makes it particularly useful for quickly identifying which functions dominate execution time. It is suitable for use in test environments and can tolerate being used on moderately loaded systems due to its small performance impact.

# Examples

**Example 1** (profiling.md, "Tool Summary"): The source provides a comparison table showing eprof's characteristics:
- Results: Per process/function to screen/file
- Size of Result: Medium
- Effects on Program Execution Time: Small slowdown
- Records Number of Calls: Yes
- Records Execution Time: Only total
- Records Called by: No
- Records Garbage Collection: No

# Relationships

## Builds Upon
- **profiling-strategy** -- eprof is one tool in the profiling strategy toolkit

## Enables
- **profiling-analysis** -- eprof results are input to profiling analysis

## Related
- **tprof** -- another tracing-based profiler
- **dbg-profiling** -- another approach to timing function calls

## Contrasts With
- **fprof** -- fprof records both own and total time, caller-callee relationships, and GC info, but causes significant slowdown and produces large results
- **cprof** -- cprof only counts calls (no timing) but has even lower overhead

# Common Errors

- **Error**: Expecting eprof to show which functions called which (caller-callee chains).
  **Correction**: eprof does not record "called by" information; use fprof if you need call chain details.

- **Error**: Expecting separate "own time" and "accumulated time" from eprof.
  **Correction**: eprof records only total execution time, not the distinction between own and accumulated.

# Common Confusions

- **Confusion**: Thinking eprof and fprof provide the same information.
  **Clarification**: eprof provides less detail than fprof (no own time, no caller info, no GC info) but with much lower overhead. The Tool Summary table explicitly contrasts them.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "eprof" subsection under "Tools," plus the "Tool Summary" comparison table.

# Verification Notes

- Definition: Directly quoted from source's eprof subsection.
- Key Properties: Items from text description supplemented by Tool Summary table.
- Confidence: HIGH -- explicitly described with comparison table in source.
- Cross-references: fprof, cprof slugs correspond to cards in this extraction.
- Uncertainties: None.
