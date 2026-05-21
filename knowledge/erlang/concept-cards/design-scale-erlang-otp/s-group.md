---
# === CORE IDENTIFICATION ===
concept: S_group
slug: s-group

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
section: "Distributed Erlang — Scalable Distributed Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - s_group
  - node group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sd-erlang
extends: []
related:
  - semi-explicit-placement
  - hidden-node
contrasts_with:
  - fully-connected-network

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an s_group in SD Erlang?"
  - "How does SD Erlang reduce network connectivity?"
---

# Quick Definition

An s_group is the SD Erlang layer that groups nodes so that members transitively share connections and a namespace; nodes shared between s_groups act as gateways.

# Core Definition

"SD Erlang defines a new layer called an s_group. Nodes can belong to zero, one, or more s_groups, and nodes that belong to the same s_group transitively share connections and a namespace. A namespace is a set of names registered using the `global:register_name/2` function in distributed Erlang or the `s_group:register_name/3` function in SD Erlang. Names registered in distributed Erlang are replicated on all connected normal (not hidden) nodes. In SD Erlang, the name is replicated on all nodes of the given s_group" (Cesarini & Vinoski, pp. 390-391).

# Prerequisites

- **SD Erlang** — The s_group is the central construct of SD Erlang; understand SD Erlang first.

# Key Properties

1. A node can belong to zero, one, or more s_groups.
2. Nodes in the same s_group transitively share connections.
3. Nodes in the same s_group share a namespace.
4. Names registered with `s_group:register_name/3` are replicated only on nodes of that s_group.
5. A node shared between two s_groups acts as a gateway, transmitting messages between them.
6. S_groups reduce connectivity and namespace size compared with full distributed Erlang.

# Construction / Recognition

## To Construct/Create:
1. Assign nodes to one or more s_groups.
2. Register names within an s_group using `s_group:register_name/3`.
3. Share a node between s_groups to create a gateway.
4. Arrange nodes in different configurations by clustering and connecting them via gateways.

## To Identify/Recognize:
1. Recognize an s_group as a partial-connectivity group whose namespace is replicated only within the group.

# Context & Application

- **Typical contexts**: Large SD Erlang systems scaling beyond the distributed Erlang full-mesh limit.
- **Common applications**: Clustering nodes and connecting clusters via gateway nodes.
- **Historical/stylistic notes**: SD Erlang's node-group concept lets a programmer arrange nodes in different configurations (p. 391).

# Examples

**Example 1** (p. 391, Figure 13-7): Two s_groups G1 and G2, each with three Erlang nodes; node C belongs to both s_groups and acts as a gateway.

**Example 2** (pp. 390-391): In distributed Erlang, names registered with `global:register_name/2` are replicated on all connected normal nodes; in SD Erlang, a name registered with `s_group:register_name/3` is replicated only on nodes of the given s_group.

# Relationships

## Builds Upon
- **SD Erlang** — The s_group is the layer SD Erlang adds

## Enables
- S_groups enable partial connectivity and partitioned namespaces, the basis of SD Erlang scalability.

## Related
- **Semi-explicit placement** — Complements s_groups in SD Erlang
- **Hidden node** — Both provide isolation between groups of nodes

## Contrasts With
- **Fully connected network** — In a full mesh all visible nodes connect and share a namespace; s_groups limit both to group members

# Common Errors

- **Error**: Registering a global name expecting it to be visible across all s_groups
  **Correction**: `s_group:register_name/3` replicates the name only within the given s_group; use a gateway node to bridge groups.

# Common Confusions

- **Confusion**: A node can belong to only one s_group.
  **Clarification**: A node can belong to zero, one, or more s_groups; nodes in multiple s_groups act as gateways.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Scalable Distributed Erlang," pages 390-391. See Figure 13-7.

# Verification Notes

- Definition source: Direct quote from pp. 390-391.
- Confidence rationale: HIGH — the source explicitly defines the s_group and namespace.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
