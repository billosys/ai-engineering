---
# === CORE IDENTIFICATION ===
concept: Out-of-Band Message
slug: out-of-band-message

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: generic-server
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.4 The callback function section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - out-of-band messages
  - naked message

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - message-passing
extends: []
related:
  - gen-server-handle-info
  - gen-server-timeout
  - gen-server-call
  - gen-server-cast
contrasts_with:
  - gen-server-call
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an out-of-band message in a gen_server?"
  - "What kinds of messages does handle_info/2 receive?"
  - "Why might naked messages arrive at a gen_server?"
---

# Quick Definition

An out-of-band message is any message arriving in a `gen_server`'s mailbox that was not sent via `gen_server:call` or `gen_server:cast` — for example, a naked `!` message from a socket or a timeout event.

# Core Definition

Out-of-band messages are messages to a `gen_server` process that were not sent using `call` or `cast` and are therefore handled by the `handle_info/2` callback (Ch. 3, "Handling out-of-band messages"). They can happen when a server needs to communicate with some other component that relies on direct messages rather than OTP library calls — for example, a socket or a port driver. Typically they are naked messages sent with the plain `!` operator. The book advises avoiding sending out-of-band messages to a `gen_server` when it can be helped.

# Prerequisites

- **gen_server behaviour** — Out-of-band messages are defined relative to `gen_server`'s `call`/`cast` machinery.
- **Message passing** — Out-of-band messages are plain Erlang messages.

# Key Properties

1. Any message not sent via `call` or `cast`.
2. Always handled by the `handle_info/2` callback.
3. Often naked `!` messages from sockets or port drivers.
4. Server timeout events arrive as out-of-band `timeout` messages.
5. The book recommends avoiding them where possible.

# Construction / Recognition

## To Recognize an Out-of-Band Message:
1. Note whether it was sent through `gen_server:call`/`cast` — if not, it is out-of-band.
2. It will be dispatched to `handle_info/2`, not `handle_call/3` or `handle_cast/2`.

# Context & Application

Out-of-band messages are unavoidable when a server owns a resource — like an active socket — that delivers data as raw messages.

- **Typical contexts**: Servers owning active TCP sockets or port drivers; timeout-driven servers.
- **Common applications**: `tr_server` receives `{tcp, Socket, RawData}` messages from its active socket as out-of-band data.

# Examples

**Example 1** (Ch. 3): An active socket forwards incoming TCP data as `{tcp, Socket, RawData}` messages; these are out-of-band as far as the `gen_server` container is concerned and go to `handle_info/2`.

**Example 2** (Ch. 3): A `gen_server` server timeout generates an out-of-band message with the single atom `timeout`.

# Relationships

## Related
- **gen-server-handle-info** — The callback that handles out-of-band messages.
- **gen-server-timeout** — Timeout events arrive as out-of-band messages.

## Contrasts With
- **gen-server-call** — `call` messages are in-band, dispatched to `handle_call/3`.
- **gen-server-cast** — `cast` messages are in-band, dispatched to `handle_cast/2`.

# Common Errors

- **Error**: Routinely sending `!` messages to a `gen_server`.
  **Correction**: Use `call`/`cast`; reserve out-of-band messages for external components that require them.

# Common Confusions

- **Confusion**: Thinking out-of-band messages are errors.
  **Clarification**: They are legitimate (e.g. socket data, timeouts); they are simply messages outside the `call`/`cast` protocol.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "Handling out-of-band messages." See Listing 3.5 and Table 3.5.

# Verification Notes

- Definition source: Direct adaptation of "Handling out-of-band messages."
- Confidence rationale: HIGH — explicit definition in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `message-passing` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
