---
# === CORE IDENTIFICATION ===
concept: The Error Logger
slug: error-logger

# === CLASSIFICATION ===
category: error-handling
subcategory: logging
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Error Logger"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error_logger"
  - "OTP error logger"
  - "SASL error logging"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - otp
extends: []
related:
  - rotating-log
  - report-browser
  - alarm-management
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OTP error logger?"
  - "How do I log and analyze errors in an OTP system?"
---

# Quick Definition

The error logger is the customizable OTP subsystem for recording errors, warnings, and informational messages. Programmers call `error_logger:error_msg/1,2` and `error_logger:error_report/1`; configuration decides where the entries are stored.

# Core Definition

"The OTP system comes packaged with a customizable error logger" (Programming Erlang, "The Error Logger"). It can be seen from three points of view: the *programmer view* (the function calls used to log an error), the *configuration view* (where and how the logger stores its data), and the *report view* (analysis of errors after the fact). The programmer API includes `error_logger:error_msg(String)`, `error_logger:error_msg(Format, Data)` (arguments like `io:format`), and `error_logger:error_report(Report)`. The error logger produces supervisor reports, progress reports, and crash reports automatically, plus error/warning/info reports the programmer raises explicitly. It is configured via configuration files and chosen by the boot argument (`erl -boot start_sasl` for a production environment).

# Prerequisites

- **gen_event** — the error logger infrastructure follows the gen_event pattern, with installable handlers.
- **OTP** — the error logger is a packaged OTP subsystem.

# Key Properties

1. Three views: programmer (API calls), configuration (storage), report (analysis).
2. Programmer API: `error_msg/1`, `error_msg/2`, `error_report/1` (this is a subset).
3. Automatic reports: supervisor reports, progress reports, crash reports — produced without programmer action.
4. Explicit reports: error, warning, informational — tags with no semantic meaning, used to classify entries.
5. Started via boot argument: `erl -boot start_clean` (development) or `erl -boot start_sasl` (production); SASL handles error logging, overload protection.
6. Storage is configurable: shell only, single text file, or a rotating log.

# Construction / Recognition

## To Use the Error Logger:
1. Start Erlang with `erl -boot start_sasl` and a `-config` file for production logging.
2. In code, call `error_logger:error_msg("...")` or `error_logger:error_msg(Format, Data)` to record an error.
3. Configure where output goes via a `.config` file's `sasl` section.
4. Analyze stored errors later with the `rb` (report browser) module.

## To Recognize:
1. `=ERROR REPORT====` lines in the shell are error logger output.
2. Calls to `error_logger:error_msg` are programmer-raised log entries.

# Context & Application

- **Typical contexts**: Production OTP systems where errors must be recorded and later investigated.
- **Common applications**: `my_alarm_handler` calls `error_logger:error_msg("*** Tell the Engineer to turn on the fan~n")`; the `sellaprime` system logs all server crashes.
- **Historical/stylistic notes**: "The error logger described here has been run for years in live products."

# Examples

**Example 1** ("Logging an Error"): `error_logger:error_msg("An error has occurred\n").` produces an `=ERROR REPORT====` entry with a timestamp in the shell.

**Example 2** ("Logging an Error"): `error_logger:error_report([{tag1,data1},a_term,{tag2,data}]).` produces a structured report listing `tag1: data1`, `a_term`, `tag2: data`.

# Relationships

## Builds Upon
- **gen_event** — the error logger is built on the generic event handler infrastructure.

## Enables
- **Rotating log** — one of the storage configurations for the error logger.
- **Report browser** — the `rb` module reads and analyzes error logger output.

## Related
- **Alarm management** — the alarm handler reports through the error logger.
- **Supervisor** — supervisor and crash reports are produced automatically by the error logger.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Expecting `error_logger:error_msg` output to be saved with only the `elog2` (single-file) configuration.
  **Correction**: That configuration saves only progress reports; programmer error messages need a rotating log configuration.

- **Error**: Running a production system with `erl -boot start_clean`.
  **Correction**: Use `erl -boot start_sasl` so SASL provides full error logging and overload protection.

# Common Confusions

- **Confusion**: Thinking error/warning/info tags carry runtime semantics.
  **Clarification**: "These three terms have no semantic meaning; they are merely tags used by the programmer" to classify log entries.

- **Confusion**: Believing supervisor and crash reports must be coded by hand.
  **Clarification**: They are produced automatically "without the programmer having to do anything."

# Source Reference

Chapter 23: Making a System with OTP, section "The Error Logger" (subsections "Logging an Error", "Configuring the Error Logger", "Analyzing the Errors"). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "The Error Logger".
- Confidence rationale: HIGH — the source explicitly defines the error logger and its three views.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
