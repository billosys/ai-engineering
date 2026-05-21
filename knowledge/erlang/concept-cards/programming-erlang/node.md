---
# === CORE IDENTIFICATION ===
concept: Node
slug: node

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-models
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "Two Models for Distribution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang node"
  - "Name@Host"
  - "short name"
  - "long name"
  - "nonode@nohost"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - distributed-erlang
  - magic-cookie
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang node?"
  - "How do I start an Erlang node?"
  - "What is the difference between short and long node names?"
---

# Quick Definition

A node is a self-contained Erlang system — a complete virtual machine with its own address space and its own set of processes — identified by a name of the form `Name@Host`.

# Core Definition

A *node* is a self-contained Erlang system containing a complete virtual machine with its own address space and its own set of processes (Chapter 14, "Two Models for Distribution"). A node is started with a name using the `erl` command-line flags `-sname` (short name) or `-name` (long, fully qualified name); the node name has the form `Name@Host`, where `Name` and `Host` are both atoms (and must be quoted if they contain nonatomic characters). Short names (`-sname`) are used for nodes on the same machine or the same subnet and are the only option when no DNS service is available; long names (`-name`) are used for nodes on different networks. The BIF `node()` returns the name of the local node, returning `nonode@nohost` if the node is not distributed; `is_alive()` returns `true` if the local node is alive and can be part of a distributed system.

# Prerequisites

- **Process** — A node contains and runs processes; it is the home of a process set.

# Key Properties

1. A node is a complete Erlang virtual machine with its own address space and processes.
2. Node names have the form `Name@Host`, both parts atoms.
3. `-sname` starts a node with a short name; `-name` starts one with a long, fully qualified name.
4. Short names work on the same machine/subnet and without DNS; long names work across networks.
5. `node()` returns the local node name, or `nonode@nohost` if not distributed.
6. Multiple nodes can run on one host or be spread across machines.

# Construction / Recognition

## To Start a Node:
1. Run `erl -sname Name` for a short-named node on the local host.
2. Run `erl -name Name -setcookie C` for a long-named node, with a magic cookie.
3. The shell prompt then prints the node name, e.g. `(gandalf@localhost) 1>`.

## To Recognize It:
1. Look for `Name@Host` atoms in shell prompts and code.
2. Look for `node()`, `nodes()`, and `-sname`/`-name` flags.

# Context & Application

- **Typical contexts**: Distributed Erlang systems; clusters of cooperating VMs.
- **Common applications**: Running client and server on separate nodes; spawning processes on remote nodes.
- **Historical/stylistic notes**: On many systems `-sname gandalf` produces `gandalf@H` where `H` is the local hostname, not `gandalf@localhost`.

# Examples

**Example 1** (Chapter 14, "Stage 2"): `$ erl -sname gandalf` starts a node named `gandalf` on the local host; the shell prompt becomes `(gandalf@localhost) 1>`.

**Example 2** (Chapter 14, "Stage 3"): `doris $ erl -name gandalf -setcookie abc` starts a long-named node `gandalf@doris.myerl.example.com` for cross-machine distribution.

# Relationships

## Builds Upon
- **Process** — a node is the container for a set of processes.

## Enables
- **Distributed Erlang** — distributed programs run on sets of nodes.
- **Remote spawning** — processes can be spawned on a named node.

## Related
- **Magic cookie** — nodes must share a cookie to communicate.
- **Distribution BIFs** — `node/0`, `nodes/0`, `is_alive/0` operate on nodes.

## Contrasts With
- This is a foundational distribution concept; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Using `localhost` in examples when `-sname` actually produced `Name@H` with a real hostname.
  **Correction**: Use the hostname `H` shown in your shell prompt.
- **Error**: Using `-sname` for nodes on different networks where DNS-resolvable long names are needed.
  **Correction**: Use `-name` with fully qualified hostnames across networks.

# Common Confusions

- **Confusion**: A node is the same as a physical machine.
  **Clarification**: A node is an Erlang VM; multiple nodes can run on one machine.
- **Confusion**: Short and long names are interchangeable.
  **Clarification**: `-sname` and `-name` nodes cannot freely interconnect; choose consistently based on network topology and DNS availability.

# Source Reference

Chapter 14: Distributed Programming, section "Two Models for Distribution" (the "node" definition), "Building the Name Server" (Stages 2 and 3, `-sname`/`-name` usage), and "Libraries and BIFS for Distributed Programming" (the `node/0` and `is_alive/0` BIFs).

# Verification Notes

- Definition source: Direct adaptation of the node definition and the `-sname`/`-name` discussion.
- Confidence rationale: HIGH — a node is explicitly defined and its naming explained.
- Uncertainties: None.
- Cross-reference status: This is the canonical `node` card. Other slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
