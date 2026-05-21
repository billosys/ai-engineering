---
# === CORE IDENTIFICATION ===
concept: Event-Driven State Machine
slug: event-driven-state-machine

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: state-machine-theory
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_statem Behaviour"
chapter_number: null
pdf_page: null
section: "Event-Driven State Machines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "event-driven Mealy machine"
  - "EDSM"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - gen-statem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_statem?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

An event-driven state machine is a computational model where the input is an event that triggers a state transition, and the output is actions executed during that transition, following the relation `State(S) x Event(E) -> Actions(A), State(S')`.

# Core Definition

As defined in the OTP Design Principles: "For an Event-Driven State Machine, the input is an event that triggers a state transition and the output is actions executed during the state transition. Analogously to the mathematical model of a Finite State Machine, it can be described as a set of relations of the following form: `State(S) x Event(E) -> Actions(A), State(S')`." The documentation further explains: "These relations are interpreted as follows: if we are in state S, and event E occurs, we are to perform actions A, and make a transition to state S'. Notice that S' can be equal to S, and that A can be empty." Because actions and next state depend only on the current state and event, this is classified as a Mealy machine.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Follows the relation `State(S) x Event(E) -> Actions(A), State(S')`.
2. The next state `S'` can be equal to the current state `S` (a self-transition).
3. Actions `A` can be empty.
4. Classified as a Mealy machine since output depends on both state and input.
5. In `gen_statem`, a "state change" is distinct from a "state transition" -- a state change occurs only when `S' =/= S` (Erlang's strict inequality `=/=`).
6. `gen_statem` augments the basic model with server `Data`, making it Turing complete.

# Construction / Recognition

## To Construct/Create:
1. Define a finite set of states.
2. Define the set of possible events (inputs).
3. For each state-event pair, define the actions to perform and the next state.
4. Identify the initial state.

## To Identify/Recognize:
1. System behavior depends on a current state and incoming events.
2. Events trigger transitions that may change the state and produce actions.
3. Can be represented as a state diagram with states, events, and transition actions.

# Context & Application

The event-driven state machine model is the theoretical foundation for `gen_statem`. Understanding this model is essential for designing state machines in OTP. The ballpoint pen example in the documentation illustrates how everyday devices can be modeled this way: the pen has two states (retracted, exposed), two events (push-end, push-side), and transition actions (expose tip, retract tip).

# Examples

**Example 1** (statem.md, "Event-Driven State Machines"): The formal relation is expressed as:

```erlang
State(S) x Event(E) -> Actions(A), State(S')
```

**Example 2** (statem.md, "Everyday State Machine"): A ballpoint pen modeled as a state machine. In the `Retracted` state, a `push-end` event causes the action "Expose tip" and transitions to the `Exposed` state. A `push-side` event in the `Retracted` state causes no action and remains in `Retracted`.

**Example 3** (statem.md, "Event-Driven State Machines"): The source distinguishes state change from state transition: "In gen_statem we define a state change as a state transition in which the new state S' is different from the current state S, where 'different' means Erlang's strict inequality: `=/=` also known as 'does not match'. gen_statem does more things during state changes than during other state transitions."

# Relationships

## Builds Upon
- None within this source -- this is the foundational theoretical model.

## Enables
- **gen_statem** -- The OTP behaviour that implements this model.
- **Transition actions** -- The "Actions(A)" component of the model.
- **State callback** -- The code that implements the state-event-action relations.

## Related
- **gen_statem** -- The OTP behaviour implementing event-driven state machines.

## Contrasts With
- None explicitly within this source.

# Common Errors

- **Error**: Treating every state callback return as a "state change."
  **Correction**: Only when `S' =/= S` (the new state is different from the current state) does gen_statem consider it a state change. Returning to the same state is a state transition but not a state change. This distinction matters because state changes trigger retry of postponed events, cancel state timeouts, and invoke state enter calls.

# Common Confusions

- **Confusion**: The event-driven state machine model is limited to a finite number of states.
  **Clarification**: While based on Finite State Machine theory, gen_statem augments the model with server Data, making it Turing complete. "There is no restriction on the number of states (assuming sufficient virtual machine memory), or on the number of distinct input events."

# Source Reference

Described in the "Event-Driven State Machines" section at the beginning of the gen_statem Behaviour chapter, including the formal model, Mealy machine classification, and the "Everyday State Machine" ballpoint pen example.

# Verification Notes

- Definition source: Directly quoted from the "Event-Driven State Machines" section of statem.md.
- Confidence rationale: High -- the model is explicitly defined with formal notation and examples.
- Uncertainties: None.
- Cross-reference status: Foundational concept referenced by all other gen_statem cards.
