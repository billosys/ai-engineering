---
# === CORE IDENTIFICATION ===
concept: Sharing Data
slug: sharing-data

# === CLASSIFICATION ===
category: distribution
subcategory: data-sharing
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Sharing Data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - data-sharing strategy
  - data replication strategy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reliability
extends: []
related:
  - share-nothing
  - share-something
  - share-everything
  - replication
  - message-delivery-semantics
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data-sharing strategy?"
  - "How do I decide how to replicate data across nodes?"
---

# Quick Definition

Sharing data is the design decision, made per table and state, of whether and how to replicate it across nodes — choosing among share nothing, share something, and share everything.

# Core Definition

"When you are thinking about your strategies for avoiding a single point of failure and for recovery, you have to make a new set of decisions about whether and how you are going to replicate data across your nodes, node families, and clusters" (Cesarini & Vinoski, p. 410). "For every table and state, you have three approaches you can choose from: share nothing, share something, and share everything. Choose your data replication strategy wisely, and pick the one that most closely matches the level of scale or availability for which you are aiming" (p. 411).

# Prerequisites

- **Reliability** — Data-sharing decisions follow from single-point-of-failure and recovery thinking, which serve reliability.

# Key Properties

1. A decision made per table and per item of state.
2. Three approaches: share nothing, share something, share everything.
3. The choice affects availability (fault tolerance, resilience, reliability) and scalability.
4. Some decisions can be deferred to stress testing and benchmarking; others made up front.
5. Accessing and moving data is one of the hardest parts of distributed systems and a common source of bottlenecks.
6. A real system typically mixes all three strategies for different data.

# Construction / Recognition

## To Construct/Create:
1. For each table and state, assess the required scale and availability.
2. Choose share nothing, share something, or share everything to match.
3. Consider the needs of the chosen retry strategy when deciding.
4. Iterate, possibly revisiting earlier architecture choices.

## To Identify/Recognize:
1. Recognize the strategy by how much data/state is replicated: none, some, or all.

# Context & Application

- **Typical contexts**: Step 6 of designing a distributed architecture — picking a sharing strategy for all data and state.
- **Common applications**: Deciding whether session data, shopping carts, and account balances are replicated.
- **Historical/stylistic notes**: Consistent hashing can also be used to keep multiple copies of data without putting them on all nodes (p. 422).

# Examples

**Example 1** (p. 411): For every table and state, you choose among share nothing, share something, and share everything — picking the one matching the desired scale or availability.

**Example 2** (p. 417): When done, the choice "will often result in a mixture of the three recovery strategies, depending on the importance of the state change."

# Relationships

## Builds Upon
- **Reliability** — Data sharing serves reliability and recovery

## Enables
- **Share nothing** — One of the three sharing strategies
- **Share something** — One of the three sharing strategies
- **Share everything** — One of the three sharing strategies

## Related
- **Replication** — Sharing data is replicating it across nodes
- **Message delivery semantics** — Sharing strategy must be chosen alongside the retry strategy

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Picking one sharing strategy for the whole system
  **Correction**: The strategy is chosen per table and state; a real system mixes all three depending on the importance of each state change.

# Common Confusions

- **Confusion**: Data sharing is purely a database concern.
  **Clarification**: It applies to both data and state (e.g., behavior loop data), and is an architectural design decision.

# Source Reference

Chapter 13: Systems That Never Stop, "Sharing Data," pages 410-411, and "Summing Up," pages 421-422.

# Verification Notes

- Definition source: Direct quote from pp. 410-411.
- Confidence rationale: HIGH — the source explicitly frames the three-way choice.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
