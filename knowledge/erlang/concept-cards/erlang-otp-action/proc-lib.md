---
# === CORE IDENTIFICATION ===
concept: proc_lib
slug: proc-lib

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-startup
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
  - "proc_lib module"
  - "proc_lib:spawn"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - crash-report
  - sasl
  - otp-behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is proc_lib used for?"
  - "How do I start a non-behaviour process that follows OTP conventions?"
---

# Quick Definition

`proc_lib` is a `stdlib` module that starts processes "the OTP way," setting them up to follow the conventions behaviours rely on — most notably so SASL can produce crash reports for them.

# Core Definition

`proc_lib` is a module in the Erlang `stdlib` application that supports starting processes the OTP way, so they are properly set up to follow all the necessary conventions. When a process is started with `proc_lib:spawn/1` instead of plain `spawn/1`, it participates in the OTP infrastructure — for example, SASL will produce a crash report if it dies. Behaviour implementations (`gen_server`, `supervisor`, etc.) already use `proc_lib` internally, so this work is done automatically; `proc_lib` is needed directly only in the (relatively unlikely) case of writing processes that are not built on an existing behaviour (Ch. 7, Section 7.1.4).

# Prerequisites

- **Process** — `proc_lib` is about how processes are spawned and set up; the process concept is foundational to it.

# Key Properties

1. Part of the `stdlib` application.
2. `proc_lib:spawn/1` starts a process with OTP conventions in place.
3. Processes started via `proc_lib` get SASL crash reports on failure.
4. OTP behaviours use `proc_lib` internally — you rarely call it directly.
5. Recommended whenever you write processes not based on a behaviour.

# Construction / Recognition

## To Use proc_lib:
1. Replace `spawn(Fun)` with `proc_lib:spawn(Fun)` when starting a non-behaviour process.
2. The process is now OTP-conventional and will produce a crash report on abnormal exit (with SASL running).

## To Recognize:
1. Non-behaviour code calling `proc_lib:spawn` rather than bare `spawn` signals intent to follow OTP conventions.

# Context & Application

- **Typical contexts**: Writing custom processes outside the standard behaviours.
- **Common applications**: Ensuring custom workers integrate with SASL crash reporting.
- **Historical/stylistic notes**: The book frames direct use of `proc_lib` as uncommon, since behaviours cover most cases.

# Examples

**Example 1** (Section 7.1.4): `spawn(fun die_please2:go/0)` gives little error information on crash, whereas `proc_lib:spawn(fun die_please2:go/0)` produces a full `=CRASH REPORT====`.

# Relationships

## Builds Upon
- **Process** — `proc_lib` governs how processes are spawned.

## Enables
- **crash-report** — `proc_lib`-started processes can be crash-reported by SASL.

## Related
- **SASL** — Reads from processes set up the OTP way.
- **OTP behaviour** — Behaviours use `proc_lib` internally.

## Contrasts With
- None.

# Common Errors

- **Error**: Using plain `spawn` for processes you want SASL to report on.
  **Correction**: Use `proc_lib:spawn` so the process follows OTP conventions.

# Common Confusions

- **Confusion**: Believing you must call `proc_lib` yourself in normal OTP code.
  **Clarification**: Behaviours already do this for you; direct use is only for hand-rolled processes.

# Source Reference

Chapter 7: Logging and event handling the Erlang/OTP way, Section 7.1.4 "SASL and crash reports," subsection "When SASL doesn't help."

# Verification Notes

- Definition source: Synthesized from Section 7.1.4 discussion of `proc_lib`.
- Confidence rationale: MEDIUM — `proc_lib` is described in context but not given a formal standalone definition.
- Uncertainties: The book mentions only `proc_lib:spawn/1`; the module has a broader API not covered here.
- Cross-reference status: Verified.
