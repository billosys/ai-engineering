---
# === CORE IDENTIFICATION ===
concept: Network Partition
slug: network-partition

# === CLASSIFICATION ===
category: distribution
subcategory: failure-modes
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "CAP Confusion"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - partition
  - network partitions
  - split brain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fallacies-of-distributed-computing
extends: []
related:
  - cap-theorem
  - share-something
  - hinted-handoff
  - fault-tolerance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a network partition?"
  - "How do I handle a network partition?"
---

# Quick Definition

A network partition is a failure in which the network or nodes fail and messages are delayed or lost, splitting a distributed system so parts cannot communicate.

# Core Definition

The book ties the network partition directly to the "P" of the CAP theorem: "Partition tolerance guarantees continued system operation even when the network or nodes fail and messages are delayed or lost" (Cesarini & Vinoski, p. 418). A partition is precisely the condition in which "the network or nodes fail and messages are delayed or lost." Partitions are inherent in distributed systems, and "partitions in those environments can be hard to understand and troubleshoot," especially on cloud infrastructure where you do not control the network (p. 385).

# Prerequisites

- **Fallacies of distributed computing** — A network partition is what makes the "network is reliable" fallacy dangerous; understand the fallacies first.

# Key Properties

1. A condition where the network or nodes fail and messages are delayed or lost.
2. Splits a distributed system so parts cannot communicate.
3. Inherent in distributed systems — the "P" in CAP, automatically chosen for you.
4. Hard to distinguish from a slow or crashed node.
5. Especially hard to understand and troubleshoot on cloud infrastructure with unknown topology.
6. Forces a tradeoff between consistency and availability during the partition.

# Construction / Recognition

## To Construct/Create:
This is a failure mode, not an artifact. To handle it:
1. Assume partitions will occur and design for partition tolerance.
2. Choose a consistency/availability tradeoff for the partitioned period.
3. Decide how divergent state (e.g., shopping carts) is merged or discarded when the partition heals.
4. Use mechanisms such as hinted handoff or eventual consistency to keep operating and self-heal.

## To Identify/Recognize:
1. Recognize a partition when nodes cannot communicate and behave as though others have crashed.

# Context & Application

- **Typical contexts**: Any distributed system, especially multi-data-center and cloud deployments.
- **Common applications**: Reasoning about CAP tradeoffs, share-something merge strategies, Riak Core hinted handoffs.
- **Historical/stylistic notes**: Some have claimed Mnesia is a CA system, "but clearly they've never attempted to use it during a network partition (conditions under which it is anything but available)" (p. 418).

# Examples

**Example 1** (p. 414, Figure 14-7): With a share-something architecture, a network partition leaves two shopping carts that must be merged or one discarded when the partition heals.

**Example 2** (p. 388): Riak Core uses hinted handoffs to ensure N copies are stored even when replica vnodes are unreachable because of a network partition.

# Relationships

## Builds Upon
- **Fallacies of distributed computing** — A partition is the realization of "the network is reliable" being false

## Enables
- Awareness of partitions motivates partition-tolerant design and merge strategies.

## Related
- **Cap theorem** — Partition tolerance is the "P" in CAP
- **Share something** — Share-something must merge state after a partition
- **Hinted handoff** — Keeps replication intact during a partition
- **Fault tolerance** — Partitions are a failure mode fault tolerance must handle

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Designing as if partitions are rare and can be ignored
  **Correction**: Partitions are inherent in distributed systems; design for partition tolerance and define how divergent state is reconciled.

# Common Confusions

- **Confusion**: A partition is the same as a node crash.
  **Clarification**: A partition is a communication failure; from the outside it is indistinguishable from a crash or a slow node, which is exactly what makes it hard to handle.

# Source Reference

Chapter 13: Systems That Never Stop, "CAP Confusion," pages 417-419, with partition-handling examples on pages 414 and 388.

# Verification Notes

- Definition source: Synthesized from the CAP partition-tolerance definition on p. 418 and partition discussion on pp. 385, 414.
- Confidence rationale: MEDIUM — the source describes network partitions extensively and consistently but defines them via the CAP "P" rather than as a standalone formal definition.
- Uncertainties: The term "split brain" is included as an alias for searchability though the book does not use that exact phrase.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
