---
# === CORE IDENTIFICATION ===
concept: Event
slug: event

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: foundational

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 166
section: "Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - system event
  - producer
  - consumer

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - event-manager
  - event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

An event represents a state change in the system — such as a high CPU load, a hardware failure, or a trace event — sent as a message to an event manager for handling.

# Core Definition

"An *event* represents a state change in the system. It could be a high CPU load, a hardware failure, or a trace event resulting from the activity in a port" (Cesarini & Vinoski, p. 166). Events are generated and "sent to the manager in the form of a message." For every event generated, the system might take a specific set of actions: generate SNMP traps; send emails, SMSs, or pager messages; collect statistics; print messages to a console; or log the event to a file. The book names the two roles around an event: "We call these processes that generate events *producers* and processes receiving and handling these events *consumers*" (p. 166).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An event represents a state change in the system.
2. Examples: high CPU load, hardware failure, port trace activity, alarms, warnings, equipment state changes, network connectivity issues.
3. An event is delivered as a message.
4. Each event may trigger a specific set of actions.
5. *Producers* generate events; *consumers* receive and handle them.

# Construction / Recognition

## To Generate an Event:
1. Detect a state change worth reporting.
2. Send it as a message to an event manager (e.g., via `gen_event:notify/2`).

## To Recognize an Event:
1. Look for messages flowing into an event manager.
2. Look for distinct, discrete state-change notifications rather than continuous data.

# Context & Application

- **Typical contexts**: Monitoring and observability — collecting statistics, logging, and alerting.
- **Common applications**: Alarms, warnings, equipment state changes, debug traces.
- **Historical/stylistic notes**: The chapter motivates events with a monitoring scenario: the same event types must trigger different actions (widget, email, SMS, phone call) at different times depending on external factors (p. 166).

# Examples

**Example 1** (p. 166): A high CPU load, a hardware failure, or a port trace event — each is an event representing a system state change.

**Example 2** (p. 171, shell command 3): `gen_event:notify(P, {set_alarm, {no_frequency, self()}})` sends a `set_alarm` event to a manager.

# Relationships

## Builds Upon
- *(Foundational — nothing within this source.)*

## Enables
- **event-manager** — An event manager exists to receive and route events.
- **event-handler** — Event handlers exist to handle events.

## Related
- **event-manager** — Events are sent to the manager as messages.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Treating continuous metric streams as individual events.
  **Correction**: An event is a discrete state change; aggregate continuous data before turning thresholds into events.

# Common Confusions

- **Confusion**: Conflating an event with the action taken in response to it.
  **Clarification**: An event is the state-change notification; the response (SNMP trap, email, log entry) is a separate action chosen by a handler.

# Source Reference

Chapter 6: Event Handlers, Section "Events," pages 166-167. See Figure 7-1.

# Verification Notes

- Definition source: Direct quote from p. 166.
- Confidence rationale: HIGH — the source opens the chapter with an explicit definition of an event.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
