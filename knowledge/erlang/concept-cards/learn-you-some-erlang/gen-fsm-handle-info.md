---
concept: gen_fsm handle_info
slug: gen-fsm-handle-info
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The gen_fsm Callbacks"
extraction_confidence: high
aliases:
  - "handle_info/3"
  - FSM out-of-band messages
prerequisites:
  - gen-fsm
extends: []
related:
  - fsm-monitor-integration
  - fsm-handle-event
contrasts_with:
  - fsm-handle-event
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
---

# gen_fsm handle_info

## Quick Definition

`handle_info/3` is the `gen_fsm` callback for out-of-band messages — anything sent to the FSM with the `!` operator or arriving as a signal, rather than through the event functions.

## Core Definition

`handle_info/3` for `gen_fsm` parallels `handle_info` in `gen_server` and `gen_event`: it handles messages that did not come through the FSM's event-sending API. It receives `(Info, StateName, Data)` and returns the same kinds of tuples as a state function.

## Prerequisites

- **gen_fsm** — `handle_info/3` is a `gen_fsm` callback.

## Key Properties

1. Handles out-of-band messages — `!`-sent messages, monitor `'DOWN'` messages, exit signals.
2. Signature is `handle_info(Info, StateName, Data)`.
3. Returns the same tuples as `StateName/2` (`{next_state, ...}`, `{stop, ...}`).
4. It is the FSM equivalent of `gen_server`'s and `gen_event`'s `handle_info`.
5. A common use is receiving the `{'DOWN', Ref, process, Pid, Reason}` message from a monitor.

## Construction / Recognition

## To Use handle_info/3

1. Export and implement `handle_info/3`.
2. Match expected out-of-band messages (e.g. `'DOWN'` tuples).
3. Return `{next_state, StateName, Data}` or `{stop, Reason, Data}`.
4. Add a catch-all clause that logs unexpected messages and stays in the current state.

## Context & Application

In `trade_fsm`, `handle_info/3` handles the peer FSM's death: it matches `{'DOWN', Ref, process, Pid, Reason}` against the stored monitor reference and returns `{stop, {other_down, Reason}, S}`. The catch-all clause logs anything else with the `unexpected/2` helper.

**OTP version note:** `gen_statem` folds out-of-band messages into its general event handling (as `info`-type events) rather than a dedicated `handle_info/3`; the *purpose* — handling non-API messages — carries over.

## Examples

**Example 1** (Ch. 15): `handle_info({'DOWN', Ref, process, Pid, Reason}, _, S=#state{other=Pid, monitor=Ref}) -> {stop, {other_down, Reason}, S};`

**Example 2** (Ch. 15): `handle_info(Info, StateName, Data) -> unexpected(Info, StateName), {next_state, StateName, Data}.`

## Relationships

## Builds Upon

- **gen_fsm** — Provides the `handle_info/3` callback.

## Related

- **fsm-monitor-integration** — Monitor `'DOWN'` messages arrive through `handle_info/3`.

## Contrasts With

- **fsm-handle-event** — `handle_event/3` handles *global events* sent through the FSM API; `handle_info/3` handles messages that bypass the API entirely.

## Common Errors

- **Error**: Expecting `!`-sent messages to reach a state function.
  **Correction**: Raw messages reach `handle_info/3`, not `StateName/2`; only API-sent events reach state functions.

## Common Confusions

- **Confusion**: Conflating `handle_info/3` with `handle_event/3`.
  **Clarification**: `handle_event/3` is for *global events* sent via `send_all_state_event`; `handle_info/3` is for out-of-band messages (`!`, signals, `'DOWN'`).

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "The gen_fsm Callbacks" (the `handle_info/3` clauses).

## Verification Notes

- Definition: Synthesised from the callback's role and the `trade_fsm` `handle_info/3` code.
- Key Properties: Adapted from the code and the parallel to `gen_server`/`gen_event`.
- Confidence: HIGH — shown with code, though the book describes it briefly.
