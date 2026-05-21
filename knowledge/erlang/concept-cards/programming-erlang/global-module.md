---
# === CORE IDENTIFICATION ===
concept: global Module
slug: global-module

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-libraries
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "Libraries and BIFS for Distributed Programming"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "global registration"
  - "global name registration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
  - distributed-erlang
extends: []
related:
  - rpc-module
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which module registers names across distributed nodes?"
  - "How do I maintain a fully connected network of nodes?"
  - "How does the global module relate to distributed Erlang?"
---

# Quick Definition

`global` is a standard Erlang library module with functions for registering names and locks in a distributed system and for maintaining a fully connected network of nodes.

# Core Definition

When writing distributed programs, two standard modules cover most needs: `rpc`, which provides remote procedure call services, and `global`, which "has functions for the registration of names and locks in a distributed system and for the maintenance of a fully connected network" (Chapter 14, "Libraries and BIFS for Distributed Programming"). Where the BIF `register/2` registers a process name *locally* on one node, `global` provides registration of names that are visible cluster-wide, plus distributed locks, and it works to keep the set of nodes fully connected. The chapter introduces `global` at this overview level rather than developing its full API in detail.

# Prerequisites

- **Node** — `global` registers names and maintains connectivity across nodes.
- **Distributed Erlang** — `global` operates within a distributed Erlang cluster.

# Key Properties

1. `global` is a standard library module for distributed programming.
2. It provides registration of names across a distributed system (cluster-wide, not node-local).
3. It provides distributed locks.
4. It helps maintain a fully connected network of nodes.
5. It is one of the two main modules (with `rpc`) that hide distribution complexity.

# Construction / Recognition

## To Use global:
1. Register cluster-wide names through the `global` module rather than the node-local `register/2` BIF.
2. Use `global`'s lock functions to coordinate across nodes.
3. Rely on `global` to keep the node network fully connected.

## To Recognize It:
1. Look for calls into the `global` module for name registration or locks.
2. Distinguish cluster-wide `global` registration from node-local `register/2`.

# Context & Application

- **Typical contexts**: Distributed systems needing globally visible process names or distributed locking.
- **Common applications**: Cluster-wide service registries; coordinating exclusive access across nodes.
- **Historical/stylistic notes**: The chapter mentions `global` only at an overview level, pointing readers to the manual page for detail.

# Examples

**Example 1** (Chapter 14, "Libraries and BIFS for Distributed Programming"): The book lists `global` as one of the two modules covering most distributed-programming needs, with "functions for the registration of names and locks in a distributed system and for the maintenance of a fully connected network."

**Example 2** (Chapter 14): The source does not provide a worked code example for `global`; it is introduced as a companion to `rpc` and deferred to the manual pages.

# Relationships

## Builds Upon
- **Distribution BIFs** — `global` is built on top of the lower-level distribution primitives.

## Enables
- Cluster-wide name registration and distributed locking.

## Related
- **rpc module** — the companion standard module for distributed programming.

## Contrasts With
- A standard-library facility; no commonly confused counterpart developed in this chapter.

# Common Errors

- **Error**: Using the node-local `register/2` BIF and expecting names to be visible cluster-wide.
  **Correction**: Use the `global` module for names that must be reachable from any node.

# Common Confusions

- **Confusion**: `global` registration and local `register/2` are equivalent.
  **Clarification**: `register/2` is node-local; `global` registration is cluster-wide and also coordinates connectivity.
- **Confusion**: `global` is a substitute for `rpc`.
  **Clarification**: They are complementary — `rpc` does remote calls; `global` does distributed naming and locking.

# Source Reference

Chapter 14: Distributed Programming, section "Libraries and BIFS for Distributed Programming" (the overview of the `global` module).

# Verification Notes

- Definition source: Synthesized from the brief overview of `global` in "Libraries and BIFS for Distributed Programming"; the chapter does not develop the API.
- Confidence rationale: MEDIUM — `global` is named and its purpose stated, but no detailed API or worked example is given in the source.
- Uncertainties: Exact function signatures are out of scope of this chapter; the card stays at the source's overview level.
- Cross-reference status: Slugs match canonical `node`/`distributed-erlang` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
