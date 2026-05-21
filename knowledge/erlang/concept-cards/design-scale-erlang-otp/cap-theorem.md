---
# === CORE IDENTIFICATION ===
concept: CAP Theorem
slug: cap-theorem

# === CLASSIFICATION ===
category: distribution
subcategory: distributed-systems-theory
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "CAP Confusion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - CAP
  - "CAP theorem: Brewer's conjecture"
  - safety and liveness

# === TYPED RELATIONSHIPS ===
prerequisites:
  - consistency-models
extends: []
related:
  - consistency-availability-tradeoff
  - network-partition
  - fallacies-of-distributed-computing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the CAP theorem?"
  - "What distinguishes strong consistency from weak consistency?"
---

# Quick Definition

The CAP theorem states that in any distributed system it is impossible to fully provide consistency, availability, and partition tolerance at all times.

# Core Definition

"The CAP theorem, a conjecture originally put forward in 2000 by Eric Brewer and formally proven in 2002 by Seth Gilbert and Nancy Lynch, states that in any distributed system it is impossible to fully provide consistency, availability, and partition tolerance at all times" (Cesarini & Vinoski, p. 417). For CAP, consistency guarantees clients get correct responses; availability guarantees the system eventually services every request; partition tolerance guarantees continued operation even when the network or nodes fail and messages are delayed or lost (pp. 417-418).

# Prerequisites

- **Consistency models** — CAP frames the consistency-versus-availability choice; understand consistency models first.

# Key Properties

1. In any distributed system, you cannot fully provide consistency, availability, and partition tolerance at all times.
2. Consistency: clients get correct responses to all requests (a safety property).
3. Availability: the system eventually services every request, reads and updates (a liveness property).
4. Partition tolerance: the system keeps operating even when the network/nodes fail and messages are lost.
5. Partition tolerance is inherent in distributed systems, so the realistic choice is between consistency and availability.
6. Real tradeoffs are never as simple as the flawed "pick two" framing.

# Construction / Recognition

## To Construct/Create:
This is a theorem to apply, not an artifact. To apply it:
1. Accept that partitions will occur — partition tolerance is mandatory.
2. For each part of the application, choose the consistency/availability tradeoff it needs.
3. Allow different parts of one application to make different tradeoffs.

## To Identify/Recognize:
1. Recognize a CAP tradeoff whenever a design must sacrifice consistency or availability during a partition.

# Context & Application

- **Typical contexts**: Reasoning about every distributed-system design.
- **Common applications**: Justifying why a system favors consistency in one area (user registration) and availability in another (data delivery).
- **Historical/stylistic notes**: CAP is related to Lamport's safety and liveness (1977) and the FLP impossibility result of the 1980s. The claim that "Mnesia is a CA system" is debunked — it is anything but available during a network partition (p. 418).

# Examples

**Example 1** (p. 418): CAP consistency is a safety property ("nothing bad happens"); availability is a liveness property ("something good eventually happens").

**Example 2** (pp. 418-419): A fitness-tracker application — user registration requires strong consistency to prevent duplicate usernames, while data delivery favors high availability over fully consistent updates.

# Relationships

## Builds Upon
- **Consistency models** — CAP frames the consistency end of the spectrum against availability

## Enables
- CAP reasoning enables informed consistency/availability tradeoffs per application part.

## Related
- **Consistency-availability tradeoff** — The practical tradeoff CAP formalizes
- **Network partition** — The "P" in CAP
- **Fallacies of distributed computing** — Both express that delay and failure are inherent in distributed systems

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Treating CAP as "pick two"
  **Correction**: Partition tolerance is inherent in distributed systems, so the realistic choice is between consistency and availability; real tradeoffs are a spectrum, not a binary pick.

# Common Confusions

- **Confusion**: A system can be a "CA" system that gives up partition tolerance.
  **Clarification**: Partitions are inherent in distributed systems; claiming a CA system (e.g., "Mnesia is CA") ignores that it is unavailable during a partition.

# Source Reference

Chapter 13: Systems That Never Stop, "CAP Confusion," pages 417-419.

# Verification Notes

- Definition source: Direct quote from p. 417.
- Confidence rationale: HIGH — the source dedicates a named section to CAP with explicit definitions.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
