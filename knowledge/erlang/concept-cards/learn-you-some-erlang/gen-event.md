---
concept: gen_event Behaviour
slug: gen-event
category: otp-behaviours
subcategory: event-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "Generic Event Handlers"
extraction_confidence: high
aliases:
  - "gen_event"
  - generic event handler behaviour
prerequisites:
  - otp-behaviour
  - gen-server
  - process
extends:
  - otp-behaviour
related:
  - event-handler
  - event-manager
contrasts_with:
  - gen-server
  - gen-fsm
answers_questions:
  - "What is the gen_event behaviour?"
  - "How does a behaviour relate to its callback module?"
---

# gen_event Behaviour

## Quick Definition

`gen_event` is the OTP behaviour for event handling. It runs an *event manager* process that accepts callback modules (event handlers) and calls their functions on every incoming event.

## Core Definition

"The `gen_event` behavior differs quite a bit from the `gen_server` and `gen_fsm` behaviors in that you are never really starting a process. ... The `gen_event` behavior basically runs the process that accepts and calls functions, and you only need to provide a module with these functions. This means that you have nothing to do with event manipulation except to place your callback functions in a format that pleases the event manager" (Ch. 16, "Generic Event Handlers").

A `gen_event` callback module implements `init/1`, `handle_event/2`, `handle_call/2`, `handle_info/2`, `code_change/3`, and `terminate/2`.

## Prerequisites

- **OTP behaviour** — `gen_event` is one of the core OTP behaviours.
- **gen_server** — Its callbacks parallel `gen_server`'s (`handle_event` is like `handle_cast`).
- **Process** — The event manager is a process; handlers run inside it.

## Key Properties

1. You do not spawn a process per callback module; you attach handlers to a manager.
2. The standard spawn/init/loop/terminate pattern applies to *event handlers*, not to your code starting a process.
3. `handle_event/2` is asynchronous, like `gen_server:handle_cast/2`.
4. `handle_call/2` allows synchronous interaction with a specific handler.
5. `handle_info/2` handles out-of-band messages (e.g. `!`-sent messages, exit signals).
6. Each handler keeps its own state, carried around by the manager.
7. OTP separates the generic part (the manager) from the specific part (your handler callbacks).

## Construction / Recognition

## To Write a gen_event Callback Module

1. Add `-behavior(gen_event).`
2. Implement `init/1` returning `{ok, State}`.
3. Implement `handle_event/2`, `handle_call/2`, `handle_info/2`.
4. Implement `code_change/3` and `terminate/2`.
5. Start a manager with `gen_event:start_link/0` and attach the handler with `gen_event:add_handler/3`.

## Context & Application

`gen_event` is "one of the many strategies to handle notifications." Its most common real-world uses — not shown in the book — are logging and system alarms (see the `error_logger` module). Chapter 16 instead builds a curling scoreboard and press-feed notification system.

The behaviour is current in modern OTP; no deprecation applies.

## Examples

**Example 1** (Ch. 16): `curling_scoreboard` declares `-behavior(gen_event).` and forwards `{set_teams, ...}`, `{add_points, ...}`, and `next_round` events to a hardware module.

**Example 2** (Ch. 16): `{ok, Pid} = gen_event:start_link()` starts a manager; `gen_event:add_handler(Pid, curling_scoreboard, [])` attaches a handler.

## Relationships

## Builds Upon

- **OTP behaviour** — Generic event-handling machinery factored out by OTP.

## Related

- **event-handler** — The callback module attached to a manager.
- **event-manager** — The process `gen_event` runs.

## Contrasts With

- **gen-server** — A `gen_server` is one process; a `gen_event` manager hosts many swappable handlers.
- **gen-fsm** — Both are specialised behaviours, but `gen_event` is about notifications, not state transitions.

## Common Errors

- **Error**: Expecting `gen_event:start_link/0` to start your callback module's process.
  **Correction**: It starts only the manager; handlers must be added separately with `add_handler/3`.

## Common Confusions

- **Confusion**: Thinking each handler runs in its own process.
  **Clarification**: All handlers run inside the single event manager process; a long-looping handler blocks the others.

## Source Reference

Chapter 16: "Event Handlers," section "Generic Event Handlers" (callback subsections) and "It's Curling Time!" for worked examples.

## Verification Notes

- Definition: Direct quote from "Generic Event Handlers."
- Key Properties: Synthesised from the callback subsections and the curling examples.
- Confidence: HIGH — behaviour and callbacks explicitly described.
