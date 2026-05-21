---
# === CORE IDENTIFICATION ===
concept: Opening a Port
slug: opening-a-port

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
  - open_port
  - open_port/2

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-port
extends: []
related:
  - port-owner
  - port-settings
  - port-drivers
  - closing-a-port
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you create a port in Erlang?"
  - "What arguments does open_port/2 take?"
  - "What does open_port return?"
  - "How does Erlang decide whether to start an external program or a port driver?"
---

# Quick Definition
`open_port(PortName, PortSettings)` is the BIF that creates a new port, returning a port identifier. The `PortName` specifies what external program or port driver to connect to, and `PortSettings` is a list of options controlling the port's behavior.

# Core Definition
The Erlang Reference Manual states: "To create a port, call `open_port(PortName, PortSettings)`. It returns a port identifier `Port` as the result of opening the new port. Messages can be sent to and received from a port identifier, just like a PID. Port identifiers can also be linked to using `link/1`, or registered under a name using `register/2`." (Ports and Port Drivers chapter, "Port BIFs" section).

The manual further explains: "`PortName` is usually a tuple `{spawn, Command}`, where the string `Command` is the name of the external program. The external program runs outside the Erlang workspace, unless a port driver with the name `Command` is found. If `Command` is found, that driver is started." (Ports and Port Drivers chapter, "Port BIFs" section).

# Prerequisites
- **erlang-port** -- Must understand the port concept before creating one

# Key Properties
1. `open_port/2` takes a `PortName` and a list of `PortSettings`
2. Returns a port identifier that can be used like a pid for messaging, linking, and registration
3. `PortName` is typically `{spawn, Command}` where `Command` names the external program
4. If a port driver matching `Command` exists, the driver is started instead of an external program
5. The calling process becomes the port owner
6. The port identifier can be linked to with `link/1` and registered with `register/2`

# Construction / Recognition
## To Construct/Create:
1. Call `open_port({spawn, Command}, PortSettings)` where `Command` is the external program
2. `PortSettings` should include framing options like `{packet, N}` and optionally `binary`
3. The calling process becomes the port owner automatically

## To Identify/Recognize:
1. The return value of `open_port/2` is a port identifier
2. Port identifiers are listed by `erlang:ports()`

# Context & Application
`open_port/2` is the entry point for all port-based external program communication. It establishes the connection between the Erlang VM and the external process, sets up the communication protocol (packet framing, binary vs. list mode), and returns a handle for subsequent interaction.

**Typical contexts:**
- Starting an external program for data processing
- Connecting to a port driver for high-performance C integration
- Wrapping command-line tools for use within an Erlang system

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Basic port creation:
```erlang
Port = open_port({spawn, "my_program"}, [{packet, 2}, binary])
```
This starts `my_program` as an external process with 2-byte length-prefixed packets and binary data mode.

**Example 2** (Ports and Port Drivers, "Port BIFs" section): Port driver selection: if a port driver named `"my_program"` is already loaded, `open_port({spawn, "my_program"}, Settings)` will start the driver instead of an external OS process. "The external program runs outside the Erlang workspace, unless a port driver with the name `Command` is found."

# Relationships
## Builds Upon
- **erlang-port** -- open_port creates ports

## Enables
- **port-owner** -- The calling process becomes the port owner
- **port-message-protocol** -- After opening, the port can exchange messages

## Related
- **port-settings** -- PortSettings controls the port's behavior
- **port-drivers** -- open_port may start a port driver instead of an external program
- **closing-a-port** -- Ports opened with open_port must eventually be closed

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Forgetting to specify `{packet, N}` and assuming the port automatically frames messages
  **Correction**: Without `{packet, N}`, data arrives as raw bytes with no message boundaries. Specify `{packet, 1}`, `{packet, 2}`, or `{packet, 4}` to have length-prefixed framing.

- **Error**: Passing an invalid command name and not handling the resulting error
  **Correction**: If the command cannot be found, `open_port/2` raises an error. Wrap the call in a try/catch or ensure the external program exists.

# Common Confusions
- **Confusion**: Thinking `open_port` always starts an external OS process
  **Clarification**: If a port driver with a matching name is already loaded, `open_port({spawn, Command}, _)` starts the driver instead. The driver runs inside the Erlang VM, not as a separate OS process.

# Source Reference
Ports and Port Drivers chapter, "Port BIFs" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description with clear parameters
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
