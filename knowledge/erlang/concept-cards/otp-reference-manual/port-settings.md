---
# === CORE IDENTIFICATION ===
concept: Port Settings
slug: port-settings

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
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - port options
  - PortSettings

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-port
  - opening-a-port
extends: []
related:
  - port-message-protocol
  - port-drivers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What options can be passed to open_port/2?"
  - "How does the {packet, N} option work?"
  - "How do you configure a port to use binaries instead of lists?"
---

# Quick Definition
Port settings are the list of options passed as the second argument to `open_port/2`. They configure how data is framed between Erlang and the external program, including packet length headers and binary vs. list mode.

# Core Definition
The Erlang Reference Manual states: "`PortSettings` is a list of settings (options) for the port. The list typically contains at least a tuple `{packet, N}`, which specifies that data sent between the port and the external program are preceded by an N-byte length indicator. Valid values for N are 1, 2, or 4. If binaries are to be used instead of lists of bytes, the option `binary` must be included." (Ports and Port Drivers chapter, "Port BIFs" section).

# Prerequisites
- **erlang-port** -- Settings configure port behavior
- **opening-a-port** -- Settings are passed to `open_port/2`

# Key Properties
1. Port settings are a list of options passed to `open_port/2`
2. `{packet, N}` adds an N-byte length header to each message (N = 1, 2, or 4)
3. `{packet, 1}` supports messages up to 255 bytes
4. `{packet, 2}` supports messages up to 65,535 bytes
5. `{packet, 4}` supports messages up to 4 GB
6. `binary` option causes data to be received as binaries instead of lists of bytes
7. Without `{packet, N}`, data arrives as a raw byte stream with no message boundaries
8. Data sent to or received from a port must be an I/O list (binary or a possibly deep list of binaries or integers 0-255)

# Construction / Recognition
## To Construct/Create:
1. Build a list of options: `[{packet, N}]` for length-prefixed framing
2. Add `binary` to receive data as binaries: `[{packet, N}, binary]`
3. Pass the list as the second argument to `open_port/2`

## To Identify/Recognize:
1. The second argument to any `open_port/2` call is the settings list
2. `erlang:port_info(Port)` can reveal some configured settings

# Context & Application
Port settings define the communication contract between Erlang and the external program. The `{packet, N}` option is especially important because both sides must agree on the framing protocol -- the external program must read and write the same N-byte length headers.

**Typical contexts:**
- Configuring packet framing for structured communication with external programs
- Choosing between binary and list data representation based on performance needs
- Setting up the communication protocol before any data exchange

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Common port settings:
```erlang
Port = open_port({spawn, "my_program"}, [{packet, 4}, binary])
```
This configures 4-byte length headers and binary data mode.

**Example 2** (Ports and Port Drivers, "Port BIFs" section): Data format requirement: "In the following examples, `Data` must be an I/O list. An I/O list is a binary or a (possibly deep) list of binaries or integers in the range 0 through 255."

# Relationships
## Builds Upon
- **erlang-port** -- Settings configure port behavior
- **opening-a-port** -- Settings are the second argument to `open_port/2`

## Enables
- **port-message-protocol** -- Settings determine how messages are framed and encoded

## Related
- **port-drivers** -- Port driver behavior may also be affected by settings

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Using `{packet, N}` in Erlang but not implementing the corresponding length-header protocol in the external program
  **Correction**: Both sides must agree on the framing. The external program must read/write N-byte big-endian length headers before each message payload.

- **Error**: Sending data larger than the packet size allows (e.g., >255 bytes with `{packet, 1}`)
  **Correction**: Choose a packet size appropriate for your data: `{packet, 2}` for up to 64KB, `{packet, 4}` for larger payloads.

# Common Confusions
- **Confusion**: Thinking `{packet, N}` refers to TCP packet sizes
  **Clarification**: `{packet, N}` in port settings specifies a length-header framing protocol between the Erlang VM and the external program's stdin/stdout. It is unrelated to network packet sizes.

# Source Reference
Ports and Port Drivers chapter, "Port BIFs" section.

# Verification Notes
- Definition source: Direct from source for `{packet, N}` and `binary` options
- Confidence rationale: Medium -- the reference manual describes the most common options but the full list requires consulting the `erlang:open_port/2` BIF documentation
- Uncertainties: Additional port settings exist (e.g., `stream`, `{line, N}`, `exit_status`, `use_stdio`, `nouse_stdio`) but are not described in this source chapter
- Cross-reference status: All referenced slugs correspond to planned cards
