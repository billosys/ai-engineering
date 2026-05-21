---
# === CORE IDENTIFICATION ===
concept: handle_info (Spontaneous Messages)
slug: handle-info

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
section: "Spontaneous Messages to the Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "handle_info/2"
  - "spontaneous messages"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-callbacks
  - message-passing
extends: []
related:
  - gen-server-call
  - gen-server-cast
  - link
contrasts_with:
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is handle_info?"
  - "How does a gen_server handle messages not sent by call or cast?"
---

# Quick Definition

`handle_info(Info, State)` is the gen_server callback for spontaneous messages — any message arriving at the server that was not sent via `gen_server:call` or `gen_server:cast`.

# Core Definition

"The callback function `handle_info(Info, State)` is used for handling spontaneous messages to the server. Spontaneous messages are any messages that arrive at the server that were not sent by explicitly calling `gen_server:call` or `gen_server:cast`" (Programming Erlang, "Spontaneous Messages to the Server"). For example, if the server is linked to another process and is trapping exits, it might suddenly receive an unexpected `{'EXIT', Pid, What}` message. Alternatively, any process that discovers the server's PID can send it a message directly. Any such message ends up at the server as the value of `Info`. The return values are the same as for `handle_cast`: `{noreply, State}`, `{noreply, State, Timeout}`, or `{stop, Reason, State}`.

# Prerequisites

- **gen_server** — `handle_info` is one of the gen_server callbacks.
- **gen_server callbacks** — it is one of the six required functions.
- **Message passing** — spontaneous messages arrive via ordinary `!` sends.

# Key Properties

1. Handles only messages NOT sent through `gen_server:call` or `gen_server:cast`.
2. The arriving message becomes the value of `Info`.
3. Typical sources: `{'EXIT', Pid, What}` from a linked process; raw messages from any process holding the server's PID.
4. Return values are identical to `handle_cast/2`.
5. A default no-op clause `handle_info(_Info, State) -> {noreply, State}.` is common when the server expects no spontaneous messages.

# Construction / Recognition

## To Use handle_info:
1. Decide what spontaneous messages the server may receive (e.g. exit signals, timer messages).
2. Write a `handle_info(Pattern, State)` clause for each.
3. Return `{noreply, NewState}` to continue, or `{stop, Reason, State}` to terminate.

## To Recognize:
1. A `handle_info/2` clause matching `{'EXIT', _, _}` indicates the server handles linked-process failures.

# Context & Application

- **Typical contexts**: Servers that link to or monitor other processes, or that receive timer/system messages.
- **Common applications**: Catching `{'EXIT', Pid, What}` when the server traps exits; receiving ad-hoc messages from processes that know its PID.
- **Historical/stylistic notes**: `prime_server` and `area_server` keep the default no-op `handle_info` because they expect no spontaneous messages.

# Examples

**Example 1** ("Filling in the gen_server Template"): `my_bank` keeps the default `handle_info(_Info, State) -> {noreply, State}.` because no spontaneous messages are expected.

**Example 2** ("Spontaneous Messages to the Server"): The book's worked case — a server linked to another process and trapping exits "might suddenly receive an unexpected `{'EXIT', Pid, What}` message," which arrives at `handle_info/2` as `Info`.

# Relationships

## Builds Upon
- **gen_server** — `handle_info` is part of the gen_server callback contract.

## Enables
- **gen_server callbacks** — `handle_info` is one of the six required callbacks.

## Related
- **gen_server:call** — `handle_info` catches what does *not* arrive via `call`.
- **link** — linked processes' `{'EXIT', ...}` signals surface in `handle_info`.

## Contrasts With
- **gen_server:cast** — casts are delivered to `handle_cast`; spontaneous (non-cast) messages go to `handle_info`.

# Common Errors

- **Error**: Assuming all incoming messages reach `handle_call` or `handle_cast`.
  **Correction**: Messages sent by plain `!` (including exit signals) reach `handle_info/2`.

- **Error**: Omitting a catch-all `handle_info` clause, causing the server to crash on unexpected messages.
  **Correction**: Provide a default `handle_info(_Info, State) -> {noreply, State}.` clause.

# Common Confusions

- **Confusion**: Thinking `handle_info` handles casts.
  **Clarification**: Casts go to `handle_cast/2`; `handle_info/2` handles only messages that bypassed both `call` and `cast`.

- **Confusion**: Believing exit signals are automatically handled by gen_server.
  **Clarification**: If the server traps exits, `{'EXIT', ...}` signals arrive as ordinary messages at `handle_info/2`.

# Source Reference

Chapter 22: Introducing OTP, section "Spontaneous Messages to the Server" (within "The gen_server Callback Structure"). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "Spontaneous Messages to the Server".
- Confidence rationale: HIGH — explicitly defined in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
