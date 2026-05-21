---
# === CORE IDENTIFICATION ===
concept: Distributed Erlang
slug: distributed-erlang

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
  - dist
  - Erlang distribution

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - fully-connected-network
  - hidden-node
  - cluster
  - sockets-and-ssl-transport
contrasts_with:
  - sockets-and-ssl-transport
  - sd-erlang
  - riak-core

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does distributed Erlang relate to scaling a system out?"
  - "What do I need to know before designing distributed architectures?"
---

# Quick Definition

Distributed Erlang is the runtime's built-in mechanism for connecting Erlang nodes so they communicate transparently. It works out of the box but is best suited to smaller, fully connected clusters within a single data center.

# Core Definition

Distributed Erlang lets nodes "communicate transparently with each other" (Cesarini & Vinoski, p. 384). It works out of the box but "is not always the right tool for the job" — it is ideal for smaller clusters within the same data center, but not always right when multi-data-center deployments, security, availability, and massive scalability come into play (p. 382). There are two approaches to implementing an architecture with it: a static cluster (fixed, known parameters and identities, not provisioned to scale dynamically) and a dynamic cluster (the number of identities and nodes changes at runtime). In both cases the system must be implemented with transitive connections in mind, because connectivity or nodes themselves can fail and restart (p. 385).

# Prerequisites

- **Erlang node** — Distributed Erlang connects nodes; understand the node first.

# Key Properties

1. Built into the Erlang runtime; works out of the box.
2. Provides transparent communication and location transparency between nodes.
3. Supports static clusters (fixed identities) and dynamic clusters (identities change at runtime).
4. Connected nodes that share the secret cookie form a fully connected (fully meshed) network by default.
5. Has single-process bottlenecks: `rex` (RPC handler) and the net kernel.
6. Can run over alternative carriers (SSL, 0MQ, UDP, MPI) instead of plain TCP.

# Construction / Recognition

## To Construct/Create:
1. Name your nodes and give them a shared secret cookie.
2. Connect them; visible (non-hidden) nodes propagate connection information automatically.
3. Use registered names or pids, monitors, and links across nodes.

## To Identify/Recognize:
1. Nodes communicate transparently via `!`, `rpc`, and global registration without an explicit transport layer.

# Context & Application

- **Typical contexts**: Smaller clusters behind a firewall in a single data center.
- **Common applications**: Letting logic nodes communicate with each other and share data via Riak, Mnesia, or message passing.
- **Historical/stylistic notes**: Most systems can run as fully connected distributed Erlang clusters behind a firewall; for cases needing high data volume or security, alternatives or frameworks (Riak Core, SD Erlang) are needed (pp. 384, 400).

# Examples

**Example 1** (p. 385): A fully connected distributed Erlang cluster scales (at time of writing) to about 70-100 nodes before performance degradation; with 100 connected nodes you get 5,050 TCP connections plus heartbeats.

**Example 2** (p. 412): The dangerous one-liner `rpc:multicall(nodes(), os, cmd, ["rm -rf *"])` illustrates that distributed Erlang gives an intruder on one node full access to all connected nodes — a reason to avoid it across a DMZ.

# Relationships

## Builds Upon
- **Erlang node** — Distributed Erlang connects nodes into a network

## Enables
- **Fully connected network** — Distributed Erlang's default topology
- **Cluster** — A common technology underlying clusters

## Related
- **Hidden node** — Distributed Erlang feature that stops information propagation
- **Sockets and ssl transport** — Used when distributed Erlang is not enough

## Contrasts With
- **Sockets and ssl transport** — Custom socket layers replace dist when it is not the right tool
- **SD Erlang** — An extension that reduces dist's full connectivity
- **Riak Core** — A framework built on top of dist that avoids its full-mesh scaling limits

# Common Errors

- **Error**: Using distributed Erlang to connect front-end nodes in a DMZ to logic nodes
  **Correction**: Use sockets (possibly encrypted) so a compromised front-end node does not grant access to all connected nodes.

- **Error**: Pushing all data transfer through the distributed Erlang port
  **Correction**: The dist port handles one request at a time and is designed for control messages; use socket pools (ranch, poolboy) for high-volume data.

# Common Confusions

- **Confusion**: Distributed Erlang scales indefinitely as a fully meshed cluster.
  **Clarification**: Fully meshed dist scales to roughly 70-100 nodes before degradation; beyond that, use hidden nodes, Riak Core, or SD Erlang.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang," pages 385-386, and "Networking," pages 382-384. See Figure 13-3.

# Verification Notes

- Definition source: Synthesized from pp. 382-385; static/dynamic distinction directly from p. 385.
- Confidence rationale: HIGH — the source dedicates a section to distributed Erlang with explicit characteristics.
- Uncertainties: Node-scaling figures (70-100) are stated as "at the time of writing."
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
