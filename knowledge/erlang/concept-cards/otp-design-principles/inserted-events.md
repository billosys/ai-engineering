---
# === CORE IDENTIFICATION ===
concept: Inserted Events
slug: inserted-events

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: state-machine
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_statem Behaviour"
chapter_number: null
pdf_page: null
section: "Inserted Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "next_event action"
  - "self-generated events"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - state-callback
  - transition-actions
  - event-types
extends: []
related:
  - state-enter-calls
  - postponing-events
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a gen_statem state machine?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

Inserted events are events that a `gen_statem` generates to itself using the `{next_event, EventType, EventContent}` transition action, enabling self-messaging and pre-processing patterns, with the `internal` event type being exclusive to this mechanism.

# Core Definition

As described in the OTP Design Principles: "It can sometimes be beneficial to be able to generate events to your own state machine. This can be done with the transition action `{next_event, EventType, EventContent}`." The source further explains: "You can generate events of any existing type, but the internal type can only be generated through action next_event. Hence, it cannot come from an external source, so you can be certain that an internal event is an event from your state machine to itself."

# Prerequisites

- **gen_statem** -- The behaviour that processes inserted events.
- **State callback** -- The function that returns next_event actions and handles inserted events.
- **Transition actions** -- next_event is a transition action.
- **Event types** -- Inserted events have an event type, including the exclusive `internal` type.

# Key Properties

1. Created via the transition action `{next_event, EventType, EventContent}`.
2. Can generate events of any existing event type (cast, call, info, timeout types, internal).
3. The `internal` event type can only be generated through `next_event` -- guaranteeing it is self-originated.
4. Inserted events are stored and inserted all together during the state transition.
5. Inserted events are processed before any external events in the queue.
6. Inserted events cancel event timeouts just like external events do.
7. Cannot be inserted from a state enter call.
8. Multiple next_event actions can be returned in a single actions list.

# Construction / Recognition

## To Construct/Create:
1. Return `{next_event, EventType, EventContent}` in the transition actions list.
2. Use `internal` as the EventType for events that should be provably self-generated.
3. Handle the inserted event in the appropriate state callback clause.

## To Identify/Recognize:
1. The `{next_event, ...}` action in a transition actions list.
2. State callback clauses matching `internal` as the EventType.
3. Event handling patterns where external input is pre-processed and re-dispatched.

# Context & Application

Inserted events are useful for pre-processing incoming data (e.g., decrypting chunks, collecting characters), or for decomposing complex event handling into multiple stages. The source notes: "Using internal events also can make it easier to synchronize the state machines." A variant is to use a complex state with one state callback, modeling state with tuples like `{MainFSMState, SubFSMState}`.

# Examples

**Example 1** (statem.md, "Inserted Events"): Converting button down/up events into internal button events:

```erlang
handle_common(cast, {down,Button}, Data) ->
    {keep_state, Data#{button => Button}};
handle_common(cast, {up,Button}, Data) ->
    case Data of
        #{button := Button} ->
            {keep_state, maps:remove(button, Data),
             [{next_event,internal,{button,Button}}]};
        #{} ->
            keep_state_and_data
    end;
```

**Example 2** (statem.md, "Inserted Events"): The locked state handles the internal button event:

```erlang
locked(internal, {button,Button},
  #{code := Code, length := Length, buttons := Buttons} = Data) ->
    ...
```

**Example 3** (statem.md, "Inserted Events"): Postponing internal events in the open state for later handling:

```erlang
open(internal, {button,_}, Data) ->
    {keep_state, Data, [postpone]};
```

# Relationships

## Builds Upon
- **Transition actions** -- next_event is a transition action.
- **Event types** -- Inserted events have event types, with `internal` being exclusive.
- **State callback** -- Returns next_event actions and handles inserted events.
- **gen_statem** -- The engine that queues and dispatches inserted events.

## Enables
- Pre-processing patterns where external events are transformed into internal events.
- Sub-state-machine integration within a single gen_statem process.
- Synchronization between logical sub-machines within a process.

## Related
- **State enter calls** -- An alternative mechanism for state entry logic (inserted events cannot be used from enter calls, but enter calls can sometimes replace the need for inserted events).
- **Postponing events** -- Inserted events can be postponed like any other event.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Inserting events from a state enter call.
  **Correction**: State enter calls have restrictions -- you "must not...insert any events." Use inserted events only from regular event-handling callback returns.

- **Error**: Forgetting that inserted events cancel event timeouts.
  **Correction**: Inserted events cancel event timeouts "just as external events do." If you combine next_event with an event timeout in the same transition, the inserted event will cancel the timeout.

# Common Confusions

- **Confusion**: Inserted events are placed at the end of the event queue.
  **Clarification**: Inserted events are processed before any external events already in the queue, similar to how zero-time timeouts are "immediately inserted to be processed after any events already enqueued, and before any not yet received external events."

- **Confusion**: `internal` events can come from outside the process.
  **Clarification**: "The internal type can only be generated through action next_event. Hence, it cannot come from an external source, so you can be certain that an internal event is an event from your state machine to itself."

# Source Reference

Described in the "Inserted Events" section of the gen_statem Behaviour chapter, with the button down/up pre-processing example.

# Verification Notes

- Definition source: Directly from the "Inserted Events" section of statem.md.
- Confidence rationale: High -- explicitly defined with clear semantics and a detailed pre-processing example.
- Uncertainties: None.
- Cross-reference status: References gen-statem, state-callback, transition-actions, event-types, state-enter-calls, postponing-events.
