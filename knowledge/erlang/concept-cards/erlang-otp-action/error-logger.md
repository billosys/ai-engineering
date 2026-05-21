---
# === CORE IDENTIFICATION ===
concept: error_logger Module
slug: error-logger

# === CLASSIFICATION ===
category: error-handling
subcategory: logging
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Logging and event handling the Erlang/OTP way"
chapter_number: 7
pdf_page: null
section: "7.1.3 The standard logging functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error_logger"
  - "standard logging functions"
  - "error logger process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logging-in-erlang-otp
extends: []
related:
  - severity-level
  - error-logger-events
  - gen-event
  - sasl
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the error_logger module?"
  - "How do I write a log message in Erlang?"
  - "What functions does the standard Erlang logging API provide?"
---

# Quick Definition

`error_logger` is the standard Erlang logging module in the `kernel` application; it provides functions like `info_msg/2`, `warning_msg/2`, and `error_msg/2` for emitting log messages, plus report variants that carry a type tag.

# Core Definition

`error_logger` is the module in the `kernel` application that provides the standard API for posting log messages. Its basic functions — `error_msg/1,2`, `warning_msg/1,2`, and `info_msg/1,2` — take a format string and an optional list of data values, with the same interface as `io:format/1,2`. They are more tolerant than `io:format`: a bad format specification still produces a message rather than crashing. A more modern set of functions — `error_report`, `warning_report`, `info_report` — accept a report term and optionally a type, allowing user-defined report types. The name `error_logger` also refers to the always-present registered system process to which all these log events are sent; it is a `gen_event` event manager (Ch. 7, Section 7.1.3).

# Prerequisites

- **Logging in Erlang/OTP** — `error_logger` is the central piece of that system; understanding the overall design situates the module.

# Key Properties

1. Lives in the `kernel` application's standard library.
2. Provides only three severity levels: error, warning, info.
3. Message functions (`*_msg`) use `io:format`-style format strings.
4. Report functions (`*_report`) accept a report term and an optional type tag.
5. More tolerant of format errors than `io:format` — a bad spec still yields a message.
6. The registered process named `error_logger` is a `gen_event` event manager that always exists.

# Construction / Recognition

## To Emit a Log Message:
1. Call `error_logger:info_msg(Format)` or `info_msg(Format, Data)` with format string and data list.
2. Use `warning_msg` or `error_msg` for higher severities.
3. For typed structured reports, use `info_report(Type, Report)` etc.

## To Recognize:
1. Output appears with a `=INFO REPORT====`/`=ERROR REPORT====` heading and timestamp.

# Context & Application

- **Typical contexts**: Application code that needs to record events or errors.
- **Common applications**: Routine logging; the target the SASL handler and custom handlers subscribe to.
- **Historical/stylistic notes**: Historically there were only info and error messages; warnings are mapped to errors by default.

# Examples

**Example 1** (Section 7.1.3): `error_logger:info_msg("This is an ~s message~n", ["info"])` produces "This is an info message" under an `=INFO REPORT====` heading.

**Example 2** (Section 7.1.3): Passing the wrong number of arguments — `info_msg("This is an ~s message~n", ["info", this_is_an_unused_atom])` — still produces an `ERROR:` line with the format and data rather than crashing.

# Relationships

## Builds Upon
- **Logging in Erlang/OTP** — `error_logger` is the standard API component of that system.

## Enables
- **error-logger-events** — Each call generates a specific event tuple consumed by handlers.

## Related
- **gen_event** — The `error_logger` process is a `gen_event` event manager.
- **SASL** — Adds a handler to `error_logger` for behaviour reports.
- **Severity level** — Functions are organized by error/warning/info.

## Contrasts With
- None.

# Common Errors

- **Error**: Passing a non-list as the second argument to `*_msg/2`.
  **Correction**: The second argument must always be a list of terms, one per format specifier.

# Common Confusions

- **Confusion**: Thinking `error_logger` is only for errors.
  **Clarification**: It handles info and warning messages too, and is the general event sink for the logging system.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1.3 "The standard logging functions." See Table 7.1 for the events these functions generate.

# Verification Notes

- Definition source: Directly adapted from Section 7.1.3 and 7.2.1.
- Confidence rationale: HIGH — the book lists the API functions explicitly with examples.
- Uncertainties: None.
- Cross-reference status: Verified.
