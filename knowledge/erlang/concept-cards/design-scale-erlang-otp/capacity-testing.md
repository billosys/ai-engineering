---
# === CORE IDENTIFICATION ===
concept: Capacity Testing
slug: capacity-testing

# === CLASSIFICATION ===
category: testing
subcategory: load-testing
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning — Capacity Testing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - capacity testing
  - soak testing
  - spike testing
  - stress testing
  - load testing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - capacity-planning
extends: []
related:
  - bottleneck
  - throughput
  - latency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is capacity testing?"
  - "What are soak, spike, stress, and load testing?"
---

# Quick Definition

Capacity testing exercises a scalable system under heavy load to ensure stability and understand its behavior, using four strategies: soak, spike, stress, and load testing.

# Core Definition

"Capacity testing is a must when working with any scalable and available system to help ensure its stability and understand its behavior under heavy load. This is true regardless of what programming language you use to code the system" (Cesarini & Vinoski, p. 431). It comprises four strategies: soak testing (consistent load over time to detect degradation), spike testing (handling and recovering from peak loads), stress testing (gradually increasing load until bottlenecks and system limits are hit), and load testing (a constant rate close to limits to confirm stability).

# Prerequisites

- **Capacity planning** — Capacity testing validates capacity planning; understand it first.

# Key Properties

1. Exercises the system under heavy load to ensure stability and understand behavior.
2. Soak testing: a consistent load over time (potentially months) to detect performance degradation across the whole stack.
3. Spike testing: ensures peak loads can be handled and recovered from quickly.
4. Stress testing: gradually increases load until bottlenecks and system limits are hit.
5. Load testing: pushes the system at a constant rate near its limits for at least 24 hours.
6. Requires hardware to generate load, run simulators, and run parallel tests.

# Construction / Recognition

## To Construct/Create:
1. Write simulators that expose external service APIs and replicate their behavior.
2. Run soak tests for consistent long-term load.
3. Run spike tests for peak-load recovery.
4. Run stress tests, removing each bottleneck found and rerunning.
5. Run load tests for at least 24 hours near the limits.

## To Identify/Recognize:
1. Recognize each strategy by its load shape: consistent (soak), peaks (spike), increasing (stress), constant-near-limit (load).

# Context & Application

- **Typical contexts**: Validating any scalable, available system before going live.
- **Common applications**: Removing bottlenecks; testing failure behavior; validating the system blueprint.
- **Historical/stylistic notes**: Load tools for an Erlang system are usually written in Erlang; tools include Basho Bench, MZBench, and Tsung. The authors once caused a major IP-telephony provider outage by load-testing without diverting traffic to simulators (p. 432).

# Examples

**Example 1** (p. 431): Stress testing gradually increases the generated load until bottlenecks (long message queues) and system limits (running out of ports, memory, hard disk) are hit; once a bottleneck is removed, the stress test is rerun.

**Example 2** (p. 432): Simulators are standalone Erlang nodes that expose an external service's API and replicate its behavior — needed because third parties usually will not allow testing against live systems.

# Relationships

## Builds Upon
- **Capacity planning** — Capacity testing validates capacity planning

## Enables
- **Bottleneck** — Capacity testing exposes bottlenecks
- Capacity testing enables confidence in stability and failure behavior.

## Related
- **Bottleneck** — Stress testing finds bottlenecks
- **Throughput** — Tracked across capacity tests
- **Latency** — Tracked across capacity tests

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Load testing the final pre-launch system without diverting traffic to simulators
  **Correction**: Always connect to simulators and throttle toward external providers; the authors caused a provider outage by forgetting this.

# Common Confusions

- **Confusion**: One kind of test covers all capacity needs.
  **Clarification**: Four distinct strategies — soak, spike, stress, load — each exercise a different load profile and reveal different problems.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning — Capacity Testing," pages 431-433. See Figures 15-3 and 15-4.

# Verification Notes

- Definition source: Direct quotes from pp. 431-432.
- Confidence rationale: HIGH — the source dedicates a named subsection and enumerates all four strategies explicitly.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
