---
concept: Event Manager
slug: event-manager
category: otp-behaviours
subcategory: event-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "Handle This! *pumps shotgun*"
extraction_confidence: high
aliases:
  - manager
  - "gen_event manager"
  - event hub
prerequisites:
  - gen-event
  - process
extends: []
related:
  - event-handler
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# Event Manager

## Quick Definition

An event manager is the process run by `gen_event`. It accepts event handler callback modules and runs their functions on every incoming event, acting as a central notification hub.

## Core Definition

"This third approach simply takes a process that accepts functions and lets them run on any incoming event. This process is usually called an *event manager*" (Ch. 16, "Handle This!"). The manager forwards every event it receives to all attached handlers, which run inside it.

## Prerequisites

- **gen_event** — The behaviour that implements the manager.
- **Process** — The manager is a single Erlang process.

## Key Properties

1. A single process hosts any number of event handlers.
2. Events are delivered to it asynchronously with `gen_event:notify/2` or synchronously with `gen_event:sync_notify/2`.
3. With `sync_notify/2`, the call returns only after all handlers have processed the event.
4. Synchronous calls to a specific handler use `gen_event:call/3,4`.
5. Started with `gen_event:start_link/0` (or `start/0`).
6. The manager keeps running even when all handlers are removed.

## Construction / Recognition

## To Use an Event Manager

1. Start it: `{ok, Pid} = gen_event:start_link()`.
2. Attach handlers with `gen_event:add_handler/3` (as many as needed).
3. Send events with `gen_event:notify/2` (async) or `gen_event:sync_notify/2` (sync).
4. Query a handler with `gen_event:call/3`.
5. Remove handlers with `gen_event:delete_handler/3`.

## Context & Application

The event manager's advantages over per-subscriber processes: the server forwards events only once (to the manager); large data is transferred once and shared by all callbacks; no need to spawn processes for short-lived tasks. Its downsides: long-running handler functions block each other, and an infinitely-looping handler can stall all event handling.

The book recommends wrapping `gen_event` calls in an *abstraction module* (e.g. the `curling` module) so callers do not depend on the manager's protocol directly. The manager effectively becomes a "message hub, just routing messages to whoever needs them."

## Examples

**Example 1** (Ch. 16): `gen_event:notify(Pid, {set_teams, "Pirates", "Scotsmen"})` sends an event that the scoreboard handler turns into a hardware call.

**Example 2** (Ch. 16): The `curling` module's `start_link/2` starts a manager, attaches the `curling_scoreboard` and `curling_accumulator` handlers, and returns the pid — hiding `gen_event` from callers.

## Relationships

## Builds Upon

- **gen_event** — The behaviour providing the manager.

## Related

- **event-handler** — Handlers run inside the manager.

## Common Errors

- **Error**: Calling `gen_event` functions directly from many places in the codebase.
  **Correction**: Wrap them in an abstraction module so the protocol can change without breaking callers.

## Common Confusions

- **Confusion**: Thinking `sync_notify/2` makes `handle_event/2` synchronous.
  **Clarification**: `handle_event/2` is still asynchronous; `sync_notify/2` only blocks the *caller* until all handlers have seen the event.

## Source Reference

Chapter 16: "Event Handlers," sections "Handle This! *pumps shotgun*" and "It's Curling Time!" (the `curling` abstraction module).

## Verification Notes

- Definition: Direct quote from "Handle This!".
- Key Properties: Synthesised from the advantages/downsides list and the `notify`/`sync_notify`/`call` discussion.
- Confidence: HIGH — explicitly defined.
