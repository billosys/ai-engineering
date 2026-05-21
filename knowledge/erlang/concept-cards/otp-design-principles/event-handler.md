---
# === CORE IDENTIFICATION ===
concept: Event Handler
slug: event-handler

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-event
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_event Behaviour"
chapter_number: null
pdf_page: null
section: "Event Handling Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_event handler"
  - "event handler module"
  - "event handler callback module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
  - callback-module
extends:
  - callback-module
related:
  - gen-event-notify
  - adding-event-handler
  - deleting-event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler in gen_event?"
  - "How do event handlers relate to event managers in gen_event?"
  - "How do I implement a gen_event event handler?"
---

# Quick Definition

An event handler is a callback module installed in a gen_event event manager that processes events by implementing `init/1`, `handle_event/2`, and `terminate/2`.

# Core Definition

According to the gen_event Behaviour chapter: "In the event manager, zero, one, or many event handlers are installed. When the event manager is notified about an event, the event is processed by all the installed event handlers." Each event handler is "implemented as a callback module." The event manager maintains a list of `{Module, State}` pairs, where "each Module is an event handler, and State is the internal state of that event handler."

# Prerequisites

- **gen_event** — event handlers are part of the gen_event framework.
- **Event Manager** — event handlers are installed in an event manager.
- **Callback Module** — an event handler is a callback module.

# Key Properties

1. Implemented as a callback module with `-behaviour(gen_event)`.
2. Must implement `init/1`, `handle_event/2`, and `terminate/2`.
3. Each handler has its own independent internal state.
4. Multiple handlers can be installed in a single event manager.
5. Handlers can be dynamically added and removed at runtime.
6. All handlers process each event, in the order they were added.
7. `init/1` returns `{ok, State}`, `handle_event/2` returns `{ok, State1}`, `terminate/2` does cleanup.

# Construction / Recognition

## To Construct/Create:
1. Create a module with `-behaviour(gen_event)`.
2. Implement `init/1` to return `{ok, InitialState}`.
3. Implement `handle_event(Event, State)` to process events, returning `{ok, NewState}`.
4. Implement `terminate(Args, State)` to clean up resources.
5. Install the handler with `gen_event:add_handler(Manager, Module, InitArgs)`.

## To Identify/Recognize:
1. A module with `-behaviour(gen_event)` attribute.
2. Exports `init/1`, `handle_event/2`, `terminate/2`.
3. Installed in an event manager, not started as its own process.

# Context & Application

Event handlers provide the extensible, pluggable processing logic in gen_event. Because handlers are added and removed dynamically, the system's event processing capabilities can change at runtime. The source's example shows this clearly: a `terminal_logger` handler is always installed, and a `file_logger` handler can be added temporarily when file logging is needed, then removed when it is not.

# Examples

**Example 1** (events.md, "Example"): The `terminal_logger` event handler:
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

**Example 2** (events.md, "Example"): The `file_logger` event handler, which maintains a file descriptor as state:
```erlang
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
- **gen_event** — event handlers are the callback module component of gen_event
- **Event Manager** — handlers are installed in and dispatched by the event manager
- **Callback Module** — an event handler is a specific type of callback module

## Enables
- No specific downstream concepts.

## Related
- **Adding Event Handler** — how handlers get installed in the event manager
- **Deleting Event Handler** — how handlers are removed from the event manager
- **gen_event:notify** — triggers handle_event/2 on all installed handlers

## Contrasts With
- No direct contrasts, but implicitly differs from gen_server callback modules in that multiple handler modules coexist in a single process (the event manager).

# Common Errors

- **Error**: Not implementing `terminate/2` for handlers that acquire resources in `init/1`.
  **Correction**: The source states that "terminate/2 is to be the opposite of init/1 and do any necessary cleaning up." For `file_logger`, the file descriptor opened in `init/1` must be closed in `terminate/2`.

# Common Confusions

- **Confusion**: Thinking each event handler runs in its own process.
  **Clarification**: All event handlers run within the single event manager process. Each handler is a `{Module, State}` pair maintained by the event manager, not a separate process.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter, "Event Handling Principles" and "Example" sections (events.md).

# Verification Notes

- Definition source: Directly quoted from events.md "Event Handling Principles" section.
- Confidence rationale: High — explicitly defined with two complete examples (terminal_logger, file_logger).
- Uncertainties: None.
- Cross-reference status: References gen-event, event-manager, callback-module, adding-event-handler, deleting-event-handler, gen-event-notify (planned cards).
