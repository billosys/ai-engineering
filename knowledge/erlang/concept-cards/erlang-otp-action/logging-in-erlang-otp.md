---
# === CORE IDENTIFICATION ===
concept: Logging in Erlang/OTP
slug: logging-in-erlang-otp

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
section: "7.1 Logging in Erlang/OTP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang/OTP logging system"
  - "OTP logging facilities"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - gen-server
extends: []
related:
  - error-logger
  - sasl
  - gen-event
  - severity-level
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What logging facilities does Erlang/OTP provide?"
  - "Should I use Erlang's native logging system or an external one?"
  - "What are the building blocks of the OTP logging system?"
---

# Quick Definition

Erlang/OTP ships built-in logging facilities — the `error_logger` module, the SASL application, and the `gen_event` event-handling infrastructure — that together let an application emit, route, and act on log messages and events.

# Core Definition

Logging in Erlang/OTP is provided by three cooperating pieces: the `error_logger` module in the `kernel` application (the basic logging API), the SASL application (which adds extended logging for OTP behaviours such as supervisor progress reports and crash reports), and the `gen_event` behaviour, which is the event-handling framework the whole logging system is built on. Together they give a way to emit log messages and a framework for doing custom logging and event handling in general (Ch. 7, "Logging in Erlang/OTP"). The native log format is unusual and not directly consumable by common log-parsing tools, so the choice of whether to use it depends on whether the system is a new OTP-based system or must fit into existing non-Erlang infrastructure.

# Prerequisites

- **OTP application** — SASL and the logger are applications that must be started; understanding the application concept frames how logging fits in.
- **gen_server** — The behaviour-based processes whose crashes the logging system reports; the standard error reports come from such processes.

# Key Properties

1. The primary logging API is the `error_logger` module, part of the `kernel` application.
2. Extended logging for OTP behaviours is provided by the SASL application.
3. The event-handling framework underneath uses the `gen_event` behaviour.
4. Standard log messages are always available in any Erlang system; behaviour reports require SASL or another handler.
5. The default log format is non-standard and not directly parseable by external tools.

# Construction / Recognition

## To Use the Logging System:
1. Call `error_logger` functions (`error_msg`, `warning_msg`, `info_msg`) to emit messages.
2. Start the SASL application (`application:start(sasl)`) to get supervisor progress reports and crash reports.
3. Optionally add a custom `gen_event` handler to reformat or redirect log events.

## To Recognize:
1. Console output prefixed with `=ERROR REPORT====`, `=INFO REPORT====`, or `=CRASH REPORT====` headings with timestamps indicates the OTP logger at work.

# Context & Application

- **Typical contexts**: Any production OTP system that needs visibility into what its processes, supervisors, and workers are doing.
- **Common applications**: Emitting application log messages, capturing crash diagnostics, building custom event streams.
- **Historical/stylistic notes**: The decision to use the native logger vs. an external system depends on the surrounding infrastructure.

# Examples

**Example 1** (Section 7.1, motivating discussion): The Simple Cache application has supervisors, workers, leases timing out, and tables being manipulated, yet a user has "no simple way to find out more" — motivating the addition of logging.

**Example 2** (Section 7.1.3): `error_logger:info_msg("This is a message~n")` prints a timestamped `=INFO REPORT====` heading followed by the message.

# Relationships

## Builds Upon
- **gen_event** — The event-handling framework on which the logging system is built.

## Enables
- **error-logger** — The concrete logging API module.
- **sasl** — Adds crash and progress reports on top of the base logger.

## Related
- **Severity level** — Logging systems classify messages by importance.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting the native log format to be parseable by tools like log4j-style parsers.
  **Correction**: The format is non-standard; add a custom `gen_event` handler to emit a compatible format if needed.

# Common Confusions

- **Confusion**: Believing logging requires an external library.
  **Clarification**: Logging is built into the standard Erlang/OTP distribution via `error_logger`, SASL, and `gen_event`.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1 "Logging in Erlang/OTP."

# Verification Notes

- Definition source: Synthesized from Section 7.1 and 7.1.2.
- Confidence rationale: HIGH — the book explicitly enumerates the three facilities and their roles.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this chapter.
