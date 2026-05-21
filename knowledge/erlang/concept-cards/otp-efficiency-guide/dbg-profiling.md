---
# === CORE IDENTIFICATION ===
concept: dbg Profiling
slug: dbg-profiling

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
section: "dbg"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dbg tracing for profiling"
  - "dbg timestamp profiling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - fprof
  - eprof
  - tprof
  - large-system-profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "How can I time function calls in a heavily loaded live system?"
---

# Quick Definition

`dbg` is the generic Erlang tracing frontend that can be used as a precision profiling instrument by employing the `timestamp` or `cpu_timestamp` options to measure how long specific function calls take for a specific process.

# Core Definition

The Erlang Efficiency Guide describes dbg's profiling use: "`dbg` is a generic Erlang trace tool. By using the `timestamp` or `cpu_timestamp` options it can be used as a precision instrument to profile how long a function call takes for a specific process. This can be very useful when trying to understand where time is spent in a heavily loaded system as it is possible to limit the scope of what is profiled to be very small."

The introductory section adds: "`dbg` is the generic Erlang tracing frontend. By using the `timestamp` or `cpu_timestamp` options it can be used to time how long function calls in a live system take."

# Prerequisites

- **Profiling Strategy** -- Understanding when precision per-process timing is the right approach.

# Key Properties

1. Generic Erlang trace tool repurposed for profiling.
2. Uses `timestamp` option for wall-clock timing.
3. Uses `cpu_timestamp` option for CPU time timing.
4. Can target a specific process for profiling.
5. Scope can be limited to very small portions of the system.
6. Useful for heavily loaded systems where broad profiling tools would add too much overhead.
7. Functions as a "precision instrument" for targeted profiling.

# Construction / Recognition

## To Use dbg for Profiling:
1. Identify the specific process and function(s) to profile.
2. Set up dbg tracing with `timestamp` or `cpu_timestamp` option.
3. Observe the timestamps in trace output to calculate function call duration.
4. Analyze the time differences between function entry and return.

## To Recognize When dbg Profiling Is Appropriate:
1. You need to profile a specific process in a heavily loaded system.
2. You want minimal impact on the rest of the system.
3. You need precision timing for specific function calls (not broad system-wide profiling).
4. You are working in a live/production system where fprof's overhead is unacceptable.

# Context & Application

`dbg` is not primarily a profiling tool -- it is a generic tracing frontend. However, its ability to attach timestamps to trace events makes it a valuable precision profiling instrument. The key advantage is its narrow scope: unlike fprof or eprof, which profile broadly, dbg can be aimed at a single process and a small set of functions. This makes it ideal for investigating specific bottlenecks in production systems where broad profiling would either be too slow or generate too much data.

The choice between `timestamp` and `cpu_timestamp` mirrors the broader wall-clock vs. CPU time distinction covered in the benchmarking chapter.

# Examples

**Example 1** (profiling.md, "dbg"): The source describes dbg as "a precision instrument to profile how long a function call takes for a specific process," emphasizing its value "when trying to understand where time is spent in a heavily loaded system as it is possible to limit the scope of what is profiled to be very small."

# Relationships

## Builds Upon
- **profiling-strategy** -- dbg profiling is one approach within the broader profiling strategy

## Enables
- Targeted profiling of specific functions in live systems

## Related
- **fprof** -- provides broader profiling with more detail but much higher overhead
- **eprof** -- provides per-process timing but with broader scope
- **tprof** -- tracing profiler with multiple measurement modes
- **wall-clock-vs-cpu-time** -- dbg's `timestamp` vs `cpu_timestamp` options reflect this distinction
- **large-system-profiling** -- dbg is useful for profiling within large systems

## Contrasts With
- No direct contrasts provided in source, though dbg's precision/narrow-scope nature implicitly contrasts with fprof's broad/heavy approach.

# Common Errors

- **Error**: Using dbg to profile an entire system rather than targeted functions.
  **Correction**: dbg is most useful as a precision instrument for specific processes and functions; use fprof or eprof for broader profiling.

- **Error**: Forgetting to use `timestamp` or `cpu_timestamp` options.
  **Correction**: Without these options, dbg traces events but does not record timing, making it useless for profiling.

# Common Confusions

- **Confusion**: Thinking dbg is only a debugging tool, not a profiling tool.
  **Clarification**: The Erlang Efficiency Guide explicitly describes dbg as usable for profiling via its timestamp options, making it a "precision instrument" for timing function calls.

- **Confusion**: Conflating `timestamp` and `cpu_timestamp`.
  **Clarification**: `timestamp` records wall-clock time (including I/O waits, OS scheduling); `cpu_timestamp` records CPU time (only computation, no I/O).

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "dbg" subsection under "Tools," plus the introductory tool listing. See `m:dbg` manual page in Runtime Tools for full usage details.

# Verification Notes

- Definition: Directly quoted from both the introductory listing and the dbg subsection.
- Key Properties: All derived from the two source passages about dbg.
- Confidence: HIGH -- explicitly described with clear use case in the official documentation.
- Cross-references: Related tool slugs correspond to cards in this extraction.
- Uncertainties: None.
