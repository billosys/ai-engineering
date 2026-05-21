---
# === CORE IDENTIFICATION ===
concept: Reliability
slug: reliability

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: availability-properties
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Reliability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reliable system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - availability
extends: []
related:
  - fault-tolerance
  - resilience
  - redundancy
  - single-point-of-failure
contrasts_with:
  - fault-tolerance
  - resilience
  - availability

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is reliability?"
  - "How does a system keep functioning when components fail?"
---

# Quick Definition

Reliability is a system's ability to keep functioning under particular predefined conditions, including failure and data inconsistency, by relying on redundancy of components.

# Core Definition

"The reliability of a system is its ability to function under particular predefined conditions. In software and distributed systems, these conditions often include failure and inconsistency. In other words, the system has to continue functioning even when components that comprise it fail themselves or when data becomes inconsistent because it fails to replicate across nodes" (Cesarini & Vinoski, p. 406). Achieving reliability requires thinking about the redundancy of components — including data and state, which must be replicated and consistent across nodes.

# Prerequisites

- **Availability** — Reliability is one of the concepts availability encompasses; understand availability first.

# Key Properties

1. The ability to function under particular predefined conditions.
2. Those conditions often include failure and data inconsistency.
3. The system must keep functioning even when components fail or data fails to replicate.
4. Reliability requires redundancy — not only of hardware and software but of data and state.
5. Closely tied to having no single point of failure.

# Construction / Recognition

## To Construct/Create:
1. Identify the predefined conditions (including failures) under which the system must function.
2. Provide redundancy of components, data, and state across nodes.
3. Replicate data and keep it consistent across nodes.
4. Ensure business logic can redirect requests to a responsive node when one is unresponsive.

## To Identify/Recognize:
1. A system is reliable if, under the predefined conditions, it continues to function as defined — not merely accept requests.

# Context & Application

- **Typical contexts**: Distributed systems where components and data are subject to failure.
- **Common applications**: Redirecting a request to a responsive node when a node terminates, is slow, or is partitioned away.
- **Historical/stylistic notes**: A system can be highly available but unreliable — see the mainframe customer who claimed 100% availability but processed errored requests manually (p. 400).

# Examples

**Example 1** (p. 406): If a node is unresponsive because it has terminated, is slow, or got separated in a network partition, your business logic should be capable of redirecting the request to a responsive node — that is reliable behavior.

**Example 2** (p. 400): A mainframe system whose front-end nodes always accepted and acknowledged requests but logged and processed logic/service-node failures manually — highly available, but unreliable, because it did not always function as defined.

# Relationships

## Builds Upon
- **Availability** — Reliability is a component of availability

## Enables
- Reliability enables continued correct function under failure conditions.

## Related
- **Fault tolerance** — A sibling component of availability
- **Resilience** — A sibling component of availability
- **Redundancy** — Reliability requires redundancy of components and data
- **Single point of failure** — Reliability is undermined by single points of failure

## Contrasts With
- **Fault tolerance** — Reliability is continued correct function; fault tolerance is predictable behavior during failure
- **Resilience** — Reliability is sustained function; resilience is fast recovery
- **Availability** — A system can be available (accepting requests) yet unreliable (not functioning as defined)

# Common Errors

- **Error**: Treating "front-end always up" as proof of reliability
  **Correction**: Reliability requires the system to actually function as defined under failure, not just accept and acknowledge requests.

# Common Confusions

- **Confusion**: Reliability and availability are interchangeable.
  **Clarification**: Availability is uptime; reliability is functioning correctly under predefined conditions — a system can be available but unreliable.

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability," pages 406-407, and "Tradeoffs Between Consistency and Availability," pages 419-420.

# Verification Notes

- Definition source: Direct quote from p. 406.
- Confidence rationale: HIGH — the source explicitly defines reliability.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
