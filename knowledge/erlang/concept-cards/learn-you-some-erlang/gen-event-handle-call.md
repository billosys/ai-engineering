---
concept: gen_event handle_call
slug: gen-event-handle-call
category: otp-behaviours
subcategory: event-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "The handle_call Function"
extraction_confidence: high
aliases:
  - "handle_call/2"
  - synchronous event-handler query
prerequisites:
  - gen-event
  - event-handler
extends: []
related:
  - event-handler
  - event-manager
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# gen_event handle_call

## Quick Definition

`handle_call/2` is the `gen_event` callback for synchronously querying *one specific* event handler in a manager, invoked by `gen_event:call/3,4`.

## Core Definition

"The `handle_call` function is similar to a `gen_server`'s `handle_call` callback, except that it can return `{ok, Reply, NewState}`, `{ok, Reply, NewState, hibernate}`, `{remove_handler, Reply}`, or `{swap_handler, Reply, Args1, NewState, Handler2, Args2}`. The `gen_event:call/3-4` function is used to make the call" (Ch. 16, "The handle_call Function").

## Prerequisites

- **gen_event** — `handle_call/2` is a `gen_event` callback.
- **Event handler** — The call targets a specific handler.

## Key Properties

1. Invoked by `gen_event:call(Manager, HandlerId, Request)`.
2. Returns `{ok, Reply, NewState}`, `{ok, Reply, NewState, hibernate}`, `{remove_handler, Reply}`, or `{swap_handler, Reply, Args1, NewState, Handler2, Args2}`.
3. Because a manager may host many handlers, a call must target exactly *one* handler — you cannot fan a call out to all of them.
4. The targeted handler is named by its `HandlerId` (the module name, or `{Module, Ref}`).

## Construction / Recognition

## To Query a Handler Synchronously

1. Implement `handle_call(Request, State)` in the handler, returning an `{ok, Reply, NewState}` tuple.
2. Call it with `gen_event:call(ManagerPid, HandlerId, Request)`.
3. Use a `{Module, Ref}` `HandlerId` if multiple instances of the module are attached.

## Context & Application

In the curling example, `curling_accumulator` keeps the running game state and answers a `game_data` query: `handle_call(game_data, S=#state{teams=T, round=R}) -> {ok, {orddict:to_list(T), {round, R}}, S}.` The `curling` module wraps this as `game_info(Pid) -> gen_event:call(Pid, curling_accumulator, game_data).` — using the bare module name as the handler id because only one accumulator is attached.

## Examples

**Example 1** (Ch. 16): `curling_accumulator`'s `handle_call(game_data, S) -> {ok, {orddict:to_list(T), {round, R}}, S}.`

**Example 2** (Ch. 16): `game_info(Pid) -> gen_event:call(Pid, curling_accumulator, game_data).`

## Relationships

## Builds Upon

- **gen_event** — Provides the synchronous-query callback.

## Related

- **event-handler** — The call targets a specific handler.
- **event-manager** — `gen_event:call/3` routes the request through the manager.

## Common Errors

- **Error**: Expecting `gen_event:call/3` to query all handlers at once.
  **Correction**: A call targets exactly one handler; "we'll be forced to choose only one handler to reply to us."

## Common Confusions

- **Confusion**: Thinking `handle_call/2` works like `handle_event/2`.
  **Clarification**: `handle_event/2` is asynchronous and reaches every handler; `handle_call/2` is synchronous and targets a single, named handler.

## Source Reference

Chapter 16: "Event Handlers," section "The handle_call Function"; usage in "Alert the Press!" (the `curling_accumulator` handler).

## Verification Notes

- Definition: Direct quote from "The handle_call Function."
- Key Properties: Return values copied from the source's list.
- Confidence: HIGH — explicitly defined with code.
