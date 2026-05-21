---
# === CORE IDENTIFICATION ===
concept: Consensus Protocol
slug: consensus-protocol

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
section: "Consistency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - consensus protocols
  - Paxos
  - Raft

# === TYPED RELATIONSHIPS ===
prerequisites:
  - consistency-models
extends: []
related:
  - cap-theorem
contrasts_with:
  - eventual-consistency

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a consensus protocol?"
  - "How is strong consistency achieved in a distributed system?"
---

# Quick Definition

A consensus protocol is an algorithm in which a majority of replicas vote and agree on each update, delivering strong consistency at the cost of high coordination, latency, and reduced availability.

# Core Definition

"Even higher degrees of consistency can be achieved using consensus protocols such as Paxos, Zookeeper Atomic Broadcast (ZAB), and Raft, where a majority of replicas must vote and agree on updates for a given value. These protocols can deliver strong consistency guarantees, but to achieve them they require a high degree of coordination among replicas and so can have negative impacts on latency and availability" (Cesarini & Vinoski, p. 416).

# Prerequisites

- **Consistency models** — Consensus protocols sit at the strong end of the consistency spectrum; understand the spectrum first.

# Key Properties

1. A majority of replicas must vote and agree on updates for a given value.
2. Delivers strong consistency guarantees.
3. Requires a high degree of coordination among replicas.
4. Negatively impacts latency and availability.
5. Examples include Paxos, Zookeeper Atomic Broadcast (ZAB), and Raft.
6. You should use a proven implementation rather than inventing your own.

# Construction / Recognition

## To Construct/Create:
1. For an update, require a majority of replicas to vote and agree.
2. Use a proven implementation (e.g., Riak Ensemble implements Multi-Paxos).
3. Accept the latency and availability cost the coordination imposes.

## To Identify/Recognize:
1. Recognize a consensus protocol by majority voting/agreement among replicas before an update is committed.

# Context & Application

- **Typical contexts**: Applications that genuinely require strong consistency guarantees.
- **Common applications**: Strongly consistent distributed stores; coordination services.
- **Historical/stylistic notes**: "If your application requires this level of consistency guarantee, you are far better off using an implementation of a proven consensus protocol than trying to invent your own" — Riak Ensemble implements Multi-Paxos, an optimized version of basic Paxos (p. 416).

# Examples

**Example 1** (p. 416): Paxos, Zookeeper Atomic Broadcast (ZAB), and Raft are named as consensus protocols where a majority of replicas must vote and agree on updates.

**Example 2** (p. 416): Riak Ensemble implements Multi-Paxos, an optimized version of basic Paxos.

# Relationships

## Builds Upon
- **Consistency models** — Consensus protocols achieve the strong end of the spectrum

## Enables
- Consensus protocols enable strong consistency guarantees.

## Related
- **Cap theorem** — Consensus protocols choose consistency, accepting reduced availability

## Contrasts With
- **Eventual consistency** — Eventual consistency relaxes coordination for availability; consensus protocols maximize coordination for consistency

# Common Errors

- **Error**: Inventing your own consensus algorithm
  **Correction**: Use a proven implementation of an established consensus protocol.

# Common Confusions

- **Confusion**: Consensus protocols have no downside.
  **Clarification**: They deliver strong consistency but require high coordination, hurting latency and availability — and full consensus is impossible if even a single part is failing (FLP result, p. 418).

# Source Reference

Chapter 13: Systems That Never Stop, "Consistency," page 416, and "CAP Confusion," page 418 (FLP impossibility result).

# Verification Notes

- Definition source: Direct quote from p. 416.
- Confidence rationale: HIGH — the source explicitly describes consensus protocols and names examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
