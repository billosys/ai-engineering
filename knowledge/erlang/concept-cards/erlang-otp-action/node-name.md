---
# === CORE IDENTIFICATION ===
concept: Node Name
slug: node-name

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2.1 Starting a node"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "long node name"
  - "short node name"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - erlang-cluster
  - epmd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a node name?"
  - "When do I use long vs. short node names?"
---

# Quick Definition

A node name is the `nodename@hostname` atom identifying an Erlang node; it comes in two forms — long (fully qualified host) set with `-name`, and short (subnet-local host) set with `-sname`.

# Core Definition

A node name is the atom of the form `nodename@hostname` that uniquely identifies an Erlang node, letting other nodes find and address it. There are two kinds. Long names use fully qualified domain names (e.g. `simple_cache@mybox.home.net`) and require a working DNS; a node is given a long name with `erl -name`. Short names omit the qualified host part (e.g. `simple_cache@mybox`) and are used where fully qualified names do not work — common in some production environments or on wireless LANs where two computers can connect but cannot resolve each other via DNS; a node is given a short name with `erl -sname`. Short names work as long as the nodes are on the same subnet. Long-name and short-name nodes operate in different communication modes and cannot belong to the same cluster (Ch. 8, Section 8.2.1).

# Prerequisites

- **erlang-node** — A node name identifies a node; the node concept comes first.

# Key Properties

1. An atom of the form `nodename@hostname`.
2. Long names: fully qualified host, set with `-name`, need working DNS.
3. Short names: unqualified host, set with `-sname`, work on the same subnet.
4. Shown in the Erlang shell prompt.
5. Long-name and short-name nodes cannot be in the same cluster.
6. Non-distributed VMs have the name `nonode@nohost`.

# Construction / Recognition

## To Choose a Name Form:
1. Use `-name` (long) when DNS resolves fully qualified hostnames.
2. Use `-sname` (short) when DNS does not work or nodes are simply on the same subnet.
3. Quote the name with single quotes when referencing it as an argument if it contains dots.

## To Recognize:
1. A name with a dotted host part is long; without dots it is short.

# Context & Application

- **Typical contexts**: Starting nodes for clusters, testing, and production.
- **Common applications**: Naming contact nodes; addressing remote registered processes.
- **Historical/stylistic notes**: The book recommends switching to `-sname` if `-name` connection fails because of unresolvable DNS.

# Examples

**Example 1** (Section 8.2.1): `erl -name simple_cache` yields the long name `simple_cache@mybox.home.net`.

**Example 2** (Section 8.2.1): `erl -sname simple_cache` yields the short name `simple_cache@mybox`.

# Relationships

## Builds Upon
- **erlang-node** — The node name identifies a node.

## Enables
- **erlang-cluster** — Nodes find each other by name to form clusters.

## Related
- **EPMD** — EPMD maps node names to communication ports.

## Contrasts With
- None.

# Common Errors

- **Error**: Using a fully qualified `-name` when DNS cannot resolve the host.
  **Correction**: Switch to `-sname` for short names that work on the local subnet.

# Common Confusions

- **Confusion**: Believing long and short names are interchangeable.
  **Clarification**: They use different communication modes; all nodes in a cluster must use the same form.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.1 "Starting a node," including the "Long and short names can't be mixed" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 8.2.1.
- Confidence rationale: HIGH — the book explicitly describes both name forms.
- Uncertainties: None.
- Cross-reference status: Verified.
