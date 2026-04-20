---
concept: Handle Errors
slug: handle-errors-decisions
category: error-handling
subcategory: error-handling-strategy
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Handle errors"
extraction_confidence: high
aliases:
  - don't discard errors
  - error handling decisions
prerequisites:
  - returning-errors
related:
  - error-strings
  - indent-error-flow
  - in-band-errors
  - dont-panic-decisions
contrasts_with: []
answers_questions:
  - "Is it okay to use _ to discard errors in Go?"
  - "What are the valid ways to handle an error in Go?"
  - "When can you ignore an error in Go?"
---

# Quick Definition

Do not discard errors with `_`. Every error must be deliberately handled: address it immediately, return it to the caller, or in exceptional situations call `log.Fatal` or `panic`. If ignoring an error is truly safe, document why with a comment.

# Core Definition

> "Code that encounters an error should make a deliberate choice about how to handle it. It is not usually appropriate to discard errors using `_` variables. If a function returns an error, do one of the following: Handle and address the error immediately. Return the error to the caller. In exceptional situations, call `log.Fatal` or (if absolutely necessary) `panic`." -- Google Go Style Guide, "Handle errors"

# Prerequisites

- Understanding of Go's error return conventions
- Familiarity with `log.Fatal` and `panic` behavior

# Key Properties

1. **No silent discarding**: Do not use `_` to ignore errors without justification.
2. **Three valid choices**: Handle immediately, return to caller, or call `log.Fatal`/`panic`.
3. **Comment when ignoring**: In rare cases where ignoring is safe (e.g., `bytes.Buffer.Write`), add a comment explaining why.
4. **`log.Fatal` for impossible conditions**: Use `log.Fatal` only for truly impossible states, not routine errors.

# Construction / Recognition

**Good -- explicitly ignoring a documented never-fail function:**

```go
var b *bytes.Buffer

n, _ := b.Write(p) // never returns a non-nil error
```

**Handling pattern -- address immediately:**

```go
if err != nil {
    // handle the error
    return fmt.Errorf("operation failed: %w", err)
}
```

**Handling pattern -- return to caller:**

```go
result, err := doSomething()
if err != nil {
    return nil, err
}
```

# Context & Application

Silently discarding errors is one of the most common sources of hard-to-diagnose bugs in Go programs. When an error is ignored, the program continues with invalid assumptions, often failing much later in an unrelated location. The explicit handling requirement ensures that every failure path is considered by the developer.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **returning-errors**: How errors are returned from functions.
- **indent-error-flow**: How to structure code so error handling comes first.
- **dont-panic-decisions**: When `panic` and `log.Fatal` are appropriate.

# Common Errors

1. Using `_` to discard errors without a justifying comment.
2. Logging an error but then continuing as if it did not happen.
3. Using `panic` for routine errors instead of returning them.

# Common Confusions

- **`log.Fatalf` is not stdlib log**: Google's `log.Fatalf` differs from the standard library's `log.Fatalf`. The guide notes this distinction explicitly.
- **When ignoring is okay**: Only when the function is documented as never returning a non-nil error (e.g., `bytes.Buffer.Write`).

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Handle errors" section.

# Verification Notes

Confidence: high. All guidance and examples are taken directly from the source text.
