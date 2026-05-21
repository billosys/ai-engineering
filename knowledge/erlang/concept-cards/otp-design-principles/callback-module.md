---
# === CORE IDENTIFICATION ===
concept: Callback Module
slug: callback-module

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Overview"
chapter_number: null
pdf_page: null
section: "Behaviours"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "callback mod"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
extends: []
related:
  - gen-server
  - gen-event
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a callback module?"
  - "How does a behaviour module relate to a callback module?"
  - "How do I implement a callback module?"
---

# Quick Definition

A callback module is the user-written, application-specific part of an OTP behaviour, which exports a pre-defined set of callback functions that the behaviour module invokes.

# Core Definition

According to the OTP Design Principles Overview, a behaviour divides process code into "a generic part (a behaviour module) and a specific part (a callback module)." The callback module must "export a pre-defined set of functions, the callback functions." The behaviour module handles generic process management (message passing, receive loops, error handling), while the callback module contains the application-specific logic invoked by the behaviour at well-defined points.

# Prerequisites

- **Behaviour** — callback modules are the user-written counterpart to OTP behaviour modules.

# Key Properties

1. Contains application-specific logic, separate from generic process management.
2. Must export a pre-defined set of callback functions as specified by the behaviour.
3. Declared using the `-behaviour(BehaviourName)` module attribute.
4. The compiler warns about missing callback functions when this attribute is present.
5. Interface functions and callback functions are usually co-located in the same module.

# Construction / Recognition

## To Construct/Create:
1. Create a new Erlang module file.
2. Add the `-behaviour(BehaviourName)` module attribute (e.g., `-behaviour(gen_server)`).
3. Implement all required callback functions (e.g., `init/1`, `handle_call/3`, `handle_cast/2` for gen_server).
4. Define interface functions (e.g., `start_link/0`, `alloc/0`) that delegate to the behaviour module.
5. Export both interface functions and callback functions.

## To Identify/Recognize:
1. Contains a `-behaviour(...)` attribute.
2. Exports functions matching the callback signatures defined by the behaviour (e.g., `init/1`, `handle_call/3`).
3. Typically contains both interface functions (public API) and callback functions (invoked by the behaviour).

# Context & Application

Callback modules are the primary unit of user-written code in OTP applications. Rather than implementing process logic from scratch, developers write callback modules that plug into OTP behaviours. This separation provides several benefits noted in the source: the server name and protocol are hidden from clients, the functionality of the behaviour can be extended without changing any callback module, and code is more readable and consistent.

# Examples

**Example 1** (design_principles.md, "Behaviours"): The `ch2` module is a callback module for the custom `server` behaviour:
```erlang
-module(ch2).
-export([start/0]).
-export([alloc/0, free/1]).
-export([init/0, handle_call/2, handle_cast/2]).

start() ->
    server:start(ch2).

alloc() ->
    server:call(ch2, alloc).

free(Ch) ->
    server:cast(ch2, {free, Ch}).

init() ->
    channels().

handle_call(alloc, Chs) ->
    alloc(Chs).

handle_cast({free, Ch}, Chs) ->
    free(Ch, Chs).
```

**Example 2** (design_principles.md, "Behaviours"): The compiler checks callback completeness:
```erlang
-module(chs3).
-behaviour(gen_server).
...
3> c(chs3).
./chs3.erl:10: Warning: undefined call-back function handle_call/3
```

# Relationships

## Builds Upon
- **Behaviour** — a callback module is the user-specific counterpart to a behaviour module.

## Enables
- **gen_server** — gen_server callback modules implement server logic
- **gen_event** — gen_event callback modules implement event handler logic

## Related
- **Worker Process** — workers are typically implemented as callback modules
- **Supervision Tree** — callback modules are the building blocks of supervision tree processes

## Contrasts With
- No explicit contrasts, but implicitly contrasts with writing plain Erlang processes without behaviours (as in the `ch1` example).

# Common Errors

- **Error**: Not implementing all required callback functions.
  **Correction**: The compiler warns about missing callbacks. Ensure every function specified by the behaviour is implemented and exported.

- **Error**: Placing interface functions and callback functions in separate modules.
  **Correction**: The source advises that "it is usually good programming practice to have the code corresponding to one process contained in a single module."

# Common Confusions

- **Confusion**: Thinking the callback module IS the behaviour.
  **Clarification**: The behaviour module (e.g., `gen_server`) is the generic, OTP-provided part. The callback module is the user-written, application-specific part. Together they form a complete process implementation.

# Source Reference

OTP Design Principles, Overview, "Behaviours" section (design_principles.md).

# Verification Notes

- Definition source: Directly quoted from design_principles.md "Behaviours" section.
- Confidence rationale: High — explicitly defined and illustrated with examples in the source.
- Uncertainties: None.
- Cross-reference status: References behaviour, gen-server, gen-event (planned cards).
