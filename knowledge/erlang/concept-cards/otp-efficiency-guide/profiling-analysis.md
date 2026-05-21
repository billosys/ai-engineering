---
# === CORE IDENTIFICATION ===
concept: Profiling Analysis
slug: profiling-analysis

# === CLASSIFICATION ===
category: performance-methodology
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Profiling"
chapter_number: null
pdf_page: null
section: "What to Look For"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "profiling result analysis"
  - "what to look for in profiling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
extends:
  - profiling-strategy
related:
  - fprof
  - eprof
  - cprof
  - tprof
  - benchmarking-best-practices
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "What should I look for in profiling results?"
  - "How do I decide what to optimize after profiling?"
---

# Quick Definition

Profiling analysis is the practice of interpreting profiling results by looking for functions with high call counts and long "own" execution time, then systematically questioning whether the number of calls, test ordering, redundant computations, or data representations can be improved.

# Core Definition

The Erlang Efficiency Guide provides a structured approach to analyzing profiling results: "When analyzing the result file from the profiling activity, look for functions that are called many times and have a long 'own' execution time (time excluding calls to other functions). Functions that are called a lot of times can also be interesting, as even small things can add up to quite a bit if repeated often."

The guide then provides a systematic checklist of questions to ask:
- "Is it possible to reduce the number of times the function is called?"
- "Can any test be run less often if the order of tests is changed?"
- "Can any redundant tests be removed?"
- "Does any calculated expression give the same result each time?"
- "Are there other ways to do this that are equivalent and more efficient?"
- "Can another internal data representation be used to make things more efficient?"

The section concludes: "These questions are not always trivial to answer. Some benchmarks might be needed to back up your theory and to avoid making things slower if your theory is wrong."

# Prerequisites

- **Profiling Strategy** -- You must have profiled your program before you can analyze the results.

# Key Properties

1. Focus on functions with high "own" execution time (excluding called functions).
2. Focus on functions called many times (even small per-call costs accumulate).
3. Analysis involves asking structured optimization questions.
4. Optimization hypotheses should be validated with benchmarks.
5. Reducing call count can be as effective as reducing per-call cost.
6. Test ordering and redundant test elimination are valid optimization strategies.
7. Caching calculated expressions that produce the same result each time.
8. Alternative data representations may improve efficiency.

# Construction / Recognition

## To Analyze Profiling Results:
1. Sort functions by "own" execution time to find the most time-consuming.
2. Sort functions by call count to find the most frequently called.
3. Identify functions that are both frequently called and have high own time.
4. For each hot function, systematically ask the six optimization questions.
5. Formulate optimization hypotheses.
6. Validate hypotheses with benchmarks before implementing.

## The Six Optimization Questions:
1. Can the number of calls be reduced?
2. Can test ordering be changed to run expensive tests less often?
3. Can redundant tests be removed?
4. Can calculated expressions be cached (memoized)?
5. Are there equivalent but more efficient algorithms?
6. Can the internal data representation be changed for better performance?

# Context & Application

This section bridges profiling (data collection) and optimization (code changes). The guide emphasizes that profiling data alone is not actionable -- it must be interpreted through a systematic framework of questions. The explicit mention that "benchmarks might be needed to back up your theory" connects this concept directly to the benchmarking chapter, creating a profile-analyze-benchmark-optimize workflow.

The advice about test ordering and redundant test removal is particularly relevant to pattern matching and guard sequences in Erlang, where the order of clauses can significantly affect performance.

# Examples

**Example 1** (profiling.md, "What to Look For"): The source provides the six optimization questions as a checklist for analyzing any hot function found during profiling.

**Example 2** (profiling.md, "What to Look For"): The source explicitly connects analysis to benchmarking: "Some benchmarks might be needed to back up your theory and to avoid making things slower if your theory is wrong. For details, see Benchmarking."

# Relationships

## Builds Upon
- **profiling-strategy** -- analysis is the interpretation step after data collection

## Enables
- **benchmarking-best-practices** -- analysis produces optimization hypotheses that need benchmarking
- Informed optimization decisions

## Related
- **fprof** -- fprof provides own time and accumulated time data used in analysis
- **eprof** -- eprof provides per-function time percentages used in analysis
- **cprof** -- cprof provides call count data used in analysis
- **tprof** -- tprof provides call count, time, and heap allocation data

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Optimizing a function with high accumulated time but low own time.
  **Correction**: Focus on "own" execution time first. High accumulated time may simply mean the function calls other slow functions -- optimize those instead.

- **Error**: Implementing optimizations without benchmarking them first.
  **Correction**: The source explicitly warns: "Some benchmarks might be needed to back up your theory and to avoid making things slower if your theory is wrong."

# Common Confusions

- **Confusion**: Thinking the most-called function is always the bottleneck.
  **Clarification**: A function called millions of times may be trivially fast. The key is the combination of call count and own execution time. "Even small things can add up to quite a bit if repeated often," but the starting point should be functions with long own execution time.

- **Confusion**: Conflating "own time" with "accumulated time" in profiling results.
  **Clarification**: "Own" execution time is the time a function uses for its own execution, excluding time in called functions. Accumulated time includes called functions. The guide specifically says to look for long "own" execution time.

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "What to Look For" section. Cross-references the Benchmarking chapter for validation of optimization hypotheses.

# Verification Notes

- Definition: Directly quoted from source, including the full list of six optimization questions.
- Key Properties: All derived from the "What to Look For" section.
- Confidence: HIGH -- the source provides explicit, structured guidance with a numbered checklist.
- Cross-references: benchmarking-best-practices, fprof, eprof, cprof, tprof slugs all correspond to cards in this extraction.
- Uncertainties: None.
