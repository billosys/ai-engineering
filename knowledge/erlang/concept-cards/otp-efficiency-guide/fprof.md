---
# === CORE IDENTIFICATION ===
concept: fprof
slug: fprof

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
section: "fprof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "file-based profiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - eprof
  - cprof
  - tprof
  - profiling-analysis
contrasts_with:
  - eprof
  - cprof

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does fprof compare to eprof and cprof?"
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "Which profiling tool gives the most detailed information?"
---

# Quick Definition

`fprof` is an Erlang/OTP profiling tool that measures execution time per function (both own time and accumulated time including called functions), displayed per process. It provides the most detailed profiling information but significantly slows down the profiled program.

# Core Definition

The Erlang Efficiency Guide describes fprof as follows: "`fprof` measures the execution time for each function, both own time, that is, how much time a function has used for its own execution, and accumulated time, that is, including called functions. The values are displayed per process. You also get to know how many times each function has been called." The guide further notes that "`fprof` is based on trace to file to minimize runtime performance impact" and that "using `fprof` is just a matter of calling a few library functions."

The introduction to the Profiling chapter states: "`fprof` provides the most detailed information about where the program time is spent, but it significantly slows down the program it profiles."

# Prerequisites

- **Profiling Strategy** -- Understanding why profiling is necessary and how to choose the right tool is essential before using fprof.

# Key Properties

1. Measures both "own time" (time in the function itself) and "accumulated time" (including called functions).
2. Results displayed per process.
3. Records the number of times each function is called.
4. Records execution time (total and own).
5. Records "called by" relationships between functions.
6. Records garbage collection information.
7. Based on trace to file to minimize runtime performance impact.
8. Causes significant slowdown of the profiled program.
9. Produces large result sets.

# Construction / Recognition

## To Use fprof:
1. Call fprof library functions to set up profiling (see `m:fprof` manual page).
2. Run the code to be profiled.
3. Stop profiling.
4. Analyze the trace file to produce a report.
5. Examine own time and accumulated time per function per process.

## To Recognize When fprof Is Appropriate:
1. You need detailed per-function timing (both own and accumulated time).
2. You need to understand caller-callee relationships.
3. You need garbage collection information.
4. The program can tolerate significant slowdown during profiling.

# Context & Application

`fprof` is the most comprehensive built-in profiling tool in Erlang/OTP. It is best suited for development and testing environments where the significant runtime slowdown is acceptable. For production or heavily loaded systems, `dbg` with timestamps or `tprof` may be more appropriate due to their lower overhead.

The trace-to-file mechanism means fprof collects data first and analyzes later, which helps reduce (but does not eliminate) the performance impact during collection.

**External tools complement fprof:**
- `erlgrind` can visualize fprof data in kcachegrind
- `eflame` provides flamegraph output as an alternative to fprof

# Examples

**Example 1** (profiling.md, "Tool Summary"): The source provides a comparison table showing fprof's characteristics:
- Results: Per process to screen/file
- Size of Result: Large
- Effects on Program Execution Time: Significant slowdown
- Records Number of Calls: Yes
- Records Execution Time: Total and own
- Records Called by: Yes
- Records Garbage Collection: Yes

# Relationships

## Builds Upon
- **profiling-strategy** -- fprof is one tool in the profiling strategy toolkit

## Enables
- **profiling-analysis** -- fprof results are input to profiling analysis

## Related
- **tprof** -- another tracing-based profiler with different trade-offs
- **dbg-profiling** -- generic tracing that can also time function calls

## Contrasts With
- **eprof** -- eprof shows only total time (not own time), produces medium-sized results, and causes less slowdown
- **cprof** -- cprof counts calls only (no timing), produces small results, and causes minimal slowdown

# Common Errors

- **Error**: Running fprof on a production system.
  **Correction**: fprof causes significant slowdown; use lower-overhead tools like `dbg` or `tprof` for production profiling.

- **Error**: Profiling the entire application with fprof when only one module is suspect.
  **Correction**: Focus profiling on specific processes or code paths to limit the size of results and reduce overhead.

# Common Confusions

- **Confusion**: Thinking fprof's "own time" includes time in called functions.
  **Clarification**: "Own time" is strictly the time a function uses for its own execution, excluding calls to other functions. "Accumulated time" includes called functions.

- **Confusion**: Believing fprof's overhead will not affect timing measurements.
  **Clarification**: While trace-to-file minimizes impact, fprof still significantly slows the program, so absolute timing values may differ from unproled execution.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "fprof" subsection under "Tools," plus the "Tool Summary" comparison table.

# Verification Notes

- Definition: Directly quoted from source's fprof subsection and introductory tool list.
- Key Properties: Items 1-6 from the Tool Summary table; items 7-9 from the text description.
- Confidence: HIGH -- explicitly defined with detailed characteristics in both text and table form.
- Cross-references: eprof, cprof slugs correspond to planned cards; contrasts derived from the Tool Summary table.
- Uncertainties: None.
