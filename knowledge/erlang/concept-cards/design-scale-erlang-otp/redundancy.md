---
# === CORE IDENTIFICATION ===
concept: Redundancy
slug: redundancy

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: availability-properties
tier: intermediate

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
  - redundant
  - site redundancy
  - triple redundancy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - single-point-of-failure
extends: []
related:
  - reliability
  - replication
  - load-balancing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is redundancy?"
  - "How do I design a system with no single point of failure?"
---

# Quick Definition

Redundancy is the practice of having at least two — preferably three — of every component, so that the failure of one does not bring down the system.

# Core Definition

To have no single point of failure, "you need to have at least two of everything. At least two computers with software distributed and running a failover strategy across them. At least two copies of your data and state. Two routers, gateways, and interfaces, so that if the primary one fails, the secondary takes over. Alternative power supplies (or battery backups) for the same reason" (Cesarini & Vinoski, p. 406). Because two of something makes the survivor a single point of failure, "using three or more instances instead of just two is normally a given when high reliability is a critical requirement. All of this comes at a higher bandwidth and latency cost" (p. 406).

# Prerequisites

- **Single point of failure** — Redundancy is the remedy for single points of failure; understand the problem first.

# Key Properties

1. Having at least two of every component, preferably three or more.
2. Covers computers, data and state copies, routers, gateways, interfaces, and power supplies.
3. Redundant computers run a failover strategy across them.
4. Two of something is itself risky; three or more is the norm for critical reliability.
5. Site redundancy places copies in geographically remote data centers.
6. Redundancy comes at a higher bandwidth and latency cost — and a financial cost.

# Construction / Recognition

## To Construct/Create:
1. Provide at least two (ideally three) of each component.
2. Run a failover strategy across redundant computers.
3. Replicate data and state.
4. Provide redundant networks, power supplies, and — where affordable — geographically remote sites.

## To Identify/Recognize:
1. Recognize redundancy when every component has a standby that can take over on failure.

# Context & Application

- **Typical contexts**: High-availability and high-reliability systems.
- **Common applications**: Failover hardware, replicated data, redundant networks, site redundancy.
- **Historical/stylistic notes**: European telecom recommendations guarantee sufficient distance between two sites that a bomb dropped anywhere between them leaves one site unaffected — "the price you have to pay for high availability" (pp. 406-407). Availability ultimately becomes a question of costs, tradeoffs, and risks.

# Examples

**Example 1** (p. 406): At least two computers running a failover strategy, two copies of data and state, two routers/gateways/interfaces, and alternative power supplies or battery backups.

**Example 2** (p. 460): A system with triple redundancy that still failed unnoticed because crashes were silently restarted — showing redundancy alone is not enough without monitoring.

# Relationships

## Builds Upon
- **Single point of failure** — Redundancy exists to eliminate single points of failure

## Enables
- **Reliability** — Redundancy is what makes a system reliable
- **Replication** — Data redundancy is achieved through replication

## Related
- **Reliability** — Redundancy is the means to reliability
- **Replication** — The data-and-state form of redundancy
- **Load balancing** — Distributes requests across redundant front-end nodes

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Providing exactly two of a component and considering the system safe
  **Correction**: Once one fails, the survivor is a single point of failure; use three or more for critical reliability.

# Common Confusions

- **Confusion**: Redundancy alone guarantees a working system.
  **Clarification**: Even triple-redundant systems can fail silently — redundancy must be paired with monitoring (p. 460).

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability," pages 406-408, including the "Extraordinary Measures" sidebar.

# Verification Notes

- Definition source: Direct quote from p. 406.
- Confidence rationale: HIGH — the source explicitly and extensively describes redundancy.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
