---
# === CORE IDENTIFICATION ===
concept: Report Browser (rb module)
slug: report-browser

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
section: "Analyzing the Errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rb module"
  - "rb"
  - "report browser tool"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-logger
  - rotating-log
extends: []
related:
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rb module?"
  - "How do I read and analyze the OTP error logs?"
---

# Quick Definition

The report browser (`rb`) is the OTP module for reading the error logs. You start it with `rb:start/0,1`, list entries with `rb:list/0`, show one with `rb:show/1`, and search with `rb:grep/1`.

# Core Definition

"Reading the error logs is the responsibility of the `rb` module. It has an extremely simple interface" (Programming Erlang, "Analyzing the Errors"). To use it, Erlang must first be started with the correct configuration file so the error logs can be located; then `rb:start(Options)` starts the report browser (e.g. `rb:start([{max,20}])` reads the last twenty entries). `rb:list()` lists the entries with their number, type, process, and timestamp; `rb:show(N)` displays entry number `N`; `rb:grep(RegExp)` finds all reports matching a regular expression. The `rb` module also has functions to select specific error types and extract them to a file, so log analysis can be fully automated.

# Prerequisites

- **The error logger** — `rb` reads the output the error logger produces.
- **Rotating log** — `rb` typically reads entries from a configured rotating log.

# Key Properties

1. `rb:start(Options)` — starts the report browser; `{max, N}` limits how many entries to read.
2. `rb:list()` — lists log entries by number, type, process, date, and time.
3. `rb:show(N)` — displays the full content of entry `N`.
4. `rb:grep(RegExp)` — finds all reports matching a regular expression.
5. `rb:help()` — prints usage information.
6. Can select specific error types and extract them to a file, enabling automated analysis.

# Construction / Recognition

## To Use the Report Browser:
1. Start Erlang with the same `-config` file that locates the error logs.
2. Run `rb:start([{max, N}])` to read the last `N` entries.
3. Run `rb:list()` to see the entries.
4. Run `rb:show(N)` to inspect a specific entry, or `rb:grep(RegExp)` to search.

## To Recognize:
1. Shell interaction with `rb:start`, `rb:list`, `rb:show` indicates error-log analysis with the report browser.

# Context & Application

- **Typical contexts**: Post-mortem investigation of errors in a production OTP system.
- **Common applications**: In the `sellaprime` system, `rb:show(5)` reveals a `CRASH REPORT` for the `area_server` with the `function_clause` error and a full process snapshot.
- **Historical/stylistic notes**: The book recommends spending time interacting with `rb` to learn what it can do, and notes that error-log analysis can be fully automated.

# Examples

**Example 1** ("Analyzing the Errors"): `rb:start([{max,20}])` followed by `rb:list()` lists log entries; `rb:show(8)` displays the entry produced by `error_logger:error_msg/1`.

**Example 2** ("Starting the System"): `rb:show(5)` shows a `CRASH REPORT` for `area_server`, including its `error_info` (`{function_clause, ...}`), `ancestors`, `links`, `heap_size`, and `reductions`.

# Relationships

## Builds Upon
- **The error logger** — `rb` reads the logs the error logger writes.
- **Rotating log** — `rb` typically reads entries from a rotating log.

## Enables
- (No further concepts in this chapter build on `rb`.)

## Related
- **Supervisor** — crash and supervisor reports, viewed via `rb`, are produced when supervised processes fail.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Starting `rb` without the configuration file that locates the error logs.
  **Correction**: Start Erlang with the same `-config` file used when the logs were written, so `rb` can find them.

- **Error**: Trying to delete old error reports manually.
  **Correction**: There is no need — the rotating log deletes old entries; `rb` simply reads what remains.

# Common Confusions

- **Confusion**: Thinking `rb` writes log entries.
  **Clarification**: `rb` only *reads* and analyzes logs; the error logger writes them.

- **Confusion**: Believing `rb` shows live errors as they happen.
  **Clarification**: `rb` reads stored log entries; `rb:start` snapshots a fixed number of past reports.

# Source Reference

Chapter 23: Making a System with OTP, section "Analyzing the Errors" and "Reading the Log"; also used in "Starting the System". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "Analyzing the Errors".
- Confidence rationale: HIGH — the `rb` interface is explicitly described and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
