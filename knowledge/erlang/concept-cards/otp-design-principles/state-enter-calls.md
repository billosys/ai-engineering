---
# === CORE IDENTIFICATION ===
concept: State Enter Calls
slug: state-enter-calls

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
section: "State Enter Calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "state enter call"
  - "state enter actions"
  - "enter callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - callback-mode
  - state-callback
extends:
  - state-callback
related:
  - transition-actions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use state enter calls in gen_statem?"
  - "How do I implement a gen_statem state machine?"
---

# Quick Definition

State enter calls are optional automatic invocations of the state callback with special arguments `(enter, OldState, ...)` that occur whenever a `gen_statem` performs a state change, enabling state entry actions to be co-located with the rest of the state's callback code.

# Core Definition

As described in the OTP Design Principles: "The gen_statem behaviour can, if this is enabled, regardless of callback mode, automatically call the state callback with special arguments whenever the state changes, so you can write state enter actions near the rest of the state transition rules." The feature is enabled by returning a list containing `state_enter` from `callback_mode/0`, e.g., `[state_functions, state_enter]`.

# Prerequisites

- **gen_statem** -- The behaviour providing state enter call functionality.
- **Callback mode** -- Must include `state_enter` in the callback_mode return value.
- **State callback** -- The function that handles both regular events and enter calls.

# Key Properties

1. Enabled by including `state_enter` in the `callback_mode/0` return list.
2. Called with `(enter, OldState, Data)` in state_functions mode, or `(enter, OldState, State, Data)` in handle_event_function mode.
3. The state enter call is not an event -- it has restrictions on return values and actions.
4. Restrictions: must not change the state, must not postpone, must not insert events, must not change the callback module.
5. The first state entered after `init/1` gets a state enter call with `OldState` equal to the current state.
6. Can be repeated using `{repeat_state, ...}` or `repeat_state_and_data` return values, in which case `OldState` equals the current state.
7. Forces you to handle state enter calls in all states.

# Construction / Recognition

## To Construct/Create:
1. Return `[state_functions, state_enter]` or `[handle_event_function, state_enter]` from `callback_mode/0`.
2. Add an enter clause as the first clause of each state function:
   ```erlang
   StateName(enter, OldState, Data) ->
       ... state enter actions ...
       {keep_state, NewData};
   ```
3. Handle the enter call in every state (this is mandatory when enabled).

## To Identify/Recognize:
1. `callback_mode/0` returns a list containing `state_enter`.
2. State callbacks have clauses matching `enter` as the EventType.
3. Enter clauses return `keep_state` or `keep_state_and_data` (never `next_state` with a different state).

# Context & Application

State enter calls are useful when a state machine specification uses state entry actions. They enable co-locating entry logic with the state's event handling code. Common use cases include initializing state-specific resources, starting state-specific timeouts, and performing entry actions like locking/unlocking a door. "Depending on how your state machine is specified, this can be a very useful feature, but it forces you to handle the state enter calls in all states."

# Examples

**Example 1** (statem.md, "State Enter Calls"): Basic state enter call pattern:

```erlang
StateName(enter, OldState, Data) ->
    ... code for state enter actions here ...
    {keep_state, NewData};
StateName(EventType, EventContent, Data) ->
    ... code for actions here ...
    {next_state, NewStateName, NewData}.
```

**Example 2** (statem.md, "State Enter Actions"): The code_lock example with state enter calls:

```erlang
callback_mode() ->
    [state_functions, state_enter].

locked(enter, _OldState, Data) ->
    do_lock(),
    {keep_state, Data#{buttons => []}};
locked(cast, {button,Button}, #{code := Code} = Data) ->
    ...

open(enter, _OldState, _Data) ->
    do_unlock(),
    {keep_state_and_data,
     [{state_timeout,10_000,lock}]};
open(state_timeout, lock, Data) ->
    {next_state, locked, Data}.
```

**Example 3** (statem.md, "State Enter Calls"): First state after init gets enter call with OldState equal to current state: "The first state that is entered after init/1 will get a state enter call with OldState equal to the current state."

# Relationships

## Builds Upon
- **State callback** -- State enter calls are handled by the same state callback functions.
- **Callback mode** -- Must include `state_enter` to enable this feature.
- **gen_statem** -- The engine that automatically invokes enter calls on state changes.

## Enables
- Clean separation of state entry logic from event handling logic within the same function.
- Initialization of state-specific timeouts and resources.

## Related
- **Transition actions** -- Limited set of actions allowed from state enter calls (no postpone, no next_event, no callback module changes).

## Contrasts With
- None directly, though inserted events can sometimes serve as an alternative for state entry logic.

# Common Errors

- **Error**: Attempting to change state from a state enter call.
  **Correction**: "You must not change the state" from an enter call. Return `{keep_state, NewData}` or `keep_state_and_data` only.

- **Error**: Attempting to postpone or insert events from a state enter call.
  **Correction**: "Since the state enter call is not an event there are restrictions...You must not...postpone this non-event, insert any events, or change the callback module."

- **Error**: Not handling enter calls in all states.
  **Correction**: When state enter calls are enabled, every state must handle the `enter` event type. Failing to do so will cause a function clause error.

# Common Confusions

- **Confusion**: State enter calls happen on every state transition.
  **Clarification**: State enter calls happen only on state changes (`S' =/= S`), not on every state transition. Returning `keep_state` does not trigger an enter call. Use `repeat_state` to explicitly re-trigger the enter call.

- **Confusion**: `repeat_state` and `keep_state` are equivalent.
  **Clarification**: With state enter calls enabled, `repeat_state` triggers a re-entry call (with `OldState` equal to the current state), while `keep_state` does not.

# Source Reference

Described in the "State Enter Calls" section and the "State Enter Actions" section of the gen_statem Behaviour chapter. Also demonstrated in the "Example Revisited" section.

# Verification Notes

- Definition source: Directly from the "State Enter Calls" and "State Enter Actions" sections of statem.md.
- Confidence rationale: High -- explicitly defined with restrictions enumerated and complete code examples.
- Uncertainties: None.
- Cross-reference status: References gen-statem, callback-mode, state-callback, transition-actions.
