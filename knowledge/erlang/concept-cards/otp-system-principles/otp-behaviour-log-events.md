---
# === CORE IDENTIFICATION ===
concept: OTP Behaviour Log Events
slug: otp-behaviour-log-events

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
section: "Log events from OTP behaviours"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OTP progress reports"
  - "OTP error reports"
  - "behaviour log events"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logger
  - error-logging
extends: []
related:
  - supervisor-behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I enable progress reports from OTP behaviours?"
  - "What log events do OTP behaviours generate?"
  - "How does Logger relate to SASL error logging?"
---

# Quick Definition

OTP behaviour log events are progress reports, supervisor reports, crash reports, and other error/information reports that the standard OTP behaviours (supervisor, gen_server, etc.) send to Logger during normal operation and failure scenarios.

# Core Definition

As stated in the OTP System Principles: "The standard behaviours (`supervisor`, `gen_server`, and so on) send progress and error information to Logger. Progress reports are by default not logged, but can be enabled by setting the primary log level to `info`, for example by using the Kernel configuration parameter `logger_level`." Supervisor reports, crash reports, and other error and information reports are logged by default through the log handler set up when the Kernel application is started.

# Prerequisites

- **logger** — OTP behaviour log events are sent through the Logger facility
- **error-logging** — this concept extends the general error logging infrastructure to OTP-specific events

# Key Properties

1. Standard behaviours (`supervisor`, `gen_server`, etc.) send log events to Logger.
2. Progress reports are generated but **not logged by default** — they require `info` log level.
3. Supervisor reports and crash reports **are** logged by default.
4. Progress reports can be enabled via `-kernel logger_level info`.
5. Prior to OTP 21.0, these reports required the SASL application to be running.
6. The old SASL-dependent behaviour can be restored with `logger_sasl_compatible` set to `true`.
7. The log handler is set up when the Kernel application starts.

# Construction / Recognition

## To Construct/Create:
1. Use OTP behaviours (supervisor, gen_server, etc.) — they automatically generate log events.
2. To see progress reports, set the primary log level to `info`:
   ```text
   erl -kernel logger_level info
   ```
3. Supervisor reports and crash reports appear at the default log level.

## To Identify/Recognize:
1. Progress reports appear with the format `=PROGRESS REPORT====` followed by a timestamp.
2. They contain details such as `application: started_at:` or `supervisor: started:` with child spec details.
3. Error and crash reports use `=ERROR REPORT====` or `=CRASH REPORT====` format.

# Context & Application

OTP behaviour log events are essential for understanding system startup, supervision activity, and failure handling. Progress reports show which applications and supervisor children have started, making them invaluable for debugging startup issues. Crash reports provide detailed information about why supervised processes failed. In production, these events are typically captured by Logger handlers configured to write to files with appropriate log levels and filtering.

# Examples

**Example 1** (Error Logging, "Log events from OTP behaviours"): Enabling progress reports and viewing application startup:
```text
% erl -kernel logger_level info
Erlang/OTP 21 [erts-10.0] [source-13c50db] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [hipe]

=PROGRESS REPORT==== 8-Jun-2018::16:54:19.916404 ===
    application: kernel
    started_at: nonode@nohost
=PROGRESS REPORT==== 8-Jun-2018::16:54:19.922908 ===
    application: stdlib
    started_at: nonode@nohost
```

**Example 2** (Error Logging, "Log events from OTP behaviours"): Supervisor child start progress report:
```text
=PROGRESS REPORT==== 8-Jun-2018::16:54:19.925755 ===
    supervisor: {local,kernel_safe_sup}
    started: [{pid,<0.74.0>},
              {id,disk_log_sup},
              {mfargs,{disk_log_sup,start_link,[]}},
              {restart_type,permanent},
              {shutdown,1000},
              {child_type,supervisor}]
```

# Relationships

## Builds Upon
- **logger** — all OTP behaviour log events are sent through Logger
- **error-logging** — extends the general error logging concept to OTP-specific structured events

## Enables
- Production debugging — progress reports reveal system startup sequence and supervision structure
- Failure analysis — crash reports and supervisor reports detail why and how processes failed

## Related
- **supervisor-behaviour** — supervisors generate progress reports when children start and error reports on child failures

## Contrasts With
- No direct contrast in source.

# Common Errors

- **Error**: Expecting to see progress reports at the default log level.
  **Correction**: Progress reports require setting the primary log level to `info` (e.g., `-kernel logger_level info`). They are not logged by default.

- **Error**: Starting the SASL application just to get supervisor and crash reports (pre-OTP 21.0 habit).
  **Correction**: Since OTP 21.0, supervisor and crash reports are handled by Logger in the Kernel application. SASL is no longer required.

# Common Confusions

- **Confusion**: Thinking all OTP behaviour log events are suppressed by default.
  **Clarification**: Only progress reports are suppressed by default. Supervisor reports, crash reports, and other error/information reports are logged by default through the log handler set up at Kernel startup.

- **Confusion**: Thinking the OTP 21.0 Logger change is backwards-incompatible with no migration path.
  **Clarification**: The old SASL-dependent behaviour can be restored by setting the Kernel configuration parameter `logger_sasl_compatible` to `true`.

# Source Reference

"Log events from OTP behaviours" section, "Error Logging" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Directly quoted from source text with full example output.
- Confidence rationale: High — explicit description with concrete configuration and output examples.
- Uncertainties: None.
- Cross-reference status: References logger, error-logging (cards in this extraction), supervisor-behaviour (external card).
