---
# === CORE IDENTIFICATION ===
concept: Port Owner
slug: port-owner

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
  - port owning process
  - connected process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - erlang-process
extends: []
related:
  - open-port
  - port-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the owner of a port?"
  - "What happens to a port when its owner dies?"
  - "How can port ownership be transferred?"
---

# Quick Definition

A port's owner is the Erlang process that receives the port's incoming data; when the owner dies, the port is automatically closed.

# Core Definition

Because ports do not execute any Erlang code themselves, each port has an *owner*, which is a normal Erlang process. When a port receives data from the outside, it is sent to the port owner, which decides what to do with it. The process that opens a port becomes the owner by default, but ownership can be handed over to another process — for example, using the BIF `erlang:port_connect/2`. If the port owner dies, the port is closed automatically ("Erlang and OTP in Action," Ch. 12, Sections 12.1.1 and 12.2.1).

# Prerequisites

- **Port** — Ownership is a property of a port.
- **Process** — The owner is an Erlang process.

# Key Properties

1. Every port has exactly one owner process at a time.
2. The process that calls `open_port/2` becomes the owner by default.
3. All incoming data from the port is delivered to the owner's mailbox.
4. Ownership can be transferred to another process via `erlang:port_connect/2`.
5. If the owner process dies, the port is closed automatically.
6. Any process that knows both the port ID and the owner's pid is allowed to send messages to the port.

# Construction / Recognition

## To Construct/Create:
1. Call `open_port/2` — the calling process becomes the owner.
2. Optionally call `erlang:port_connect/2` to hand ownership to another process.

## To Identify/Recognize:
1. The process whose mailbox receives `{Port, {data, Data}}` messages from a port.

# Context & Application

- **Typical contexts**: Managing the lifecycle of a port-connected external program.
- **Common applications**: Implementing the owning process as a `gen_server` (e.g., `jp_server`) so port management is tied to process lifecycle.
- **Historical/stylistic notes**: Making the owner a `gen_server` lets the owner's death (and thus the port's closure) integrate with OTP supervision.

# Examples

**Example 1** (Section 12.2.1): "There'll always be an associated Erlang process that owns the port, and any incoming data from the port will end up in the owner's mailbox. If the owner dies, the port gets closed."

**Example 2** (Section 12.1.1): Ownership can be handed over to another process using the BIF `erlang:port_connect/2`.

# Relationships

## Builds Upon
- **Port** — The owner is the controlling process of a port.
- **Process** — The owner is an ordinary Erlang process.

## Related
- **open_port BIF** — Establishes the initial owner.
- **Port message-passing protocol** — Data flows between the port and its owner.

# Common Errors

- **Error**: Letting the owner process die unexpectedly while the external program is still needed.
  **Correction**: Tie the owner to OTP supervision so a port closure can be detected and the program restarted.

# Common Confusions

- **Confusion**: Thinking the port itself runs Erlang code.
  **Clarification**: A port runs no Erlang code; the owner process does, acting on the data the port delivers.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Sections 12.1.1 "Plain ports" and 12.2.1 "The Erlang side of the port."

# Verification Notes

- Definition source: Direct adaptation of Sections 12.1.1 and 12.2.1.
- Confidence rationale: HIGH — the book explicitly describes the owner concept and its lifecycle semantics.
- Uncertainties: None.
- Cross-reference status: `process` owned by Agent 1.
- Re-extraction notes: Fresh extraction; no prior card existed.
