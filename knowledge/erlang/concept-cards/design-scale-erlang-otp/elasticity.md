---
# === CORE IDENTIFICATION ===
concept: Elasticity
slug: elasticity

# === CLASSIFICATION ===
category: performance
subcategory: scaling
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Horizontal and Vertical Scaling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - elastic
  - elastic scaling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - horizontal-scaling
extends: []
related:
  - scalability
  - system-blueprint
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is elasticity?"
  - "How does a system add and remove nodes at runtime?"
---

# Quick Definition

Elasticity is the ability to add and remove nodes and computers at runtime, catering not only for failure but also for peak loads and a growing user base.

# Core Definition

Erlang/OTP's location transparency and asynchronous message passing "facilitates elasticity, the ability to add and remove nodes (and computers) at runtime so you can cater not only for failure, but also for peak loads and systems with a growing user base" (Cesarini & Vinoski, p. 426).

# Prerequisites

- **Horizontal scaling** — Elasticity is the runtime form of horizontal scaling; understand it first.

# Key Properties

1. The ability to add and remove nodes (and computers) at runtime.
2. Caters for failure recovery.
3. Caters for peak loads.
4. Caters for systems with a growing user base.
5. Built on the location transparency of processes and asynchronous message passing.
6. Requires loosely coupled nodes that can come and go.

# Construction / Recognition

## To Construct/Create:
1. Build the system from loosely coupled nodes that can come and go.
2. Use process location transparency so a single-machine system distributes easily.
3. Add nodes for peaks and a growing user base; remove them when not needed.

## To Identify/Recognize:
1. Recognize elasticity when nodes and computers can join and leave the running system without disruption.

# Context & Application

- **Typical contexts**: Cloud deployments with variable load.
- **Common applications**: Adding computing capacity in the run-up to events (payday, Black Friday) and releasing it afterward.
- **Historical/stylistic notes**: "The key to the scalability of your system is ensuring you have loosely coupled nodes that can come and go. This provides elasticity to add computing power and scale on demand" (p. 442).

# Examples

**Example 1** (p. 426): Elasticity lets you add and remove nodes and computers at runtime, catering for failure, peak loads, and a growing user base.

**Example 2** (p. 442): The chapter summary stresses loosely coupled nodes that can come and go as the basis of elasticity and scaling on demand.

# Relationships

## Builds Upon
- **Horizontal scaling** — Elasticity is horizontal scaling performed at runtime

## Enables
- Elasticity enables scaling on demand for peaks, growth, and failure recovery.

## Related
- **Scalability** — Elasticity is a runtime aspect of scalability
- **System blueprint** — A cluster blueprint enables orderly elastic scaling

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Building tightly coupled nodes that cannot be added or removed cleanly
  **Correction**: Use loosely coupled nodes that can come and go — this is the key to elasticity.

# Common Confusions

- **Confusion**: Elasticity only handles peak loads.
  **Clarification**: It caters for failure recovery and a growing user base as well as peak loads.

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling," page 426, and "Summing Up," page 442.

# Verification Notes

- Definition source: Direct quote from p. 426.
- Confidence rationale: HIGH — the source explicitly defines elasticity.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
