---
# === CORE IDENTIFICATION ===
concept: Alarm Management
slug: alarm-management

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
section: "Alarm Management"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "alarm handler"
  - "alarm_handler"
  - "OTP alarms"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - error-logger
extends: []
related:
  - supervisor
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is alarm management in OTP?"
  - "How do I raise and clear an alarm in an OTP system?"
---

# Quick Definition

Alarm management is the OTP mechanism for raising and clearing alarms. The OTP `alarm_handler` is a `gen_event` callback; you set an alarm with `alarm_handler:set_alarm/1` and clear it with `alarm_handler:clear_alarm/1`, and install custom handlers to react.

# Core Definition

OTP provides a real alarm handler, "a callback module for the OTP `gen_event` behavior" (Programming Erlang, "Alarm Management"). Alarms are just events. The default `alarm_handler` (available after `erl -boot start_sasl`) does nothing special — setting an alarm merely produces an information report. A custom handler is installed by swapping it into the alarm manager with `gen_event:swap_handler/3`. The custom handler's `handle_event(Event, State)` matches `{set_alarm, AlarmId}` and `{clear_alarm, AlarmId}` events — where the event tuple is `{EventType, EventArg}` — and returns `{ok, NewState}`. Alarms are raised with `alarm_handler:set_alarm(AlarmId)` and cleared with `alarm_handler:clear_alarm(AlarmId)`.

# Prerequisites

- **gen_event** — the alarm handler is a gen_event callback module.
- **The error logger** — custom alarm handlers typically report through `error_logger:error_msg`.

# Key Properties

1. Alarms are a special case of events; the alarm handler is a `gen_event` callback module.
2. The default `alarm_handler` (from `start_sasl`) only emits an information report on `set_alarm`.
3. A custom handler is installed via `gen_event:swap_handler(alarm_handler, {alarm_handler, swap}, {my_handler, Arg})`.
4. `set_alarm(AlarmId)` raises an alarm; `clear_alarm(AlarmId)` clears it.
5. `handle_event/2` clauses match `{set_alarm, Id}` and `{clear_alarm, Id}` and return `{ok, NewState}`.
6. The custom handler's `init/1` argument may be any value; its only role is identification when printed.

# Construction / Recognition

## To Manage Alarms:
1. Write a `gen_event` callback module (e.g. `my_alarm_handler`) implementing `handle_event/2` for `{set_alarm, Id}` and `{clear_alarm, Id}`.
2. Install it: `gen_event:swap_handler(alarm_handler, {alarm_handler, swap}, {my_alarm_handler, xyz})`.
3. In application code, call `alarm_handler:set_alarm(Id)` before the risky operation and `alarm_handler:clear_alarm(Id)` after.

## To Recognize:
1. Calls to `alarm_handler:set_alarm`/`clear_alarm` manage alarms.
2. A `gen_event` callback matching `{set_alarm, ...}` events is a custom alarm handler.

# Context & Application

- **Typical contexts**: Signalling and responding to abnormal but expected operational conditions.
- **Common applications**: In the `sellaprime` system, the `tooHot` alarm is raised while computing a large prime (`K > 100`) and cleared afterwards; the supervisor installs `my_alarm_handler` in its `init/1`.
- **Historical/stylistic notes**: The book contrasts the real OTP alarm handler with the simple do-nothing event handler shown earlier in the chapter.

# Examples

**Example 1** ("Alarm Management"): `my_alarm_handler`'s event clauses:

```erlang
handle_event({set_alarm, tooHot}, N) ->
    error_logger:error_msg("*** Tell the Engineer to turn on the fan~n"),
    {ok, N+1};
handle_event({clear_alarm, tooHot}, N) ->
    error_logger:error_msg("*** Danger over. Turn off the fan~n"),
    {ok, N};
```

**Example 2** ("The Prime Number Server"): `prime_server` brackets a large-prime computation with `alarm_handler:set_alarm(tooHot)` and `alarm_handler:clear_alarm(tooHot)`.

# Relationships

## Builds Upon
- **gen_event** — the alarm handler is a gen_event callback module.

## Enables
- (No further concepts in this chapter build directly on alarm management.)

## Related
- **The error logger** — custom alarm handlers report alarm events through the error logger.
- **Supervisor** — the `sellaprime` supervisor installs the custom alarm handler in its `init/1`.
- **OTP application** — alarm handling is part of the packaged `sellaprime` application.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Setting an alarm but never clearing it.
  **Correction**: Pair every `set_alarm(Id)` with a `clear_alarm(Id)` once the condition has passed.

- **Error**: Expecting the default `alarm_handler` to take action.
  **Correction**: The default handler only emits an info report; install a custom `gen_event` handler to react.

# Common Confusions

- **Confusion**: Thinking alarms are a separate subsystem from events.
  **Clarification**: "Alarms are just events"; the alarm handler is an ordinary `gen_event` callback module.

- **Confusion**: Believing the `init/1` argument to the custom handler is meaningful.
  **Clarification**: In the book's example the argument `xyz` "has no particular significance"; it only helps identify the handler when printed.

# Source Reference

Chapter 23: Making a System with OTP, section "Alarm Management" and "Reading the Log". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "Alarm Management".
- Confidence rationale: HIGH — alarms, the alarm handler, and set/clear are explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
