---
concept: FSM State Data
slug: fsm-state-data
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
  - "StateData"
  - FSM data
  - carried data
prerequisites:
  - gen-fsm
  - record
extends: []
related:
  - fsm-state-function
  - fsm-event
  - finite-state-machine
contrasts_with: []
answers_questions:
  - "How do I implement a stateful process?"
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
---

# FSM State Data

## Quick Definition

FSM state data is the context (data) that a `gen_fsm` carries across state transitions, separate from the state *name*. It is the last argument of every state callback.

## Core Definition

The state-data argument is "the data that was carried over the calls" (Ch. 15, "The StateName Function"). It is distinct from the FSM's *state name*: the `init/1` return `{ok, StateName, Data}` separates the two — `StateName` is the atom naming the state, and `Data` is the arbitrary term holding the FSM's working context. Every state function receives this data as its final argument and returns an updated version inside its `{next_state, NextStateName, NewStateData}` tuple.

## Prerequisites

- **gen_fsm** — State data is threaded through `gen_fsm` callbacks.
- **Record** — In practice the state data is usually a record holding the FSM's fields.

## Key Properties

1. State data is separate from the state name; the name selects behaviour, the data holds context.
2. It is the last argument of `StateName/2`, `StateName/3`, `handle_event/3`, `handle_sync_event/4`, and `handle_info/3`.
3. It is updated by being returned (transformed) inside each callback's result tuple.
4. It is typically an Erlang record so fields can be named and selectively updated.
5. `code_change/4` receives and may transform the state data alongside the state name.

## Construction / Recognition

## To Use State Data

1. Define a record for the FSM's working context.
2. Return `{ok, StartState, #state{...}}` from `init/1`.
3. In each state callback, pattern-match the record argument and update fields as needed.
4. Return the modified record inside the `{next_state, ...}` or `{reply, ...}` tuple.

## Context & Application

In `trade_fsm`, the state data is a record holding the user's name, the other player's pid, both item lists, a monitor reference, and a delayed-reply `from` field:

```erlang
-record(state, {name="", other, ownitems=[], otheritems=[], monitor, from}).
```

`init(Name) -> {ok, idle, #state{name=Name}}.` starts the FSM in the `idle` state with that record as its data.

**OTP version note:** `gen_statem` uses the identical idea but calls it simply *Data*, returning `{next_state, NextState, NewData}`. The concept transfers unchanged.

## Examples

**Example 1** (Ch. 15): `negotiate({make_offer, Item}, S=#state{ownitems=OwnItems})` updates the carried record: `{next_state, negotiate, S#state{ownitems=add(Item, OwnItems)}}`.

**Example 2** (Ch. 15): `negotiate(ready, From, S)` stores the synchronous caller in the data with `S#state{from=From}` so a reply can be sent later via `gen_fsm:reply/2`.

## Relationships

## Builds Upon

- **gen_fsm** — The behaviour that threads state data through callbacks.

## Related

- **fsm-state-function** — Each state function receives and returns the state data.
- **fsm-event** — Events cause the state data to be updated.
- **finite-state-machine** — State data is the FSM's working context.

## Common Errors

- **Error**: Returning the old, unmodified record after an event that should have changed it.
  **Correction**: Thread the updated record into the return tuple; Erlang data is immutable, so an unreturned update is lost.

## Common Confusions

- **Confusion**: Conflating the state *name* with the state *data*.
  **Clarification**: `gen_fsm` keeps them separate — the name (atom) decides which function runs; the data (any term) holds the context.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "The StateName Function" and "The gen_fsm Callbacks" (the `#state{}` record definition and `init/1`).

## Verification Notes

- Definition: Adapted from the description of the `StateData` argument and the `{ok, StateName, Data}` return.
- Key Properties: Synthesised from the callback signatures and the `trade_fsm` record.
- Confidence: HIGH — explicit in the callback descriptions and code.
