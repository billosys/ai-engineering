---
# === CORE IDENTIFICATION ===
concept: Distributed Erlang System
slug: distributed-erlang-system

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "Distributed Erlang System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - distributed system
  - Erlang cluster

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - erlang-node
  - node-connections
  - distributed-security
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distributed Erlang system?"
  - "How do Erlang runtime systems communicate with each other?"
  - "Are message passing and links transparent across nodes?"
---

# Quick Definition
A distributed Erlang system consists of multiple Erlang runtime systems (nodes) communicating with each other over TCP/IP. Message passing, links, and monitors are transparent when using pids, but registered names are local to each node.

# Core Definition
The Erlang Reference Manual states: "A _distributed Erlang system_ consists of a number of Erlang runtime systems communicating with each other. Each such runtime system is called a _node_. Message passing between processes at different nodes, as well as links and monitors, are transparent when pids are used. Registered names, however, are local to each node. This means that the node must be specified as well when sending messages, and so on, using registered names." The manual also states: "The distribution mechanism is implemented using TCP/IP sockets." (Distributed Erlang chapter, "Distributed Erlang System" section).

# Prerequisites
- **erlang-process** -- Distribution extends the process communication model across nodes

# Key Properties
1. Consists of multiple Erlang runtime systems (nodes) communicating over a network
2. Implemented using TCP/IP sockets by default
3. Message passing is transparent when using pids -- `Pid ! Message` works across nodes
4. Links and monitors work transparently across nodes when using pids
5. Registered names are local to each node -- must specify `{Name, Node}` for remote registered names
6. An alternative carrier mechanism can be implemented (documented in ERTS User's Guide)
7. Security warning: starting a distributed node without TLS exposes it to attacks granting full access

# Construction / Recognition
## To Construct/Create:
1. Start each Erlang runtime system with `-name` or `-sname` flag to make it a node
2. Ensure nodes share the same magic cookie (or configure per-node cookies)
3. Nodes connect automatically when another node's name is first used
4. Or connect explicitly using `net_adm:ping(Node)` or `net_kernel:connect_node(Node)`

## To Identify/Recognize:
1. `is_alive/0` returns `true` if the runtime system is a node
2. `nodes/0` returns the list of connected visible nodes
3. `node/0` returns the name of the current node

# Context & Application
Distributed Erlang is one of the language's defining features. It extends the actor model across machine boundaries, enabling fault-tolerant systems that span multiple physical or virtual machines. The transparency of message passing means that code written for a single node often works in a distributed setting with minimal changes.

**Typical contexts:**
- Building fault-tolerant systems with redundancy across machines
- Scaling systems horizontally by distributing work across nodes
- Hot code upgrades with rolling restarts across a cluster
- OTP applications with distributed supervisors and global name registration

# Examples
**Example 1** (Distributed Erlang, "Distributed Erlang System" section): The transparency of distribution: "Message passing between processes at different nodes, as well as links and monitors, are transparent when pids are used."

**Example 2** (Distributed Erlang, "Distributed Erlang System" section): The limitation of registered names: "Registered names, however, are local to each node. This means that the node must be specified as well when sending messages, and so on, using registered names."

# Relationships
## Builds Upon
- **erlang-process** -- Distribution extends process communication across nodes

## Enables
- **erlang-node** -- Nodes are the building blocks of a distributed system
- **node-connections** -- Nodes must connect to form a distributed system
- **distributed-security** -- Security is needed to protect distributed systems

## Related
- **distribution-bifs** -- BIFs for working with distributed systems

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Starting distributed nodes without TLS and assuming the system is secure
  **Correction**: The source explicitly warns: "Starting a distributed node without also specifying `-proto_dist inet_tls` will expose the node to attacks that may give the attacker complete access to the node and by extension the cluster."

# Common Confusions
- **Confusion**: Thinking registered names work across nodes without qualification
  **Clarification**: Registered names are local to each node. To send to a registered name on another node, use `{Name, Node} ! Message` syntax.

# Source Reference
Distributed Erlang chapter, "Distributed Erlang System" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definition in opening paragraph
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
