---
# === CORE IDENTIFICATION ===
concept: Sloppy Quorum
slug: sloppy-quorum

# === CLASSIFICATION ===
category: distribution
subcategory: replication
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Distributed Erlang — Riak Core"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sloppy quorums

# === TYPED RELATIONSHIPS ===
prerequisites:
  - riak-core
  - vnode
extends: []
related:
  - hinted-handoff
  - eventual-consistency
contrasts_with:
  - consensus-protocol

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a sloppy quorum?"
  - "How does Riak Core stay available during a partition?"
---

# Quick Definition

A sloppy quorum counts write/read acknowledgments without caring whether they come from primary or alternative (handoff) vnodes, preserving availability when primary vnodes are down or unreachable.

# Core Definition

"Writes require W acknowledgments to be considered successful, and similarly reads are considered successful with R results, but Riak doesn't care whether those quorums comprise primary or alternative vnodes (hence the term 'sloppy'). If Riak were to instead use strict quorums, which consist only of primary vnodes, the result would be diminished system availability when primaries were down or unreachable" (Cesarini & Vinoski, p. 388). Sloppy quorums work hand in hand with hinted handoffs.

# Prerequisites

- **Riak Core** — Sloppy quorums are a Riak Core mechanism; understand the framework first.
- **Vnode** — Quorums are counted in terms of vnodes.

# Key Properties

1. A write succeeds when W acknowledgments are received; a read succeeds when R results are received.
2. The acknowledging vnodes may be primary or alternative (handoff) vnodes.
3. Sloppy quorums preserve availability when primary vnodes are down or unreachable.
4. They are part of Riak Core's hinted-handoff mechanism.
5. They contrast with strict quorums, which count only primary vnodes.

# Construction / Recognition

## To Construct/Create:
1. Configure replication factor N and quorum thresholds W and R.
2. On a write/read, accept acknowledgments from any vnode — primary or alternative.
3. Consider the operation successful once W (write) or R (read) acknowledgments arrive.

## To Identify/Recognize:
1. Recognize a sloppy quorum when an operation succeeds despite some primary vnodes being unavailable.

# Context & Application

- **Typical contexts**: Eventually consistent distributed key-value stores like Riak.
- **Common applications**: Maintaining read/write availability during network partitions or node failures.
- **Historical/stylistic notes**: Default thresholds are W=R=N/2+1 (so 2 when N is 3).

# Examples

**Example 1** (p. 388): A write is considered successful with W acknowledgments and a read with R results, regardless of whether those came from primary or alternative vnodes.

**Example 2** (p. 388): If Riak used strict quorums (primary vnodes only), availability would be diminished whenever primaries were down or unreachable — the sloppy quorum avoids this.

# Relationships

## Builds Upon
- **Riak Core** — Sloppy quorums are a Riak Core mechanism
- **Vnode** — Quorums count vnode acknowledgments

## Enables
- **Hinted handoff** — Sloppy quorums make handoff vnodes count toward success

## Related
- **Hinted handoff** — Sloppy quorums are part of the hinted-handoff mechanism
- **Eventual consistency** — Sloppy quorums support the eventually consistent model

## Contrasts With
- **Consensus protocol** — Consensus protocols require majority agreement among primary replicas; sloppy quorums relax this for availability

# Common Errors

- **Error**: Assuming a successful write means all primary vnodes have the data
  **Correction**: With a sloppy quorum, some acknowledgments may come from alternative vnodes; hinted handoff later delivers the data to the primaries.

# Common Confusions

- **Confusion**: A quorum always means primary replicas.
  **Clarification**: A strict quorum does; a sloppy quorum deliberately counts alternative vnodes too, trading strict correctness for availability.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," page 388.

# Verification Notes

- Definition source: Direct quote from p. 388.
- Confidence rationale: HIGH — the source explicitly defines sloppy quorums and contrasts them with strict quorums.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
