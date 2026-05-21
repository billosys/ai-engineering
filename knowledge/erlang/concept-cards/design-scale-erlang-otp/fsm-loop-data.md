---
# === CORE IDENTIFICATION ===
concept: FSM Loop Data
slug: fsm-loop-data

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
pdf_page: 147
section: "Starting the FSM"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - loop data
  - FSM state data
  - "LoopData"
  - state data

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-fsm-behavior
extends: []
related:
  - fsm-states-and-state-functions
  - fsm-state-transitions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a finite state machine with gen_statem?"
  - "What is a finite state machine behavior (gen_statem)?"
---

# Quick Definition

FSM loop data is the application-specific data threaded through a generic FSM's state callbacks — distinct from the current state name — passed forward (possibly modified) on every transition.

# Core Definition

In a generic FSM, the `init/1` callback returns `{ok, StartState, LoopData}`, where "`LoopData` contains the data passed to the state callback functions" (Cesarini & Vinoski, p. 147). It is the second argument of every `State/2` callback and is carried forward in the `{next_state, NextState, NewLoopData}` return tuple. The loop data is the *specific* part of the FSM — the book's generic/specific table lists "the loop data" as specific while "storing the loop data" is generic (p. 145). The current *state* is tracked separately by the behavior; loop data holds everything else the FSM needs to remember. In the coffee machine, the loop data in the *payment* state is the tuple `{Type, Price, Paid}` — selection, price, and amount paid so far.

# Prerequisites

- **Generic FSM behavior** — Loop data is stored by the `gen_fsm` machinery; you must understand the behavior.

# Key Properties

1. Returned initially by `init/1` as the third element of `{ok, StartState, LoopData}`.
2. Passed as the last argument to every state callback function.
3. Carried forward as `NewLoopData` in the `{next_state, NextState, NewLoopData}` tuple.
4. Distinct from the current state name, which the behavior tracks separately.
5. Can be any Erlang term — a tuple, record, list, or `[]`/`null` when unused.
6. Different states may need a different shape of loop data.

# Construction / Recognition

## To Use FSM Loop Data:
1. Decide what the FSM must remember beyond its current state.
2. Return it from `init/1` as `{ok, StartState, LoopData}`.
3. Read it from the last argument of each state callback.
4. Return the updated value as `NewLoopData` in the transition tuple.

# Context & Application

- **Typical contexts**: Any FSM state that needs to remember data across events.
- **Common applications**: The coffee machine's `{Type, Price, Paid}` tuple in the *payment* state.
- **Historical/stylistic notes**: The book notes the loop data "could have been done in one variable containing a record, but as different states need a different number of arguments," a simple tuple was cleaner for the coffee example (pp. 143-144).

# Examples

**Example 1** (p. 147): `init([])` returns `{ok, selection, []}` — start state `selection`, loop data the empty list (unused at startup).

**Example 2** (p. 149-150): The *selection* state creates the *payment* loop data: `{next_state, payment, {Type, Price, 0}}` — selection, price, and amount paid (initially 0).

# Relationships

## Builds Upon
- **Generic FSM behavior** — Loop data is stored and threaded by the `gen_fsm` machinery.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **FSM states and state functions** — Loop data is the last argument of every state callback.
- **FSM state transitions** — A transition carries the loop data forward.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Storing the FSM's current state inside the loop data.
  **Correction**: The current state is tracked by the behavior (it's the callback function name); loop data holds only the *other* data the FSM needs.

# Common Confusions

- **Confusion**: Thinking loop data and the FSM state are the same thing.
  **Clarification**: The state is the named callback function the FSM is in; loop data is the separate, application-specific data threaded through transitions.

# Source Reference

Chapter 5: Finite State Machines, Section "Starting the FSM," page 147; payment-state loop data discussed on pages 143-144 and 150.

# Verification Notes

- Definition source: Direct quotes from pp. 145-147.
- Confidence rationale: HIGH — the source explicitly defines loop data and its place in the init and state callbacks.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
