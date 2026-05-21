---
# === CORE IDENTIFICATION ===
concept: Erlang Cluster
slug: erlang-cluster

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2 Nodes and clustering"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cluster"
  - "network of nodes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - connecting-nodes
  - epmd
  - magic-cookie
  - resource-discovery
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang cluster?"
  - "What does fully connected mean for a cluster?"
  - "How large can an Erlang cluster practically be?"
---

# Quick Definition

An Erlang cluster is a group of two or more Erlang nodes that are aware of each other; by default it is fully connected — every node knows and communicates directly with every other node.

# Core Definition

An Erlang cluster (the official documentation calls it a *network of nodes*) is formed when two or more Erlang nodes become aware of each other. By default a cluster is *fully connected*: every node in the cluster knows about every other node and communicates directly with each of them. Nodes also exchange information about any other nodes they are connected to, so when two separate clusters touch they merge into one larger fully connected cluster. As a practical limit a cluster may have a couple of dozen nodes but not hundreds, because the communication overhead of keeping a fully connected network in touch increases quadratically with the number of nodes. Hidden nodes — configured not to propagate node information — can be used to link clusters into larger, not-fully-connected structures (Ch. 8, Section 8.2).

# Prerequisites

- **erlang-node** — A cluster is composed of nodes; the node concept comes first.

# Key Properties

1. Formed by two or more mutually aware nodes.
2. Fully connected by default — every node connects directly to every other.
3. Nodes propagate knowledge of other nodes, so touching clusters merge.
4. Practical size limit is a couple of dozen nodes, not hundreds.
5. Communication overhead grows quadratically with node count.
6. Hidden nodes can join clusters without full propagation.

# Construction / Recognition

## To Form a Cluster:
1. Start two or more nodes with compatible names and the same cookie.
2. Connect them (e.g., `net_adm:ping/1` from one node to another).
3. Connecting more nodes causes transitive merging into one full network.

## To Recognize:
1. Call `nodes()` on a node — a non-empty list of node names indicates cluster membership.

# Context & Application

- **Typical contexts**: Distributed services, replicated data stores, peer-to-peer systems.
- **Common applications**: Distributed caches; resource discovery; Mnesia replication.
- **Historical/stylistic notes**: The book deliberately says "cluster" instead of "network of nodes" to avoid confusion with computer networks.

# Examples

**Example 1** (Section 8.2.2): Nodes `a`, `b`, `c` — connecting `a` to `b` then `b` to `c` results in a fully connected three-node cluster, as `nodes()` on each confirms.

**Example 2** (Section 8.2.2): If clusters `{a,b}` and `{c,d}` exist and `a` connects to `d`, all four nodes merge into one fully connected cluster.

# Relationships

## Builds Upon
- **erlang-node** — Nodes are the members of a cluster.

## Enables
- **resource-discovery** — Resource discovery operates across the nodes of a cluster.

## Related
- **connecting-nodes** — The act that forms a cluster.
- **EPMD** — Underpins how cluster nodes find each other.
- **magic-cookie** — Cookies control which nodes may join a cluster.

## Contrasts With
- None.

# Common Errors

- **Error**: Designing for hundreds of nodes in one fully connected cluster.
  **Correction**: Keep clusters to a couple of dozen nodes; quadratic overhead makes large full meshes impractical.

# Common Confusions

- **Confusion**: Thinking a cluster must be explicitly configured as a whole.
  **Clarification**: A cluster forms organically — nodes propagate knowledge of each other, so touching clusters merge automatically.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2 "Nodes and clustering," Figure 8.4 and the "Hidden nodes" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 8.2.
- Confidence rationale: HIGH — the book explicitly defines a cluster and its full-connectivity property.
- Uncertainties: None.
- Cross-reference status: Verified.
