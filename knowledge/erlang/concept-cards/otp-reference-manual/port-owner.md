---
# === CORE IDENTIFICATION ===
concept: Port Owner
slug: port-owner

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Ports and Port Drivers"
chapter_number: null
pdf_page: null
section: "Ports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - connected process
  - port connected process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-port
extends: []
related:
  - port-message-protocol
  - opening-a-port
  - closing-a-port
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port owner in Erlang?"
  - "What happens to a port when its owner terminates?"
  - "Can the port owner be changed?"
  - "Can any process send messages to a port?"
---

# Quick Definition
The port owner (also called the connected process) is the Erlang process that created a port or has been designated as the port's current owner. All communication from the port flows to the port owner, and if the port owner terminates, the port is closed.

# Core Definition
The Erlang Reference Manual states: "The Erlang process creating a port is said to be the _port owner_, or the _connected process_ of the port. All communication to and from the port must go through the port owner. If the port owner terminates, so does the port (and the external program, if it is written correctly)." The manual also notes: "In fact, any process can send messages to the port, but the port owner must be identified in the message." (Ports and Port Drivers chapter, "Ports" and "Port BIFs" sections).

# Prerequisites
- **erlang-process** -- The port owner is an Erlang process
- **erlang-port** -- Must understand what a port is

# Key Properties
1. The process that creates a port (calls `open_port/2`) is initially the port owner
2. All output from the port (data messages, closed confirmations) is sent to the port owner
3. If the port owner terminates, the port is closed and the external program should terminate
4. The port owner is linked to the port by default
5. Any process can send command messages to a port, but the sender pid in the message must match the port owner
6. The port owner can be changed using `{Pid, {connect, NewPid}}` message or `port_connect/2` BIF
7. When port ownership is transferred, the old owner remains linked to the port (link must be explicitly removed with `unlink/1`)
8. The new owner is not automatically linked to the port

# Construction / Recognition
## To Set/Change:
1. The initial port owner is the process that calls `open_port/2`
2. Send `Port ! {Pid, {connect, NewPid}}` to transfer ownership to `NewPid`
3. Or call `port_connect(Port, NewPid)` to transfer ownership

## To Identify:
1. Use `erlang:port_info(Port, connected)` to find the current port owner
2. The port owner receives all data and status messages from the port

# Context & Application
The port owner pattern ensures that port communication has a clear responsibility boundary. Only one process receives data from the port, which simplifies protocol handling. The coupling between port owner and port lifetime (owner termination closes the port) provides automatic cleanup.

**Typical contexts:**
- The process managing an external program's lifecycle
- A gen_server wrapping port communication
- Any process that needs to control and respond to an external program

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Changing the port owner:
```erlang
Port ! {self(), {connect, NewPid}}
```
The port replies with `{Port, connected}` to the old owner. The old owner remains linked to the port.

**Example 2** (Ports and Port Drivers, "Port BIFs" section): Using the BIF:
```erlang
port_connect(Port, NewPid)
```
"Sets the port owner of `Port` to `NewPid`. The old port owner `Pid` stays linked to the port and must call `unlink(Port)` if this is not desired."

# Relationships
## Builds Upon
- **erlang-process** -- The port owner is a process
- **erlang-port** -- The port owner controls a port

## Enables
- **port-message-protocol** -- Messages from the port are sent to the port owner

## Related
- **opening-a-port** -- The process that opens a port becomes its owner
- **closing-a-port** -- Owner termination closes the port

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Transferring port ownership with `port_connect/2` but forgetting that the old owner remains linked
  **Correction**: After transferring ownership, the old owner should call `unlink(Port)` to remove the link. Otherwise, if the port closes, the old owner receives an exit signal.

- **Error**: Assuming the new port owner is automatically linked to the port
  **Correction**: The new owner must explicitly call `link(Port)` if it wants to be notified when the port closes.

# Common Confusions
- **Confusion**: Thinking only the port owner can send messages to a port
  **Clarification**: Any process can send messages to a port, but the `Pid` field in the message must identify the port owner. The port receives data from anyone, but sends replies only to the owner.

# Source Reference
Ports and Port Drivers chapter, "Ports" and "Port BIFs" sections.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definition and clear behavioral description
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
