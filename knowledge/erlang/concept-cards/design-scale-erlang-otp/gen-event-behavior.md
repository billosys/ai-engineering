---
# === CORE IDENTIFICATION ===
concept: Generic Event Behavior
slug: gen-event-behavior

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
  - "gen_event"
  - event behavior
  - generic event manager behavior

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-manager
  - event-handler
  - gen-server
extends:
  - gen-server
related:
  - notifying-events
  - gen-event-call
  - swapping-event-handlers
contrasts_with:
  - gen-server
  - generic-fsm-behavior

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "What is an OTP behavior?"
  - "How does a behavior relate to its callback module?"
---

# Quick Definition

The generic event behavior (`gen_event`) is the OTP library module providing all generic event-handling code — starting/stopping the manager, adding/removing/upgrading handlers, and forwarding events — while application-specific handlers supply the callbacks.

# Core Definition

"Generic event handlers and managers are part of the standard library application, and like all other behaviors, are split up into generic and specific code. The `gen_event` module contains all of the generic code. The process running this code is often referred to as the event manager. The callback modules subscribing to the events and handling them through a set of callback functions are called the event handlers" (Cesarini & Vinoski, p. 167). The generic side handles starting/stopping the manager, sending events, sending synchronous requests, forwarding events/requests to handlers, adding/deleting handlers, and upgrading handlers. The specific side handles the events, the event handlers, initializing handlers, handler loop data, handling events/requests, and cleaning up (Table 7-1, p. 167). Although the generic server "still acts as its foundation, it is very different from the behaviors we've looked at so far" — most notably in supporting many handlers per manager (p. 168).

> **OTP-27+ note:** `gen_event` remains current in modern OTP. The book's APIs (`add_handler/3`, `notify/2`, etc.) are unchanged.

# Prerequisites

- **Event manager** — The `gen_event` process *is* the event manager.
- **Event handler** — The behavior's callback modules are event handlers.
- **Generic server** — The generic server is the foundation of `gen_event`.

# Key Properties

1. Generic code lives in the `gen_event` standard-library module.
2. Specific code lives in callback modules — the event handlers.
3. Generic responsibilities: start/stop manager, send events, send sync requests, forward to handlers, add/delete/upgrade handlers.
4. Specific responsibilities: the events, the handlers, initializing handlers, handler loop data, handling events, cleanup.
5. Unique among behaviors: one manager, zero-or-more handlers (one-to-many).
6. The event manager by default traps exits.
7. `gen_event:start_link/0` accepts no callback modules, arguments, or options and invokes no callbacks — it just sets the handler list to empty.

# Construction / Recognition

## To Use the gen_event Behavior:
1. Start the manager with `gen_event:start_link/0,1`.
2. Implement handler callback modules carrying `-behavior(gen_event)`.
3. Add handlers with `add_handler/3` (or `add_sup_handler/3`).
4. Push events with `notify/2` / `sync_notify/2`; query with `call/3`.
5. Remove handlers with `delete_handler/3`; stop the manager with `stop/1`.

# Context & Application

- **Typical contexts**: Any subsystem needing pluggable, runtime-swappable event handling.
- **Common applications**: Logging, metrics, and alarm subsystems; the SASL `alarm_handler`.
- **Historical/stylistic notes**: The book presents `gen_event` as the last worker behavior before supervisors; it differs sharply from `gen_server` and `gen_fsm` due to the one-to-many manager/handler model (pp. 168, 185-186).

# Examples

**Example 1** (p. 168): The `gen_event` start/stop API — `start_link/0,1` returns `{ok, Pid}` or `{error, {already_started, Pid}}`; `stop/1` returns `ok`.

**Example 2** (Table 7-2, pp. 185-186): The mapping of `gen_event` functions to callbacks — `notify/2`/`sync_notify/2` → `handle_event/2`, `call/3` → `handle_call/2`, `delete_handler/3` → `terminate/2`.

# Relationships

## Builds Upon
- **Generic server** — `gen_event` is built on the generic server foundation.

## Enables
- **notifying-events** — Events are pushed via `gen_event` functions.
- **gen-event-call** — Synchronous handler queries via `gen_event:call/3`.
- **swapping-event-handlers** — Runtime handler swapping via `swap_handler/3`.

## Related
- **event-manager** — The `gen_event` process is the manager.
- **event-handler** — Callback modules are the handlers.

## Contrasts With
- **Generic server** — `gen_server` is one-to-one (process to callback module); `gen_event` is one-to-many.
- **Generic FSM behavior** — `gen_fsm` and `gen_event` are both worker behaviors built on `gen_server`, but `gen_event` is the only one supporting multiple callback modules per process.

# Common Errors

- **Error**: Passing callback modules or arguments to `gen_event:start_link/0`.
  **Correction**: `start_link/0` takes no callback modules, arguments, or options; add handlers separately with `add_handler/3`.

# Common Confusions

- **Confusion**: Expecting `gen_event` to behave like `gen_server` with a single callback module.
  **Clarification**: `gen_event`'s defining feature is the one-to-many relationship — one manager runs many handlers, all in one process.

# Source Reference

Chapter 6: Event Handlers, Section "Generic Event Managers and Handlers," pages 167-168; summary in Table 7-2, pages 185-186.

# Verification Notes

- Definition source: Direct quotes from pp. 167-168.
- Confidence rationale: HIGH — the source explicitly defines the behavior and its generic/specific split.
- Uncertainties: The OTP-27+ note is added per taxonomy guidance; `gen_event` is unchanged from the book's era.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
