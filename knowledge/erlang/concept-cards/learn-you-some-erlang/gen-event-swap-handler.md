---
concept: gen_event Swap Handler
slug: gen-event-swap-handler
category: otp-behaviours
subcategory: event-handling
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "The handle_event Function"
extraction_confidence: medium
aliases:
  - "swap_handler"
  - handler swapping
  - "remove_handler"
prerequisites:
  - event-handler
  - gen-event
extends: []
related:
  - event-handler
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# gen_event Swap Handler

## Quick Definition

`swap_handler` and `remove_handler` are `gen_event` callback return values that, respectively, replace the current handler with a new one or drop it from the manager.

## Core Definition

A `handle_event/2` callback may return `remove_handler` or `{swap_handler, Args1, NewState, NewHandler, Args2}`. "`remove_handler` drops the handler from the manager." For `swap_handler`, "the manager first call[s] `CurrentHandler:terminate(Args1, NewState)` and removing the current handler, and then adding a new one by calling `NewHandler:init(Args2, ResultFromTerminate)`" (Ch. 16, "The handle_event Function").

## Prerequisites

- **Event handler** — Swapping/removing operate on handlers.
- **gen_event** — These are `gen_event` callback return values.

## Key Properties

1. `remove_handler` — drops the current handler; useful when a handler knows it is finished.
2. `{swap_handler, Args1, NewState, NewHandler, Args2}` — replaces the handler with another.
3. On swap, the manager calls `OldHandler:terminate(Args1, NewState)` then `NewHandler:init(Args2, ResultFromTerminate)`.
4. The new handler's `init` receives the old handler's `terminate` result, so state can be carried over.
5. `handle_call/2` has an analogous `{remove_handler, Reply}` / `{swap_handler, Reply, ...}` return.
6. Swapping "is not used too frequently" — apply it when you know a specific event should hand control to a different handler.

## Construction / Recognition

## To Swap or Remove a Handler

1. To finish a handler: return `remove_handler` from its callback.
2. To hand off to another: return `{swap_handler, Args1, NewState, NewHandler, Args2}`.
3. Have the new handler's `init/1` accept the value the old handler's `terminate/2` returns.

## Context & Application

The book describes swapping as something "you'll simply know when you need it and apply it then" — a way to give control to a new handler when a specific event has occurred. It is the less-common cousin of plain `add_handler`/`delete_handler` management.

## Examples

**Example 1** (Ch. 16): A `handle_event/2` clause returns `remove_handler` when its handler "knows it's finished and it has nothing else to do."

**Example 2** (Ch. 16): A `handle_event/2` returns `{swap_handler, Args1, NewState, NewHandler, Args2}`, prompting the manager to terminate the old handler and init the new one.

## Relationships

## Builds Upon

- **Event handler** — Swapping/removing change which handlers are attached.

## Related

- **gen-event** — Provides the callback return values.

## Common Errors

- **Error**: Writing a `NewHandler:init/1` that ignores the value from the old handler's `terminate`.
  **Correction**: `swap_handler`'s purpose is state carry-over; accept and use the `terminate` result in the new `init`.

## Common Confusions

- **Confusion**: Thinking `swap_handler` runs `init/1` (arity 1).
  **Clarification**: On a swap the manager calls the new handler's init with the old handler's terminate result as an extra argument.

## Source Reference

Chapter 16: "Event Handlers," section "The handle_event Function" (and "The handle_call Function" for the analogous returns).

## Verification Notes

- Definition: Direct quotes from "The handle_event Function."
- Key Properties: Adapted from the callback-return discussion.
- Confidence: MEDIUM — described but, as the book itself notes, "not used too frequently"; no full worked example is given.
