---
# === CORE IDENTIFICATION ===
concept: gen_server:cast (Asynchronous Cast)
slug: gen-server-cast

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Calls and Casts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:cast"
  - "cast"
  - "asynchronous cast"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-callbacks
extends: []
related:
  - gen-server-call
  - handle-info
contrasts_with:
  - gen-server-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_server:cast?"
  - "What is the difference between a call and a cast?"
---

# Quick Definition

`gen_server:cast(Name, Msg)` sends an asynchronous message to a gen_server with no return value. It invokes `handle_cast/2` in the callback module; the sender does not wait.

# Core Definition

"`gen_server:cast(Name, Msg)` implements a *cast*, which is just a call with no return value (actually just a message, but traditionally it's called a cast to distinguish it from a remote procedure call)" (Programming Erlang, "Calls and Casts"). The corresponding callback routine is `handle_cast(Msg, State)`. The handler "usually just returns `{noreply, NewState}`, which changes the state of the server, or `{stop, ...}`, which stops the server." Where `gen_server:call` is used for synchronous remote procedure calls, `cast` is used for fire-and-forget messages.

# Prerequisites

- **gen_server** — `cast` is part of the gen_server client API.
- **gen_server callbacks** — `cast` triggers the `handle_cast/2` callback.

# Key Properties

1. Asynchronous: the sender does not block and gets no return value.
2. `Msg` becomes the first argument of `handle_cast/2`.
3. `handle_cast/2` normally returns `{noreply, NewState}`; `{stop, Reason, State}` stops the server.
4. Used relatively less frequently than `call` in the simple use of gen_server.
5. Technically just a message, named "cast" to distinguish it from a remote procedure call.

# Construction / Recognition

## To Use gen_server:cast:
1. Write an interface function calling `gen_server:cast(ServerName, MsgTerm)`.
2. In the callback module, write a `handle_cast(MsgTerm, State)` clause.
3. Return `{noreply, NewState}` to continue with the updated state.

## To Recognize:
1. An interface function delegating to `gen_server:cast` performs an asynchronous send.
2. A `handle_cast/2` clause is the server-side counterpart of a cast.

# Context & Application

- **Typical contexts**: Notifications and state changes that need no acknowledgement.
- **Common applications**: The mini-template and `my_bank` provide the default `handle_cast(_Msg, State) -> {noreply, State}.` since the bank uses only calls.
- **Historical/stylistic notes**: The book covers the simplest use of gen_server, where casts appear "relatively infrequently."

# Examples

**Example 1** ("Filling in the gen_server Template"): `my_bank` provides the do-nothing default cast handler: `handle_cast(_Msg, State) -> {noreply, State}.`

**Example 2** ("Calls and Casts"): The template entry for `handle_cast` documents its return values as `{noreply, State}`, `{noreply, State, Timeout}`, or `{stop, Reason, State}`.

# Relationships

## Builds Upon
- **gen_server** — `cast` is part of the gen_server client API.

## Enables
- **gen_server callbacks** — `cast` invokes `handle_cast/2`.

## Related
- **handle_info** — handles messages arriving by neither `call` nor `cast`.

## Contrasts With
- **gen_server:call** — `call` is synchronous and returns a reply; `cast` is asynchronous with no return value.

# Common Errors

- **Error**: Using `cast` when the caller needs the result.
  **Correction**: `cast` returns nothing; use `call` when a reply is required.

- **Error**: Returning a `{reply, ...}` tuple from `handle_cast/2`.
  **Correction**: `handle_cast/2` returns `{noreply, State}` or `{stop, ...}` — there is no client awaiting a reply.

# Common Confusions

- **Confusion**: Thinking a cast guarantees the message was processed.
  **Clarification**: A cast is fire-and-forget; the sender gets no acknowledgement that the server handled it.

- **Confusion**: Believing cast and call differ only in name.
  **Clarification**: `call` blocks for a reply and invokes `handle_call/3`; `cast` does not block and invokes `handle_cast/2`.

# Source Reference

Chapter 22: Introducing OTP, section "Calls and Casts" (within "The gen_server Callback Structure"). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "Calls and Casts".
- Confidence rationale: HIGH — explicitly defined and templated in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
