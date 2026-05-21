---
# === CORE IDENTIFICATION ===
concept: Logging Severity Level
slug: severity-level

# === CLASSIFICATION ===
category: error-handling
subcategory: logging
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.1.1 Logging in general"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "log level"
  - "logging level"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - logging-in-erlang-otp
  - error-logger
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a logging severity level?"
  - "When should I use error vs. warning vs. info vs. debug?"
  - "How many log levels does Erlang's standard logging API provide?"
---

# Quick Definition

A severity level is a label attached to a log message that indicates how important the information is, letting operators filter messages by minimum importance. A common scheme uses critical, error, warning, info, and debug.

# Core Definition

A logging severity level indicates the importance of the information being logged. The book describes a common five-level scheme — critical (or severe), error, warning, info, and debug — though names vary between systems. Operators typically set a minimum level of interest: setting it to *debug* shows everything, *info* shows everything except debug, *warn* shows only problems, and so on. Erlang's standard `error_logger` API provides only three of these: error, warning, and info; this is not a major limitation because custom report types and event handlers are easy to add (Ch. 7, Sections 7.1.1, 7.1.3).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Indicates the importance of a logged message.
2. The common five-level scheme: critical/severe, error, warning, info, debug.
3. Erlang's standard `error_logger` API exposes only three levels: error, warning, info.
4. Operators can set a minimum level; messages below it are not shown.
5. By default in Erlang, warnings are mapped to errors (changeable with `erl +W w`).

# Construction / Recognition

## To Choose a Level:
1. **Critical/severe** — manual action needed immediately; the system has failed catastrophically. Use rarely.
2. **Error** — something bad but not critical (a subsystem crashed and restarted). Needs fixing but can wait.
3. **Warn** — something potentially bad that can be ignored or worked around for now.
4. **Info** — an informational message; something happened worth noting.
5. **Debug** — details for the developer to diagnose a running system.

# Context & Application

- **Typical contexts**: Every logging system attaches severity to messages.
- **Common applications**: Filtering log noise; routing critical events to alerting.
- **Historical/stylistic notes**: Historically Erlang had only info and error; warnings were added later and still map to errors by default.

# Examples

**Example 1** (Section 7.1.1): "Critical or severe" is "reserved for the kind of emergency that people need to be dragged out of bed at 3 A.M. to fix."

**Example 2** (Section 7.1.1): An info message may be good ("backup job finished") or slightly bad ("couldn't send mail; will retry in five minutes").

# Relationships

## Builds Upon
- None.

## Enables
- **error-logger** — Its API functions are organized by severity level.

## Related
- **Logging in Erlang/OTP** — Severity levels are a building block of any logging system.

## Contrasts With
- None.

# Common Errors

- **Error**: Logging too much at error level so operators start ignoring messages.
  **Correction**: Reserve error for genuine problems; use info/debug for routine detail.

# Common Confusions

- **Confusion**: Assuming Erlang's logger supports all five levels.
  **Clarification**: The standard `error_logger` API has only error, warning, and info.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Sections 7.1.1 "Logging in general" and 7.1.3 "The standard logging functions."

# Verification Notes

- Definition source: Directly adapted from Section 7.1.1's level descriptions.
- Confidence rationale: HIGH — the book explicitly defines each level.
- Uncertainties: None.
- Cross-reference status: Verified.
