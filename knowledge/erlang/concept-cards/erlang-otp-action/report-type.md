---
# === CORE IDENTIFICATION ===
concept: Report Type
slug: report-type

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "user-defined report type"
  - "log report type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-logger
extends: []
related:
  - error-logger-events
  - sasl
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a report type in Erlang logging?"
  - "How do applications define their own report types?"
---

# Quick Definition

A report type is a tag attached to a log report that classifies it; standard reports use `std_error`, `std_warning`, or `std_info`, while applications can define their own type tags that the system ignores unless a handler acts on them.

# Core Definition

A report type is a classifying tag carried by report-style log events. The modern `error_logger` functions `error_report/2`, `warning_report/2`, and `info_report/2` accept a `Type` argument in addition to the report term. When a report function is called without a specified type, the type field defaults to `std_error`, `std_warning`, or `std_info` respectively. Any other type identifier may be used for user-defined report types. The key property of user-defined report types is that the system ignores them unless an event handler has been added to act on them — this is exactly how SASL works: applications define their own report types, and SASL adds a handler for the OTP behaviour reports (Ch. 7, Sections 7.1.3 and 7.2.3).

# Prerequisites

- **error_logger** — Report types are a feature of the `error_logger` report functions.

# Key Properties

1. A tag classifying a log report.
2. Standard untyped reports get `std_error`, `std_warning`, or `std_info`.
3. Applications may use any other identifier as a custom type.
4. User-defined report types are ignored unless a handler acts on them.
5. The `Type` field appears in `*_report` event tuples.

# Construction / Recognition

## To Use a Custom Report Type:
1. Call `error_logger:info_report(Type, Report)` (or `error_report`/`warning_report`) with your own `Type` atom.
2. Add a `gen_event` handler that matches that `Type` in `handle_event/2`.

## To Recognize:
1. The middle element of a `*_report` event tuple is the report type.

# Context & Application

- **Typical contexts**: Extending logging with application-specific structured reports.
- **Common applications**: SASL's behaviour reports; custom diagnostic categories.
- **Historical/stylistic notes**: The standard `error_logger` API has only three severity levels, but report types let applications add their own categories.

# Examples

**Example 1** (Section 7.2.3): For `error_report`, `warning_report`, or `info_report` events, the type field is `std_error`, `std_warning`, or `std_info` if the report function was called without a specified type.

**Example 2** (Section 7.1.4): SASL adds report types and a handler for supervisor and crash reports — reports the system would otherwise ignore.

# Relationships

## Builds Upon
- **error_logger** — Report functions carry the type tag.

## Enables
- None.

## Related
- **error-logger-events** — The `Type` field is part of `*_report` event tuples.
- **SASL** — Adds report types and the handler that acts on them.

## Contrasts With
- None.

# Common Errors

- **Error**: Emitting a custom report type but never adding a handler for it.
  **Correction**: Define a handler that matches the type, or the report is silently ignored.

# Common Confusions

- **Confusion**: Thinking report types are the same as severity levels.
  **Clarification**: Severity is error/warning/info; report type is an orthogonal classification tag.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Sections 7.1.3 "The standard logging functions" and 7.2.3 "Acting on error events."

# Verification Notes

- Definition source: Synthesized from Sections 7.1.3 and 7.2.3.
- Confidence rationale: MEDIUM — the concept is described and used but not given a single formal definition.
- Uncertainties: None.
- Cross-reference status: Verified.
