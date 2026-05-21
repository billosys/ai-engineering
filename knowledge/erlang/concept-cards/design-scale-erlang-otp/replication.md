---
# === CORE IDENTIFICATION ===
concept: Primary-Primary and Primary-Secondary Replication
slug: replication

# === CLASSIFICATION ===
category: distribution
subcategory: replication
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Consistency — Share everything"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - primary-primary replication
  - primary-secondary replication
  - master-master replication
  - master-slave replication

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sharing-data
extends: []
related:
  - share-everything
  - redundancy
  - consistency-models
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is primary-primary replication?"
  - "What distinguishes primary-primary from primary-secondary replication?"
---

# Quick Definition

Replication is the copying of data across nodes. Primary-primary replication lets any node serve and modify data; primary-secondary replication designates a single primary responsible for the data.

# Core Definition

In a share-everything architecture, "we call this primary-primary replication. This contrasts with primary-secondary replication, where a single primary node is responsible for the data. The secondary nodes can access the data, but must coordinate any destructive operations such as inserts or deletes with the primary if they wish to modify the data. If the primary is lost, either the system stops working entirely, or it provides a degraded service level where writes and updates are not allowed, or one of the secondaries takes over as primary" (Cesarini & Vinoski, p. 417).

# Prerequisites

- **Sharing data** — Replication is the mechanism by which data is shared across nodes; understand data sharing first.

# Key Properties

1. Replication copies data and state across nodes.
2. Primary-primary: every node can serve and modify the data; on failure another takes over.
3. Primary-secondary: a single primary owns the data; secondaries read it but coordinate destructive operations with the primary.
4. If a primary-secondary primary is lost, the system stops, degrades to read-only, or a secondary is promoted.
5. Restarting nodes must copy data from a primary to regain a current view of state.

# Construction / Recognition

## To Construct/Create:
1. For primary-primary: replicate all data to all nodes; allow any node to take over requests.
2. For primary-secondary: designate one primary; route destructive operations through it.
3. On primary loss in primary-secondary, decide whether to stop, degrade, or promote a secondary.

## To Identify/Recognize:
1. Recognize primary-primary when any node can modify data; primary-secondary when only one node owns writes.

# Context & Application

- **Typical contexts**: Share-everything and other replicated architectures.
- **Common applications**: Failover designs for highly reliable systems.
- **Historical/stylistic notes**: Share-everything uses primary-primary replication; on node recovery, the node must connect to a primary and retrieve a copy of the data to resync.

# Examples

**Example 1** (pp. 416-417, Figure 14-8): In the share-everything example, two logic nodes each duplicate session state and shopping carts to the other — primary-primary replication, where if a node terminates the other takes over.

**Example 2** (p. 417): In primary-secondary replication, if the primary is lost the system either stops entirely, degrades to disallow writes/updates, or promotes a secondary to primary.

# Relationships

## Builds Upon
- **Sharing data** — Replication is the mechanism of data sharing

## Enables
- **Share everything** — Share-everything is built on primary-primary replication
- **Redundancy** — Data redundancy is achieved through replication

## Related
- **Share everything** — Uses primary-primary replication
- **Redundancy** — Replication provides data redundancy
- **Consistency models** — Replication strategy interacts with the chosen consistency model

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a recovered node can serve requests immediately
  **Correction**: A restarting node must copy data from a primary and become consistent before accepting requests.

# Common Confusions

- **Confusion**: Primary-secondary secondaries cannot access the data.
  **Clarification**: Secondaries can read the data; they must coordinate destructive operations (inserts, deletes) with the primary.

# Source Reference

Chapter 13: Systems That Never Stop, "Consistency — Share everything," page 417. See Figure 14-8.

# Verification Notes

- Definition source: Direct quote from p. 417.
- Confidence rationale: HIGH — the source explicitly names and contrasts both replication models.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
