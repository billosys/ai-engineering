---
# === CORE IDENTIFICATION ===
concept: Finite State Machines the Erlang Way
slug: fsm-the-erlang-way

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
pdf_page: 136
section: "Finite State Machines the Erlang Way"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - pure Erlang FSM
  - hand-rolled FSM
  - FSM with tail-recursive functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-state-machine
extends:
  - finite-state-machine
related:
  - fsm-states-and-state-functions
  - fsm-events
  - generic-fsm-behavior
contrasts_with:
  - generic-fsm-behavior

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

In Erlang, an FSM is implemented in pure Erlang by representing each state as a tail-recursive function and each event as a message; state transitions are achieved simply by calling the next state's function.

# Core Definition

"In Erlang, each state is represented within a tail-recursive function and events are represented as messages" (Cesarini & Vinoski, p. 137). Upon receiving an event, the FSM executes one or more actions before transitioning to its next state; "the state transition is achieved by calling the next function, determined by the combination of the current state and inbound event" (p. 137). When you start an FSM you must give it a starting state and initialize it — typically by spawning an `init/0` function that does setup work and then calls the first state function. "The keys to keeping FSMs simple are selective receives, tail-recursive functions, and the ability to initialize the FSM when spawning the process" (p. 138). You should fully design the FSM — drawing a diagram — before coding, and split it into smaller cooperating FSMs if it grows complex.

# Prerequisites

- **Finite state machine** — You must understand the abstract FSM model (states, events, transitions) before implementing one in Erlang.

# Key Properties

1. Each state is a tail-recursive function.
2. Each event is a message received in a `receive` clause.
3. A transition is just a tail call to the next state's function.
4. The (state, event) combination determines the action and the next state function.
5. The FSM is started by spawning an `init` function that does setup, then calls the first state function.
6. Out-of-sequence events stay in the process mailbox until matched in a state that handles them — a selective receive.

# Construction / Recognition

## To Implement a Pure-Erlang FSM:
1. Write one function per state, each with a `receive` block.
2. In each clause, perform the actions, then tail-call the next state function.
3. Re-invoke the current state's function to "ignore" an event without transitioning.
4. Write `start/0` to `spawn` `init/0`, and `init/0` to do setup then call the first state.

## To Recognize the Pattern:
1. Look for a set of mutually tail-recursive functions, each containing a `receive`.

# Context & Application

- **Typical contexts**: Embedded and protocol code before (or instead of) migrating to a generic FSM behavior.
- **Common applications**: The coffee machine example modeled directly in Erlang with `selection/0`, `payment/3`, and `remove/0` functions.
- **Historical/stylistic notes**: The book uses the pure-Erlang FSM to motivate the split into generic (`gen_fsm`) and specific code before introducing the behavior.

# Examples

**Example 1** (p. 137): State *day* as a tail-recursive function:

```erlang
day() ->
    receive
        eclipse -> day();
        sunset  -> night()
    end.
```

**Example 2** (p. 138): Starting and initializing the FSM:

```erlang
start() ->
    spawn(?MODULE, init, []).

init() ->
    create_earth(),
    day().
```

## Worked Example

The coffee machine *selection* state in pure Erlang (p. 142):

```erlang
%% State: drink selection
selection() ->
    receive
        {selection, Type, Price} ->
            hw:display("Please pay:~w", [Price]),
            payment(Type, Price, 0);
        {pay, Coin} ->
            hw:return_change(Coin),
            selection();
        _Other -> % cancel
            selection()
    end.
```

# Relationships

## Builds Upon
- **Finite state machine** — This is the idiomatic Erlang realization of the abstract FSM model.

## Enables
- **generic-fsm-behavior** — Splitting the pure-Erlang FSM into generic and specific code motivates the `gen_fsm` behavior.

## Related
- **fsm-states-and-state-functions** — States are the tail-recursive functions.
- **fsm-events** — Events are the messages received.

## Contrasts With
- **generic-fsm-behavior** — The pure-Erlang FSM mixes generic and specific code; `gen_fsm` extracts the generic parts into a library module.

# Common Errors

- **Error**: Omitting a catch-all clause in a state's `receive`, so an unhandled event causes the FSM to block on a non-matching message.
  **Correction**: Include a clause (e.g., `_Other -> current_state()`) to re-invoke the state for events that should be ignored.

# Common Confusions

- **Confusion**: Thinking a state transition needs a special construct.
  **Clarification**: A transition is simply a tail call to the next state's function — nothing more.

# Source Reference

Chapter 5: Finite State Machines, Section "Finite State Machines the Erlang Way," pages 137-138; pure-Erlang coffee machine in "The Erlang Coffee Machine," pages 141-144.

# Verification Notes

- Definition source: Direct quotes from pp. 137-138.
- Confidence rationale: HIGH — the source explicitly states the implementation idiom and provides multiple code examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
