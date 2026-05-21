---
# === CORE IDENTIFICATION ===
concept: cprof
slug: cprof

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
section: "cprof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "call count profiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - fprof
  - eprof
  - tprof
  - profiling-analysis
contrasts_with:
  - fprof
  - eprof

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does fprof compare to eprof and cprof?"
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "Which profiling tool has the lowest overhead?"
---

# Quick Definition

`cprof` is an Erlang/OTP profiling tool that counts how many times each function is called on a per-module basis. It has low performance degradation and does not require recompilation, sitting between `fprof` and `cover` in terms of features.

# Core Definition

The Erlang Efficiency Guide describes cprof: "`cprof` is something in between `fprof` and `cover` regarding features. It counts how many times each function is called when the program is run, on a per module basis. `cprof` has a low performance degradation effect (compared with `fprof`) and does not need to recompile any modules to profile (compared with `cover`)."

# Prerequisites

- **Profiling Strategy** -- Understanding the profiling approach and when call-count profiling is sufficient.

# Key Properties

1. Counts how many times each function is called.
2. Results reported on a per-module basis.
3. Low performance degradation effect (compared with fprof).
4. Does not need to recompile any modules to profile (compared with cover).
5. Produces small result sets.
6. Causes small slowdown.
7. Does not record execution time.
8. Does not record "called by" relationships.
9. Does not record garbage collection information.
10. Results reported per module to caller.

# Construction / Recognition

## To Use cprof:
1. Start cprof profiling (see `m:cprof` manual page in Tools).
2. Run the code to be profiled.
3. Stop profiling and retrieve call counts.
4. Examine which functions are called most frequently, per module.

## To Recognize When cprof Is Appropriate:
1. You only need to know how many times functions are called (not how long they take).
2. You want minimal performance impact on the running system.
3. You cannot recompile modules (which would be needed for `cover`).
4. You want a quick overview of call patterns at the module level.

# Context & Application

`cprof` is the lightest-weight of the three traditional Erlang profilers (fprof, eprof, cprof). By measuring only call counts without timing, it imposes minimal overhead on the running system. This makes it suitable for initial investigation in production-adjacent environments where even eprof's small slowdown might be unacceptable.

Call counts can reveal "hot" functions -- those called an unexpectedly high number of times -- which may indicate algorithmic issues, redundant computations, or tight loops worth optimizing.

# Examples

**Example 1** (profiling.md, "Tool Summary"): The source provides a comparison table showing cprof's characteristics:
- Results: Per module to caller
- Size of Result: Small
- Effects on Program Execution Time: Small slowdown
- Records Number of Calls: Yes
- Records Execution Time: No
- Records Called by: No
- Records Garbage Collection: No

# Relationships

## Builds Upon
- **profiling-strategy** -- cprof is one tool in the profiling strategy toolkit

## Enables
- **profiling-analysis** -- call count data informs analysis of hot functions

## Related
- **tprof** -- tprof can also measure call counts along with time and heap allocations

## Contrasts With
- **fprof** -- fprof records detailed timing and call chains but causes significant slowdown and produces large results
- **eprof** -- eprof records total execution time but not own time; higher overhead than cprof but provides timing data

# Common Errors

- **Error**: Expecting cprof to tell you how long functions take to execute.
  **Correction**: cprof only counts calls; use eprof or fprof for timing information.

- **Error**: Confusing cprof with cover.
  **Correction**: cover requires module recompilation; cprof does not. They serve different purposes (cprof for call counts, cover for code coverage).

# Common Confusions

- **Confusion**: Thinking that the most-called function is necessarily the bottleneck.
  **Clarification**: A function called many times may be fast; a function called fewer times may be slow. cprof data should be combined with timing data from eprof or fprof for a complete picture.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "cprof" subsection under "Tools," plus the "Tool Summary" comparison table.

# Verification Notes

- Definition: Directly quoted from source's cprof subsection.
- Key Properties: From text description and Tool Summary table.
- Confidence: HIGH -- explicitly described with comparison table in source.
- Cross-references: fprof, eprof slugs correspond to cards in this extraction.
- Uncertainties: None.
