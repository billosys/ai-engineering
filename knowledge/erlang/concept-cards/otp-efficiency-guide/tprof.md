---
# === CORE IDENTIFICATION ===
concept: tprof
slug: tprof

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
section: "Never Guess About Performance Bottlenecks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "tracing profiler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends: []
related:
  - fprof
  - eprof
  - cprof
  - profiling-analysis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "What profiling tool can measure heap allocations per function call?"
---

# Quick Definition

`tprof` is an Erlang/OTP tracing profiler that can measure call count, call time, or heap allocations per function call. It provides flexible profiling capabilities covering multiple dimensions of function behavior.

# Core Definition

The Erlang Efficiency Guide describes tprof in its introductory tool listing: "`tprof` is a tracing profiler that can measure call count, call time, or heap allocations per function call." This positions tprof as a versatile profiling tool that can operate in multiple measurement modes.

# Prerequisites

- **Profiling Strategy** -- Understanding why profiling is needed and how to select the appropriate measurement mode.

# Key Properties

1. Tracing-based profiler.
2. Can measure call count (how many times a function is called).
3. Can measure call time (how long each function call takes).
4. Can measure heap allocations per function call.
5. Multiple measurement modes provide flexibility in what to profile.

# Construction / Recognition

## To Use tprof:
1. Select the measurement mode: call count, call time, or heap allocations.
2. Start tprof profiling on the target code (see `m:tprof` manual page).
3. Run the code to be profiled.
4. Stop profiling and examine results.

## To Recognize When tprof Is Appropriate:
1. You need to profile heap allocations per function (unique to tprof among built-in tools).
2. You want flexible choice between counting calls, timing calls, or measuring allocations.
3. You want a single tool that can address multiple profiling concerns.

# Context & Application

`tprof` is listed first among the profiling tools in the Erlang Efficiency Guide, suggesting it is the recommended starting point for profiling in modern Erlang/OTP. Its ability to measure heap allocations per function call is unique among the built-in profilers and particularly valuable for diagnosing memory-related performance issues without resorting to the more heavyweight memory profiling approach.

The three measurement modes (call count, call time, heap allocations) mean that `tprof` can address questions that previously required multiple tools: `cprof` for call counts, `fprof`/`eprof` for timing, and manual instrumentation for allocation tracking.

# Examples

**Example 1** (profiling.md, "Never Guess About Performance Bottlenecks"): The source lists tprof as the first tool in the profiling toolkit: "`tprof` is a tracing profiler that can measure call count, call time, or heap allocations per function call."

# Relationships

## Builds Upon
- **profiling-strategy** -- tprof is one tool in the profiling strategy toolkit

## Enables
- **profiling-analysis** -- tprof results feed into analysis of bottlenecks

## Related
- **fprof** -- fprof provides more detailed timing with caller/callee info but higher overhead
- **eprof** -- eprof provides per-process/function timing
- **cprof** -- cprof provides call counting with minimal overhead
- **memory-profiling** -- tprof's heap allocation mode is relevant to memory profiling

## Contrasts With
- No direct tool-vs-tool contrasts provided in source for tprof specifically.

# Common Errors

- **Error**: Using tprof in call-count mode when timing information is needed.
  **Correction**: Select the appropriate mode for your question -- call time for performance, call count for frequency, heap allocations for memory.

# Common Confusions

- **Confusion**: Thinking tprof replaces fprof entirely.
  **Clarification**: The source does not present tprof as a replacement for fprof. fprof still provides unique features like caller-callee tracking and garbage collection recording that are not mentioned for tprof.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, introductory tool listing in "Never Guess About Performance Bottlenecks" section. The source refers to the `m:tprof` manual page for detailed usage.

# Verification Notes

- Definition: Directly quoted from source's introductory tool enumeration.
- Key Properties: Derived from the single descriptive sentence in the source.
- Confidence: HIGH -- explicitly listed and described in the official documentation.
- Note: tprof does not have its own subsection under "Tools" in this chapter (unlike fprof, eprof, cprof), and is not included in the Tool Summary table. Its description comes solely from the introductory paragraph.
- Cross-references: All related tool slugs correspond to cards in this extraction.
- Uncertainties: The source provides less detail about tprof than about fprof/eprof/cprof. Additional information would be in the tprof manual page.
