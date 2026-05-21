---
# === CORE IDENTIFICATION ===
concept: Erlang Node
slug: erlang-node

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2 Nodes and clustering"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "node"
  - "Erlang VM node"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
extends: []
related:
  - erlang-cluster
  - node-name
  - epmd
  - magic-cookie
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang node?"
  - "How do I start an Erlang node?"
  - "What is the difference between long and short node names?"
---

# Quick Definition

An Erlang node is a running Erlang VM that has been configured to work in distributed mode; it always has a name of the form `nodename@hostname` that lets other nodes find and talk to it.

# Core Definition

An Erlang node is a running Erlang VM that has been configured to work in distributed mode (networking enabled). A node always has a name — an atom of the form `nodename@hostname` — which allows other nodes to find it and communicate with it. The built-in function `node()` returns the current local node name; it is `nonode@nohost` for a VM not running in distributed mode. Multiple nodes can run on a single host machine. A node is started in distributed mode by running `erl` with either the `-name` flag (long, fully qualified names, requiring working DNS) or the `-sname` flag (short names, for environments where fully qualified names do not work; valid as long as nodes are on the same subnet). Long-name and short-name nodes use different communication modes and cannot be part of the same cluster (Ch. 8, Section 8.2).

# Prerequisites

- **distributed-erlang** — A node is the unit of Erlang distribution; the distribution concept frames it.

# Key Properties

1. A running Erlang VM configured for distributed mode.
2. Always has a name of the form `nodename@hostname`.
3. `node()` returns the local node name (`nonode@nohost` if not distributed).
4. Multiple nodes can run on one host.
5. Started with `erl -name` (long names) or `erl -sname` (short names).
6. Long-name and short-name nodes cannot mix in one cluster.

# Construction / Recognition

## To Start a Node:
1. Run `erl -name simple_cache` for a long (fully qualified) name with working DNS.
2. Or run `erl -sname simple_cache` for a short name on the same subnet.
3. The shell prompt shows the node name, e.g. `(simple_cache@mybox.home.net)1>`.

## To Recognize:
1. A VM whose shell prompt includes a `name@host` is a node; `nonode@nohost` means non-distributed.

# Context & Application

- **Typical contexts**: Typically one node per machine, but several may run on one host for testing.
- **Common applications**: Distributed services, clusters, contact nodes, remote shells.
- **Historical/stylistic notes**: `werl` is the Windows shell variant; the same `-name`/`-sname` flags apply.

# Examples

**Example 1** (Section 8.2.1): `erl -name simple_cache` started with a working DNS yields a prompt `(simple_cache@mybox.home.net)1>`.

**Example 2** (Section 8.2.1): `erl -sname simple_cache` yields `(simple_cache@mybox)1>` — no periods in the host part because it uses short names.

# Relationships

## Builds Upon
- **distributed-erlang** — A node is the realization of Erlang distribution.

## Enables
- **erlang-cluster** — Two or more nodes aware of each other form a cluster.

## Related
- **node-name** — A node is identified by its `name@host` atom.
- **EPMD** — The daemon that maps node names to ports.
- **magic-cookie** — Nodes authenticate with a shared cookie.

## Contrasts With
- None.

# Common Errors

- **Error**: Trying to connect a `-name` node to an `-sname` node.
  **Correction**: All connected nodes must use the same naming mode; long and short names cannot mix.

# Common Confusions

- **Confusion**: Thinking a node equals a physical machine.
  **Clarification**: A node is a VM instance; multiple nodes can run on a single host.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2 "Nodes and clustering," subsection 8.2.1 "Starting a node," and the "Nodes" sidebar.

# Verification Notes

- Definition source: Directly adapted from the Section 8.2 "Nodes" sidebar and 8.2.1.
- Confidence rationale: HIGH — the book explicitly defines what a node is.
- Uncertainties: None.
- Cross-reference status: Verified.
