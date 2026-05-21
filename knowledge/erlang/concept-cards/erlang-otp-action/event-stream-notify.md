---
# === CORE IDENTIFICATION ===
concept: gen_event notify
slug: event-stream-notify

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
section: "7.3.1 The event stream API"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event:notify/2"
  - "notify/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
extends: []
related:
  - event-stream-api
  - handle-event-callback
  - gen-server-cast
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are events posted to a gen_event event manager?"
  - "What does gen_event:notify/2 do?"
---

# Quick Definition

`gen_event:notify/2` posts an event asynchronously to an event manager, which dispatches it to every registered handler's `handle_event/2`; it is the `gen_event` analogue of `gen_server:cast/2`.

# Core Definition

`gen_event:notify/2` is the `gen_event` function for posting events asynchronously to an event manager. It is analogous to `gen_server:cast/2` — being asynchronous, the caller continues immediately after posting. When an event is posted via `notify/2`, the event manager calls each currently registered handler's `handle_event/2` with the event. In a custom event stream, the event-posting API functions (such as `sc_event:lookup/1`) are wrappers around `gen_event:notify/2` (Ch. 7, Section 7.3.1).

# Prerequisites

- **gen_event** — `notify/2` is part of the `gen_event` API.
- **event-manager** — `notify/2` posts an event to an event manager.

# Key Properties

1. Posts an event asynchronously to an event manager.
2. The caller does not block waiting for handlers to process the event.
3. The manager dispatches the event to every registered handler's `handle_event/2`.
4. The `gen_event` analogue of `gen_server:cast/2`.

# Construction / Recognition

## To Post an Event:
1. Call `gen_event:notify(Manager, Event)` with the manager reference and the event term.
2. Typically wrap this in an API function so callers don't reference the manager directly.

## To Recognize:
1. A call to `gen_event:notify/2`, often inside an event stream API function.

# Context & Application

- **Typical contexts**: Instrumenting application code to publish events.
- **Common applications**: Posting cache events (`lookup`, `create`, `replace`, `delete`) onto a custom stream.
- **Historical/stylistic notes**: Because it is asynchronous, the publisher is decoupled from handler processing time.

# Examples

**Example 1** (Section 7.3.1): The four `sc_event` event handling API functions are wrappers around `gen_event:notify/2`, which posts events asynchronously, similar to `gen_server:cast/2`.

# Relationships

## Builds Upon
- **gen_event** — `notify/2` is a `gen_event` function.
- **event-manager** — The target of `notify/2`.

## Enables
- None.

## Related
- **event-stream-api** — API posting functions wrap `notify/2`.
- **handle-event-callback** — Events posted via `notify/2` arrive at `handle_event/2`.
- **gen-server-cast** — The asynchronous analogue in `gen_server`.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting `notify/2` to return a handler result.
  **Correction**: It is asynchronous and returns immediately; replies, if any, must be arranged separately.

# Common Confusions

- **Confusion**: Thinking `notify/2` calls one handler.
  **Clarification**: The manager dispatches the event to all registered handlers.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.3.1 "The event stream API."

# Verification Notes

- Definition source: Directly adapted from Section 7.3.1.
- Confidence rationale: HIGH — the book explicitly describes `notify/2` and its analogy to `cast/2`.
- Uncertainties: None.
- Cross-reference status: Verified; `gen-server-cast` is owned by Agent 2.
