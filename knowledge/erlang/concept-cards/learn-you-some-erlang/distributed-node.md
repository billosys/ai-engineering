---
concept: Distributed Node
slug: distributed-node
category: distribution
subcategory: distribution-model
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "This Is My Boomstick"
extraction_confidence: high
aliases:
  - "node"
  - "Erlang node"
  - "distributed node"
prerequisites:
  - distributed-erlang
extends: []
related:
  - epmd
  - node-connection
  - erlang-cookie
  - hidden-node
contrasts_with: []
answers_questions:
  - "What is a distributed Erlang node?"
  - "How do I name and start an Erlang node?"
  - "What is the difference between long names and short names?"
---

# Distributed Node

## Quick Definition

A node is a running Erlang VM with a name, ready to connect to other VMs. In Erlang each VM is a node — you can run many nodes on one computer or one per computer.

## Core Definition

"An instance of an Erlang VM that is up and running, ready to connect to other VMs, is called a *node*" (Ch. 26, "This Is My Boomstick"). Unlike communities that equate a node with a server, in Erlang each VM is a node; 50 nodes may run on one computer or across 50 computers. A node is given a name of the form `Name@Host`, where the host comes from DNS or the computer's host file. Names must be unique; starting a node with a name already in use on the same host produces a crash. Names are *long* (fully qualified domain names, containing a period) or *short* (hostnames with no period); nodes with short names cannot communicate with nodes with long names.

## Prerequisites

- **Distributed-erlang** — A node is the unit of a distributed Erlang system

## Key Properties

1. Each running Erlang VM is one node
2. Node names take the form `Name@Host`
3. Names must be unique on a host; a clash produces a crash message
4. *Long names* are fully qualified domain names (contain a period); *short names* have no period
5. Short-name and long-name nodes cannot communicate with each other
6. Start with `erl -sname short_name` or `erl -name long_name`
7. `node()` returns the current node's name; `nodes()` lists connected nodes
8. A non-distributed node can become distributed at runtime via `net_kernel:start/1`

## Construction / Recognition

### To start a node

1. Short names: `erl -sname short_name@domain` (or just `erl -sname short_name`)
2. Long names: `erl -name long_name@some.domain`
3. Optionally specify a direct IP: `erl -name name@127.0.0.1`
4. Windows users start `werl` from the command line, not via a shortcut

## Context & Application

Running many nodes on a single computer with short names is the easiest way to experiment with distribution, since connecting nodes across hosts is "a special kind of pain."

## Examples

**Example** (Ch. 26): Starting two short-named nodes —

```
$ erl -sname ketchup
(ketchup@ferdmbp)1>
$ erl -sname fries
(fries@ferdmbp)1>
```

**Example** (Ch. 26): `node()` returns `ketchup@ferdmbp`; `nodes()` returns `[fries@ferdmbp]` after a connection.

## Relationships

### Builds Upon

- **Distributed-erlang** — Nodes are the building blocks of distribution

### Related

- **Epmd** — Registers node names so nodes can find each other
- **Node-connection** — Nodes connect to form clusters
- **Erlang-cookie** — Controls which nodes a node will connect to
- **Hidden-node** — A node started with `-hidden` that does not auto-join the mesh

## Common Errors

- **Error**: Starting a node with a name already taken on the same host.
  **Correction**: Names must be unique; a clash produces a terrible crash message.
- **Error**: Trying to connect a short-name node to a long-name node.
  **Correction**: Short-name and long-name nodes cannot communicate; use the same naming scheme everywhere.

## Common Confusions

- **Confusion**: Thinking a node is a physical server.
  **Clarification**: In Erlang each VM is a node; many can run on one machine.
- **Confusion**: Believing the naming style is cosmetic.
  **Clarification**: Long vs short names determine interoperability — mismatched styles cannot connect.

## Source Reference

Chapter 26, "Distribunomicon," sections "This Is My Boomstick" and "Through the Desert on a Node with No Name."

## Verification Notes

- Definition: Direct adaptation from "This Is My Boomstick" and the naming section
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter defines nodes and naming precisely
- Cross-references: `distributed-erlang`, `epmd`, `node-connection`, `erlang-cookie`, `hidden-node` planned this chapter
