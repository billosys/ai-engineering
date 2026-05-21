---
# === CORE IDENTIFICATION ===
concept: gen_server:cast
slug: gen-server-cast

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
  - "gen_server:cast/2"
  - asynchronous message

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - message-passing
extends:
  - gen-server
related:
  - gen-server-handle-cast
  - gen-server-call
  - gen-server-start-link
contrasts_with:
  - gen-server-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does gen_server:cast do?"
  - "How do you send an asynchronous message to a gen_server?"
  - "When should I use cast instead of call?"
---

# Quick Definition

`gen_server:cast/2` sends an asynchronous message to a `gen_server` process; it returns immediately without waiting for any reply.

# Core Definition

`gen_server:cast/2` sends an asynchronous message to a `gen_server` process (Ch. 3, Table 3.3). The function returns immediately without waiting for a reply. The first argument is the registered name or pid of the server; the second is the message payload. Its associated callback is `Module:handle_cast/2`. `cast` is used when no reply is needed — for example, a `stop` command where the caller assumes the container will shut itself down on receiving the message.

# Prerequisites

- **gen_server behaviour** — `cast` is a `gen_server` library function.
- **Message passing** — `cast` is built on asynchronous Erlang message passing.

# Key Properties

1. Sends an asynchronous message; the caller does not wait.
2. Returns immediately, with no reply value from the server.
3. Its associated callback is `Module:handle_cast/2`.
4. The payload is automatically wrapped with dispatch metadata.
5. Used for fire-and-forget commands such as `stop`, `replace`, `delete`.

# Construction / Recognition

## To Use cast:
1. Call `gen_server:cast(ServerRef, Message)`.
2. Pass the registered name or pid as `ServerRef`.
3. Use it only when no return value is needed.
4. Wrap it in an API function so the message format stays hidden.

# Context & Application

`cast` is used for commands and updates where the caller does not need an answer and should not be blocked.

- **Typical contexts**: Stop commands, state updates, deletions.
- **Common applications**: `tr_server:stop/0` uses `gen_server:cast(?SERVER, stop)`; `sc_element:replace/2` and `delete/1` use `cast`.

# Examples

**Example 1** (Ch. 3): `stop()` uses `gen_server:cast(?SERVER, stop)`; the function returns immediately and the container shuts itself down on receiving the message.

**Example 2** (Ch. 6): `sc_element:replace/2` and `delete/1` use asynchronous `cast` because neither needs a reply.

# Relationships

## Builds Upon
- **gen_server behaviour** — `cast` is one of its library functions.

## Enables
- **gen-server-handle-cast** — `cast` triggers the `handle_cast/2` callback.

## Contrasts With
- **gen-server-call** — `cast` is asynchronous and returns immediately; `call` is synchronous and waits for a reply.

# Common Errors

- **Error**: Using `cast` when the caller actually needs the result.
  **Correction**: Use `call` for operations whose result the caller depends on.

# Common Confusions

- **Confusion**: Thinking `cast` confirms the message was handled.
  **Clarification**: `cast` only sends; it returns before the server processes the message and gives no acknowledgement.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.3 "The API section." See Listing 3.3, Tables 3.3 and 3.5.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.3 and Table 3.3.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `message-passing` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
