---
# === CORE IDENTIFICATION ===
concept: gen_statem Behaviour
slug: gen-statem

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: state-machine
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_statem Behaviour"
chapter_number: null
pdf_page: null
section: "gen_statem Behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_statem"
  - "generic state machine"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - callback-module
extends:
  - behaviour
related:
  - event-driven-state-machine
  - callback-mode
  - supervision-tree
contrasts_with:
  - gen-server
  - gen-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_statem?"
  - "What distinguishes gen_server from gen_statem?"
  - "What must I know before using gen_statem?"
  - "How do I implement a gen_statem state machine?"
---

# Quick Definition

`gen_statem` is an OTP behaviour module for implementing event-driven state machines, providing built-in support for state-specific event handling, event postponing, inserted events, state enter calls, and multiple timeout types.

# Core Definition

As described in the OTP Design Principles documentation, `gen_statem` is a behaviour that implements an event-driven state machine following the model `State(S) x Event(E) -> Actions(A), State(S')`. The behaviour engine "holds the state machine state, server data, timer references, a queue of postponed messages, and other metadata. It receives all process messages, handles the system messages, and calls the callback module with state machine specific events." Similar to most `gen_` behaviours, `gen_statem` keeps a server `Data` item besides the state, and "since there is no restriction on the number of states...or on the number of distinct input events, a state machine implemented with this behaviour is Turing complete."

# Prerequisites

- **Behaviour** -- Understanding of OTP behaviours and the callback module pattern.
- **Callback module** -- How callback modules provide the implementation for behaviour engines.

# Key Properties

1. Implements an event-driven Mealy machine model where output actions depend on current state and input event.
2. Supports two callback modes: `state_functions` and `handle_event_function`.
3. Maintains both a state and a separate server `Data` term (a map or any Erlang term).
4. Provides three timeout types: state timeout, event timeout, and generic (named) timeouts.
5. Supports postponing events to be retried after a state change.
6. Supports inserted events (next_event action) including the `internal` event type.
7. Supports optional state enter calls on state changes.
8. Distinguishes "state change" (`S' =/= S`) from "state transition" (any event handling).
9. Can be started as part of a supervision tree using `start_link` or standalone using `start`.

# Construction / Recognition

## To Construct/Create:
1. Create a callback module with `-behaviour(gen_statem).`
2. Export and implement `init/1` to return `{ok, InitialState, Data}`.
3. Export and implement `callback_mode/0` to return the chosen callback mode.
4. Implement state callback functions for each state (in `state_functions` mode) or a single `handle_event/4` function (in `handle_event_function` mode).
5. Optionally implement `terminate/3` for cleanup.
6. Start the server with `gen_statem:start_link/3,4` (supervised) or `gen_statem:start/3,4` (standalone).

## To Identify/Recognize:
1. Module contains `-behaviour(gen_statem).` declaration.
2. Exports `callback_mode/0` returning `state_functions` or `handle_event_function`.
3. State callback functions take `(EventType, EventContent, Data)` or `handle_event/4` takes `(EventType, EventContent, State, Data)`.
4. Returns tuples like `{next_state, NextState, NewData}` or `{keep_state, NewData}`.

# Context & Application

You should consider using `gen_statem` over `gen_server` when your process logic is naturally described as a state machine and you need features such as co-located callback code per state, event postponing, inserted events, state enter calls, or the built-in timeout types. For simple state machines not needing these features, `gen_server` is suitable -- the call overhead difference is small (approximately 2 vs 3.3 microseconds roundtrip).

# Examples

**Example 1** (statem.md, "Example"): The code_lock example implements a door with a code lock as a `gen_statem`. The door starts in the `locked` state. Button presses are collected and compared to the code. On a correct code, the door transitions to `open` with a 10-second state timeout before relocking:

```erlang
-module(code_lock).
-behaviour(gen_statem).

init(Code) ->
    do_lock(),
    Data = #{code => Code, length => length(Code), buttons => []},
    {ok, locked, Data}.

callback_mode() ->
    state_functions.
```

**Example 2** (statem.md, "Starting gen_statem"): Starting the state machine within a supervision tree:

```erlang
start_link(Code) ->
    gen_statem:start_link({local,?NAME}, ?MODULE, Code, []).
```

# Relationships

## Builds Upon
- **Behaviour** -- gen_statem is an OTP behaviour, following the callback module pattern.
- **Callback module** -- The callback module provides state-specific event handling logic.

## Enables
- **Callback mode** -- The choice of how events are dispatched to callback functions.
- **Transition actions** -- Actions returned from callbacks that the engine executes.
- **State enter calls** -- Optional automatic callbacks on state change.
- **Postponing events** -- Deferring events to be retried after a state change.

## Related
- **Supervision tree** -- gen_statem processes are typically started as part of a supervision tree.
- **Event-driven state machine** -- The theoretical model that gen_statem implements.

## Contrasts With
- **gen_server** -- gen_server is simpler but lacks state-specific dispatch, postponing, inserted events, and state enter calls.
- **gen_event** -- gen_event manages event handlers, not state machine transitions.

# Common Errors

- **Error**: Using `gen_statem` when `gen_server` would suffice, adding unnecessary complexity.
  **Correction**: Only use `gen_statem` when you need its key features (state-specific dispatch, postponing, enter calls, timeouts). For simple request-response servers, `gen_server` is more appropriate.

- **Error**: Confusing "state change" with "state transition."
  **Correction**: A state transition is any event handling. A state change is a state transition where `S' =/= S`. State changes trigger special behavior: postponed events are retried, state timeouts are canceled, and state enter calls are invoked.

# Common Confusions

- **Confusion**: gen_statem replaces gen_fsm.
  **Clarification**: `gen_statem` is the successor to `gen_fsm` (which is deprecated). It provides a superset of `gen_fsm` functionality with a cleaner and more powerful API.

- **Confusion**: The state must be an atom.
  **Clarification**: In `state_functions` mode, the state must be an atom. In `handle_event_function` mode, the state can be any Erlang term, enabling complex states like tuples.

# Source Reference

The gen_statem behaviour is documented across the entire "gen_statem Behaviour" chapter of the OTP Design Principles guide. The introductory sections cover the event-driven model, when to use gen_statem, and the callback module structure.

# Verification Notes

- Definition source: Directly from the "gen_statem Behaviour" chapter opening, "Event-Driven State Machines" section, and "When to use gen_statem" section.
- Confidence rationale: High -- the behaviour is explicitly and thoroughly defined throughout the source with detailed examples.
- Uncertainties: None.
- Cross-reference status: References behaviour, callback-module, gen-server, gen-event, supervision-tree from other sources.
