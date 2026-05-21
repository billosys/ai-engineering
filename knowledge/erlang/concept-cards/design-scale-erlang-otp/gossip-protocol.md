---
# === CORE IDENTIFICATION ===
concept: Gossip Protocol
slug: gossip-protocol

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - gossip
  - epidemic protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - riak-core
extends: []
related:
  - peer-to-peer-architecture
  - hinted-handoff
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a gossip protocol?"
  - "How do masterless peer nodes share cluster state?"
---

# Quick Definition

A gossip protocol is a communication scheme in which peer nodes share information — such as cluster topology changes — with randomly selected other nodes, so updates propagate and the system self-heals.

# Core Definition

In Riak Core, "nodes use a gossip protocol to communicate shared information such as cluster topology changes and the vnode claims to other randomly selected nodes. If updates to the cluster topology were missed on particular nodes for whatever reason, the gossip protocol forwards these changes, ensuring that the system heals itself" (Cesarini & Vinoski, p. 388).

# Prerequisites

- **Riak Core** — The gossip protocol is described in the context of Riak Core's masterless peer nodes.

# Key Properties

1. Peer nodes share information with other randomly selected nodes.
2. The shared information includes cluster topology changes and vnode claims.
3. Missed updates are eventually forwarded by continued gossiping.
4. The protocol ensures the system heals itself after missed updates.
5. It suits masterless, peer-based architectures with no central coordinator.

# Construction / Recognition

## To Construct/Create:
1. Have each node periodically pick random peer nodes.
2. Exchange shared state (topology, vnode claims) with those peers.
3. Continue gossiping so missed updates eventually reach all nodes.

## To Identify/Recognize:
1. Recognize a gossip protocol by random peer-to-peer exchange of state with eventual convergence, rather than a central broadcast.

# Context & Application

- **Typical contexts**: Masterless peer-node clusters such as Riak Core.
- **Common applications**: Propagating cluster topology changes and vnode claims; self-healing after missed updates.
- **Historical/stylistic notes**: The chapter also lists Gossip among peer-to-peer protocols alongside BitTorrent, Gnutella, and Kazaa (p. 395).

# Examples

**Example 1** (p. 388): Riak Core nodes, which are peers with no master node, use a gossip protocol to communicate topology changes and vnode claims to randomly selected nodes.

**Example 2** (p. 388): If updates to the cluster topology were missed on particular nodes, the gossip protocol forwards these changes, ensuring the system heals itself.

# Relationships

## Builds Upon
- **Riak Core** — The gossip protocol is described as part of Riak Core's masterless design

## Enables
- The gossip protocol enables self-healing propagation of cluster state.

## Related
- **Peer to peer architecture** — Gossip is a peer-to-peer communication style
- **Hinted handoff** — Both contribute to Riak Core's self-healing

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Relying on a single broadcast to keep all nodes in sync
  **Correction**: Use a gossip protocol so missed updates are eventually forwarded and the system converges.

# Common Confusions

- **Confusion**: Gossip guarantees every node sees an update immediately.
  **Clarification**: Gossip provides eventual propagation through repeated random exchange, not instantaneous consistency.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Riak Core," page 388, and "Peer to Peer," page 395.

# Verification Notes

- Definition source: Direct quote from p. 388.
- Confidence rationale: MEDIUM — the source describes the gossip protocol's role in Riak Core clearly but does not give a standalone formal definition of gossip protocols in general.
- Uncertainties: General gossip-protocol mechanics are only briefly characterized.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
