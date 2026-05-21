---
# === CORE IDENTIFICATION ===
concept: FSM Events
slug: fsm-events

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
pdf_page: 148
section: "Sending Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - asynchronous events
  - "send_event"
  - "gen_fsm:send_event"
  - FSM message

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-fsm-behavior
  - fsm-states-and-state-functions
extends: []
related:
  - fsm-state-transitions
  - fsm-synchronous-events
  - fsm-send-all-state-events
contrasts_with:
  - fsm-synchronous-events

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "How do I handle synchronous versus asynchronous messages in a gen_server?"
---

# Quick Definition

An FSM event is a message sent to an FSM that triggers handling in the current state's callback function; asynchronous events are sent with `gen_fsm:send_event/2`, which returns `ok` immediately.

# Core Definition

Events drive an FSM: when handled, "they trigger state transitions. Events are usually sent in client functions defined in the callback module" (Cesarini & Vinoski, p. 148). Asynchronous events are sent using `gen_fsm:send_event(Name, Event)`, which "sends the `Event` to the FSM, which handles it in the callback function `State(Event, LoopData)` in the callback module. After handling the request, the `State/2` function returns the new loop data with the `next_state` or the `stop` reason" (p. 148). Events need not comprise only static values — a variable can be embedded, as in `{pay, Coin}` where the inserted coin's value is bound. The book recommends collecting all client functions that generate events in one place in the callback module, even though this is not mandatory (p. 146).

# Prerequisites

- **Generic FSM behavior** — Events are sent to a `gen_fsm` process; you must understand the behavior.
- **FSM states and state functions** — An event is dispatched to the current state's callback function.

# Key Properties

1. An event is a message sent to the FSM.
2. Asynchronous events are sent with `gen_fsm:send_event(Name, Event)`, which returns `ok` immediately.
3. The event is handled in `State(Event, LoopData)` in the callback module.
4. Events can carry data — static tags or runtime-bound values.
5. Events are handled first-in, first-out (FIFO) and removed from the mailbox when read.
6. The callback returns `{next_state, NextState, NewLoopData}` (optionally with `Timeout`/`hibernate`) or `{stop, Reason, NewLoopData}`.

# Construction / Recognition

## To Send an Asynchronous Event:
1. Define a client function in the callback module.
2. Have it call `gen_fsm:send_event(?MODULE, Event)`.
3. The event is delivered to the current state's `State/2` callback.

## To Recognize Event Handling:
1. Look for `gen_fsm:send_event/2` calls in client functions.
2. Look for `*DBG* ... got event ... in state ...` trace lines.

# Context & Application

- **Typical contexts**: Any interaction with a running FSM that does not need a reply.
- **Common applications**: The coffee machine's `tea/0`, `espresso/0`, `pay/1`, `cancel/0`, `cup_removed/0` client functions.
- **Historical/stylistic notes**: All events in the coffee machine example are asynchronous; the book later contrasts this with synchronous events for cases needing a reply (p. 154).

# Examples

**Example 1** (p. 148): Drink-selection client functions sending asynchronous events:

```erlang
tea()       -> gen_fsm:send_event(?MODULE, {selection, tea, 100}).
espresso()  -> gen_fsm:send_event(?MODULE, {selection, espresso, 100}).
americano() -> gen_fsm:send_event(?MODULE, {selection, americano, 150}).
cappuccino()-> gen_fsm:send_event(?MODULE, {selection, cappuccino, 150}).
```

**Example 2** (p. 149): Action client functions, where `pay/1` embeds a runtime variable in the event:

```erlang
pay(Coin)     -> gen_fsm:send_event(?MODULE, {pay, Coin}).
cancel()      -> gen_fsm:send_event(?MODULE, cancel).
cup_removed() -> gen_fsm:send_event(?MODULE, cup_removed).
```

# Relationships

## Builds Upon
- **Generic FSM behavior** — Events are the input mechanism of `gen_fsm`.

## Enables
- **fsm-state-transitions** — Handling an event produces a transition.

## Related
- **FSM states and state functions** — Events are dispatched to state functions.
- **fsm-send-all-state-events** — A variant for events handled regardless of state.

## Contrasts With
- **fsm-synchronous-events** — Asynchronous events return `ok` immediately; synchronous events block the caller until a reply is produced.

# Common Errors

- **Error**: Relying on selective receive to reorder out-of-sequence events with `gen_fsm`.
  **Correction**: `gen_fsm` handles events strictly FIFO and removes them when read; it does not provide selective receive. Buffer out-of-sequence events in loop data or add a state.

# Common Confusions

- **Confusion**: Thinking events must be static, fixed values.
  **Clarification**: Events can carry runtime data; the source explicitly notes `{pay, Coin}` binds a variable into the event.

# Source Reference

Chapter 5: Finite State Machines, Section "Sending Events" / "Asynchronous events," pages 148-149.

# Verification Notes

- Definition source: Direct quotes from pp. 148-149.
- Confidence rationale: HIGH — the source explicitly defines events, the send function, and provides client-function examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
