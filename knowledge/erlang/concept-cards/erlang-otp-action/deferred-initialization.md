---
# === CORE IDENTIFICATION ===
concept: Deferred Initialization
slug: deferred-initialization

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: generic-server
tier: advanced

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
  - "zero-timeout trick"
  - "deferred startup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server-init
  - gen-server-timeout
  - gen-server-handle-info
extends:
  - gen-server-timeout
related:
  - gen-server-start-link
  - out-of-band-message
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is deferred initialization in a gen_server?"
  - "How do you do slow startup work without blocking the start_link caller?"
  - "Why return a 0 timeout from init/1?"
---

# Quick Definition

Deferred initialization is a `gen_server` technique in which `init/1` returns a `0` timeout so that slow startup work happens in `handle_info/2` instead of blocking the `start_link` caller.

# Core Definition

Deferred initialization is the book's term for a well-known trick: `init/1` returns a `0` server timeout, which triggers an immediate timeout message, so the `handle_info/2` timeout clause runs as the first thing after initialization (Ch. 3, Section 3.2.4). This lets `init/1` finish quickly so the caller of `start_link(...)` is not left hanging, while still making the server immediately jump to a specific piece of code where it can perform the time-consuming part of startup — in the RPC server's case, waiting for a connection on a listening socket.

# Prerequisites

- **gen_server init/1 callback** — The `0` timeout is returned from `init/1`.
- **gen_server server timeout** — The mechanism that fires the immediate timeout.
- **gen_server handle_info/2 callback** — Receives the timeout and does the deferred work.

# Key Properties

1. `init/1` returns a `0` timeout in its return tuple.
2. The `0` timeout fires immediately, producing a `timeout` message.
3. The slow startup work runs in the `handle_info/2` timeout clause.
4. `init/1` finishes quickly, so `start_link` returns promptly.
5. It is a deliberate (well-known) use of the server-timeout mechanism.

# Construction / Recognition

## To Defer Initialization:
1. Do only the fast setup in `init/1`.
2. Return `{ok, State, 0}` — the `0` schedules an immediate timeout.
3. Put the slow startup work in the `timeout` clause of `handle_info/2`.

# Context & Application

Deferred initialization keeps the `start_link` caller (and any supervisor waiting on it) unblocked while a server that needs slow startup work still gets that work done first.

- **Typical contexts**: Servers whose startup includes blocking operations such as `accept` on a socket.
- **Common applications**: `tr_server` defers waiting for a TCP connection (`gen_tcp:accept/1`) into `handle_info/2`.

# Examples

**Example 1** (Ch. 3): `tr_server:init/1` creates the listening socket then returns `{ok, #state{...}, 0}`; the immediate timeout makes `handle_info/2` call `gen_tcp:accept/1` — slow work moved out of `init/1`.

# Relationships

## Builds Upon
- **gen_server server timeout** — Deferred initialization is a specific use of the timeout mechanism.

## Related
- **gen-server-start-link** — `start_link` blocks on `init/1`; deferring keeps that block short.
- **out-of-band-message** — The deferred work is triggered by an out-of-band `timeout` message.

## Contrasts With
- This is a technique; the source draws no direct contrast.

# Common Errors

- **Error**: Doing the slow startup work directly in `init/1`.
  **Correction**: Return a `0` timeout and move the slow work to `handle_info/2`.

# Common Confusions

- **Confusion**: Thinking the `0` timeout means "no timeout."
  **Clarification**: A `0` timeout fires immediately; `infinity` means no timeout.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "Handling out-of-band messages." See Listings 3.4 and 3.5.

# Verification Notes

- Definition source: Direct adaptation of the deferred-initialization discussion in Section 3.2.4.
- Confidence rationale: HIGH — the source explicitly describes and names this trick.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
