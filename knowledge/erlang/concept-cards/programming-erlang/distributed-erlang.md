---
# === CORE IDENTIFICATION ===
concept: Distributed Erlang
slug: distributed-erlang

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
  - "distributed programming"
  - "Erlang cluster"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - spawn
extends: []
related:
  - node
  - magic-cookie
  - remote-spawning
  - distribution-bifs
  - rpc-module
contrasts_with:
  - socket-based-distribution

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a distributed Erlang program?"
  - "How does a node relate to distributed Erlang?"
  - "What must I understand before distributed programming?"
---

# Quick Definition

Distributed Erlang is the model in which programs run on a set of trusted Erlang nodes, and all the usual primitives — `spawn`, `send`, `receive`, `link` — work transparently over the network just as on a single node.

# Core Definition

Distributed programs are programs designed to run on networks of computers that coordinate their activities only by message passing (Chapter 14, introduction). In *distributed Erlang*, programs are written to run on Erlang *nodes*; you can spawn a process on any node, and all the message-passing and error-handling primitives discussed in earlier chapters work as in the single-node case (Chapter 14, "Two Models for Distribution"). Distributed Erlang applications run in a *trusted* environment: since any node can perform any operation on any other Erlang node, a high degree of trust is involved. Such applications are typically run on clusters on the same LAN behind a firewall, though they can run on an open network. The reasons for writing distributed applications are performance, reliability (fault tolerance across machines), scalability, intrinsic distribution, and fun.

# Prerequisites

- **Process** — Distributed Erlang spawns and coordinates processes.
- **Message passing** — Distributed processes coordinate only by exchanging messages.
- **Spawn** — Writing a distributed program is largely a matter of spawning processes on the right nodes.

# Key Properties

1. Programs run on a set of Erlang nodes.
2. `spawn`, `send`, `receive`, and `link` work transparently across the network.
3. The environment is *trusted* — any node can do anything to any other node.
4. Typically deployed on a LAN behind a firewall.
5. Distribution is motivated by performance, reliability, scalability, intrinsic distribution, and fun.

# Construction / Recognition

## To Write a Distributed Erlang Program:
1. Write and test the program in a regular nondistributed Erlang session.
2. Test it on two Erlang nodes on the same computer.
3. Test it on two nodes on physically separated computers on the same LAN.
4. Test it on two machines in different domains, configuring firewalls and security.

## To Recognize It:
1. Look for `spawn(Node, ...)` and `rpc:call(Node, ...)` calls.
2. Look for node names of the form `Name@Host` and `-sname`/`-name` startup flags.

# Context & Application

- **Typical contexts**: Clusters of trusted machines controlled from a single point.
- **Common applications**: Distributed name servers; file transfer between nodes; parallel computation.
- **Historical/stylistic notes**: The book recommends developing distributed programs in stages, starting nondistributed and adding nodes incrementally.

# Examples

**Example 1** (Chapter 14, "Building the Name Server"): The `kvs` key-value server is first run locally, then with a client on node `bilbo` and server on node `gandalf` — `rpc:call(gandalf@localhost, kvs, store, [weather, fine])` performs the first distributed computation.

**Example 2** (Chapter 14, "The File Server Revisited"): A file server is built with no new code — `dist_demo:rpc(Pid, file, get_cwd, [])` reuses the standard `file` module remotely over a distributed connection.

# Relationships

## Builds Upon
- **Process** and **message passing** — distributed Erlang is concurrent Erlang spread over nodes.

## Enables
- **Remote spawning** — spawning processes on other nodes.
- **Distribution BIFs** — the node-related primitives.

## Related
- **Node** — the unit a distributed program runs on.
- **Magic cookie** — the authentication mechanism connecting nodes.
- **rpc module** — the standard library for remote procedure calls.

## Contrasts With
- **Socket-based distribution** — runs in an *untrusted* environment with a less powerful but more secure model.

# Common Errors

- **Error**: Running distributed Erlang on the open Internet without securing connections.
  **Correction**: Restrict it to trusted LANs behind firewalls, or set up secure channels first.
- **Error**: Skipping the staged development process and testing directly across domains.
  **Correction**: Develop in stages — local, two local nodes, LAN, then cross-domain.

# Common Confusions

- **Confusion**: Distributed Erlang is secure against malicious nodes.
  **Clarification**: It is a *trusted* model — any node can do anything to any other; use socket-based distribution for untrusted environments.
- **Confusion**: Distributed programming requires fundamentally different primitives.
  **Clarification**: `spawn`, `send`, `receive`, and `link` work transparently across nodes; only where processes run changes.

# Source Reference

Chapter 14: Distributed Programming, introduction, sections "Two Models for Distribution," "Writing a Distributed Program," and "Building the Name Server."

# Verification Notes

- Definition source: Direct adaptation of the "Two Models for Distribution" section and chapter introduction.
- Confidence rationale: HIGH — distributed Erlang is explicitly defined and contrasted with socket-based distribution.
- Uncertainties: None.
- Cross-reference status: This is the canonical `distributed-erlang` card. Other slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
