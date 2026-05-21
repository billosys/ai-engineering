---
# === CORE IDENTIFICATION ===
concept: Error Report
slug: error-report

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
section: "7.1.4 SASL and crash reports"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "ERROR REPORT"
  - "generic server termination report"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-logger
extends: []
related:
  - gen-server
  - sasl
contrasts_with:
  - crash-report

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an error report?"
  - "What does the standard error report show when a gen_server terminates?"
---

# Quick Definition

An error report is the standard, concise diagnostic the Erlang error logger emits when a behaviour-based process terminates abnormally, showing the server name, last message, state, and termination reason.

# Core Definition

An error report is the `=ERROR REPORT====` record produced by the base `error_logger` (without SASL) when a behaviour-based process such as a `gen_server` terminates abnormally. It is concise: it names the terminating generic server, the last message it received, the server state at the time, and the reason for termination (the exception and its stack trace). Error reports are always available in any Erlang system; the richer crash report is an additional record produced only when SASL is running (Ch. 7, Section 7.1.4).

# Prerequisites

- **error_logger** — Error reports are emitted by the `error_logger` infrastructure.

# Key Properties

1. Emitted under an `=ERROR REPORT====` heading with a timestamp.
2. Available without SASL, in any Erlang system.
3. For a `gen_server` termination, shows the server name, last message, state, and reason.
4. Concise compared to the SASL crash report.

# Construction / Recognition

## To Obtain an Error Report:
1. Run a behaviour-based process; when it terminates abnormally, the error report is emitted automatically.

## To Recognize:
1. Look for `=ERROR REPORT====` followed by lines like `** Generic server ... terminating` and `** Reason for termination ==`.

# Context & Application

- **Typical contexts**: Any OTP system, even without SASL started.
- **Common applications**: Basic visibility into behaviour-process failures.
- **Historical/stylistic notes**: The book contrasts the error report (always present) with the SASL crash report (added detail).

# Examples

**Example 1** (Section 7.1.4): `die_please:start_link()` crashing yields an `=ERROR REPORT====` reading `** Generic server die_please terminating`, `** Last message in was timeout`, `** When Server state == {state}`, and a `Reason for termination` block with the `badmatch`.

# Relationships

## Builds Upon
- **error_logger** — The error logger emits error reports.

## Enables
- None.

## Related
- **gen_server** — Behaviour servers produce error reports on abnormal termination.
- **SASL** — Adds the companion crash report.

## Contrasts With
- **crash-report** — The crash report is the richer SASL-produced companion; the error report is the always-present concise version.

# Common Errors

- **Error**: Assuming the error report includes full process detail like ancestors and memory stats.
  **Correction**: That detail is in the SASL crash report; the error report is intentionally concise.

# Common Confusions

- **Confusion**: Thinking error reports require SASL.
  **Clarification**: Error reports are always available; only crash reports need SASL.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1.4 "SASL and crash reports," subsection "Basic error reports."

# Verification Notes

- Definition source: Synthesized from the error report examples in Section 7.1.4.
- Confidence rationale: MEDIUM — shown by example and contrasted with crash reports, but not given a formal standalone definition.
- Uncertainties: None.
- Cross-reference status: Verified.
