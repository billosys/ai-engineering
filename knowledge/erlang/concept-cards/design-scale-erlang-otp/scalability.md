---
# === CORE IDENTIFICATION ===
concept: Scalability
slug: scalability

# === CLASSIFICATION ===
category: performance
subcategory: scaling
tier: foundational

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
  - scalable system

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - horizontal-scaling
  - vertical-scaling
  - elasticity
  - capacity-planning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scalability?"
  - "How can a system be scaled?"
---

# Quick Definition

Scalability is a system's ability to handle changes in demand and behave predictably, especially under spikes or sustained heavy loads. It can be achieved vertically or horizontally.

# Core Definition

"The scalability of a system is its ability to handle changes in demand and behave predictably, especially under spikes or sustained heavy loads. Scalability can be achieved vertically, by throwing more powerful computers at the problem, or horizontally, by adding more nodes and hardware" (Cesarini & Vinoski, p. 424).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is the central theme of chapter 14, on top of which horizontal/vertical scaling, capacity planning, and elasticity are built.

# Key Properties

1. The ability to handle changes in demand.
2. The ability to behave predictably under spikes or sustained heavy loads.
3. Achievable vertically (more powerful computers) or horizontally (more nodes and hardware).
4. Erlang/OTP systems do not scale magically — they require the right tradeoffs.
5. Scalability tradeoffs are intertwined with consistency and availability tradeoffs.

# Construction / Recognition

## To Construct/Create:
1. Decide whether to scale vertically, horizontally, or both.
2. Make consistency/availability tradeoffs that support the scaling model.
3. Use loosely coupled nodes that can come and go (elasticity).
4. Validate through capacity testing.

## To Identify/Recognize:
1. A system is scalable if it handles increased demand while still behaving predictably.

# Context & Application

- **Typical contexts**: Any system expecting growth or variable load.
- **Common applications**: Adding computing capacity for peaks; designing systems with a growing user base.
- **Historical/stylistic notes**: "While Erlang/OTP systems do not scale magically, using OTP and making the right tradeoffs takes a large part of the pain out of the process" (p. 424).

# Examples

**Example 1** (p. 424): Scalability can be achieved vertically by throwing more powerful computers at the problem, or horizontally by adding more nodes and hardware.

**Example 2** (p. 428): The predictable behavior of the Erlang runtime, where a balanced system under heavy load yields constant throughput, addresses most scalability use cases.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- **Horizontal scaling** — One way to achieve scalability
- **Vertical scaling** — One way to achieve scalability
- **Capacity planning** — Plans the resources scalability needs
- **Elasticity** — Runtime scaling builds on scalability

## Related
- **Horizontal scaling** — Scaling out by adding nodes
- **Vertical scaling** — Scaling up with more powerful machines
- **Elasticity** — Adding/removing nodes at runtime

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Adding complexity for scale before it is needed
  **Correction**: "Be realistic in your capacity planning and add complexity only when you need it" (p. 430); premature optimization is the root of all evil.

# Common Confusions

- **Confusion**: Scalability is purely about adding computing capacity.
  **Clarification**: Scaling out must be carefully integrated with consistency and availability models; it is not just about adding capacity (p. 424).

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling," page 424.

# Verification Notes

- Definition source: Direct quote from p. 424.
- Confidence rationale: HIGH — the source explicitly defines scalability.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
