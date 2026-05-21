---
# === CORE IDENTIFICATION ===
concept: Port Message Protocol
slug: port-message-protocol

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
section: "Port BIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - port messages
  - port communication protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-port
  - port-owner
extends: []
related:
  - opening-a-port
  - port-settings
  - closing-a-port
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What messages can be sent to a port?"
  - "What messages does a port send back?"
  - "How does a process send data to an external program through a port?"
  - "What BIFs provide alternatives to port message passing?"
---

# Quick Definition
Ports communicate using a defined message protocol. Processes send messages of the form `{Pid, {command, Data}}`, `{Pid, close}`, or `{Pid, {connect, NewPid}}` to a port. The port sends `{Port, {data, Data}}`, `{Port, closed}`, `{Port, connected}`, or `{'EXIT', Port, Reason}` messages back to its owner.

# Core Definition
The Erlang Reference Manual defines the messages that can be sent to a port:
- `{Pid, {command, Data}}` -- "Sends `Data` to the port."
- `{Pid, close}` -- "Closes the port. Unless the port is already closed, the port replies with `{Port, closed}` when all buffers have been flushed and the port really closes."
- `{Pid, {connect, NewPid}}` -- "Sets the port owner of `Port` to `NewPid`. Unless the port is already closed, the port replies with `{Port, connected}` to the old port owner."

Messages received from a port (sent to the owner):
- `{Port, {data, Data}}` -- "`Data` is received from the external program."
- `{Port, closed}` -- "Reply to `Port ! {Pid, close}`."
- `{Port, connected}` -- "Reply to `Port ! {Pid, {connect, NewPid}}`."
- `{'EXIT', Port, Reason}` -- "If the port has terminated for some reason."

(Ports and Port Drivers chapter, "Port BIFs" section).

# Prerequisites
- **erlang-port** -- Must understand the port concept
- **port-owner** -- The port owner (Pid) must be identified in outgoing messages and receives all incoming messages

# Key Properties
1. Three outgoing message types: command (send data), close, and connect (transfer ownership)
2. Four incoming message types: data, closed, connected, and EXIT
3. All outgoing messages require the port owner's pid as the first element
4. Any process can send messages to a port, but the pid in the message must be the port owner
5. All incoming messages from the port are sent to the port owner
6. Messages sent to ports are delivered asynchronously (since OTP 16)
7. Data must be an I/O list: a binary or a (possibly deep) list of binaries or integers 0-255
8. BIF alternatives exist: `port_command/2`, `port_close/1`, `port_connect/2`

# Construction / Recognition
## To Send Data to a Port:
1. `Port ! {self(), {command, Data}}` -- send data via message
2. Or call `port_command(Port, Data)` -- equivalent BIF

## To Close a Port:
1. `Port ! {self(), close}` -- request port closure via message
2. Or call `port_close(Port)` -- equivalent BIF

## To Transfer Ownership:
1. `Port ! {self(), {connect, NewPid}}` -- transfer via message
2. Or call `port_connect(Port, NewPid)` -- equivalent BIF

## To Receive Data:
```erlang
receive
    {Port, {data, Data}} -> handle_data(Data);
    {Port, closed} -> handle_closed();
    {'EXIT', Port, Reason} -> handle_exit(Reason)
end
```

# Context & Application
The port message protocol provides a structured way to communicate with external programs. It follows the same message-passing paradigm as inter-process communication, making ports feel natural within Erlang's concurrency model. The BIF alternatives (`port_command/2`, `port_close/1`, `port_connect/2`) provide the same functionality with slightly different error handling semantics.

**Typical contexts:**
- Sending commands to and receiving results from external programs
- Implementing request/response protocols with external tools
- Building gen_server wrappers around port communication

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Sending data to a port:
```erlang
Port ! {self(), {command, "hello"}}
```
Or equivalently:
```erlang
port_command(Port, "hello")
```

**Example 2** (Ports and Port Drivers, "Port BIFs" section): The full set of BIF alternatives:
- `port_command(Port, Data)` -- sends Data to the port
- `port_close(Port)` -- closes the port
- `port_connect(Port, NewPid)` -- changes the port owner
- `erlang:port_info(Port, Item)` -- returns port information
- `erlang:ports()` -- returns all ports on the current node

**Example 3** (Ports and Port Drivers, "Port BIFs" section): Additional port driver BIFs:
- `port_control/3` -- synchronous control operation on a port driver
- `erlang:port_call/3` -- synchronous call to a port driver

# Relationships
## Builds Upon
- **erlang-port** -- The message protocol defines how to communicate with ports
- **port-owner** -- Messages require the owner pid and replies go to the owner

## Enables
Nothing directly -- the protocol is the complete communication mechanism.

## Related
- **opening-a-port** -- Ports must be opened before messages can be exchanged
- **port-settings** -- Settings affect how data is framed in messages
- **closing-a-port** -- The close message/BIF is part of this protocol

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Sending `{self(), {command, Data}}` to a port when `self()` is not the port owner
  **Correction**: The `Pid` in the message must be the port owner. If another process needs to send data, it should go through the port owner or the port owner should be changed first.

- **Error**: Forgetting to handle `{'EXIT', Port, Reason}` messages
  **Correction**: If the external program crashes or the port closes unexpectedly, an EXIT message is sent to the owner. Always include a handler for this case.

# Common Confusions
- **Confusion**: Thinking `port_command/2` and `Port ! {self(), {command, Data}}` are fundamentally different
  **Clarification**: They achieve the same result. The BIF form provides slightly different error handling (raises an error if the port is invalid), but both send the data asynchronously to the port.

# Source Reference
Ports and Port Drivers chapter, "Port BIFs" section.

# Verification Notes
- Definition source: Direct from source -- all message formats explicitly listed
- Confidence rationale: High -- complete enumeration of message types with descriptions
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
