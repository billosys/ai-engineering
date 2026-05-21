---
# === CORE IDENTIFICATION ===
concept: Logger
slug: logger

# === CLASSIFICATION ===
category: production-ops
subcategory: logging
tier: intermediate

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
  - "Kernel Logger"
  - "logger module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-logging
extends: []
related:
  - otp-behaviour-log-events
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Logger in Erlang/OTP?"
  - "How does Logger relate to SASL error logging?"
---

# Quick Definition

Logger is the logging facility in the Erlang/OTP Kernel application that handles error information from the runtime system and provides a user interface for configuring log output, destinations, and formatting.

# Core Definition

As stated in the OTP System Principles: "The error information is handled by Logger, which is part of the Kernel application." The source further describes: "The system can be configured so that log events are written to file or to the TTY, or both. In addition, user-defined applications can send and format log events using Logger." Logger's user interface is documented in the `logger` manual page and the Logging section of the Kernel User's Guide.

# Prerequisites

- **error-logging** — Logger is the facility that handles error logging in the runtime system

# Key Properties

1. Part of the Kernel application (always available).
2. Handles error information from the runtime system.
3. Configurable output destinations: file, TTY, or both.
4. Provides a user interface for sending and formatting log events.
5. Supports a primary log level that controls which events are logged.
6. User-defined applications can send their own log events through Logger.
7. Replaces the older SASL-dependent error logging (prior to OTP 21.0).

# Construction / Recognition

## To Construct/Create:
1. Logger is started automatically as part of the Kernel application — no manual setup required.
2. Configure via Kernel configuration parameters (e.g., `logger_level`).
3. Add log handlers to direct output to files or other destinations.
4. Use the `logger` module API to send log events from application code.

## To Identify/Recognize:
1. Log output produced by the runtime system or OTP behaviours is handled by Logger.
2. The `logger` module provides the programmatic interface.
3. Configuration is done via Kernel application parameters.

# Context & Application

Logger is the central logging facility in modern Erlang/OTP (OTP 21.0+). It replaced the older approach where supervisor reports, crash reports, and progress reports were only logged when the SASL application was running. The SASL-compatible behaviour can still be enabled for backwards compatibility by setting the Kernel configuration parameter `logger_sasl_compatible` to `true`. In production systems, Logger is configured with appropriate handlers to write structured logs to files, with log rotation and filtering.

# Examples

**Example 1** (Error Logging, "Error Information From the Runtime System"): Enabling info-level logging to see progress reports:
```text
% erl -kernel logger_level info
```

**Example 2** (Error Logging, "Log events from OTP behaviours"): For backwards compatibility with pre-OTP 21.0 behaviour, the Kernel configuration parameter `logger_sasl_compatible` can be set to `true`.

# Relationships

## Builds Upon
- **error-logging** — Logger is the facility that handles runtime error information

## Enables
- **otp-behaviour-log-events** — OTP behaviour log events are sent through Logger
- Log analysis and monitoring in production systems

## Related
- **otp-behaviour-log-events** — standard behaviours send progress and error information to Logger
- **SASL** — Logger replaced SASL-dependent logging as of OTP 21.0

## Contrasts With
- No direct contrast in source (the older SASL-based approach is mentioned as a predecessor, not a current alternative).

# Common Errors

- **Error**: Expecting supervisor and crash reports to require SASL to be running (pre-OTP 21.0 assumption).
  **Correction**: Since OTP 21.0, Logger in the Kernel application handles these reports. SASL is no longer required for basic error logging.

# Common Confusions

- **Confusion**: Conflating Logger with the older SASL error logging.
  **Clarification**: Prior to OTP 21.0, supervisor, crash, and progress reports were only logged when the SASL application was running. Since OTP 21.0, Logger (in Kernel) handles these by default. The old behaviour can be restored with `logger_sasl_compatible` set to `true`.

# Source Reference

"Error Information From the Runtime System" and "Log events from OTP behaviours" sections, "Error Logging" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Directly stated in source text, supplemented with details from the OTP behaviours section.
- Confidence rationale: High — explicitly named and described with configuration examples.
- Uncertainties: None.
- Cross-reference status: References error-logging, otp-behaviour-log-events (cards in this extraction).
