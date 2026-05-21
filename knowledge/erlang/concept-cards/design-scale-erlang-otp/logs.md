---
# === CORE IDENTIFICATION ===
concept: Logs
slug: logs

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
section: "Monitoring — Logs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - log
  - logging
  - audit trail

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monitoring
extends: []
related:
  - metrics
  - alarms
  - oam
contrasts_with:
  - metrics
  - alarms

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a log?"
  - "How should I design my logging strategy?"
---

# Quick Definition

A log is an entry in a file or database that records an event forming part of an audit trail — a system event or a state change in the business logic.

# Core Definition

"A log is an entry in a file or database that records an event that can be used as part of an audit trail. The entry could reflect a system event in the Erlang VM or operating system, or an event that triggers a state change in your business logic. Logs are used for a variety of purposes, including tracing, debugging, auditing, compliance monitoring, and billing. Different log entries are usually tagged, allowing you to decide the level of granularity of what is stored at runtime. Common tags include debug, info, notice, warning, and error" (Cesarini & Vinoski, p. 447).

# Prerequisites

- **Monitoring** — Logs are one of the three monitoring facilities; understand monitoring first.

# Key Properties

1. An entry in a file or database recording an event, part of an audit trail.
2. Records system events (Erlang VM, OS) or business-logic state changes.
3. Used for tracing, debugging, auditing, compliance monitoring, and billing.
4. Entries are tagged (debug, info, notice, warning, error) to control runtime granularity.
5. Unique identifiers must link log entries across nodes to recreate the request flow.
6. Different log types should use separate files (and possibly formats); reduce repetition.
7. Logs should be append-only when stored locally and ideally form a relational model.

# Construction / Recognition

## To Construct/Create:
1. Trace each request's functional information flow; identify where it changes system state.
2. Assign a unique ID when an external client request enters the system.
3. Log incoming/outgoing requests and results, with the unique ID, at notable state changes.
4. Use separate files per log type; reduce repetition by linking via identifiers.
5. Plan the logging strategy before coding — logs may be the only reason for unique IDs.

## To Identify/Recognize:
1. Recognize a log as a timestamped, tagged record of an event forming part of an audit trail.

# Context & Application

- **Typical contexts**: Production systems handling many requests; auditing and billing.
- **Common applications**: Following request flow across nodes; proving innocence/admitting guilt for missing transactions; building customer profiles.
- **Historical/stylistic notes**: SASL provides free supervisor, progress, error, and crash reports; Lager is a popular open-source logging framework. Logs can also be viewed as FSMs where each entry is a state.

# Examples

**Example 1** (pp. 451-452, "Where Is My Text Message?"): Using unique identifiers, the team traced three SMSs through front-end, logic, and service node logs and the SMSC delivery report log, proving the system handled them in milliseconds and the delay was the user's handset being out of coverage.

**Example 2** (p. 448): A system where processes crashed daily but were automatically restarted — failure was so well isolated the team had no idea the system was riddled with bugs; automated discovery of SASL crash and error reports is needed.

# Relationships

## Builds Upon
- **Monitoring** — Logs are one of the three monitoring facilities

## Enables
- Logs enable tracing, debugging, auditing, compliance monitoring, and billing.

## Related
- **Metrics** — A sibling monitoring facility
- **Alarms** — A sibling monitoring facility
- **OAM** — Logs are collected and managed via OAM

## Contrasts With
- **Metrics** — A log records a state-changing event; a metric is a polled numeric value
- **Alarms** — A log records that something happened; an alarm indicates something is ongoing

# Common Errors

- **Error**: Adding your own log entries to the SASL logs
  **Correction**: This mixes logs of different types and purposes; use separate files (and possibly formats) for every log type.

- **Error**: Designing logging after coding
  **Correction**: Think through the logging strategy before coding — logs may be the only reason for unique IDs in the business logic.

# Common Confusions

- **Confusion**: A log and a metric are interchangeable observability data.
  **Clarification**: A log records a discrete state-changing event; a metric is a numeric value polled at intervals.

# Source Reference

Chapter 15: Monitoring and Preemptive Support, "Monitoring — Logs," pages 447-452. See the Lager sidebar and the "Where Is My Text Message?" sidebar.

# Verification Notes

- Definition source: Direct quote from p. 447.
- Confidence rationale: HIGH — the source dedicates a named subsection with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
