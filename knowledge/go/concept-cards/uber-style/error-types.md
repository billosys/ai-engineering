---
concept: Error Types
slug: error-types
category: error-handling
subcategory: error-declaration
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Error Types"
extraction_confidence: high
aliases:
  - error declaration strategies
  - error creation patterns
prerequisites:
  - go-error-interface
related:
  - error-wrapping
  - error-naming
  - handle-errors-once
contrasts_with:
  - dont-panic
answers_questions:
  - "What is an error sentinel in Go?"
  - "What is a custom error type?"
  - "What distinguishes a sentinel error from a custom error type?"
  - "What distinguishes `errors.Is` from `errors.As`?"
---

# Quick Definition

Go offers four primary strategies for declaring errors -- `errors.New` for static strings, `fmt.Errorf` for dynamic strings, top-level sentinel variables for matchable static errors, and custom error types for matchable dynamic errors. The choice depends on whether callers need to match the error and whether the message requires runtime context.

# Core Definition

The Uber Go Style Guide presents a decision matrix for error declaration based on two axes: whether the caller needs to match the error, and whether the error message is static or dynamic.

> "Consider the following before picking the option best suited for your use case. Does the caller need to match the error so that they can handle it? If yes, we must support the `errors.Is` or `errors.As` functions by declaring a top-level error variable or a custom type." -- Uber Go Style Guide, "Error Types"

The decision matrix:

| Error matching? | Error Message | Guidance |
|---|---|---|
| No | static | `errors.New` |
| No | dynamic | `fmt.Errorf` |
| Yes | static | top-level `var` with `errors.New` |
| Yes | dynamic | custom `error` type |

# Prerequisites

- Understanding of Go's `error` interface (`Error() string`)
- Familiarity with `errors.New` and `fmt.Errorf`
- Knowledge of `errors.Is` and `errors.As` for error matching

# Key Properties

1. **Sentinel errors** (top-level `var` with `errors.New`) are package-level variables that callers match with `errors.Is`. They carry a fixed message string.
2. **Custom error types** are structs implementing the `error` interface. They carry dynamic contextual fields and callers match them with `errors.As`.
3. **Unexported `errors.New`** calls produce errors that cannot be matched by callers and are suitable for opaque error propagation.
4. **`fmt.Errorf` without `%w`** produces dynamic, unmatchable errors.
5. Exported error variables and types become part of the package's public API.

# Construction / Recognition

**Sentinel error (matchable, static):**

```go
// package foo
var ErrCouldNotOpen = errors.New("could not open")

func Open() error {
  return ErrCouldNotOpen
}

// package bar
if err := foo.Open(); err != nil {
  if errors.Is(err, foo.ErrCouldNotOpen) {
    // handle the error
  } else {
    panic("unknown error")
  }
}
```

**Custom error type (matchable, dynamic):**

```go
// package foo
type NotFoundError struct {
  File string
}

func (e *NotFoundError) Error() string {
  return fmt.Sprintf("file %q not found", e.File)
}

func Open(file string) error {
  return &NotFoundError{File: file}
}

// package bar
if err := foo.Open("testfile.txt"); err != nil {
  var notFound *NotFoundError
  if errors.As(err, &notFound) {
    // handle the error
  } else {
    panic("unknown error")
  }
}
```

# Context & Application

Use this decision matrix at the point of error origination -- where a new error is first created, not where an existing error is propagated. For propagation, see the error-wrapping concept. The choice directly affects whether downstream callers can programmatically react to specific failure modes versus treating all errors uniformly.

# Examples

**No matching needed, static message:**

```go
func Open() error {
  return errors.New("could not open")
}
```

**No matching needed, dynamic message:**

```go
func Open(file string) error {
  return fmt.Errorf("file %q not found", file)
}
```

# Relationships

- **error-wrapping**: Covers propagation of errors from downstream calls, complementing the origination patterns described here.
- **error-naming**: Defines naming conventions for the sentinel variables and custom types declared using these patterns.
- **handle-errors-once**: Governs how callers should react once they receive these errors.

# Common Errors

1. Using `fmt.Errorf` for a static message when callers need to match it -- callers cannot use `errors.Is` on a freshly formatted string.
2. Exporting error variables or types without realizing they become part of the public API contract.
3. Using `errors.Is` to match a custom error type -- `errors.Is` is for sentinel values; use `errors.As` for custom types.

# Common Confusions

- **`errors.Is` vs `errors.As`**: `errors.Is` checks if an error in the chain matches a specific *value* (sentinel). `errors.As` checks if an error in the chain matches a specific *type* (custom error type) and extracts it.
- **Sentinel error vs custom error type**: Sentinels are fixed-message package-level variables; custom types are structs carrying dynamic context fields.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Error Types" section.

# Verification Notes

Confidence: high. The decision matrix, code examples, and guidance are directly quoted from the source text. All four error declaration strategies are explicitly enumerated in the guide.
