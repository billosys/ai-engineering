---
# === CORE IDENTIFICATION ===
concept: Erlang Port
slug: erlang-port

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
  - port
  - Erlang port

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - port-owner
  - opening-a-port
  - port-message-protocol
  - port-drivers
  - closing-a-port
contrasts_with:
  - erlang-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang port?"
  - "How does Erlang communicate with external programs?"
  - "What is the relationship between a port and its owner process?"
---

# Quick Definition
A port is the basic mechanism for communication between Erlang and external programs. It provides a byte-oriented interface to an external OS process, allowing Erlang to send and receive lists of bytes (including binaries) through a controlled channel.

# Core Definition
The Erlang Reference Manual states: "_Ports_ provide the basic mechanism for communication with the external world, from Erlang's point of view. They provide a byte-oriented interface to an external program. When a port has been created, Erlang can communicate with it by sending and receiving lists of bytes, including binaries." The external program "resides in another OS process. By default, it reads from standard input (file descriptor 0) and writes to standard output (file descriptor 1). The external program is to terminate when the port is closed." (Ports and Port Drivers chapter, "Ports" section).

# Prerequisites
- **erlang-process** -- Ports are owned by processes and communicate using the same message-passing paradigm

# Key Properties
1. Ports provide a byte-oriented interface to external programs
2. The external program runs in a separate OS process
3. By default, the external program reads from stdin (fd 0) and writes to stdout (fd 1)
4. The external program should terminate when the port is closed
5. Every port has a port owner (connected process) through which all communication flows
6. If the port owner terminates, the port (and the external program) also terminates
7. Port identifiers can be used like pids for sending messages, linking, and registering names
8. Messages sent to ports are delivered asynchronously (since OTP 16)
9. Ports can also be implemented as port drivers (linked-in C code) rather than external OS processes

# Construction / Recognition
## To Construct/Create:
1. Call `open_port(PortName, PortSettings)` -- returns a port identifier
2. `PortName` is usually `{spawn, Command}` where `Command` is the external program name
3. `PortSettings` is a list of options such as `{packet, N}` and `binary`

## To Identify/Recognize:
1. Port identifiers are a distinct data type, similar to pids
2. `erlang:ports()` returns a list of all ports on the current node
3. `erlang:port_info(Port, Item)` returns information about a port

# Context & Application
Ports are Erlang's primary mechanism for interoperating with non-Erlang programs. They provide a safe boundary: the external program runs in its own OS process, so crashes in the external program do not bring down the Erlang VM. This is in contrast to port drivers (NIFs/linked-in drivers) which run inside the VM and can crash the entire runtime.

**Typical contexts:**
- Running external command-line programs and communicating with them
- Interfacing with C/C++ programs via stdin/stdout
- Legacy system integration
- Any scenario where the external program should be isolated from the Erlang VM

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Creating a port:
```erlang
Port = open_port({spawn, Command}, [binary, {packet, 4}])
```
This starts the external program `Command` with 4-byte length-prefixed packet framing and binary data mode.

**Example 2** (Ports and Port Drivers, "Ports" section): The external program model: "The external program resides in another OS process. By default, it reads from standard input (file descriptor 0) and writes to standard output (file descriptor 1). The external program is to terminate when the port is closed."

# Relationships
## Builds Upon
- **erlang-process** -- Ports are owned by processes and use message passing

## Enables
- **port-owner** -- Every port has an owner process
- **opening-a-port** -- `open_port/2` creates ports
- **port-message-protocol** -- The message format for port communication
- **port-drivers** -- Port drivers are an alternative implementation
- **closing-a-port** -- Ports can be closed

## Related
Nothing additional.

## Contrasts With
- **erlang-process** -- Processes are internal Erlang execution units; ports bridge to external OS processes. Both use message passing, but ports provide a byte-oriented interface rather than Erlang term exchange.

# Common Errors
- **Error**: Forgetting that the external program must handle stdin/stdout for communication
  **Correction**: The external program must read from fd 0 and write to fd 1. If it uses other I/O channels, the port cannot communicate with it.

- **Error**: Assuming port communication is synchronous
  **Correction**: Messages sent to ports are delivered asynchronously (since OTP 16). The source explicitly notes this change.

# Common Confusions
- **Confusion**: Confusing Erlang ports with network ports (TCP/UDP)
  **Clarification**: Erlang ports are a VM-level abstraction for communicating with external OS processes via stdin/stdout. They are unrelated to TCP/UDP network ports, although network communication can be implemented using ports.

# Source Reference
Ports and Port Drivers chapter, "Ports" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- clear, explicit definition in the opening paragraph
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards in this extraction
