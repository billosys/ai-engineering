---
# === CORE IDENTIFICATION ===
concept: Distribution Connection
slug: distribution-connection

# === CLASSIFICATION ===
category: distribution
subcategory: protocol
tier: advanced

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Distribution Protocol"
chapter_number: null
pdf_page: null
section: "Protocol between Connected Nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "connected nodes protocol"
  - "distribution channel"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distribution-protocol
  - distribution-handshake
  - external-term-format
  - distribution-header
extends:
  - distribution-protocol
related:
  - alternative-distribution-carrier
  - distribution-controller-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do connected Erlang nodes exchange messages?"
  - "What are distribution control messages?"
  - "What is the message format between connected nodes?"
---

# Quick Definition

Once the distribution handshake succeeds, connected nodes exchange messages using a framing format of a 4-byte length, a distribution header (with atom cache), a control message tuple, and an optional payload message -- all encoded in external term format. Control messages encode distributed operations like send, link, monitor, exit, and spawn.

# Core Definition

The ERTS documentation describes the format of messages passed between connected nodes (since ERTS 5.7.2 / OTP R13B) as:

| 4 bytes | d bytes | n bytes | m bytes |
|---------|---------|---------|---------|
| Length  | DistributionHeader | ControlMessage | Message |

Where `Length` = d + n + m. The distribution header manages the atom cache and fragmentation. The `ControlMessage` is a tuple encoded in external term format (version byte omitted). The `Message` is the actual payload, present only for send-type operations.

Control messages are tuples whose first element identifies the operation. The protocol defines operations including: `LINK` (1), `SEND` (2), `EXIT` (3), `REG_SEND` (6), `GROUP_LEADER` (7), `EXIT2` (8), `MONITOR_P` (19), `DEMONITOR_P` (20), `MONITOR_P_EXIT` (21), plus newer variants with trace tokens, sender information, payload separation, spawn requests, unlink IDs, and alias/priority signals.

# Prerequisites

- **distribution-protocol** -- The connection phase is phase 4 of the distribution protocol
- **distribution-handshake** -- The handshake must succeed before connected operation begins
- **external-term-format** -- Control messages and payloads use external term format encoding
- **distribution-header** -- Every message is preceded by a distribution header

# Key Properties

1. Messages use 4-byte big-endian length headers (contrasted with 2-byte during handshake)
2. Every message includes a distribution header before the control message
3. The version number (131) is omitted from terms following a distribution header
4. Control messages are tuples; the first element is an integer operation tag
5. `SEND_SENDER` (22) replaces `SEND` (2) when `DFLAG_SEND_SENDER` is negotiated
6. `PAYLOAD_*` variants (24-28) separate the exit reason into the message part for better caching
7. `SPAWN_REQUEST` (29) and `SPAWN_REPLY` (31) enable distributed spawning (OTP 23+)
8. `UNLINK_ID` (35) and `UNLINK_ID_ACK` (36) implement the reliable link protocol (mandatory from OTP 26)
9. `ALTACT_SIG_SEND` (37) handles alias, priority, and exit signals (OTP 28+)
10. Data must be delivered in exact order with no loss; ordering can be relaxed by rejecting strict-order flags

# Construction / Recognition

## To Construct/Create:
1. After a successful handshake, the distribution controller process or port handles message dispatch
2. Use `erlang:dist_ctrl_get_data/1` to get outgoing data to send
3. Use `erlang:dist_ctrl_put_data/2` to inject received data
4. The runtime system handles encoding control messages and payloads

## To Identify/Recognize:
1. Post-handshake traffic on a distribution connection
2. 4-byte length-prefixed messages containing distribution headers
3. Control message tuples with integer tags as the first element

# Context & Application

The connected-nodes protocol is where all distributed Erlang operations happen: message passing, link/unlink, monitor/demonitor, exit signals, and distributed spawning. Each operation is encoded as a specific control message type. Understanding this protocol is essential for implementing distribution carriers, analyzing distribution traffic, and comprehending how distributed Erlang guarantees (like link reliability) are implemented at the wire level.

# Examples

**Example 1** (Protocol between Connected Nodes): Sending a message to a registered process:
```erlang
%% This generates a REG_SEND control message:
%% {6, FromPid, Unused, ToName}
%% followed by the Message payload
{reg_server, 'bar@host'} ! {request, self(), data}.
```

**Example 2** (Protocol between Connected Nodes): The link protocol using UNLINK_ID (OTP 26+):
```
%% To set up a link:
LINK: {1, FromPid, ToPid}

%% To remove a link (new protocol):
UNLINK_ID: {35, Id, FromPid, ToPid}

%% Acknowledgement (must be sent before any other signals to sender):
UNLINK_ID_ACK: {36, Id, FromPid, ToPid}
```

# Relationships

## Builds Upon
- **distribution-protocol** -- This is the final phase of the distribution protocol
- **distribution-handshake** -- Must complete successfully before connected operation
- **external-term-format** -- All terms are encoded in external term format
- **distribution-header** -- Every message is preceded by a distribution header

## Related
- **alternative-distribution-carrier** -- Custom carriers must deliver these messages reliably and in order
- **distribution-controller-process** -- The process (or port) responsible for dispatching this traffic

## Contrasts With
None

# Common Errors

- **Error**: Delivering messages out of order on a distribution channel
  **Correction**: By default, data must be delivered in exact order with no loss. Ordering can only be relaxed by rejecting strict-order flags (`dist_util:strict_order_flags/0`), which limits ordering to same sender/receiver pairs.

- **Error**: Using the old `UNLINK` (4) signal on OTP 26+ nodes
  **Correction**: The `UNLINK` signal is obsolete from OTP 26. Use `UNLINK_ID` (35) and `UNLINK_ID_ACK` (36) instead.

# Common Confusions

- **Confusion**: Thinking `SEND` and `SEND_SENDER` are interchangeable
  **Clarification**: Once a `SEND_SENDER` (22) or `SEND_SENDER_TT` (23) has been sent on a connection, no more `SEND` (2) or `SEND_TT` (12) messages may be sent in the same direction. The transition is one-way.

- **Confusion**: Thinking `PAYLOAD_*` variants change message semantics
  **Clarification**: The `PAYLOAD_*` control messages (e.g., `PAYLOAD_EXIT`) have the same semantics as their non-PAYLOAD counterparts. The difference is structural: the reason/message is moved from the control tuple to the separate message part, enabling better atom cache utilization.

# Source Reference

"Distribution Protocol" chapter, section "Protocol between Connected Nodes" and all "New Ctrlmessages" subsections through OTP 28, plus the "Link Protocol" subsection.

# Verification Notes

- Definition source: Direct from source text with control message tables
- Confidence rationale: HIGH -- explicitly defined with complete message type catalog
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
