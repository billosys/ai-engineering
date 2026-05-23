---
# === CORE IDENTIFICATION ===
concept: EPMD Protocol
slug: epmd-protocol

# === CLASSIFICATION ===
category: distribution
subcategory: protocol
tier: intermediate

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Distribution Protocol"
chapter_number: null
pdf_page: null
section: "EPMD Protocol"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "EPMD wire protocol"
  - "port mapper protocol"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - epmd
  - distribution-protocol
extends: []
related:
  - distribution-handshake
  - alternative-node-discovery
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does EPMD relate to the distribution protocol?"
  - "How does a node register with EPMD?"
  - "How does a node look up another node's port via EPMD?"
---

# Quick Definition

The EPMD protocol is the request/response wire protocol used to communicate with the Erlang Port Mapper Daemon. It supports registering nodes, looking up distribution ports, listing registered names, and administrative operations like killing EPMD. All requests are preceded by a 2-byte length field.

# Core Definition

The EPMD protocol defines how distributed Erlang nodes interact with the EPMD daemon. Every request has the format: a 2-byte big-endian length field followed by the request data. The protocol supports the following operations:

1. **Registering a node** (`EPMD_ALIVE2_REQ`, tag 120): A node sends its port number, node type (77 = normal, 72 = hidden/C-node), protocol (0 = TCP/IPv4), highest and lowest supported distribution versions, node name, and optional extra data. EPMD responds with `EPMD_ALIVE2_X_RESP` (tag 118, 32-bit creation) or `EPMD_ALIVE2_RESP` (tag 121, 16-bit creation). The TCP connection to EPMD must remain open as long as the node is distributed; closing it unregisters the node.

2. **Port lookup** (`EPMD_PORT2_REQ`, tag 122): A node queries EPMD for the distribution port of another node by name. EPMD responds with `EPMD_PORT2_RESP` (tag 119) containing the port, node type, protocol, version range, and node name -- or just an error result code. EPMD closes the connection after responding.

3. **Name listing** (`EPMD_NAMES_REQ`, tag 110): Returns the EPMD port number followed by text entries for each registered node.

4. **Dump** (`EPMD_DUMP_REQ`, tag 100): Debug feature returning all data from EPMD.

5. **Kill** (`EPMD_KILL_REQ`, tag 107): Kills EPMD (rarely used; restricted by default).

# Prerequisites

- **epmd** -- Understanding what EPMD is and its role in the system
- **distribution-protocol** -- The EPMD protocol serves the distribution protocol's node discovery phase

# Key Properties

1. All requests are prefixed by a 2-byte big-endian length field
2. Node registration uses `EPMD_ALIVE2_REQ` (tag 120) with response tag 118 (32-bit creation) or 121 (16-bit creation)
3. The registration connection must remain open -- closing it unregisters the node
4. Port lookup uses `EPMD_PORT2_REQ` (tag 122) with response tag 119
5. EPMD closes the connection after a port lookup response
6. The `HighestVersion` and `LowestVersion` fields indicate supported distribution protocol versions (version 6 for OTP 23+, mandatory from OTP 25)
7. `NodeType` distinguishes normal Erlang nodes (77) from hidden/C-nodes (72)
8. The `Creation` value differentiates between successive incarnations of nodes with the same name

# Construction / Recognition

## To Construct/Create:
1. Node registration happens automatically when a distributed node starts
2. Port lookup happens automatically when connecting to another node
3. The `erl_epmd` module in the Kernel application handles all EPMD communication
4. Manual queries: `epmd -names`, `epmd -kill`, `epmd -stop Name`

## To Identify/Recognize:
1. TCP connections to port 4369 (default)
2. Requests begin with a 2-byte length prefix
3. Each request type has a unique tag byte

# Context & Application

The EPMD protocol is the standard node discovery mechanism for Erlang distribution. Every distributed node registers itself with the local EPMD on startup, and every outgoing connection begins with an EPMD port lookup on the target host. Understanding the protocol is important when implementing alternative node discovery, debugging connectivity issues, or designing systems that need to work without EPMD.

# Examples

**Example 1** (EPMD Protocol, Register a Node): When node `foo@host` starts distribution, it sends:
```
EPMD_ALIVE2_REQ:
| 120 | PortNo(2) | NodeType(1) | Protocol(1) | HighVer(2) | LowVer(2) | Nlen(2) | "foo" | Elen(2) | Extra |
```
EPMD responds with:
```
EPMD_ALIVE2_X_RESP:
| 118 | Result(1) | Creation(4) |
```
Result = 0 means success.

**Example 2** (EPMD Protocol, Port lookup): To connect to node `bar@host`, the local node queries `host`'s EPMD:
```
EPMD_PORT2_REQ:
| 122 | "bar" |
```
EPMD responds with the full node information including the distribution port, or an error code if the node is not registered.

# Relationships

## Builds Upon
- **epmd** -- The daemon that implements this protocol
- **distribution-protocol** -- The EPMD protocol enables the node discovery phase of distribution

## Related
- **distribution-handshake** -- After EPMD provides the port, the distribution handshake begins
- **alternative-node-discovery** -- Custom EPMD modules can replace the standard EPMD protocol

## Contrasts With
None

# Common Errors

- **Error**: Closing the TCP connection to EPMD after registration
  **Correction**: The registration connection must be kept open for the lifetime of the distributed node. Closing it automatically unregisters the node.

- **Error**: Assuming EPMD handles authentication
  **Correction**: EPMD only maps node names to ports. Authentication (cookie-based) happens during the distribution handshake, not via EPMD.

# Common Confusions

- **Confusion**: Thinking EPMD communicates with remote nodes
  **Clarification**: EPMD only communicates with local processes and with remote EPMD query clients. It does not participate in the actual distribution connection between nodes.

- **Confusion**: Thinking `Creation` is just a serial number
  **Clarification**: `Creation` distinguishes between successive incarnations of a node with the same name, preventing stale process identifiers from being accepted by a new node instance. It is embedded in every pid, port, and reference created by the node.

# Source Reference

"Distribution Protocol" chapter, section "EPMD Protocol", covering register, unregister, port lookup, names, dump, kill, and stop request formats.

# Verification Notes

- Definition source: Direct from source text with wire format tables
- Confidence rationale: HIGH -- explicitly defined with complete message formats
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
