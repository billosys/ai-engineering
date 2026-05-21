---
# === CORE IDENTIFICATION ===
concept: Hidden Nodes
slug: hidden-nodes

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
section: "Hidden Nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - hidden node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-connections
extends:
  - erlang-node
related:
  - transitive-connections
  - c-nodes
  - distribution-command-line-flags
contrasts_with:
  - transitive-connections

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a hidden node in Erlang?"
  - "How do you start a hidden node?"
  - "Why would you use a hidden node?"
  - "How does a hidden node differ from a regular node?"
---

# Quick Definition
A hidden node is an Erlang node started with the `-hidden` flag. Connections to hidden nodes are not transitive, hidden nodes do not appear in `nodes/0`, and they are not tracked by the `global` module. Hidden nodes are used for operations and maintenance tasks that should not disturb the cluster.

# Core Definition
The Erlang Reference Manual states: "In a distributed Erlang system, it is sometimes useful to connect to a node without also connecting to all other nodes. An example is some kind of Operation and Maintenance functionality used to inspect the status of a system, without disturbing it. For this purpose, a _hidden node_ can be used." The manual further states: "A hidden node is a node started with the command-line flag `-hidden`. Connections between hidden nodes and other nodes are not transitive; they must be set up explicitly. Also, hidden nodes do not show up in the list of nodes returned by `nodes/0`. Instead, `nodes(hidden)` or `nodes(connected)` must be used. This means, for example, that the hidden node is not added to the set of nodes that `global` is keeping track of." (Distributed Erlang chapter, "Hidden Nodes" section).

# Prerequisites
- **erlang-node** -- Hidden nodes are a special type of node
- **node-connections** -- Must understand normal connection behavior to understand how hidden nodes differ

# Key Properties
1. Started with the `-hidden` command-line flag
2. Connections to/from hidden nodes are not transitive -- must be set up explicitly
3. Not listed in `nodes/0` -- use `nodes(hidden)` or `nodes(connected)` instead
4. Not tracked by the `global` module
5. Can connect to regular nodes without triggering transitive connections to other nodes
6. Ideal for monitoring, debugging, and operations tasks
7. Multiple hidden nodes can connect to the same cluster independently

# Construction / Recognition
## To Construct/Create:
1. Start the node with `-hidden` flag: `erl -sname monitor -hidden`
2. Explicitly connect to target nodes: `net_adm:ping(TargetNode)`

## To Identify/Recognize:
1. Hidden nodes do not appear in `nodes/0`
2. Use `nodes(hidden)` to list hidden nodes
3. Use `nodes(connected)` to list all connected nodes (visible + hidden)

# Context & Application
Hidden nodes provide a way to connect to a running cluster for inspection or maintenance without affecting the cluster's topology or global state. This is essential for production operations where connecting a debugging tool should not cause side effects.

**Typical contexts:**
- Remote debugging shells connecting to production clusters
- Monitoring and metrics collection nodes
- Operation and maintenance tools
- C nodes (which are always hidden)

# Examples
**Example 1** (Distributed Erlang, "Hidden Nodes" section): Use case: "An example is some kind of Operation and Maintenance functionality used to inspect the status of a system, without disturbing it."

**Example 2** (Distributed Erlang, "Hidden Nodes" section): Listing hidden nodes: "hidden nodes do not show up in the list of nodes returned by `nodes/0`. Instead, `nodes(hidden)` or `nodes(connected)` must be used."

# Relationships
## Builds Upon
- **erlang-node** -- Hidden nodes are a specialized type of node
- **node-connections** -- Hidden nodes have non-transitive connections

## Enables
Nothing directly.

## Related
- **transitive-connections** -- Hidden nodes bypass transitive connection behavior
- **c-nodes** -- C nodes act as hidden nodes in the distributed system
- **distribution-command-line-flags** -- `-hidden` flag creates hidden nodes

## Contrasts With
- **transitive-connections** -- Regular (visible) nodes participate in transitive connections. Hidden nodes do not.

# Common Errors
- **Error**: Using `nodes/0` to find hidden nodes
  **Correction**: `nodes/0` only returns visible nodes. Use `nodes(hidden)` for hidden nodes or `nodes(connected)` for all connected nodes.

# Common Confusions
- **Confusion**: Thinking hidden nodes cannot be connected to at all
  **Clarification**: Hidden nodes can connect and be connected to -- connections just must be established explicitly rather than transitively.

# Source Reference
Distributed Erlang chapter, "Hidden Nodes" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- complete, self-contained section with explicit definition
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
