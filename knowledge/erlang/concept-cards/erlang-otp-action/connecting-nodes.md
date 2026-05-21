---
# === CORE IDENTIFICATION ===
concept: Connecting Nodes
slug: connecting-nodes

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
section: "8.2.2 Connecting nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "net_adm:ping"
  - "node connection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - erlang-cluster
extends: []
related:
  - epmd
  - magic-cookie
  - node-name
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I connect two Erlang nodes?"
  - "What does net_adm:ping/1 return?"
  - "Do nodes find each other automatically?"
---

# Quick Definition

Connecting nodes is the act of making two Erlang nodes aware of each other, most simply with `net_adm:ping/1`, which returns `pong` on success and `pang` on failure.

# Core Definition

Connecting nodes is the process by which separate Erlang nodes become aware of each other and join a cluster. Nodes do not actively try to find each other — they must be given a reason to look. The simplest way, when connecting is all you want, is the standard library function `net_adm:ping/1`, which takes a target node name and returns the atom `pong` if communication succeeded or `pang` otherwise. Once two nodes are connected they keep track of each other and exchange information about other nodes they know, so the cluster becomes fully connected and stays connected even if the node that introduced two others later dies. The built-in `nodes()` function lists the currently connected nodes (Ch. 8, Section 8.2.2).

# Prerequisites

- **erlang-node** — Connecting acts on nodes.
- **erlang-cluster** — Connecting nodes is how a cluster is formed and grown.

# Key Properties

1. Nodes do not discover each other automatically — connection must be triggered.
2. `net_adm:ping(Node)` is the simplest way to connect.
3. `net_adm:ping` returns `pong` on success, `pang` on failure.
4. Connected nodes exchange knowledge of other nodes, forming a full mesh.
5. The cluster survives the loss of the node that introduced others.
6. `nodes()` lists currently connected nodes.

# Construction / Recognition

## To Connect Nodes:
1. Ensure both nodes share the same magic cookie and compatible name forms.
2. From one node, call `net_adm:ping('other@host')`.
3. Check the result is `pong`; verify with `nodes()` on each node.

## To Recognize:
1. A `net_adm:ping/1` call, or a non-empty `nodes()` list, indicates node connection activity.

# Context & Application

- **Typical contexts**: Bootstrapping clusters; joining a new node to a running cluster.
- **Common applications**: Pinging known contact nodes at application startup.
- **Historical/stylistic notes**: `pang` is Swedish for "bang," as in "crash, bang, it failed."

# Examples

**Example 1** (Section 8.2.2): `net_adm:ping('b@mybox.home.net')` returns `pong`; afterward `nodes()` on each node shows the other.

**Example 2** (Section 8.2.2): After connecting `a-b` and `b-c`, killing `b` leaves `a` and `c` still connected to each other — `nodes()` confirms it.

# Relationships

## Builds Upon
- **erlang-node** — Connection acts on nodes.
- **erlang-cluster** — Connecting builds the cluster.

## Enables
- None.

## Related
- **EPMD** — EPMD resolves node names to ports during connection.
- **magic-cookie** — Connection fails if cookies differ.
- **node-name** — Connection targets a node by name.

## Contrasts With
- None.

# Common Errors

- **Error**: `net_adm:ping` returning `pang` because of a DNS-unresolvable fully qualified name.
  **Correction**: Restart nodes with `-sname` (short names) and retry; verify with command-line `ping`.

# Common Confusions

- **Confusion**: Expecting nodes to find each other on their own.
  **Clarification**: Connection must be triggered (e.g., a `ping`); EPMDs never locate each other automatically.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.2 "Connecting nodes."

# Verification Notes

- Definition source: Directly adapted from Section 8.2.2.
- Confidence rationale: HIGH — the book demonstrates connection with `net_adm:ping` explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
