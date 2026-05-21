---
concept: gen_event notify
slug: gen-event-notify
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
  - "gen_event:notify/2"
  - "gen_event:sync_notify/2"
  - event notification
prerequisites:
  - gen-event
  - event-manager
extends: []
related:
  - event-manager
  - gen-event-handle-call
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# gen_event notify

## Quick Definition

`gen_event:notify/2` sends an event to an event manager asynchronously; `gen_event:sync_notify/2` sends it synchronously, blocking the caller until every handler has processed it.

## Core Definition

"All incoming events can come from `gen_event:notify/2`, which is asynchronous, like `gen_server:cast/2`. There is also `gen_event:sync_notify/2`, which is synchronous. ... The idea here is that the function call returns only after all the event handlers have seen and treated the new message" (Ch. 16, "The handle_event Function").

## Prerequisites

- **gen_event** — `notify`/`sync_notify` are `gen_event` functions.
- **Event manager** — Events are sent *to* a manager.

## Key Properties

1. `notify/2` is asynchronous — analogous to `gen_server:cast/2`.
2. `sync_notify/2` is synchronous — the call returns only after all handlers have treated the event.
3. Both deliver the event to *every* handler attached to the manager.
4. Both ultimately invoke each handler's `handle_event/2` callback.
5. `handle_event/2` itself stays asynchronous regardless; `sync_notify/2` only blocks the *caller*.

## Construction / Recognition

## To Send an Event

1. Fire-and-forget: `gen_event:notify(ManagerPid, Event)`.
2. Wait until all handlers have processed it: `gen_event:sync_notify(ManagerPid, Event)`.

## Context & Application

The curling example sends all game events with `notify/2` — e.g. `gen_event:notify(Pid, {set_teams, "Pirates", "Scotsmen"})`. The `curling` abstraction module wraps these so callers never see the `gen_event` protocol. `sync_notify/2` is the right choice when the caller must know an event has been fully processed before continuing.

## Examples

**Example 1** (Ch. 16): `gen_event:notify(Pid, {add_points, "Pirates", 3})` — asynchronously delivers the event to all handlers.

**Example 2** (Ch. 16): `set_teams(Pid, TeamA, TeamB) -> gen_event:notify(Pid, {set_teams, TeamA, TeamB}).` — the `curling` module wraps `notify/2`.

## Relationships

## Builds Upon

- **Event manager** — Events are notified to a manager.

## Related

- **gen-event-handle-call** — `gen_event:call/3` is the synchronous *single-handler query*, distinct from `sync_notify/2`.

## Common Errors

- **Error**: Using `notify/2` when the caller must be sure the event was handled before proceeding.
  **Correction**: Use `sync_notify/2`, which returns only after every handler has treated the event.

## Common Confusions

- **Confusion**: Thinking `sync_notify/2` makes `handle_event/2` synchronous.
  **Clarification**: `handle_event/2` stays asynchronous; `sync_notify/2` only blocks the calling process.

## Source Reference

Chapter 16: "Event Handlers," section "The handle_event Function"; usage throughout "It's Curling Time!".

## Verification Notes

- Definition: Direct quote from "The handle_event Function."
- Key Properties: Synthesised from the notify discussion.
- Confidence: HIGH — explicitly defined.
