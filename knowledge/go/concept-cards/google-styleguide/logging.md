---
# === CORE IDENTIFICATION ===
concept: Logging Conventions
slug: logging

# === CLASSIFICATION ===
category: libraries
subcategory: observability
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Logging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "log package usage"
  - "structured logging"
  - "glog"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - contexts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What logging package should I use in Go at Google?"
  - "What is the difference between log.Fatal and log.Exit?"
  - "When should I use the non-formatting log functions?"
  - "Is there a log.Panic in the Google variant?"
---

# Quick Definition

Use the appropriate logging library (standard `log`, `glog`, or `klog`). Prefer non-formatting versions when no formatting is needed. Use `log.Fatal` for stacktrace aborts and `log.Exit` for clean stops. There is no `log.Panic`.

# Core Definition

Google Go programs use a variant of the standard `log` package with a similar but more powerful interface that interoperates with internal systems. The open source equivalent is `glog`. Key conventions: `log.Fatal` aborts with a stacktrace, `log.Exit` stops without one, and there is no `log.Panic` (unlike the standard library). When no formatting is needed, prefer the non-formatting version (e.g., `log.Info(v)` instead of `log.Infof("%v", v)`).

# Prerequisites

- **Go standard library log package** -- Basic familiarity with Go's built-in logging
- **Error handling patterns** -- Understanding when to log vs return errors

# Key Properties

1. **log.Fatal**: Aborts the program with a stacktrace
2. **log.Exit**: Stops the program without a stacktrace
3. **No log.Panic**: Unlike the standard library, the Google variant has no Panic function
4. **Non-formatting preference**: Use `log.Info(v)` over `log.Infof("%v", v)` when no formatting is needed
5. **Don't log AND return**: Choose one or the other to avoid duplicate error reporting

# Construction / Recognition

## To Apply:
1. Choose the appropriate log package for your context (log, glog, or klog)
2. Use `log.Fatal` when a stacktrace is helpful for debugging the exit
3. Use `log.Exit` for clean exits without stacktraces
4. Use the non-formatting variant when there is nothing to format
5. Either log an error or return it -- do not do both

## To Recognize:
1. Code using `log.Infof("%v", v)` when `log.Info(v)` would suffice
2. Code that both logs an error and returns it to the caller

# Context & Application

Logging conventions ensure consistent observability across a codebase. The guidance to avoid logging AND returning errors prevents duplicate noise in logs -- the caller receiving the error should decide how to handle it. The preference for non-formatting versions reduces unnecessary format string processing.

# Examples

**Example 1 -- Prefer non-formatting version**:

```go
// Good:
log.Info(value)

// Bad (unnecessary formatting):
log.Infof("%v", value)
```

**Example 2 -- Fatal vs Exit**:

```go
// Abort with stacktrace for debugging:
log.Fatal("unexpected state: no connections available")

// Clean exit without stacktrace:
log.Exit("shutting down gracefully")
```

# Relationships

## Related
- **contexts** -- Contexts often carry information relevant to logging (trace IDs, deadlines)

# Common Errors

- **Error**: Logging an error and also returning it to the caller
  **Correction**: Choose one: either log the error (if this is the final handler) or return it (if the caller should decide).

- **Error**: Using `log.Panic` in Google Go code
  **Correction**: There is no `log.Panic` in the Google logging variant. Use `log.Fatal` or `log.Exit` instead.

# Common Confusions

- **Confusion**: Assuming the Google log package behaves identically to the standard library `log`
  **Clarification**: The Google variant has a different API surface: it includes `log.Exit`, has level-based logging (Info, Warning, Error), and lacks `log.Panic`.

# Source Reference

Chapter 3: Style Decisions, Section "Logging" under "Common libraries".

# Verification Notes

- Definition source: Directly from the "Logging" section of the Style Decisions document
- Confidence rationale: HIGH -- the guidance is explicit with specific function behaviors noted
- Uncertainties: Some internal details about Google's log variant are not fully described
- Cross-reference status: References best practices on logging errors and custom verbosity levels
