---
# === CORE IDENTIFICATION ===
concept: Establishing a Performance Baseline
slug: performance-baseline

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
section: "14.1.2. Establishing a baseline"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "baseline"
  - "performance baseline"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - performance-goals
extends: []
related:
  - performance-tuning
  - profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a performance baseline?"
  - "Why do you establish a baseline before tuning?"
  - "How broad should a baseline be?"
---

# Quick Definition

A performance baseline is a set of measurements of the system's current metrics, taken before any tuning, against which the impact of later changes is judged.

# Core Definition

If your goals are measurable, you can establish baselines. You run tests to find out where you currently stand with regard to the metrics for your goals — for example, the current CPU consumption and throughput of the system before any tuning is done. The broader the baseline, the easier it will be to determine the impact of any changes you make (Chapter 14, Section 14.1.2).

# Prerequisites

- **Determining performance goals** — Goals must be measurable for a baseline to be meaningful.

# Key Properties

1. A baseline records the system's current values for the metrics named in the goals.
2. It is measured before any tuning changes are made.
3. It requires measurable goals — you baseline the same metrics you set targets for.
4. A broader baseline makes the impact of later changes easier to determine.
5. It is the reference point for "measure the results" later in the tuning loop.

# Construction / Recognition

## To Construct/Create:
1. Identify the metrics named in your performance goals (e.g. CPU usage, throughput).
2. Run tests against the untuned system.
3. Record the measured values as the baseline.
4. Make the baseline as broad as practical — more metrics, more scenarios.

# Context & Application

- **Typical contexts**: Step 2 of the performance-tuning loop, before profiling and optimization.
- **Common applications**: Measuring erlware.org's current CPU consumption and throughput before optimizing.
- **Historical/stylistic notes**: Sometimes the baseline reveals there was no real problem where one was assumed.

# Examples

**Example 1** (Section 14.1.2): The book gives "current CPU consumption and throughput of your system, before you do any tuning" as the kind of values a baseline captures.

# Relationships

## Related
- **Performance tuning methodology** — The baseline is step 2 of the loop.
- **Profiling** — Profiling follows baselining when measurements show goals are unmet.

# Common Errors

- **Error**: Skipping the baseline and tuning straight away.
  **Correction**: Without a baseline you cannot prove a change helped.

- **Error**: Measuring only one narrow metric.
  **Correction**: Broaden the baseline so the impact of changes is easier to attribute.

# Common Confusions

- **Confusion**: Thinking a baseline is a one-time formality.
  **Clarification**: It is the comparison reference used every time results are measured during the tuning loop.

# Source Reference

Chapter 14: Optimization and performance, Section 14.1.2 "Establishing a baseline."

# Verification Notes

- Definition source: Direct adaptation of Section 14.1.2.
- Confidence rationale: HIGH — the concept is explicitly defined.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
