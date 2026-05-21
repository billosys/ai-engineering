---
# === CORE IDENTIFICATION ===
concept: Hinted Handoff
slug: hinted-handoff

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
  - hinted handoffs

# === TYPED RELATIONSHIPS ===
prerequisites:
  - riak-core
  - vnode
extends: []
related:
  - sloppy-quorum
  - network-partition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is hinted handoff?"
  - "How does Riak Core stay available during a partition?"
---

# Quick Definition

Hinted handoff is a Riak Core mechanism that stores data in an alternative vnode when the intended primary or replica vnode is unreachable, then hands the data off to the correct vnode once it becomes available.

# Core Definition

"Riak Core uses hinted handoffs to ensure that N copies of the data are stored, even if the primary vnode or some of the replica vnodes are down or unreachable because of a network partition. In such a case, Riak Core stores the data in an alternative vnode and gives that vnode a hint as to where the data really should be stored. When the unreachable vnodes again become available, the alternative vnodes hand the data off to them, thereby healing the system" (Cesarini & Vinoski, p. 388).

# Prerequisites

- **Riak Core** — Hinted handoff is a Riak Core mechanism; understand the framework first.
- **Vnode** — Handoff operates over vnodes.

# Key Properties

1. Ensures N copies of data are stored even when primary or replica vnodes are unreachable.
2. Data is stored in an alternative vnode along with a hint indicating where it really belongs.
3. When the unreachable vnodes become available again, alternative vnodes hand the data off to them.
4. The handoff heals the system after a partition or node failure.
5. Hinted handoffs are part of Riak Core's sloppy-quorum mechanism.

# Construction / Recognition

## To Construct/Create:
1. On a write, attempt to store N copies in the intended vnodes.
2. If a target vnode is unreachable, store the copy in an alternative vnode with a hint.
3. When the target vnode recovers, have the alternative vnode hand off the data.

## To Identify/Recognize:
1. Recognize hinted handoff when data temporarily resides on a non-owning vnode tagged with a hint.

# Context & Application

- **Typical contexts**: Eventually consistent distributed stores recovering from network partitions or node failures.
- **Common applications**: Self-healing of Riak Core clusters after partitions.
- **Historical/stylistic notes**: Works together with sloppy quorums — quorum acknowledgments can come from alternative (handoff) vnodes.

# Examples

**Example 1** (p. 388): When a primary vnode is unreachable because of a network partition, Riak Core stores the data in an alternative vnode with a hint; once the primary recovers, the alternative vnode hands the data off, healing the system.

**Example 2** (p. 388): Hinted handoffs are described as part of Riak Core's sloppy quorums — writes still require W acknowledgments, but those may come from alternative handoff vnodes.

# Relationships

## Builds Upon
- **Riak Core** — Hinted handoff is a Riak Core mechanism
- **Vnode** — Handoff moves data between vnodes

## Enables
- Hinted handoff enables self-healing after partitions and node failures.

## Related
- **Sloppy quorum** — Hinted handoffs are part of the sloppy-quorum mechanism
- **Network partition** — Hinted handoff is what keeps replication intact during a partition

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming data is permanently stored on the alternative vnode
  **Correction**: The alternative vnode holds it only temporarily, with a hint; it hands the data off once the intended vnode recovers.

# Common Confusions

- **Confusion**: Hinted handoff means data is lost when a vnode is down.
  **Clarification**: The opposite — it ensures N copies are kept even when vnodes are unreachable, and reconciles them on recovery.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," page 388.

# Verification Notes

- Definition source: Direct quote from p. 388.
- Confidence rationale: HIGH — the source explicitly defines hinted handoffs.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
