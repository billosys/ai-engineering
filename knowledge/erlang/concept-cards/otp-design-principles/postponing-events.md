---
# === CORE IDENTIFICATION ===
concept: Postponing Events
slug: postponing-events

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
section: "Postponing Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "postpone"
  - "event postponing"
  - "deferred events"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - state-callback
  - transition-actions
extends: []
related:
  - event-driven-state-machine
  - event-timeout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use postponing events in gen_statem?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

Postponing events in `gen_statem` defers the current event to be automatically retried after the next state change (`OldState =/= NewState`), serving as a structured substitute for Erlang's selective receive.

# Core Definition

As described in the OTP Design Principles: "If you want to ignore a particular event in the current state and handle it in a future state, you can postpone the event. A postponed event is retried after a state change, that is, OldState =/= NewState." Postponing is ordered by the transition action `postpone` (or `{postpone, true}`). The source further states that "The transition action postpone is designed to model selective receives."

# Prerequisites

- **gen_statem** -- The behaviour that manages the queue of postponed events.
- **State callback** -- The function from which postpone is returned as a transition action.
- **Transition actions** -- Postpone is one of the available transition actions.

# Key Properties

1. Ordered by the transition action `postpone` or `{postpone, true}` in the actions list.
2. Postponed events are retried only after a state change (`OldState =/= NewState`), not after every state transition.
3. On state change, the event queue is restarted from the oldest postponed event.
4. Acts as a substitute for Erlang's selective receive.
5. Both mechanisms (postpone and selective receive) have the same theoretical time and memory complexity, but selective receive has smaller constant factors.
6. Postponed events cancel event timeouts just as external events do.
7. Cannot be used from `init/1` (the action is ignored since there is no event to postpone).

# Construction / Recognition

## To Construct/Create:
1. Return the `postpone` atom or `{postpone, true}` in the transition actions list.
2. Ensure the state will eventually change so postponed events are retried.

```erlang
open(cast, {button,_}, Data) ->
    {keep_state, Data, [postpone]};
```

## To Identify/Recognize:
1. The `postpone` action in a state callback's return value.
2. Events that are not handled in the current state but expected to be handled after a state change.

# Context & Application

Postponing is used when an event is valid but cannot be handled in the current state. The source demonstrates this with the code_lock example: button presses while the door is open are postponed until the door returns to the locked state. The design decision of what belongs in the state vs. server data is important: "If a change in the value changes the set of events that is handled, the value should be in the State. Otherwise no postponed events will be retried since only the server Data changes."

# Examples

**Example 1** (statem.md, "Postponing Events"): Postponing button events in the open state:

```erlang
open(cast, {button,_}, Data) ->
    {keep_state, Data, [postpone]};
```

**Example 2** (statem.md, "Selective Receive"): The source compares postponing to selective receive. In the plain Erlang version, the `open` function uses `receive after` which implicitly postpones all messages:

```erlang
open(Code, Length) ->
    receive
    after 10_000 ->
        do_lock(),
        locked(Code, Length, [])
    end.
```

"The selective receive in this case causes open to implicitly postpone any events to the locked state."

**Example 3** (statem.md, "Example Revisited"): In the full example, internal button events are postponed in the open state:

```erlang
open(internal, {button,_}, _) ->
    {keep_state_and_data, [postpone]};
```

# Relationships

## Builds Upon
- **Transition actions** -- Postpone is a transition action returned from state callbacks.
- **gen_statem** -- The engine manages the postponed event queue.
- **State callback** -- The function that returns the postpone action.

## Enables
- Modeling selective receive behavior within the gen_statem framework.
- Handling events in a future state without losing them.

## Related
- **Event-driven state machine** -- Postponing is related to the concept of state changes triggering different event handling.
- **Event timeout** -- Postponed events cancel event timeouts.

## Contrasts With
- None directly, though it is an alternative to Erlang's selective receive mechanism.

# Common Errors

- **Error**: Expecting postponed events to be retried when only server Data changes (not State).
  **Correction**: "A postponed event is only retried after a state change." If the value that changes the set of handled events is kept in Data rather than State, postponed events will never be retried. "If a change in the value changes the set of events that is handled, the value should be in the State."

- **Error**: Combining postpone with event timeouts.
  **Correction**: "Note that postponed and inserted events cancel this time-out [event timeout] just as external events do." A postponed event retried during a state change will cancel any event timeout started in the same transition.

- **Error**: Postponing events without ever changing state, creating a memory leak.
  **Correction**: Ensure the state machine will eventually perform a state change so postponed events are retried. Otherwise postponed events accumulate indefinitely.

# Common Confusions

- **Confusion**: Postponed events are retried on every state transition.
  **Clarification**: Postponed events are retried only after a state change (where `OldState =/= NewState`), not after every callback return. Returning `keep_state` does not trigger retry of postponed events.

- **Confusion**: Postpone drops the event.
  **Clarification**: Postpone defers the event -- it is stored and will be retried after the next state change. It is not discarded.

# Source Reference

Described in the "Postponing Events" section, including the "Fuzzy State Diagrams" and "Selective Receive" subsections of the gen_statem Behaviour chapter.

# Verification Notes

- Definition source: Directly from the "Postponing Events" section of statem.md.
- Confidence rationale: High -- explicitly defined with clear semantics, examples, and comparison to selective receive.
- Uncertainties: None.
- Cross-reference status: References gen-statem, state-callback, transition-actions, event-timeout, event-driven-state-machine.
