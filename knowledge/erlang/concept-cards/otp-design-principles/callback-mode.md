---
# === CORE IDENTIFICATION ===
concept: Callback Mode
slug: callback-mode

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
  - "callback mode"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - callback-module
extends: []
related:
  - state-functions-mode
  - handle-event-function-mode
  - state-enter-calls
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_statem's state_functions mode differ from handle_event_function?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

The callback mode is a property of a `gen_statem` callback module that determines how events are dispatched to callback functions, choosing between one function per state (`state_functions`) or a single function for all states (`handle_event_function`).

# Core Definition

As stated in the OTP Design Principles: "The gen_statem behaviour supports two callback modes: state_functions -- Events are handled by one callback function per state. handle_event_function -- Events are handled by one single callback function." The callback mode "is a property of the callback module and is set at server start. It may be changed due to a code upgrade/downgrade, or when changing the callback module." It is "selected by implementing a mandatory callback function `Module:callback_mode()` that returns one of the callback modes."

# Prerequisites

- **gen_statem** -- The behaviour that uses callback modes to dispatch events.
- **Callback module** -- The module that implements the callback mode function.

# Key Properties

1. Two modes available: `state_functions` and `handle_event_function`.
2. Set by implementing the mandatory `callback_mode/0` function.
3. Can return a single atom or a list containing the mode and `state_enter` to enable state enter calls.
4. `state_functions` restricts states to atoms; `handle_event_function` allows any Erlang term as state.
5. The callback mode may be changed during code upgrade/downgrade or when changing the callback module.

# Construction / Recognition

## To Construct/Create:
1. Implement the mandatory `callback_mode/0` function in the callback module.
2. Return `state_functions` for per-state callback functions, or `handle_event_function` for a single handler.
3. Optionally return a list like `[state_functions, state_enter]` to also enable state enter calls.

## To Identify/Recognize:
1. Look for the `callback_mode/0` export and its return value.
2. If it returns `state_functions`, each state is a separate exported function.
3. If it returns `handle_event_function`, a single `handle_event/4` function handles all events.

# Context & Application

The choice of callback mode shapes the overall structure of the callback module. The source recommends: "choose state_functions -- it is the one most like gen_fsm." Use `handle_event_function` when you need non-atom states, or when you prefer to branch on event type first rather than state, or when you want to share event handling logic across states more directly.

# Examples

**Example 1** (statem.md, "Callback Modes"): Selecting state_functions mode:

```erlang
callback_mode() ->
    state_functions.
```

**Example 2** (statem.md, "State Enter Actions"): Enabling state enter calls with state_functions:

```erlang
callback_mode() ->
    [state_functions, state_enter].
```

**Example 3** (statem.md, "Callback Mode: handle_event_function"): Enabling handle_event_function with state enter:

```erlang
callback_mode() ->
    [handle_event_function, state_enter].
```

# Relationships

## Builds Upon
- **gen_statem** -- Callback mode is a core configuration property of the gen_statem behaviour.
- **Callback module** -- The callback mode is set by a function in the callback module.

## Enables
- **State functions mode** -- One of the two callback modes.
- **Handle event function mode** -- The other callback mode.
- **State enter calls** -- Enabled by including `state_enter` in the callback_mode return list.

## Related
- **State callback** -- The actual function(s) that handle events, determined by callback mode.

## Contrasts With
- None directly -- the two modes are the contrasting options within this concept.

# Common Errors

- **Error**: Forgetting to export `callback_mode/0`.
  **Correction**: `callback_mode/0` is a mandatory callback that must be exported. Without it, the gen_statem will fail to start.

- **Error**: Using non-atom states in `state_functions` mode.
  **Correction**: "With state_functions, you are restricted to use atom-only states." Use `handle_event_function` for non-atom states.

# Common Confusions

- **Confusion**: The callback mode cannot be changed at runtime.
  **Clarification**: The callback mode "may be changed due to a code upgrade/downgrade, or when changing the callback module" using `change_callback_module`, `push_callback_module`, or `pop_callback_module` transition actions.

# Source Reference

Described in the "Callback Modes" section and "Choosing the Callback Mode" subsection of the gen_statem Behaviour chapter.

# Verification Notes

- Definition source: Directly from the "Callback Modes" section of statem.md.
- Confidence rationale: High -- explicitly defined with clear descriptions of both modes and their differences.
- Uncertainties: None.
- Cross-reference status: References gen-statem, callback-module; related to state-functions-mode and handle-event-function-mode.
