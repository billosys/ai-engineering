---
# === CORE IDENTIFICATION ===
concept: Transition Actions
slug: transition-actions

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
section: "Transition Actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "transition action"
  - "actions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - state-callback
extends: []
related:
  - postponing-events
  - inserted-events
  - state-timeout
  - event-timeout
  - generic-timeout
  - hibernation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a gen_statem state machine?"
  - "What must I know before using gen_statem?"
---

# Quick Definition

Transition actions are commands returned in a list from a `gen_statem` state callback that instruct the behaviour engine to perform specific operations after the callback returns, such as replying to callers, setting timeouts, postponing events, or inserting new events.

# Core Definition

As described in the OTP Design Principles: "There are more specific transition actions that a callback function can command the gen_statem engine to do after the callback function return. These are commanded by returning a list of actions in the return value from the callback function." The documentation distinguishes between general actions (code executed within the callback before returning) and transition actions (commands for the engine). "Out of these transition actions, the only immediate action is reply for replying to a caller. The other actions are collected and handled later during the state transition."

# Prerequisites

- **gen_statem** -- The behaviour engine that executes transition actions.
- **State callback** -- The function that returns transition actions in its return value.

# Key Properties

1. Returned as a list in the state callback return tuple (e.g., `{next_state, S, D, Actions}`).
2. Only `reply` is executed immediately; all others are collected and handled during the state transition.
3. For non-reply, non-next_event actions, the last of a specific type overrides previous ones.
4. Inserted events (`next_event`) are stored and inserted all together.
5. An empty actions list is equivalent to not returning the actions field.

# Available Transition Actions

1. `{postpone, Boolean}` -- Postpone the current event.
2. `{hibernate, Boolean}` -- Hibernate the gen_statem after the transition.
3. `{state_timeout, Time, EventContent [, Opts]}` -- Start/update/cancel a state timeout.
4. `{{timeout, Name}, Time, EventContent [, Opts]}` -- Start/update/cancel a generic (named) timeout.
5. `{timeout, Time, EventContent [, Opts]}` -- Start an event timeout.
6. `{reply, From, Reply}` -- Reply to a caller.
7. `{next_event, EventType, EventContent}` -- Insert an event to be processed next.
8. `{change_callback_module, NewModule}` -- Change the callback module.
9. `{push_callback_module, NewModule}` -- Push current module and set a new one.
10. `pop_callback_module` -- Pop and restore the previous callback module.

# Construction / Recognition

## To Construct/Create:
1. Include an actions list as the last element of the return tuple from a state callback.
2. Compose the list with one or more action tuples.
3. Multiple actions of the same type: the last one wins (except for `reply` and `next_event` which can appear multiple times).

## To Identify/Recognize:
1. A list in the fourth element of `{next_state, State, Data, Actions}` or similar return tuples.
2. Contains tuples like `{reply, From, Reply}`, `{state_timeout, Time, Content}`, `postpone`, etc.

# Context & Application

Transition actions are the mechanism by which state callbacks communicate side effects to the gen_statem engine. They enable the full range of gen_statem features including timeouts, event postponing, event insertion, replying to callers, and hibernation. "You can, for example, reply to many callers, generate multiple next events, and set a time-out to use absolute instead of relative time (using the Opts field)."

# Examples

**Example 1** (statem.md, "Example"): Starting a state timeout when transitioning to the open state:

```erlang
{next_state, open, Data#{buttons := []},
 [{state_timeout,10_000,lock}]}
```

**Example 2** (statem.md, "All State Events"): Replying to a caller:

```erlang
handle_common({call,From}, code_length, #{code := Code} = Data) ->
    {keep_state, Data,
     [{reply,From,length(Code)}]}.
```

**Example 3** (statem.md, "Inserted Events"): Inserting an internal event:

```erlang
{keep_state, maps:remove(button, Data),
 [{next_event,internal,{button,Button}}]}
```

# Relationships

## Builds Upon
- **State callback** -- Transition actions are returned from state callbacks.
- **gen_statem** -- The engine that processes transition actions.

## Enables
- **Postponing events** -- Via the `{postpone, true}` or `postpone` action.
- **Inserted events** -- Via the `{next_event, EventType, EventContent}` action.
- **State timeout** -- Via the `{state_timeout, Time, EventContent}` action.
- **Event timeout** -- Via the `{timeout, Time, EventContent}` action.
- **Generic timeout** -- Via the `{{timeout, Name}, Time, EventContent}` action.
- **Hibernation** -- Via the `{hibernate, true}` or `hibernate` action.

## Related
- **Event types** -- Timeout and next_event actions generate new events with corresponding event types.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting multiple timeout actions of the same type to all take effect.
  **Correction**: "The rest set transition options where the last of a specific type override the previous." Only the last state_timeout (for example) in the actions list takes effect.

- **Error**: Changing the callback module from a state enter call.
  **Correction**: `change_callback_module`, `push_callback_module`, and `pop_callback_module` "cannot be done from a state enter call."

# Common Confusions

- **Confusion**: All transition actions are executed immediately.
  **Clarification**: "The only immediate action is reply for replying to a caller. The other actions are collected and handled later during the state transition."

# Source Reference

Described in the "Transition Actions" section of the gen_statem Behaviour chapter, with a complete enumeration of all available actions and their semantics.

# Verification Notes

- Definition source: Directly from the "Transition Actions" section of statem.md.
- Confidence rationale: High -- explicitly defined with a complete list of all action types.
- Uncertainties: None.
- Cross-reference status: References gen-statem, state-callback; related to all timeout types, postponing-events, inserted-events, hibernation.
