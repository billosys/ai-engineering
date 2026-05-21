---
# === CORE IDENTIFICATION ===
concept: Complex State
slug: complex-state

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
section: "Complex State"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "non-atom state"
  - "compound state"
  - "hierarchical state"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - handle-event-function-mode
  - postponing-events
extends:
  - handle-event-function-mode
related:
  - state-timeout
  - state-enter-calls
contrasts_with:
  - state-functions-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a gen_statem state machine?"
  - "How does gen_statem's state_functions mode differ from handle_event_function?"
---

# Quick Definition

Complex state in `gen_statem` refers to using non-atom state values (such as tuples) enabled by the `handle_event_function` callback mode, allowing state data that affects event handling or postponed event retry to be encoded directly in the state term.

# Core Definition

As described in the OTP Design Principles: "The callback mode handle_event_function enables using a non-atom state as described in section Callback Modes, for example, a complex state term like a tuple." The source identifies two key reasons for complex states: "One reason to use this is when you have a state item that when changed should cancel the state time-out, or one that affects the event handling in combination with postponing events."

# Prerequisites

- **gen_statem** -- The behaviour that supports complex states.
- **Handle event function mode** -- Required for non-atom states.
- **Postponing events** -- Understanding why state data placement matters for postponed event retry.

# Key Properties

1. Requires `handle_event_function` callback mode (state_functions restricts to atom states).
2. State can be any Erlang term: tuples, records, maps, etc.
3. Changing any part of a complex state constitutes a "state change" for gen_statem, triggering retry of postponed events and cancellation of state timeouts.
4. Enables encoding state data that affects event handling directly in the state term.
5. Enables hierarchical states like `{StateName, SubState}`.
6. Pattern matching on complex states in handle_event/4 clauses provides structured dispatch.

# Construction / Recognition

## To Construct/Create:
1. Use `handle_event_function` callback mode.
2. Define state as a tuple or other compound term, e.g., `{StateName, LockButton}`.
3. Use pattern matching in `handle_event/4` clauses to dispatch on parts of the state.
4. Return `{next_state, {NewStateName, Item}, Data}` for state transitions.

## To Identify/Recognize:
1. `callback_mode/0` returns `handle_event_function` (or list containing it).
2. States are tuples, records, or other non-atom terms.
3. Pattern matching in `handle_event/4` destructures the state.

# Context & Application

Complex states solve the design problem of where to keep data that affects which events are handled. The source explains with a concrete scenario: if the lock button configuration is kept in server Data rather than State, changing it would not trigger retry of postponed events. By making the state `{StateName, LockButton}`, changing the lock button becomes a state change, causing postponed events to be retried with the new configuration.

# Examples

**Example 1** (statem.md, "Complex State"): Defining state as `{StateName, LockButton}`:

```erlang
init({Code, LockButton}) ->
    process_flag(trap_exit, true),
    Data = #{code => Code, length => length(Code), buttons => []},
    {ok, {locked, LockButton}, Data}.

callback_mode() ->
    [handle_event_function, state_enter].
```

**Example 2** (statem.md, "Complex State"): Handling events with pattern matching on complex state:

```erlang
handle_event(enter, _OldState, {locked,_}, Data) ->
    do_lock(),
    {keep_state, Data#{buttons := []}};
...
handle_event(cast, {button,LockButton}, {open,LockButton}, Data) ->
    {next_state, {locked,LockButton}, Data};
```

**Example 3** (statem.md, "Complex State"): Changing the lock button triggers a state change with postponed event retry:

```erlang
handle_event(
  {call,From}, {set_lock_button,NewLockButton},
  {StateName,OldLockButton}, Data) ->
    {next_state, {StateName,NewLockButton}, Data,
     [{reply,From,OldLockButton}]}.
```

The source describes the scenario: "we can make the lock button part of the state so when we then change the lock button in the locked state, the change becomes a state change and all postponed events are retried, therefore the lock is immediately locked!"

# Relationships

## Builds Upon
- **Handle event function mode** -- Required for non-atom states.
- **Postponing events** -- Complex states are often motivated by the need for postponed events to be retried when a state data item changes.
- **gen_statem** -- The engine that detects state changes for complex state terms.

## Enables
- Hierarchical state machines within a single gen_statem process.
- Protocol implementations with `{StateName, server}` / `{StateName, client}` patterns.
- Encoding configuration that affects event handling directly in the state.

## Related
- **State timeout** -- Changing any part of a complex state cancels the state timeout (since it is a state change).
- **State enter calls** -- State enter calls are triggered when any part of the complex state changes.

## Contrasts With
- **State functions mode** -- state_functions requires atom-only states and cannot use complex states.

# Common Errors

- **Error**: Using complex states with `state_functions` callback mode.
  **Correction**: "With state_functions, you are restricted to use atom-only states." Switch to `handle_event_function` for complex states.

- **Error**: Not realizing that changing any part of a complex state is a state change.
  **Correction**: If the state is `{locked, x}` and transitions to `{locked, y}`, gen_statem treats this as a state change (since `{locked, x} =/= {locked, y}`). This cancels state timeouts and retries postponed events.

# Common Confusions

- **Confusion**: Complex state and server Data serve the same purpose.
  **Clarification**: Data that affects which events are handled (especially with postponed events) should be in the State so changes trigger state changes. Data that does not affect event handling should be in server Data. The source warns: "an incorrect design decision of what belongs in the state, may become a hard to find bug some time later, when event postponing is introduced."

# Source Reference

Described in the "Complex State" section of the gen_statem Behaviour chapter, with the configurable lock button example.

# Verification Notes

- Definition source: Directly from the "Complex State" section of statem.md.
- Confidence rationale: High -- explicitly defined with a detailed motivating example and complete code.
- Uncertainties: None.
- Cross-reference status: References gen-statem, handle-event-function-mode, postponing-events, state-timeout, state-enter-calls; contrasts with state-functions-mode.
