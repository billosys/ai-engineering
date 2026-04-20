---
concept: Handle Errors Once
slug: handle-errors-once
category: error-handling
subcategory: error-handling-strategy
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Handle Errors Once"
extraction_confidence: high
aliases:
  - don't log and return
  - single error handling
prerequisites:
  - error-types
  - error-wrapping
related:
  - error-naming
  - dont-panic
contrasts_with: []
answers_questions:
  - "What distinguishes logging-and-returning from wrapping-and-returning errors?"
---

# Quick Definition

Each error should be handled exactly once: either wrap it and return it for a caller to handle, or log it and degrade gracefully. Never do both -- logging an error and then returning it causes duplicate noise as each caller up the stack repeats the pattern.

# Core Definition

The Uber Go Style Guide establishes a principle that callers should handle each error only once, choosing from among several valid strategies:

> "Regardless of how the caller handles the error, it should typically handle each error only once. The caller should not, for example, log the error and then return it, because *its* callers may handle the error as well." -- Uber Go Style Guide, "Handle Errors Once"

Valid handling strategies include:
- Matching with `errors.Is` or `errors.As` and branching
- Logging and degrading gracefully (for recoverable, non-critical errors)
- Returning a well-defined domain error
- Returning the error, wrapped or verbatim

# Prerequisites

- Understanding of error wrapping with `%w` (see error-wrapping)
- Knowledge of `errors.Is` and `errors.As` for error matching
- Familiarity with graceful degradation patterns

# Key Properties

1. **One handling action per error**: Do not both log and return the same error.
2. **Wrap-and-return**: Add context and let a higher-level caller decide what to do.
3. **Log-and-degrade**: For non-critical operations, log the error and continue with reduced functionality.
4. **Match-and-branch**: Use `errors.Is`/`errors.As` to handle specific errors differently while wrapping and returning all others.

# Construction / Recognition

**Bad -- log and return:**

```go
u, err := getUser(id)
if err != nil {
  // BAD: See description
  log.Printf("Could not get user %q: %v", id, err)
  return err
}
```

**Good -- wrap and return:**

```go
u, err := getUser(id)
if err != nil {
  return fmt.Errorf("get user %q: %w", id, err)
}
```

**Good -- log and degrade gracefully:**

```go
if err := emitMetrics(); err != nil {
  // Failure to write metrics should not
  // break the application.
  log.Printf("Could not emit metrics: %v", err)
}
```

**Good -- match and degrade gracefully:**

```go
tz, err := getUserTimeZone(id)
if err != nil {
  if errors.Is(err, ErrUserNotFound) {
    // User doesn't exist. Use UTC.
    tz = time.UTC
  } else {
    return fmt.Errorf("get user %q: %w", id, err)
  }
}
```

# Context & Application

This principle prevents cascading duplicate log entries. When a function logs an error and then returns it, every caller up the stack that also logs-and-returns creates another log line for the same failure. The result is excessive noise in application logs with little additional diagnostic value. The fix is to choose one responsibility at each level: either add context and pass the error upward, or absorb the error and handle it locally.

# Examples

See Construction / Recognition above for the four patterns from the source.

# Relationships

- **error-wrapping**: The "wrap and return" strategy relies on proper use of `%w` for context.
- **error-types**: The "match and branch" strategy relies on sentinel errors or custom types.
- **dont-panic**: Another error handling concern -- panicking is never an acceptable handling strategy in production.

# Common Errors

1. Logging an error and then returning it, causing duplicate log entries at every level of the call stack.
2. Silently discarding errors without logging or returning -- this loses diagnostic information entirely.
3. Always wrapping and returning without ever logging -- at some point, typically at the top of the call stack, an error must be logged or presented to the user.

# Common Confusions

- **"Handle once" does not mean "ignore"**: The principle is about not *duplicating* handling. Every error must still be handled somewhere -- either absorbed (logged/degraded) or propagated (wrapped/returned).
- **Log-and-degrade is not log-and-return**: Logging and degrading means the function continues with reduced functionality and does *not* return the error. Logging and returning means the function both logs *and* passes the error upward.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Handle Errors Once" section.

# Verification Notes

Confidence: high. The "handle each error only once" principle and all four handling patterns (bad: log-and-return; good: wrap-and-return, log-and-degrade, match-and-degrade) are explicitly provided with code examples in the source.
