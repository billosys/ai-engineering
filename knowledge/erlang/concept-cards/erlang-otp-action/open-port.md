---
# === CORE IDENTIFICATION ===
concept: open_port BIF
slug: open-port

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.1. The Erlang side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "open_port/2"
  - "erlang:open_port/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
extends: []
related:
  - port-owner
  - priv-directory
  - port-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you open a port to an external program?"
  - "What options can you pass to open_port/2?"
  - "What do the binary, packet, and exit_status options do?"
---

# Quick Definition

`open_port/2` is the BIF that creates a port, launching an external program (`{spawn, ProgramPath}`) and configuring data handling via an options list.

# Core Definition

`open_port/2` is the built-in function used to create a port. It is typically called with `open_port({spawn, ProgramPath}, Options)`, where `ProgramPath` is the path of an executable file (commonly placed in the application's `priv` directory) and `Options` is a list specifying how the port should treat data going to and from the foreign code. Common options include `binary` (deliver data as binaries rather than byte lists), `{packet, N}` (prefix each data chunk with an N-byte length header, where N is 1, 2, or 4), and `exit_status` (deliver the exit status of the external program as a message) ("Erlang and OTP in Action," Ch. 12, Section 12.2.1).

# Prerequisites

- **Port** — `open_port/2` creates a port.

# Key Properties

1. Called as `open_port({spawn, ProgramPath}, Options)` for an external program.
2. The calling process becomes the port owner.
3. `binary` — incoming data is delivered as binaries instead of lists of bytes.
4. `{packet, N}` — prepends an N-byte (1, 2, or 4) length header to each chunk; N is the same for both directions.
5. `exit_status` — the owner receives an out-of-band message with the external program's exit status.
6. The executable is normally located by `code:priv_dir(AppName)` joined with the program name.
7. For a linked-in driver, `open_port({spawn, DriverName}, Options)` uses the driver's registered name, not a file path.

# Construction / Recognition

## To Construct/Create:
1. Determine the program path, e.g. `filename:join([code:priv_dir(AppName), "jp_prog"])`.
2. Call `open_port({spawn, ProgramPath}, [binary, {packet, 4}, exit_status])`.
3. Store the returned port identifier (e.g., in `gen_server` state).

## To Identify/Recognize:
1. A call `open_port({spawn, ...}, [...])` whose result is a `#Port<...>` value.

# Context & Application

- **Typical contexts**: Starting the foreign program in a `gen_server`'s `init/1` callback.
- **Common applications**: `jp_server` opens a port to the `jp_prog` JSON parser with `[binary, {packet, 4}, exit_status]`.
- **Historical/stylistic notes**: For a linked-in driver the same `open_port` form is used, but the library must first be loaded with `erl_ddll:load/2`.

# Examples

**Example 1** (Section 12.2.1): `Port = open_port({spawn, filename:join([PrivDir, "jp_prog"])}, [binary, {packet, 4}, exit_status])`.

**Example 2** (Section 12.3.4): For a linked-in driver, `open_port({spawn, "jp_driver"}, [binary])` after `erl_ddll:load(PrivDir, "jp_driver")`.

# Relationships

## Builds Upon
- **Port** — `open_port/2` is the constructor for a port.

## Enables
- **Port owner** — The caller becomes the owner.

## Related
- **priv directory** — Where the external executable normally lives.
- **Port message-passing protocol** — Options shape the messages the port exchanges.

# Common Errors

- **Error**: Using `{packet, N}` with a linked-in driver.
  **Correction**: Drop `{packet, N}` for linked-in drivers — the `erl_driver` API already supplies the data size.

- **Error**: Reading a `{packet, 4}` length header straight into a `uint32_t` on the C side.
  **Correction**: Packet headers are network byte order (big-endian); decode them endianness-independently.

# Common Confusions

- **Confusion**: Thinking the `{spawn, Name}` argument is always a file path.
  **Clarification**: For an external program it is a file path; for a linked-in driver it is the driver's registered name.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.2.1 "The Erlang side of the port."

# Verification Notes

- Definition source: Direct adaptation of Section 12.2.1, with the driver form from 12.3.4.
- Confidence rationale: HIGH — the book shows `open_port/2` usage and explains each option.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
