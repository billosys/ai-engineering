---
concept: Remote Procedure Call (rpc Module)
slug: remote-procedure-call
category: distribution
subcategory: distribution-model
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "The rpc Module"
extraction_confidence: high
aliases:
  - "RPC"
  - "rpc module"
  - "remote procedure call"
  - "rpc:call"
  - "rpc:multicall"
prerequisites:
  - distributed-message-passing
  - node-connection
extends: []
related:
  - distributed-message-passing
contrasts_with: []
answers_questions:
  - "What is the rpc module?"
  - "How do I run a function on a remote Erlang node?"
  - "How do I call many nodes at once?"
---

# Remote Procedure Call (rpc Module)

## Quick Definition

The `rpc` module runs functions on remote Erlang nodes and returns the results locally. It supports synchronous calls, asynchronous promise-style calls, and calls across many nodes at once.

## Core Definition

The `rpc` module "contains functions that let you execute commands on remote nodes, as well as a few functions that facilitate parallel operations" (Ch. 26, "The rpc Module"). The basic operation is `rpc:call(Node, Module, Function, Args)` — it runs the function on the remote node and returns whatever the function returned, or `{badrpc, Reason}` on failure; a fifth argument adds a timeout. Asynchronous variants (`rpc:async_call/4` paired with `rpc:yield/1`) act as promises/futures. Multi-node functions (`rpc:multicall/4` and `rpc:eval_everywhere/4`) call or cast to many nodes at once.

## Prerequisites

- **Distributed-message-passing** — RPC is built on transparent cross-node messaging
- **Node-connection** — Target nodes must be connected

## Key Properties

1. `rpc:call(Node, Module, Function, Args)` runs a function remotely, returning its result or `{badrpc, Reason}`
2. `rpc:call/5` adds a timeout, returning `{badrpc, timeout}` if exceeded
3. `rpc:async_call(Node, M, F, A)` returns a key; `rpc:yield(Key)` later fetches the result (promise/future)
4. `rpc:nb_yield(Key)` polls without blocking; `rpc:nb_yield(Key, Timeout)` waits up to a timeout
5. `rpc:cast(Node, M, F, A)` runs a command remotely and ignores the result
6. `rpc:multicall(Nodes, M, F, A)` calls many nodes; returns `{Results, BadNodes}`
7. `rpc:eval_everywhere(Nodes, M, F, A)` casts to many nodes (the multi-node form of `cast`)

## Construction / Recognition

### To call a remote node

1. Synchronous: `rpc:call(Node, Module, Function, Args)`
2. Asynchronous: `Key = rpc:async_call(...)`, do other work, then `rpc:yield(Key)`
3. Many nodes, results needed: `rpc:multicall(Nodes, M, F, A)`
4. Many nodes, fire-and-forget: `rpc:eval_everywhere(Nodes, M, F, A)`

## Context & Application

Asynchronous RPC is useful when a remote call is slow: send it off, do other work, then collect the result. `multicall`/`eval_everywhere` scale to clusters where calling each node individually would not.

## Examples

**Example** (Ch. 26): A synchronous call —

```erlang
(cthulu@ferdmbp)1> rpc:call(lovecraft@ferdmbp, lists, sort, [[a,e,f,t,h,s,a]]).
[a,a,e,f,h,s,t]
```

**Example** (Ch. 26): A multicall checking liveness — `rpc:multicall(nodes(), erlang, is_alive, [])` returns `{[true,true,true,true],[]}` (left side alive, right side unreachable).

## Relationships

### Builds Upon

- **Distributed-message-passing** — RPC is layered on cross-node messaging
- **Node-connection** — Targets must be connected nodes

### Related

- **Distributed-message-passing** — Remote `spawn` is described as essentially a remote procedure call

## Common Errors

- **Error**: Ignoring the `{badrpc, Reason}` return.
  **Correction**: RPC failures (including `{badrpc, timeout}`) return that tuple; handle it explicitly.
- **Error**: Calling many nodes with repeated single `rpc:call`s.
  **Correction**: Use `multicall`/`eval_everywhere`, which scale to large clusters.

## Common Confusions

- **Confusion**: Thinking `rpc:async_call` returns the result.
  **Clarification**: It returns a key; `rpc:yield` (or `nb_yield`) fetches the actual result later.
- **Confusion**: Believing `rpc:multicall`'s result is a flat list.
  **Clarification**: It returns `{Results, BadNodes}` — successes and unreachable nodes separated.

## Source Reference

Chapter 26, "Distribunomicon," section "The rpc Module."

## Verification Notes

- Definition: Direct adaptation from "The rpc Module"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates each `rpc` function
- Cross-references: `distributed-message-passing`, `node-connection` planned this chapter
