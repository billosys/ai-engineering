---
# === CORE IDENTIFICATION ===
concept: Error Handling Philosophy (Concurrent)
slug: error-handling-philosophy

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: error-philosophy
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Error Handling Philosophy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "remote detection and handling of errors"
  - "let some other process fix the error"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - link
  - monitor
extends: []
related:
  - let-it-crash
  - exit-signal
  - supervisor
contrasts_with:

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between error handling in sequential and concurrent programs?"
  - "How do links relate to process supervision?"
  - "What foundational concepts underpin error handling?"
---

# Quick Definition

The Erlang concurrent error-handling philosophy is based on remote detection and handling of errors: instead of fixing an error in the process where it occurs, you let that process die and correct the error in some other, observing process.

# Core Definition

Error handling in concurrent Erlang programs is based on the idea of *remote detection and handling of errors*. When designing a fault-tolerant system, you assume errors will occur, processes will crash, and machines will fail; the job is to detect errors after they occur and correct them so that users notice no failure or loss of service. Because the work concentrates on cure rather than prevention, systems carry very little defensive code and instead carry code to clean up after errors. The philosophy is summed up in two phrases: "Let some other process fix the error" and "Let it crash" (Chapter 13, "Error Handling Philosophy"). Detecting errors and finding out why something failed is built into the Erlang VM at a very low level; building groups of processes that observe each other and take corrective action is provided by the OTP libraries (the supervision tree).

# Prerequisites

- **Process** — Remote handling assumes many processes, so the death of one is not catastrophic.
- **Link** — One mechanism by which one process observes another's health.
- **Monitor** — The unidirectional alternative for one process to observe another.

# Key Properties

1. Errors are handled remotely, in a process other than the one where the error occurred.
2. Fault tolerance assumes errors *will* occur — design for cure, not prevention.
3. Observing processes work transparently across machine boundaries.
4. A genuinely fault-tolerant system needs at least two machines, since one whole machine may crash.
5. The language provides the low-level detection mechanism; OTP provides the supervision structure.

# Construction / Recognition

## To Apply the Philosophy:
1. Write problem-solving code with minimal defensive checks.
2. Arrange processes to monitor each other for health, using links or monitors.
3. When a process dies, have the observing process perform corrective action.
4. For real fault tolerance, spread observing processes across multiple machines.

## To Recognize It:
1. Look for paired observer processes rather than inline error handling.
2. Look for cross-machine links/monitors guarding critical processes.

# Context & Application

- **Typical contexts**: All fault-tolerant Erlang/OTP systems.
- **Common applications**: Database transaction rollback; OS-style resource cleanup after a process crash.
- **Historical/stylistic notes**: The chapter frames this as an extension of sequential error handling (Chapter 6) to the concurrent world — if a `catch`/`try` fails or the whole machine fails, "let some other process fix the error."

# Examples

**Example 1** (Chapter 13, "Let Some Other Process Fix the Error"): Processes are arranged to monitor each other; if one dies, another observes this and performs corrective actions. The book's analogy: if you need surgery you go to a doctor rather than operate on yourself.

**Example 2** (Chapter 13, sidebar "Getting Some Other Guy to Fix It"): Trivial faults can be fixed locally with `catch`/`try`; if that fails and something big goes wrong, the process should crash and let some other process fix the error.

# Relationships

## Builds Upon
- **Process** and **link**/**monitor** — the mechanisms that make remote handling possible.

## Enables
- **Supervisor** — the OTP structure that operationalizes this philosophy.

## Related
- **Let it crash** — the companion phrase; the crashing half of the philosophy.
- **Exit signal** — the propagation mechanism that informs observers.

## Contrasts With
- **Defensive programming** — focuses on prevention within one process; this philosophy focuses on remote cure.

# Common Errors

- **Error**: Trying to build a fault-tolerant system on a single machine.
  **Correction**: Use at least two machines so an observer survives if the first machine crashes.
- **Error**: Handling every error inside the failing process.
  **Correction**: Let the process die and correct the error in an observing process.

# Common Confusions

- **Confusion**: Fault tolerance means errors never happen.
  **Clarification**: Fault tolerance assumes errors *will* happen and focuses on detection and correction.
- **Confusion**: This philosophy is purely an OTP library concern.
  **Clarification**: The detection primitive is in the language/VM; OTP only provides the higher-level supervision structure.

# Source Reference

Chapter 13: Errors in Concurrent Programs, section "Error Handling Philosophy" and its subsections "Let Some Other Process Fix the Error" and "Let It Crash," plus the sidebar "Getting Some Other Guy to Fix It."

# Verification Notes

- Definition source: Direct adaptation of the "Error Handling Philosophy" section.
- Confidence rationale: HIGH — the philosophy is explicitly stated and named in the source.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards and canonical `process`/`link`/`monitor`/`supervisor`.
- Re-extraction notes: Fresh extraction; no pre-existing card.
