---
# === CORE IDENTIFICATION ===
concept: Fully Connected Network
slug: fully-connected-network

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-transport
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Distributed Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fully meshed network
  - fully meshed cluster
  - fully connected cluster

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
extends: []
related:
  - hidden-node
  - cluster
contrasts_with:
  - hidden-node
  - peer-to-peer-architecture

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fully connected network in distributed Erlang?"
  - "How does distributed Erlang relate to scaling a system out?"
---

# Quick Definition

A fully connected (fully meshed) network is the default distributed Erlang topology in which every visible node is directly connected to every other. It scales well to roughly 70-100 nodes before performance degrades.

# Core Definition

In a fully connected distributed Erlang cluster, "when a new node is added to the cluster, information on all visible (nonhidden) nodes that share the secret cookie gets propagated to it, connections are set up, and monitoring kicks in" (Cesarini & Vinoski, p. 385). Such clusters "are ideal for systems of certain size and requirements" but, depending on node configuration and message size/frequency, "scale at the time of writing to about 70 to 100 nodes before performance degradation starts becoming evident" (p. 385).

# Prerequisites

- **Distributed Erlang** — A fully connected network is the default topology of distributed Erlang; understand it first.

# Key Properties

1. Every visible (non-hidden) node is directly connected to every other.
2. Adding a node propagates information about all visible nodes that share the secret cookie.
3. Connections and monitoring are set up automatically.
4. Connection count grows quadratically: N nodes produce N(N-1)/2 TCP connections.
5. Heartbeats run across all connections, creating node and network overhead.
6. Scales to roughly 70-100 nodes before performance degradation; further bottlenecks include `rex` and the net kernel.

# Construction / Recognition

## To Construct/Create:
1. Start distributed Erlang nodes sharing a secret cookie.
2. Connect them; the runtime automatically fully meshes all visible nodes.

## To Identify/Recognize:
1. Every node has a direct connection and heartbeat to every other visible node.

# Context & Application

- **Typical contexts**: Small-to-medium clusters within a single data center behind a firewall.
- **Common applications**: The vast majority of Erlang systems handling up to tens of thousands of requests per second.
- **Historical/stylistic notes**: To scale beyond the full-mesh limit, use hidden nodes as gateways, or frameworks such as Riak Core and SD Erlang (pp. 385-386).

# Examples

**Example 1** (p. 385): With 100 connected nodes you get 5,050 TCP connections (100+99+...+2+1) and heartbeats across them all, creating overhead in both the nodes and the network.

**Example 2** (p. 386): Hidden nodes act as gateways stopping the propagation of information across clusters of fully meshed nodes, providing isolation and scalability.

# Relationships

## Builds Upon
- **Distributed Erlang** — The fully connected network is its default topology

## Enables
- Fully connected networks underpin small distributed Erlang clusters and Riak Core rings.

## Related
- **Hidden node** — Used to break up full meshes for scalability
- **Cluster** — A fully connected network is a way of structuring a cluster

## Contrasts With
- **Hidden node** — Hidden nodes deliberately do not join the full mesh
- **Peer-to-peer architecture** — P2p forms ad hoc, changing connections rather than a full mesh

# Common Errors

- **Error**: Scaling a fully meshed cluster past ~100 nodes
  **Correction**: Use hidden nodes as gateways, or move to Riak Core or SD Erlang.

# Common Confusions

- **Confusion**: A fully connected network is required for distributed Erlang.
  **Clarification**: It is the default for visible nodes, but hidden nodes and partially connected designs (s_groups in SD Erlang) are possible.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang," pages 385-386. See Figure 13-3.

# Verification Notes

- Definition source: Synthesized from pp. 385-386; connection-count example quoted directly.
- Confidence rationale: HIGH — the source explicitly discusses the fully meshed topology and its scaling limits.
- Uncertainties: The 70-100 node figure is stated as "at the time of writing."
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
