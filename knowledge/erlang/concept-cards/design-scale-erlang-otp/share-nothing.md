---
# === CORE IDENTIFICATION ===
concept: Share-Nothing Architecture
slug: share-nothing

# === CLASSIFICATION ===
category: distribution
subcategory: data-sharing
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Sharing Data — Share nothing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - share nothing
  - shared-nothing architecture

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sharing-data
extends:
  - sharing-data
related:
  - share-something
  - share-everything
  - load-balancing
contrasts_with:
  - share-something
  - share-everything

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a share-nothing architecture?"
  - "How do I decide how to replicate data across nodes?"
---

# Quick Definition

A share-nothing architecture replicates no data or state between nodes; each collection of nodes owns an independent copy of its data, giving linear scalability at the cost of losing state when a node fails.

# Core Definition

"The share-nothing architecture is where no data or state is shared. This could be specific to a node, a node family, or a cluster. Once you have addressed the underlying infrastructure, such as hardware, networks, and load balancing, share-nothing architectures can result in linearly scalable systems. Because each collection of nodes has an independent copy of its own data and state, it can operate on its own. When you need to scale, all you need to do is add more infrastructure and reconfigure your load balancers" (Cesarini & Vinoski, p. 411).

# Prerequisites

- **Sharing data** — Share-nothing is one of the three data-sharing strategies; understand the framing first.

# Key Properties

1. No data or state is shared between nodes, node families, or clusters.
2. Each collection of nodes owns an independent copy of its own data and state.
3. Can result in linearly scalable systems.
4. Scaling means adding infrastructure and reconfiguring load balancers.
5. Losing a node loses all the state and data associated with it.
6. Requests must be routed to the node that stores their matching state.

# Construction / Recognition

## To Construct/Create:
1. Keep each node's (or node family's) data and state entirely independent.
2. Address infrastructure: hardware, networks, load balancing.
3. Scale by adding infrastructure and reconfiguring load balancers.
4. Route each request to the node holding its session/state.

## To Identify/Recognize:
1. Recognize share-nothing when losing a node loses its state, with no replica elsewhere.

# Context & Application

- **Typical contexts**: Systems prioritizing linear scalability over state preservation.
- **Common applications**: Stateless or cheaply re-establishable workloads where re-login after node loss is acceptable.
- **Historical/stylistic notes**: The most scalable of the three sharing strategies but the least fault-tolerant for state.

# Examples

**Example 1** (pp. 411-412, Figure 14-5): Two front-end and two logic nodes; clients send login requests, sessions are created on primary logic nodes; when a logic node crashes, its sessions are lost and affected clients must log on again.

**Example 2** (p. 412): Because session state is not copied across nodes, you get better scalability — you can keep adding front-end and logic nodes as simultaneous users increase.

# Relationships

## Builds Upon
- **Sharing data** — Share-nothing is one of the three data-sharing strategies

## Enables
- Share-nothing enables linearly scalable systems.

## Related
- **Share something** — The middle-ground sharing strategy
- **Share everything** — The full-replication sharing strategy
- **Load balancing** — Share-nothing relies on consistent request routing

## Contrasts With
- **Share something** — Share-something replicates some data; share-nothing replicates none
- **Share everything** — Share-everything replicates all data; share-nothing replicates none

# Common Errors

- **Error**: Routing a returning client's request to any node
  **Correction**: Each request must be routed to the node that stores its matching session data, or the client must log on again.

# Common Confusions

- **Confusion**: Share-nothing means nodes do not communicate.
  **Clarification**: Nodes still communicate and forward requests; they simply do not replicate data and state to one another.

# Source Reference

Chapter 13: Systems That Never Stop, "Sharing Data — Share nothing," pages 411-412. See Figure 14-5.

# Verification Notes

- Definition source: Direct quote from p. 411.
- Confidence rationale: HIGH — the source dedicates a named subsection with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
