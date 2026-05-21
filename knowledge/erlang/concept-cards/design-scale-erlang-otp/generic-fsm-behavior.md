---
# === CORE IDENTIFICATION ===
concept: Generic FSM Behavior
slug: generic-fsm-behavior

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: fsm
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Finite State Machines"
chapter_number: 5
pdf_page: 144
section: "Generic FSMs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_fsm"
  - generic FSM
  - FSM behavior
  - "gen_statem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fsm-the-erlang-way
  - gen-server
extends:
  - gen-server
related:
  - fsm-states-and-state-functions
  - fsm-events
  - fsm-loop-data
  - fsm-termination
contrasts_with:
  - gen-server
  - fsm-the-erlang-way

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a finite state machine behavior (gen_statem)?"
  - "How do I implement a finite state machine with gen_statem?"
  - "What distinguishes a gen_server from a gen_statem?"
---

# Quick Definition

The generic FSM behavior (`gen_fsm`) is the OTP library module that holds all the generic FSM machinery — spawning, message handling, timeouts, stopping — while the application-specific states and actions go in a callback module.

# Core Definition

The generic FSM behavior separates generic FSM functionality from specific functionality, "the same course we took with generic servers" (Cesarini & Vinoski, p. 144). "We can view the FSM as an extension of the generic server, with state handling added on top. Messages become events and callback functions that receive the messages become states. All of the generic code is placed in a library module called `gen_fsm`, while all of the specifics are placed in a callback module" (p. 145). The generic side handles spawning the FSM, storing the loop data and current state, sending synchronous and asynchronous events, receiving replies, timeouts, and stopping the FSM. The specific side — in the callback module — handles initializing the state, the loop data itself, the events and how they are handled per state, the FSM states, state transitions, and cleanup (Table 6-1, p. 145).

> **OTP-27+ note:** `gen_fsm` has been deprecated and superseded by `gen_statem`. The book (targeting an earlier OTP release) teaches `gen_fsm`; the concepts — states as callbacks, events, state data — carry over to `gen_statem`.

# Prerequisites

- **Finite state machines the Erlang way** — The behavior is motivated by splitting a pure-Erlang FSM into generic and specific parts.
- **Generic server** — `gen_fsm` is presented as an extension of `gen_server`; its start/stop/error semantics are nearly identical.

# Key Properties

1. Generic code lives in the `gen_fsm` library module; specifics live in a callback module.
2. The callback module carries `-behavior(gen_fsm)`, used for compile-time warnings on missing callbacks.
3. Started with `gen_fsm:start_link/3,4` or `gen_fsm:start/3,4`; the start call invokes `Mod:init/1`.
4. `Mod:init/1` returns `{ok, StartState, LoopData}`, `{stop, Reason}`, or `ignore`.
5. Generic responsibilities: spawning, storing state and loop data, sending events, receiving replies, timeouts, stopping.
6. Specific responsibilities: initializing state, the loop data, the events, handling per state, the states, transitions, cleanup.
7. Returning a control tuple that violates the protocol terminates the behavior with `bad_return_value`.

# Construction / Recognition

## To Implement a gen_fsm Callback Module:
1. Declare `-module`, `-behavior(gen_fsm)`, and `-export` the start/stop functions, callbacks, state functions, and client functions.
2. Write a `start_link/0` client function wrapping `gen_fsm:start_link/4`.
3. Implement `init/1` returning `{ok, StartState, LoopData}`.
4. Implement one state callback function per state.
5. Implement `handle_event/3`, `handle_sync_event/4`, `handle_info/3`, and `terminate/3` as needed.

# Context & Application

- **Typical contexts**: Any system whose behavior is naturally modeled as states and events — protocol handlers, device controllers, the phone controller exercise.
- **Common applications**: The `coffee_fsm` module migrating the pure-Erlang coffee machine to the behavior.
- **Historical/stylistic notes**: The book notes `gen_fsm` "might not be the most commonly used behavior, [but] when it fits your application it will greatly simplify your task" (p. 160).

# Examples

**Example 1** (p. 146): The `coffee_fsm` callback module header:

```erlang
-module(coffee_fsm).
-behavior(gen_fsm).
-export([start_link/0, stop/0]).
-export([init/1, terminate/3, handle_event/3]). % Callback functions
-export([selection/2, payment/2, remove/2]).    % States
```

**Example 2** (p. 147): Starting and initializing:

```erlang
start_link() ->
    gen_fsm:start_link({local, ?MODULE}, ?MODULE, [], []).

init([]) ->
    hw:reboot(),
    hw:display("Make Your Selection", []),
    process_flag(trap_exit, true),
    {ok, selection, []}.
```

# Relationships

## Builds Upon
- **Generic server** — `gen_fsm` is "an extension of the generic server, with state handling added on top."
- **Finite state machines the Erlang way** — The behavior generalizes the pure-Erlang FSM idiom.

## Enables
- **fsm-states-and-state-functions** — States are defined as exported callback functions.
- **fsm-events** — Events are sent via `gen_fsm:send_event/2` and friends.
- **fsm-termination** — Stopping the FSM is handled by the behavior.

## Related
- **fsm-loop-data** — The behavior stores the loop data passed between states.

## Contrasts With
- **Generic server** — `gen_server` is a client-server behavior; `gen_fsm` adds explicit state handling. A `gen_server` callback handles `handle_call`/`handle_cast`; a `gen_fsm` callback has one function per state.
- **Finite state machines the Erlang way** — The pure-Erlang FSM intermixes generic and specific code; the behavior factors the generic code into a library.

# Common Errors

- **Error**: Returning `{next_state, ...}` from `init/1` instead of `{ok, StartState, LoopData}`.
  **Correction**: `init/1` must return `{ok, NextState, LoopData}` (or `{stop, Reason}` / `ignore`); a wrong tuple terminates the FSM with `bad_return_value`.

# Common Confusions

- **Confusion**: Thinking `gen_fsm` is unrelated to `gen_server`.
  **Clarification**: The book explicitly frames the FSM behavior as an extension of the generic server — messages become events, message-handling callbacks become states.

# Source Reference

Chapter 5: Finite State Machines, Sections "Generic FSMs" and "A Behavior Example," pages 144-148. See Table 6-1 (generic vs. specific) and Table 6-2 (gen_fsm callbacks).

# Verification Notes

- Definition source: Direct quotes from pp. 144-145.
- Confidence rationale: HIGH — the source defines the behavior, its module split, and its callback contract explicitly.
- Uncertainties: The OTP-27+ note (deprecation in favor of `gen_statem`) is added from extraction-baseline knowledge per the taxonomy's OTP-27+ guidance; the source itself predates it.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
