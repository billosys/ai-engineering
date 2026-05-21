---
# === CORE IDENTIFICATION ===
concept: Consistent Hashing
slug: consistent-hashing

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
  - consistent hash

# === TYPED RELATIONSHIPS ===
prerequisites:
  - riak-core
extends: []
related:
  - vnode
  - partitioning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is consistent hashing?"
  - "How is data spread evenly across a distributed cluster?"
---

# Quick Definition

Consistent hashing spreads key-value data evenly across a cluster while minimizing the amount of data relocation required when nodes are added or removed.

# Core Definition

"Each vnode claims a range of the 160-bit integer space of the SHA-1 hash function, which Riak Core uses as the basis of its consistent hashing system. Consistent hashing spreads key-value data evenly across the cluster while minimizing the amount of data relocation required as physical nodes are operationally added to or removed from the cluster" (Cesarini & Vinoski, p. 387). A key is hashed to a value, and the vnode owning the range that includes that hash value owns the key.

# Prerequisites

- **Riak Core** — Consistent hashing is presented as the basis of Riak Core's data model; understand Riak Core first.

# Key Properties

1. Maps keys onto a fixed hash space (in Riak Core, the 160-bit SHA-1 integer space).
2. Each vnode owns a contiguous range of the hash space.
3. A key is owned by the vnode whose range includes the key's hash value.
4. Spreads key-value data evenly across the cluster.
5. Minimizes data relocation when nodes are added to or removed from the cluster.

# Construction / Recognition

## To Construct/Create:
1. Choose a hash function and divide its output space into ranges, one per vnode.
2. Assign each range to a vnode (and each vnode to a physical node).
3. To place a key, hash it and find the vnode whose range contains the hash value.

## To Identify/Recognize:
1. Recognize consistent hashing when adding/removing a node moves only the affected ranges, not all data.

# Context & Application

- **Typical contexts**: Distributed key-value stores and any system sharding data across nodes.
- **Common applications**: Riak Core's data distribution; sharding data and load-balancing jobs across a cluster.
- **Historical/stylistic notes**: Used together with vnodes so that adding or removing physical nodes affects only a few vnodes' worth of data.

# Examples

**Example 1** (p. 387): To store data, Riak Core hashes the key to obtain its hash value, then determines which vnode owns the range of 160-bit values that includes that hash value.

**Example 2** (p. 388): In a 16-node cluster, removing node 1 redistributes only vnodes 1, 17, 33, and 49 — not all data — because consistent hashing localizes the reshuffling.

# Relationships

## Builds Upon
- **Riak Core** — Consistent hashing is the basis of Riak Core's data model

## Enables
- **Vnode** — Vnodes claim hash ranges defined by consistent hashing
- **Partitioning** — Consistent hashing is one way to partition data

## Related
- **Partitioning** — Consistent hashing is a partitioning technique

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting no data movement at all when scaling
  **Correction**: Consistent hashing minimizes relocation, but the ranges owned by added/removed nodes still move.

# Common Confusions

- **Confusion**: Consistent hashing keeps data on the same node forever.
  **Clarification**: It minimizes relocation; vnodes that stay in service keep their data, but ranges belonging to added/removed nodes are moved.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," pages 387-388. See Figure 13-4.

# Verification Notes

- Definition source: Direct quote from p. 387.
- Confidence rationale: HIGH — the source explicitly defines consistent hashing and its benefit.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
