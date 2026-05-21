---
# === CORE IDENTIFICATION ===
concept: State Callback
slug: state-callback

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
section: "State Callback"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "state callback function"
  - "event-handling callback function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - callback-mode
extends: []
related:
  - state-functions-mode
  - handle-event-function-mode
  - transition-actions
  - event-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a gen_statem state machine?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

The state callback is the callback function that handles an event in the current state of a `gen_statem`, with its form depending on the callback mode: `Module:StateName/3` in `state_functions` mode or `Module:handle_event/4` in `handle_event_function` mode.

# Core Definition

As stated in the OTP Design Principles: "The state callback is the callback function that handles an event in the current state, and which function that is depends on the callback mode." In `state_functions` mode, the signature is `Module:StateName(EventType, EventContent, Data)`. In `handle_event_function` mode, it is `Module:handle_event(EventType, EventContent, State, Data)`. The function receives the event type, event content, and current server data (plus state in handle_event_function mode), and returns a tuple specifying the next state, updated data, and optional transition actions.

# Prerequisites

- **gen_statem** -- The behaviour whose engine calls state callbacks.
- **Callback mode** -- Determines which function form is used as the state callback.

# Key Properties

1. In `state_functions` mode: `StateName(EventType, EventContent, Data)`.
2. In `handle_event_function` mode: `handle_event(EventType, EventContent, State, Data)`.
3. Also handles state enter calls when enabled (with `enter` as the EventType and `OldState` as EventContent).
4. The `init/1` callback decides the first state and behaves like a state callback returning `{ok, State, Data}` or `{ok, State, Data, Actions}`.

# Key Return Values

1. `{next_state, NextState, NewData [, Actions]}` -- Set next state and update data. If `NextState =/= State`, it is a state change.
2. `{keep_state, NewData [, Actions]}` -- Same as next_state with `NextState =:= State` (no state change).
3. `keep_state_and_data | {keep_state_and_data, Actions}` -- No change to state or data.
4. `{repeat_state, NewData [, Actions]}` -- Like keep_state but repeats state enter call if enabled.
5. `repeat_state_and_data | {repeat_state_and_data, Actions}` -- Like keep_state_and_data but repeats enter call.
6. `{stop, Reason [, NewData]}` -- Stop the server.
7. `{stop_and_reply, Reason, [NewData,] ReplyActions}` -- Stop after sending replies.

# Construction / Recognition

## To Construct/Create:
1. Define the function matching the chosen callback mode signature.
2. Pattern match on EventType and EventContent to handle different events.
3. Return an appropriate tuple with the next state, data, and optional actions.
4. Handle state enter calls (if enabled) as the first clause: `StateName(enter, OldState, Data)`.

## To Identify/Recognize:
1. Functions exported with arity 3 matching state names (state_functions mode).
2. A single `handle_event/4` export (handle_event_function mode).
3. Return values are tuples starting with `next_state`, `keep_state`, `stop`, etc.

# Context & Application

State callbacks are the core of a gen_statem implementation -- they define all the behavior of the state machine. Every event received by the gen_statem engine is dispatched to a state callback. The callback must handle the event and return the next state, updated data, and any transition actions.

# Examples

**Example 1** (statem.md, "State Callback"): Return value demonstrating a state change:

```erlang
locked(cast, {button,Button}, #{code := Code} = Data) ->
    ...
    if
        NewButtons =:= Code ->
            {next_state, open, Data#{buttons := []},
             [{state_timeout,10_000,lock}]};
        true ->
            {next_state, locked, Data#{buttons := NewButtons}}
    end.
```

**Example 2** (statem.md, "State Callback"): Using keep_state_and_data:

```erlang
open(cast, {button,_}, Data) ->
    {next_state, open, Data}.
%% equivalent to: {keep_state, Data} or keep_state_and_data
```

**Example 3** (statem.md, "The First State"): The init/1 callback acting as the first state callback:

```erlang
init(Code) ->
    do_lock(),
    Data = #{code => Code, length => length(Code), buttons => []},
    {ok, locked, Data}.
```

# Relationships

## Builds Upon
- **gen_statem** -- State callbacks are called by the gen_statem engine.
- **Callback mode** -- Determines the function signature of the state callback.

## Enables
- **Transition actions** -- Returned in the actions list from state callbacks.
- **Postponing events** -- Ordered by returning the `postpone` action.
- **State enter calls** -- Handled by the state callback with special arguments.

## Related
- **State functions mode** -- One state callback function per state.
- **Handle event function mode** -- One state callback function for all states.
- **Event types** -- EventType is the first argument to state callbacks.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Returning `{next_state, SameState, Data}` when `{keep_state, Data}` is intended, not realizing both are equivalent when the state is unchanged.
  **Correction**: While functionally equivalent for non-state-change transitions, use `keep_state` or `keep_state_and_data` for clarity when you intend to stay in the current state, especially in handle_event_function mode where you might not have the state name readily available.

- **Error**: Using the `postpone` action from `init/1`.
  **Correction**: "If you use the postpone action from this function, that action is ignored, since there is no event to postpone."

# Common Confusions

- **Confusion**: `keep_state` and `next_state` with the same state are different.
  **Clarification**: `{keep_state, NewData}` is "Same as the next_state values with NextState =:= State, that is, no state change." They produce identical behavior. `keep_state` is a convenience form.

- **Confusion**: `repeat_state` is the same as `keep_state`.
  **Clarification**: `repeat_state` is "Same as the keep_state values, but if state enter calls are enabled; repeat it as if this state was entered again." Without state enter calls enabled, they are identical.

# Source Reference

Described in the "State Callback" section and "The First State" subsection of the gen_statem Behaviour chapter, with return values enumerated.

# Verification Notes

- Definition source: Directly from the "State Callback" section of statem.md including all return value forms.
- Confidence rationale: High -- explicitly defined with complete enumeration of return value forms.
- Uncertainties: None.
- Cross-reference status: References gen-statem, callback-mode, transition-actions, event-types.
