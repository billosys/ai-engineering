---
# === CORE IDENTIFICATION ===
concept: Custom Event Stream
slug: custom-event-stream

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.3 Adding a custom event stream to the Simple Cache"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application-level event stream"
  - "application-specific event stream"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
  - event-handler
extends: []
related:
  - event-stream-api
  - event-stream-notify
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a custom event stream?"
  - "Why would an application publish its own event stream?"
  - "How is a custom event stream built with gen_event?"
---

# Quick Definition

A custom event stream is an application-specific `gen_event`-based notification channel — separate from the error logger — through which an application publishes its own events so users can subscribe with their own handlers.

# Core Definition

A custom event stream is an application-level event stream that an application creates with the `gen_event` behaviour, separate from the system error logger. The application starts its own event manager, defines a protocol of event tuples it will post, instruments its code to post those events at points of interest, and exposes an API so consumers can subscribe with their own handlers. For the Simple Cache, the book builds such a stream to publish events about insertion, deletion, lease timeouts, and lookups — letting users answer questions like "How many lookups did the cache have in the last hour?" The event manager is hooked into the application's supervision structure so it starts and stops with the application (Ch. 7, Section 7.3).

# Prerequisites

- **gen_event** — A custom event stream is built on the `gen_event` behaviour.
- **event-manager** — The stream is realized as a `gen_event` event manager.
- **event-handler** — Consumers subscribe by adding handlers to the stream.

# Key Properties

1. An application-specific event channel, separate from the error logger.
2. Built on a dedicated `gen_event` event manager.
3. Defines its own protocol of event tuples.
4. Exposes an API for posting events and for subscribing handlers.
5. The event manager is supervised so it starts/stops with the application.
6. Lets external code hook into the application without knowing its internals.

# Construction / Recognition

## To Create a Custom Event Stream:
1. Write an API module that starts a `gen_event` manager (e.g., `sc_event`).
2. Define the event protocol — the set of event tuples to post.
3. Add the event manager to the application's supervision tree.
4. Instrument the application code to post events at key points.
5. Provide wrapper functions for adding/removing subscriber handlers.

## To Recognize:
1. An application module that wraps `gen_event:start_link`, `add_handler`, and `notify` for its own event protocol.

# Context & Application

- **Typical contexts**: Applications that want to expose observability or extension points.
- **Common applications**: Statistics gathering, monitoring, letting other applications react to events.
- **Historical/stylistic notes**: Encapsulation is less complete than for a server — the protocol must be understood by every subscriber handler, so it should be documented.

# Examples

**Example 1** (Section 7.3): The Simple Cache custom event stream publishes `{lookup, Key}`, `{create, {Key, Value}}`, `{replace, {Key, Value}}`, and `{delete, Key}` events.

**Example 2** (Section 7.3.2): The `sc_event` event manager is added as a `worker` child of the new root supervisor `sc_sup`, so it starts and stops with the cache application.

# Relationships

## Builds Upon
- **gen_event** — The behaviour underlying the custom stream.
- **event-manager** — The stream's container process.
- **event-handler** — Subscribers attach handlers.

## Enables
- **event-stream-api** — The API module that fronts the custom stream.

## Related
- **event-stream-notify** — Events are posted into the stream with `notify/2`.
- **supervisor** — The stream's event manager is supervised.

## Contrasts With
- None.

# Common Errors

- **Error**: Letting the event protocol tuples leak into other parts of the code.
  **Correction**: Confine the protocol to the API module and the subscriber handlers; expose only API functions.

# Common Confusions

- **Confusion**: Thinking a custom event stream must reuse the error logger.
  **Clarification**: It is a separate `gen_event` manager; events can optionally be forwarded to the error logger by a handler.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.3 "Adding a custom event stream to the Simple Cache," subsections 7.3.1–7.3.3.

# Verification Notes

- Definition source: Synthesized from Section 7.3's introduction and design discussion.
- Confidence rationale: HIGH — the book devotes a full section to building one.
- Uncertainties: None.
- Cross-reference status: Verified.
