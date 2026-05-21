---
concept: Finite-State Machine
slug: finite-state-machine
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "What Is a Finite-State Machine?"
extraction_confidence: high
aliases:
  - FSM
  - state machine
prerequisites:
  - process
  - selective-receive
  - pattern-matching
extends: []
related:
  - gen-fsm
  - fsm-state-function
  - fsm-event
  - fsm-state-data
contrasts_with:
  - gen-server
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "What distinguishes gen_server from a finite-state-machine behaviour?"
---

# Finite-State Machine

## Quick Definition

A finite-state machine (FSM) is a system with a finite number of states, where inputs (events) force transitions between those states. In Erlang it is implemented as a process running a set of functions (the states) and receiving messages (events).

## Core Definition

The book defines a finite-state machine as "not really a machine, but it does have a finite number of states." The Erlang FSMs "are more inspired by [the mathematical definition] than a direct implementation." Concretely: "A typical Erlang finite-state machine can be implemented as a process running a given set of functions (their states) and receiving messages (events) that force a state transition" (Ch. 15, "What Is a Finite-State Machine?").

The book illustrates this with a dog FSM having three states — `bark`, `wag_tail`, `sit` — where events such as `pet` and `squirrel` drive transitions, and a one-state cat FSM that ignores all events.

## Prerequisites

- **Process** — An FSM is a process running state functions in a loop.
- **Selective receive** — Hand-rolled FSMs use `receive` to match events; different states accept different messages.
- **Pattern matching** — Events are dispatched by matching message shapes.

## Key Properties

1. There is a finite, enumerated set of states; the machine is always in exactly one.
2. Each state determines which events it can handle and what transition each event triggers.
3. Events may be synchronous (caller waits for a reply) or asynchronous (fire-and-forget).
4. Some events are *global* — they cause the same reaction in any state (e.g. the dog smelling food).
5. State data (context) is carried alongside the state name across transitions.
6. Unhandled events in a given state are typically logged and ignored rather than crashing the FSM.

## Construction / Recognition

## To Model a System as an FSM

1. Enumerate the distinct states the system can be in.
2. For each state, list the events it must respond to.
3. For each (state, event) pair, define the resulting next state and any side effects.
4. Identify global events that apply regardless of state.
5. Decide whether each event is synchronous or asynchronous.

## Context & Application

FSMs are central to many industrial protocol implementations; the book notes they "were used so frequently in the telecom world that the OTP engineers ended up writing a behavior for them: `gen_fsm`." Chapter 15 builds a full asynchronous client-to-client trading system as an FSM.

**OTP version note:** The book implements FSMs with the `gen_fsm` behaviour. Modern Erlang/OTP (baseline OTP 27+) deprecates `gen_fsm` in favour of `gen_statem`. The *concept* of a finite-state machine is fully current; only the specific OTP behaviour name has changed. The book's FSM design principles transfer directly to `gen_statem`.

## Examples

**Example 1** (Ch. 15): The dog FSM with states `bark`, `wag_tail`, `sit`. A sitting dog that sees a squirrel barks; a barking dog that is petted wags its tail.

**Example 2** (Ch. 15): The cat FSM `cat_fsm` with the single state `dont_give_crap` — no event ever changes its state.

**Example 3** (Ch. 15): The `trade_fsm` trading system with states `idle`, `idle_wait`, `negotiate`, `wait`, and `ready`.

## Relationships

## Builds Upon

- **Process** — An FSM is a long-lived process looping over state functions.

## Related

- **gen-fsm** — The OTP behaviour that generalises FSM mechanics.
- **fsm-state-function** — Each state is a callback function.
- **fsm-event** — The inputs that drive transitions.
- **fsm-state-data** — The context carried across transitions.

## Contrasts With

- **gen-server** — A `gen_server` has a single conceptual state and handles calls/casts; an FSM has multiple named states, each handling events differently.

## Common Errors

- **Error**: Not handling out-of-band messages received during a state.
  **Correction**: Add a catch-all clause that logs the unexpected event and stays in the current state.
- **Error**: Using synchronous events on both sides of two communicating FSMs.
  **Correction**: This deadlocks both FSMs; prefer asynchronous events between FSMs.

## Common Confusions

- **Confusion**: Thinking Erlang FSMs are a strict mathematical (DFA/NFA) implementation.
  **Clarification**: They are *inspired* by the mathematical definition but are pragmatic processes; states are functions and events are messages.
- **Confusion**: Believing `gen_fsm` is the current OTP behaviour.
  **Clarification**: As of OTP 20+, `gen_fsm` is deprecated; `gen_statem` is the supported FSM behaviour. The FSM concept itself is unchanged.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," sections "What Is a Finite-State Machine?" and "A Trading System Specification." See the dog/cat FSM examples and the `trade_fsm` state diagrams.

## Verification Notes

- Definition: Direct adaptation from the chapter's opening section.
- Key Properties: Synthesised from the dog/cat examples and the discussion of global and synchronous/asynchronous events.
- Confidence: HIGH — the source explicitly defines and extensively illustrates the concept.
- OTP version note added per extraction instructions; the book's `gen_fsm` examples are kept unchanged.
