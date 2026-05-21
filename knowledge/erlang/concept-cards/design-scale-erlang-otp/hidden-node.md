---
# === CORE IDENTIFICATION ===
concept: Hidden Node
slug: hidden-node

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-transport
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Distributed Erlang"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - hidden nodes
  - gateway node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - fully-connected-network
extends: []
related:
  - cluster
  - riak-core
contrasts_with:
  - fully-connected-network

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a hidden node?"
  - "How does distributed Erlang relate to scaling a system out?"
---

# Quick Definition

A hidden node is a distributed Erlang node that does not join the full mesh of visible nodes; it acts as a gateway that stops information from propagating across fully meshed clusters.

# Core Definition

"Hidden nodes ... act as gateways stopping the propagation of information across clusters of fully meshed nodes. They provide you with isolation and scalability, but you have to build frameworks that sit on top of them" (Cesarini & Vinoski, p. 386). Because they do not join the visible full mesh, information about all visible nodes is not propagated to them, which lets them link separate fully meshed clusters without merging them.

# Prerequisites

- **Distributed Erlang** — Hidden nodes are a distributed Erlang feature.
- **Fully connected network** — Hidden nodes exist to break up the full mesh; understand the mesh first.

# Key Properties

1. A hidden node does not join the fully meshed network of visible nodes.
2. It stops the propagation of node information across clusters of fully meshed nodes.
3. It can act as a gateway connecting separate fully meshed clusters.
4. It provides isolation and scalability.
5. Using hidden nodes requires building frameworks on top of them.

# Construction / Recognition

## To Construct/Create:
1. Start a node configured as hidden.
2. Connect it to nodes in multiple clusters as a gateway.
3. Build a framework atop it to route messages between clusters.

## To Identify/Recognize:
1. A hidden node does not appear in the `nodes()` list of visible nodes and is not part of the automatic full mesh.

# Context & Application

- **Typical contexts**: Scaling distributed Erlang beyond the ~100-node full-mesh limit.
- **Common applications**: Gateways between fully meshed clusters; running multiple Riak Core clusters connected via hidden nodes acting as gateways (p. 389).
- **Historical/stylistic notes**: Node connections and visibility are covered in detail earlier in the book ("Node Connections and Visibility," p. 49).

# Examples

**Example 1** (p. 386): Hidden nodes act as gateways stopping the propagation of information across clusters of fully meshed nodes, providing isolation and scalability.

**Example 2** (p. 389): More complex Riak Core patterns include running multiple Riak Core clusters connected to each other via hidden nodes acting as gateways.

# Relationships

## Builds Upon
- **Distributed Erlang** — Hidden nodes are a feature of distributed Erlang
- **Fully connected network** — They exist to break up the full mesh

## Enables
- Hidden nodes enable scaling beyond the full-mesh limit and connecting separate clusters.

## Related
- **Cluster** — Hidden nodes act as gateways between clusters
- **Riak Core** — Riak Core clusters can be connected via hidden-node gateways

## Contrasts With
- **Fully connected network** — Hidden nodes deliberately do not join the full mesh

# Common Errors

- **Error**: Expecting hidden nodes to route cross-cluster traffic automatically
  **Correction**: They provide isolation, but you must build the routing framework that sits on top of them.

# Common Confusions

- **Confusion**: A hidden node is disconnected or invisible to everything.
  **Clarification**: It is connected to specific nodes but excluded from the automatic full mesh and information propagation among visible nodes.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang," page 386. See also "Node Connections and Visibility," page 49.

# Verification Notes

- Definition source: Direct quote from p. 386.
- Confidence rationale: MEDIUM — chapters 12-15 describe the hidden node's role as a gateway but defer the detailed visibility mechanics to an earlier chapter (p. 49).
- Uncertainties: Configuration mechanics covered earlier in the book, not chapters 12-15.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
