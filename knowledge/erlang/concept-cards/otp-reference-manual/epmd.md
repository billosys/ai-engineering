---
# === CORE IDENTIFICATION ===
concept: EPMD
slug: epmd

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
section: "epmd"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erlang Port Mapper Daemon

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-connections
extends: []
related:
  - node-naming
  - distribution-command-line-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is EPMD?"
  - "How do Erlang nodes find each other on a host?"
  - "Is EPMD started manually or automatically?"
---

# Quick Definition
EPMD (Erlang Port Mapper Daemon) is a service that runs on every host where Erlang nodes are started. It maps symbolic node names to machine addresses (TCP port numbers), enabling nodes to find and connect to each other.

# Core Definition
The Erlang Reference Manual states: "The Erlang Port Mapper Daemon _epmd_ is automatically started at every host where an Erlang node is started. It is responsible for mapping the symbolic node names to machine addresses." (Distributed Erlang chapter, "epmd" section).

# Prerequisites
- **erlang-node** -- EPMD serves named nodes
- **node-connections** -- EPMD enables nodes to find each other for connection

# Key Properties
1. Automatically started on every host where an Erlang node is started
2. Maps symbolic node names to machine addresses (TCP ports)
3. One EPMD instance per host, shared by all Erlang nodes on that host
4. Runs as a background daemon process
5. Listens on port 4369 by default
6. Nodes register with EPMD when they start
7. Connecting nodes query EPMD on the remote host to find the target node's port

# Construction / Recognition
## To Construct/Create:
1. EPMD starts automatically when the first Erlang node starts on a host
2. Can be started manually with the `epmd` command

## To Identify/Recognize:
1. The `epmd` process is visible in the OS process list
2. `epmd -names` lists all registered node names on a host

# Context & Application
EPMD is a critical infrastructure component for distributed Erlang. When node A wants to connect to node B on host H, A contacts EPMD on host H to look up the TCP port where B is listening. Without EPMD, nodes cannot discover each other's listening ports.

**Typical contexts:**
- Automatically present in any distributed Erlang deployment
- Managed by systemd or similar service managers in production
- Queried for debugging distributed connectivity issues

# Examples
**Example 1** (Distributed Erlang, "epmd" section): "The Erlang Port Mapper Daemon _epmd_ is automatically started at every host where an Erlang node is started. It is responsible for mapping the symbolic node names to machine addresses."

# Relationships
## Builds Upon
- **erlang-node** -- EPMD maps node names to addresses
- **node-connections** -- EPMD enables connection establishment

## Enables
Nothing directly -- EPMD is infrastructure.

## Related
- **node-naming** -- EPMD maps the node name to a port
- **distribution-command-line-flags** -- EPMD port can be configured via flags

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Running a firewall that blocks EPMD's port (4369) and wondering why nodes cannot connect
  **Correction**: Ensure port 4369 (or the configured EPMD port) is open between hosts that need to form a cluster.

# Common Confusions
- **Confusion**: Thinking each node runs its own EPMD
  **Clarification**: One EPMD instance runs per host, shared by all Erlang nodes on that host. Multiple nodes on the same host all register with the same EPMD.

# Source Reference
Distributed Erlang chapter, "epmd" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- concise, explicit definition
- Uncertainties: None -- the section is brief but complete for the reference manual
- Cross-reference status: All referenced slugs correspond to planned cards
