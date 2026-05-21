---
# === CORE IDENTIFICATION ===
concept: FSM States and State Functions
slug: fsm-states-and-state-functions

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
pdf_page: 149
section: "Defining states"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - state callback function
  - "State/2"
  - state function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-fsm-behavior
extends: []
related:
  - fsm-events
  - fsm-state-transitions
  - fsm-loop-data
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

In a generic FSM, each state is defined as an exported callback function whose name is the state name; it receives the event as its first argument and the loop data as its second.

# Core Definition

"States in FSMs are defined in callback functions, where the name of the function is the name of the state, `Event` is the first argument, and `LoopData` is the second one. Remember that state callback functions are defined in the callback module and have to be exported" (Cesarini & Vinoski, p. 149). For asynchronous events the state function has arity 2 — `State(Event, LoopData)` — and after handling the event returns the new loop data with the next state via `{next_state, NextState, NewLoopData}` (or with a `Timeout`, `hibernate`, or a `stop` reason). For synchronous events the state function has arity 3 — `State(Event, From, LoopData)` — and returns a `{reply, Reply, NextState, NewLoopData}` tuple. The start state is the one returned by `init/1` (p. 149).

# Prerequisites

- **Generic FSM behavior** — State functions are the callback-module half of the `gen_fsm` behavior; you must understand the behavior to define states.

# Key Properties

1. The function name *is* the state name.
2. `State/2` handles asynchronous events: `State(Event, LoopData)`.
3. `State/3` handles synchronous events: `State(Event, From, LoopData)`.
4. State functions must be defined in the callback module and exported.
5. A `State/2` clause returns `{next_state, NextState, NewLoopData}` (optionally with `Timeout`, `hibernate`, or `{stop, Reason, NewLoopData}`).
6. A `State/3` clause returns `{reply, Reply, NextState, NewLoopData}` or a `next_state`/`stop` tuple.
7. Each state typically has a catch-all clause to ignore events that need no action or transition.

# Construction / Recognition

## To Define an FSM State:
1. Choose the state name; it becomes the function name.
2. Write a clause per event the state handles, pattern matching the event in the first argument.
3. Perform the actions, then return `{next_state, NextState, NewLoopData}`.
4. Add a catch-all clause `State(_Other, LoopData) -> {next_state, State, LoopData}` for ignored events.
5. Export the state function.

# Context & Application

- **Typical contexts**: Every state of a `gen_fsm` callback module.
- **Common applications**: The coffee machine's `selection/2`, `payment/2`, and `remove/2` state functions.
- **Historical/stylistic notes**: Without the catch-all clause, an unmatched event (e.g., `selection(cancel, [])`) causes a runtime error because no clause matches (pp. 149-150).

# Examples

**Example 1** (p. 149): The *selection* state callback function:

```erlang
selection({selection, Type, Price}, _LoopData) ->
    hw:display("Please pay:~w", [Price]),
    {next_state, payment, {Type, Price, 0}};
selection({pay, Coin}, LoopData) ->
    hw:return_change(Coin),
    {next_state, selection, LoopData};
selection(_Other, LoopData) ->
    {next_state, selection, LoopData}.
```

**Example 2** (pp. 150-151): The *payment* state uses guards to branch on whether enough has been paid:

```erlang
payment({pay, Coin}, {Type,Price,Paid}) when Coin+Paid >= Price ->
    NewPaid = Coin + Paid,
    hw:display("Preparing Drink.", []),
    hw:return_change(NewPaid - Price),
    hw:drop_cup(), hw:prepare(Type),
    hw:display("Remove Drink.", []),
    {next_state, remove, null};
```

# Relationships

## Builds Upon
- **Generic FSM behavior** — State functions are the callback half of `gen_fsm`.

## Enables
- **fsm-state-transitions** — A state function's return tuple chooses the next state.

## Related
- **fsm-events** — The first argument of a state function is the event.
- **fsm-loop-data** — The last argument of a state function is the loop data.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Omitting the catch-all clause, so an event the state should ignore (e.g., `cancel`) triggers a function-clause runtime error.
  **Correction**: Always add a final `State(_Other, LoopData) -> {next_state, State, LoopData}` clause.

- **Error**: Forgetting to export the state function.
  **Correction**: State callback functions must be exported from the callback module.

# Common Confusions

- **Confusion**: Thinking states are stored as data in loop data.
  **Clarification**: In a `gen_fsm`, a state *is* a callback function; the current state name is tracked by the behavior, not by the loop data.

# Source Reference

Chapter 5: Finite State Machines, Section "Defining states," pages 149-152.

# Verification Notes

- Definition source: Direct quote from p. 149.
- Confidence rationale: HIGH — the source explicitly defines state callback functions and provides multiple worked examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
