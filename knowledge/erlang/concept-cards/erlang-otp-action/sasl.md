---
# === CORE IDENTIFICATION ===
concept: SASL Application
slug: sasl

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "System Architecture Support Libraries"
  - "sasl application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logging-in-erlang-otp
  - error-logger
extends: []
related:
  - crash-report
  - otp-application
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the SASL application?"
  - "What does starting SASL add to the logging system?"
  - "Why does SASL stand for something other than the authentication framework?"
---

# Quick Definition

SASL (System Architecture Support Libraries) is one of the five basic Erlang/OTP applications; among other services it adds an event handler that produces detailed crash reports and supervisor progress reports.

# Core Definition

SASL stands for *System Architecture Support Libraries* and is one of the five basic applications the rest of Erlang/OTP builds on (`erts`, `kernel`, `stdlib`, `sasl`, `compiler`). It is a small collection of important services for system management. With respect to logging, SASL adds a `gen_event` handler to the `error_logger` process that listens for reports sent by the standard OTP behaviours — when supervisors start or restart child processes, when a child dies unexpectedly, or when a behaviour-based process such as a `gen_server` crashes. The book stresses that "OTP SASL isn't SASL": despite the name, it has nothing to do with the SASL authentication framework of RFC 2222 (Ch. 7, Section 7.1.4).

# Prerequisites

- **Logging in Erlang/OTP** — SASL is one of the three logging facilities; the overall system frames its role.
- **error_logger** — SASL adds its report handler to the `error_logger` event manager.

# Key Properties

1. Acronym for System Architecture Support Libraries.
2. One of the five basic OTP applications.
3. Started like any application: `application:start(sasl)`.
4. Adds a handler to `error_logger` for OTP behaviour reports.
5. Produces crash reports and supervisor progress reports.
6. Unrelated to the SASL network-authentication framework.

# Construction / Recognition

## To Use SASL:
1. Call `application:start(sasl)`.
2. Observe additional progress messages as SASL services start.
3. Crash and progress reports now appear when behaviour-based processes fail or supervisors act.

## To Recognize:
1. After SASL starts, a process crash yields a `=CRASH REPORT====` heading with extensive process detail.

# Context & Application

- **Typical contexts**: Any OTP system in development or production where rich crash diagnostics are wanted.
- **Common applications**: Debugging crashes in a live system; observing supervisor restart activity.
- **Historical/stylistic notes**: The book notes SASL was named long before RFC 2222 created the authentication acronym.

# Examples

**Example 1** (Section 7.1.4): Running `die_please:start_link()` without SASL yields only an `=ERROR REPORT====`; after `application:start(sasl)`, the same crash also yields a detailed `=CRASH REPORT====`.

**Example 2** (Section 7.1.4): SASL only adds reports for processes that follow OTP conventions — a plain `spawn`ed process gets no crash report, but a `proc_lib:spawn`ed one does.

# Relationships

## Builds Upon
- **error_logger** — SASL registers its report handler on the `error_logger` event manager.

## Enables
- **crash-report** — SASL is what produces crash reports.

## Related
- **supervisor** — SASL reports supervisor start/restart progress.
- **OTP application** — SASL is itself an application that must be started.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting SASL crash reports for processes started with plain `spawn`.
  **Correction**: SASL only reports for OTP-conventional processes; start non-behaviour processes via `proc_lib`.

# Common Confusions

- **Confusion**: Thinking SASL relates to the SASL authentication standard.
  **Clarification**: In Erlang it means System Architecture Support Libraries — a system-management application.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1.4 "SASL and crash reports," including the sidebar "OTP SASL isn't SASL."

# Verification Notes

- Definition source: Directly adapted from the Section 7.1.4 sidebar and discussion.
- Confidence rationale: HIGH — the book explicitly defines SASL and its role.
- Uncertainties: None.
- Cross-reference status: Verified.
