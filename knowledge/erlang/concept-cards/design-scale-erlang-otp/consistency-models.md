---
# === CORE IDENTIFICATION ===
concept: Consistency Models
slug: consistency-models

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
  - consistency
  - monotonic read
  - monotonic write
  - read your own writes
  - strong consistency

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sharing-data
extends: []
related:
  - eventual-consistency
  - consensus-protocol
  - cap-theorem
contrasts_with:
  - eventual-consistency

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the different consistency models?"
  - "What distinguishes strong consistency from weak consistency?"
---

# Quick Definition

Consistency models describe the spectrum of guarantees a distributed system makes about the visibility, ordering, and recency of data updates across replicas — from weak (eventual) to strong.

# Core Definition

"When dealing with distributed systems, there are multiple forms of consistency that differ due to varying degrees of visibility, ordering, and replica coordination" (Cesarini & Vinoski, p. 415). Models range from weak (eventual consistency) through monotonic read and monotonic write (recency guarantees), read your own writes, and combinations thereof, up to strong consistency achieved via consensus protocols. Stronger ordering guarantees "come at a cost of increased coordination across the distributed system, and thus potentially increased latencies and lower availability" (p. 415).

# Prerequisites

- **Sharing data** — Consistency models govern how shared/replicated data behaves; understand data sharing first.

# Key Properties

1. Models differ in visibility, ordering, and replica coordination.
2. Eventual consistency (weak): updates can occur in different orders at different replicas; reads can return stale values.
3. Monotonic read: you never again see a value older than one you just read.
4. Monotonic write: an update finishes before any further update you issue for the same value.
5. Read your own writes: you always see your own most recent updates.
6. Stronger guarantees require more coordination, raising latency and lowering availability.
7. Distributed consistency is different from the "C" in ACID (which means transactions preserve database constraints).

# Construction / Recognition

## To Construct/Create:
1. Determine the visibility/ordering/recency guarantees each part of the application needs.
2. Choose the weakest model that still satisfies correctness, to limit coordination cost.
3. For strong consistency, use a proven consensus protocol rather than inventing one.

## To Identify/Recognize:
1. Recognize a model by what it guarantees about staleness and ordering of reads and writes.

# Context & Application

- **Typical contexts**: Any distributed system replicating data across nodes.
- **Common applications**: Different parts of one application may need different models — user registration needs strong consistency, data delivery may tolerate eventual consistency.
- **Historical/stylistic notes**: Databases such as Riak can simultaneously support both strong and eventual consistency, letting the application choose (p. 419).

# Examples

**Example 1** (p. 415): Under the monotonic read model you are guaranteed never to see a value older than the one you just read; under monotonic write, any update you issue finishes before further updates you issue for the same value.

**Example 2** (pp. 418-419): A fitness tracker application — user registration requires strong consistency so two users cannot register the same username, while data delivery favors high availability over fully consistent updates.

# Relationships

## Builds Upon
- **Sharing data** — Consistency models govern replicated/shared data

## Enables
- Choosing a consistency model enables appropriate latency/availability tradeoffs.

## Related
- **Eventual consistency** — The weakest model on the spectrum
- **Consensus protocol** — Used to achieve strong consistency
- **Cap theorem** — Frames the consistency-versus-availability choice

## Contrasts With
- **Eventual consistency** — The weak end of the spectrum, contrasted with stronger models

# Common Errors

- **Error**: Applying strong consistency uniformly across an application
  **Correction**: Different parts of the same application can require different tradeoffs; use the weakest model that preserves correctness.

# Common Confusions

- **Confusion**: Distributed-systems consistency is the same as the "C" in ACID.
  **Clarification**: ACID consistency means transactions preserve database constraints upon completion; distributed consistency levels concern visibility, ordering, and recency across replicas.

# Source Reference

Chapter 13: Systems That Never Stop, "Consistency," pages 415-416, and "CAP Confusion," pages 417-419.

# Verification Notes

- Definition source: Direct quotes from pp. 415-416.
- Confidence rationale: HIGH — the source explicitly enumerates and defines several consistency models.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
