---
# === CORE IDENTIFICATION ===
concept: Eventual Consistency
slug: eventual-consistency

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
  - eventually consistent
  - weak consistency

# === TYPED RELATIONSHIPS ===
prerequisites:
  - consistency-models
extends:
  - consistency-models
related:
  - cap-theorem
  - share-something
  - riak-core
contrasts_with:
  - consensus-protocol

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is eventual consistency?"
  - "What distinguishes strong consistency from weak consistency?"
---

# Quick Definition

Eventual consistency is a weak consistency model in which updates at different replicas can occur in different orders and reads can return stale values, in exchange for read/write availability and predictable latency.

# Core Definition

"One weak form of consistency is eventual consistency, where updates at different replicas can occur in different orders, and reads can return stale values. While this consistency model sounds like it might do more harm than good, in practice it can be valuable for applications requiring read and write availability and predictable latency even when the system is operating under conditions of partial failure, as long as those applications can handle occasionally reading stale data" (Cesarini & Vinoski, p. 415).

# Prerequisites

- **Consistency models** — Eventual consistency is the weak end of the consistency spectrum; understand the spectrum first.

# Key Properties

1. Updates at different replicas can occur in different orders.
2. Reads can return stale values.
3. Provides read and write availability and predictable latency.
4. Valuable even under conditions of partial failure.
5. Requires that applications can handle occasionally reading stale data.
6. Has the lowest coordination cost of the consistency models.

# Construction / Recognition

## To Construct/Create:
1. Allow replicas to apply updates independently and converge over time.
2. Accept that reads may return stale values.
3. Design the application to tolerate occasionally stale data.

## To Identify/Recognize:
1. Recognize eventual consistency when reads may be stale and replica update orders may differ, but the system stays available.

# Context & Application

- **Typical contexts**: Applications needing read/write availability and predictable latency under partial failure.
- **Common applications**: Riak Core's replicated data model; messaging where duplicating messages reduces loss risk without strong guarantees.
- **Historical/stylistic notes**: Databases such as Riak can support both strong and eventual consistency, letting the application choose what it needs (p. 419).

# Examples

**Example 1** (p. 386): Riak Core "provides an eventually consistent replicated data model on a system of masterless peer nodes."

**Example 2** (p. 417): Messaging — "duplicating the messages through eventual consistency will greatly reduce the risk of them getting lost if you lose a node, but with no strong guarantee that you will never lose a message."

# Relationships

## Builds Upon
- **Consistency models** — Eventual consistency is one model on the spectrum

## Enables
- Eventual consistency enables high availability and predictable latency under partial failure.

## Related
- **Cap theorem** — Eventual consistency favors availability over consistency
- **Share something** — Shared data is often eventually consistent
- **Riak Core** — Provides an eventually consistent data model

## Contrasts With
- **Consensus protocol** — Consensus delivers strong consistency at higher coordination cost; eventual consistency relaxes it for availability

# Common Errors

- **Error**: Using eventual consistency for data that cannot tolerate stale reads
  **Correction**: Use it only where the application can handle occasionally reading stale data; use stronger models otherwise.

# Common Confusions

- **Confusion**: Eventual consistency means data is never consistent.
  **Clarification**: Replicas do converge; the model simply allows temporary divergence and stale reads in exchange for availability.

# Source Reference

Chapter 13: Systems That Never Stop, "Consistency," page 415, and "Distributed Erlang — Riak Core," page 386.

# Verification Notes

- Definition source: Direct quote from p. 415.
- Confidence rationale: HIGH — the source explicitly defines eventual consistency.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
