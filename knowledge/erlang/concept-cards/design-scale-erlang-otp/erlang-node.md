---
# === CORE IDENTIFICATION ===
concept: Erlang Node
slug: erlang-node

# === CLASSIFICATION ===
category: distribution
subcategory: node-model
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Distributed Architectures (intro)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - node
  - Erlang runtime instance

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - otp-release
  - semantic-node-type
  - cluster
contrasts_with:
  - cluster

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang node?"
  - "What concepts are needed before building distributed architectures?"
---

# Quick Definition

An Erlang node is the smallest executable standalone unit of an Erlang system: a single running instance of the Erlang runtime system. Distributed systems are built by connecting many such nodes.

# Core Definition

"A node is the smallest executable standalone unit consisting of a running instance of the Erlang runtime system" (Cesarini & Vinoski, p. 378). Each node consists of a number of loosely coupled OTP applications, defined in its OTP release file. The release determines the services the node provides and the tasks it is capable of handling. Nodes that share a release file contain the same set of OTP applications and are considered to be nodes of the same type. An Erlang system can comprise just one standalone node, but more typically consists of multiple nodes grouped into one or more clusters (p. 378).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is the starting point from which all distributed-architecture concepts in chapters 12-15 are built.

# Key Properties

1. A node is one running instance of the Erlang runtime system (the BEAM VM).
2. A node runs a set of loosely coupled OTP applications defined in its OTP release file.
3. Nodes sharing a release file are of the same type.
4. A node is the unit of failure isolation in a distributed Erlang system — losing a node should not affect requests not routed through it.
5. A single node can be standalone, or one of many nodes grouped into clusters.

# Construction / Recognition

## To Construct/Create:
1. Define an OTP release file listing the applications the node will run.
2. Start an instance of the Erlang runtime system loading that release.
3. Optionally give it a name and connect it to other nodes to form a distributed system.

## To Identify/Recognize:
1. A node is a single OS process running the BEAM VM.
2. Its identity in a distributed system is its node name (and cookie for connection).

# Context & Application

- **Typical contexts**: Every Erlang system, from a single-node prototype to a multi-cluster production deployment, is composed of nodes.
- **Common applications**: Splitting system functionality across nodes for maintainability, scalability, and availability; running multiple node instances of the same type for redundancy.
- **Historical/stylistic notes**: OTP historically defined the components of a single node well but stopped short of describing how nodes group into clusters; the RELEASE EU project formalized the multi-node terminology (p. 379).

# Examples

**Example 1** (p. 379): A system of three Erlang nodes — one running web servers, one handling business logic, one acting as a database — appears to the end user as a single black-box system.

**Example 2** (p. 380): A single node running an Erlang web server (Yaws, Webmachine, Cowboy), business logic, and an Erlang database (Mnesia, CouchDB, Riak) all in one VM reduces internode I/O but creates a single point of failure.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- **Otp release** — A release file defines what applications a node runs
- **Semantic node type** — Nodes are classified by their functional purpose
- **Cluster** — Nodes are grouped into clusters to form a system

## Related
- **Otp release** — Determines the services a node provides
- **Cluster** — The grouping unit above the node

## Contrasts With
- **Cluster** — A node is a single runtime instance; a cluster is a group of nodes

# Common Errors

- **Error**: Combining all applications (front-end, logic, database) into a single node for "speed"
  **Correction**: This is acceptable only for simple systems; for anything else, split functionality across nodes to isolate failure and enable scaling.

- **Error**: Treating a node failure as catastrophic system-wide
  **Correction**: Design so that losing a node has no impact on requests not routed through it.

# Common Confusions

- **Confusion**: A node is a physical computer.
  **Clarification**: A node is a running instance of the runtime system; multiple nodes can run on one computer, and multiple distributed VMs on one machine may be needed to fully use many-core hardware.

# Source Reference

Chapter 12: Distributed Architectures, introductory section, page 378. See also "Node Types and Families," pages 379-381.

# Verification Notes

- Definition source: Direct quote from p. 378.
- Confidence rationale: HIGH — the source explicitly and clearly defines a node in its opening paragraph.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards (otp-release, semantic-node-type, cluster).
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
