---
# === CORE IDENTIFICATION ===
concept: Partitioning
slug: partitioning

# === CLASSIFICATION ===
category: distribution
subcategory: data-distribution
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Horizontal and Vertical Scaling — Amdahl's Law"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - sharding
  - data partitioning

# === TYPED RELATIONSHIPS ===
prerequisites:
  - horizontal-scaling
extends: []
related:
  - consistent-hashing
  - riak-core
  - cluster
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is partitioning?"
  - "How is a data set split across distributed nodes?"
---

# Quick Definition

Partitioning (sharding) is splitting a data set and its operations into distributed nodes so they can run in parallel, scaling a system past the limits of a single machine's cores.

# Core Definition

The book introduces partitioning as the response to the diminishing returns predicted by Amdahl's Law: "When we reach a certain limit, adding more cores improves performance only marginally. This is where it makes sense to scale your system by partitioning your data set and operations into distributed nodes, running them in parallel" (Cesarini & Vinoski, p. 425). At the cluster level, the book also frames it as "sharding across identical clusters to increase computing power and availability" (p. 378), and Riak Core uses consistent hashing "to shard your data and load balancing jobs across the cluster" (p. 429).

# Prerequisites

- **Horizontal scaling** — Partitioning is how you scale out a data set across nodes; understand horizontal scaling first.

# Key Properties

1. Splits a data set and its operations across distributed nodes.
2. Lets partitioned work run in parallel.
3. The response to the marginal returns of adding cores (Amdahl's Law).
4. Can be applied at the cluster level (sharding across identical clusters).
5. Riak Core shards data via consistent hashing and load-balances jobs across the cluster.

# Construction / Recognition

## To Construct/Create:
1. Identify a data set whose processing exceeds a single machine's effective core count.
2. Split the data set and its operations across distributed nodes.
3. Run the partitions in parallel; use consistent hashing to assign data to nodes.
4. Optionally shard across identical clusters for more computing power and availability.

## To Identify/Recognize:
1. Recognize partitioning when a data set is divided so different nodes own and process different subsets.

# Context & Application

- **Typical contexts**: Scaling out beyond the point where adding cores no longer helps.
- **Common applications**: Sharding key-value data across a Riak Core cluster; sharding across identical clusters.
- **Historical/stylistic notes**: Partitioning is closely tied to consistent hashing, which spreads data evenly while minimizing relocation when nodes are added or removed.

# Examples

**Example 1** (p. 425): When adding more cores improves performance only marginally, it makes sense to scale by partitioning the data set and operations into distributed nodes running in parallel.

**Example 2** (p. 429): Riak Core, despite being a fully meshed Erlang cluster, scales well by using consistent hashing to shard data and load-balance jobs across the cluster.

# Relationships

## Builds Upon
- **Horizontal scaling** — Partitioning is a horizontal-scaling technique for data

## Enables
- Partitioning enables parallel processing of a data set beyond a single machine's limits.

## Related
- **Consistent hashing** — A common mechanism for assigning partitions to nodes
- **Riak Core** — Uses consistent hashing to shard data across a cluster
- **Cluster** — Sharding can be applied across identical clusters

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Partitioning prematurely before core-level scaling is exhausted
  **Correction**: Partition when adding cores yields only marginal improvement; do not over-engineer.

# Common Confusions

- **Confusion**: Partitioning and replication are the same.
  **Clarification**: Partitioning splits a data set across nodes so each owns a subset; replication copies the same data to multiple nodes for redundancy.

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling — Amdahl's Law," page 425, and "Capacity Planning," page 429. See also Chapter 12, page 378 (sharding across clusters).

# Verification Notes

- Definition source: Synthesized from pp. 425, 429, and 378; the chapter does not give a single standalone formal definition of partitioning.
- Confidence rationale: MEDIUM — partitioning/sharding is discussed across several passages but not as a formally defined named concept; the definition is synthesized.
- Uncertainties: The book treats partitioning mostly through consistent hashing and Riak Core rather than as a standalone topic.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
