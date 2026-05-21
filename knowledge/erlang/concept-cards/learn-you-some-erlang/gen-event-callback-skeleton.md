---
concept: gen_event Callback Skeleton
slug: gen-event-callback-skeleton
category: otp-behaviours
subcategory: event-handling
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "Game Events"
extraction_confidence: high
aliases:
  - event-handler skeleton
  - "gen_event skeleton"
prerequisites:
  - gen-event
  - event-handler
extends: []
related:
  - event-handler
  - gen-event-handle-call
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
  - "How does a behaviour relate to its callback module?"
---

# gen_event Callback Skeleton

## Quick Definition

The `gen_event` callback skeleton is a minimal handler module with the six required callbacks stubbed out, a reusable starting point for any `gen_event` handler.

## Core Definition

The book presents a skeleton "that we can use for every `gen_event` callback module out there" (Ch. 16, "Game Events"):

```erlang
-module(gen_event_callback).
-behavior(gen_event).
-export([init/1, handle_event/2, handle_call/2, handle_info/2,
         code_change/3, terminate/2]).

init([]) -> {ok, []}.
handle_event(_, State) -> {ok, State}.
handle_call(_, State) -> {ok, ok, State}.
handle_info(_, State) -> {ok, State}.
code_change(_OldVsn, State, _Extra) -> {ok, State}.
terminate(_Reason, _State) -> ok.
```

## Prerequisites

- **gen_event** — The skeleton implements the `gen_event` behaviour.
- **Event handler** — The skeleton is the bare form of a handler module.

## Key Properties

1. Declares `-behavior(gen_event).` and exports the six callbacks.
2. `init/1` returns `{ok, State}` (here `{ok, []}`).
3. `handle_event/2` returns `{ok, State}` — does nothing, updates nothing.
4. `handle_call/2` returns `{ok, ok, State}` — replies `ok`, changes nothing.
5. `handle_info/2` returns `{ok, State}`.
6. `code_change/3` returns `{ok, State}`; `terminate/2` returns `ok`.
7. You then fill in only the callbacks your handler actually needs.

## Construction / Recognition

## To Use the Skeleton

1. Copy the six-callback skeleton into a new module.
2. Rename the module and add `-behavior(gen_event).`
3. Replace the `init/1` body with your real initial state.
4. Add real clauses to `handle_event/2` (and `handle_call/2` if needed).
5. Leave the unused callbacks as trivial stubs.

## Context & Application

The book uses this skeleton to derive `curling_scoreboard` (fills in `handle_event/2`), `curling_feed` (fills in `init/1` and `handle_event/2`), and `curling_accumulator` (fills in `init/1`, `handle_event/2`, `handle_call/2`). It is the practical answer to "where do I start" for a `gen_event` handler.

## Examples

**Example 1** (Ch. 16): `curling_scoreboard` is the skeleton with `handle_event/2` filled in to forward `{set_teams, ...}`, `{add_points, ...}`, and `next_round` events.

**Example 2** (Ch. 16): `curling_feed` is the skeleton with `init([Pid]) -> {ok, Pid}` and a `handle_event` that forwards events to `Pid`.

## Relationships

## Builds Upon

- **gen_event** — The behaviour the skeleton declares.

## Related

- **event-handler** — The skeleton is the starting form of a handler.
- **gen-event-handle-call** — The `handle_call/2` stub becomes a real query handler when filled in.

## Common Errors

- **Error**: Forgetting to export one of the six callbacks.
  **Correction**: All six must be exported; the behaviour requires them even if some stay stubs.

## Common Confusions

- **Confusion**: Thinking every callback must do real work.
  **Clarification**: Unused callbacks are fine left as trivial `{ok, State}` stubs; you fill in only what your handler needs.

## Source Reference

Chapter 16: "Event Handlers," section "Game Events" (the `gen_event_callback` skeleton).

## Verification Notes

- Definition: Skeleton copied directly from the source.
- Key Properties: Adapted from the skeleton and the curling handlers derived from it.
- Confidence: HIGH — the skeleton is given verbatim.
