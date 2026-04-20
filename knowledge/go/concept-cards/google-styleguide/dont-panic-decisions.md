---
concept: Don't Panic
slug: dont-panic-decisions
category: error-handling
subcategory: panic-avoidance
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Don't panic"
extraction_confidence: high
aliases:
  - no panic for errors
  - avoid panic
prerequisites:
  - returning-errors
  - handle-errors-decisions
related:
  - must-functions
  - goroutine-lifetimes-decisions
contrasts_with: []
answers_questions:
  - "When should panic be used in Go?"
  - "What should be used instead of panic for startup errors?"
  - "How should impossible conditions be handled in Go?"
---

# Quick Definition

Do not use `panic` for normal error handling; use `error` and multiple return values instead. For fatal startup errors, use `log.Exit` (which calls `os.Exit`). Reserve `panic` and `log.Fatal` only for truly "impossible" conditions that represent bugs.

# Core Definition

> "Do not use `panic` for normal error handling. Instead, use `error` and multiple return values." -- Google Go Style Guide, "Don't panic"

> "Within `package main` and initialization code, consider `log.Exit` for errors that should terminate the program (e.g., invalid configuration), as in many of these cases a stack trace will not help the reader." -- Google Go Style Guide, "Don't panic"

> "For errors that indicate 'impossible' conditions, namely bugs that should always be caught during code review and/or testing, a function may reasonably return an error or call `log.Fatal`." -- Google Go Style Guide, "Don't panic"

# Prerequisites

- Understanding of Go's `panic` and `recover` mechanism
- Knowledge of `error` return patterns
- Familiarity with `log.Exit` and `log.Fatal`

# Key Properties

1. **No panic for normal errors**: Use `error` and multiple return values for all expected failure modes.
2. **`log.Exit` for startup failures**: Use `log.Exit` (calls `os.Exit`) for configuration errors and fatal startup conditions where a stack trace is unhelpful. Note that deferred functions will not run.
3. **`log.Fatal` for impossible bugs**: Reserve for conditions that should have been caught in code review or testing.
4. **`log.Fatalf` is not stdlib**: Google's `log.Fatalf` differs from the standard library version.

# Construction / Recognition

**Normal error handling -- return errors:**

```go
func Process(input string) (*Result, error) {
    if input == "" {
        return nil, fmt.Errorf("empty input")
    }
    // ...
    return result, nil
}
```

**Startup failure -- use log.Exit:**

```go
func main() {
    cfg, err := loadConfig()
    if err != nil {
        log.Exitf("invalid configuration: %v", err)
    }
}
```

# Context & Application

Unlike languages with exception-based error handling, Go uses explicit error returns. `panic` bypasses this model and makes code harder to reason about because callers cannot decide how to handle the failure. In production services, an unrecovered panic in any goroutine terminates the entire process. The `log.Exit` path is specifically recommended for startup because stack traces are noise when the error is "config file not found."

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **must-functions**: The `MustXYZ` pattern is the controlled exception to the no-panic rule, limited to initialization.
- **handle-errors-decisions**: The broader guidance on how to handle errors.
- **goroutine-lifetimes-decisions**: Panics in goroutines are especially dangerous since they crash the process.

# Common Errors

1. Using `panic` for input validation or expected error conditions.
2. Using `panic` instead of `log.Exit` for startup failures (unnecessary stack trace).
3. Confusing Google's `log.Fatalf` with the standard library's version.

# Common Confusions

- **`log.Exit` vs. `log.Fatal`**: `log.Exit` calls `os.Exit` (no stack trace, deferred functions don't run). `log.Fatal` may include a stack trace and is reserved for "impossible" bug conditions.
- **When panic is acceptable**: See the `must-functions` concept and the best practices guidance on when panic is acceptable.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Don't panic" section.

# Verification Notes

Confidence: high. All guidance is directly from the source text.
