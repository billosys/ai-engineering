---
concept: Node Connection
slug: node-connection
category: distribution
subcategory: distribution-model
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Connecting Nodes"
extraction_confidence: high
aliases:
  - "node connection"
  - "connecting nodes"
  - "net_kernel:connect_node"
  - "node mesh"
prerequisites:
  - distributed-node
  - epmd
extends: []
related:
  - erlang-cookie
  - hidden-node
  - distributed-message-passing
contrasts_with: []
answers_questions:
  - "How do I connect Erlang nodes?"
  - "Why do Erlang nodes form a full mesh?"
  - "How do I detect when a node disconnects?"
---

# Node Connection

## Quick Definition

A node connection joins two Erlang nodes so they can exchange messages. When a node joins a connected group, it automatically connects to every node in that group, forming a full mesh.

## Core Definition

A node can "decide to set up a connection to another node" (Ch. 26, "This Is My Boomstick"). When it does, "both nodes automatically start monitoring each other, and they can tell if the connection is dropped or a node disappears." Crucially, "when a new node joins another node that is already part of a group of nodes connected together, the new node automatically connects to the entire group" — everyone connects to everyone. Connections are made with `net_kernel:connect_node(NodeName)`, which returns `true` on success or `false` on failure (Ch. 26, "Connecting Nodes").

## Prerequisites

- **Distributed-node** — Connections join named nodes
- **Epmd** — Nodes locate each other by name through EPMD before connecting

## Key Properties

1. `net_kernel:connect_node(NodeName)` sets up a connection, returning `true` or `false`
2. Connected nodes automatically monitor each other for disconnection
3. Joining a connected group connects you to the entire group (full mesh)
4. Almost any inter-node interaction (`spawn/2`, sending to a remote pid) auto-creates a connection
5. `nodes()` lists connected nodes; `nodes(known)` lists all ever-connected nodes
6. `erlang:disconnect_node(Node)` disconnects a node without shutting it down
7. `erlang:monitor_node(NodeName, true)` delivers `{nodedown, NodeName}` if the node dies

## Construction / Recognition

### To connect nodes

1. Start the nodes with matching name styles and cookies
2. From one node call `net_kernel:connect_node(OtherNode@Host)`
3. A `true` result means you are in distributed mode; `false` usually means a network/host-file problem
4. Verify with `nodes()`

## Context & Application

Mesh connectivity aids fault tolerance (no node is left isolated) but limits scalability because of the number of connections and the chatter involved. The book recommends splitting large systems into smaller clusters.

## Examples

**Example** (Ch. 26): Connecting `fries` to `ketchup` —

```erlang
(ketchup@ferdmbp)1> net_kernel:connect_node(fries@ferdmbp).
true
```

**Example** (Ch. 26): The zombie-survivor mesh — when Rick meets Bill and they share frequencies, the connections spread until any survivor can contact any other directly.

## Relationships

### Builds Upon

- **Distributed-node** — Connections link nodes
- **Epmd** — Name resolution precedes connection

### Related

- **Erlang-cookie** — Two nodes connect only if their cookies match
- **Hidden-node** — A hidden node connects without joining the full mesh
- **Distributed-message-passing** — Connections carry cross-node messages

## Common Errors

- **Error**: `connect_node` returns `false` and you assume the API is wrong.
  **Correction**: `false` usually means a network or host-file misconfiguration; fix host files and retry.
- **Error**: Connecting an admin node to a cluster node, accidentally joining the whole mesh.
  **Correction**: Use a `-hidden` node, or `erlang:send(Dest, Msg, [noconnect])`, to avoid auto-meshing.

## Common Confusions

- **Confusion**: Thinking you must connect to each node individually.
  **Clarification**: Joining one node in a connected group connects you to the entire group automatically.
- **Confusion**: Believing connections need explicit setup for every interaction.
  **Clarification**: Almost any interaction (spawn, message to a remote pid) auto-creates a connection.

## Source Reference

Chapter 26, "Distribunomicon," sections "This Is My Boomstick," "Connecting Nodes," and "More Tools."

## Verification Notes

- Definition: Direct adaptation from "This Is My Boomstick" and "Connecting Nodes"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter demonstrates connections in detail
- Cross-references: `distributed-node`, `epmd`, `erlang-cookie`, `hidden-node`, `distributed-message-passing` planned this chapter
