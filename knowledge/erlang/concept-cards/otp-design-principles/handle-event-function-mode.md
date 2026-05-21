---
# === CORE IDENTIFICATION ===
concept: Handle Event Function Mode
slug: handle-event-function-mode

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
section: "Callback Modes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "handle_event_function"
  - "handle_event_function callback mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - callback-mode
extends:
  - callback-mode
related:
  - state-callback
  - complex-state
contrasts_with:
  - state-functions-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_statem's state_functions mode differ from handle_event_function?"
  - "How do I implement a gen_statem state machine?"
---

# Quick Definition

`handle_event_function` is a `gen_statem` callback mode where all events in all states are handled by a single `Module:handle_event/4` function, enabling the use of non-atom states and flexible branching strategies.

# Core Definition

As described in the OTP Design Principles: "handle_event_function -- Events are handled by one single callback function." In this mode, "The event is handled by: `Module:handle_event(EventType, EventContent, State, Data)`." The source explains: "With handle_event_function, you are free to mix strategies, as all events and states are handled in the same callback function." This mode "enables the use of non-atom states, for example, complex states, or even hierarchical states."

# Prerequisites

- **gen_statem** -- The behaviour that provides the callback mode mechanism.
- **Callback mode** -- Understanding of how callback modes determine event dispatch.

# Key Properties

1. A single `handle_event/4` function handles all events in all states.
2. States can be any Erlang term, not just atoms (enables complex states).
3. Allows both event-centric and state-centric branching strategies.
4. The `State` argument is passed explicitly to `handle_event/4`.
5. Enables hierarchical states such as `{StateName, server}` or `{StateName, client}`.
6. Function can grow large and typically requires branching to helper functions.

# Construction / Recognition

## To Construct/Create:
1. Set `callback_mode/0` to return `handle_event_function` (or `[handle_event_function, state_enter]`).
2. Export and implement `handle_event/4`.
3. Branch on `State` and/or `EventType` within the function body.
4. States can be atoms, tuples, or any Erlang term.

## To Identify/Recognize:
1. `callback_mode/0` returns `handle_event_function`.
2. Module exports `handle_event/4`.
3. State values may be non-atom terms (tuples, records, etc.).

# Context & Application

This mode "works equally well when you want to focus on one event at the time or on one state at the time, but function `Module:handle_event/4` quickly grows too large to handle without branching to helper functions." It is the required mode for non-atom states. The source gives the example of protocol implementations where state might be `{StateName, server}` or `{StateName, client}` to differentiate client-side and server-side handling.

# Examples

**Example 1** (statem.md, "One State Callback"): The code_lock example reimplemented with handle_event_function, branching on event first:

```erlang
callback_mode() ->
    handle_event_function.

handle_event(cast, {button,Button}, State, #{code := Code} = Data) ->
    case State of
        locked ->
            %% handle button in locked state
            ...;
        open ->
            keep_state_and_data
    end;
handle_event(state_timeout, lock, open, Data) ->
    do_lock(),
    {next_state, locked, Data}.
```

**Example 2** (statem.md, "Callback Mode: handle_event_function"): With state enter calls, branching on state first:

```erlang
callback_mode() ->
    [handle_event_function, state_enter].

handle_event(enter, _OldState, locked, Data) ->
    do_lock(),
    {keep_state, Data#{buttons := []}};
handle_event(enter, _OldState, open, _Data) ->
    do_unlock(),
    {keep_state_and_data,
     [{state_timeout,10_000,lock}]}.
```

# Relationships

## Builds Upon
- **Callback mode** -- handle_event_function is one of the two available callback modes.
- **gen_statem** -- The behaviour providing handle_event_function dispatch.

## Enables
- **Complex state** -- Non-atom states are only possible with handle_event_function mode.
- **State callback** -- The handle_event/4 function is the state callback for all states.

## Related
- **State callback** -- The handle_event/4 function signature and return values.

## Contrasts With
- **State functions mode** -- state_functions uses one function per state (atoms only) vs. one function for all states and any state type.

# Common Errors

- **Error**: Letting `handle_event/4` grow too large without helper functions.
  **Correction**: The source warns that `handle_event/4` "quickly grows too large to handle without branching to helper functions." Factor out state-specific or event-specific logic into separate helper functions.

# Common Confusions

- **Confusion**: handle_event_function means you must branch on events first.
  **Clarification**: You can branch on state first, event first, or use a mixed strategy. The source shows both approaches in different examples. With state enter calls, branching on state first often works better.

# Source Reference

Described in the "Callback Modes" section, "Choosing the Callback Mode" subsection, and the "One State Callback" section where code_lock is reimplemented using handle_event_function.

# Verification Notes

- Definition source: Directly from the "Callback Modes" and "One State Callback" sections of statem.md.
- Confidence rationale: High -- explicitly defined and demonstrated with complete code examples.
- Uncertainties: None.
- Cross-reference status: References gen-statem, callback-mode; contrasts with state-functions-mode; related to complex-state.
