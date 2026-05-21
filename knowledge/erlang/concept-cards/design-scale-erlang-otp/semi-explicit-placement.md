---
# === CORE IDENTIFICATION ===
concept: Semi-Explicit Placement
slug: semi-explicit-placement

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
  - semiexplicit placement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sd-erlang
extends: []
related:
  - s-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is semi-explicit placement in SD Erlang?"
  - "How does SD Erlang decide where to place nodes?"
---

# Quick Definition

Semi-explicit placement is an SD Erlang concept that controls where new nodes are placed, based on communication distances to other nodes and on node attributes.

# Core Definition

"To enable SD Erlang applications to be portable and scalable, a concept of semiexplicit placement is also introduced. This controls the placement of new nodes based on communication distances to other nodes and on node attributes. Node attributes are hardware-, software-, and programmer-defined characteristics of nodes that enable them to be aware of their unique characteristics and their neighboring nodes. Communication distances use the time it takes to transfer data from one node to another as a metric. Assuming connections with equal bandwidth, shorter transfer times correspond to smaller communication distances between nodes" (Cesarini & Vinoski, p. 391).

# Prerequisites

- **SD Erlang** — Semi-explicit placement is an SD Erlang concept; understand SD Erlang first.

# Key Properties

1. Controls the placement of new nodes.
2. Placement is based on communication distances and node attributes.
3. Node attributes are hardware-, software-, and programmer-defined characteristics.
4. Communication distance uses data-transfer time as its metric.
5. With equal bandwidth, shorter transfer times mean smaller communication distances.
6. It makes SD Erlang applications portable and scalable.

# Construction / Recognition

## To Construct/Create:
1. Define node attributes describing each node's hardware, software, and programmer-set characteristics.
2. Measure communication distances between nodes via data-transfer times.
3. Place new nodes guided by those distances and attributes rather than fully manually or fully automatically.

## To Identify/Recognize:
1. Recognize semi-explicit placement when node placement is guided by measured distances and attributes rather than purely explicit or purely implicit assignment.

# Context & Application

- **Typical contexts**: Large, portable SD Erlang deployments.
- **Common applications**: Positioning new nodes to reduce communication distance and improve scalability.
- **Historical/stylistic notes**: Introduced alongside the s_group concept in the RELEASE project's SD Erlang.

# Examples

**Example 1** (p. 391): Node attributes are hardware-, software-, and programmer-defined characteristics that enable nodes to be aware of their unique characteristics and their neighboring nodes.

**Example 2** (p. 391): Communication distance uses data-transfer time as a metric — assuming equal bandwidth, shorter transfer times correspond to smaller communication distances.

# Relationships

## Builds Upon
- **SD Erlang** — Semi-explicit placement is part of SD Erlang

## Enables
- Semi-explicit placement enables portable, scalable SD Erlang applications.

## Related
- **S group** — Both are SD Erlang constructs that together support scalability

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Placing nodes without regard to communication distance
  **Correction**: Use communication distance and node attributes to position nodes for scalability and portability.

# Common Confusions

- **Confusion**: Semi-explicit placement means the programmer fully specifies node locations.
  **Clarification**: It is "semi"-explicit — placement is guided by measured distances and attributes, not fully specified by hand.

# Source Reference

Chapter 12: Distributed Architectures, "Distributed Erlang — Scalable Distributed Erlang," page 391.

# Verification Notes

- Definition source: Direct quote from p. 391.
- Confidence rationale: HIGH — the source explicitly defines semi-explicit placement, node attributes, and communication distance.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
