---
concept: Event Handler Identifier
slug: handler-id
category: otp-behaviours
subcategory: event-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Event Handlers"
chapter_number: 16
pdf_page: null
section: "Game Events"
extraction_confidence: high
aliases:
  - "HandlerId"
  - handler identifier
  - "{Module, Ref}"
prerequisites:
  - event-handler
  - event-manager
extends: []
related:
  - event-handler
contrasts_with: []
answers_questions:
  - "What is the gen_event behaviour?"
---

# Event Handler Identifier

## Quick Definition

A handler identifier is the value used to address a specific event handler instance in a manager. It is either the bare module name or a `{Module, Ref}` tuple for uniqueness.

## Core Definition

"If you want to call, add, or delete a specific handler when there's more than one instance of it, you'll need to find a way to uniquely identify it. My favorite way of doing this ... is to just use `make_ref()` as a unique value. ... you add it by calling `add_handler/3` as `gen_event:add_handler(Pid, {Module, Ref}, Args)`. From this point on, you can use `{Module, Ref}` to talk to that specific handler" (Ch. 16, "Game Events").

## Prerequisites

- **Event handler** — Handler ids name specific handlers.
- **Event manager** — Handlers are addressed within a manager.

## Key Properties

1. The bare `Module` works as an id when only one instance of the module is attached.
2. With multiple instances of one module, the manager picks one "in an undefined manner."
3. `{Module, Ref}` (with `Ref` from `make_ref()`) gives each instance a unique id.
4. The same id is used by `add_handler/3`, `delete_handler/3`, and `call/3`.
5. The id chosen at `add_handler` time must be reused to address that handler later.

## Construction / Recognition

## To Identify a Handler

1. Single instance → use the bare module name as the id.
2. Multiple instances → attach with `{Module, make_ref()}` and keep the tuple.
3. Use the same id for later `delete_handler/3` or `call/3` calls.

## Context & Application

The curling press feed uses `{curling_feed, make_ref()}` so each reporter's subscription is individually removable: `join_feed/2` returns the `HandlerId`, and `leave_feed/2` deletes exactly that one. The book's vivid framing: a unique id "makes sure that some guy from the *Head-Smashed-In Buffalo Jump* press leaving the place won't disconnect a journalist from *The Economist*." By contrast, `game_info/1` uses the bare `curling_accumulator` id because only one accumulator exists.

## Examples

**Example 1** (Ch. 16): `HandlerId = {curling_feed, make_ref()}` — a unique id for one press subscriber.

**Example 2** (Ch. 16): `gen_event:call(Pid, curling_accumulator, game_data)` uses the bare module name as the id.

## Relationships

## Builds Upon

- **Event handler** — Handler ids name handler instances.

## Related

- **event-manager** — Handlers are added/removed/queried within a manager by id.

## Common Errors

- **Error**: Attaching several instances of one module under the bare module name, then trying to delete a specific one.
  **Correction**: Use `{Module, make_ref()}` ids so each instance is uniquely addressable.

## Common Confusions

- **Confusion**: Thinking the bare module name always uniquely identifies a handler.
  **Clarification**: It does only when a single instance is attached; with multiple instances the manager picks one arbitrarily.

## Source Reference

Chapter 16: "Event Handlers," sections "Game Events" and "Alert the Press!".

## Verification Notes

- Definition: Direct quote from "Game Events."
- Key Properties: Synthesised from the `{Module, Ref}` discussion.
- Confidence: HIGH — explicitly described with code.
