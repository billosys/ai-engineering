---
# === CORE IDENTIFICATION ===
concept: Resource Discovery Algorithm
slug: resource-discovery-algorithm

# === CLASSIFICATION ===
category: distribution
subcategory: resource-discovery
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.3.2 The algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "resource trading algorithm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resource-discovery
  - resource-discovery-terminology
extends: []
related:
  - resource-discovery-server
  - resource-trading
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the resource discovery algorithm work?"
  - "How does a new node synchronize its resources with a cluster?"
---

# Quick Definition

The resource discovery algorithm synchronizes a joining node with the cluster: the new node broadcasts what it has, peers cache anything matching their "I want" list and reply with their own resources, and each side keeps only what it wants.

# Core Definition

The resource discovery algorithm is the procedure by which nodes synchronize their knowledge of cluster resources (Ch. 8, Section 8.3.2). Consider connected nodes `a` and `b`, already synchronized, when a third node `c` joins. To get in sync, the resource discovery server on `c` sends messages to `a` and `b` informing them of the resources it has locally. The servers on `a` and `b` receive these messages, cache the information about any resource whose type matches their local "I want" list, and then respond by sending information about their own local resources back to `c`. Node `c` caches the resources of types it wants and discards information about types it does not care about. The book describes it as a game of "I'll show you mine, if you show me yours." Because the protocol uses only asynchronous messages and does not strictly depend on getting answers from every node, the system is fairly resilient to failures.

# Prerequisites

- **resource-discovery** — The algorithm is the core of the resource discovery system.
- **resource-discovery-terminology** — The algorithm trades resources, types, and tuples.

# Key Properties

1. Triggered when a node wants to synchronize with the cluster.
2. The joining node broadcasts its local resources to all known nodes.
3. Each receiver caches resources matching its "I want" list.
4. Receivers reply with their own local resources.
5. Each node keeps only resource types it wants, discarding the rest.
6. Uses only asynchronous messages — resilient to missing replies.

# Construction / Recognition

## The Algorithm Steps:
1. The joining node sends its local resource tuples to every known node.
2. Each receiver caches the sender's resources that match its target types.
3. Each receiver replies with its own local resources.
4. The joining node caches received resources of wanted types and discards the others.
5. After all replies are handled, every node has consistent matching information.

## To Recognize:
1. A broadcast of local resources followed by reciprocal replies is the discovery algorithm at work.

# Context & Application

- **Typical contexts**: A node joining or re-synchronizing with a cluster.
- **Common applications**: Caches discovering each other; any service-locating exchange.
- **Historical/stylistic notes**: The book stresses understanding the algorithm before reading the implementation.

# Examples

**Example 1** (Section 8.3.2, Figure 8.6): Node `c` joins with a resource of type `z` (which `a` and `b` want) and seeks type `x`; after trading, `a` and `b` learn about `z@c`, and `c` learns the type-`x` resources while discarding type-`y` ones.

# Relationships

## Builds Upon
- **resource-discovery** — The algorithm is the system's mechanism.
- **resource-discovery-terminology** — It operates on resources, types, and tuples.

## Enables
- **resource-trading** — The `trade_resources` operation drives the algorithm.

## Related
- **resource-discovery-server** — The `gen_server` that executes the algorithm.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting full consistency immediately after triggering trading.
  **Correction**: The exchange is asynchronous; allow time for replies before relying on discovered data.

# Common Confusions

- **Confusion**: Thinking nodes exchange all resources unconditionally.
  **Clarification**: Each node keeps only resources whose types are on its "I want" list and discards the rest.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.3.2 "The algorithm," Figure 8.6.

# Verification Notes

- Definition source: Directly adapted from Section 8.3.2.
- Confidence rationale: HIGH — the book describes the algorithm step by step with a figure.
- Uncertainties: None.
- Cross-reference status: Verified.
