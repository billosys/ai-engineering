---
# === CORE IDENTIFICATION ===
concept: Distribution Protocol
slug: distribution-protocol

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang distribution protocol"
  - "dist protocol"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - epmd
  - epmd-protocol
  - distribution-handshake
  - distribution-connection
  - external-term-format
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang distribution protocol?"
  - "How does EPMD relate to the distribution protocol?"
  - "What are the phases of the Erlang distribution protocol?"
---

# Quick Definition

The Erlang distribution protocol is the wire protocol that governs how Erlang nodes discover each other, establish connections, authenticate, and exchange messages. It can be divided into four phases: low-level socket connection, handshake with name exchange and authentication, `net_kernel` authentication, and connected operation.

# Core Definition

The ERTS documentation states that the distribution protocol "can be divided into four parts": (1) Low-level socket connection, (2) Handshake, interchange node name, and authenticate, (3) Authentication (done by `net_kernel`), and (4) Connected. A node fetches the port number of another node through EPMD (at the other host) to initiate a connection request.

Phases 3 and 4 are performed at the same level, but `net_kernel` disconnects the other node if it communicates using an invalid cookie (after 1 second). All multi-byte integer fields in the protocol are in big-endian order.

The protocol is stable and has been so for many years. It is not secure by itself; for secure distribution, nodes should be configured to use distribution over TLS.

# Prerequisites

None -- this is the top-level overview of the distribution protocol.

# Key Properties

1. Four phases: socket connection, handshake, `net_kernel` authentication, connected
2. EPMD is used by default for port lookup (node discovery)
3. EPMD listens on port 4369 by default
4. For each host running a distributed Erlang node, an EPMD instance must also be running
5. All multi-byte integer fields are big-endian
6. The protocol is not secure by itself -- TLS should be used for secure distribution
7. Cookie-based authentication: `net_kernel` disconnects after 1 second if the cookie is invalid
8. The protocol version used by OTP 23+ is version 6; OTP 25+ only supports version 6

# Construction / Recognition

## To Construct/Create:
1. Start a distributed Erlang node (e.g., `erl -sname foo` or `erl -name foo@host`)
2. The node automatically registers with EPMD and begins accepting distribution connections
3. Connecting to another node triggers the full protocol sequence

## To Identify/Recognize:
1. Distribution connections use 2-byte packet headers during the handshake phase, switching to 4-byte headers after connection is established
2. EPMD communication uses 2-byte length-prefixed requests on port 4369

# Context & Application

The distribution protocol is the backbone of Erlang's distributed computing model. Every time `net_kernel:connect_node/1` is called (or implicitly when sending a message to a remote pid or registered name), the protocol is initiated. Understanding its phases is essential when implementing alternative distribution carriers, debugging connectivity issues, or designing secure distributed systems.

# Examples

**Example 1** (Distribution Protocol, introduction): Starting distributed nodes and connecting them:
```erlang
%% On host1:
$ erl -sname foo
(foo@host1)1> net_adm:ping('bar@host2').
pong
```
The `ping` triggers the full protocol: EPMD port lookup, TCP connect, handshake, cookie verification, connected.

**Example 2** (Distribution Protocol, four parts): The four phases illustrated:
```
Phase 1: A opens TCP connection to B's distribution port (obtained from EPMD)
Phase 2: A and B exchange names, capabilities, and challenges (handshake)
Phase 3: net_kernel verifies cookie authentication
Phase 4: Connection is up -- messages flow using distribution headers + external term format
```

# Relationships

## Builds Upon
None

## Related
- **epmd** -- The daemon that enables node discovery for the distribution protocol
- **epmd-protocol** -- The specific request/response protocol between nodes and EPMD
- **distribution-handshake** -- Phase 2 of the distribution protocol in detail
- **distribution-connection** -- Phase 4 of the distribution protocol: message exchange between connected nodes
- **external-term-format** -- The encoding used for terms in distribution messages

## Contrasts With
None

# Common Errors

- **Error**: Assuming the distribution protocol provides security
  **Correction**: The protocol is not secure by itself. Use distribution over TLS (`-proto_dist inet_tls`) for security.

- **Error**: Forgetting that EPMD must be running on each host
  **Correction**: An EPMD instance must run on every host with distributed Erlang nodes. It starts automatically with `erl` but can also be started manually.

# Common Confusions

- **Confusion**: Thinking EPMD is part of the distribution protocol between nodes
  **Clarification**: EPMD has its own separate protocol. It is used for node discovery (port lookup) before the distribution protocol between nodes begins. The distribution protocol itself is the handshake and connected-node communication.

- **Confusion**: Thinking all four phases are distinct sequential stages
  **Clarification**: Phases 3 (authentication) and 4 (connected) operate at the same level. If cookie authentication fails in phase 3, the connection established in phase 4 is torn down after 1 second.

# Source Reference

"Distribution Protocol" chapter, opening paragraphs describing the four-part structure, EPMD role, and security warning.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with clear structure
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
