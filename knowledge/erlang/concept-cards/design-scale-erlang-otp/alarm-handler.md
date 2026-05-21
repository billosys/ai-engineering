---
# === CORE IDENTIFICATION ===
concept: Alarm Handler
slug: alarm-handler

# === CLASSIFICATION ===
category: production-ops
subcategory: alarm-handling
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 184
section: "The SASL Alarm Handler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "alarm_handler"
  - SASL alarm handler
  - "set_alarm"
  - "clear_alarm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-manager
  - event-handler
extends:
  - event-handler
related:
  - notifying-events
  - swapping-event-handlers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I monitor a production system and provide preemptive support?"
---

# Quick Definition

An alarm handler is the part of a system that records ongoing issues and takes appropriate action; the SASL `alarm_handler` is a basic event-manager-and-handler shipped with Erlang/OTP, meant to be replaced or complemented as needs grow.

# Core Definition

"An alarm handler is the part of the system that records ongoing issues and takes appropriate actions. If your system reaches a high memory mark or is running out of disk space (or frequencies), you will want to set (or raise) an alarm. When memory usage decreases or old log files are deleted, the respective alarms are cleared. At any point in time, it should be possible to inspect the list of active alarms and get a snapshot of ongoing issues" (Cesarini & Vinoski, p. 184). "The SASL alarm handler process is an event manager and handler that comes as part of the Erlang runtime system and provides this functionality. It is a very basic alarm handler you are encouraged to replace or complement in your own project when more functionality is required" (p. 184). Its wrapper API exports `alarm_handler:set_alarm({AlarmId, Description})`, `alarm_handler:clear_alarm(AlarmId)`, and `alarm_handler:get_alarms()`.

# Prerequisites

- **Event manager** — The SASL alarm handler *is* an event manager.
- **Event handler** — It bundles a default handler that can be swapped out.

# Key Properties

1. Records ongoing issues and (in advanced systems) takes corrective action.
2. The SASL `alarm_handler` is a built-in event manager plus handler in the Erlang runtime.
3. API: `set_alarm({AlarmId, Description})`, `clear_alarm(AlarmId)`, `get_alarms() -> [{AlarmId, Description}]`.
4. Started via `application:start(sasl)`; check with `whereis(alarm_handler)`.
5. The default handler is deliberately basic — intended to be replaced or complemented.
6. A replacement must handle the events `{set_alarm, {AlarmId, AlarmDescr}}` and `{clear_alarm, AlarmId}`.
7. The default handler does not scale: no statistics, no logging, no dependency-aware clearing.

# Construction / Recognition

## To Use the SASL Alarm Handler:
1. Run `whereis(alarm_handler)`; if `undefined`, start it with `application:start(sasl)`.
2. Raise an alarm with `alarm_handler:set_alarm({AlarmId, Description})`.
3. Clear it with `alarm_handler:clear_alarm(AlarmId)`.
4. Inspect active alarms with `alarm_handler:get_alarms()`.

## To Replace the Handler:
1. Implement a new handler that handles `{set_alarm, ...}` and `{clear_alarm, ...}` events.
2. Swap it in with `gen_event:swap_handler(alarm_handler, {alarm_handler, swap}, {NewHandler, Args})`.
3. In the new handler's `init`, match `{Args, {alarm_handler, Alarms}}` to inherit the existing alarm list.

# Context & Application

- **Typical contexts**: System monitoring — surfacing and tracking ongoing faults.
- **Common applications**: Raising a `fan_failure` or `cabinet_door_open` alarm in a hardware rack.
- **Historical/stylistic notes**: The basic SASL handler embodies the Erlang philosophy of "start simple and add complexity as your system grows" (p. 184). The book's own `freq_overload` manager is a worked alternative.

# Examples

**Example 1** (p. 184): Raising and clearing alarms with the SASL handler:

```erlang
alarm_handler:set_alarm({103, fan_failure}).
alarm_handler:set_alarm({104, cabinet_door_open}).
alarm_handler:clear_alarm(104).
alarm_handler:get_alarms().   %% => [{103, fan_failure}]
```

**Example 2** (p. 184): Swapping the SASL handler — the new handler's `init` pattern matches `{Args, {alarm_handler, Alarms}}`, where `Alarms` is a list of `{AlarmId, Description}` tuples.

# Relationships

## Builds Upon
- **Event handler** — An alarm handler is a specialized event handler.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **notifying-events** — Alarms are raised and cleared by notifying `set_alarm`/`clear_alarm` events.
- **swapping-event-handlers** — The SASL handler is designed to be replaced via `swap_handler/3`.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Relying on the basic SASL `alarm_handler` for a large production system.
  **Correction**: It does not scale (no statistics, logging, or dependency-aware clearing); replace or complement it with a project-specific handler as the system grows.

# Common Confusions

- **Confusion**: Thinking the alarm handler must be built from scratch.
  **Clarification**: Erlang ships the SASL `alarm_handler` as a working starting point; you extend or swap it rather than starting empty.

# Source Reference

Chapter 6: Event Handlers, Section "The SASL Alarm Handler," pages 184-185. Alarming is revisited in Chapters 9, 11, and 16.

# Verification Notes

- Definition source: Direct quotes from p. 184.
- Confidence rationale: HIGH — the source explicitly defines an alarm handler and documents the SASL `alarm_handler` API.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
