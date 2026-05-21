---
# === CORE IDENTIFICATION ===
concept: gen_server handle_info/2 Callback
slug: gen-server-handle-info

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
  - "handle_info/2"
  - "out-of-band message callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - behaviour-callback-section
  - message-passing
extends:
  - behaviour-callback-section
related:
  - out-of-band-message
  - gen-server-timeout
  - gen-server-handle-call
  - gen-server-handle-cast
contrasts_with:
  - gen-server-handle-call
  - gen-server-handle-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the gen_server handle_info/2 callback do?"
  - "How does a gen_server handle messages not sent via call or cast?"
  - "Which callback handles timeout messages?"
---

# Quick Definition

`handle_info/2` is the `gen_server` callback for out-of-band messages — any message arriving in the server's mailbox that was not sent with `call` or `cast`, including timeout messages.

# Core Definition

`handle_info/2` handles messages sent to a `gen_server` container that were not sent using one of the `call` or `cast` functions — typically naked messages sent with the plain `!` operator (Ch. 3, Section 3.2.4, Table 3.5). It is the one callback that does not correspond to any `gen_server` library function. Such out-of-band messages arrive when the callback code communicates with a component that uses direct messages — for instance, a socket or a port driver. When a `gen_server` timeout fires, an out-of-band message with the single atom `timeout` is generated and delivered to `handle_info/2`.

# Prerequisites

- **gen_server behaviour** — `handle_info/2` is a `gen_server` callback.
- **Behaviour callback function section** — `handle_info/2` lives in the callback section.
- **Message passing** — Out-of-band messages are plain Erlang messages.

# Key Properties

1. Handles messages not sent via `call` or `cast` (out-of-band messages).
2. The only callback with no corresponding `gen_server` library function.
3. Receives the `timeout` atom message when a server timeout fires.
4. Common for processes interacting with sockets or port drivers.
5. Returns the same kinds of tuples as `handle_cast/2` (`noreply`/`stop`).

# Construction / Recognition

## To Write handle_info/2:
1. Add one clause per kind of out-of-band message.
2. Add a `timeout` clause if the server uses server timeouts.
3. Handle data messages (e.g. `{tcp, Socket, Data}`) from sockets.
4. Return `{noreply, NewState}` or `{stop, Reason, NewState}`.

# Context & Application

`handle_info/2` is where a server deals with the messy outside world — sockets, ports, timers. The book notes you should avoid sending out-of-band messages to a `gen_server` if you can help it.

- **Typical contexts**: Servers owning active sockets or port drivers; deferred initialization via timeout.
- **Common applications**: `tr_server:handle_info/2` has a `timeout` clause (accepts a TCP connection) and a `{tcp, Socket, RawData}` clause (handles RPC data).

# Examples

**Example 1** (Ch. 3, Listing 3.5): `tr_server:handle_info/2` has two clauses — a `timeout` clause that calls `gen_tcp:accept/1`, and a `{tcp, Socket, RawData}` clause that executes the RPC.

**Example 2** (Ch. 6): `sc_element`'s `handle_info/2` receives the lease `timeout` message and shuts the storage process down.

# Relationships

## Builds Upon
- **Behaviour callback function section** — `handle_info/2` is one of its callbacks.

## Related
- **out-of-band-message** — `handle_info/2` is the callback that handles these.
- **gen-server-timeout** — Timeout firing delivers a `timeout` message to `handle_info/2`.

## Contrasts With
- **gen-server-handle-call** / **gen-server-handle-cast** — Those handle `call`/`cast` messages; `handle_info/2` handles everything else.

# Common Errors

- **Error**: Sending naked `!` messages to a `gen_server` when `call`/`cast` would do.
  **Correction**: Avoid out-of-band messages to a `gen_server` unless an external component (socket, port) requires them.

# Common Confusions

- **Confusion**: Expecting `handle_info/2` to have a matching library function like the other callbacks.
  **Clarification**: It is the special case — no library function corresponds to it; it catches everything `call`/`cast` did not send.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "The callback function section" and "Handling out-of-band messages." See Listing 3.5, Table 3.5, and the "gen_server timeout events" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.4.
- Confidence rationale: HIGH — explicit, detailed treatment in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `message-passing` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
