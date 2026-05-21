---
concept: Event Handler
slug: event-handler
category: otp-behaviours
subcategory: event-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "The handle_event Function"
extraction_confidence: high
aliases:
  - handler
  - "gen_event handler"
  - callback handler
prerequisites:
  - gen-event
  - event-manager
extends: []
related:
  - event-manager
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
  - "How does a behaviour relate to its callback module?"
---

# Event Handler

## Quick Definition

An event handler is a `gen_event` callback module attached to an event manager. It is "a bunch of functions running in the manager," each keeping its own state, invoked on every event the manager receives.

## Core Definition

The book describes event handlers as "a bunch of functions running in the manager. ... Each event handler can hold its own state, which is carried around by the manager" (Ch. 16, "Generic Event Handlers"). A handler's core callback is `handle_event(Event, State)`, "more or less the core of `gen_event`'s callback modules."

## Prerequisites

- **gen_event** — Handlers implement the `gen_event` behaviour.
- **event-manager** — Handlers must be attached to a manager to run.

## Key Properties

1. A handler is a module implementing `init/1`, `handle_event/2`, `handle_call/2`, `handle_info/2`, `code_change/3`, `terminate/2`.
2. Multiple handlers (even multiple instances of the same module) can be attached to one manager.
3. Each handler keeps its own private state.
4. `handle_event/2` may return `{ok, NewState}`, `{ok, NewState, hibernate}`, `remove_handler`, or `{swap_handler, Args1, NewState, NewHandler, Args2}`.
5. `remove_handler` drops the handler; `swap_handler` replaces it with another (calling `terminate` on the old and `init` on the new).
6. To address a specific instance, attach it under `{Module, Ref}` (commonly using `make_ref()`).
7. Attach with `gen_event:add_handler/3`; remove with `gen_event:delete_handler/3`.

## Construction / Recognition

## To Add a Handler

1. Write the callback module (or reuse the skeleton with `{ok, State}` returns).
2. Attach it: `gen_event:add_handler(ManagerPid, Module, Args)`.
3. For uniquely identifiable instances: `gen_event:add_handler(Pid, {Module, make_ref()}, Args)`.
4. Remove it: `gen_event:delete_handler(Pid, HandlerId, Arg)` — the `Arg` is passed to `terminate/2`.

## Context & Application

In the curling example, `curling_scoreboard` forwards events to hardware, `curling_feed` forwards events to a subscriber pid, and `curling_accumulator` keeps running game state. Multiple press-feed handlers are added under `{curling_feed, make_ref()}` so each reporter can be individually unsubscribed.

For handlers that must be cleaned up when their owner crashes, use `gen_event:add_sup_handler/3` instead — the book warns this has a backward-compatibility wart involving links and superfluous `'EXIT'` messages.

## Examples

**Example 1** (Ch. 16): `curling_feed` — `handle_event(Event, Pid) -> Pid ! {curling_feed, Event}, {ok, Pid}.` blindly forwards events to a subscriber.

**Example 2** (Ch. 16): `join_feed(Pid, ToPid)` adds a handler under `HandlerId = {curling_feed, make_ref()}` and returns that id so `leave_feed/2` can delete exactly that instance.

## Relationships

## Builds Upon

- **gen_event** — The behaviour the handler implements.

## Related

- **event-manager** — Handlers run inside a manager and are added/removed via `gen_event` calls.

## Common Errors

- **Error**: Adding multiple handlers of the same module under the bare module name, then trying to delete one.
  **Correction**: The manager picks an instance in an undefined manner; use `{Module, Ref}` ids to address a specific instance.
- **Error**: Writing a handler with a long-running or infinite loop in `handle_event/2`.
  **Correction**: Handlers share the manager process; forward to a separate process for long work.

## Common Confusions

- **Confusion**: Thinking a handler is a process.
  **Clarification**: A handler is a set of callback functions running *inside* the manager process, with its own carried state.

## Source Reference

Chapter 16: "Event Handlers," sections "The handle_event Function," "Game Events," and "Alert the Press!" (the `{Module, Ref}` technique and `add_sup_handler/3` discussion).

## Verification Notes

- Definition: Adapted from "Generic Event Handlers."
- Key Properties: `handle_event/2` return values copied from the source's enumerated list; instance-id technique from "Alert the Press!".
- Confidence: HIGH — explicitly defined with code.
