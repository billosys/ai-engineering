---
# === CORE IDENTIFICATION ===
concept: Alarms
slug: alarms

# === CLASSIFICATION ===
category: production-ops
subcategory: observability
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Monitoring and Preemptive Support"
chapter_number: 15
pdf_page: 444
section: "Monitoring — Alarms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - alarm
  - alarm handler
  - threshold-based alarm
  - state-based alarm

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monitoring
  - metrics
extends: []
related:
  - logs
  - oam
  - preemptive-support
contrasts_with:
  - logs
  - metrics

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an alarm?"
  - "What distinguishes a threshold-based alarm from a state-based alarm?"
---

# Quick Definition

An alarm is a subset of events associated with a state — raised when a monitored issue manifests, remaining active until resolved, then cleared. Alarms can be threshold-based or state-based.

# Core Definition

"Alarms are a subset of events associated with a state. While an event will tell you that something happened, an alarm will indicate that something is ongoing" (Cesarini & Vinoski, p. 455). "An alarm is raised when the issue you are monitoring manifests itself ... The alarm is said to remain active until the issue is resolved ... When this happens, the alarm is said to be cleared" (pp. 455-456). Alarms can carry a severity (cleared, indeterminate, critical, major, minor, warning) and are either threshold-based (raised when a metric exceeds a limit) or state-based (triggered by a potentially harmful state change).

# Prerequisites

- **Monitoring** — Alarms are one of the three monitoring facilities; understand monitoring first.
- **Metrics** — Threshold-based alarms are raised from monitored metrics.

# Key Properties

1. A subset of events associated with a state — indicating something is ongoing, not just that something happened.
2. Raised when the monitored issue manifests; remains active until resolved; then cleared.
3. Can carry a severity: cleared, indeterminate, critical, major, minor, warning.
4. Severities are configured per system, letting teams and scripts react differently.
5. Threshold-based alarms are raised when a metric exceeds a limit.
6. State-based alarms are triggered by a potentially harmful state change (hardware issue, unresponsive API, node down).
7. Can originate from the affected node or the OAM node.

# Construction / Recognition

## To Construct/Create:
1. Decide which issues warrant alarms and their severities.
2. For threshold-based alarms, monitor metrics and raise when a limit is exceeded.
3. For state-based alarms, trigger on harmful state changes.
4. Clear the alarm when the issue is resolved.
5. Fine-tune thresholds to eliminate false positives and manage false negatives.

## To Identify/Recognize:
1. Recognize an alarm by its lifecycle — raised, active, cleared — and its association with an ongoing state.

# Context & Application

- **Typical contexts**: Production monitoring; preemptive support.
- **Common applications**: Disk-full alarms with escalating severity; long-message-queue alarms raised on managed nodes; hardware-fault alarms.
- **Historical/stylistic notes**: SASL has a basic alarm handler (raise/clear, no severities or dependencies); elarm is the de facto Erlang alarm manager for OAM nodes, handling severities, duplication, and operator interaction.

# Examples

**Example 1** (pp. 456-457): A disk 80% full might be a minor-severity alarm (deal with it after the coffee break); at 90% it becomes major (call out of office hours); at 95% it becomes critical (a pager call gets someone out of bed).

**Example 2** (p. 456): Processes with very long message queues — a symptom of issues about to happen — must be monitored and alarmed on the managed nodes, since sending all process message-queue lengths to the OAM node is not feasible.

# Relationships

## Builds Upon
- **Monitoring** — Alarms are one of the three monitoring facilities
- **Metrics** — Threshold-based alarms are raised from metrics

## Enables
- **Preemptive support** — Alarms drive preemptive support automation

## Related
- **Logs** — A sibling monitoring facility; all alarm events are logged
- **OAM** — Alarms are aggregated and consolidated in the OAM node

## Contrasts With
- **Logs** — A log records that something happened; an alarm indicates something is ongoing
- **Metrics** — A metric is raw numeric data; an alarm is an event raised when a state or threshold condition is met

# Common Errors

- **Error**: Increasing the supervisor's allowed restarts to silence repeated crashes
  **Correction**: That is not the solution; solve the root problem causing the crashes (related discussion p. 448).

- **Error**: Tolerating many false positives
  **Correction**: Fine-tune thresholds — too many false positives result in serious alarms being ignored.

# Common Confusions

- **Confusion**: An alarm and an event are the same.
  **Clarification**: An event tells you something happened (a socket closed); an alarm indicates something is ongoing (inability to create any socket connection).

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring — Alarms," pages 455-459. See the Elarm sidebar.

# Verification Notes

- Definition source: Direct quotes from pp. 455-456.
- Confidence rationale: HIGH — the source dedicates a named subsection defining alarms, severities, and the threshold/state distinction.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
