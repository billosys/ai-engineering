---
# === CORE IDENTIFICATION ===
concept: OTP Release
slug: otp-release

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment-units
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Distributed Architectures (intro)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - release
  - release file
  - OTP release file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - semantic-node-type
  - node-family
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release?"
  - "How does a release relate to the applications it bundles?"
---

# Quick Definition

An OTP release is a release file that lists the set of loosely coupled OTP applications a node runs, thereby determining the services that node provides. Nodes that share a release file are considered nodes of the same type.

# Core Definition

"Each node consists of a number of loosely coupled OTP applications, defined in its OTP release file. An OTP release determines the services the node provides and tasks it is capable of handling. Nodes that share a release file contain the same set of OTP applications and are considered to be nodes of the same type" (Cesarini & Vinoski, p. 378). The release is the unit that ties a node's identity (its type) to a concrete bundle of applications.

# Prerequisites

- **Erlang node** — A release defines what a node runs; you must understand the node before the release that configures it.

# Key Properties

1. A release file enumerates the set of OTP applications a node runs.
2. The release determines the services a node provides and the tasks it can handle.
3. Two nodes sharing a release file run the same set of applications and are the same type.
4. Releases group nodes into node families: node types running the same release form a node family.

# Construction / Recognition

## To Construct/Create:
1. Identify the OTP applications a node type must run.
2. List them in the release file along with their versions.
3. Deploy the release to one or more nodes; each becomes a node of that type.

## To Identify/Recognize:
1. Two nodes are the same type if and only if they share a release file.
2. Multiple node instances of the same release form a node family.

# Context & Application

- **Typical contexts**: Defining node types, grouping nodes into node families, deploying distributed systems.
- **Common applications**: Rolling out multiple instances of a node type for availability and scalability; grouping nodes by release version.
- **Historical/stylistic notes**: Multiple node instances of the same type could be running different versions of the same release (p. 380).

# Examples

**Example 1** (p. 380): Multiple node instances of the same semantic type could be running different versions of the same release; running multiple instances supports availability and scalability.

**Example 2** (p. 381): Node families are groups of node types running the same OTP release, optionally grouped further by criteria such as data center, cloud region, or release version.

# Relationships

## Builds Upon
- **Erlang node** — A release configures what applications a node runs

## Enables
- **Semantic node type** — A shared release file defines node type identity
- **Node family** — Node types running the same release form a node family

## Related
- **Semantic node type** — Type identity derives from the shared release
- **Node family** — The grouping built directly from a shared release

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming all nodes of a type run identical release versions
  **Correction**: Instances of the same node type may run different versions of the same release.

# Common Confusions

- **Confusion**: A release is the same thing as a node type.
  **Clarification**: The release is the file/bundle of applications; the node type is the semantic classification that the shared release establishes.

# Source Reference

Chapter 12: Distributed Architectures, introductory section and "Node Types and Families," pages 378-381.

# Verification Notes

- Definition source: Direct quote from p. 378; synthesized with node-family discussion on p. 381.
- Confidence rationale: MEDIUM — the source describes the release's role clearly in distributed terms but does not give a standalone formal definition of the release file format here (covered elsewhere in the book's earlier chapters).
- Uncertainties: The mechanics of release packaging are covered in earlier chapters, not chapters 12-15.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
