---
# === CORE IDENTIFICATION ===
concept: Crash Report
slug: crash-report

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
  - "CRASH REPORT"
  - "SASL crash report"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sasl
extends: []
related:
  - error-logger
  - gen-server
  - proc-lib
contrasts_with:
  - error-report

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a crash report?"
  - "How do I get a crash report for a process that isn't a behaviour?"
  - "What information does a crash report contain?"
---

# Quick Definition

A crash report is a detailed diagnostic record produced by SASL when an OTP-conventional process terminates abnormally; it lists the crasher's pid, initial call, exception, ancestors, links, and memory statistics.

# Core Definition

A crash report is the detailed report SASL generates when a behaviour-based or `proc_lib`-started process dies unexpectedly. While the plain `error_logger` emits a short `=ERROR REPORT====` for a `gen_server` termination, SASL adds a `=CRASH REPORT====` containing much more information about the failed process: its initial call, pid, registered name, the exception, ancestors, queued messages, links, dictionary, `trap_exit` flag, status, and heap/stack/reduction counts, plus a "neighbours" section. This information is valuable when debugging a crash in a live system. Crash reports are produced only for processes that follow OTP conventions — those built on behaviours, or plain processes started via `proc_lib:spawn` (Ch. 7, Section 7.1.4).

# Prerequisites

- **SASL** — Crash reports only appear when the SASL application is running, because SASL installs the handler that produces them.

# Key Properties

1. Emitted under a `=CRASH REPORT====` heading with a timestamp.
2. Produced only when SASL is running.
3. Generated only for OTP-conventional processes (behaviours or `proc_lib`-started).
4. Contains initial call, pid, registered name, exception, ancestors, links, and memory stats.
5. Includes a "neighbours" section describing related processes.

# Construction / Recognition

## To Obtain a Crash Report:
1. Start the SASL application.
2. Build the process on an OTP behaviour, or start it via `proc_lib:spawn/1` rather than plain `spawn/1`.
3. When the process crashes, SASL emits the crash report automatically.

## To Recognize:
1. Look for the `=CRASH REPORT====` heading followed by a `crasher:` block.

# Context & Application

- **Typical contexts**: Debugging failures in running OTP systems.
- **Common applications**: Post-mortem analysis of why a worker or server died.
- **Historical/stylistic notes**: Behaviour code gets crash reporting "for free" because the behaviour does the `proc_lib` setup work.

# Examples

**Example 1** (Section 7.1.4): With SASL running, `die_please:start_link()` crashing on a `badmatch` produces a `=CRASH REPORT====` listing `initial call: die_please:init/1`, the `exception exit`, ancestors, links, and heap/stack sizes.

**Example 2** (Section 7.1.4): A plain `spawn(fun die_please2:go/0)` gives only sparse output, but `proc_lib:spawn(fun die_please2:go/0)` produces a full crash report.

# Relationships

## Builds Upon
- **SASL** — SASL installs the handler that emits crash reports.

## Enables
- None.

## Related
- **error_logger** — Crash reports are SASL-added events alongside standard error reports.
- **gen_server** — Behaviour-based servers automatically produce crash reports on termination.
- **proc_lib** — Lets non-behaviour processes participate in crash reporting.

## Contrasts With
- **error-report** — The short standard error report; the crash report is the richer SASL companion.

# Common Errors

- **Error**: Starting a worker process with plain `spawn` and wondering why no crash report appears.
  **Correction**: Use a behaviour or `proc_lib:spawn` so the process is set up the OTP way.

# Common Confusions

- **Confusion**: Thinking the crash report replaces the error report.
  **Clarification**: Both appear — the error report is emitted, and SASL adds the crash report with extra detail.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1.4 "SASL and crash reports," subsections "Basic error reports," "Starting SASL," and "When SASL doesn't help."

# Verification Notes

- Definition source: Directly adapted from Section 7.1.4 examples.
- Confidence rationale: HIGH — the book shows crash report output explicitly.
- Uncertainties: None.
- Cross-reference status: Verified; `proc-lib` and `error-report` are companion cards in this chapter.
