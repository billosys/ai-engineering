---
# === CORE IDENTIFICATION ===
concept: Vnode
slug: vnode

# === CLASSIFICATION ===
category: distribution
subcategory: data-distribution
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
  - virtual node
  - vnodes

# === TYPED RELATIONSHIPS ===
prerequisites:
  - riak-core
  - consistent-hashing
extends: []
related:
  - hinted-handoff
  - sloppy-quorum
contrasts_with:
  - erlang-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a vnode?"
  - "How is data spread evenly across a distributed cluster?"
---

# Quick Definition

A vnode (virtual node) is a unit in Riak Core that claims a range of the consistent-hash space; physical nodes host many vnodes, decoupling data ownership from physical node count.

# Core Definition

"Riak Core runs on a cluster of physical nodes overlaid with a system of virtual nodes, also known as vnodes. The number of vnodes is configurable, but a typical Riak Core cluster includes 15-20 physical nodes that collectively host 256 vnodes. Each vnode claims a range of the 160-bit integer space of the SHA-1 hash function" (Cesarini & Vinoski, p. 387). When a Riak Core cluster is first created, physical nodes claim ownership of vnodes such that adjacent vnodes are not stored on the same physical node (p. 388).

# Prerequisites

- **Riak Core** — Vnodes are a Riak Core construct; understand the framework first.
- **Consistent hashing** — Vnodes claim ranges of the consistent-hash space.

# Key Properties

1. A vnode is a virtual node overlaid on a cluster of physical nodes.
2. The number of vnodes is configurable (e.g., 256 vnodes over 15-20 physical nodes).
3. Each vnode claims a range of the 160-bit SHA-1 hash space.
4. Adjacent vnodes are placed on different physical nodes so replicas land on distinct nodes.
5. Adding or removing a physical node moves only a few vnodes, not all data.

# Construction / Recognition

## To Construct/Create:
1. Configure the desired number of vnodes for the cluster.
2. Have physical nodes claim ownership of vnodes so adjacent vnodes are on different physical nodes.
3. Assign each vnode a range of the consistent-hash space.

## To Identify/Recognize:
1. Recognize a vnode as a hash-range owner that is hosted by, but distinct from, a physical node.

# Context & Application

- **Typical contexts**: Riak Core clusters and the Riak key-value store.
- **Common applications**: Decoupling data ownership from physical node count so clusters can start small and grow with minimal disruption.
- **Historical/stylistic notes**: By storing replicas in consecutive vnodes on a cluster of at least five physical nodes, Riak Core tries to guarantee replicas land on different physical nodes (p. 388).

# Examples

**Example 1** (p. 388, Figure 13-4): When looking up a value, the hash of the key points to a vnode, which in turn points to the primary Erlang node responsible for that value.

**Example 2** (p. 388): In a 16-node cluster, taking node 1 out of service redistributes vnodes 1, 17, 33, and 49 across existing nodes; if a new node is added, four vnodes move to it from their current locations.

# Relationships

## Builds Upon
- **Riak Core** — Vnodes are part of Riak Core's architecture
- **Consistent hashing** — Vnodes claim ranges of the consistent-hash space

## Enables
- **Hinted handoff** — Data is stored in alternative vnodes when primaries are down
- **Sloppy quorum** — Quorums can comprise primary or alternative vnodes

## Related
- **Hinted handoff** — Operates over vnodes
- **Sloppy quorum** — Counts vnode acknowledgments

## Contrasts With
- **Erlang node** — A vnode is a virtual hash-range owner; an Erlang node is a physical runtime instance hosting many vnodes

# Common Errors

- **Error**: Running a Riak Core cluster with fewer than the recommended physical nodes
  **Correction**: At least the recommended five physical nodes are needed for Riak Core to guarantee replicas land on different physical nodes.

# Common Confusions

- **Confusion**: A vnode is the same as a physical Erlang node.
  **Clarification**: A vnode is virtual; many vnodes are hosted on each physical node, and vnodes can move between physical nodes when the cluster rebalances.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," pages 387-388. See Figure 13-4.

# Verification Notes

- Definition source: Direct quote from p. 387.
- Confidence rationale: HIGH — explicit definition and worked rebalancing example in source.
- Uncertainties: Vnode/physical-node counts stated as typical.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
