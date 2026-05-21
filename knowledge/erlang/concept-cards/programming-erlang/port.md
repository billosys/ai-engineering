---
# === CORE IDENTIFICATION ===
concept: Port
slug: port

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "How Erlang Communicates with External Programs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang port"
  - "open_port"
  - "connected process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
extends: []
related:
  - port-program
  - port-protocol
  - linked-in-driver
  - trapping-exits
contrasts_with:

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port in Erlang?"
  - "How does Erlang communicate with external programs?"
  - "How do I create a port?"
---

# Quick Definition

A port is an Erlang object that connects the Erlang system to an external program; you send it messages and receive messages from it, and as far as the programmer is concerned it behaves just like an Erlang process.

# Core Definition

Erlang communicates with external programs through objects called *ports*. If you send a message to a port, the message is sent to the external program connected to the port; messages from the external program appear as Erlang messages coming from the port (Chapter 15, "How Erlang Communicates with External Programs"). As far as the programmer is concerned, a port behaves just like an Erlang process — you can send it messages, register it, and link to it. If the external program crashes, an exit signal is sent to the connected process; if the connected process dies, the external program is killed. The process that creates a port is the *connected process* for that port: all messages to the port must be tagged with the connected process's PID, and all messages from the external program are sent to the connected process. A port is created with `open_port(PortName, [Opt])`, where `PortName` is e.g. `{spawn, Command}` or `{fd, In, Out}` and `Opt` includes packetization options such as `{packet, N}`, `stream`, and `{line, Max}`.

# Prerequisites

- **Process** — A port behaves like a process; you must understand processes first.
- **Message passing** — A port is driven entirely by sending and receiving messages.

# Key Properties

1. A port connects the Erlang system to an external operating system process.
2. A port behaves like an Erlang process — it can be messaged, registered, and linked.
3. The creator of a port is its *connected process*; all port messages are tagged with that PID.
4. If the external program crashes, an exit signal goes to the connected process; if the connected process dies, the external program is killed.
5. `open_port({spawn, Command}, Opts)` starts an external program; `{fd, In, Out}` reuses file descriptors.
6. Options `{packet, N}`, `stream`, and `{line, Max}` control how data is framed.

# Construction / Recognition

## To Create and Use a Port:
1. Call `Port = open_port({spawn, "./command"}, [{packet, 2}])`.
2. Send data with `Port ! {self(), {command, Data}}` where `Data` is an I/O list.
3. Receive replies with `receive {Port, {data, Data}} -> ... end`.
4. Close it with `Port ! {self(), close}`.

## To Recognize It:
1. Look for `open_port/2` calls and `{Port, {data, Data}}` receive clauses.
2. Look for messages tagged with the connected process's PID.

# Context & Application

- **Typical contexts**: Safely interfacing Erlang to programs written in other languages.
- **Common applications**: The `example1` C program is driven through a port; the connected process traps exits and handles `{'EXIT', Port, Reason}`.
- **Historical/stylistic notes**: Using a port is the *safe* way to interface foreign code — the external program runs outside the Erlang VM, so a bug in it cannot crash Erlang.

# Examples

**Example 1** (Chapter 15, "The Erlang Program"): `Port = open_port({spawn, "./example1"}, [{packet, 2}])` starts the external C program and frames each message with a 2-byte length header.

**Example 2** (Chapter 15): To send a command, `Port ! {self(), {command, encode(Msg)}}`; to receive the reply, `receive {Port, {data, Data}} -> ... end`.

# Relationships

## Builds Upon
- **Process** and **message passing** — a port is a process-like, message-driven object.

## Enables
- **Port program** — the external program a port talks to.
- **Linked-in driver** — a port whose driver code is linked into the Erlang VM.

## Related
- **Port protocol** — the byte-stream convention exchanged through a port.
- **Trapping exits** — the connected process usually traps exits to detect external-program crashes.

## Contrasts With
- **Socket interfacing** — a socket does not behave like a process; a port does (it can be linked, messaged from a remote node, etc.).

# Common Errors

- **Error**: Sending port messages not tagged with the connected process's PID.
  **Correction**: All messages to the port must carry the connected process's PID, e.g. `{self(), {command, Data}}`.
- **Error**: Not trapping exits in the connected process and missing external-program crashes.
  **Correction**: Call `process_flag(trap_exit, true)` so the crash arrives as `{'EXIT', Port, Reason}`.

# Common Confusions

- **Confusion**: A port and a socket are the same kind of object.
  **Clarification**: A port behaves like a process (linkable, remotely messageable); a socket does not.
- **Confusion**: A port runs the external code inside the Erlang VM.
  **Clarification**: A `{spawn, Command}` port runs the external program *outside* the VM as a separate OS process — the safe approach.

# Source Reference

Chapter 15: Interfacing Techniques, sections "How Erlang Communicates with External Programs" (the `open_port/2` spec and port messages) and "The Erlang Program" (the `example1` port usage).

# Verification Notes

- Definition source: Direct adaptation of "How Erlang Communicates with External Programs."
- Confidence rationale: HIGH — ports, the connected process, and `open_port` are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `process`/`message-passing`/`trapping-exits` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
