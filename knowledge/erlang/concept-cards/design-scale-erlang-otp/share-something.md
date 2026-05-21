---
# === CORE IDENTIFICATION ===
concept: Share-Something Architecture
slug: share-something

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
section: "Sharing Data — Share something"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - share something
  - shared-something architecture

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sharing-data
extends:
  - sharing-data
related:
  - share-nothing
  - share-everything
  - eventual-consistency
  - network-partition
contrasts_with:
  - share-nothing
  - share-everything

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a share-something architecture?"
  - "How do I decide how to replicate data across nodes?"
---

# Quick Definition

A share-something architecture replicates some but not all data and state across nodes — a compromise that increases fault tolerance while keeping replication overhead lower than full sharing.

# Core Definition

"The share-something architecture, where you duplicate some but not all of your data ... is a compromise: you copy some, but not all of the data and state associated with each session. The strategy reduces the overhead of copying while increasing the level of fault tolerance" (Cesarini & Vinoski, pp. 412-413). It trades off some scalability, because the shared data must be copied across nodes on every change and kept consistent when nodes are added or restart.

# Prerequisites

- **Sharing data** — Share-something is one of the three data-sharing strategies; understand the framing first.

# Key Properties

1. Some, but not all, data and state is replicated across nodes.
2. A compromise between share-nothing and share-everything.
3. Reduces copying overhead while increasing fault tolerance.
4. Trades off some scalability — shared data is copied on every change and on node add/restart.
5. Requires resolving conflicts (e.g., merging) when a partitioned node rejoins.
6. Ideal where occasional request loss is acceptable but state for expensive operations must be retained.

# Construction / Recognition

## To Construct/Create:
1. Identify which data and state must survive node failure (e.g., session data).
2. Replicate only that subset across the relevant nodes.
3. Define a routing strategy and a conflict-resolution/merge strategy for when nodes rejoin.

## To Identify/Recognize:
1. Recognize share-something when some state survives a node loss while other state does not.

# Context & Application

- **Typical contexts**: Systems where expensive operations' state must survive but occasional loss elsewhere is acceptable.
- **Common applications**: Replicating session data so users stay logged in, while not replicating shopping-cart contents.
- **Historical/stylistic notes**: An instant-messaging server can distribute the session record across nodes but not share status notifications and messages, sending those with at-most-once semantics (p. 414).

# Examples

**Example 1** (pp. 412-413, Figure 14-6): Session state is copied across all logic nodes so a client need not log in again after a node failure, but shopping-cart contents are not copied, so users find their carts emptied when a node is lost.

**Example 2** (p. 414): After a network partition, two shopping carts exist and must be merged or one discarded — the Dynamo approach includes uncertain items, leaving the shopper to remove or return them.

# Relationships

## Builds Upon
- **Sharing data** — Share-something is one of the three data-sharing strategies

## Enables
- Share-something enables fault tolerance for selected state without full replication cost.

## Related
- **Share nothing** — The no-replication strategy
- **Share everything** — The full-replication strategy
- **Eventual consistency** — Shared data may be eventually consistent
- **Network partition** — Share-something must merge state after a partition

## Contrasts With
- **Share nothing** — Share-nothing replicates no state; share-something replicates some
- **Share everything** — Share-everything replicates all state; share-something replicates only a subset

# Common Errors

- **Error**: Not defining how to merge divergent copies after a partition
  **Correction**: Decide up front how partitioned copies are merged or which is discarded.

# Common Confusions

- **Confusion**: Share-something means all important data is safe.
  **Clarification**: Only the explicitly replicated subset survives a node loss; un-replicated state (e.g., shopping carts) is still lost.

# Source Reference

Chapter 13: Systems That Never Stop, "Sharing Data — Share something," pages 412-414. See Figures 14-6 and 14-7.

# Verification Notes

- Definition source: Direct quote from pp. 412-413.
- Confidence rationale: HIGH — the source dedicates a named subsection with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
