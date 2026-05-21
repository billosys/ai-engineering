---
# === CORE IDENTIFICATION ===
concept: Event Handler
slug: event-handler

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 167
section: "Adding Event Handlers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - handler
  - "gen_event handler"
  - event handler callback module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-manager
  - gen-event-behavior
extends: []
related:
  - notifying-events
  - swapping-event-handlers
  - supervised-event-handlers
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I implement a gen_server callback module?"
  - "What is a callback module?"
---

# Quick Definition

An event handler is a `gen_event` callback module that subscribes to a manager's events; it is added and removed dynamically at runtime, and the same handler can serve multiple managers and event types.

# Core Definition

"*Event handlers* are behavior callback modules that handle these types of actions. They subscribe to events sent to a manager, allowing different handlers to subscribe to the same events. Different managers handling different event types can use the same event handler" (Cesarini & Vinoski, p. 167). "Event handlers are added to and removed from the event manager process dynamically, at runtime. They are considered more generic than other behaviors because you can implement an event handler that can not only handle different event types, but do so in different event managers" (p. 169). A handler is added with `gen_event:add_handler(Name, Mod, Args)`, which calls `Mod:init(Args)` expecting `{ok, LoopData}`; the loop data refers to that particular handler instance. A handler is deleted with `gen_event:delete_handler/3`, which invokes `Mod:terminate/2`.

# Prerequisites

- **Event manager** — Handlers are added to a manager and run within its process.
- **Generic event behavior** — A handler is a `gen_event` callback module.

# Key Properties

1. A `gen_event` callback module — declares `-behavior(gen_event)`.
2. Added/removed dynamically at runtime via `add_handler/3` and `delete_handler/3`.
3. Callbacks: `init/1`, `terminate/2`, `handle_event/2`, `handle_info/2` (and optionally `handle_call/2`).
4. `init/1` must return `{ok, LoopData}` (or `{ok, LoopData, hibernate}`) or the handler is *not* added.
5. The same handler module can be added to many managers and handle many event types.
6. The same handler can be added multiple times to one manager, each with its own loop data, distinguished by `{Module, Id}`.
7. Each handler has its own loop data, stored by the manager in a list.

# Construction / Recognition

## To Implement an Event Handler:
1. Declare `-module`, `-behavior(gen_event)`, and export `init/1`, `terminate/2`, `handle_event/2`, `handle_info/2`.
2. Implement `init/1` returning `{ok, LoopData}`.
3. Implement `handle_event/2` returning `{ok, NewData}` (or `remove_handler` / a swap tuple).
4. Implement `terminate/2` for cleanup.
5. Add it to a manager with `gen_event:add_handler(Name, Mod, Args)`.

# Context & Application

- **Typical contexts**: Logging, statistics collection, alarm handling — pluggable actions for a manager's events.
- **Common applications**: The `logger` handler (logs to file or stdout) and `counters` handler (bumps an ETS counter).
- **Historical/stylistic notes**: A handler can be specified as `{Module, Id}` so client functions can differentiate multiple handlers using the same callback module (p. 170).

# Examples

**Example 1** (p. 169): The `logger` event handler's `init/1`:

```erlang
-module(logger).
-behavior(gen_event).
-export([init/1, terminate/2, handle_event/2, handle_info/2]).
init(standard_io) ->
    {ok, {standard_io, 1}};
init({file, File}) ->
    {ok, Fd} = file:open(File, write),
    {ok, {Fd, 1}};
init(Args) ->
    {error, {args, Args}}.
```

**Example 2** (p. 174): The `counters` handler stores metrics in an ETS table, initialized in `init/1` and torn down in `terminate/2`.

# Relationships

## Builds Upon
- **Event manager** — A handler runs inside a manager's process.
- **Generic event behavior** — A handler is a `gen_event` callback module.

## Enables
- **notifying-events** — Handlers receive notified events in `handle_event/2`.
- **swapping-event-handlers** — Handlers can be swapped, passing state to a successor.
- **supervised-event-handlers** — A handler can be added supervised.

## Related
- **notifying-events** — `handle_event/2` is the handler's notification callback.

## Contrasts With
- **Generic server** — A `gen_server` has one callback module per process; a manager has many handlers, each a callback module.

# Common Errors

- **Error**: Returning `ok` from `init/1` instead of `{ok, LoopData}`.
  **Correction**: Whenever `init/1` does not return `{ok, LoopData}`, the handler is silently *not* added; always return `{ok, LoopData}` or `{error, Reason}`.

# Common Confusions

- **Confusion**: Thinking each handler module can be added only once per manager.
  **Clarification**: The same handler can be added multiple times, each with its own loop data; use `{Module, Id}` to tell instances apart.

# Source Reference

Chapter 6: Event Handlers, Section "Adding Event Handlers," pages 167-171. See Figures 7-2 and 7-3.

# Verification Notes

- Definition source: Direct quotes from pp. 167-169.
- Confidence rationale: HIGH — the source explicitly defines event handlers and their dynamic add/remove semantics.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
