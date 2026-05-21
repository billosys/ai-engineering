---
# === CORE IDENTIFICATION ===
concept: Error Logging
slug: error-logging

# === CLASSIFICATION ===
category: error-handling
subcategory: runtime-errors
tier: foundational

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Error Logging"
chapter_number: null
pdf_page: null
section: "Error Information From the Runtime System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "runtime error reporting"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - logger
  - otp-behaviour-log-events
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Erlang runtime system report errors?"
  - "Where does error information from the runtime system go?"
---

# Quick Definition

Error logging in Erlang/OTP refers to the mechanism by which the runtime system outputs information about process terminations caused by uncaught error exceptions, handled by Logger as part of the Kernel application.

# Core Definition

As stated in the OTP System Principles: "Error information from the runtime system, that is, information about a process terminating because of an uncaught error exception, is by default written to the terminal (TTY)." This error information is handled by Logger, which is part of the Kernel application. The exit reasons used by the runtime system (such as `badarg`) are described in the Erlang Reference Manual's "Errors and Error Handling" section.

# Prerequisites

This is a foundational concept with no prerequisites.

# Key Properties

1. The runtime system generates error information when a process terminates due to an uncaught error exception.
2. By default, error information is written to the terminal (TTY).
3. Error information is handled by Logger, part of the Kernel application.
4. Exit reasons (e.g., `badarg`, `badmatch`) describe the cause of the error.
5. The system can be configured to write log events to file, TTY, or both.

# Construction / Recognition

## To Construct/Create:
1. Error logging happens automatically — any process that terminates with an uncaught exception produces an error report.
2. Configure output destination (file, TTY, or both) via Logger configuration.

## To Identify/Recognize:
1. Error reports appear with the format `=ERROR REPORT====` followed by a timestamp.
2. The report includes the process ID and the exit value.

# Context & Application

Error logging is fundamental to understanding and debugging Erlang systems. When a process crashes due to an unhandled exception, the runtime system automatically produces an error report. In development, these reports appear on the terminal. In production, Logger is typically configured to write them to log files. User-defined applications can also send and format log events using Logger.

# Examples

**Example 1** (Error Logging, "Error Information From the Runtime System"): A runtime error report:
```text
=ERROR REPORT==== 9-Dec-2003::13:25:02 ===
Error in process <0.27.0> with exit value: {{badmatch,[1,2,3]},[{m,f,1},{shell,eval_loop,2}]}
```

# Relationships

## Builds Upon
- No prerequisites — this is a foundational concept.

## Enables
- **logger** — Logger is the facility that handles error information from the runtime system
- **otp-behaviour-log-events** — OTP behaviours produce their own log events through the same logging infrastructure

## Related
- **logger** — Logger handles all error information
- **otp-behaviour-log-events** — standard behaviours also produce log events

## Contrasts With
- No direct contrast in source.

# Common Errors

- **Error**: Ignoring error reports during development, assuming they are informational.
  **Correction**: Error reports indicate process crashes — they should be investigated as potential bugs.

# Common Confusions

- **Confusion**: Thinking error logging must be explicitly enabled.
  **Clarification**: Error logging is automatic. The runtime system reports uncaught exceptions by default; no configuration is needed for basic error reporting.

# Source Reference

"Error Information From the Runtime System" section, "Error Logging" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Directly quoted from source text.
- Confidence rationale: High — explicit definition with example output.
- Uncertainties: None.
- Cross-reference status: References logger, otp-behaviour-log-events (cards in this extraction).
