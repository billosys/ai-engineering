---
concept: Returning Errors
slug: returning-errors
category: error-handling
subcategory: error-returns
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Returning errors"
extraction_confidence: high
aliases:
  - error return convention
  - error as last return
prerequisites:
  - go-error-interface
related:
  - error-strings
  - handle-errors-decisions
  - in-band-errors
contrasts_with: []
answers_questions:
  - "Where should error appear in a Go function's return list?"
  - "Why should exported functions return the error interface instead of a concrete error type?"
  - "What does a nil error signal in Go?"
---

# Quick Definition

Use `error` as the last return value to signal that a function can fail. Return `nil` to indicate success. Exported functions must return the `error` interface type, not concrete error types, to avoid subtle nil-interface bugs.

# Core Definition

> "Use `error` to signal that a function can fail. By convention, `error` is the last result parameter." -- Google Go Style Guide, "Returning errors"

> "Exported functions that return errors should return them using the `error` type. Concrete error types are susceptible to subtle bugs: a concrete `nil` pointer can get wrapped into an interface and thus become a non-nil value." -- Google Go Style Guide, "Returning errors"

# Prerequisites

- Understanding of Go's `error` interface
- Knowledge of Go's multiple return values
- Familiarity with nil interface semantics

# Key Properties

1. **Error is last**: By convention, `error` is always the last return parameter.
2. **nil means success**: Returning a `nil` error is the idiomatic way to signal a successful operation.
3. **Non-error values unspecified on failure**: When a function returns an error, callers must treat all non-error return values as unspecified unless explicitly documented otherwise.
4. **Use interface type for exports**: Exported functions must use the `error` interface, not concrete types like `*os.PathError`, to avoid nil-pointer-in-interface bugs.

# Construction / Recognition

**Good -- error as last return, using error interface:**

```go
func Good() error { /* ... */ }
```

```go
func GoodLookup() (*Result, error) {
    // ...
    if err != nil {
        return nil, err
    }
    return res, nil
}
```

**Bad -- returning a concrete error type:**

```go
func Bad() *os.PathError { /*...*/ }
```

# Context & Application

A function that takes a `context.Context` argument should usually return an `error` so that the caller can determine if the context was cancelled while the function was running. The nil-interface pitfall is particularly dangerous: a concrete nil pointer (e.g., `(*os.PathError)(nil)`) wrapped into the `error` interface becomes a non-nil `error` value, breaking `if err != nil` checks.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **error-strings**: Conventions for formatting the string content of errors.
- **handle-errors-decisions**: What to do once you receive an error.
- **in-band-errors**: Why separate error returns are preferred over sentinel values.

# Common Errors

1. Returning a concrete error type from an exported function, which can cause nil-interface bugs.
2. Assuming non-error return values are valid when the error is non-nil.
3. Placing the error parameter somewhere other than last in the return list.

# Common Confusions

- **Concrete nil vs. interface nil**: A `(*os.PathError)(nil)` returned as `error` is non-nil. This is why exported functions must return the `error` interface directly.
- **Zero values on error**: Non-error return values are commonly their zero values when an error is returned, but this cannot be assumed without documentation.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Returning errors" section.

# Verification Notes

Confidence: high. All guidance, rationale, and code examples are taken directly from the source text.
