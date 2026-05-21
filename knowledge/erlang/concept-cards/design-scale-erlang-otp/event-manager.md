---
# === CORE IDENTIFICATION ===
concept: Event Manager
slug: event-manager

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 166
section: "Generic Event Managers and Handlers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event manager"
  - event manager process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event
  - gen-server
extends: []
related:
  - event-handler
  - gen-event-behavior
  - notifying-events
contrasts_with:
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "What is a special process?"
---

# Quick Definition

An event manager is an Erlang process running the `gen_event` generic code that receives events and forwards them to a set of subscribed event handlers — uniquely, one manager can run zero or more handlers.

# Core Definition

"An *event manager* is an Erlang process that receives a specific type of event, which could be alarms, warnings, equipment state changes, debug traces, or issues related to network connectivity" (Cesarini & Vinoski, p. 166). The process runs the generic `gen_event` library code (p. 167). "Unlike other behaviors, which allow only one callback module per instance, an event manager can take care of zero or more event handlers ... But despite the possibility of there being multiple handlers, they will all be executed in a single event manager process" (p. 168). Events are handled by the manager process, which "invokes all added handlers sequentially, one at a time" (p. 172).

# Prerequisites

- **Event** — An event manager exists to receive and route events.
- **Generic server** — The generic server "still acts as its foundation" for the event behavior.

# Key Properties

1. An Erlang process running the generic `gen_event` code.
2. Receives events as messages from producers.
3. Holds zero or more event handlers — a one-to-many relationship unique among OTP behaviors.
4. All handlers run inside the single event manager process.
5. Invokes added handlers sequentially, one at a time, per event.
6. Can be started registered (`local`/`global`/`via`) or unregistered (use the pid).

# Construction / Recognition

## To Start an Event Manager:
1. Call `gen_event:start_link(NameScope)` to start it registered, or `start_link/0` for an unregistered one.
2. The manager begins with an empty handler list — no callback modules are invoked at start.
3. Add handlers dynamically with `gen_event:add_handler/3`.

# Context & Application

- **Typical contexts**: Monitoring subsystems that must route events to varying sets of actions.
- **Common applications**: Alarm managers, debug-trace managers, equipment-state managers; the book's `freq_overload` manager.
- **Historical/stylistic notes**: The book calls the one-to-many manager/handler relationship "the biggest difference between the event manager and other OTP behaviors" (p. 185).

# Examples

**Example 1** (p. 171): `{ok, P} = gen_event:start()` starts an unregistered event manager.

**Example 2** (pp. 181-183): `freq_overload:start_link/0` wraps `gen_event:start_link({local, ?MODULE})` and adds the `counters` and `logger` handlers.

# Relationships

## Builds Upon
- **Event** — The manager's reason for existing is to receive events.
- **Generic server** — The generic server is the foundation of the event behavior.

## Enables
- **event-handler** — Handlers are added to a manager.
- **gen-event-behavior** — The manager runs the `gen_event` generic code.

## Related
- **notifying-events** — Events are pushed to the manager via `notify/2`/`sync_notify/2`.

## Contrasts With
- **Generic server** — A `gen_server` allows exactly one callback module; an event manager runs zero or more handlers.

# Common Errors

- **Error**: Sending many events to a manager with slow handlers and letting the message queue grow.
  **Correction**: Handlers run sequentially in the single manager process; ensure handlers do not become bottlenecks, and consider synchronous events to throttle producers.

# Common Confusions

- **Confusion**: Thinking each handler runs in its own process.
  **Clarification**: All handlers of a manager execute within the *single* event manager process, sequentially.

# Source Reference

Chapter 6: Event Handlers, Sections "Events" and "Generic Event Managers and Handlers," pages 166-168. See Figure 7-2.

# Verification Notes

- Definition source: Direct quotes from pp. 166-168.
- Confidence rationale: HIGH — the source explicitly defines the event manager and its one-to-many relationship with handlers.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
