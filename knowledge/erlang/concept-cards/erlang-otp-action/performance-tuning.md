---
# === CORE IDENTIFICATION ===
concept: Performance Tuning Methodology
slug: performance-tuning

# === CLASSIFICATION ===
category: performance
subcategory: methodology
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Optimization and performance"
chapter_number: 14
pdf_page: null
section: "14.1. How to approach performance tuning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "performance tuning"
  - "optimization process"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - performance-goals
  - performance-baseline
  - profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should you approach performance tuning?"
  - "What are the steps of the performance-tuning process?"
  - "When should you optimize code?"
---

# Quick Definition

Performance tuning is a systematic, iterative process: set goals, establish a baseline, profile, decide which problems to attack, optimize one at a time, and measure again — repeating until goals are met.

# Core Definition

The only way to be successful at performance improvement in general is to be systematic. Some problems may be obvious, but beyond that you need to measure, establish baselines, look for bottlenecks, optimize, and measure again to see whether performance improved. The book frames tuning as a loop: determine your goals, establish a baseline, profile, decide which problems to attack, optimize, and measure the results — repeating until the goals are satisfied or you give up. Optimization should only be on your mind when you know you need to save those extra milliseconds or kilobytes; modifying code for efficiency alone, possibly sacrificing simplicity and maintainability, should be a last resort, done only after the code has been made beautiful but still is not fast enough (Chapter 14, Section 14.1, Figure 14.1).

# Prerequisites

This is a foundational methodology concept with no prerequisites within this source.

# Key Properties

1. The process is a repeating loop: goals → baseline → profile → decide → optimize → measure → (repeat).
2. Optimization is a last resort, applied only after "make it beautiful" has failed to make it fast enough.
3. Quoting Joe Armstrong: "Make it work, then make it beautiful, then if you really, really have to, make it fast."
4. Changes are made one at a time so each change's effect can be measured.
5. Not every suspected problem is worth attacking — pick the issues with the best payoff for the available time.
6. An "obvious improvement" often has no measurable effect, or even makes things worse — measurement decides.

# Construction / Recognition

## To Construct/Create (the process):
1. **Determine goals** — define SMART performance goals.
2. **Establish a baseline** — measure where the system stands today.
3. **Profile the system** — find where time, memory, or bandwidth is spent.
4. **Decide which problems to attack** — pick the best-payoff issues for the timeframe.
5. **Optimize** — change the code, one issue at a time.
6. **Measure the results** — re-run measurements, compare to baseline; if goals met, stop; otherwise return to step 3.

# Context & Application

- **Typical contexts**: Any time a system fails to meet stated performance requirements.
- **Common applications**: The Erlware team applies this process to optimize the erlware.org site when adding hardware is not an option.
- **Historical/stylistic notes**: The chapter epigraph: "There is no such thing as fast, only fast enough" (Joe Armstrong).

# Examples

**Example 1** (Section 14.1): The Erlware team sets goals from actual site hits and traffic trends, then works the loop.

**Example 2** (Section 14.1.5): The book warns that an "obvious improvement" frequently turns out to have no measurable effect or to be worse — hence measure again.

# Relationships

## Related
- **Determining performance goals** — Step 1 of the process.
- **Establishing a baseline** — Step 2 of the process.
- **Profiling** — Step 3 of the process.

# Common Errors

- **Error**: Optimizing code before it works and is well-structured.
  **Correction**: Make it work, then beautiful; optimize only if it is still not fast enough.

- **Error**: Making several changes at once, then being unable to tell which one helped.
  **Correction**: Change one thing at a time and measure between changes.

# Common Confusions

- **Confusion**: Believing performance tuning is mostly intuition and clever tricks.
  **Clarification**: Intuition helps, but the reliable part is the science — measure, baseline, profile, repeat.

# Source Reference

Chapter 14: Optimization and performance, Section 14.1 "How to approach performance tuning" (14.1.1-14.1.5), Figure 14.1.

# Verification Notes

- Definition source: Direct adaptation of Section 14.1 and Figure 14.1.
- Confidence rationale: HIGH — the process is explicitly enumerated.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
