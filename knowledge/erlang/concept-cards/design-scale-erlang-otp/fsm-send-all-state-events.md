---
# === CORE IDENTIFICATION ===
concept: FSM Send-All-State Events
slug: fsm-send-all-state-events

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
pdf_page: 155
section: "Asynchronous events to all states"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "send_all_state_event"
  - all-state events
  - "handle_event/3"
  - "handle_sync_event/4"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fsm-events
extends:
  - fsm-events
related:
  - fsm-synchronous-events
  - fsm-termination
contrasts_with:
  - fsm-events

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

A send-all-state event is an FSM event delivered to a single `handle_event/3` (or synchronous `handle_sync_event/4`) callback regardless of the FSM's current state, instead of to a per-state callback.

# Core Definition

"If you want to send an asynchronous event but are not concerned about the state in which it is received, you can use the `send_all_state_event/2` call" (Cesarini & Vinoski, p. 155). The event is "passed as the first argument to the `handle_event/3` callback function, which executes the actions and then returns the `{next_state, NextState, NewLoopData}` tuple back to the `gen_fsm` control loop" (pp. 155-156). The synchronous counterpart is `sync_send_all_state_event/2`, handled in `handle_sync_event/4`. As with generic servers, the `handle_info/3` callback handles all non-OTP-compliant messages — exit signals, monitors, and messages sent with `Pid ! Msg` — returning the same range of control tuples as `handle_event/3` and `State/2` (p. 156).

# Prerequisites

- **FSM events** — Send-all-state events are a state-independent variant of ordinary FSM events.

# Key Properties

1. `gen_fsm:send_all_state_event(NameScope, Event)` sends an asynchronous event handled regardless of state.
2. Handled in the single `handle_event/3` callback, not in per-state functions.
3. `gen_fsm:sync_send_all_state_event/2` is the synchronous counterpart, handled in `handle_sync_event/4`.
4. `handle_event/3` returns `{next_state, NextState, NewLoopData}` (optionally with `Timeout`/`hibernate`) or `{stop, Reason, NewLoopData}`.
5. `handle_info/3` handles all non-OTP messages (exit signals, monitors, `Pid ! Msg`) and returns the same control tuples.

# Construction / Recognition

## To Send an All-State Event:
1. Define a client function calling `gen_fsm:send_all_state_event(?MODULE, Event)`.
2. Implement `handle_event(Event, StateName, LoopData)` to perform the actions.
3. Return a `next_state` or `stop` control tuple.

# Context & Application

- **Typical contexts**: Events meaningful in every state — printing loop data, stopping the FSM.
- **Common applications**: Triggering normal termination from any state; non-OTP messages routed to `handle_info/3`.
- **Historical/stylistic notes**: The book uses `sync_send_all_state_event/2` for coffee-machine termination "after all, it doesn't really matter what state it is in, as long as it stops" (p. 157).

# Examples

**Example 1** (p. 156): The control-tuple contract for all-state callbacks:

```erlang
gen_fsm:send_all_state_event(NameScope, Event) -> ok
Mod:handle_info/3,
Mod:handle_event/3 -> {next_state, NextState, NewLoopData}
                      {next_state, NextState, NewLoopData, Timeout}
                      {next_state, NextState, NewLoopData, hibernate}
                      {stop, Reason, NewLoopData}
```

**Example 2** (p. 159): Stopping the FSM via the synchronous all-state path, handled in `handle_sync_event/4`:

```erlang
handle_sync_event(stop, _From, _State, LoopData) ->
    {stop, normal, LoopData}.
```

# Relationships

## Builds Upon
- **FSM events** — All-state events are a state-independent form of FSM events.

## Enables
- **fsm-termination** — All-state events are commonly used to stop the FSM.

## Related
- **fsm-synchronous-events** — `sync_send_all_state_event/2` combines synchronous and all-state semantics.

## Contrasts With
- **FSM events** — Ordinary events are dispatched to the *current state's* callback; all-state events go to a single `handle_event/3` callback regardless of state.

# Common Errors

- **Error**: Implementing per-state clauses for an event that should be handled uniformly everywhere.
  **Correction**: Use `send_all_state_event/2` and a single `handle_event/3` clause rather than duplicating the event in every state function.

# Common Confusions

- **Confusion**: Thinking `handle_info/3` and `handle_event/3` are interchangeable.
  **Clarification**: `handle_event/3` handles OTP-compliant all-state events sent via `send_all_state_event/2`; `handle_info/3` handles non-OTP messages such as exit signals and `Pid ! Msg`.

# Source Reference

Chapter 5: Finite State Machines, Section "Asynchronous events to all states," pages 155-156; synchronous all-state events on pages 157-158.

# Verification Notes

- Definition source: Direct quotes from pp. 155-156.
- Confidence rationale: HIGH — the source explicitly defines the send-all-state functions and their callbacks.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
