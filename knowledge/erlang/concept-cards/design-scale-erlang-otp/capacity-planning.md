---
# === CORE IDENTIFICATION ===
concept: Capacity Planning
slug: capacity-planning

# === CLASSIFICATION ===
category: production-ops
subcategory: capacity
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - capacity plan

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scalability
  - semantic-node-type
extends: []
related:
  - throughput
  - latency
  - capacity-testing
  - system-blueprint
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is capacity planning?"
  - "How do I ensure my system can handle its designed load even after a failure?"
---

# Quick Definition

Capacity planning is the work of understanding what resources node types use so the hardware and infrastructure can be optimized for efficiency and cost, guaranteeing the system handles its designed load.

# Core Definition

"Understanding what resources your node types use and how they interact with each other allows you to optimize the hardware and infrastructure in terms of both efficiency and cost. This work is called capacity planning. Its purpose is to try to guarantee that your system can withstand the load it was designed to handle, and, with time, scale to manage increased demand" (Cesarini & Vinoski, p. 426).

# Prerequisites

- **Scalability** — Capacity planning serves scalability goals; understand scalability first.
- **Semantic node type** — Capacity planning measures resource use per node type.

# Key Properties

1. Understanding the resources each node type uses and how node types interact.
2. Optimizes hardware and infrastructure for both efficiency and cost.
3. Guarantees the system can withstand its designed load and scale with demand.
4. Requires simulating high loads and testing the system end to end.
5. Different node types are memory-bound, CPU-bound, or I/O-bound and need different hardware.
6. Must account for handling the designed load even after a software, hardware, or network failure.

# Construction / Recognition

## To Construct/Create:
1. Determine each node type's resource profile (memory-, CPU-, or I/O-bound).
2. Simulate high loads and test the system end to end.
3. Choose hardware that matches each node type's profile.
4. Size node ratios so the designed load is handled even after losing a node of each type.

## To Identify/Recognize:
1. Recognize capacity planning as the analysis tying load, resource use, and node ratios to hardware choices.

# Context & Application

- **Typical contexts**: Sizing and balancing a distributed system before going live.
- **Common applications**: Cost optimization; ensuring no single point of failure leaves enough capacity.
- **Historical/stylistic notes**: Measured in throughput and latency; the cluster blueprint is derived from the lessons learned during capacity planning.

# Examples

**Example 1** (p. 408): A memory-bound front-end node holding millions of idle TCP connections needs different hardware from a CPU-bound front-end node spending its time parsing JSON or XML.

**Example 2** (p. 429): If a system has two front-end nodes per logic node both running at 100% capacity, losing one halves capacity; you need at least three front-end nodes at 66% CPU each and two back-end nodes at 50% each to handle peak load after a failure.

# Relationships

## Builds Upon
- **Scalability** — Capacity planning serves scalability goals
- **Semantic node type** — Capacity planning measures resource use per node type

## Enables
- **Capacity testing** — Capacity planning is validated by capacity testing
- **System blueprint** — The cluster blueprint is derived from capacity planning

## Related
- **Throughput** — A core measure in capacity planning
- **Latency** — A core measure in capacity planning
- **System blueprint** — The formalized output of capacity planning

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Sizing nodes to run at 100% capacity
  **Correction**: Leave headroom — e.g., three front-end nodes at 66% CPU — so losing any node still handles peak load.

# Common Confusions

- **Confusion**: Capacity planning is only about adding enough hardware.
  **Clarification**: It is also a cost-optimization exercise and must account for handling the designed load after a failure.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning," pages 426-430. See Figure 15-2.

# Verification Notes

- Definition source: Direct quote from p. 426.
- Confidence rationale: HIGH — the source dedicates a named section with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
