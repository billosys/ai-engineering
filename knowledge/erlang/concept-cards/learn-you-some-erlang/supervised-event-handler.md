---
concept: Supervised Event Handler
slug: supervised-event-handler
category: otp-behaviours
subcategory: event-handling
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "Alert the Press!"
extraction_confidence: high
aliases:
  - "add_sup_handler"
  - "gen_event:add_sup_handler/3"
  - supervised handler
prerequisites:
  - event-handler
  - event-manager
extends:
  - event-handler
related:
  - event-handler
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# Supervised Event Handler

## Quick Definition

A supervised event handler is one attached with `gen_event:add_sup_handler/3`, which links the caller to the manager so each side learns when the other fails — at the cost of a known backward-compatibility wart.

## Core Definition

"All that needs to be done is to change the call from `gen_event:add_handler/3` to `gen_event:add_sup_handler/3`. If we crash, the handler is gone. Then on the opposite end, if the `gen_event` manager crashes, the message `{gen_event_EXIT, Handler, Reason}` is sent back to us" (Ch. 16, "Alert the Press!").

## Prerequisites

- **Event handler** — A supervised handler is a handler attached differently.
- **Event manager** — The supervision link is between the caller and the manager.

## Key Properties

1. Attached with `gen_event:add_sup_handler/3` instead of `add_handler/3`.
2. A link is set up between the calling process and the event manager.
3. If the caller crashes, its supervised handler is terminated (`terminate({stop, Reason}, State)`).
4. If the handler itself crashes, the caller receives `{gen_event_EXIT, HandlerId, Reason}`.
5. **Wart:** `gen_event` predates monitors and never unlinks; when the manager shuts down, the caller gets `{gen_event_EXIT, ...}` and *then* either crashes (not trapping exits) or gets a confusing extra `'EXIT'` message.

## Construction / Recognition

## To Use a Supervised Handler

1. Attach the handler with `gen_event:add_sup_handler(ManagerPid, HandlerId, Args)`.
2. Be prepared to handle `{gen_event_EXIT, HandlerId, Reason}` messages.
3. Decide whether to trap exits, given the manager-shutdown wart.

## Context & Application

The book introduces supervised handlers to solve a real problem in the curling press feed: "What if one of the curling feed subscribers crashes? Do we just keep the handler going on there?" `add_sup_handler/3` cleans that up. But the book warns it is "a bit like" an over-attentive family scolding a child — because `gen_event` "predates the appearance of monitors" and keeps the link alive, the manager-shutdown case is messy. The verdict: "It will be safer, even if it risks being more annoying in some cases. Safety first."

## Examples

**Example 1** (Ch. 16): Switching `gen_event:add_handler/3` to `gen_event:add_sup_handler/3` so a crashing curling-feed subscriber's handler is removed automatically.

**Example 2** (Ch. 16): On manager shutdown, the caller receives `{gen_event_EXIT, Handler, Reason}` followed by a superfluous `'EXIT'` message.

## Relationships

## Builds Upon

- **Event handler** — A supervised handler is an ordinary handler attached with supervision.

## Related

- **event-manager** — The supervision link binds the caller to the manager.

## Common Errors

- **Error**: Using `add_sup_handler/3` without handling `{gen_event_EXIT, ...}` messages.
  **Correction**: Match and handle that message; otherwise the caller may crash unexpectedly.

## Common Confusions

- **Confusion**: Expecting `add_sup_handler/3` to use monitors and behave cleanly.
  **Clarification**: `gen_event` predates monitors; it uses links and does not unlink, producing the documented manager-shutdown wart.

## Source Reference

Chapter 16: "Event Handlers," section "Alert the Press!" and the sidebar "Don't Drink Too Much Kool-Aid."

## Verification Notes

- Definition: Direct quotes from "Alert the Press!".
- Key Properties: Synthesised from the section and the wart sidebar.
- Confidence: HIGH — explicitly defined, wart and all.
