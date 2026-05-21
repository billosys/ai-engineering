---
# === CORE IDENTIFICATION ===
concept: gen_server handle_cast/2 Callback
slug: gen-server-handle-cast

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
  - "handle_cast/2"
  - "callback for asynchronous messages"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-cast
  - behaviour-callback-section
extends:
  - behaviour-callback-section
related:
  - gen-server-handle-call
  - gen-server-handle-info
contrasts_with:
  - gen-server-handle-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the gen_server handle_cast/2 callback do?"
  - "How does a gen_server handle asynchronous messages?"
  - "How do you make a gen_server stop from handle_cast/2?"
---

# Quick Definition

`handle_cast/2` is the `gen_server` callback for asynchronous messages; it is invoked for every message sent with `gen_server:cast/2` and sends no reply.

# Core Definition

`handle_cast/2` is the callback for asynchronous messages (Ch. 3, Section 3.2.4). Any message sent using `gen_server:cast/2` is handled by `handle_cast/2`. It is similar to `handle_call/3` except there is no `From` argument, because no reply is expected. It returns a 2-or-3-tuple: `{noreply, NewState}` to continue running, or `{stop, Reason, NewState}` to terminate the server. A `Reason` of `normal` indicates a graceful shutdown.

# Prerequisites

- **gen_server behaviour** — `handle_cast/2` is a `gen_server` callback.
- **gen_server:cast** — `cast` is what triggers `handle_cast/2`.
- **Behaviour callback function section** — `handle_cast/2` lives in the callback section.

# Key Properties

1. Invoked for every message sent via `gen_server:cast/2`.
2. Takes two arguments: the message and the current state — no `From`.
3. Sends no reply.
4. Returns `{noreply, NewState}` to continue or `{stop, Reason, NewState}` to terminate.
5. A `stop` tuple with reason `normal` signals a graceful shutdown.

# Construction / Recognition

## To Write handle_cast/2:
1. Pattern-match the message in the first argument (one clause per message).
2. Update the state as needed.
3. Return `{noreply, NewState}` to keep running, or `{stop, normal, State}` to shut down.

# Context & Application

`handle_cast/2` handles fire-and-forget commands and updates.

- **Typical contexts**: Stop commands, state updates, deletions.
- **Common applications**: `tr_server:handle_cast/2` handles `stop` by returning `{stop, normal, State}`; `sc_element`'s `handle_cast/2` handles `replace` (`noreply`) and `delete` (`stop`).

# Examples

**Example 1** (Ch. 3): For the `stop` message, `handle_cast/2` returns `{stop, normal, State}`, telling the container to terminate gracefully.

**Example 2** (Ch. 6): `sc_element`'s `handle_cast/2` returns `noreply` for `{replace, Value}` (server stays alive with new state) and `stop` for `delete` (server shuts down).

# Relationships

## Builds Upon
- **Behaviour callback function section** — `handle_cast/2` is one of its callbacks.

## Related
- **gen-server-cast** — `cast` triggers `handle_cast/2`.
- **gen-server-handle-info** — Handles out-of-band messages instead.

## Contrasts With
- **gen-server-handle-call** — `handle_cast/2` has no `From` and sends no reply; `handle_call/3` has `From` and replies.

# Common Errors

- **Error**: Trying to reply to the caller from `handle_cast/2`.
  **Correction**: `cast` messages have no caller waiting; use `call`/`handle_call` if a reply is needed.

# Common Confusions

- **Confusion**: Confusing the `stop` atom in the message with the `stop` atom in the return tuple.
  **Clarification**: The message atom could be anything; the `stop` in the return tuple is what instructs the container to terminate.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "The callback function section." See Listing 3.4 and Table 3.5.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.4.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
