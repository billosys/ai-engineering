---
# === CORE IDENTIFICATION ===
concept: Profiling Strategy
slug: profiling-strategy

# === CLASSIFICATION ===
category: performance-methodology
subcategory: null
tier: foundational

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
  - "profiling methodology"
  - "performance profiling"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - fprof
  - eprof
  - cprof
  - tprof
  - dbg-profiling
  - lcnt
  - profiling-analysis
  - benchmarking-best-practices
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "Why should I not guess about performance bottlenecks?"
---

# Quick Definition

Profiling strategy is the principle that performance bottlenecks must be identified through measurement rather than guessing, using the profiling tools provided by Erlang/OTP. Even experienced developers often guess wrong about where bottlenecks lie.

# Core Definition

The Erlang Efficiency Guide opens its Profiling chapter with a categorical directive: "Even experienced software developers often guess wrong about where the performance bottlenecks are in their programs. Therefore, profile your program to see where the performance bottlenecks are and concentrate on optimizing them." The guide then enumerates the built-in profiling tools available in Erlang/OTP: `tprof` (tracing profiler for call count, call time, or heap allocations), `fprof` (detailed time profiling with significant slowdown), `dbg` (generic tracing frontend usable for timing), and `lcnt` (lock contention profiling).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Performance bottlenecks should never be guessed at -- they must be measured.
2. Even experienced developers guess wrong about bottleneck locations.
3. Erlang/OTP provides multiple built-in profiling tools with different trade-offs.
4. Open-source tools (erlgrind, eflame, recon, perf) complement the built-in tools.
5. The choice of tool depends on the type of bottleneck (CPU time, memory, lock contention).

# Construction / Recognition

## To Apply Profiling Strategy:
1. Identify the performance concern (slow response, high memory, contention).
2. Select the appropriate profiling tool based on the concern type.
3. Run the profiler on the relevant code path or system.
4. Analyze the results to locate actual bottlenecks.
5. Optimize only the identified bottlenecks.
6. Verify improvements with benchmarks (see `benchmarking-best-practices`).

## To Recognize the Need for Profiling:
1. System performance does not meet requirements.
2. Specific operations are slower than expected.
3. Memory usage is unexpectedly high.
4. Contention suspected in parallel operations.

# Context & Application

This principle is the entry point for all performance optimization work in Erlang/OTP. The guide presents it as the very first topic in the Profiling chapter, establishing it as a prerequisite mindset before introducing any specific tools. The emphasis on measurement over guessing reflects a pragmatic engineering culture: optimize what matters, not what you think matters.

**Available built-in tools:**
- `tprof` -- call count, call time, or heap allocation per function
- `fprof` -- most detailed time information, but significant slowdown
- `dbg` -- precision timing for specific processes in live systems
- `lcnt` -- lock contention profiling for parallel interactions

**Open-source tools:**
- `erlgrind` -- visualize fprof data in kcachegrind
- `eflame` -- flamegraph output alternative to fprof
- `recon` -- collection of profiling and debugging tools
- `perf` -- Linux sampling profiler with low overhead (requires `+JPperf true` and JIT)

# Examples

**Example 1** (profiling.md, "Never Guess About Performance Bottlenecks"): The source lists four built-in tools as the primary means to find bottlenecks: `tprof` for measuring call count/time/heap allocations, `fprof` for detailed time profiling, `dbg` for precision timing in live systems, and `lcnt` for lock contention analysis.

**Example 2** (profiling.md, "Never Guess About Performance Bottlenecks"): The source mentions `perf` as a Linux sampling profiler that provides fprof-like functionality with much lower overhead, available when the emulator is started with `+JPperf true` and JIT is enabled.

# Relationships

## Builds Upon
- No prerequisites -- this is a foundational principle.

## Enables
- **fprof** -- one of the tools used to implement this strategy
- **eprof** -- one of the tools used to implement this strategy
- **cprof** -- one of the tools used to implement this strategy
- **tprof** -- one of the tools used to implement this strategy
- **dbg-profiling** -- one of the tools used to implement this strategy
- **lcnt** -- one of the tools used to implement this strategy
- **profiling-analysis** -- analysis follows from profiling

## Related
- **benchmarking-best-practices** -- benchmarking validates optimization hypotheses
- **memory-profiling** -- memory-specific profiling approach

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Optimizing code based on intuition without profiling first.
  **Correction**: Always profile before optimizing; the actual bottleneck is often not where you expect.

- **Error**: Using only one profiling tool for all performance problems.
  **Correction**: Different tools serve different purposes -- use `fprof` for time, `lcnt` for contention, memory functions for memory issues.

# Common Confusions

- **Confusion**: Believing that profiling tools are interchangeable.
  **Clarification**: Each tool measures different things (call count vs. execution time vs. lock contention) and has different performance impacts on the profiled system.

- **Confusion**: Thinking profiling is only needed for slow code.
  **Clarification**: Profiling is also used for memory issues, lock contention, and understanding system behavior in parallel/distributed settings.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, section "Never Guess About Performance Bottlenecks." Also references the "Tools" section for built-in tools and external tools (erlgrind, eflame, recon, perf).

# Verification Notes

- Definition: Directly quoted "never guess" principle from source.
- Key Properties: All derived from the introductory section of the Profiling chapter.
- Tool list: Explicitly enumerated in source with descriptions.
- Confidence: HIGH -- the source states this principle explicitly and prominently.
- Cross-references: All tool slugs correspond to planned cards in this extraction.
- Uncertainties: None.
