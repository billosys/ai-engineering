---
# === CORE IDENTIFICATION ===
concept: gen_event (Generic Event Handling)
slug: gen-event

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "Generic Event Handling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event"
  - "generic event handler"
  - "event handler"
  - "-behaviour(gen_event)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - callback-module
  - message-passing
extends: []
related:
  - error-logger
  - alarm-management
  - gen-server
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_event?"
  - "How does Erlang decouple generating an event from processing it?"
---

# Quick Definition

`gen_event` is the OTP behaviour for generic event handling. It provides a named place to send events and lets you install (and swap) custom handler callbacks that decide how each event is processed.

# Core Definition

An *event* "is just something that happens — something noteworthy that the programmer thinks somebody should do something about" (Programming Erlang, "Generic Event Handling"). An *event handler* is the process that receives event messages. The book builds a simple `event_handler` by hand — `make(Name)` creates a "do nothing" handler, `event(Name, X)` sends an event, `add_handler(Name, Fun)` installs a handler function — and then explains that the real OTP `gen_event` behaviour follows this pattern. The key idea: "the event handler provides an infrastructure where we can install custom handlers," decoupling event generation from event processing. "This is not 'late binding' — it's 'very late binding, and you can change your mind later.'" The error logger and the alarm handler are both built on `gen_event`.

# Prerequisites

- **Behaviour** — `gen_event` is an OTP behaviour, declared with `-behaviour(gen_event)`.
- **Callback module** — handlers are supplied as callback modules / functions.
- **Message passing** — events are delivered to the handler as messages.

# Key Properties

1. Decouples event *generation* from event *processing*.
2. An event is any Erlang term sent as `{event, E}` to a registered process.
3. Custom handlers can be installed and swapped at any time without stopping the system.
4. The `gen_event` callback module exports `init/1`, `handle_event/2`, `handle_call/2`, `handle_info/2`, `terminate/2`, `code_change/3`.
5. `handle_event(Event, State)` returns `{ok, NewState}`.
6. The error logger and alarm handler infrastructures both follow the event-handler pattern.

# Construction / Recognition

## To Construct a gen_event Handler:
1. Write a callback module with `-behaviour(gen_event).`.
2. Implement `init/1` returning `{ok, State}`.
3. Implement `handle_event(Event, State)` clauses, each returning `{ok, NewState}`.
4. Install it into a running event manager (e.g. via `gen_event:swap_handler/3`).

## To Recognize:
1. A module with `-behaviour(gen_event).` and a `handle_event/2` function is a gen_event callback.

# Context & Application

- **Typical contexts**: Logging, alarm management, monitoring — anywhere event generation must be decoupled from processing.
- **Common applications**: `my_alarm_handler` is a gen_event callback; the OTP `error_logger` and `alarm_handler` are gen_event-based.
- **Historical/stylistic notes**: The book uses the hand-written `event_handler` to motivate the "very late binding" idea before introducing the real `gen_event`.

# Examples

**Example 1** ("Generic Event Handling"): The hand-written generic event handler's loop installs and runs handler functions:

```erlang
my_handler(Fun) ->
    receive
        {add, Fun1} -> my_handler(Fun1);
        {event, Any} -> (catch Fun(Any)), my_handler(Fun)
    end.
```

**Example 2** ("Alarm Management"): `my_alarm_handler` is a `gen_event` callback whose `handle_event/2` reacts to `{set_alarm, tooHot}` and `{clear_alarm, tooHot}`, returning `{ok, NewState}`.

# Relationships

## Builds Upon
- **Behaviour** — `gen_event` is one of the OTP behaviours.

## Enables
- **Error logger** — the error logger infrastructure follows the gen_event pattern.
- **Alarm management** — the OTP alarm handler is a gen_event callback module.

## Related
- **gen_server** — another OTP behaviour with a similar callback structure.

## Contrasts With
- **gen_server** — `gen_server` models a single client/server; `gen_event` models a manager into which many handlers can be plugged and swapped.

# Common Errors

- **Error**: Statically linking event-processing code to event-generating code.
  **Correction**: Use gen_event so processing can be changed by installing a new handler without stopping the system.

- **Error**: Returning the wrong tuple from `handle_event/2`.
  **Correction**: `handle_event/2` must return `{ok, NewState}`.

# Common Confusions

- **Confusion**: Thinking installing a handler is ordinary late binding.
  **Clarification**: The book stresses it is "very late binding" — the handler can be replaced at runtime, even after events have started flowing.

- **Confusion**: Believing an event handler must do something with every event.
  **Clarification**: The default ("do nothing") handler simply discards events; processing is only added when a handler is installed.

# Source Reference

Chapter 23: Making a System with OTP, section "Generic Event Handling"; also referenced in "Alarm Management" and "Digging Deeper". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "Generic Event Handling".
- Confidence rationale: HIGH — events and event handlers are explicitly defined; gen_event is named as the OTP behaviour following the pattern.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
