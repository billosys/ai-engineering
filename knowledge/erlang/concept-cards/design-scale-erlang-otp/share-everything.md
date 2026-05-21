---
# === CORE IDENTIFICATION ===
concept: Share-Everything Architecture
slug: share-everything

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
section: "Consistency — Share everything"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - share everything
  - shared-everything architecture

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sharing-data
extends:
  - sharing-data
related:
  - share-nothing
  - share-something
  - replication
  - consistency-availability-tradeoff
contrasts_with:
  - share-nothing
  - share-something

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a share-everything architecture?"
  - "How do I decide how to replicate data across nodes?"
---

# Quick Definition

A share-everything architecture replicates all data and state across all nodes, so any node can take over a request — the most reliable but least scalable data-sharing strategy.

# Core Definition

"This is where the share-everything architecture comes into the picture. All your data is shared across all of the nodes, any of which might, upon hardware or software failure, take over the requests. If there is any uncertainty over the outcome of a request, an error is returned to the user" (Cesarini & Vinoski, p. 416). "The share-everything architecture is the most reliable of all data-sharing strategies, but this reliability comes at the cost of scalability. It tolerates the loss of nodes without impacting consistency of data, but if some nodes go wrong, it also loses availability. This strategy is also the most expensive to run and maintain" (p. 417).

# Prerequisites

- **Sharing data** — Share-everything is one of the three data-sharing strategies; understand the framing first.

# Key Properties

1. All data and state is replicated across all nodes.
2. Any node can take over a request upon hardware or software failure.
3. The most reliable data-sharing strategy.
4. The least scalable and most expensive to run and maintain.
5. Tolerates node loss without impacting data consistency, but loses availability when nodes go wrong.
6. A restarting node must connect to a primary and copy all data before accepting requests.
7. Suited to money, shares, and transactional data where inconsistency or loss is unacceptable.

# Construction / Recognition

## To Construct/Create:
1. Replicate every table and item of state across all nodes.
2. Use primary-primary replication so any node can take over.
3. On uncertainty over a request's outcome, return an error to the user.
4. Have a restarting node copy all data from a primary before accepting requests.

## To Identify/Recognize:
1. Recognize share-everything when every node holds a complete, consistent copy of all data.

# Context & Application

- **Typical contexts**: Systems handling money, equity trades, or other operations where loss or inconsistency is unacceptable.
- **Common applications**: Banking and financial systems; transactional data requiring exactly-once semantics.
- **Historical/stylistic notes**: Does not necessarily require distributed transactions, but needs them for data like money or shares you cannot afford to lose (p. 417).

# Examples

**Example 1** (pp. 416-417, Figure 14-8): Sessions and shopping-cart contents are duplicated in two logic nodes; if a node terminates, the other takes over; a recovered node accepts no requests until its data is consistent with the active node.

**Example 2** (p. 416): If you withdraw from multiple ATMs more funds than you have, you get the money but are later penalized for overdrawing — with no single point of failure and redundant hardware/software, the risk of such errors is minimized.

# Relationships

## Builds Upon
- **Sharing data** — Share-everything is one of the three data-sharing strategies

## Enables
- Share-everything enables maximum reliability and node-loss tolerance for critical data.

## Related
- **Share nothing** — The no-replication strategy
- **Share something** — The partial-replication strategy
- **Replication** — Share-everything uses primary-primary replication
- **Consistency-availability tradeoff** — Share-everything favors reliability/consistency over scalability

## Contrasts With
- **Share nothing** — Share-nothing replicates no state; share-everything replicates all
- **Share something** — Share-something replicates a subset; share-everything replicates everything

# Common Errors

- **Error**: Using share-everything for all data to be safe
  **Correction**: It is the most expensive and least scalable strategy; use it only for the subset of data and requests (e.g., money) that truly require it.

# Common Confusions

- **Confusion**: Share-everything guarantees both reliability and availability.
  **Clarification**: It is the most reliable strategy and tolerates node loss without consistency impact, but it loses availability when nodes go wrong.

# Source Reference

Chapter 13: Systems That Never Stop, "Consistency — Share everything," pages 416-417. See Figure 14-8.

# Verification Notes

- Definition source: Direct quote from pp. 416-417.
- Confidence rationale: HIGH — the source dedicates a named subsection with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
