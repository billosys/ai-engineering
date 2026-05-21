---
concept: gen_fsm Behaviour
slug: gen-fsm
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "Generic Finite-State Machines"
extraction_confidence: high
aliases:
  - "gen_fsm"
  - generic finite-state machine
  - generic FSM behaviour
prerequisites:
  - finite-state-machine
  - gen-server
  - otp-behaviour
extends:
  - otp-behaviour
related:
  - fsm-state-function
  - fsm-event
  - fsm-state-data
contrasts_with:
  - gen-server
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "How does a behaviour relate to its callback module?"
  - "What distinguishes gen_server from a finite-state-machine behaviour?"
---

# gen_fsm Behaviour

## Quick Definition

`gen_fsm` is the OTP behaviour for finite-state machines, a specialised `gen_server` that handles synchronous and asynchronous *events* instead of calls and casts. Each FSM state is represented by a callback function.

## Core Definition

"The `gen_fsm` behavior is somewhat similar to `gen_server` in that it is a specialized version of that behavior. The biggest difference is that rather than handling *calls* and *casts*, we're handling *synchronous* and *asynchronous* events. Similar to our dog and cat examples, each state is represented by a function" (Ch. 15, "Generic Finite-State Machines").

A `gen_fsm` callback module implements: `init/1`; one or more `StateName/2` (async) and `StateName/3` (sync) state functions; `handle_event/3` and `handle_sync_event/4` for global events; `handle_info/3`; `terminate/3`; and `code_change/4`.

## Prerequisites

- **Finite-state machine** — `gen_fsm` is the generic implementation of the FSM concept.
- **gen_server** — `gen_fsm` is described as a specialised version of `gen_server`; understanding calls/casts/timeouts/`hibernate` carries over.
- **OTP behaviour** — `gen_fsm` is one of the OTP behaviours splitting generic from specific code.

## Key Properties

1. `init/1` returns `{ok, StateName, Data}` (also with `Timeout` or `hibernate`, or `{stop, Reason}`).
2. `StateName/2` handles asynchronous events; `StateName/3` handles synchronous events and receives a `From` argument.
3. State functions return `{next_state, NextStateName, NewData}`, `{stop, Reason, NewData}`, and (for sync) `{reply, Reply, NextStateName, NewData}` variants.
4. Async events are sent with `gen_fsm:send_event/2`; sync events with `gen_fsm:sync_send_event/2,3`.
5. Global events use `gen_fsm:send_all_state_event/2` and `gen_fsm:sync_send_all_state_event/2,3`, handled by `handle_event/3` / `handle_sync_event/4`.
6. `gen_fsm:reply/2` sends a delayed reply to a synchronous caller, exactly as in `gen_server`.

## Construction / Recognition

## To Write a gen_fsm Callback Module

1. Add `-behavior(gen_fsm).`
2. Implement `init/1` returning `{ok, StartStateName, Data}`.
3. Export and implement one `StateName/2` (and/or `StateName/3`) function per state.
4. Implement `handle_event/3` / `handle_sync_event/4` for global events.
5. Implement `handle_info/3`, `terminate/3`, `code_change/4`.
6. Expose a public API that wraps the `gen_fsm:*` send functions.

## Context & Application

`gen_fsm` is used for protocol implementations and any process whose behaviour depends on its current mode. Chapter 15 builds the `trade_fsm` trading system on `gen_fsm`.

**OTP version note:** As of Erlang/OTP 20, `gen_fsm` is **deprecated in favour of `gen_statem`**. `gen_statem` offers richer features (state enter calls, event postponement, two callback modes). The book's `gen_fsm` examples remain instructive for the FSM concept, but new code should target `gen_statem`. The conceptual model — states, events, transitions, state data — is preserved across both.

## Examples

**Example 1** (Ch. 15): `trade_fsm` declares `-behavior(gen_fsm).` and exports `init/1, handle_event/3, handle_sync_event/4, handle_info/3, terminate/3, code_change/4` plus custom state functions `idle/2, idle/3, idle_wait/2, ...`.

**Example 2** (Ch. 15): `start_link(Name) -> gen_fsm:start_link(?MODULE, [Name], []).`

## Relationships

## Builds Upon

- **OTP behaviour** — Generic FSM machinery factored out by OTP.
- **gen_server** — `gen_fsm` is a specialised `gen_server`.

## Related

- **fsm-state-function** — The per-state callbacks `gen_fsm` dispatches to.
- **fsm-event** — Synchronous and asynchronous inputs.
- **fsm-state-data** — Data passed as the last callback argument.

## Contrasts With

- **gen-server** — Handles calls/casts with one conceptual state; `gen_fsm` handles events with many named states.

## Common Errors

- **Error**: Forgetting to export the custom state functions, so the behaviour cannot dispatch to them.
  **Correction**: Export every `StateName/2` and `StateName/3`.
- **Error**: Sending a global-event message with `send_event` (or vice versa).
  **Correction**: Use `send_all_state_event`/`sync_send_all_state_event` for global events.

## Common Confusions

- **Confusion**: Thinking `gen_fsm`'s "state" means the same as a `gen_server`'s state.
  **Clarification**: In `gen_fsm`, "state" is the named mode (`idle`, `negotiate`); the carried data is the *state data*, a separate concept.
- **Confusion**: Believing `gen_fsm` is current OTP.
  **Clarification**: It is deprecated; `gen_statem` is the supported behaviour. The book predates this change.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "Generic Finite-State Machines" (covering `init`, `StateName`, `handle_event`, `handle_sync_event`, `code_change`, `terminate`) and "The gen_fsm Callbacks."

## Verification Notes

- Definition: Direct quote from "Generic Finite-State Machines."
- Key Properties: Synthesised from the callback subsections and the `trade_fsm` public API.
- Confidence: HIGH — callbacks and return values are explicitly enumerated.
- OTP version note added per extraction instructions; book examples kept as-is.
