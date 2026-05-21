---
# === CORE IDENTIFICATION ===
concept: Determining Performance Goals (SMART)
slug: performance-goals

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
section: "14.1.1. Determining your performance goals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "SMART goals"
  - "performance goals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - performance-tuning
extends: []
related:
  - performance-baseline
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you set performance goals?"
  - "What does the SMART acronym mean for performance tuning?"
  - "How do you know when performance tuning is finished?"
---

# Quick Definition

Performance goals should be SMART — Specific, Measurable, Attainable, Realistic, and Timely — so you know precisely when the tuning effort is done.

# Core Definition

Before you begin tuning, you should know when you can say you are finished. Goals should have the characteristics captured by the SMART acronym: **Specific** (clearly defined, e.g. in terms of CPU usage or throughput per second); **Measurable** (verifiable through systematic measurement); **Attainable** (reasonable to achieve within the limits of the project); **Realistic** (achievable given current resources and motivation, not only through a heroic team effort); and **Timely** (finishable within a predetermined time, so the effort stays focused). Goals are set from concrete data such as actual traffic and projected growth (Chapter 14, Section 14.1.1).

# Prerequisites

- **Performance tuning methodology** — Setting goals is the first step of the tuning loop.

# Key Properties

1. **Specific** — defined in concrete terms like CPU usage or throughput per second.
2. **Measurable** — verifiable by systematic measurement.
3. **Attainable** — reasonable to reach within the project's limits.
4. **Realistic** — achievable with current resources, not only through extraordinary effort.
5. **Timely** — bounded by a predetermined time limit to keep effort focused.
6. Goals are derived from real data — actual traffic volume, historical trends, and projected growth.

# Construction / Recognition

## To Construct/Create:
1. Gather data: actual transaction volume, historical traffic trends, projected future load.
2. Define specific, numeric targets (e.g. throughput per second, CPU usage).
3. Confirm each target is measurable, attainable, and realistic.
4. Set a time limit for the tuning effort.

# Context & Application

- **Typical contexts**: The start of any performance-tuning effort.
- **Common applications**: The Erlware team sets goals from erlware.org hit counts and a six-month traffic projection.
- **Historical/stylistic notes**: SMART is a widely used goal-setting mnemonic, applied here to performance work.

# Examples

**Example 1** (Section 14.1.1): The Erlware team looks at actual hits and transaction volume, reviews the last few months' trends, projects six months ahead, and sets the current tuning goals from that.

# Relationships

## Related
- **Establishing a baseline** — Measurable goals make a meaningful baseline possible.

# Common Errors

- **Error**: Setting open-ended goals with no time limit.
  **Correction**: Make goals Timely — a deadline focuses effort and filters out the unimportant.

- **Error**: Setting goals so high they are unattainable.
  **Correction**: Keep goals Attainable and Realistic within project resources.

# Common Confusions

- **Confusion**: Thinking "make it faster" is a goal.
  **Clarification**: It is not Specific or Measurable; a goal must name a metric and a target value.

# Source Reference

Chapter 14: Optimization and performance, Section 14.1.1 "Determining your performance goals."

# Verification Notes

- Definition source: Direct adaptation of Section 14.1.1.
- Confidence rationale: HIGH — the SMART criteria are explicitly listed.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
