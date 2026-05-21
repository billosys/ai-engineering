---
# === CORE IDENTIFICATION ===
concept: Event Manager
slug: event-manager

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
  - "gen_event manager"
  - "event manager process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
extends: []
related:
  - event-handler
  - gen-event-notify
  - adding-event-handler
  - deleting-event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event manager in gen_event?"
  - "How do event handlers relate to event managers in gen_event?"
  - "How do I start a gen_event event manager?"
---

# Quick Definition

An event manager is a named process in OTP's gen_event framework that receives events and dispatches them to all installed event handlers for processing.

# Core Definition

According to the gen_event Behaviour chapter: "In OTP, an event manager is a named object to which events can be sent. An event can be, for example, an error, an alarm, or some information that is to be logged." The source further explains: "An event manager is implemented as a process and each event handler is implemented as a callback module. The event manager essentially maintains a list of {Module, State} pairs, where each Module is an event handler, and State is the internal state of that event handler."

# Prerequisites

- **gen_event** — the event manager is the process component of the gen_event framework.

# Key Properties

1. Implemented as a single Erlang process.
2. Can be locally or globally registered by name.
3. Maintains a list of `{Module, State}` pairs — one per installed event handler.
4. When notified of an event, calls `handle_event/2` on all installed handlers in order.
5. Started with `gen_event:start_link/1` (supervised) or `gen_event:start/1` (standalone).
6. Automatically terminated by its supervisor when part of a supervision tree.

# Construction / Recognition

## To Construct/Create:
1. Start with `gen_event:start_link({local, Name})` for a supervised event manager.
2. Or use `gen_event:start({local, Name})` for a standalone event manager.
3. Add event handlers using `gen_event:add_handler/3`.
4. Send events using `gen_event:notify/2`.

## To Identify/Recognize:
1. A process started with `gen_event:start_link/1` or `gen_event:start/1`.
2. Holds a list of installed event handler modules.
3. Dispatches events to handlers when `gen_event:notify/2` is called.

# Context & Application

The event manager is the central dispatcher in gen_event's architecture. It decouples event producers (which call `gen_event:notify/2`) from event consumers (event handler callback modules). Event handlers can be added and removed at runtime without stopping the event manager or affecting other handlers. This makes the architecture highly extensible.

# Examples

**Example 1** (events.md, "Starting an Event Manager"): Starting an event manager for error handling:
```erlang
gen_event:start_link({local, error_man})
```
"gen_event:start_link/1 spawns and links to a new event manager process." The argument `{local, error_man}` specifies the local registration name.

**Example 2** (events.md, "Stopping"): Stopping a standalone event manager:
```erlang
gen_event:stop(error_man).
```
"When an event manager is stopped, it gives each of the installed event handlers the chance to clean up by calling terminate/2."

# Relationships

## Builds Upon
- **gen_event** — the event manager is the process component of gen_event.

## Enables
- **Adding Event Handler** — handlers are added to the event manager
- **Deleting Event Handler** — handlers are removed from the event manager
- **gen_event:notify** — events are sent to the event manager for dispatch

## Related
- **Event Handler** — event handlers are installed in the event manager
- **Supervision Tree** — event managers can be supervised

## Contrasts With
- No direct contrasts in source. Implicitly differs from gen_server in that the event manager holds multiple callback modules, not just one.

# Common Errors

- **Error**: Using `gen_event:start/1` for an event manager that should be supervised.
  **Correction**: "gen_event:start_link/1 must be used if the event manager is part of a supervision tree."

# Common Confusions

- **Confusion**: Thinking the event manager is just a module name.
  **Clarification**: The event manager is an actual Erlang process. It is "implemented as a process" that maintains handler state and dispatches events.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter, "Event Handling Principles" and "Starting an Event Manager" sections (events.md).

# Verification Notes

- Definition source: Directly quoted from events.md "Event Handling Principles" section.
- Confidence rationale: High — explicitly defined in multiple sections with examples.
- Uncertainties: None.
- Cross-reference status: References gen-event, event-handler, gen-event-notify, adding-event-handler, deleting-event-handler (planned cards).
