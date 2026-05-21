---
# === CORE IDENTIFICATION ===
concept: Hiding the Server Protocol
slug: server-protocol-hiding

# === CLASSIFICATION ===
category: api-design
subcategory: encapsulation
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.3 The API section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - protocol hiding
  - "hiding the protocol"
  - server protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour-api-section
  - gen-server
extends:
  - behaviour-api-section
related:
  - gen-server-call
  - gen-server-cast
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a server's protocol?"
  - "Why should the API hide the server protocol?"
  - "How do API functions encapsulate message formats?"
---

# Quick Definition

A server's protocol is the set of messages it accepts. Hiding the protocol means wrapping those messages in API functions so callers never depend on the message formats.

# Core Definition

The set of messages that a process will accept is referred to as its *protocol* (Ch. 3, "Hiding the protocol"). One of the main tasks of the API is to hide this protocol from the rest of the world. Message formats — even simple atoms like `get_count` and `stop`, or complex tuples — are implementation details that users of a module should not know, because depending on them would make future changes hard. By wrapping communication with the server in API functions, the users of the module remain oblivious to the message formats. A second level of hiding also occurs: the OTP libraries hide the real wire messages, since the data passed to `call`/`cast` is only the payload.

# Prerequisites

- **Behaviour API section** — Protocol hiding is a purpose of the API section.
- **gen_server behaviour** — The protocol is the messages a `gen_server` accepts.

# Key Properties

1. A server's protocol is the set of messages it accepts.
2. Message formats are implementation details, not public contract.
3. API functions wrap message construction and sending.
4. Hiding the protocol lets the message format change without breaking clients.
5. OTP adds a second level of hiding by wrapping payloads with metadata.

# Construction / Recognition

## To Hide the Protocol:
1. Define the internal message format (atoms, tuples).
2. Write API functions that build and send those messages via `call`/`cast`.
3. Export only the API functions; never document or expose the raw messages.

# Context & Application

Protocol hiding is core to API design for servers: it decouples clients from the server's internals so the server can evolve.

- **Typical contexts**: Designing any `gen_server` module's public surface.
- **Common applications**: `tr_server` accepts `get_count` and `stop` atoms but exposes only `get_count/0` and `stop/0` API functions.

# Examples

**Example 1** (Ch. 3): `tr_server` internally accepts the atoms `get_count` and `stop`, but users call the API functions `get_count()` and `stop()` and never see the atoms.

**Example 2** (Ch. 3): A hypothetical `add_user` API function wraps a complex `{add_user, [...]}` tuple message so clients do not depend on that format.

# Relationships

## Builds Upon
- **Behaviour API section** — Protocol hiding is one of the API section's purposes.

## Related
- **gen-server-call** / **gen-server-cast** — The API functions wrap these to send protocol messages.

## Contrasts With
- This is a design principle; the source draws no direct contrast.

# Common Errors

- **Error**: Letting clients send raw protocol messages directly to the server.
  **Correction**: Force all communication through API functions so the message format stays private.

# Common Confusions

- **Confusion**: Thinking the payload passed to `call`/`cast` is the actual message on the wire.
  **Clarification**: It is only the payload; OTP wraps it with metadata — a second layer of hiding.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.3 "The API section," subsection "Hiding the protocol" and the "Double blind" sidebar.

# Verification Notes

- Definition source: Direct adaptation of "Hiding the protocol."
- Confidence rationale: HIGH — explicit definition of "protocol" and its hiding.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
