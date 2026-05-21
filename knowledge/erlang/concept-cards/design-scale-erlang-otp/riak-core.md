---
# === CORE IDENTIFICATION ===
concept: Riak Core
slug: riak-core

# === CLASSIFICATION ===
category: distribution
subcategory: distributed-frameworks
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
  - riak_core

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - fully-connected-network
extends: []
related:
  - consistent-hashing
  - vnode
  - sloppy-quorum
  - hinted-handoff
  - gossip-protocol
  - eventual-consistency
contrasts_with:
  - sd-erlang
  - distributed-erlang

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Riak Core?"
  - "How does distributed Erlang relate to scaling a system out?"
---

# Quick Definition

Riak Core is a distributed framework, built on top of distributed Erlang, that provides an eventually consistent replicated data model on a cluster of masterless peer nodes, using consistent hashing for high availability with no single point of failure.

# Core Definition

"Riak Core is a framework that provides an eventually consistent replicated data model on a system of masterless peer nodes providing high availability and helping guarantee no single point of failure. It is built on top of distributed Erlang and is the foundation of the distributed Riak key-value store, based on ideas from the 2007 Dynamo paper from Amazon" (Cesarini & Vinoski, p. 386). It runs a cluster of physical nodes overlaid with a configurable system of virtual nodes (vnodes) and uses consistent hashing over the 160-bit SHA-1 space.

# Prerequisites

- **Distributed Erlang** — Riak Core is built on top of distributed Erlang.
- **Fully connected network** — Riak Core nodes form a fully meshed ring; understand the topology first.

# Key Properties

1. Built on top of distributed Erlang; foundation of the Riak key-value store.
2. Provides an eventually consistent replicated data model.
3. Runs on masterless peer nodes — no master node, eliminating a single point of failure.
4. Overlays physical nodes with configurable virtual nodes (vnodes), e.g., ~256 vnodes on 15-20 physical nodes.
5. Uses consistent hashing over the 160-bit SHA-1 integer space.
6. Replicates each write N times (default N=3); writes succeed at W acknowledgments, reads at R results (default W=R=N/2+1).
7. Limited to about a hundred nodes in the core, which can act as hubs/gateways to other clusters.

# Construction / Recognition

## To Construct/Create:
1. Deploy a cluster of at least the recommended five physical nodes.
2. Configure a number of vnodes; physical nodes claim ownership of ranges of the hash space.
3. Hash keys to vnodes; store N replicas across consecutive vnodes.
4. Tune N, W, and R for the desired availability/consistency tradeoff.

## To Identify/Recognize:
1. Recognize Riak Core by its masterless ring of physical nodes hosting vnodes with consistent hashing.

# Context & Application

- **Typical contexts**: Systems requiring high availability and self-healing after node or network failures.
- **Common applications**: Distributed key-value storage; logic nodes forming a fully meshed ring used for messaging, job scheduling, and request routing; star architectures for storage and analytics.
- **Historical/stylistic notes**: Based on the 2007 Amazon Dynamo paper; created and maintained by Basho. Related projects include NkCLUSTER and NkDIST.

# Examples

**Example 1** (p. 387): To store data, a client sends a write with key and value; Riak Core hashes the key, finds the owning vnode, and stores N copies (default 3) — one in the primary vnode and the rest in the next N-1 vnodes — completing when W copies are written.

**Example 2** (p. 388): In a 16-node cluster, permanently removing node 1 causes Riak Core to redistribute only vnodes 1, 17, 33, and 49 across existing nodes, without reshuffling all data.

# Relationships

## Builds Upon
- **Distributed Erlang** — Riak Core is built on top of it
- **Fully connected network** — Riak Core nodes form a fully meshed ring

## Enables
- **Consistent hashing** — Riak Core's data-distribution mechanism
- **Vnode** — Riak Core's unit of virtual node
- **Sloppy quorum** — Riak Core's quorum model
- **Hinted handoff** — Riak Core's data-recovery mechanism
- **Gossip protocol** — How Riak Core nodes share topology

## Related
- **Eventual consistency** — Riak Core's data-model guarantee

## Contrasts With
- **SD Erlang** — A different approach to scaling distributed Erlang
- **Distributed Erlang** — Riak Core builds on it but avoids its full-mesh scaling limits as a giant switch

# Common Errors

- **Error**: Using Riak Core just because it exists
  **Correction**: Ask whether the problem falls into the category of problems consistent hashing and Riak Core solve; do not over-engineer.

# Common Confusions

- **Confusion**: Riak Core has a master node.
  **Clarification**: Riak Core nodes are peers; there is no master node, and a gossip protocol keeps topology consistent.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," pages 386-390. See Figures 13-4, 13-5, 13-6.

# Verification Notes

- Definition source: Direct quote from p. 386.
- Confidence rationale: HIGH — the source gives a multi-page treatment with an explicit definition.
- Uncertainties: Node-count figures stated as typical/at-time-of-writing.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
