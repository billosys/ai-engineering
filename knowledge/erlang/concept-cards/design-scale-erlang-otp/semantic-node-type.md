---
# === CORE IDENTIFICATION ===
concept: Semantic Node Type
slug: semantic-node-type

# === CLASSIFICATION ===
category: distribution
subcategory: node-model
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Node Types and Families"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - node type
  - semantic node types

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - otp-release
extends: []
related:
  - front-end-node
  - logic-node
  - service-node
  - node-family
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I split a system into node types?"
  - "What concepts are needed before designing distributed architectures?"
---

# Quick Definition

A semantic node type classifies a node by the overall functionality and purpose it serves in a cluster. The three common types are front-end, logic (back-end), and service nodes.

# Core Definition

Semantic node types "classify the functionality and purpose of the nodes in the cluster" (Cesarini & Vinoski, p. 379). They describe the overall responsibility of each node. A single node — especially in small or simple systems — could have multiple responsibilities and act as front-end, logic, and service node all in one. In a multinode system, the responsibilities of the node types are spread across multiple nodes for maintainability, scalability, and availability (p. 380).

# Prerequisites

- **Erlang node** — Node types classify nodes; you must understand the node first.
- **OTP release** — Node type identity is established by the shared release file.

# Key Properties

1. A node type describes the overall responsibility/purpose of a node, not a strict technical boundary.
2. The three common semantic types are front-end, logic (back-end), and service nodes.
3. One node may carry multiple responsibilities (multiple types) in a small system.
4. Splitting responsibilities across node types isolates failure and enables independent tuning of the VM and hardware.
5. Memory-bound and CPU-bound functionality should be kept in separate node types where possible.

# Construction / Recognition

## To Construct/Create:
1. Break the system's functionality down into manageable, standalone responsibilities.
2. Categorize those responsibilities as front-end, logic, or service.
3. Keep memory-bound and CPU-bound functionality in separate node types.
4. Assign each responsibility its own node type (or combine in simple systems).

## To Identify/Recognize:
1. Determine what a node is responsible for: external connectivity (front-end), business logic (logic), or a backing service (service).

# Context & Application

- **Typical contexts**: The first step in designing a distributed architecture — splitting system functionality into standalone nodes.
- **Common applications**: Three-layer architecture (front-end -> logic -> service); fine-tuning hardware per node type for cost and performance.
- **Historical/stylistic notes**: The terminology was discussed and formalized as part of the RELEASE EU-funded research project (p. 379).

# Examples

**Example 1** (p. 379, Figure 13-1): An HTTP-handling system with three semantic node types — a web server front-end node, a logic node, and a database service node.

**Example 2** (p. 380): A node running an Erlang web server, OTP glue/business logic, and an Erlang database all in one VM acts as front-end, logic, and service node simultaneously — convenient but a single point of failure.

# Relationships

## Builds Upon
- **Erlang node** — Node types are a classification of nodes
- **OTP release** — Shared release files establish type identity

## Enables
- **Front-end node** — A specific semantic node type
- **Logic node** — A specific semantic node type
- **Service node** — A specific semantic node type
- **Node family** — Node types running the same release form a family

## Related
- **Node family** — Node types group into families

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Building one node that does everything in a non-trivial system
  **Correction**: Combining everything reduces internode I/O but creates a single point of failure and limits scaling; split responsibilities across node types.

- **Error**: Mixing memory-bound and CPU-bound work in the same node type
  **Correction**: Keep them separate to enable per-type VM and hardware tuning.

# Common Confusions

- **Confusion**: Node types are rigid technical categories enforced by the runtime.
  **Clarification**: Node types are merely a way for designers to describe the overall responsibility of each node; one node can hold several.

# Source Reference

Chapter 12: Distributed Architectures, "Node Types and Families," pages 379-381. See Figure 13-1 (semantic node types).

# Verification Notes

- Definition source: Direct quote from p. 379; synthesized with discussion on p. 380.
- Confidence rationale: HIGH — the source explicitly introduces and names the concept and its three subtypes.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
