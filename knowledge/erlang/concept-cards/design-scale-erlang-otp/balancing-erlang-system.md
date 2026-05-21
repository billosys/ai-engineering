---
# === CORE IDENTIFICATION ===
concept: Balancing an Erlang System
slug: balancing-erlang-system

# === CLASSIFICATION ===
category: performance
subcategory: capacity
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning — Balancing Your System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - balanced system
  - balancing your system
  - "CPU-bound, memory-bound, I/O-bound"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bottleneck
  - throughput
  - latency
extends: []
related:
  - capacity-planning
  - capacity-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a balanced Erlang system?"
  - "How does a balanced Erlang system behave under heavy load?"
---

# Quick Definition

A balanced Erlang system is one whose bottlenecks have been removed, so throughput stays constant under load while latency varies — its scaling limited only by CPU, memory, or I/O.

# Core Definition

"In a properly balanced Erlang system running at maximum capacity, the throughput should remain constant while latency varies" (Cesarini & Vinoski, p. 433). Removing bottlenecks yields "a constant throughput regardless of the number of simultaneous requests ... The limit on how much a node can scale is now determined by system limits such as CPU load, available memory, or I/O. We refer to nodes hitting these limits as being CPU-bound, memory-bound, or I/O-bound" (p. 434). A system is stable "only when all performance bottlenecks have been removed or optimized."

# Prerequisites

- **Bottleneck** — Balancing a system means removing its bottlenecks; understand bottlenecks first.
- **Throughput** — Constant throughput is the hallmark of balance.
- **Latency** — Latency varies in a balanced system while throughput holds.

# Key Properties

1. A balanced system has had all performance bottlenecks removed or optimized.
2. At maximum capacity, throughput stays constant while latency varies.
3. The BEAM VM is one of the few VMs displaying this property under sustained extreme loads.
4. Scaling is then limited only by system limits — CPU-bound, memory-bound, or I/O-bound.
5. Peak-load throughput might drop a little — a small price for predictability.
6. A system is stable only when bottlenecks are removed, leaving only external-dependency limits.

# Construction / Recognition

## To Construct/Create:
1. Stress test a single node with simulators to find bottlenecks.
2. Remove or optimize each bottleneck, rerunning the test.
3. Continue until throughput is constant regardless of simultaneous requests.
4. Identify whether the node is then CPU-, memory-, or I/O-bound.

## To Identify/Recognize:
1. Recognize a balanced system when its throughput graph is flat across simultaneous-request counts.

# Context & Application

- **Typical contexts**: Tuning a system after capacity testing.
- **Common applications**: Achieving predictable behavior under sustained extreme load.
- **Historical/stylistic notes**: Most other languages experience degraded throughput because processes have high context-switching costs; the Erlang VM, optimized for concurrency, greatly reduces this risk (p. 434).

# Examples

**Example 1** (p. 433): In a balanced Erlang system with constant 20,000 requests/second throughput, 20,000 simultaneous requests give 1-second latency and 40,000 give 2-second latency — throughput constant, latency doubled.

**Example 2** (p. 434, Figure 15-6): Removing bottlenecks gives constant throughput regardless of simultaneous requests; the shaded area shows the performance degradation of a badly balanced system.

# Relationships

## Builds Upon
- **Bottleneck** — Balancing is the removal of bottlenecks
- **Throughput** — Constant throughput is the goal of balancing
- **Latency** — Latency varies in a balanced system

## Enables
- A balanced system enables predictable behavior under sustained extreme load.

## Related
- **Capacity planning** — Balancing is part of capacity planning
- **Capacity testing** — Balancing is achieved through capacity testing

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Optimizing every node type
  **Correction**: Some node types may never face heavy load; be wary of premature optimization and test single nodes first.

# Common Confusions

- **Confusion**: A balanced system never slows down.
  **Clarification**: In a balanced system throughput stays constant but latency still rises with simultaneous requests; balance means predictability, not infinite speed.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning — Balancing Your System," pages 433-435. See Figures 15-5 and 15-6.

# Verification Notes

- Definition source: Direct quotes from pp. 433-434.
- Confidence rationale: HIGH — the source dedicates a named subsection with explicit characterization.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
