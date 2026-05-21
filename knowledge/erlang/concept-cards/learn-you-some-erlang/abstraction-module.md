---
concept: Abstraction Module
slug: abstraction-module
category: otp-behaviours
subcategory: design
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
  - interface module
  - wrapper module
  - API module
prerequisites:
  - otp-behaviour
extends: []
related:
  - fsm-public-api
  - event-manager
contrasts_with: []
answers_questions:
  - "How does a behaviour relate to its callback module?"
---

# Abstraction Module

## Quick Definition

An abstraction module is a module that wraps the raw OTP behaviour calls (`gen_event`, `gen_server`, `gen_fsm`) behind named, friendly functions, hiding the protocol from callers.

## Core Definition

The book observes that calling a behaviour's module directly forces you to "show everyone what our protocol looks like. A better option would be to provide an *abstraction module* on top of it that just wraps up all the calls we need" (Ch. 16, "Game Events").

## Prerequisites

- **OTP behaviour** — Abstraction modules wrap behaviour calls.

## Key Properties

1. It wraps raw `gen_*` calls in named functions.
2. It makes the code "look a lot nicer to everyone using our code."
3. It lets the implementation change without breaking callers.
4. It reduces the chance of writing protocol messages incorrectly.
5. It can also encode which handlers/components are required for a standard setup.

## Construction / Recognition

## To Write an Abstraction Module

1. List the operations callers need.
2. Write one named function per operation, wrapping the appropriate `gen_*` call.
3. Optionally, have a `start_link` that wires up required handlers/children.
4. Export only the friendly functions; keep the protocol internal.

## Context & Application

The `curling` module is the book's example: it exports `start_link/2`, `set_teams/3`, `add_points/3`, `next_round/1`, `join_feed/2`, `leave_feed/2`, and `game_info/1`, each wrapping a `gen_event` call. Its `start_link/2` also attaches the `curling_scoreboard` and `curling_accumulator` handlers automatically — encoding the "standard curling game" setup. The same idea appears as the FSM public API in `trade_fsm`.

## Examples

**Example 1** (Ch. 16): `curling:add_points(Pid, Team, N) -> gen_event:notify(Pid, {add_points, Team, N}).` — a wrapper hiding the `gen_event` protocol.

**Example 2** (Ch. 16): `curling:start_link/2` attaches the required handlers, so callers do not have to know which handlers a game needs.

## Relationships

## Builds Upon

- **OTP behaviour** — The abstraction module sits on top of a behaviour.

## Related

- **fsm-public-api** — The FSM-specific instance of this pattern.
- **event-manager** — Often the thing being abstracted.

## Common Errors

- **Error**: Letting callers invoke `gen_event`/`gen_server` functions directly across the codebase.
  **Correction**: Provide an abstraction module so the protocol is centralized and changeable.

## Common Confusions

- **Confusion**: Thinking an abstraction module adds no value because it just forwards calls.
  **Clarification**: It makes code readable, prevents malformed protocol messages, and decouples callers from the implementation — real value beyond mere forwarding.

## Source Reference

Chapter 16: "Event Handlers," section "Game Events" (the `curling` module); the same pattern as `trade_fsm`'s public API in Chapter 15.

## Verification Notes

- Definition: Direct quote from "Game Events."
- Key Properties: Synthesised from the `curling` module discussion.
- Confidence: HIGH — explicitly named and exemplified.
