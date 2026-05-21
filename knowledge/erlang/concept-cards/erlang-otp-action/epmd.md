---
# === CORE IDENTIFICATION ===
concept: Erlang Port Mapper Daemon (EPMD)
slug: epmd

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2.3 How Erlang nodes find each other and communicate"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "EPMD"
  - "Erlang Port Mapper Daemon"
  - "epmd"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - connecting-nodes
  - erlang-cluster
  - magic-cookie
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is EPMD?"
  - "How do Erlang nodes on different machines find each other?"
  - "What port does EPMD use?"
---

# Quick Definition

EPMD (the Erlang Port Mapper Daemon) is a per-machine daemon that tracks which Erlang nodes run locally and on which ports, so that a remote node can look up and connect to a node by name.

# Core Definition

EPMD, the Erlang Port Mapper Daemon, is a daemon process that runs on each machine hosting Erlang nodes. Whenever a node starts, it checks that EPMD is running on its local machine and starts it otherwise. EPMD keeps track of which nodes are running on the local machine and which ports they have been assigned. When an Erlang node on one machine wants to talk to a remote node, the local EPMD contacts the EPMD on the remote machine (by default over TCP/IP on port 4369) and asks whether a node by that name is running; if so, the remote EPMD replies with the port for communicating directly with that remote node. EPMDs never try to locate each other automatically — communication must always be triggered by one node looking for another (Ch. 8, Section 8.2.3).

# Prerequisites

- **erlang-node** — EPMD's purpose is to track and locate nodes.

# Key Properties

1. One EPMD per machine; started automatically by the first node.
2. Tracks the names and assigned ports of local nodes.
3. A local EPMD contacts a remote EPMD to resolve a remote node's port.
4. Uses TCP/IP on port 4369 by default.
5. EPMDs never locate each other automatically — lookup is triggered by node connection attempts.

# Construction / Recognition

## How It Works:
1. A starting node ensures EPMD is running locally, starting it if needed.
2. The node registers its name and port with EPMD.
3. To reach a remote node, the local EPMD queries the remote EPMD on port 4369.
4. The remote EPMD returns the port for direct node-to-node communication.

## To Recognize:
1. On a UNIX-like OS, `ps ax | grep -i epmd` shows the `epmd -daemon` process.

# Context & Application

- **Typical contexts**: Underpins all node connection in distributed Erlang.
- **Common applications**: Name resolution behind `net_adm:ping/1` and cluster formation.
- **Historical/stylistic notes**: Firewalls blocking port 4369 are a common cause of nodes failing to connect across machines.

# Examples

**Example 1** (Section 8.2.3): `ps ax | grep -i epmd` shows a process line like `/usr/local/lib/erlang/erts-5.6.2/bin/epmd -daemon`.

**Example 2** (Section 8.2.3): When a node wants a remote node, its local EPMD asks the remote EPMD over TCP port 4369 and receives the remote node's communication port in reply.

# Relationships

## Builds Upon
- **erlang-node** — EPMD exists to track and locate nodes.

## Enables
- **connecting-nodes** — Node connection relies on EPMD for name-to-port resolution.

## Related
- **erlang-cluster** — EPMD underpins cluster formation.
- **magic-cookie** — Cookies authorize the connection EPMD helps establish.

## Contrasts With
- None.

# Common Errors

- **Error**: Firewall rules blocking TCP port 4369 between machines.
  **Correction**: Allow port 4369 (and the node's assigned port) so EPMDs and nodes can communicate.

# Common Confusions

- **Confusion**: Thinking EPMDs broadcast to discover each other.
  **Clarification**: EPMDs never locate each other automatically; a node connection attempt triggers the lookup.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.3 "How Erlang nodes find each other and communicate."

# Verification Notes

- Definition source: Directly adapted from Section 8.2.3.
- Confidence rationale: HIGH — the book explicitly defines EPMD and its protocol.
- Uncertainties: None.
- Cross-reference status: Verified.
