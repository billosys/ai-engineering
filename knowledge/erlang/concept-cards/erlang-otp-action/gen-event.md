---
# === CORE IDENTIFICATION ===
concept: gen_event Behaviour
slug: gen-event

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
section: "7.2.1 Introducing the gen_event behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event"
  - "event handling behaviour"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - gen-server
extends:
  - otp-behaviour
related:
  - event-manager
  - event-handler
  - error-logger
  - custom-event-stream
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the gen_event behaviour?"
  - "How does gen_event differ from gen_server?"
  - "What callbacks does a gen_event handler module implement?"
---

# Quick Definition

`gen_event` is the OTP behaviour for event handling: it provides an event manager process to which any number of handler callback modules can be added and removed dynamically, each receiving every posted event.

# Core Definition

`gen_event` is the Erlang/OTP behaviour that implements the event-handling framework underlying the logging system. Its interface is similar to `gen_server` — it has `init`, `code_change`, and `terminate` callbacks and requires `handle_call` and `handle_info` — but it replaces `handle_cast/2` with `handle_event/2`, which is where events are received. The crucial structural difference: a `gen_server` container is tied to a single callback module at startup, whereas a `gen_event` container (the *event manager*) starts with no callback module; one or several handlers may be added and removed dynamically afterward. When an event is posted, all currently registered handler modules are called individually to handle it (Ch. 7, Section 7.2.1).

# Prerequisites

- **OTP behaviour** — `gen_event` is one of the standard behaviours; understanding the behaviour pattern is needed first.
- **gen_server** — The `gen_event` interface is explicitly described by analogy to `gen_server`.

# Key Properties

1. Implements OTP event handling; the logging system is built on it.
2. The container process is called an *event manager*.
3. An event manager starts with no callback module — handlers are added dynamically.
4. Multiple handler modules can be registered with one event manager.
5. Callbacks: `init`, `handle_event/2`, `handle_call`, `handle_info`, `code_change`, `terminate`.
6. A handler callback cannot stop the manager; it can return `remove_handler` to remove itself.

# Construction / Recognition

## To Use gen_event:
1. Start an event manager with `gen_event:start_link/0,1` (often from a supervisor).
2. Write a handler module implementing the `gen_event` callbacks.
3. Register the handler with `gen_event:add_handler/3` (and remove with `delete_handler/3`).
4. Post events with `gen_event:notify/2`.

## To Recognize:
1. A `gen_event` handler module is identified by `handle_event/2` and the absence of a `handle_cast/2`.

# Context & Application

- **Typical contexts**: Logging, event streams, monitoring, any one-to-many notification.
- **Common applications**: Hooking custom handlers into `error_logger`; building application-specific event streams.
- **Historical/stylistic notes**: Callback modules rarely provide their own `start_link` because of the one-to-many relationship.

# Examples

**Example 1** (Section 7.2.1, Figure 7.1): A `gen_server` container is always tied to one callback module, while a `gen_event` container can have any number of callback modules added and removed dynamically.

**Example 2** (Section 7.2.2, Listing 7.3): `custom_error_report.erl` is a bare-bones `gen_event` handler for the error logger that receives events and returns `{ok, State}`.

# Relationships

## Builds Upon
- **OTP behaviour** — `gen_event` is a standard OTP behaviour.

## Enables
- **event-manager** — The `gen_event` container process.
- **event-handler** — The dynamically registered callback modules.
- **custom-event-stream** — Built by starting a `gen_event` manager and posting your own events.

## Related
- **error_logger** — The `error_logger` process is a `gen_event` event manager.

## Contrasts With
- **gen_server** — A `gen_server` has one fixed callback module; a `gen_event` manager has any number of dynamically managed handlers.

# Common Errors

- **Error**: Returning a `stop` value from a `gen_event` callback as you would in `gen_server`.
  **Correction**: A `gen_event` callback can't stop the manager; return `remove_handler` to remove itself instead.

- **Error**: Doing strange things to the process state in a handler.
  **Correction**: Other handlers share the manager; keep handler behaviour well-mannered.

# Common Confusions

- **Confusion**: Assuming `gen_event` works exactly like `gen_server` with renamed callbacks.
  **Clarification**: Arguments and return values differ subtly; check the documentation.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.2.1 "Introducing the gen_event behaviour," Figure 7.1, and Listing 7.3.

# Verification Notes

- Definition source: Directly adapted from Section 7.2.1.
- Confidence rationale: HIGH — the book explicitly introduces and defines the behaviour and contrasts it with `gen_server`.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
