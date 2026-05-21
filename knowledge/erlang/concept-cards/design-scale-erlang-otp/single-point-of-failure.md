---
# === CORE IDENTIFICATION ===
concept: Single Point of Failure
slug: single-point-of-failure

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: failure-modes
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
  - SPOF
  - single points of failure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reliability
extends: []
related:
  - redundancy
  - availability
  - load-balancing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a single point of failure?"
  - "How do I design a system with no single point of failure?"
---

# Quick Definition

A single point of failure is a component whose failure brings down the whole system. Eliminating it means having at least two — preferably three — of everything.

# Core Definition

"A single point of failure means that if a particular component in your system fails, your whole system fails. That component could be a process, a node, a computer, or even the network tying it all together. This means that in order for your system to have no single point of failure, you need to have at least two of everything" (Cesarini & Vinoski, p. 406). "Having only two of everything might itself be a problem ... since if one of something goes down, the remaining instance automatically becomes a single point of failure. For this reason, using three or more instances instead of just two is normally a given when high reliability is a critical requirement" (p. 406).

# Prerequisites

- **Reliability** — Eliminating single points of failure is central to reliability; understand reliability first.

# Key Properties

1. A component whose failure causes the whole system to fail.
2. The component may be a process, node, computer, or the network itself.
3. Eliminating it requires at least two of everything: computers, data copies, routers, gateways, interfaces, power supplies.
4. Two of everything is risky — losing one makes the survivor a single point of failure.
5. Three or more instances is normal when high reliability is critical.
6. Redundancy comes at higher bandwidth and latency cost.

# Construction / Recognition

## To Construct/Create:
This is a flaw to eliminate, not to build. To eliminate it:
1. Provide at least two (preferably three) of every component — computers, data copies, routers, power supplies.
2. Run a failover strategy across redundant computers.
3. Place computers in separate, geographically remote data centers if possible.

## To Identify/Recognize:
1. Recognize a single point of failure as any component with no redundant counterpart.

# Context & Application

- **Typical contexts**: Any system aiming for high availability and reliability.
- **Common applications**: Redundant hardware, replicated data, redundant networks, geographic site redundancy.
- **Historical/stylistic notes**: US regulatory disaster-recovery guidelines for financial institutions recommend a minimum 200-300 miles between primary and secondary data centers (p. 406).

# Examples

**Example 1** (pp. 407-408, Figure 14-3): A front-end node forwards a request to a logic node which then fails; because there is no single point of failure, the front-end node forwards the request to a secondary logic node, which handles it — the client never knows.

**Example 2** (p. 406, "Extraordinary Measures"): A builder's digger cut a single cable, taking out a site's Internet, landline, and mobile connectivity for a week — a physical single point of failure that site redundancy would have prevented.

# Relationships

## Builds Upon
- **Reliability** — Eliminating single points of failure is required for reliability

## Enables
- Eliminating single points of failure enables high availability.

## Related
- **Redundancy** — The remedy for single points of failure
- **Availability** — High availability requires no single point of failure
- **Load balancing** — Load balancers route around failed front-end nodes

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Providing exactly two of everything
  **Correction**: Once one fails, the survivor becomes a single point of failure; use three or more when high reliability is critical.

# Common Confusions

- **Confusion**: A single point of failure is always a piece of hardware.
  **Clarification**: It can be a process, a node, a computer, or the network tying everything together.

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability," pages 406-408. See Figure 14-3 and the "Extraordinary Measures" sidebar.

# Verification Notes

- Definition source: Direct quote from p. 406.
- Confidence rationale: HIGH — the source explicitly defines single point of failure.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
