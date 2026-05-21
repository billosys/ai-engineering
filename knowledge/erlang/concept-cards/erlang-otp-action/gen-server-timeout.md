---
# === CORE IDENTIFICATION ===
concept: gen_server Server Timeout
slug: gen-server-timeout

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
  - server timeout
  - "gen_server timeout event"
  - timeout event

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-handle-info
extends:
  - gen-server
related:
  - gen-server-init
  - out-of-band-message
  - deferred-initialization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a gen_server server timeout?"
  - "How does a gen_server timeout event work?"
  - "What happens when a gen_server timeout fires?"
---

# Quick Definition

A `gen_server` server timeout is a per-callback timeout value that, when it expires, generates an out-of-band `timeout` message delivered to `handle_info/2`.

# Core Definition

When a `gen_server` has set a timeout and that timeout triggers, an out-of-band message with the single atom `timeout` is generated, and the `handle_info/2` callback is invoked to handle it (Ch. 3, "gen_server timeout events" sidebar). The timeout is set as an extra element in a callback's return tuple (e.g. the third element of `init/1`'s `{ok, State, Timeout}`). A timeout of `0` triggers an immediate timeout. The mechanism is usually used to make servers wake up and take some action if they have received no requests within the timeout period. If a callback omits the timeout value, the timeout reverts to `infinity`.

# Prerequisites

- **gen_server behaviour** — Server timeouts are a `gen_server` feature.
- **gen_server handle_info/2 callback** — The timeout message is delivered to `handle_info/2`.

# Key Properties

1. Set as an extra element in a callback's return tuple.
2. When it expires, an out-of-band `timeout` message is generated.
3. The `timeout` message is delivered to `handle_info/2`.
4. A timeout of `0` triggers an immediate timeout.
5. If a callback omits the timeout, it reverts to `infinity`.

# Construction / Recognition

## To Use a Server Timeout:
1. Add a timeout value as the extra tuple element in `init/1` or another callback's return.
2. Add a `timeout` clause to `handle_info/2`.
3. Re-specify the timeout in every clause of every callback if you rely on it continuously.

# Context & Application

Server timeouts let a server take action on inactivity, or — using a `0` timeout — defer slow startup work out of `init/1`.

- **Typical contexts**: Idle-timeout actions; deferred initialization; lease/expiry management.
- **Common applications**: `tr_server` uses a `0` timeout for deferred initialization (accepting a connection); `sc_element` uses the timeout to expire cache entries when their lease runs out.

# Examples

**Example 1** (Ch. 3): `tr_server:init/1` returns a `0` timeout so a `timeout` message immediately hits `handle_info/2`, where the server waits for a TCP connection — deferred initialization.

**Example 2** (Ch. 6): `sc_element` sets the server timeout to the remaining lease time; if the process is not accessed within the lease, the `timeout` message reaches `handle_info/2`, which shuts it down.

# Relationships

## Builds Upon
- **gen_server behaviour** — Server timeouts are part of `gen_server`.

## Related
- **gen-server-init** — A `0` timeout from `init/1` triggers immediate deferred work.
- **out-of-band-message** — The `timeout` message is an out-of-band message.
- **deferred-initialization** — Built using a `0` server timeout.

## Contrasts With
- This is a mechanism; the source draws no direct contrast.

# Common Errors

- **Error**: Forgetting to return the timeout value in some callback clause when you rely on timeouts.
  **Correction**: Re-specify the timeout in every clause of every callback; otherwise it reverts to `infinity`.

# Common Confusions

- **Confusion**: Thinking the `timeout` message goes to `handle_call` or `handle_cast`.
  **Clarification**: Timeout events are out-of-band messages and always go to `handle_info/2`.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4, "gen_server timeout events" sidebar. Chapter 6: "Setting server timeouts" sidebar in Section 6.4.1.

# Verification Notes

- Definition source: Direct adaptation of the "gen_server timeout events" and "Setting server timeouts" sidebars.
- Confidence rationale: HIGH — explicit definition in dedicated sidebars.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
