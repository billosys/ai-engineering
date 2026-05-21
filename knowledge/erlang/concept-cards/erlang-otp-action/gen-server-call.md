---
# === CORE IDENTIFICATION ===
concept: gen_server:call
slug: gen-server-call

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
section: "3.2.3 The API section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:call/2"
  - "gen_server:call/3"
  - synchronous call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - message-passing
extends:
  - gen-server
related:
  - gen-server-handle-call
  - gen-server-cast
  - gen-server-start-link
contrasts_with:
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does gen_server:call do?"
  - "How do you send a synchronous request to a gen_server?"
  - "What is the default timeout of gen_server:call?"
---

# Quick Definition

`gen_server:call/2` sends a synchronous message to a `gen_server` process and waits for a reply, suspending the caller until the answer arrives (or a timeout fires).

# Core Definition

`gen_server:call/2` sends a synchronous message to a `gen_server` process and waits for a reply (Ch. 3, Table 3.3). It implements synchronous request-reply in a reliable way, with a default timeout of 5 seconds before it gives up; the three-argument variant `gen_server:call/3` lets you specify a timeout in milliseconds, or `infinity`. The first argument is the registered name or pid of the server; the second is the message payload. The associated callback is `Module:handle_call/3`. The OTP libraries automatically wrap the payload with metadata so the container knows which callback handles it and how to reply.

# Prerequisites

- **gen_server behaviour** — `call` is a `gen_server` library function.
- **Message passing** — `call` is built on Erlang message passing, made synchronous.

# Key Properties

1. Sends a synchronous request and waits for a reply.
2. Temporarily suspends the calling process until the reply arrives.
3. Default timeout is 5 seconds; `call/3` allows a custom timeout or `infinity`.
4. Its associated callback is `Module:handle_call/3`.
5. The payload is automatically wrapped with reply-routing metadata.

# Construction / Recognition

## To Use call:
1. Call `gen_server:call(ServerRef, Message)`.
2. Pass the registered name or pid as `ServerRef`.
3. Use `call/3` if you need a non-default timeout.
4. Wrap it in an API function so the message format stays hidden.

# Context & Application

`call` is used whenever the client needs an answer — a query, a fetch — and cannot proceed without it.

- **Typical contexts**: Read operations, queries, anything requiring a return value.
- **Common applications**: `tr_server:get_count/0` uses `gen_server:call(?SERVER, get_count)`; `sc_element:fetch/1` uses `call` to get the stored value.

# Examples

**Example 1** (Ch. 3): `get_count()` calls `gen_server:call(?SERVER, get_count)`, suspending the caller until the server replies with `{ok, N}`.

**Example 2** (Ch. 6): `sc_element:fetch/1` uses `call` because it must wait for the stored value to be returned.

# Relationships

## Builds Upon
- **gen_server behaviour** — `call` is one of its library functions.

## Enables
- **gen-server-handle-call** — `call` triggers the `handle_call/3` callback.

## Contrasts With
- **gen-server-cast** — `call` is synchronous and waits for a reply; `cast` is asynchronous and returns immediately.

# Common Errors

- **Error**: Having a server call itself with `gen_server:call` from inside a callback.
  **Correction**: This deadlocks — the request queues behind the running callback; a server cannot call itself.

- **Error**: Using `call` for operations that exceed the 5-second default timeout.
  **Correction**: Use `call/3` with a longer timeout or `infinity`.

# Common Confusions

- **Confusion**: Thinking the message you pass is the actual message sent on the wire.
  **Clarification**: It is only the payload; OTP wraps it with metadata for dispatch and reply routing.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.3 "The API section." See Listing 3.3, Tables 3.3 and 3.5, and the "Double blind" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.3 and Table 3.3.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `message-passing` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
