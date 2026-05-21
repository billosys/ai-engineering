---
# === CORE IDENTIFICATION ===
concept: gen_server Behaviour
slug: gen-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_server"
  - "generic server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - callback-module
  - client-server-model
extends:
  - behaviour
related:
  - gen-server-call
  - gen-server-cast
  - gen-server-init
  - gen-server-terminate
  - handle-info
contrasts_with:
  - gen-statem
  - gen-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_server?"
  - "How do I implement a gen_server callback module?"
  - "What must I know before implementing a gen_server?"
  - "What distinguishes gen_server from gen_statem?"
---

# Quick Definition

`gen_server` is the OTP behaviour for implementing the server side of a client-server relation, providing a standardized framework for synchronous and asynchronous request handling with managed state.

# Core Definition

The OTP Design Principles state that `gen_server` is one of the four standard Erlang/OTP behaviours, described as "for implementing the server of a client-server relation." It is the OTP formalization of the generic server pattern shown in the Overview chapter, corresponding (in greatly simplified form) to the custom `server` module example. A gen_server callback module must implement callbacks including `init/1`, `handle_call/3`, `handle_cast/2`, and optionally `handle_info/2`, `terminate/2`, and `code_change/3`.

# Prerequisites

- **Behaviour** — gen_server is an OTP behaviour.
- **Callback Module** — users implement gen_server by writing a callback module.
- **Client-Server Model** — gen_server implements the server side of this model.

# Key Properties

1. Implements the server side of a client-server relation.
2. Started with `gen_server:start_link/4` (supervised) or `gen_server:start/4` (standalone).
3. Supports synchronous requests via `gen_server:call/2` and asynchronous requests via `gen_server:cast/2`.
4. Maintains internal state passed through all callback invocations.
5. `gen_server:start_link/4` is synchronous — it does not return until the gen_server is initialized and ready.
6. Automatically terminated by its supervisor in a supervision tree.
7. Interface functions and callback functions are typically in the same module.

# Construction / Recognition

## To Construct/Create:
1. Create a module with `-behaviour(gen_server)`.
2. Implement `init/1` returning `{ok, State}` to initialize the server state.
3. Implement `handle_call/3` for synchronous requests, returning `{reply, Reply, NewState}`.
4. Implement `handle_cast/2` for asynchronous requests, returning `{noreply, NewState}`.
5. Optionally implement `handle_info/2`, `terminate/2`, and `code_change/3`.
6. Define interface functions (e.g., `start_link/0`) that call `gen_server:start_link/4`.
7. Define API functions that call `gen_server:call/2` or `gen_server:cast/2`.

## To Identify/Recognize:
1. Module contains `-behaviour(gen_server)`.
2. Exports `init/1`, `handle_call/3`, `handle_cast/2`.
3. Interface functions use `gen_server:start_link/4`, `gen_server:call/2`, `gen_server:cast/2`.

# Context & Application

`gen_server` is the most commonly used OTP behaviour. It is the standard way to implement any process that manages state and responds to requests from other processes. The source's channel allocation server example demonstrates its typical use: managing a shared resource (channels) where clients allocate and free resources via synchronous and asynchronous calls.

# Examples

**Example 1** (gen_server_concepts.md, "Example"): A complete gen_server callback module for channel allocation:
```erlang
-module(ch3).
-behaviour(gen_server).

-export([start_link/0]).
-export([alloc/0, free/1]).
-export([init/1, handle_call/3, handle_cast/2]).

start_link() ->
    gen_server:start_link({local, ch3}, ch3, [], []).

alloc() ->
    gen_server:call(ch3, alloc).

free(Ch) ->
    gen_server:cast(ch3, {free, Ch}).

init(_Args) ->
    {ok, channels()}.

handle_call(alloc, _From, Chs) ->
    {Ch, Chs2} = alloc(Chs),
    {reply, Ch, Chs2}.

handle_cast({free, Ch}, Chs) ->
    Chs2 = free(Ch, Chs),
    {noreply, Chs2}.
```

# Relationships

## Builds Upon
- **Behaviour** — gen_server is an OTP behaviour
- **Client-Server Model** — gen_server implements the server side
- **Callback Module** — users write a callback module to use gen_server

## Enables
- **gen_server:call** — synchronous request mechanism
- **gen_server:cast** — asynchronous request mechanism
- **gen_server:init** — initialization callback
- **gen_server:terminate** — termination callback

## Related
- **handle_info** — handling non-request messages
- **code_change** — hot code upgrade support
- **Supervision Tree** — gen_servers are typically children in supervision trees

## Contrasts With
- **gen_statem** — for implementing state machines (multiple named states), whereas gen_server handles a single-state request-response loop
- **gen_event** — for event handling with multiple handlers, whereas gen_server is a single server process

# Common Errors

- **Error**: Using `gen_server:start/4` instead of `gen_server:start_link/4` for a supervised process.
  **Correction**: "gen_server:start_link/4 must be used if the gen_server is part of a supervision tree."

# Common Confusions

- **Confusion**: Thinking gen_server handles only synchronous requests.
  **Clarification**: gen_server supports both synchronous requests (call) and asynchronous requests (cast), as well as arbitrary messages (handle_info).

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly from gen_server_concepts.md and design_principles.md "Behaviours" section.
- Confidence rationale: High — the primary subject of the gen_server chapter with complete examples.
- Uncertainties: None.
- Cross-reference status: References behaviour, callback-module, client-server-model, gen-statem, gen-event (planned cards).
