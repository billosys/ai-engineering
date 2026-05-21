---
# === CORE IDENTIFICATION ===
concept: FSM Synchronous Events
slug: fsm-synchronous-events

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: fsm
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Finite State Machines"
chapter_number: 5
pdf_page: 156
section: "Synchronous events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sync_send_event"
  - "gen_fsm:sync_send_event"
  - synchronous FSM events
  - "State/3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fsm-events
extends:
  - fsm-events
related:
  - fsm-send-all-state-events
  - fsm-termination
contrasts_with:
  - fsm-events

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle synchronous versus asynchronous messages in a gen_server?"
  - "How do I implement a finite state machine with gen_statem?"
---

# Quick Definition

A synchronous FSM event is sent with `gen_fsm:sync_send_event/2`, which blocks the caller until the FSM produces a reply; it is handled in the `State(Event, From, LoopData)` callback returning a `{reply, ...}` tuple.

# Core Definition

Synchronous events are used "sometimes [when] we want to ensure clients can't generate a new event until their previous one is handled" (Cesarini & Vinoski, p. 156). They are sent via `sync_send_event/2` (or `sync_send_all_state_event/2`). "This call and its callback are a middle ground between using the `call/2` and `handle_call/3` functions in the generic server and using asynchronous events and event handling in FSMs. Events are handled in the `State(Event, From, LoopData)` callback, where `From` is a tuple denoting the client and the request reference. Instead of returning the `next_state` tuple, the callback returns a tuple of the format `{reply, Reply, NextState, NewLoopData}`. `Reply` is sent back to the client and becomes the return value of the `gen_fsm:sync_send_event/2` call" (p. 156). As with generic servers, you can alternatively use `gen_fsm:reply(From, Reply)` and return a plain `next_state` tuple from the `State/3` callback.

# Prerequisites

- **FSM events** — Synchronous events are the blocking counterpart of asynchronous events; you must understand events first.

# Key Properties

1. Sent via `gen_fsm:sync_send_event(NameScope, Event)` or `sync_send_event/3` (with timeout).
2. Blocks the caller until a reply is produced.
3. Handled in `State(Event, From, LoopData)` — the arity-3 state callback.
4. `From` is a tuple of the client pid and request reference.
5. The callback returns `{reply, Reply, NextState, NewLoopData}` (optionally with `Timeout`/`hibernate`), or a `next_state`/`stop` tuple.
6. `gen_fsm:reply(From, Reply)` can send the reply explicitly, allowing the callback to return a plain `next_state` tuple.
7. `sync_send_all_state_event/2` sends a synchronous request handled regardless of state in `handle_sync_event/4`.

# Construction / Recognition

## To Send a Synchronous Event:
1. Define a client function calling `gen_fsm:sync_send_event(?MODULE, Event)`.
2. Implement the arity-3 state callback `State(Event, From, LoopData)`.
3. Return `{reply, Reply, NextState, NewLoopData}` — or use `gen_fsm:reply/2` and return a `next_state` tuple.

# Context & Application

- **Typical contexts**: When a client must not proceed until the FSM confirms an event was handled.
- **Common applications**: A diagnostic client setting a hardware register and waiting for confirmation; stopping the FSM via `sync_send_all_state_event/2`.
- **Historical/stylistic notes**: The book uses `sync_send_all_state_event/2` to trigger normal termination of the coffee machine "regardless of what state it is in" (p. 157).

# Examples

**Example 1** (p. 156): The book describes a diagnostic client that asks the FSM to "set a particular value into a hardware register and take no further action until the FSM indicates the setting was successful" — a textbook case for `sync_send_event/2`.

**Example 2** (p. 159): Stopping the coffee machine via a synchronous all-state event:

```erlang
stop() -> gen_fsm:sync_send_all_state_event(?MODULE, stop).
handle_sync_event(stop, _From, _State, LoopData) ->
    {stop, normal, LoopData}.
```

# Relationships

## Builds Upon
- **FSM events** — Synchronous events are the blocking variant of FSM events.

## Enables
- **fsm-termination** — `sync_send_all_state_event/2` is used to trigger orderly FSM termination.

## Related
- **fsm-send-all-state-events** — `sync_send_all_state_event/2` is the synchronous all-state variant.

## Contrasts With
- **FSM events** — Asynchronous `send_event/2` returns `ok` immediately; `sync_send_event/2` blocks the caller until a reply is produced.

# Common Errors

- **Error**: Using `sync_send_event/2` for events that need no reply, needlessly serializing clients.
  **Correction**: Use asynchronous `send_event/2` unless the client genuinely must wait for confirmation.

# Common Confusions

- **Confusion**: Thinking the `stop` passed through `sync_send_all_state_event/2` is interpreted by `gen_fsm`.
  **Clarification**: That `stop` is just an application term with no built-in meaning; only the `{stop, Reason, LoopData}` *control tuple* returned by the callback is interpreted by the behavior.

# Source Reference

Chapter 5: Finite State Machines, Section "Synchronous events," pages 156-157; termination example on page 159.

# Verification Notes

- Definition source: Direct quotes from p. 156.
- Confidence rationale: HIGH — the source explicitly defines the synchronous call, its callback, and return tuples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
