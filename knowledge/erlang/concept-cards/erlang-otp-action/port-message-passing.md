---
# === CORE IDENTIFICATION ===
concept: Port Message-Passing Protocol
slug: port-message-passing

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
section: "12.1. Ports and NIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{command, Data}"
  - "{data, Data}"
  - port communication

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - port-owner
extends: []
related:
  - open-port
  - external-term-format
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you send data to a port?"
  - "What message does a port send when foreign code produces output?"
  - "What form does data take when communicating with a port?"
---

# Quick Definition

Erlang communicates with a port by message passing: send `{self(), {command, Data}}` to the port, and receive `{Port, {data, Data}}` back when the foreign code produces output.

# Core Definition

The basic form of communication with a port is by passing messages. To pass data from Erlang to the port (and on to the foreign code), you send a message of the form `PortID ! {self(), {command, Data}}`, where `Data` is a binary or an IO-list; the pid of the port owner must be included in the message. When a port has data to deliver from the foreign code, it sends it asynchronously to the port owner as a message of the form `{PortID, {data, Data}}`. The shape of the `Data` field depends on the options used to create the port — for example, a binary or a list of bytes, delivered in fixed-size chunks or line by line ("Erlang and OTP in Action," Ch. 12, Section 12.1).

# Prerequisites

- **Port** — Messages are exchanged with a port object.
- **Port owner** — Output messages are delivered to the owner process.

# Key Properties

1. Outgoing: `PortID ! {self(), {command, Data}}` sends data to the foreign code.
2. `Data` for a command must be a binary or an IO-list (a possibly deep list of bytes/binaries).
3. The owner pid must be included in the outgoing message tuple.
4. Incoming: the port sends `{PortID, {data, Data}}` asynchronously to the owner.
5. The shape of incoming `Data` (binary vs byte list, chunked vs line-based) depends on port options.
6. The `erlang` module also provides BIFs for direct port manipulation regardless of ownership, but the message-passing style is the usual approach.

# Construction / Recognition

## To Construct/Create:
1. To send: `Port ! {self(), {command, Data}}` where `Data` is a binary or IO-list.
2. To receive: match `{Port, {data, Data}}` in a `receive` (or in `handle_info`/`handle_call` of the owning `gen_server`).

## To Identify/Recognize:
1. Code matching `{Port, {data, _}}` messages or sending `{_, {command, _}}` tuples to a port.

# Context & Application

- **Typical contexts**: Exchanging requests and results with port-connected foreign code.
- **Common applications**: `jp_server` sends `{self(), {command, term_to_binary(Msg)}}` and waits for `{Port, {data, Data}}`.
- **Historical/stylistic notes**: Wrapping the send/receive inside a `gen_server` call lets the server perform concurrency control for the single-client external program.

# Examples

**Example 1** (Section 12.2.1): `handle_call` sends `Port ! {self(),{command, term_to_binary(Msg)}}` and then `receive {Port, {data, Data}} -> {reply, binary_to_term(Data), State} end`.

**Example 2** (Section 12.1): `open_port({spawn, "echo 'Hello world!'"}, [])` yields the message `{#Port<0.512>, {data,"'Hello world!'\n"}}`.

# Relationships

## Builds Upon
- **Port** — The protocol is how you talk to a port.
- **Port owner** — Incoming `{data, ...}` messages go to the owner.

## Related
- **open_port BIF** — Port options determine the shape of `Data`.
- **External term format** — `term_to_binary`/`binary_to_term` are commonly used to marshal `Data`.

# Common Errors

- **Error**: Sending `{command, Data}` without the owner pid.
  **Correction**: The message must be `{self(), {command, Data}}` — the owner pid is required.

- **Error**: Sending a non-binary, non-IO-list value as command data.
  **Correction**: `Data` must be a binary or an IO-list.

# Common Confusions

- **Confusion**: Assuming incoming `Data` always has the same shape.
  **Clarification**: Its shape (binary vs byte list, chunked vs line-based) depends on the options passed to `open_port/2`.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.1 "Ports and NIFs" and Section 12.2.1 "The Erlang side of the port."

# Verification Notes

- Definition source: Direct adaptation of Section 12.1 and the `handle_call` listing in 12.2.1.
- Confidence rationale: HIGH — the book gives the exact message forms.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
