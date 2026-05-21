---
# === CORE IDENTIFICATION ===
concept: State Functions Mode
slug: state-functions-mode

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
  - "state_functions"
  - "state_functions callback mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - callback-mode
extends:
  - callback-mode
related:
  - state-callback
contrasts_with:
  - handle-event-function-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_statem's state_functions mode differ from handle_event_function?"
  - "How do I implement a gen_statem state machine?"
---

# Quick Definition

`state_functions` is a `gen_statem` callback mode where each state is handled by a separate callback function named after the state, taking `(EventType, EventContent, Data)` as arguments.

# Core Definition

As described in the OTP Design Principles: "state_functions -- Events are handled by one callback function per state." In this mode, "The event is handled by: `Module:StateName(EventType, EventContent, Data)`." The source explains that "With state_functions, you are restricted to use atom-only states, and the gen_statem engine branches depending on state name for you. This encourages the callback module to co-locate the implementation of all event actions particular to one state in the same place in the code, hence to focus on one state at the time."

# Prerequisites

- **gen_statem** -- The behaviour that provides the callback mode mechanism.
- **Callback mode** -- Understanding of how callback modes determine event dispatch.

# Key Properties

1. Each state is implemented as a separate exported function named after the state atom.
2. States are restricted to atoms (the function name is the state name).
3. The gen_statem engine automatically branches to the correct function based on the current state.
4. Encourages state-centric code organization where all event handling for a state is co-located.
5. Most similar to the deprecated `gen_fsm` behaviour.
6. The recommended default choice according to the documentation.

# Construction / Recognition

## To Construct/Create:
1. Set `callback_mode/0` to return `state_functions` (or `[state_functions, state_enter]`).
2. Export a function for each state: `locked/3`, `open/3`, etc.
3. Each function has the signature `StateName(EventType, EventContent, Data)`.
4. Return `{next_state, NextState, NewData}` or similar return values.

## To Identify/Recognize:
1. `callback_mode/0` returns `state_functions`.
2. Multiple exported functions with arity 3 whose names correspond to state atoms.
3. State names appear as function names in the module's export list.

# Context & Application

This mode "fits well when you have a regular state diagram...which describes all events and actions belonging to a state visually around that state, and each state has its unique name." It is recommended as the default choice: "choose state_functions -- it is the one most like gen_fsm."

# Examples

**Example 1** (statem.md, "Example"): The code_lock example with two state functions:

```erlang
callback_mode() ->
    state_functions.

locked(cast, {button,Button}, #{code := Code} = Data) ->
    %% handle button press in locked state
    ...

open(state_timeout, lock, Data) ->
    do_lock(),
    {next_state, locked, Data};
open(cast, {button,_}, Data) ->
    {next_state, open, Data}.
```

**Example 2** (statem.md, "All State Events"): Handling common events across states using a helper function:

```erlang
locked(EventType, EventContent, Data) ->
    handle_common(EventType, EventContent, Data).

open(EventType, EventContent, Data) ->
    handle_common(EventType, EventContent, Data).
```

# Relationships

## Builds Upon
- **Callback mode** -- state_functions is one of the two available callback modes.
- **gen_statem** -- The behaviour that provides the state_functions dispatch.

## Enables
- **State callback** -- Each state function is a state callback.

## Related
- **State callback** -- The function signature and return values for state functions.

## Contrasts With
- **Handle event function mode** -- The alternative callback mode using a single `handle_event/4` function for all states, allowing non-atom states.

# Common Errors

- **Error**: Using a non-atom value as a state in state_functions mode.
  **Correction**: State_functions requires atom states because the state name is used as the callback function name. Use `handle_event_function` mode for non-atom states.

- **Error**: Forgetting to export state functions.
  **Correction**: Each state function must be exported (e.g., `-export([locked/3, open/3]).`).

# Common Confusions

- **Confusion**: All events for a state must be handled in the state function only.
  **Clarification**: Common events can be delegated to a shared helper function from within each state function (as shown in the "All State Events" section with `handle_common/3`).

# Source Reference

Described in the "Callback Modes" section, "Choosing the Callback Mode" subsection, and the primary "Example" section where code_lock is implemented using state_functions mode.

# Verification Notes

- Definition source: Directly from the "Callback Modes" section of statem.md.
- Confidence rationale: High -- explicitly defined and demonstrated throughout the primary code_lock example.
- Uncertainties: None.
- Cross-reference status: References gen-statem, callback-mode; contrasts with handle-event-function-mode.
