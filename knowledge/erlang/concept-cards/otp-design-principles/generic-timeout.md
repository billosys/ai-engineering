---
# === CORE IDENTIFICATION ===
concept: Generic Timeout
slug: generic-timeout

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
section: "Generic Time-Outs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "generic time-out"
  - "named timeout"
  - "{timeout, Name}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - transition-actions
  - event-types
extends: []
related:
  - state-callback
contrasts_with:
  - state-timeout
  - event-timeout

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes state_timeout from event_timeout in gen_statem?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

A generic timeout in `gen_statem` is a named timer that has no automatic cancellation, allowing multiple named timeouts to run simultaneously across state changes and events, generating a `{timeout, Name}` event when expired.

# Core Definition

As described in the OTP Design Principles: "There are any number of generic time-outs differing by their Name. They have no automatic canceling." Generic timeouts "may look a little bit like event time-outs but contain a name to allow for any number of them simultaneously and they are not automatically canceled." They are started via the transition action `{{timeout, Name}, Time, EventContent}`.

# Prerequisites

- **gen_statem** -- The behaviour that manages generic timeouts.
- **Transition actions** -- Generic timeout is started via a transition action.
- **Event types** -- Expiry generates a `{timeout, Name}` event type.

# Key Properties

1. Named by any Erlang term (the `Name` in `{timeout, Name}`).
2. Multiple generic timeouts with different names can run simultaneously.
3. No automatic cancellation -- not canceled by state changes or events.
4. Started via transition action `{{timeout, Name}, Time, EventContent [, Opts]}`.
5. Can be explicitly canceled with `{{timeout, Name}, cancel}` or by starting with time `infinity`.
6. Can be updated (change EventContent without resetting timer) with `{{timeout, Name}, update, NewEventContent}`.
7. Starting a new timeout with the same name cancels the previous one with that name.
8. Generates event with EventType `{timeout, Name}`.

# Construction / Recognition

## To Construct/Create:
1. Return `{{timeout, Name}, Time, EventContent}` in the transition actions list.
2. Handle the timeout in the state callback: `StateName({timeout, Name}, EventContent, Data)`.
3. Optionally cancel with `{{timeout, Name}, cancel}` or by starting with `infinity`.

## To Identify/Recognize:
1. Transition action tuple starting with `{timeout, Name}`.
2. State callback clause matching `{timeout, Name}` as the EventType.
3. Timer that must survive both state changes and incoming events.

# Context & Application

Generic timeouts fill the gap between state timeouts (canceled on state change) and event timeouts (canceled on any event). They are needed "if the state machine stays in the same state during the time-out time" is not guaranteed, or "if no disturbing unrelated events occur" is not guaranteed. Use cases include timeouts that span multiple states, multiple concurrent timers, or timers that should not be affected by unrelated events.

# Examples

**Example 1** (statem.md, "Generic Time-Outs"): Using a generic timeout named `open` instead of a state timeout:

```erlang
locked(cast, {button,Button}, #{code := Code} = Data) ->
    ...
    if
        NewButtons =:= Code ->
            do_unlock(),
            {next_state, open, Data#{buttons := []},
             [{{timeout,open},10_000,lock}]};
        ...

open({timeout,open}, lock, Data) ->
    do_lock(),
    {next_state, locked, Data};
open(cast, {button,_}, Data) ->
    {keep_state, Data};
```

**Example 2** (statem.md, "Generic Time-Outs"): The source explains: "Instead of bothering with when to cancel a time-out, a late time-out event can be handled by ignoring it if it arrives in a state where it is known to be late."

# Relationships

## Builds Upon
- **Transition actions** -- Generic timeout is started as a transition action.
- **Event types** -- Expiry generates the `{timeout, Name}` event type.
- **gen_statem** -- The engine manages named timers.

## Enables
- Cross-state timers that survive state changes.
- Multiple concurrent timers with different names.
- Timers unaffected by unrelated events.

## Related
- **State callback** -- Handles the `{timeout, Name}` event.

## Contrasts With
- **State timeout** -- State timeout is automatically canceled on state change; generic timeout is not. Only one state timeout can exist; multiple generic timeouts can coexist.
- **Event timeout** -- Event timeout is automatically canceled by any event; generic timeout is not. Only one event timeout can exist; multiple generic timeouts can coexist.

# Common Errors

- **Error**: Forgetting to cancel a generic timeout when it is no longer needed.
  **Correction**: Unlike state and event timeouts, generic timeouts have no automatic cancellation. Either cancel them explicitly with `{{timeout, Name}, cancel}`, or handle late timeout events by ignoring them in states where they are known to be irrelevant.

- **Error**: Assuming different EventContent values create different timeouts.
  **Correction**: Timeouts are identified by their type and name. "Different EventContents do not create different time-outs." Starting a timeout with the same name replaces the previous one.

# Common Confusions

- **Confusion**: Generic timeouts are canceled when the state changes.
  **Clarification**: "They have no automatic canceling." Generic timeouts persist across state changes and events. This is their key differentiator from state timeouts and event timeouts.

- **Confusion**: Generic timeout is the same as using `erlang:start_timer/3`.
  **Clarification**: Generic timeouts are managed by the gen_statem engine and produce `{timeout, Name}` events. Erlang timers produce `info` events with `{timeout, Tref, Msg}` format and offer `erlang:cancel_timer/1` which returns remaining time -- a feature gen_statem timeouts lack.

# Source Reference

Described in the "Generic Time-Outs" section and the "Time-Outs" section of the gen_statem Behaviour chapter.

# Verification Notes

- Definition source: Directly from the "Generic Time-Outs" and "Time-Outs" sections of statem.md.
- Confidence rationale: High -- explicitly defined with clear semantics and comparison to other timeout types.
- Uncertainties: None.
- Cross-reference status: References gen-statem, transition-actions, event-types; contrasts with state-timeout and event-timeout.
