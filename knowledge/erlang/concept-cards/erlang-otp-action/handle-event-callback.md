---
# === CORE IDENTIFICATION ===
concept: handle_event/2 Callback
slug: handle-event-callback

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
section: "7.2.3 Acting on error events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "handle_event/2"
  - "gen_event event callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-handler
extends: []
related:
  - error-logger-events
  - event-stream-notify
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the handle_event/2 callback do?"
  - "What does handle_event/2 return?"
---

# Quick Definition

`handle_event/2` is the `gen_event` callback invoked for every event posted to the event manager; it receives the event and the handler state and returns `{ok, NewState}` (or `remove_handler`).

# Core Definition

`handle_event/2` is the `gen_event` callback function that takes the place of `gen_server`'s `handle_cast/2`. It is the function where a handler receives events posted to its event manager. It is called with two arguments — the event term and the handler's current state — and normally returns `{ok, State}` to continue. A handler defines one `handle_event/2` clause per event shape it cares about, plus a final catch-all clause for system messages and unrecognized events. Because a `gen_event` callback cannot stop the manager, when a handler wants to detach it returns `remove_handler` instead, which causes the manager to remove it and call its `terminate` callback (Ch. 7, Sections 7.2.1 and 7.2.3).

# Prerequisites

- **gen_event** — `handle_event/2` is a callback of the `gen_event` behaviour.
- **event-handler** — The callback lives inside an event handler module.

# Key Properties

1. Replaces `gen_server`'s `handle_cast/2` in the `gen_event` interface.
2. Receives the event term and the handler state.
3. Normally returns `{ok, NewState}`.
4. Can return `remove_handler` to detach the handler.
5. Typically has multiple pattern-matching clauses plus a catch-all.

# Construction / Recognition

## To Implement handle_event/2:
1. Write one clause per event tuple shape you want to act on.
2. In each clause, perform the desired action and return `{ok, State}`.
3. Add a final `handle_event(_Event, State) -> {ok, State}` catch-all.

## To Recognize:
1. A function named `handle_event/2` in a `gen_event` module.

# Context & Application

- **Typical contexts**: Logging handlers and custom event-stream subscribers.
- **Common applications**: Reformatting and printing log events; forwarding events to other systems.
- **Historical/stylistic notes**: System messages may arrive that match none of the explicit clauses — hence the catch-all.

# Examples

**Example 1** (Section 7.2.3, Listing 7.4): A `handle_event/2` clause matches `{error, _Gleader, {Pid, Format, Data}}`, calls `io:fwrite` to print an `ERROR` line, and returns `{ok, State}`; a final `handle_event(_Event, State) -> {ok, State}` clause catches everything else.

# Relationships

## Builds Upon
- **gen_event** — The behaviour defining the callback.
- **event-handler** — The module containing `handle_event/2`.

## Enables
- None.

## Related
- **error-logger-events** — The event tuples matched in `handle_event/2` clauses.
- **event-stream-notify** — Events posted via `notify/2` arrive at `handle_event/2`.

## Contrasts With
- None.

# Common Errors

- **Error**: Forgetting the catch-all clause, causing a function-clause crash on an unmatched system message.
  **Correction**: Always end with a clause matching any event and returning `{ok, State}`.

# Common Confusions

- **Confusion**: Expecting to return a `stop` tuple as in `gen_server`.
  **Clarification**: Return `remove_handler` to detach; the manager itself cannot be stopped from a handler callback.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Sections 7.2.1 and 7.2.3 "Acting on error events," Listing 7.4.

# Verification Notes

- Definition source: Directly adapted from Sections 7.2.1 and 7.2.3.
- Confidence rationale: HIGH — the book shows the callback's signature, return values, and a full listing.
- Uncertainties: None.
- Cross-reference status: Verified.
