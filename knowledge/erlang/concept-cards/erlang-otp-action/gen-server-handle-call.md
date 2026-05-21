---
# === CORE IDENTIFICATION ===
concept: gen_server handle_call/3 Callback
slug: gen-server-handle-call

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
  - "handle_call/3"
  - "callback for synchronous requests"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-call
  - behaviour-callback-section
extends:
  - behaviour-callback-section
related:
  - gen-server-handle-cast
  - gen-server-handle-info
  - gen-server-init
contrasts_with:
  - gen-server-handle-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the gen_server handle_call/3 callback do?"
  - "How does a gen_server reply to a synchronous request?"
  - "What does handle_call/3 return?"
---

# Quick Definition

`handle_call/3` is the `gen_server` callback for synchronous requests; it is invoked every time a message sent with `gen_server:call/2` arrives, and it produces the reply.

# Core Definition

`handle_call/3` is the callback for synchronous requests, invoked every time a message is received that was sent using `gen_server:call/2` (Ch. 3, Section 3.2.4). It takes three arguments: the message (as passed to `call`), `From` (information identifying the caller), and the current server state. It typically returns a 3-tuple `{reply, Reply, NewState}`, which tells the container to send `Reply` back to the caller and continue with `NewState`. A `handle_call/3` clause may also return a `stop` tuple to shut the server down.

# Prerequisites

- **gen_server behaviour** — `handle_call/3` is a `gen_server` callback.
- **gen_server:call** — `call` is what triggers `handle_call/3`.
- **Behaviour callback function section** — `handle_call/3` lives in the callback section.

# Key Properties

1. Invoked for every message sent via `gen_server:call/2`.
2. Takes three arguments: the message, `From`, and the current state.
3. Typically returns `{reply, Reply, NewState}`.
4. The `Reply` element becomes the return value of the client's `call`.
5. May return a `stop` tuple to terminate the server.

# Construction / Recognition

## To Write handle_call/3:
1. Pattern-match the message in the first argument (one clause per message).
2. Compute the reply, often by reading the state.
3. Return `{reply, Reply, NewState}` — keep the state unchanged if nothing changed.

# Context & Application

`handle_call/3` handles read-style and any reply-requiring operations.

- **Typical contexts**: Queries, fetches, status checks.
- **Common applications**: `tr_server:handle_call/3` handles `get_count`, returning `{reply, {ok, Count}, State}`; `sc_element`'s `handle_call/3` handles `fetch`.

# Examples

**Example 1** (Ch. 3): For the `get_count` message, `handle_call/3` returns `{reply, {ok, State#state.request_count}, State}` — replying with the count and leaving state unchanged.

**Example 2** (Ch. 6): `sc_element`'s `handle_call/3` matches `fetch`, returns the stored value as `{ok, Value}`, and recomputes the lease timeout.

# Relationships

## Builds Upon
- **Behaviour callback function section** — `handle_call/3` is one of its callbacks.

## Related
- **gen-server-call** — `call` triggers `handle_call/3`.
- **gen-server-handle-info** — Handles out-of-band messages instead.

## Contrasts With
- **gen-server-handle-cast** — `handle_call/3` has a `From` argument and sends a reply; `handle_cast/2` has no `From` and sends no reply.

# Common Errors

- **Error**: Not sending a reply for a `call`-style message.
  **Correction**: Return a `{reply, ...}` tuple — the caller expects an answer.

# Common Confusions

- **Confusion**: Thinking `handle_call/3` can ignore the `From` argument freely.
  **Clarification**: `From` identifies the caller; advanced patterns (e.g. deferred replies via `gen_server:reply`) need it.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "The callback function section." See Listing 3.4 and Table 3.5.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.4.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
