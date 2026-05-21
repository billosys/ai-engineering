---
# === CORE IDENTIFICATION ===
concept: gen_event Behaviour
slug: gen-event

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_event Behaviour"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_event"
  - "generic event"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - callback-module
extends:
  - behaviour
related:
  - event-manager
  - event-handler
  - gen-event-notify
  - adding-event-handler
  - deleting-event-handler
contrasts_with:
  - gen-server
  - gen-statem

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_event?"
  - "How do event handlers relate to event managers in gen_event?"
  - "How do I implement a gen_event event handler?"
---

# Quick Definition

`gen_event` is the OTP behaviour for implementing event handling functionality, where an event manager process dispatches events to zero or more dynamically installed event handler callback modules.

# Core Definition

The OTP Design Principles describe gen_event as one of the four standard behaviours, used "for implementing event handling functionality." The gen_event Behaviour chapter explains the architecture: "an event manager is a named object to which events can be sent. In the event manager, zero, one, or many event handlers are installed. When the event manager is notified about an event, the event is processed by all the installed event handlers." The event manager is a process, and "each event handler is implemented as a callback module."

# Prerequisites

- **Behaviour** — gen_event is an OTP behaviour.
- **Callback Module** — event handlers are implemented as callback modules.

# Key Properties

1. Separates event managers (processes) from event handlers (callback modules).
2. An event manager maintains a list of `{Module, State}` pairs, one per handler.
3. Multiple event handlers can be installed in a single event manager.
4. Handlers can be dynamically added and removed at runtime.
5. When an event is notified, all installed handlers process it in order.
6. Started with `gen_event:start_link/1` (supervised) or `gen_event:start/1` (standalone).

# Construction / Recognition

## To Construct/Create:
1. Start an event manager with `gen_event:start_link({local, Name})`.
2. Write one or more event handler callback modules with `-behaviour(gen_event)`.
3. Each handler implements `init/1`, `handle_event/2`, and `terminate/2`.
4. Add handlers with `gen_event:add_handler(Manager, Module, Args)`.
5. Send events with `gen_event:notify(Manager, Event)`.

## To Identify/Recognize:
1. A module with `-behaviour(gen_event)` that implements `handle_event/2`.
2. A process started with `gen_event:start_link/1`.
3. Multiple callback modules installed in a single event manager process.

# Context & Application

`gen_event` is used when events need to be processed by multiple independent handlers that can be added and removed dynamically. The canonical example from the source is error logging: a terminal logger handler writes errors to the console, and a file logger handler can be added temporarily to also write errors to a file. This decouples event producers from event consumers.

# Examples

**Example 1** (events.md, "Example"): A terminal logger event handler:
```erlang
-module(terminal_logger).
-behaviour(gen_event).

-export([init/1, handle_event/2, terminate/2]).

init(_Args) ->
    {ok, []}.

handle_event(ErrorMsg, State) ->
    io:format("***Error*** ~p~n", [ErrorMsg]),
    {ok, State}.

terminate(_Args, _State) ->
    ok.
```

**Example 2** (events.md, "Example"): A file logger event handler:
```erlang
-module(file_logger).
-behaviour(gen_event).

-export([init/1, handle_event/2, terminate/2]).

init(File) ->
    {ok, Fd} = file:open(File, read),
    {ok, Fd}.

handle_event(ErrorMsg, Fd) ->
    io:format(Fd, "***Error*** ~p~n", [ErrorMsg]),
    {ok, Fd}.

terminate(_Args, Fd) ->
    file:close(Fd).
```

# Relationships

## Builds Upon
- **Behaviour** — gen_event is an OTP behaviour
- **Callback Module** — event handlers are callback modules

## Enables
- **Event Manager** — the process component of gen_event
- **Event Handler** — the callback module component of gen_event
- **gen_event:notify** — the mechanism for sending events
- **Adding Event Handler** — dynamic handler installation
- **Deleting Event Handler** — dynamic handler removal

## Related
- **Supervision Tree** — event managers can be part of supervision trees

## Contrasts With
- **gen_server** — gen_server is a single server process with one callback module; gen_event is one process with multiple handler callback modules
- **gen_statem** — gen_statem manages state transitions; gen_event dispatches events to handlers

# Common Errors

- **Error**: Implementing an event manager as a gen_server with a list of handlers.
  **Correction**: Use gen_event, which provides this pattern out of the box with proper handler lifecycle management.

# Common Confusions

- **Confusion**: Thinking each event handler is a separate process.
  **Clarification**: All event handlers run within the single event manager process. The event manager maintains a list of `{Module, State}` pairs and calls each handler's callbacks sequentially.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter (events.md) and Overview "Behaviours" section (design_principles.md).

# Verification Notes

- Definition source: Directly from events.md "Event Handling Principles" section and design_principles.md "Behaviours" section.
- Confidence rationale: High — the primary subject of the gen_event chapter with complete examples.
- Uncertainties: None.
- Cross-reference status: References behaviour, callback-module, event-manager, event-handler, gen-server, gen-statem (planned cards).
