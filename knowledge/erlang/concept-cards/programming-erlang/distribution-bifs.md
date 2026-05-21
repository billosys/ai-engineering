---
# === CORE IDENTIFICATION ===
concept: Distribution BIFs
slug: distribution-bifs

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
section: "Libraries and BIFS for Distributed Programming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "distribution primitives"
  - "node/0"
  - "nodes/0"
  - "monitor_node/2"
  - "disconnect_node/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
  - distributed-erlang
extends: []
related:
  - remote-spawning
  - rpc-module
  - magic-cookie
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What primitives are used for distributed programming?"
  - "How do I find which nodes are connected?"
  - "How do I monitor whether a node joins or leaves the network?"
---

# Quick Definition

The distribution BIFs are the built-in functions for distributed programming — `spawn/2,4`, `spawn_link/2,4`, `node/0,1`, `nodes/0`, `is_alive/0`, `monitor_node/2`, and `disconnect_node/1` — that operate on nodes and remote processes.

# Core Definition

The primitives used for writing distributed programs are a set of built-in functions described in the manual page for the `erlang` module (Chapter 14, "Libraries and BIFS for Distributed Programming"). They include: `spawn(Node, Fun)` and `spawn(Node, Mod, Func, ArgList)`, which work like `spawn` but spawn on `Node`; `spawn_link(Node, ...)`, the linked variants; `disconnect_node(Node)`, which forcibly disconnects a node; `monitor_node(Node, Flag)`, which when `Flag` is `true` causes the calling process to be sent `{nodeup, Node}` and `{nodedown, Node}` messages as the node joins or leaves; `node()`, which returns the local node name (`nonode@nohost` if undistributed); `node(Arg)`, which returns the node where a PID, reference, or port is located; `nodes()`, which returns the list of all other connected nodes; and `is_alive()`, which returns `true` if the local node can be part of a distributed system. In addition, the syntax `{RegName, Node} ! Msg` sends `Msg` to the registered process `RegName` on `Node`.

# Prerequisites

- **Node** — These BIFs operate on and report about nodes.
- **Distributed Erlang** — The BIFs are only meaningful in a distributed context.

# Key Properties

1. `spawn(Node, ...)` / `spawn_link(Node, ...)` create processes on a remote node.
2. `node()` returns the local node; `node(Arg)` returns the node owning a PID/reference/port.
3. `nodes()` lists all other connected nodes.
4. `is_alive()` reports whether the local node is distributed.
5. `monitor_node(Node, true)` delivers `{nodeup, Node}`/`{nodedown, Node}` messages.
6. `disconnect_node(Node)` forcibly disconnects a node.
7. `{RegName, Node} ! Msg` sends to a registered process on a remote node.

# Construction / Recognition

## To Use the Distribution BIFs:
1. Call `node()`/`nodes()` to inspect the local node and its connections.
2. Call `spawn(Node, Mod, Func, Args)` to create a remote process.
3. Call `monitor_node(Node, true)` to be notified of node up/down events.
4. Send `{RegName, Node} ! Msg` to reach a registered remote process.

## To Recognize Them:
1. Look for `spawn`/`spawn_link` calls taking a `Node` argument.
2. Look for `{nodeup, Node}` / `{nodedown, Node}` message handling.

# Context & Application

- **Typical contexts**: Low-level distributed programming when not using the higher-level `rpc`/`global` modules.
- **Common applications**: Remote process creation; monitoring cluster membership; addressing registered remote processes.
- **Historical/stylistic notes**: The book notes `spawn(Node, Mod, Func, Args)` is more robust than `spawn(Node, Fun)`, which can break when nodes do not run the same version of a module.

# Examples

**Example 1** (Chapter 14, "Libraries and BIFS for Distributed Programming"): `monitor_node(Node, true)` causes the calling process to receive `{nodeup, Node}` and `{nodedown, Node}` messages when `Node` joins or leaves the set of connected nodes.

**Example 2** (Chapter 14): The syntax `{RegName, Node} ! Msg` sends the message `Msg` to the registered process `RegName` on the node `Node`.

# Relationships

## Builds Upon
- **Node** — the BIFs operate on nodes.

## Enables
- **Remote spawning** — `spawn(Node, ...)` is the core remote-spawn primitive.

## Related
- **rpc module** — a higher-level library written using these BIFs.
- **Magic cookie** — `erlang:set_cookie/2` belongs to the same distribution surface.

## Contrasts With
- A foundational primitive set; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Using `spawn(Node, Fun)` between nodes running different module versions.
  **Correction**: Prefer `spawn(Node, Mod, Func, Args)`, which is more robust to version mismatches.
- **Error**: Calling distribution BIFs on an undistributed node and not handling `nonode@nohost`.
  **Correction**: Check `is_alive()` first; `node()` returns `nonode@nohost` when undistributed.

# Common Confusions

- **Confusion**: `nodes()` includes the local node.
  **Clarification**: `nodes()` returns all *other* connected nodes, not the local one.
- **Confusion**: `monitor_node` is the same as monitoring a process.
  **Clarification**: `monitor_node` watches a *node* and delivers `{nodeup,...}`/`{nodedown,...}`; process monitors deliver `'DOWN'` messages.

# Source Reference

Chapter 14: Distributed Programming, section "Libraries and BIFS for Distributed Programming" (the `spawn/2,4`, `spawn_link/2,4`, `disconnect_node/1`, `monitor_node/2`, `node/0,1`, `nodes/0`, `is_alive/0` BIFs and the `{RegName, Node} ! Msg` syntax).

# Verification Notes

- Definition source: Direct adaptation of the BIF list in "Libraries and BIFS for Distributed Programming."
- Confidence rationale: HIGH — each BIF is explicitly specified with its signature and behavior.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `node`/`distributed-erlang` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
