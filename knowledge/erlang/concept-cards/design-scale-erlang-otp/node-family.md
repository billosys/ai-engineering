---
# === CORE IDENTIFICATION ===
concept: Node Family
slug: node-family

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
  - node family

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
  - otp-release
extends: []
related:
  - cluster
  - erlang-node
contrasts_with:
  - cluster

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a node family?"
  - "How do I split a system into node types?"
---

# Quick Definition

A node family is a group of node types running the same OTP release, managed as a single entity. Node families are themselves grouped into clusters.

# Core Definition

"We group node types running the same OTP release into a node family. This is a way of managing nodes as a single entity. You can have different node families with the same release, but grouped together based on criteria such as data center, cloud region, or even release version. Node families are then grouped into clusters, which together give you your system" (Cesarini & Vinoski, p. 381).

# Prerequisites

- **Semantic node type** — A node family groups node types; understand node types first.
- **OTP release** — Family membership is defined by running the same OTP release.

# Key Properties

1. A node family groups node types running the same OTP release.
2. It is a unit for managing nodes as a single entity.
3. Different node families can share a release but be grouped by data center, cloud region, or release version.
4. Node families are grouped into clusters.
5. Clusters of node families together form the overall system.

# Construction / Recognition

## To Construct/Create:
1. Identify node types running the same OTP release.
2. Group them by an operational criterion (data center, cloud region, release version).
3. Manage that group as a single node family.

## To Identify/Recognize:
1. A node family is a set of nodes sharing a release that are managed together.

# Context & Application

- **Typical contexts**: Managing distributed deployments across data centers and cloud regions.
- **Common applications**: Grouping nodes for orchestration, scaling, and release-version management.
- **Historical/stylistic notes**: Part of the distributed Erlang terminology formalized by the RELEASE project (p. 379).

# Examples

**Example 1** (p. 381): Different node families running the same release but grouped by data center, cloud region, or release version.

**Example 2** (p. 381): Node families grouped into clusters; multiple clusters in a system spread services geographically across data centers managed by different cloud or infrastructure providers.

# Relationships

## Builds Upon
- **Semantic node type** — A node family groups node types
- **OTP release** — Family membership is defined by a shared release

## Enables
- **Cluster** — Node families are grouped into clusters

## Related
- **Cluster** — The grouping level above the node family
- **Erlang node** — The underlying unit

## Contrasts With
- **Cluster** — A node family shares one release; a cluster groups multiple families

# Common Errors

- **Error**: Treating every node individually for orchestration
  **Correction**: Group nodes into families so they can be managed as single entities.

# Common Confusions

- **Confusion**: A node family and a cluster are the same thing.
  **Clarification**: A node family is node types sharing a release; clusters are groups of node families.

# Source Reference

Chapter 12: Distributed Architectures, "Node Types and Families," page 381.

# Verification Notes

- Definition source: Direct quote from p. 381.
- Confidence rationale: HIGH — explicit definition in source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
