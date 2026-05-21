---
# === CORE IDENTIFICATION ===
concept: FSM State Transitions
slug: fsm-state-transitions

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
pdf_page: 137
section: "Defining states"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - state transition
  - "{next_state, NextState, NewLoopData}"
  - transition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fsm-states-and-state-functions
  - fsm-events
extends: []
related:
  - fsm-loop-data
  - finite-state-machine
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

A state transition moves an FSM from its current state to a new one; in a generic FSM it is expressed by returning a `{next_state, NextState, NewLoopData}` tuple from a state callback function.

# Core Definition

A state transition is the change of an FSM from one state to another, "determined by the combination of the current state and inbound event" (Cesarini & Vinoski, p. 137). In a pure-Erlang FSM the transition is a tail call to the next state's function; in the generic FSM behavior, "by returning the tuple `{next_state, NextState, NewLoopData}`, we return the control to the `gen_fsm` module and wait for the next event" (p. 149). To remain in the current state — to "ignore" an event — the callback returns `next_state` with the current state name unchanged. Upon receiving an event the FSM "executes one or more actions before transitioning to its next state" (p. 137); the actions happen first, the transition last.

# Prerequisites

- **FSM states and state functions** — A transition is the result of a state callback function returning a `next_state` tuple.
- **FSM events** — An event is what triggers a transition.

# Key Properties

1. A transition is chosen by the (current state, inbound event) combination.
2. Actions are executed *before* the transition completes.
3. In a generic FSM, a transition is expressed by `{next_state, NextState, NewLoopData}`.
4. Returning `next_state` with the *same* state name keeps the FSM in place (ignores the event).
5. The transition may also carry a `Timeout` or `hibernate` as a fourth element.
6. In a pure-Erlang FSM, a transition is simply a tail call to the next state function.

# Construction / Recognition

## To Express a Transition:
1. In the matching state-callback clause, run the actions for that (state, event) pair.
2. Return `{next_state, NextState, NewLoopData}` with the target state.
3. To stay put, return `{next_state, CurrentState, LoopData}`.

## To Recognize a Transition:
1. Look at the second element of a `next_state` return tuple.
2. In trace output, `*DBG* ... switched to state ...` records each transition.

# Context & Application

- **Typical contexts**: Every state callback in an FSM.
- **Common applications**: The coffee machine moving `selection -> payment -> remove -> selection`.
- **Historical/stylistic notes**: Figure 6-2's coffee machine diagram annotates each transition with the actions executed when it is taken (p. 140).

# Examples

**Example 1** (p. 149): The *selection* state transitions to *payment* on a drink selection:

```erlang
selection({selection, Type, Price}, _LoopData) ->
    hw:display("Please pay:~w", [Price]),
    {next_state, payment, {Type, Price, 0}};
```

**Example 2** (p. 151): The *payment* state transitions back to *selection* on `cancel`:

```erlang
payment(cancel, {_Type, _Price, Paid}) ->
    hw:display("Make Your Selection", []),
    hw:return_change(Paid),
    {next_state, selection, null};
```

# Relationships

## Builds Upon
- **FSM states and state functions** — A transition is produced by a state callback's return value.
- **FSM events** — Events trigger transitions.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **fsm-loop-data** — A transition carries the (possibly updated) loop data forward.
- **finite-state-machine** — Transitions are the core mechanism of the FSM model.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Performing the transition before the actions, or forgetting actions entirely.
  **Correction**: Execute the state's actions first, then return the `next_state` tuple — the FSM transitions last.

# Common Confusions

- **Confusion**: Thinking returning the same state name is a no-op error.
  **Clarification**: Returning `{next_state, CurrentState, LoopData}` is the deliberate idiom for ignoring an event while staying in the current state.

# Source Reference

Chapter 5: Finite State Machines, Sections "Finite State Machines the Erlang Way" (p. 137) and "Defining states" (pp. 149-152). See Figure 6-2.

# Verification Notes

- Definition source: Direct quotes from pp. 137 and 149.
- Confidence rationale: HIGH — the source explicitly explains transitions in both pure-Erlang and behavior forms.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
