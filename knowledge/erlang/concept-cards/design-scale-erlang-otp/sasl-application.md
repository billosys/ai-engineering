---
# === CORE IDENTIFICATION ===
concept: SASL Application
slug: sasl-application

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "The SASL Application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sasl"
  - "system architecture support libraries"
  - "SASL reports"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - application-environment
  - special-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I monitor a production system and provide preemptive support?"
---

# Quick Definition

SASL (System Architecture Support Libraries) is a standard OTP application — mandatory in any minimal release — that provides release-handling and software-upgrade libraries and an event handler producing supervisor, progress, error, and crash reports.

# Core Definition

SASL stands for system architecture support libraries; the SASL application (`sasl`) is a container for useful items needed in large-scale software design (Cesarini & Vinoski, p. 228). It is one of the mandatory applications — along with `kernel` and `stdlib` — required in a minimal OTP release, because it contains the common library modules used for release handling and software upgrades. SASL also starts an event handler that receives *supervisor reports* (a child terminated abnormally), *progress reports* (a child or application started), *error reports* (abnormal behavior termination), and *crash reports* (from processes started with `proc_lib`). Its behavior is controlled by environment variables: `sasl_error_logger`, `errlog_type`, and `utc_log` (pp. 228-231).

# Prerequisites

- **OTP application** — SASL is a standard OTP application.

# Key Properties

1. Mandatory in a minimal OTP release, alongside `kernel` and `stdlib`.
2. Contains library modules for release handling and software upgrades.
3. Provides the alarm handler and a basic CPU-load regulator (`overload`).
4. Starts an event handler producing supervisor, progress, error, and crash reports.
5. Controlled by env variables: `sasl_error_logger` (`tty`, `{file, FileName}`, or `false`), `errlog_type` (`error`/`progress`/`all`), `utc_log`.
6. SASL reports appear only when `sasl` is started and `sasl_error_logger` is not `false`.

# Construction / Recognition

## To Construct/Create:
1. Nothing to build — `sasl` ships with the standard distribution.
2. Start it with `application:start(sasl)` (or include it in the boot script).
3. Configure its reports via env variables in a `.config` file.

## To Identify/Recognize:
1. The `sasl` application in `application:which_applications()`.
2. Supervisor/progress/error/crash reports printed to the shell or a log file.

# Context & Application

- **Typical contexts**: Every OTP release; release handling and software upgrades.
- **Common applications**: Monitoring supervision-tree activity; logging crash reports.
- **Historical/stylistic notes**: The book defers full release and upgrade coverage to Chapters 11 and 12, focusing here on the SASL reports (p. 228).

# Examples

**Example 1** (pp. 210-211): Loading and starting `sasl`, which prints a long list of progress reports as its supervision tree starts.

**Example 2** (p. 231): A config file setting `sasl_error_logger` to `{file, "SASLlogs"}` and `utc_log` to `true`, storing all SASL reports to a file.

## Worked Example

A config file directing SASL reports to a file (p. 231):

```erlang
[{sasl, [{sasl_error_logger, {file, "SASLlogs"}},
         {utc_log, true}]},
 {bsc,  [{frequencies, [1,2,3,4,5,6]}]}].
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Application environment** — SASL's behavior is controlled through its environment variables.
- **Special process** — Crash reports are issued by processes started with `proc_lib`, the basis of special processes.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Expecting SASL reports without starting the `sasl` application.
  **Correction**: Reports appear only when `sasl` is running and `sasl_error_logger` is not set to `false`.

- **Error**: Starting an application that depends on `sasl` before `sasl` itself.
  **Correction**: Start `sasl` first, or use `application:ensure_all_started/1`.

# Common Confusions

- **Confusion**: Thinking SASL only handles releases and upgrades.
  **Clarification**: It also provides the alarm handler, a basic CPU-load regulator, and the event handler that produces supervisor/progress/error/crash reports.

# Source Reference

Chapter 8: Applications, "The SASL Application," pages 228-231.

# Verification Notes

- Definition source: Direct adaptation from pp. 228-231.
- Confidence rationale: HIGH — explicitly defined with the report types and env variables enumerated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
