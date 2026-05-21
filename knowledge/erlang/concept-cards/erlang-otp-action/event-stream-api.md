---
# === CORE IDENTIFICATION ===
concept: Event Stream API Module
slug: event-stream-api

# === CLASSIFICATION ===
category: api-design
subcategory: event-handling
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.3.1 The event stream API"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sc_event module"
  - "event API module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - custom-event-stream
  - event-manager
extends: []
related:
  - event-stream-notify
  - event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event stream API module?"
  - "Why wrap gen_event registration functions in an API module?"
  - "What functions belong in a custom event stream's API?"
---

# Quick Definition

An event stream API module is the module that fronts a custom `gen_event` event stream — providing `start_link`, handler-registration wrappers, and event-posting functions — so callers never deal with the `gen_event` machinery directly.

# Core Definition

An event stream API module encapsulates the implementation details of a custom event stream and exposes a small set of easy-to-use functions. In the book's Simple Cache, the `sc_event` module is this API module (Listing 7.5). It does not itself implement an OTP behaviour, but it provides: a `start_link()` function that hides a call to `gen_event:start_link/1` (starting and locally registering the event manager); wrapper functions around `gen_event:add_handler/3` and `delete_handler/3` so subscribers need not know the manager's registered name; and event-posting functions (`lookup/1`, `create/2`, `replace/2`, `delete/1`) that wrap `gen_event:notify/2`. The protocol of event tuples it posts must be understood by every subscriber callback module and so should be documented (Ch. 7, Section 7.3.1).

# Prerequisites

- **custom-event-stream** — The API module is the front of a custom event stream.
- **event-manager** — The module wraps starting and addressing a `gen_event` event manager.

# Key Properties

1. Fronts a custom `gen_event` event stream; does not itself implement a behaviour.
2. Provides a `start_link()` that hides `gen_event:start_link/1`.
3. Wraps `add_handler`/`delete_handler` so callers don't need the manager's name.
4. Provides event-posting functions wrapping `gen_event:notify/2`.
5. Defines the event protocol — the set of event tuples — in one place.

# Construction / Recognition

## To Build an Event Stream API Module:
1. Write `start_link()` calling `gen_event:start_link({local, ?MODULE})`.
2. Add `add_handler/2` and `delete_handler/2` wrappers over the `gen_event` functions.
3. Add one posting function per event type, each calling `gen_event:notify/2`.
4. Keep all event-protocol tuple shapes confined to this module.

## To Recognize:
1. A module with `start_link` plus `add_handler`/`delete_handler` wrappers and named event-posting functions, but no `-behaviour` declaration.

# Context & Application

- **Typical contexts**: Any application exposing a custom event stream.
- **Common applications**: The `sc_event` module of the Simple Cache.
- **Historical/stylistic notes**: Like a server API, the wrappers hide the protocol; but for events the encapsulation is incomplete, since subscriber handlers must also know the protocol.

# Examples

**Example 1** (Section 7.3.1, Listing 7.5): `sc_event` provides `start_link()` (wrapping `gen_event:start_link/1`), `add_handler`/`delete_handler` wrappers, and the four event-posting functions.

**Example 2** (Section 7.3.1, Table 7.2): The protocol the module posts: `{lookup, Key}` from `sc_event:lookup/1`, `{create, {Key, Value}}` from `sc_event:create/2`, `{replace, {Key, Value}}` from `sc_event:replace/2`, `{delete, Key}` from `sc_event:delete/1`.

# Relationships

## Builds Upon
- **custom-event-stream** — The API module realizes a custom event stream.
- **event-manager** — It starts and addresses the manager.

## Enables
- **event-stream-notify** — The module's posting functions wrap `notify/2`.

## Related
- **event-handler** — Subscribers register via the module's wrapper functions.

## Contrasts With
- None.

# Common Errors

- **Error**: Letting callers call `gen_event:notify` or `add_handler` directly.
  **Correction**: Route everything through the API module so the manager name and protocol stay encapsulated.

# Common Confusions

- **Confusion**: Expecting the API module to be a `gen_event` callback module.
  **Clarification**: It is a plain module that fronts the stream; the callback modules are the separate subscriber handlers.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.3.1 "The event stream API," Listing 7.5 and Table 7.2.

# Verification Notes

- Definition source: Directly adapted from Section 7.3.1.
- Confidence rationale: HIGH — the book presents the module and its design rationale explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
