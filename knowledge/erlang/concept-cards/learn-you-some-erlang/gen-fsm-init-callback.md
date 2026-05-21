---
concept: gen_fsm init Callback
slug: gen-fsm-init-callback
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The init Function"
extraction_confidence: high
aliases:
  - "gen_fsm:init/1"
  - "FSM init/1"
prerequisites:
  - gen-fsm
  - fsm-state-data
extends: []
related:
  - fsm-state-function
  - fsm-state-data
contrasts_with: []
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "How does a behaviour relate to its callback module?"
---

# gen_fsm init Callback

## Quick Definition

`init/1` is the `gen_fsm` callback that sets up the FSM. Unlike `gen_server`'s `init/1`, it must return the *starting state name* alongside the state data.

## Core Definition

"The `init` function for FSMs is the same `init/1` as used for generic servers, except the return values accepted are `{ok, StateName, Data}`, `{ok, StateName, Data, Timeout}`, `{ok, StateName, Data, hibernate}`, and `{stop, Reason}`" (Ch. 15, "The init Function"). "`StateName` is an atom and represents the next callback function to be called."

## Prerequisites

- **gen_fsm** — `init/1` is a `gen_fsm` callback.
- **fsm-state-data** — `init/1` produces the initial state data.

## Key Properties

1. Returns `{ok, StateName, Data}` — `StateName` names the FSM's starting state.
2. May also return `{ok, StateName, Data, Timeout}` or `{ok, StateName, Data, hibernate}`.
3. May return `{stop, Reason}` to abort startup, exactly as in `gen_server`.
4. `StateName` is an atom and selects the first state function to run.
5. `Timeout` and `hibernate` keep their `gen_server` semantics.

## Construction / Recognition

## To Write a gen_fsm init/1

1. Decide the FSM's starting state name (an atom).
2. Build the initial state data (often a record).
3. Return `{ok, StartState, Data}`.
4. Use `{stop, Reason}` if startup must fail.

## Context & Application

The book's dog FSM would start with `init/1` returning `{ok, bark, ...}`. The `trade_fsm` starts in `idle`: `init(Name) -> {ok, idle, #state{name=Name}}.` — the FSM begins in the `idle` state, holding only the user's name in its data.

**OTP version note:** `gen_statem`'s `init/1` returns `{ok, State, Data}` similarly; the requirement to name a starting state carries over.

## Examples

**Example 1** (Ch. 15): `init(Name) -> {ok, idle, #state{name=Name}}.` — `trade_fsm` starts in the `idle` state.

**Example 2** (Ch. 15): The dog FSM's `init/1` would return `{ok, bark, dog}` to start in the `bark` state.

## Relationships

## Builds Upon

- **gen_fsm** — Provides the `init/1` callback.

## Related

- **fsm-state-function** — `StateName` selects the first state function to run.
- **fsm-state-data** — `init/1` produces the initial data term.

## Common Errors

- **Error**: Returning `{ok, Data}` (the `gen_server` shape) from a `gen_fsm` `init/1`.
  **Correction**: A `gen_fsm` `init/1` must return `{ok, StateName, Data}` — the state name is mandatory.

## Common Confusions

- **Confusion**: Thinking the FSM "init state" is the same kind of thing as a `gen_server` state.
  **Clarification**: `StateName` is the named *mode* the FSM starts in; the carried `Data` is the separate state-data term.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "The init Function."

## Verification Notes

- Definition: Direct quotes from "The init Function."
- Key Properties: Return values copied from the source.
- Confidence: HIGH — explicitly defined.
