---
# === CORE IDENTIFICATION ===
concept: Cluster
slug: cluster

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
  - Erlang cluster

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node-family
  - erlang-node
extends: []
related:
  - system-blueprint
  - distributed-erlang
  - microservices-architecture
contrasts_with:
  - node-family

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang cluster?"
  - "How do I split a system into node types?"
---

# Quick Definition

A cluster is a group of node families that, taken together, gives you your system. Multiple clusters are used to increase availability, reliability, and scalability across geographically distributed data centers.

# Core Definition

Node families "are then grouped into clusters, which together give you your system. Multiple clusters in systems are used to increase availability, reliability, and scalability, spreading services geographically across different data centers, possibly managed by different cloud or infrastructure providers" (Cesarini & Vinoski, p. 381). Nodes of one type interact in a cluster with other node types to provide the system's end-to-end functionality (p. 378).

# Prerequisites

- **Node family** — Clusters are groups of node families; understand families first.
- **Erlang node** — The underlying unit of a cluster.

# Key Properties

1. A cluster is a group of node families.
2. Node types within a cluster interact to provide end-to-end functionality.
3. Multiple clusters are used to increase availability, reliability, and scalability.
4. Clusters can be spread geographically across data centers and infrastructure providers.
5. Clusters are needed for microservices architectures, scalability via sharding, and geographic distribution.

# Construction / Recognition

## To Construct/Create:
1. Group node families into a cluster that delivers end-to-end functionality.
2. Add multiple instances of node types to create distributed cluster patterns (system blueprints).
3. Deploy multiple clusters across data centers for availability and scale.

## To Identify/Recognize:
1. A cluster is the grouping of node families whose combined function is the system.

# Context & Application

- **Typical contexts**: Microservices architectures, sharding for scalability, geographic distribution.
- **Common applications**: Implementing a microservices architecture where each cluster provides a set of services; sharding across identical clusters to increase computing power and availability.
- **Historical/stylistic notes**: There is no single solution for clustering; tools must cater to different cluster patterns and target environments (cloud, bare metal, Raspberry Pi) (p. 378).

# Examples

**Example 1** (p. 378): Clusters used for a microservices architecture where each cluster of nodes provides a set of services, or used for scalability by sharding across identical clusters.

**Example 2** (p. 389, Figure 13-5): Logic nodes running Riak Core form a fully meshed ring used to route requests to service nodes or act as gateways to other clusters.

# Relationships

## Builds Upon
- **Node family** — A cluster is a grouping of node families

## Enables
- **System blueprint** — Distributed cluster patterns are system blueprints

## Related
- **Distributed erlang** — A common technology for connecting nodes in a cluster
- **Microservices architecture** — Clusters can each provide a set of services
- **System blueprint** — The formalization of cluster patterns

## Contrasts With
- **Node family** — A node family shares one release; a cluster groups multiple families

# Common Errors

- **Error**: Assuming one clustering tool fits all environments
  **Correction**: Tools ideal for Amazon or Rackspace may not work on Parallela or Raspberry Pi clusters; choose tools per target environment.

# Common Confusions

- **Confusion**: A cluster must run as fully connected distributed Erlang.
  **Clarification**: A cluster is a logical grouping; it may use distributed Erlang, Riak Core, SD Erlang, sockets, or a mix.

# Source Reference

Chapter 12: Distributed Architectures, introductory section and "Node Types and Families," pages 378-382.

# Verification Notes

- Definition source: Direct quote from p. 381; synthesized with p. 378.
- Confidence rationale: HIGH — the source explicitly defines clusters and their role.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
