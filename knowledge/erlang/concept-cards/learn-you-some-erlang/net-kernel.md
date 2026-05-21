---
concept: net_kernel Module
slug: net-kernel
category: distribution
subcategory: distribution-infrastructure
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "The net_kernel Module"
extraction_confidence: high
aliases:
  - "net_kernel"
  - "net_kernel module"
prerequisites:
  - distributed-node
  - node-connection
extends: []
related:
  - tick-time
contrasts_with: []
answers_questions:
  - "What does the net_kernel module do?"
  - "How do I make a non-distributed node distributed at runtime?"
  - "How do I connect and disconnect nodes programmatically?"
---

# net_kernel Module

## Quick Definition

`net_kernel` is the module for connecting and disconnecting nodes and for turning a non-distributed node into a distributed one (and back) at runtime.

## Core Definition

`net_kernel` "is the module we used to connect and disconnect nodes" (Ch. 26, "The net_kernel Module"). Beyond `net_kernel:connect_node/1`, it can transform a non-distributed node into a distributed one with `net_kernel:start/1`, and switch a distributed node back to a normal one with `net_kernel:stop/0`. It also controls the tick time, the heartbeat-based interval that determines how long before an unresponsive node is considered dead.

## Prerequisites

- **Distributed-node** — `net_kernel` manages node identity and distribution state
- **Node-connection** — `net_kernel:connect_node/1` establishes connections

## Key Properties

1. `net_kernel:connect_node(NodeName)` connects to another node
2. `net_kernel:start([Name, Type])` makes a running non-distributed node distributed
3. `Type` is `shortnames` or `longnames`, equivalent to `-sname` or `-name`
4. A third argument `net_kernel:start([Name, Type, HeartbeatInMilliseconds])` sets the heartbeat delay (default 15000 ms)
5. After four failed heartbeats a remote node is considered dead; heartbeat × 4 is the tick time
6. `net_kernel:set_net_ticktime(S)` changes the node's tick time to avoid disconnections
7. `net_kernel:stop()` switches a distributed node back to a normal node

## Construction / Recognition

### To make a node distributed at runtime

1. Start a plain `erl` shell
2. Call `net_kernel:start([nodename, shortnames])`
3. The prompt becomes a distributed node prompt

## Context & Application

`net_kernel:start/1` is useful for nodes that begin life non-distributed. Tuning the heartbeat or tick time matters when a node sends large messages that could delay heartbeats.

## Examples

**Example** (Ch. 26): Making a node distributed at runtime —

```erlang
1> net_kernel:start([romero, shortnames]).
{ok,<0.43.0>}
(romero@ferdmbp)2>
```

**Example** (Ch. 26): Tuning and stopping —

```erlang
(romero@ferdmbp)2> net_kernel:set_net_ticktime(5).
change_initiated
(romero@ferdmbp)3> net_kernel:stop().
ok
```

## Relationships

### Builds Upon

- **Distributed-node** — `net_kernel` controls node distribution state
- **Node-connection** — `connect_node/1` is a `net_kernel` function

### Related

- **Tick-time** — `net_kernel` sets the heartbeat/tick time governing node-down detection

## Common Errors

- **Error**: Expecting `net_kernel:stop()` to shut down the VM.
  **Correction**: It only makes the node non-distributed again; the VM keeps running.
- **Error**: Leaving the default tick time when sending large messages.
  **Correction**: Large messages can delay heartbeats; raise the tick time with `set_net_ticktime/1` to avoid false disconnections.

## Common Confusions

- **Confusion**: Thinking distribution can only be enabled via `erl -sname`/`-name` at startup.
  **Clarification**: `net_kernel:start/1` makes a node distributed at runtime.

## Source Reference

Chapter 26, "Distribunomicon," section "The net_kernel Module."

## Verification Notes

- Definition: Direct adaptation from "The net_kernel Module"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates each function
- Cross-references: `distributed-node`, `node-connection`, `tick-time` planned this chapter
