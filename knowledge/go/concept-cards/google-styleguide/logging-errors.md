---
# === CORE IDENTIFICATION ===
concept: Logging Errors
slug: logging-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-reporting
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Logging errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error logging"
  - "log or return errors"
  - "verbose logging"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adding-information-to-errors
extends: []
related:
  - program-checks-and-panics
  - when-to-panic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I log an error and also return it?"
  - "What log level should I use for errors?"
  - "How should I use verbose logging levels?"
---

# Quick Definition

Log or return an error, but generally not both. Let the caller decide how to handle it. Use `log.Error` sparingly (it is expensive), be careful with PII in logs, and establish conventions for verbose logging levels.

# Core Definition

When a function encounters an error it cannot handle, it should either log it or return it to the caller, but generally not both. Logging and returning creates duplication as the error propagates up the call stack. Returning gives the caller control -- they can log, rate-limit, attempt recovery, or stop the program. Log messages should clearly express what went wrong with relevant diagnostic information, like good test failure messages. Use `log.Error` sparingly because ERROR level causes a flush and has performance impact; prefer it only for actionable issues. Be careful with PII in logs. For verbose logging, establish conventions: `V(1)` for a small amount of extra info, `V(2)` for tracing, `V(3)` for large internal state dumps. Avoid accidentally calling expensive functions when verbose logging is disabled -- use conditional checks like `if log.V(2)` before calling expensive methods.

# Prerequisites

- **adding-information-to-errors** -- How to annotate errors with useful context

# Key Properties

1. Log or return, not both -- avoid duplication up the call stack
2. Returning an error gives the caller control over handling strategy
3. Log messages should be diagnostic and actionable, like good test failure messages
4. `log.Error` is expensive (causes a flush) -- use sparingly, only for actionable issues
5. Be careful with PII in log messages
6. Establish verbose logging level conventions (V(1), V(2), V(3))
7. Guard expensive operations behind `if log.V(level)` checks

# Construction / Recognition

## To Apply:
1. If you return the error, don't log it -- let the caller decide
2. If you must log (e.g., you're the handler), include relevant diagnostic context
3. Reserve ERROR level for actionable failures, not just "more serious" warnings
4. Use `if log.V(2) { log.Infof(..., expensive()) }` pattern to avoid cost when disabled

## To Recognize:
1. Each error is either logged or returned, not both
2. Error logs include actionable diagnostic information
3. Verbose logging uses conditional checks for expensive operations

# Context & Application

The downside of returning errors without logging is that logging uses the caller's line coordinates, not where the error originated. Rate limiting with `rate.Sometimes` can help when logging is necessary at intermediate levels. Within Google, monitoring systems supplement logging for alerting. The `log.V` API has a convenience form that risks accidentally evaluating expensive arguments; the conditional check form is safer.

# Examples

**Example 1 -- Guarding expensive verbose logging**:

```go
// Good:
for _, sql := range queries {
    log.V(1).Infof("Handling %v", sql)
    if log.V(2) {
        log.Infof("Handling %v", sql.Explain())
    }
    sql.Run(...)
}
```

**Example 2 -- Bad: expensive call even when log is disabled**:

```go
// Bad:
// sql.Explain called even when this log is not printed.
log.V(2).Infof("Handling %v", sql.Explain())
```

# Relationships

## Related
- **program-checks-and-panics** -- When errors are severe enough to terminate the program
- **when-to-panic** -- Distinguishing panic-worthy situations from loggable errors

## Contrasts With
(none)

# Common Errors

- **Error**: Logging an error and also returning it
  **Correction**: Choose one: log it (if you're the final handler) or return it (let caller decide)

- **Error**: Using `log.Error` for every error, causing performance impact
  **Correction**: Reserve ERROR level for actionable issues; use lower levels for informational messages

# Common Confusions

- **Confusion**: Thinking ERROR level means "more serious" than WARNING
  **Clarification**: ERROR level should be actionable; WARNING can be for serious-but-not-actionable issues

- **Confusion**: Using the convenience `log.V(2).Infof(...)` form without considering cost
  **Clarification**: Arguments are evaluated regardless of log level; use `if log.V(2)` to guard expensive operations

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "Logging errors".

# Verification Notes

- Definition source: Directly from "Logging errors" section including "Custom verbosity levels" subsection
- Confidence rationale: HIGH -- explicit guidance with examples
- Uncertainties: None
- Cross-reference status: References decisions#useful-test-failures, rate.Sometimes
