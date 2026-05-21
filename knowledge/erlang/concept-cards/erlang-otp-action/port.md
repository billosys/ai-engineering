---
# === CORE IDENTIFICATION ===
concept: Port
slug: port

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
section: "12.1.1. Plain ports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - plain port
  - Erlang port

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - foreign-code-integration
extends: []
related:
  - open-port
  - port-owner
  - linked-in-driver
  - port-message-passing
contrasts_with:
  - linked-in-driver
  - nif

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port in Erlang?"
  - "How does a plain port communicate with foreign code?"
  - "Why are plain ports safe?"
---

# Quick Definition

A port is a process-like object that connects Erlang to foreign code; a plain port runs that code as a separate OS process communicating over standard input and output.

# Core Definition

Ports are the oldest and most basic form of connecting Erlang to the world outside, and are the simplest and most common way to communicate with foreign code. A port is an object with one foot in each world — one on the Erlang language side and one on the operating system side. On the Erlang side a port is similar to a process: it is created, you can communicate with it using normal message passing, and it can die; each created port gets a unique, non-recycled identifier. With a *plain port*, the foreign code runs as an external program in a separate operating system process, using its standard input and standard output streams for communication with Erlang. Because the external program lives in its own address space, no matter what it does it cannot crash the running Erlang system ("Erlang and OTP in Action," Ch. 12, Sections 12.1 and 12.1.1).

# Prerequisites

- **Process** — A port behaves like a process on the Erlang side.
- **Foreign code integration mechanisms** — A port is one of the three integration mechanisms.

# Key Properties

1. Process-like on the Erlang side: created, communicated with via messages, can die.
2. Each port has a unique identifier that is never recycled.
3. A plain port runs foreign code as a separate OS process connected via stdin/stdout.
4. Ports are completely language-neutral — the foreign program can be in any language, even a shell script.
5. The external program lives in its own address space, so it cannot crash the Erlang VM.
6. Each port has an *owner* process; incoming data is sent to the owner; if the owner dies, the port is closed.
7. The safety of isolation costs speed — all data must move as a byte stream.

# Construction / Recognition

## To Construct/Create:
1. Call `open_port({spawn, Command}, Options)` to launch the external program and create the port.
2. The opening process becomes the port owner (ownership can be transferred with `erlang:port_connect/2`).
3. Send data with `PortID ! {self(), {command, Data}}` and receive `{PortID, {data, Data}}` messages.

## To Identify/Recognize:
1. A value printed as `#Port<0.NNN>` in the shell, produced by `open_port/2`.

# Context & Application

- **Typical contexts**: Safely calling external programs and even hardware drivers from Erlang.
- **Common applications**: Wrapping the YAJL JSON C library as an external `jp_prog` program.
- **Historical/stylistic notes**: Many UNIX-style programs can be used from Erlang as-is; sometimes a small wrapper script is needed to adapt stdin/stdout.

# Examples

**Example 1** (Section 12.1): `Port = open_port({spawn, "echo 'Hello world!'"}, []).` runs an OS command; the port sends back `{#Port<0.512>, {data,"'Hello world!'\n"}}`.

**Example 2** (Figure 12.1): External code communicates with Erlang over standard input and standard output; if the external program crashes, the port is simply closed.

# Relationships

## Builds Upon
- **Foreign code integration mechanisms** — A port is the safe, default mechanism.

## Enables
- **open_port BIF** — The function that creates a port.
- **Port owner** — Every port has an owning process.

## Related
- **Port message-passing protocol** — How data flows to and from a port.

## Contrasts With
- **Linked-in driver** — A driver runs in the VM's address space (faster, riskier); a plain port runs as a separate OS process (slower, safe).
- **NIF** — A NIF runs in a VM thread; a plain port isolates foreign code in its own process.

# Common Errors

- **Error**: Sending a command to a port without including the owner pid.
  **Correction**: Use the form `PortID ! {self(), {command, Data}}` — the owner's pid must be included.

# Common Confusions

- **Confusion**: Thinking a crashing external program can take down the Erlang VM.
  **Clarification**: With a plain port the program runs in its own OS process; a crash just closes the port — the VM is unaffected.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.1 "Ports and NIFs" and 12.1.1 "Plain ports." See Figure 12.1.

# Verification Notes

- Definition source: Direct adaptation of Sections 12.1 and 12.1.1.
- Confidence rationale: HIGH — the book explicitly defines ports and plain ports.
- Uncertainties: None.
- Cross-reference status: `process` owned by Agent 1.
- Re-extraction notes: Fresh extraction; no prior card existed.
