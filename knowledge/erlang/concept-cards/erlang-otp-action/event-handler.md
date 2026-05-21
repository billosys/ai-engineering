---
# === CORE IDENTIFICATION ===
concept: Event Handler
slug: event-handler

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.2.2 Event handler example"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event handler"
  - "event handler module"
  - "logging plug-in"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
extends: []
related:
  - error-logger-events
  - error-logger
  - handle-event-callback
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a gen_event event handler?"
  - "How do I write a handler that plugs into the error logger?"
  - "How do I register and remove an event handler?"
---

# Quick Definition

An event handler is a callback module implementing the `gen_event` behaviour; it is added to an event manager and its `handle_event/2` function is called for every event the manager receives.

# Core Definition

An event handler is a `gen_event` behaviour implementation module that is dynamically added to an event manager. It implements the standard `gen_event` callbacks — `init`, `handle_event/2`, `handle_call`, `handle_info`, `code_change`, `terminate` — and acts on the events posted to the manager. To plug into the logging infrastructure, you write such a module and register it with the `error_logger` process via `gen_event:add_handler/3` (the `error_logger` module supplies a convenience wrapper, `add_report_handler/1`). A bare-bones handler simply receives events and returns `{ok, State}`; a useful one inspects the event tuple and does something with it, such as reformatting and printing it (Ch. 7, Sections 7.2.2 and 7.2.3).

# Prerequisites

- **gen_event** — An event handler is a `gen_event` callback module.
- **event-manager** — Handlers are registered with and called by an event manager.

# Key Properties

1. A `gen_event` behaviour implementation module.
2. Added to (and removed from) an event manager dynamically.
3. Its `handle_event/2` is invoked for every event posted to the manager.
4. Multiple handlers can coexist on one manager; each is called for each event.
5. Typically lacks its own `start_link` because of the one-to-many relationship.
6. Must include a catch-all `handle_event` clause for unrecognized system messages.

# Construction / Recognition

## To Create an Event Handler:
1. Write a module with `-behaviour(gen_event)` implementing the callbacks.
2. Implement `handle_event/2` clauses matching the event tuples of interest.
3. Add a final catch-all `handle_event(_Event, State) -> {ok, State}` clause.
4. Register it with `gen_event:add_handler/3` (or a wrapper like `register_with_logger()`).
5. Remove it with `gen_event:delete_handler/3` when no longer needed.

## To Recognize:
1. A module declaring `-behaviour(gen_event)` and defining `handle_event/2` is an event handler.

# Context & Application

- **Typical contexts**: Customizing log output; subscribing to custom event streams.
- **Common applications**: Reformatting `error_logger` events; funneling cache events to a statistics or monitoring system.
- **Historical/stylistic notes**: A handler can return `remove_handler` to unregister itself.

# Examples

**Example 1** (Section 7.2.2, Listing 7.3): `custom_error_report.erl` is a skeleton handler that just receives events; its API function `register_with_logger()` hooks it into the error-logger event stream.

**Example 2** (Section 7.3.3, Listing 7.7): `sc_event_logger.erl` is a handler for the custom cache event stream; it funnels each posted cache event to the error logger as an `error_logger` message.

# Relationships

## Builds Upon
- **gen_event** — The behaviour an event handler implements.
- **event-manager** — The container that calls the handler.

## Enables
- None.

## Related
- **error-logger-events** — The event tuples a logger handler matches against.
- **handle-event-callback** — The callback through which events reach the handler.

## Contrasts With
- None.

# Common Errors

- **Error**: Omitting the catch-all `handle_event` clause.
  **Correction**: Always include a last clause to handle system messages and unrecognized events.

# Common Confusions

- **Confusion**: Expecting one handler per event manager.
  **Clarification**: Many handlers can be registered on a single manager, each called for every event.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Sections 7.2.2 "Event handler example," 7.2.3 "Acting on error events," and 7.3.3 "Subscribing to a custom event stream." Listings 7.3, 7.4, 7.7.

# Verification Notes

- Definition source: Directly adapted from Sections 7.2.2 and 7.2.3.
- Confidence rationale: HIGH — the book defines the handler concept and shows full examples.
- Uncertainties: None.
- Cross-reference status: Verified.
