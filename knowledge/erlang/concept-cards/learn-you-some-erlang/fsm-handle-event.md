---
concept: FSM Global Event Handler
slug: fsm-handle-event
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The handle_event Function"
extraction_confidence: high
aliases:
  - "handle_event/3"
  - "handle_sync_event/4"
  - global event callback
  - all-state event
prerequisites:
  - gen-fsm
  - fsm-event
extends: []
related:
  - fsm-state-function
  - fsm-state-data
contrasts_with:
  - fsm-state-function
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
---

# FSM Global Event Handler

## Quick Definition

`handle_event/3` and `handle_sync_event/4` are the `gen_fsm` callbacks for *global events* — events that must be treated the same way no matter which state the FSM is in.

## Core Definition

"For these events that should be treated the same way in every state, the `handle_event/3` callback is what you want. The function takes arguments similar to `StateName/2`, with the exception that it accepts a `StateName` variable in between them (`handle_event(Event, StateName, Data)`), telling you what the state was when the event was received. It returns the same values as `StateName/2`" (Ch. 15, "The handle_event Function").

"The `handle_sync_event/4` callback is to `StateName/3` what `handle_event/2` is to `StateName/2`. It handles synchronous global events, takes the same parameters, and returns the same kind of tuples as `StateName/3`" (Ch. 15, "The handle_sync_event Function").

## Prerequisites

- **gen_fsm** — These are `gen_fsm` callbacks.
- **fsm-event** — Global events are sent with the `*_all_state_event` functions.

## Key Properties

1. `handle_event(Event, StateName, Data)` handles asynchronous global events; returns the same tuples as `StateName/2`.
2. `handle_sync_event(Event, From, StateName, Data)` handles synchronous global events; returns the same tuples as `StateName/3`.
3. Both receive the *current* `StateName` so the callback can decide the next state contextually.
4. Async global events arrive via `gen_fsm:send_all_state_event/2`; sync ones via `gen_fsm:sync_send_all_state_event/2,3`.
5. Used for actions that apply regardless of state — e.g. cancelling a transaction.

## Construction / Recognition

## To Handle a Global Event

1. Decide whether the event applies in every state (if so, it is global).
2. Implement `handle_event/3` (async) or `handle_sync_event/4` (sync).
3. Have callers send it with `send_all_state_event` / `sync_send_all_state_event`.
4. Return a `{next_state, ...}` or `{stop, ...}` tuple as for an ordinary state function.

## Context & Application

The book's classic example of a global event is the dog smelling food: "no matter which state the dog is in, he will go looking for the source of food." In `trade_fsm`, cancellation is global — a player can cancel from any state — so it is handled by `handle_event`/`handle_sync_event` and sent via `sync_send_all_state_event`.

**OTP version note:** `gen_statem` has no separate "all-state" callback; in `handle_event_function` mode a single `handle_event/4` covers everything, and in `state_functions` mode common handling is factored manually. The *concept* of state-independent handling persists.

## Examples

**Example 1** (Ch. 15): The dog's "smell food" event would be a global event — it overrides whatever state the dog is in.

**Example 2** (Ch. 15): `cancel/1` in `trade_fsm` uses `sync_send_all_state_event(OwnPid, cancel)`, so cancellation is dispatched to `handle_sync_event/4` regardless of the FSM's current state.

## Relationships

## Builds Upon

- **gen_fsm** — Provides the global-event callbacks.

## Related

- **fsm-event** — Global events are one category of FSM event.
- **fsm-state-data** — Global handlers update the carried data like any callback.

## Contrasts With

- **fsm-state-function** — A state function handles events *only* in its own state; a global handler handles them in *every* state.

## Common Errors

- **Error**: Putting cancel/shutdown logic in every state function separately.
  **Correction**: Use a single global `handle_event`/`handle_sync_event` clause to avoid duplication and missed states.

## Common Confusions

- **Confusion**: Thinking `handle_event/3` is for out-of-band messages.
  **Clarification**: Out-of-band messages (sent with `!`) go to `handle_info/3`; `handle_event/3` is specifically for global events sent via `send_all_state_event`.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," sections "The handle_event Function" and "The handle_sync_event Function."

## Verification Notes

- Definition: Direct quotes from both callback subsections.
- Key Properties: Synthesised from the callback signatures and the cancel example.
- Confidence: HIGH — both callbacks explicitly described.
