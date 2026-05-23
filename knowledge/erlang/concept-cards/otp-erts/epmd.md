---
# === CORE IDENTIFICATION ===
concept: EPMD (Erlang Port Mapper Daemon)
slug: epmd

# === CLASSIFICATION ===
category: distribution
subcategory: registries
tier: intermediate

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "epmd"
chapter_number: null
pdf_page: null
section: "Description"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang Port Mapper Daemon"
  - "port mapper"
  - "epmd daemon"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - epmd-protocol
  - distribution-protocol
  - alternative-node-discovery
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is EPMD (Erlang Port Mapper Daemon)?"
  - "How does EPMD relate to the distribution protocol?"
  - "What role does EPMD play in Erlang distribution?"
---

# Quick Definition

EPMD (Erlang Port Mapper Daemon) is a name server that runs on every host involved in distributed Erlang. It maps symbolic node names to the TCP port numbers where those nodes accept distribution connections. EPMD listens on port 4369 by default and is started automatically when a distributed Erlang node starts.

# Core Definition

The ERTS documentation states: "This daemon acts as a name server on all hosts involved in distributed Erlang computations. When an Erlang node starts, the node has a name and it obtains an address from the host OS kernel. The name and address are sent to the `epmd` daemon running on the local host." In a TCP/IP environment, the address consists of an IP address and port number. "The job of the `epmd` daemon is to keep track of which node name listens on which address. Hence, `epmd` maps symbolic node names to machine addresses."

EPMD only tracks the `Name` part (before `@`) of a node name. The `Host` part is implicit in where EPMD was contacted. Consistent and correct TCP naming services are required for Erlang distribution to function correctly.

# Prerequisites

None -- EPMD is a foundational service for Erlang distribution.

# Key Properties

1. Listens on TCP port 4369 by default (configurable via `-port` or `ERL_EPMD_PORT`)
2. Runs on every host with distributed Erlang nodes
3. Started automatically by `erl` when starting a distributed node (if not already running)
4. Can be started manually with `epmd -daemon` for boot-time initialization
5. Only tracks the `Name` portion of `Name@Host` -- the host is implicit
6. A node unregisters by closing its TCP connection to EPMD
7. On Windows, limited to 60 nodes per EPMD instance
8. Can be restricted to specific IP addresses via `-address` or `ERL_EPMD_ADDRESS`
9. Accepts queries from remote hosts but only allows registration from local processes
10. Remote hosts can query ports and names but cannot register or perform administrative operations

# Construction / Recognition

## To Construct/Create:
1. Automatic: start a distributed node with `erl -sname foo` or `erl -name foo@host`
2. Manual: run `epmd -daemon` to start EPMD as a background process
3. Use `-port No` to run on a non-default port

## To Identify/Recognize:
1. Process named `epmd` listening on port 4369
2. Query with `epmd -names` to list registered nodes
3. Check with `epmd -port No -names` for non-default ports

# Context & Application

EPMD is the default node discovery mechanism for Erlang distribution. Without it (or a replacement), nodes cannot find each other's distribution ports. In production, EPMD is typically started at system boot and runs continuously. For systems that do not use the standard discovery mechanism, EPMD can be replaced with a custom EPMD module (using `-epmd_module`) and disabled with `-no_epmd`.

# Examples

**Example 1** (epmd command, Description): Starting EPMD and querying it:
```bash
# Start EPMD as a daemon
$ epmd -daemon

# List registered nodes
$ epmd -names
epmd: up and running on port 4369 with data:
name foo at port 45321
name bar at port 45322

# Kill EPMD (only if no nodes registered, or -relaxed_command_check)
$ epmd -kill
```

**Example 2** (epmd command, Regular Options): Restricting EPMD to specific addresses:
```bash
# Listen only on specific interfaces
$ epmd -daemon -address 192.168.1.10,10.0.0.5

# Or via environment variable
$ ERL_EPMD_ADDRESS=192.168.1.10,10.0.0.5 epmd -daemon
```

**Example 3** (epmd command, Environment Variables): Running multiple independent clusters on one host:
```bash
# Cluster A uses port 4369 (default)
$ ERL_EPMD_PORT=4369 erl -sname nodeA

# Cluster B uses port 4370
$ ERL_EPMD_PORT=4370 erl -sname nodeB
```
All nodes in a cluster must use the same EPMD port number.

# Relationships

## Builds Upon
None

## Related
- **epmd-protocol** -- The wire protocol used to communicate with EPMD
- **distribution-protocol** -- EPMD enables the node discovery phase of the distribution protocol
- **alternative-node-discovery** -- Custom EPMD modules can replace the standard daemon

## Contrasts With
None

# Common Errors

- **Error**: Forgetting that EPMD must run on every host, not just one central server
  **Correction**: Each host with distributed Erlang nodes must have its own EPMD instance. There is no centralized EPMD.

- **Error**: Trying to register a node from a remote host
  **Correction**: EPMD only accepts registration from local processes. Remote registration attempts are treated as hostile and the connection is closed immediately.

- **Error**: Running `epmd -kill` when nodes are registered without `-relaxed_command_check`
  **Correction**: By default, EPMD refuses to be killed when it has registered nodes. Start EPMD with `-relaxed_command_check` if you need this capability.

# Common Confusions

- **Confusion**: Thinking EPMD stores the full `Name@Host` node name
  **Clarification**: EPMD only stores the `Name` part (before `@`). The `Host` part is implicit in which EPMD was contacted.

- **Confusion**: Thinking EPMD is required for all Erlang distribution
  **Clarification**: EPMD is the default discovery mechanism but can be replaced entirely using `-epmd_module` and `-no_epmd`. The distribution protocol itself does not require EPMD.

- **Confusion**: Thinking EPMD participates in message routing
  **Clarification**: EPMD is only used for initial discovery (name-to-port mapping). Once nodes connect, EPMD plays no further role in their communication.

# Source Reference

"epmd" chapter, sections "Description", "Regular Options", "Interactive Options", "Environment Variables", and "Access Restrictions".

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with comprehensive command reference
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
