---
# === CORE IDENTIFICATION ===
concept: Finite State Machine
slug: finite-state-machine

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: fsm
tier: foundational

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
  - FSM
  - finite automaton
  - state machine

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - fsm-the-erlang-way
  - fsm-events
  - fsm-state-transitions
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a finite state machine behavior (gen_statem)?"
  - "What distinguishes a gen_server from a gen_statem?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

A finite state machine is an abstract model with a finite number of states and incoming events; in each state it accepts only certain events, and on receiving one it executes predetermined actions and transitions to a new state.

# Core Definition

"An FSM is an abstract model consisting of a finite number of states and incoming events. When the program is in each state, it can receive certain events from the environment — and only those events. When an event arrives and the FSM is in a certain state, the program executes some predetermined actions associated with that state and transitions to a new state. The FSM then waits for a new event, in the new state" (Cesarini & Vinoski, p. 137). Events arriving "out of sequence" — events the current state cannot handle — are handled only after the FSM transitions to a state that can deal with them. Erlang was deliberately optimized for building nontrivial, scalable FSMs: the language's prototyping origins were a soft telephony switch in which each phone was a process acting as an FSM (p. 136).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Consists of a *finite* number of states.
2. In each state it accepts only a defined subset of incoming events.
3. On receiving a valid event it executes predetermined actions, then transitions to a new state.
4. After a transition, it waits for the next event in the new state.
5. Out-of-sequence events are deferred until a state can handle them.

# Construction / Recognition

## To Design an FSM:
1. Enumerate the states the system can be in.
2. Enumerate the events each state can receive.
3. For each (state, event) pair, define the actions and the next state.
4. Draw a state diagram before coding; if it grows complex, split it into smaller cooperating FSMs.

## To Recognize a Need for an FSM:
1. Ask whether the system has distinct modes that constrain which inputs are valid.
2. If the same input means different things depending on a "current mode," an FSM fits.

# Context & Application

- **Typical contexts**: Protocol stacks, connectors, proxies, workflow systems, gaming engines, simulations.
- **Common applications**: Modeling devices and resources whose behavior depends on their current state (phones, vending machines).
- **Historical/stylistic notes**: Erlang's inventors (Armstrong, Williams, Virding) prototyped a soft telephony switch where each phone was an FSM process — captured in *Erlang the Movie* (p. 136).

# Examples

**Example 1** (p. 137, Figure 6-1): A day/night FSM — in state *day*, `eclipse` keeps it in *day* and `sunset` transitions to *night*; in state *night*, `sunrise` transitions back to *day*.

**Example 2** (pp. 139-141): The coffee vending machine FSM with three states — *selection*, *payment*, *remove* — linked by the events selection, pay, cancel, and removal.

# Relationships

## Builds Upon
- *(Foundational — nothing within this source.)*

## Enables
- **fsm-the-erlang-way** — How FSMs are implemented idiomatically in Erlang.
- **fsm-events** — Events drive FSM transitions.
- **fsm-state-transitions** — Transitions are the core FSM mechanism.

## Related
- **fsm-states-and-state-functions** — States are the building blocks of an FSM.

## Contrasts With
- **Generic server** — A `gen_server` is a client-server behavior; an FSM models state-dependent behavior. The book warns against using a `gen_server` and storing FSM state in loop data instead of using a proper FSM.

# Common Errors

- **Error**: Using a generic server and unknowingly storing the FSM state in the loop data.
  **Correction**: When the design has distinct states constraining valid events, use a generic FSM behavior; decide in the design phase whether you need an FSM or a client-server behavior.

# Common Confusions

- **Confusion**: Believing an out-of-sequence event must be an error to discard.
  **Clarification**: An out-of-sequence event is simply left unhandled until the FSM reaches a state that can deal with it — in Erlang it stays in the process mailbox.

# Source Reference

Chapter 5: Finite State Machines, Section "Finite State Machines the Erlang Way," pages 136-138. See Figure 6-1 (Erlang FSM) and the "FSMs Versus Generic Servers" sidebar.

# Verification Notes

- Definition source: Direct quote from p. 137.
- Confidence rationale: HIGH — the chapter opens with an explicit automata-theory definition of an FSM.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
