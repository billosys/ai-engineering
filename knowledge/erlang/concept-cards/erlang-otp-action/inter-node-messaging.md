---
# === CORE IDENTIFICATION ===
concept: Sending Messages Between Nodes
slug: inter-node-messaging

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
section: "8.2.5 Sending messages between connected nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "remote message passing"
  - "registered name with node tuple"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
  - location-transparency
  - erlang-cluster
extends: []
related:
  - erlang-node
  - send-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I send a message to a process on another node?"
  - "What does the {Name, Node} destination form mean?"
  - "How can I tell a remote pid from a local one?"
---

# Quick Definition

Sending messages between nodes uses the same `!` operator as local sends; a process registered on a remote node is addressed with the tuple `{RegisteredName, Node}`, and replies use the sender's pid directly.

# Core Definition

Sending messages between connected nodes works through the same message-passing primitives as local communication. To send to a process registered under a known name on a remote node, the destination is the tuple `{RegisteredName, Node}` — for example `{shell, Node} ! Message`. A bare registered name (`shell ! Message`) always refers to a process registered on the local node. To reply, a receiver simply sends to the sender's pid, because the destination node is encoded in the pid. A pid's textual representation reveals locality: the first number is zero for a local process and non-zero for one residing on another node (Ch. 8, Section 8.2.5).

# Prerequisites

- **message-passing** — Inter-node messaging is ordinary message passing extended across the network.
- **location-transparency** — The send operation behaves identically for remote destinations.
- **erlang-cluster** — The nodes must be connected in a cluster.

# Key Properties

1. Uses the same `!` operator as local message sending.
2. A remote registered process is addressed as `{RegisteredName, Node}`.
3. A bare registered name refers to the local node only.
4. Replies use the sender's pid directly — the node is encoded in it.
5. A pid's first number is zero for local processes, non-zero for remote ones.

# Construction / Recognition

## To Send to a Remote Process:
1. Register the target process under a known name on its node.
2. From another node, send with `{Name, Node} ! Message`.
3. Include `self()` in the message so the receiver can reply to your pid.

## To Recognize:
1. A send to a `{Name, Node}` tuple, or a pid whose first number is non-zero, indicates remote messaging.

# Context & Application

- **Typical contexts**: Distributed coordination, RPC-style exchanges, cluster-wide broadcasts.
- **Common applications**: Broadcasting to registered processes on all `nodes()`; the resource discovery protocol.
- **Historical/stylistic notes**: The book demonstrates this with shells registered as `shell` on nodes `b` and `c`, messaged from node `a`.

# Examples

**Example 1** (Section 8.2.5): `lists:foreach(fun(Node) -> {shell, Node} ! {self(), "hello!"} end, nodes())` sends a message to the `shell`-registered process on every connected node.

**Example 2** (Section 8.2.5): A received `From` pid prints as `<5135.37.0>` — the non-zero first number shows it comes from another node; replying with `From ! {...}` routes back to the correct node.

# Relationships

## Builds Upon
- **message-passing** — Inter-node messaging is message passing across the network.
- **location-transparency** — Makes remote sends syntactically identical to local ones.
- **erlang-cluster** — The nodes must be connected.

## Enables
- None.

## Related
- **erlang-node** — Messages are addressed to processes on named nodes.
- **send-operator** — The `!` operator used for both local and remote sends.

## Contrasts With
- None.

# Common Errors

- **Error**: Writing `Name ! Msg` and expecting it to reach a remote node.
  **Correction**: Use `{Name, Node} ! Msg`; a bare name targets only the local node.

# Common Confusions

- **Confusion**: Thinking remote sends need special functions or marshalling.
  **Clarification**: The same `!` operator works; any Erlang term can be sent as-is.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.5 "Sending messages between connected nodes."

# Verification Notes

- Definition source: Directly adapted from Section 8.2.5.
- Confidence rationale: HIGH — the book walks through remote messaging with worked examples.
- Uncertainties: None.
- Cross-reference status: Verified; `send-operator` exists as a card in this directory.
