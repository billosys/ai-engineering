---
# === CORE IDENTIFICATION ===
concept: Availability
slug: availability

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
section: "Availability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - high availability
  - uptime
  - "five nines"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - fault-tolerance
  - resilience
  - reliability
  - single-point-of-failure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is availability?"
  - "What is high availability?"
---

# Quick Definition

Availability is the uptime of a system over a certain period of time, including software maintenance and upgrades. High availability refers to systems with very low downtime.

# Core Definition

"Availability defines the uptime of a system over a certain period of time. High availability refers to systems with very low downtime, software maintenance and upgrades included" (Cesarini & Vinoski, p. 402). "High availability is the result of your system having no single point of failure, and being fault-tolerant, resilient, and reliable. It can also be the result of having a system that even in the face of partial failure can still provide some degree of service, albeit reduced from normal levels" (p. 403).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is the umbrella term under which fault tolerance, resilience, and reliability sit.

# Key Properties

1. Availability is the uptime of a system over a period, maintenance and upgrades included.
2. High availability means very low downtime.
3. High availability results from no single point of failure plus fault tolerance, resilience, and reliability.
4. It can also mean degraded service (some degree of service under partial failure).
5. "Nine nines" of uptime is only 31.6 ms of downtime per year — claimed but rarely long-lived.
6. A realistic Erlang/OTP figure is 99.999% (five nines) uptime — just over 5 minutes of downtime per year.

# Construction / Recognition

## To Construct/Create:
1. Eliminate single points of failure (at least two, ideally three, of everything).
2. Apply the Erlang/OTP programming model for fault tolerance, resilience, and reliability.
3. Make sound data-sharing and recovery-strategy tradeoffs.
4. Allow degraded service under partial failure rather than total outage.

## To Identify/Recognize:
1. Measure uptime over a period, counting all downtime including maintenance and upgrades.

# Context & Application

- **Typical contexts**: Telecom systems and, increasingly, any vertical aiming for five-nines.
- **Common applications**: Designing systems that "never stop" via redundancy and the OTP programming model.
- **Historical/stylistic notes**: British Telecom claimed nine-nines availability over a six-month AXD301 ATM switch trial (p. 402, footnote).

# Examples

**Example 1** (p. 403): Nine nines of uptime means only 31.6 milliseconds of downtime per year — less time than it takes to blink.

**Example 2** (p. 403): A realistic number often achieved with Erlang/OTP is 99.999% uptime, equating to just over 5 minutes of downtime each year, upgrades and maintenance included.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- **Fault tolerance** — A component of availability
- **Resilience** — A component of availability
- **Reliability** — A component of availability

## Related
- **Fault tolerance** — Availability encompasses fault tolerance
- **Resilience** — Availability encompasses resilience
- **Reliability** — Availability encompasses reliability
- **Single point of failure** — High availability requires having no single point of failure

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Counting only unplanned outages toward downtime
  **Correction**: Availability includes software maintenance and upgrade time as downtime.

# Common Confusions

- **Confusion**: Availability and reliability are the same thing.
  **Clarification**: A system can be highly available (front-end always accepting requests) yet unreliable (logic/service nodes silently failing, requiring manual processing) — see chapter 13's mainframe war story (p. 400).

# Source Reference

Chapter 13: Systems That Never Stop, "Availability," pages 402-403, and "Summing Up," pages 421-422.

# Verification Notes

- Definition source: Direct quote from pp. 402-403.
- Confidence rationale: HIGH — the source explicitly defines availability and high availability.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
