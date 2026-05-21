---
# === CORE IDENTIFICATION ===
concept: State Timeout
slug: state-timeout

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: state-machine
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_statem Behaviour"
chapter_number: null
pdf_page: null
section: "State Time-Outs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "state time-out"
  - "state_timeout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - transition-actions
  - event-types
extends: []
related:
  - state-callback
  - state-enter-calls
contrasts_with:
  - event-timeout
  - generic-timeout

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes state_timeout from event_timeout in gen_statem?"
  - "How do I implement a gen_statem state machine?"
---

# Quick Definition

A state timeout in `gen_statem` is a timer that is automatically canceled when a state change occurs, generating a `state_timeout` event if the state machine remains in the same state for the specified duration.

# Core Definition

As described in the OTP Design Principles: "There is one state time-out that is automatically canceled by a state change." The timeout is started via the transition action `{state_timeout, Time, EventContent}`. When it expires, it generates an event with EventType `state_timeout` and the specified EventContent. The source explains: "The timer for a state time-out is automatically canceled when the state machine does a state change."

# Prerequisites

- **gen_statem** -- The behaviour that manages state timeouts.
- **Transition actions** -- State timeout is started via a transition action.
- **Event types** -- Expiry generates a `state_timeout` event type.

# Key Properties

1. Only one state timeout can be active at a time.
2. Automatically canceled on any state change (`OldState =/= NewState`).
3. Started via transition action `{state_timeout, Time, EventContent [, Opts]}`.
4. Can be restarted by starting a new state timeout (previous one is canceled).
5. Can be explicitly canceled with `{state_timeout, cancel}` or by starting with time `infinity`.
6. Can be updated (change EventContent without resetting the timer) with `{state_timeout, update, NewEventContent}`.
7. Time is specified in milliseconds.
8. Time value of `0` inserts the timeout event immediately rather than starting a timer.

# Construction / Recognition

## To Construct/Create:
1. Return `{state_timeout, Time, EventContent}` in the transition actions list.
2. Handle the timeout in the state callback: `StateName(state_timeout, EventContent, Data)`.

## To Identify/Recognize:
1. Transition action tuple starting with `state_timeout`.
2. State callback clause matching `state_timeout` as the EventType.
3. Timer that should be canceled when leaving the current state.

# Context & Application

State timeouts are ideal for implementing "time spent in a state" semantics. The code_lock example uses a state timeout to automatically relock the door after 10 seconds in the `open` state. Because the timeout is automatically canceled on state change, there is no need to manually cancel it when leaving the state.

# Examples

**Example 1** (statem.md, "State Time-Outs"): Starting a 10-second state timeout when transitioning to open:

```erlang
{next_state, open, Data#{buttons := []},
 [{state_timeout,10_000,lock}]}
```

**Example 2** (statem.md, "State Time-Outs"): Handling the state timeout to relock the door:

```erlang
open(state_timeout, lock, Data) ->
    do_lock(),
    {next_state, locked, Data};
```

**Example 3** (statem.md, "State Enter Actions"): Starting the state timeout from a state enter call:

```erlang
open(enter, _OldState, _Data) ->
    do_unlock(),
    {keep_state_and_data,
     [{state_timeout,10_000,lock}]};
```

# Relationships

## Builds Upon
- **Transition actions** -- State timeout is started as a transition action.
- **Event types** -- Expiry generates the `state_timeout` event type.
- **gen_statem** -- The engine manages the timer and automatic cancellation.

## Enables
- Time-bounded state behavior (e.g., auto-locking after a period).

## Related
- **State callback** -- Handles the state_timeout event.
- **State enter calls** -- State timeouts are commonly started from state enter calls.

## Contrasts With
- **Event timeout** -- Event timeout is canceled by any event (not just state changes). There is one of each. State timeout persists across events within the same state.
- **Generic timeout** -- Generic timeouts are never automatically canceled. They are named and multiple can be active simultaneously.

# Common Errors

- **Error**: Expecting a state timeout to persist across state changes.
  **Correction**: "The timer for a state time-out is automatically canceled when the state machine does a state change." If you need a timeout that survives state changes, use a generic timeout or an Erlang timer.

- **Error**: Starting a state timeout with time `0` and expecting a timer.
  **Correction**: A time of `0` causes the timeout event to be "immediately inserted to be processed after any events already enqueued, and before any not yet received external events" -- no timer is actually started.

# Common Confusions

- **Confusion**: State timeout and event timeout serve the same purpose.
  **Clarification**: State timeout measures "time in a state" and is only canceled by state changes. Event timeout measures "time since last event" and is canceled by any event (including postponed and inserted events). They are different tools for different use cases.

# Source Reference

Described in the "State Time-Outs" section and the "Time-Outs" section of the gen_statem Behaviour chapter. The code_lock example uses state timeouts throughout.

# Verification Notes

- Definition source: Directly from the "State Time-Outs" and "Time-Outs" sections of statem.md.
- Confidence rationale: High -- explicitly defined with clear cancellation semantics and multiple code examples.
- Uncertainties: None.
- Cross-reference status: References gen-statem, transition-actions, event-types; contrasts with event-timeout and generic-timeout.
