---
# === CORE IDENTIFICATION ===
concept: Program Checks and Panics
slug: program-checks-and-panics

# === CLASSIFICATION ===
category: error-handling
subcategory: program-termination
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Program checks and panics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant checks"
  - "log.Fatal usage"
  - "panic vs log.Fatal"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends:
  - dont-panic
related:
  - when-to-panic
  - logging-errors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use log.Fatal vs panic?"
  - "Should I recover from panics to avoid crashes?"
  - "How should program initialization errors be handled?"
---

# Quick Definition

Libraries should return errors, not abort. Use `log.Fatal` (not panic) for unrecoverable invariant violations in the Google codebase. Do not recover panics to avoid crashes -- this can propagate corrupted state. Program initialization errors should propagate to `main` and use `log.Exit` with actionable messages.

# Core Definition

Standard error handling should use error return values. Libraries should prefer returning errors to the caller rather than aborting, especially for transient errors. When an invariant check fails and internal state is unrecoverable, `log.Fatal` is preferred over `panic` in the Google codebase because `panic` can be unreliable -- deferred functions may deadlock or further corrupt state. Resist recovering panics to avoid crashes: the further from the panic, the less you know about program state (locks held, resources open). Instead, use monitoring to surface unexpected failures. Program initialization errors (bad flags, configuration) should propagate upward to `main`, which calls `log.Exit` with a human-readable, actionable message explaining how to fix the error. `log.Fatal` is generally not appropriate for initialization errors because a stack trace is less useful than an actionable message.

# Prerequisites

(none)

# Key Properties

1. Libraries should return errors, not panic or call log.Fatal
2. `log.Fatal` preferred over `panic` for unrecoverable invariant violations
3. Do not recover panics to avoid crashes -- corrupted state may propagate
4. Program initialization errors should use `log.Exit` with actionable messages
5. `log.Fatal` is not ideal for initialization because stack traces are less helpful than instructions
6. The `net/http` server's panic recovery is considered a historical mistake

# Construction / Recognition

## To Apply:
1. Return errors from library functions for all expected failure modes
2. Use `log.Fatal` only when internal state is unrecoverably corrupt
3. Propagate initialization errors to `main` with `log.Exit`
4. Do not add `recover()` calls to avoid crashes -- fix the bug instead
5. Use monitoring to detect unexpected failures

## To Recognize:
1. Library code that returns errors rather than panicking
2. `log.Fatal` used only for true invariant violations
3. `main` functions that provide actionable error messages on startup failure

# Context & Application

The `net/http` server's practice of recovering panics from request handlers is explicitly called out as a historical mistake by experienced Go engineers. Server logs from other languages commonly show large unhandled stacktraces -- Go code should avoid this pattern. Monitoring tools are preferred over log-based alerting for detecting unexpected failures.

# Examples

**Example 1 -- Program initialization**:

Program initialization errors should propagate to `main`, which calls `log.Exit` with an error that explains how to fix the error. `log.Fatal` should not generally be used because a stack trace is not as useful as a human-generated, actionable message.

# Relationships

## Related
- **when-to-panic** -- Specific cases where panic is appropriate
- **logging-errors** -- General error logging guidance
- **dont-panic** -- The Decisions chapter rule against panics

## Contrasts With
(none)

# Common Errors

- **Error**: Using `panic` instead of `log.Fatal` for invariant violations
  **Correction**: Use `log.Fatal` -- panic may cause deferred functions to deadlock

- **Error**: Using `recover()` to prevent crashes and continue execution
  **Correction**: Do not recover panics; fix the underlying bug and use monitoring

# Common Confusions

- **Confusion**: Thinking `log.Fatal` is appropriate for initialization errors
  **Clarification**: Use `log.Exit` for initialization -- stack traces are less useful than actionable messages

- **Confusion**: Following `net/http`'s panic recovery pattern
  **Clarification**: This is considered a historical mistake; do not replicate it in your servers

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "Program initialization" and "Program checks and panics".

# Verification Notes

- Definition source: Directly from "Program initialization" and "Program checks and panics" sections
- Confidence rationale: HIGH -- explicit guidance with strong recommendations
- Uncertainties: None
- Cross-reference status: References decisions#dont-panic
