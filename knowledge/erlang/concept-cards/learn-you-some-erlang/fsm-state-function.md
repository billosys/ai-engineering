---
concept: FSM State Function
slug: fsm-state-function
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The StateName Function"
extraction_confidence: high
aliases:
  - "StateName function"
  - "StateName/2"
  - "StateName/3"
  - state callback
prerequisites:
  - gen-fsm
  - fsm-event
extends: []
related:
  - finite-state-machine
  - fsm-state-data
  - fsm-handle-event
contrasts_with: []
answers_questions:
  - "How does a behaviour relate to its callback module?"
  - "How do I implement a stateful process?"
---

# FSM State Function

## Quick Definition

In a `gen_fsm` module, each state is a callback function whose name is the state. `StateName/2` handles asynchronous events for that state and `StateName/3` handles synchronous ones.

## Core Definition

"The functions `StateName/2` and `StateName/3` are placeholder names, and you decide what they will be. ... These states dictate a context in which you handle a given event." If `init/1` returns `{ok, sitting, dog}`, then "whenever the `gen_fsm` process receives an event, either the function `sitting/2` or `sitting/3` will be called. The `sitting/2` function is called for asynchronous events, and `sitting/3` is called for synchronous events" (Ch. 15, "The StateName Function").

## Prerequisites

- **gen_fsm** — State functions are the per-state callbacks the `gen_fsm` behaviour dispatches to.
- **fsm-event** — State functions exist to handle events.

## Key Properties

1. The function name *is* the state name (an atom); the FSM's current state selects which function runs.
2. `StateName/2` arguments are `(Event, StateData)`; it handles asynchronous events.
3. `StateName/3` arguments are `(Event, From, StateData)`; it handles synchronous events.
4. `StateName/2` returns `{next_state, NextStateName, NewData}`, `{next_state, ..., Timeout}`, `{next_state, ..., hibernate}`, or `{stop, Reason, NewData}`.
5. `StateName/3` may additionally return `{reply, Reply, NextStateName, NewData}` variants and `{stop, Reason, Reply, NewData}`.
6. There is no limit on how many state functions a module may have, provided they are exported.
7. The `NextStateName` atom returned determines which state function runs next.

## Construction / Recognition

## To Add a State

1. Choose an atom name for the state.
2. Export `StateName/2` (and `StateName/3` if the state accepts synchronous events).
3. Match on each expected event and return a `{next_state, ...}` tuple.
4. Add a catch-all clause that logs the unexpected event and stays in the same state.

## Context & Application

State functions are the heart of a `gen_fsm` callback module. The book's analogy: receiving a phone call produces different reactions depending on whether you are in the state "sleeping on a Saturday morning" or "waiting for a job interview."

**OTP version note:** Under `gen_statem` (the modern replacement for `gen_fsm`), the equivalent is either one callback function per state (`state_functions` mode) or a single `handle_event/4` (`handle_event_function` mode). The "state as function" idea carries over directly in `state_functions` mode.

## Examples

**Example 1** (Ch. 15): `idle({ask_negotiate, OtherPid}, S=#state{})` is the async clause of the `idle` state, returning `{next_state, idle_wait, S#state{...}}`.

**Example 2** (Ch. 15): `idle({negotiate, OtherPid}, From, S=#state{})` is the sync clause; it stores `From` and moves to `idle_wait` without replying yet.

**Example 3** (Ch. 15): `negotiate(ready, From, S)` returns `{next_state, wait, S#state{from=From}}`.

## Relationships

## Builds Upon

- **gen_fsm** — The behaviour that calls state functions.

## Related

- **finite-state-machine** — States are the core of an FSM.
- **fsm-state-data** — The `StateData`/`Data` argument threaded through each call.
- **fsm-handle-event** — Handles events common to *all* states.

## Common Errors

- **Error**: Defining a `StateName/3` clause but forgetting to reply to the synchronous caller.
  **Correction**: Either return a `{reply, ...}` tuple or store `From` and later call `gen_fsm:reply/2`.
- **Error**: Returning an atom for `NextStateName` that has no matching exported function.
  **Correction**: Ensure every transition target names an exported state function.

## Common Confusions

- **Confusion**: Thinking `/2` and `/3` versions of a state must do the same thing.
  **Clarification**: `/2` is for asynchronous events and `/3` for synchronous events; they often have different callers and logic.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "The StateName Function," with the full list of return tuples for `StateName/3`. See also "The gen_fsm Callbacks" for `idle/2`, `idle/3`, `negotiate/2`, `negotiate/3`, etc.

## Verification Notes

- Definition: Direct quotes from "The StateName Function."
- Key Properties: Return tuples copied from the source's enumerated list.
- Confidence: HIGH — explicitly defined with code examples.
