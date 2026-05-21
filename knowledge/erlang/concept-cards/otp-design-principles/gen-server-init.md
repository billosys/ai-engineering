---
# === CORE IDENTIFICATION ===
concept: "gen_server init/1 Callback"
slug: gen-server-init

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: "Starting a Gen_Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "init callback"
  - "gen_server init"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - gen-server-call
  - gen-server-cast
  - gen-server-terminate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a gen_server initialized?"
  - "What does init/1 return?"
  - "How do I implement a gen_server callback module?"
---

# Quick Definition

`init/1` is the gen_server callback function that initializes the server's internal state when the gen_server process is started.

# Core Definition

According to the gen_server Behaviour chapter: "If name registration succeeds, the new gen_server process calls the callback function ch3:init([]). init is expected to return {ok, State}, where State is the internal state of the gen_server." The `init/1` callback receives the third argument passed to `gen_server:start_link/4` and must return the initial state that will be threaded through all subsequent callback invocations.

# Prerequisites

- **gen_server** — init/1 is a callback of the gen_server behaviour.

# Key Properties

1. Called automatically when the gen_server process starts (via `gen_server:start_link/4` or `gen_server:start/4`).
2. Receives the third argument of `start_link/4` as its parameter.
3. Must return `{ok, State}` where `State` is the initial internal state.
4. `gen_server:start_link/4` is synchronous — it does not return until `init/1` completes.
5. Can set process flags (e.g., `process_flag(trap_exit, true)`) for cleanup on termination.

# Construction / Recognition

## To Construct/Create:
1. Define `init/1` in the callback module, accepting one argument.
2. Perform any necessary initialization (creating data structures, opening resources).
3. Return `{ok, InitialState}`.
4. If trapping exits is needed for cleanup, call `process_flag(trap_exit, true)` inside `init/1`.

## To Identify/Recognize:
1. A function named `init/1` in a gen_server callback module.
2. Returns `{ok, State}`.
3. Called once at server startup, before any requests are processed.

# Context & Application

`init/1` establishes the initial state for the gen_server. All subsequent callbacks (`handle_call/3`, `handle_cast/2`, `handle_info/2`) receive and transform this state. The synchronous nature of `start_link` means the supervisor (or caller) waits until `init/1` completes, ensuring the gen_server is fully ready before any requests arrive.

# Examples

**Example 1** (gen_server_concepts.md, "Starting a Gen_Server"): Simple initialization for the channel server:
```erlang
init(_Args) ->
    {ok, channels()}.
```
The state is initialized to the set of available channels.

**Example 2** (gen_server_concepts.md, "Stopping"): Initialization with exit trapping for cleanup:
```erlang
init(Args) ->
    ...,
    process_flag(trap_exit, true),
    ...,
    {ok, State}.
```

# Relationships

## Builds Upon
- **gen_server** — init/1 is one of the required gen_server callbacks.

## Enables
- **gen_server:call** — handle_call/3 operates on the state established by init/1
- **gen_server:cast** — handle_cast/2 operates on the state established by init/1
- **gen_server:terminate** — terminate/2 can clean up resources acquired in init/1

## Related
- **handle_info** — also operates on the state established by init/1

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Performing long-running work in `init/1`, blocking the supervisor.
  **Correction**: Since `gen_server:start_link/4` is synchronous and doesn't return until init completes, keep init fast. Defer slow work to a self-sent message handled by `handle_info/2` or `handle_continue/2`.

# Common Confusions

- **Confusion**: Thinking the argument to `init/1` is always `[]`.
  **Clarification**: The argument to `init/1` is whatever was passed as the third argument to `gen_server:start_link/4`. In the example it is `[]`, but it can be any term.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Starting a Gen_Server" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Starting a Gen_Server" section.
- Confidence rationale: High — explicitly described with code examples in the source.
- Uncertainties: None.
- Cross-reference status: References gen-server, gen-server-call, gen-server-cast, gen-server-terminate, handle-info (planned cards).
