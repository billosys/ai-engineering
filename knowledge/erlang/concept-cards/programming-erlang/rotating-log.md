---
# === CORE IDENTIFICATION ===
concept: Rotating Log
slug: rotating-log

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
section: "Configuring the Error Logger"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rotating error log"
  - "circular log buffer"
  - "error_logger_mf_dir"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-logger
extends: []
related:
  - report-browser
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a rotating log?"
  - "How do I configure the error logger to store errors over time?"
---

# Quick Definition

A rotating log is a large circular buffer of error-logger files: new messages are appended, and when the log is full the earliest entries are deleted. It is configured by directory, per-file byte size, and maximum file count.

# Core Definition

"You can think of the rotating log as a large circular buffer containing messages produced by the error logger. As new messages come, they are appended to the end of the log, and when the log is full, the earliest entries in the log are deleted" (Programming Erlang, "Configuring the Error Logger"). "You decide how many files the log should occupy and how big each individual log file should be, and the system takes care of deleting old log files and creating new files in a large circular buffer." It is configured in the `sasl` section of a `.config` file via `error_logger_mf_dir` (directory), `error_logger_mf_maxbytes` (bytes per file), and `error_logger_mf_maxfiles` (number of files).

# Prerequisites

- **The error logger** — the rotating log is one of the error logger's storage configurations.

# Key Properties

1. Behaves as a circular buffer — old entries are overwritten when full.
2. Configured by three keys: `error_logger_mf_dir`, `error_logger_mf_maxbytes`, `error_logger_mf_maxfiles`.
3. The system automatically deletes old files and creates new ones.
4. You never need to manually delete error reports — rotation handles it.
5. Sized to retain the last few days or weeks of operations, sufficient for most purposes.
6. Captures programmer error messages (`error_logger:error_msg`), unlike the single-text-file configuration.

# Construction / Recognition

## To Configure a Rotating Log:
1. Create a `.config` file with a `sasl` section.
2. Set `error_logger_mf_dir` to the log directory.
3. Set `error_logger_mf_maxbytes` to the bytes per logfile (e.g. `10485760` for 10 MB).
4. Set `error_logger_mf_maxfiles` to the maximum number of logfiles.
5. Start Erlang with `erl -boot start_sasl -config <file>`.

## To Recognize:
1. A `.config` file containing `error_logger_mf_dir` configures a rotating log.

# Context & Application

- **Typical contexts**: Production systems that must keep a rolling history of errors.
- **Common applications**: `elog3.config` (rotating log plus shell) and `elog4.config` (rotating log, errors only) in the chapter.
- **Historical/stylistic notes**: For a production environment, the book pairs the rotating log with `{errlog_type, error}` so only errors — not progress/info reports — are retained.

# Examples

**Example 1** ("Rotating Log and Shell"): `elog3.config` defines a 10 MB rotating log:

```erlang
%% rotating log and minimal tty
[{sasl, [
  {sasl_error_logger, false},
  {error_logger_mf_dir,"/Users/joe/error_logs"},
  {error_logger_mf_maxbytes,10485760}, % 10 MB
  {error_logger_mf_maxfiles, 10}
]}].
```

**Example 2** ("Production Environment"): `elog4.config` adds `{errlog_type, error}` so the rotating log keeps only error reports.

# Relationships

## Builds Upon
- **The error logger** — the rotating log is a storage mode of the error logger.

## Enables
- **Report browser** — the `rb` module reads entries from the rotating log.

## Related
- **OTP application** — production OTP applications are typically started with a rotating-log `.config` file.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Using the single-text-file configuration and expecting programmer error messages to be saved.
  **Correction**: The single-file config saves only progress reports; use a rotating log to capture `error_logger:error_msg` output.

- **Error**: Sizing the rotating log too small to span the operational review interval.
  **Correction**: Size it to retain the last few days or weeks so errors can be investigated before rotation deletes them.

# Common Confusions

- **Confusion**: Thinking old log files must be manually deleted.
  **Clarification**: "You never need to actually delete an error report, since the rotation mechanism will eventually delete old error logs."

- **Confusion**: Believing the rotating log is one ever-growing file.
  **Clarification**: It is a fixed set of files acting as a circular buffer; total size is bounded by `maxbytes` × `maxfiles`.

# Source Reference

Chapter 23: Making a System with OTP, section "Configuring the Error Logger" (subsections "Rotating Log and Shell", "Production Environment"). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and config code from "Configuring the Error Logger".
- Confidence rationale: HIGH — explicitly defined with worked configuration files.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
