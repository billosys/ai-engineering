---
# === CORE IDENTIFICATION ===
concept: Scalable Distributed Erlang
slug: sd-erlang

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
  - SD Erlang
  - Scalable Distributed Erlang

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - fully-connected-network
extends:
  - distributed-erlang
related:
  - s-group
  - semi-explicit-placement
contrasts_with:
  - riak-core
  - fully-connected-network

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Scalable Distributed Erlang?"
  - "How does distributed Erlang relate to scaling a system out?"
---

# Quick Definition

Scalable Distributed Erlang (SD Erlang) is a small extension to distributed Erlang that reduces network connectivity and namespace size, allowing systems to scale to tens of thousands of nodes.

# Core Definition

"Scalable Distributed Erlang (SD Erlang) takes a different approach from that of Riak Core. SD Erlang emerged from the RELEASE research project at the University of Glasgow. Although at the time of writing it was not production-ready, the ideas behind it are interesting and have been shown to allow systems to scale to tens of thousands of nodes. The basic approach is to reduce network connectivity and the namespace through a small extension to the existing distributed Erlang" (Cesarini & Vinoski, p. 390). It introduces a new layer called an s_group and a concept of semi-explicit placement.

# Prerequisites

- **Distributed Erlang** — SD Erlang is a small extension to distributed Erlang.
- **Fully connected network** — SD Erlang exists to reduce the full connectivity of distributed Erlang.

# Key Properties

1. A small extension to existing distributed Erlang.
2. Reduces network connectivity and namespace size.
3. Has been shown to scale systems to tens of thousands of nodes.
4. Introduces the s_group layer for partial connectivity and partitioned namespaces.
5. Introduces semi-explicit placement controlling node placement by communication distance and attributes.
6. Was not production-ready at the time of writing.

# Construction / Recognition

## To Construct/Create:
1. Organize nodes into s_groups; a node can belong to zero, one, or more s_groups.
2. Register names within an s_group using `s_group:register_name/3`.
3. Use shared nodes as gateways between s_groups.
4. Use semi-explicit placement to position new nodes by communication distance and attributes.

## To Identify/Recognize:
1. Recognize SD Erlang by its s_group layer that limits connectivity and namespace replication, instead of the default full mesh.

# Context & Application

- **Typical contexts**: Systems aiming to scale distributed Erlang far beyond the full-mesh limit.
- **Common applications**: Arranging nodes in different configurations, clustering nodes and connecting them via gateways.
- **Historical/stylistic notes**: Emerged from the RELEASE research project at the University of Glasgow; documentation available on the University of Glasgow's site (p. 391).

# Examples

**Example 1** (p. 391, Figure 13-7): Two s_groups G1 and G2, each containing three Erlang nodes; node C is shared by both s_groups and acts as a gateway transmitting messages between them.

**Example 2** (p. 391): Semi-explicit placement controls the placement of new nodes based on communication distances to other nodes and on node attributes (hardware-, software-, and programmer-defined characteristics).

# Relationships

## Builds Upon
- **Distributed Erlang** — SD Erlang is a small extension to it
- **Fully connected network** — SD Erlang reduces the default full connectivity

## Enables
- **S group** — SD Erlang's new connectivity/namespace layer
- **Semi-explicit placement** — SD Erlang's node-placement concept

## Related
- **S group** — The core SD Erlang construct
- **Semi-explicit placement** — SD Erlang's placement mechanism

## Contrasts With
- **Riak Core** — A different framework for scaling distributed Erlang
- **Fully connected network** — SD Erlang deliberately avoids the full mesh

# Common Errors

- **Error**: Adopting SD Erlang in production based on this book's description
  **Correction**: At the time of writing it was not production-ready; evaluate its current status before relying on it.

# Common Confusions

- **Confusion**: SD Erlang replaces distributed Erlang entirely.
  **Clarification**: It is a small extension to existing distributed Erlang, adding the s_group layer rather than replacing the protocol.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Scalable Distributed Erlang," pages 390-391. See Figure 13-7.

# Verification Notes

- Definition source: Direct quote from p. 390.
- Confidence rationale: HIGH — the source dedicates a named subsection to SD Erlang with an explicit definition.
- Uncertainties: Production-readiness status stated as "at the time of writing."
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
