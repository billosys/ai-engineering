---
# === CORE IDENTIFICATION ===
concept: Event Timeout
slug: event-timeout

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
section: "Event Time-Outs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "event time-out"
  - "event_timeout"
  - "inactivity timeout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - transition-actions
  - event-types
extends: []
related:
  - postponing-events
  - inserted-events
contrasts_with:
  - state-timeout
  - generic-timeout

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes state_timeout from event_timeout in gen_statem?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

An event timeout in `gen_statem` is a timer that is automatically canceled by any event (including postponed and inserted events), useful for detecting inactivity, and generating a `timeout` event if no other event arrives within the specified duration.

# Core Definition

As described in the OTP Design Principles: "A time-out feature inherited from gen_statem's predecessor gen_fsm, is an event time-out, that is, if an event arrives the timer is canceled. You get either an event or a time-out, but not both." It is ordered by the transition action `{timeout, Time, EventContent}` or just an integer `Time`. The source further explains: "An event time-out is canceled by any other event so you either get some other event or the time-out event. Therefore, canceling, restarting, or updating an event time-out is neither possible nor necessary."

# Prerequisites

- **gen_statem** -- The behaviour that manages event timeouts.
- **Transition actions** -- Event timeout is started via a transition action.
- **Event types** -- Expiry generates a `timeout` event type.

# Key Properties

1. Only one event timeout can be active at a time.
2. Automatically canceled by any event: external events, postponed events retried after state change, and inserted events.
3. Started via transition action `{timeout, Time, EventContent [, Opts]}` or just `Time` (integer).
4. Cannot be explicitly canceled, restarted, or updated -- this is unnecessary since any event cancels it.
5. There is never a running event timeout while the state callback executes (any event that triggered the callback already canceled it).
6. Generates event with EventType `timeout`.
7. Inherited from the predecessor behaviour `gen_fsm`.
8. The shorthand form (just an integer) works even without an enclosing actions list.

# Construction / Recognition

## To Construct/Create:
1. Return `{timeout, Time, EventContent}` in the transition actions list, or just return the integer `Time`.
2. Handle the timeout in the state callback: `StateName(timeout, EventContent, Data)`.

## To Identify/Recognize:
1. Transition action tuple `{timeout, Time, EventContent}` (not `{state_timeout, ...}` or `{{timeout, Name}, ...}`).
2. State callback clause matching `timeout` as the EventType.
3. Timer that should reset whenever any event occurs (inactivity detection).

# Context & Application

Event timeouts are useful for acting on inactivity. The source demonstrates using an event timeout to reset the code sequence if no button is pressed for 30 seconds. However, the source warns: "An event time-out does not work well when you have for example a status call as in section All State Events, or handle unknown events, since all kinds of events will cancel the event time-out."

# Examples

**Example 1** (statem.md, "Event Time-Outs"): Resetting the button sequence after 30 seconds of inactivity:

```erlang
locked(timeout, _, Data) ->
    {next_state, locked, Data#{buttons := []}};
locked(
  cast, {button,Button},
  #{code := Code, length := Length, buttons := Buttons} = Data) ->
    ...
        true -> % Incomplete | Incorrect
            {next_state, locked, Data#{buttons := NewButtons},
             30_000} % Time in milliseconds
    ...
```

**Example 2** (statem.md, "Event Time-Outs"): The source explains the pattern: "Whenever we receive a button event we start an event time-out of 30 seconds, and if we get an event type of timeout we reset the remaining code sequence."

# Relationships

## Builds Upon
- **Transition actions** -- Event timeout is started as a transition action.
- **Event types** -- Expiry generates the `timeout` event type.
- **gen_statem** -- The engine manages the timer and automatic cancellation.

## Enables
- Inactivity detection patterns.
- Sequence reset on idle (as in the code_lock example).

## Related
- **Postponing events** -- Postponed events cancel event timeouts when retried.
- **Inserted events** -- Inserted events cancel event timeouts.

## Contrasts With
- **State timeout** -- State timeout is canceled only by state changes, not by events. State timeout measures "time in a state"; event timeout measures "time since last event."
- **Generic timeout** -- Generic timeout is never automatically canceled by either events or state changes. It must be explicitly managed.

# Common Errors

- **Error**: Using event timeouts alongside "all state events" handlers (like status calls).
  **Correction**: "An event time-out does not work well when you have for example a status call...since all kinds of events will cancel the event time-out." Any event, including unrelated ones, cancels the event timeout.

- **Error**: Combining a state change with postponed events and a zero event timeout.
  **Correction**: "If you for example combine postponing an event in a state change with starting an event time-out with time 0 there will be no time-out event inserted since the event time-out is canceled by the postponed event that is delivered due to the state change."

# Common Confusions

- **Confusion**: Event timeout can be canceled or restarted explicitly.
  **Clarification**: "Canceling, restarting, or updating an event time-out is neither possible nor necessary. Whatever event you act on has already canceled the event time-out, so there is never a running event time-out while the state callback executes."

- **Confusion**: Event timeout measures time in a state.
  **Clarification**: Event timeout measures time since the last event of any kind. It is an inactivity timer. For time-in-state semantics, use state timeout.

# Source Reference

Described in the "Event Time-Outs" section of the gen_statem Behaviour chapter, with the 30-second inactivity example for the code_lock.

# Verification Notes

- Definition source: Directly from the "Event Time-Outs" section of statem.md.
- Confidence rationale: High -- explicitly defined with clear cancellation semantics, limitations, and examples.
- Uncertainties: None.
- Cross-reference status: References gen-statem, transition-actions, event-types; contrasts with state-timeout and generic-timeout.
