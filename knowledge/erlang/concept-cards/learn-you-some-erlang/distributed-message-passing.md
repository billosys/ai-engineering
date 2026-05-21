---
concept: Distributed Message Passing
slug: distributed-message-passing
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
  - "distributed message passing"
  - "cross-node messaging"
  - "remote spawn"
prerequisites:
  - node-connection
  - message-passing
extends:
  - message-passing
related:
  - remote-procedure-call
  - name-registration-global
contrasts_with: []
answers_questions:
  - "How do processes on different nodes communicate?"
  - "How do I send a message to a registered process on another node?"
  - "How do I spawn a process on a remote node?"
---

# Distributed Message Passing

## Quick Definition

Distributed message passing extends Erlang's local message passing across nodes. A process sends a message to `{Name, Node}` or a remote pid, and the VM serializes and delivers it transparently.

## Core Definition

"The distribution model of Erlang was designed so that local processes can contact remote processes and send them regular messages" (Ch. 26, "This Is My Boomstick"). Since process registries are per-node, you reach a remote process by sending to the tuple `{RegisteredName, Node}`. Messages — including pids, atoms, tuples, and binaries — are serialized and unserialized automatically. Output is also transparently redirected across the network thanks to group leaders. Remote `spawn/2`, `spawn/4`, `spawn_link/2`, and `spawn_link/4` let you run functions on remote nodes.

## Prerequisites

- **Node-connection** — Messaging requires nodes to be connected (or it auto-connects them)
- **Message-passing** — Distributed messaging is the local model extended across nodes

## Key Properties

1. A message to a remote registered process is sent to `{Name, Node}`
2. All Erlang data structures, including pids, serialize transparently for transmission
3. Links and monitors work across nodes
4. `spawn/2` and `spawn/4` run a function on a remote node; `spawn_link/2` and `spawn_link/4` also link
5. Output (IO) from a remote process is redirected back to the original shell via group leaders
6. A pid's printed form `<X.Y.Z>` encodes the node (`0` = current node), a counter, and an overflow counter
7. `node(Pid)` returns the node where a pid is running

## Construction / Recognition

### To message a remote process

1. Register the target process locally on its node
2. From another node, send to `{Name, Node}`: `{shell, fries@ferdmbp} ! Message`

### To run code on a remote node

`spawn(NodeName, fun() -> ... end)` — the function runs there, output comes back locally

## Context & Application

Remote `spawn` is essentially a remote procedure call. The book recommends sending small, descriptive messages ("player X found item Y") rather than large state, because all communications between two nodes share one TCP connection and large messages block heartbeats.

## Examples

**Example** (Ch. 26): Sending to a registered remote shell —

```erlang
(ketchup@ferdmbp)5> {shell, fries@ferdmbp} ! {hello, from, self()}.
(fries@ferdmbp)2> receive {hello, from, OtherShell} -> OtherShell ! <<"hey there!">> end.
```

**Example** (Ch. 26): Remote spawn —

```erlang
(ketchup@ferdmbp)6> spawn(fries@ferdmbp,
                          fun() -> io:format("I'm on ~p~n", [node()]) end).
I'm on fries@ferdmbp
```

## Relationships

### Builds Upon / Extends

- **Message-passing** — Distributed messaging is the local model extended over the network

### Builds Upon

- **Node-connection** — Connected nodes are required for messaging

### Related

- **Remote-procedure-call** — Remote spawn and the `rpc` module build on cross-node messaging
- **Name-registration-global** — `global` lets you address processes without knowing their node

## Common Errors

- **Error**: Sending huge messages between nodes.
  **Correction**: Large messages block the shared TCP channel and can hold back heartbeats, causing false node-down detection; keep messages small.
- **Error**: Assuming a remote pid `<6349.52.0>` is malformed.
  **Correction**: The first number identifies the node; only `0` means the current node.

## Common Confusions

- **Confusion**: Thinking remote messaging needs special send syntax for pids.
  **Clarification**: Remote pids work exactly like local ones; only registered names need the `{Name, Node}` form.
- **Confusion**: Believing remote process output is lost.
  **Clarification**: Group leaders redirect IO back to the calling shell transparently.

## Source Reference

Chapter 26, "Distribunomicon," sections "This Is My Boomstick," "Connecting Nodes," and "More Tools."

## Verification Notes

- Definition: Direct adaptation from "This Is My Boomstick" and "Connecting Nodes"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter demonstrates cross-node messaging and remote spawn
- Cross-references: `node-connection`, `remote-procedure-call`, `name-registration-global` planned this chapter; `message-passing` shared slug
