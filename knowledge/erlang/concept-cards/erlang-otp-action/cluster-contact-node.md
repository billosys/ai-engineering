---
# === CORE IDENTIFICATION ===
concept: Cluster Contact Node
slug: cluster-contact-node

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.3.2 Making the cache aware of other nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "contact node"
  - "blank node"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-cluster
  - connecting-nodes
extends: []
related:
  - magic-cookie
  - distributed-cache
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cluster contact node?"
  - "How does a new node join a predefined cluster automatically?"
  - "Why use blank contact nodes?"
---

# Quick Definition

A cluster contact node is a known, always-available blank Erlang node that other nodes ping at startup to join a predefined cluster; running no user code, it has little reason to ever go down.

# Core Definition

A cluster contact node is part of a simple method for automatically adding a new node to a predefined cluster. The technique is to always have two known *blank* Erlang nodes running — nodes without any user-defined code, so there is little reason for them to ever go down. They are started normally with suitable names and the cluster's cookie set for authentication. Each application node is configured to ping both contact nodes by their known names; if either `net_adm:ping/1` succeeds, the node's startup is allowed to proceed, and if neither does, the node cannot join the cluster and startup fails with a crash dump. Preferably the two contact nodes run on separate physical computers (Ch. 9, Section 9.3.2).

# Prerequisites

- **erlang-cluster** — Contact nodes are how a node joins a cluster.
- **connecting-nodes** — Joining is done by pinging the contact nodes.

# Key Properties

1. A known, always-available blank node running no user code.
2. Typically two are run, preferably on separate machines.
3. New nodes ping them by known names to join the cluster.
4. Started with the cluster's magic cookie set.
5. If no contact node answers, the joining node's startup fails.
6. A simple trick that "tends to work pretty well."

# Construction / Recognition

## To Use Contact Nodes:
1. Start two blank nodes (e.g., `erl -name contact1 -setcookie xxxx`).
2. Configure each application node with the contact nodes' names.
3. At application startup, ping the contact nodes; proceed only if one answers.

## To Recognize:
1. Startup code that pings a fixed list of node names before initializing is using contact nodes.

# Context & Application

- **Typical contexts**: Bootstrapping nodes into a predefined cluster.
- **Common applications**: The distributed cache joining its cluster in `sc_app:start/2`.
- **Historical/stylistic notes**: The book frames this as one simple approach among more advanced node-discovery options.

# Examples

**Example 1** (Section 9.3.2): Two contact nodes are started with `erl -name contact1 -setcookie xxxxxxxx` and `erl -name contact2 -setcookie xxxxxxxx`.

**Example 2** (Section 9.3.2): Each cache node is configured to ping both contact nodes; the `ensure_contact()` function in `sc_app` performs the pings and proceeds only if at least one answers.

# Relationships

## Builds Upon
- **erlang-cluster** — Contact nodes serve as a fixed entry point to a cluster.
- **connecting-nodes** — Joining is done by pinging contact nodes.

## Enables
- None.

## Related
- **magic-cookie** — Contact nodes are started with the cluster's cookie.
- **distributed-cache** — The cache uses contact nodes to join its cluster.
- **OTP application** — The ping happens in the application's `start/2`.

## Contrasts With
- None.

# Common Errors

- **Error**: Running contact nodes on the same machine as all the work nodes.
  **Correction**: Preferably run them on separate physical computers so a single machine failure does not take down the cluster's entry point.

# Common Confusions

- **Confusion**: Thinking contact nodes run application logic.
  **Clarification**: They are deliberately blank — running no user code — precisely so they stay up.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.3.2 "Making the cache aware of other nodes," Figure 9.10 and Listing 9.4.

# Verification Notes

- Definition source: Directly adapted from Section 9.3.2.
- Confidence rationale: HIGH — the book explicitly describes the contact-node technique.
- Uncertainties: None.
- Cross-reference status: Verified.
