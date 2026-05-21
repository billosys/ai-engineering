---
# === CORE IDENTIFICATION ===
concept: Remote Spawning
slug: remote-spawning

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-primitives
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "An Example of Remote Spawning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "spawn/2"
  - "spawn/4"
  - "spawn on a remote node"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spawn
  - node
  - distributed-erlang
extends:
  - spawn
related:
  - distribution-bifs
  - rpc-module
  - message-passing
contrasts_with:
  - rpc-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I spawn a process on a remote node?"
  - "How does spawn relate to distributed Erlang?"
  - "How do I run code on another machine?"
---

# Quick Definition

Remote spawning is creating a process on another Erlang node by passing a node name to `spawn` or `spawn_link`; the returned PID identifies a process running on that remote node, and message passing to it works transparently.

# Core Definition

`spawn(Node, Fun)` works exactly like `spawn(Fun)`, but the new process is spawned on `Node`; `spawn(Node, Mod, Func, ArgList)` works exactly like `spawn(Mod, Func, ArgList)` but on `Node` (Chapter 14, "Libraries and BIFS for Distributed Programming"). After remote spawning, the returned `Pid` is the identifier of a process on the remote node, and all the message-passing primitives work transparently toward it. The `Mod/Func/Args` form is more robust than the `Fun` form, because `spawn(Node, Fun)` can break when the distributed nodes are not running exactly the same version of a particular module. For remote spawning to work, both nodes must have access to the spawned code — either by running from the same directory, by copying the `.beam` file, or by code-server configuration.

# Prerequisites

- **Spawn** — Remote spawning is `spawn` with a node argument.
- **Node** — The target of a remote spawn is a named node.
- **Distributed Erlang** — Remote spawning only works between connected distributed nodes.

# Key Properties

1. `spawn(Node, ...)` creates a process on the named remote node.
2. The returned `Pid` identifies a process on the remote node.
3. Message passing, links, and monitors work transparently toward the remote process.
4. The `Mod/Func/Args` form is more robust than the `Fun` form against module-version mismatches.
5. Both nodes must have the spawned module's code available.

# Construction / Recognition

## To Spawn Remotely:
1. Ensure both nodes are connected and share a cookie, and both have the module's code.
2. Call `spawn(Node, Mod, Func, Args)` (preferred) or `spawn(Node, Fun)`.
3. Use the returned `Pid` like any local PID — send it messages, link to it.

## To Recognize It:
1. Look for `spawn` / `spawn_link` calls whose first argument is a node name atom.
2. Look for PIDs printed with a nonzero first field (e.g. `<5094.40.0>`), indicating a remote process.

# Context & Application

- **Typical contexts**: Distributing computation across nodes; placing a server process on a chosen node.
- **Common applications**: The `dist_demo` example spawns a loop process on a remote node and drives it via a hand-rolled rpc.
- **Historical/stylistic notes**: Remote PIDs appear with a nonzero first number, distinguishing them from local processes.

# Examples

**Example 1** (Chapter 14, "An Example of Remote Spawning"): On `bilbo`, `Pid = dist_demo:start('gandalf@doris.myerl.example.com')` calls `spawn(Node, fun() -> loop() end)`, returning a remote PID `<5094.40.0>`.

**Example 2** (Chapter 14): `dist_demo:rpc(Pid, erlang, node, [])` then evaluates `erlang:node()` on the remote node and returns `'gandalf@doris.myerl.example.com'`.

# Relationships

## Builds Upon
- **Spawn** — remote spawning is `spawn` extended with a node argument.

## Enables
- Distributed computation and remote servers.

## Related
- **Distribution BIFs** — remote spawn is one of those BIFs.
- **Message passing** — works transparently toward remotely spawned processes.

## Contrasts With
- **rpc module** — `rpc:call` evaluates a function on a node and returns a result without keeping a process around; remote spawning creates a persistent process you message yourself.

# Common Errors

- **Error**: Using `spawn(Node, Fun)` when nodes run different versions of the module.
  **Correction**: Use `spawn(Node, Mod, Func, Args)`, which is robust to version mismatches.
- **Error**: Remote-spawning a module the remote node cannot load.
  **Correction**: Copy the `.beam` file or compile the source on every node first.

# Common Confusions

- **Confusion**: A remotely spawned process runs on the spawning node.
  **Clarification**: It runs on the target `Node`; only the `Pid` is held locally.
- **Confusion**: Remote spawning and `rpc:call` are the same.
  **Clarification**: Remote spawning creates a long-lived process; `rpc:call` performs a one-shot remote evaluation.

# Source Reference

Chapter 14: Distributed Programming, section "Libraries and BIFS for Distributed Programming" (the `spawn(Node, ...)` BIFs) and section "An Example of Remote Spawning" (the `dist_demo` example).

# Verification Notes

- Definition source: Direct adaptation of the remote `spawn` BIF specs and the `dist_demo` example.
- Confidence rationale: HIGH — remote spawning is explicitly specified and demonstrated.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `spawn`/`node`/`message-passing` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
