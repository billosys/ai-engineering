---
concept: Hidden Node
slug: hidden-node
category: distribution
subcategory: distribution-model
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Hidden Nodes"
extraction_confidence: high
aliases:
  - "hidden node"
  - "-hidden flag"
prerequisites:
  - distributed-node
  - node-connection
extends: []
related:
  - erlang-cookie
contrasts_with: []
answers_questions:
  - "What is a hidden node?"
  - "How do I connect to a node without joining the whole cluster?"
  - "How do I see hidden connections?"
---

# Hidden Node

## Quick Definition

A hidden node is a node started with the `-hidden` flag. It can connect to a specific node without automatically joining that node's full cluster mesh.

## Core Definition

Normally "pretty much any interaction between nodes will get them to set up a connection," and joining one node joins the whole group (Ch. 26, "Hidden Nodes"). This is undesirable when, for example, you want an admin node to connect to a single cluster node without becoming part of the cluster. A node started with `-hidden` connects only to the nodes you explicitly connect it to, and those connections do not propagate. Hidden connections do not appear in `nodes()` but do appear in `nodes(hidden)` and `nodes(connected)`.

## Prerequisites

- **Distributed-node** — A hidden node is still an ordinary node
- **Node-connection** — Hidden nodes form connections, just non-propagating ones

## Key Properties

1. Started with `erl -sname name -hidden`
2. A hidden node connects only to nodes it explicitly connects to
3. Its connections do not propagate to the rest of the cluster
4. `nodes()` does not show hidden connections; `nodes(hidden)` does
5. `nodes(connected)` shows all connections regardless of type
6. Other cluster nodes never see a connection to the hidden node unless told to connect to it
7. An alternative for a single message without a connection is `erlang:send(Dest, Message, [noconnect])`, but that is error-prone

## Construction / Recognition

### To use a hidden node

1. Start it with the `-hidden` flag
2. Call `net_kernel:connect_node(TargetNode)` for each node it should reach
3. Inspect connections with `nodes(hidden)` and `nodes(connected)` (not `nodes()`)

## Context & Application

Hidden nodes are ideal for admin/ops tooling — connect to one node to reload modules or debug without the cluster believing it has a new coworker to send tasks to.

## Examples

**Example** (Ch. 26): `olives` started hidden, connecting only to `mustard` —

```erlang
(olives@ferdmbp)1> net_kernel:connect_node(mustard@ferdmbp).
true
(olives@ferdmbp)2> nodes().
[]
(olives@ferdmbp)3> nodes(hidden).
[mustard@ferdmbp]
```

`salad` never sees the connection to `olives`.

## Relationships

### Builds Upon

- **Distributed-node** — A hidden node is a node with the `-hidden` flag
- **Node-connection** — It forms non-propagating connections

### Related

- **Erlang-cookie** — A hidden node still needs a matching cookie to connect

## Common Errors

- **Error**: Connecting an admin node normally and accidentally joining it to the whole cluster.
  **Correction**: Start admin/ops nodes with `-hidden` so connections do not propagate.
- **Error**: Checking `nodes()` for a hidden connection and seeing nothing.
  **Correction**: Use `nodes(hidden)` or `nodes(connected)` to see hidden connections.

## Common Confusions

- **Confusion**: Thinking a hidden node has no connections.
  **Clarification**: It has connections; they just do not show in `nodes()` or propagate to the mesh.

## Source Reference

Chapter 26, "Distribunomicon," section "Hidden Nodes."

## Verification Notes

- Definition: Direct adaptation from "Hidden Nodes"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates hidden nodes precisely
- Cross-references: `distributed-node`, `node-connection`, `erlang-cookie` planned this chapter
