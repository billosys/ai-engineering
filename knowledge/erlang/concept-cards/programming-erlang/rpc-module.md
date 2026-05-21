---
# === CORE IDENTIFICATION ===
concept: rpc Module
slug: rpc-module

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-libraries
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "Libraries and BIFS for Distributed Programming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rpc:call/4"
  - "remote procedure call"
  - "rpc:multicall"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
  - distributed-erlang
extends: []
related:
  - distribution-bifs
  - remote-spawning
  - global-module
contrasts_with:
  - remote-spawning

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform a remote procedure call in Erlang?"
  - "Which standard module provides remote procedure call services?"
  - "How does the rpc module relate to distributed Erlang?"
---

# Quick Definition

`rpc` is a standard Erlang library module that provides remote procedure call services; its most useful function, `rpc:call(Node, Mod, Function, Args)`, evaluates `Mod:Function(Args)` on a remote node and returns the result.

# Core Definition

When writing distributed programs you rarely start from scratch; the standard libraries contain modules that hide much of the complexity. Two modules cover most needs: `rpc`, which provides a number of remote procedure call services, and `global`, which handles distributed name registration and locks (Chapter 14, "Libraries and BIFS for Distributed Programming"). The single most useful function in `rpc` is `call(Node, Mod, Function, Args) -> Result | {badrpc, Reason}`, which evaluates `apply(Mod, Function, Args)` on `Node` and returns the result `Result`, or `{badrpc, Reason}` if the call fails. The `rpc` module is distinct from any locally defined `rpc` function — it is a standard library module. (The book also shows `rpc:multicall(Nodes, Mod, Func, Args)`, which performs a call on multiple nodes.)

# Prerequisites

- **Node** — `rpc:call` targets a named node.
- **Distributed Erlang** — `rpc` operates between connected distributed nodes.

# Key Properties

1. `rpc` is a standard library module providing remote procedure call services.
2. `rpc:call(Node, Mod, Function, Args)` evaluates `apply(Mod, Function, Args)` on `Node`.
3. It returns `Result` on success or `{badrpc, Reason}` on failure.
4. It hides the complexity of the lower-level distribution BIFs.
5. `rpc:multicall(Nodes, ...)` performs a call across multiple nodes at once.

# Construction / Recognition

## To Use rpc:
1. Ensure the target node is connected and shares the cookie.
2. Call `rpc:call(Node, Mod, Function, Args)`.
3. Match on `Result` or `{badrpc, Reason}`.

## To Recognize It:
1. Look for `rpc:call/4` and `rpc:multicall/4` calls.
2. Distinguish the standard `rpc` module from hand-written `rpc` helper functions.

# Context & Application

- **Typical contexts**: Invoking functions on remote nodes without managing remote processes yourself.
- **Common applications**: The distributed `kvs` name server is driven with `rpc:call(gandalf@localhost, kvs, store, [...])`.
- **Historical/stylistic notes**: The book warns that `rpc:multicall(nodes(), os, cmd, ["cd /; rm -rf *"])` shows how dangerous distributed Erlang's trust model is.

# Examples

**Example 1** (Chapter 14, "Stage 2"): `rpc:call(gandalf@localhost, kvs, store, [weather, fine])` runs `kvs:store(weather, fine)` on node `gandalf`, returning `true`.

**Example 2** (Chapter 14, "Stage 2"): `rpc:call(gandalf@localhost, kvs, lookup, [weather])` runs `kvs:lookup(weather)` remotely and returns `{ok, fine}`.

# Relationships

## Builds Upon
- **Distribution BIFs** — `rpc` is written using the lower-level distribution primitives.

## Enables
- Convenient remote function invocation across a cluster.

## Related
- **global module** — the companion standard module for distributed name registration.

## Contrasts With
- **Remote spawning** — `rpc:call` is a one-shot remote evaluation returning a value; remote spawning creates a persistent process you must message yourself.

# Common Errors

- **Error**: Confusing the standard `rpc` module with a locally defined `rpc` function.
  **Correction**: The chapter explicitly notes `rpc` is a standard library module, separate from the hand-written `rpc` helper.
- **Error**: Ignoring the `{badrpc, Reason}` return.
  **Correction**: Always match for `{badrpc, Reason}` since the remote call may fail.

# Common Confusions

- **Confusion**: `rpc:call` keeps a process alive on the remote node.
  **Clarification**: It performs a single `apply` and returns; it does not leave a persistent process.
- **Confusion**: `rpc` provides security.
  **Clarification**: It runs on distributed Erlang's trusted model — `rpc:multicall` can run arbitrary destructive commands on every node.

# Source Reference

Chapter 14: Distributed Programming, section "Libraries and BIFS for Distributed Programming" (the `rpc:call/4` spec) and section "Building the Name Server" (Stage 2, `rpc:call` examples); danger note in "Socket-Based Distribution."

# Verification Notes

- Definition source: Direct adaptation of the `rpc:call/4` spec and the `kvs` examples.
- Confidence rationale: HIGH — `rpc:call` is explicitly specified and demonstrated.
- Uncertainties: `rpc:multicall` is mentioned only via the destructive example; treated as a minor secondary detail.
- Cross-reference status: Slugs match canonical `node`/`distributed-erlang` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
