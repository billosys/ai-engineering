---
concept: Error Wrapping
slug: error-wrapping
category: error-handling
subcategory: error-propagation
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Error Wrapping"
extraction_confidence: high
aliases:
  - error context
  - wrapping errors
  - "%w vs %v"
prerequisites:
  - error-types
  - go-error-interface
related:
  - handle-errors-once
  - error-naming
contrasts_with: []
answers_questions:
  - "What is error wrapping?"
  - "How does `%w` differ from `%v` in error wrapping?"
---

# Quick Definition

Error wrapping adds context to errors as they propagate up the call stack. Use `%w` with `fmt.Errorf` when callers should be able to match the underlying error, and `%v` when the underlying error should be opaque. Avoid verbose prefixes like "failed to" that pile up through the stack.

# Core Definition

The Uber Go Style Guide identifies three options for propagating errors from a failed call:

1. Return the original error as-is (when it already has sufficient context).
2. Add context with `fmt.Errorf` and `%w` (preserves the error chain for matching).
3. Add context with `fmt.Errorf` and `%v` (obfuscates the underlying error).

> "Use `%w` if the caller should have access to the underlying error. This is a good default for most wrapped errors, but be aware that callers may begin to rely on this behavior. So for cases where the wrapped error is a known `var` or type, document and test it as part of your function's contract." -- Uber Go Style Guide, "Error Wrapping"

> "Use `%v` to obfuscate the underlying error. Callers will be unable to match it, but you can switch to `%w` in the future if needed." -- Uber Go Style Guide, "Error Wrapping"

# Prerequisites

- Understanding of `fmt.Errorf` format verbs
- Familiarity with `errors.Is` and `errors.As` for error chain traversal
- Knowledge of error propagation patterns in Go

# Key Properties

1. **`%w` preserves the error chain**: Callers can use `errors.Is` and `errors.As` to match the wrapped error.
2. **`%v` breaks the chain**: The underlying error becomes a string embedded in the new error message; callers cannot match it.
3. **Succinct context**: Avoid phrases like "failed to" -- they state the obvious and accumulate as errors percolate up.
4. **Return as-is when context is sufficient**: If the original error message already identifies the source, no wrapping is needed.

# Construction / Recognition

**Good -- succinct context with `%w`:**

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf("new store: %w", err)
}
```

**Bad -- verbose "failed to" prefix:**

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf("failed to create new store: %w", err)
}
```

**The accumulation problem:**

```
// Bad: failed to x: failed to y: failed to create new store: the error
// Good: x: y: new store: the error
```

# Context & Application

Error wrapping is applied at the propagation point -- where a function receives an error from a callee and decides how to pass it upward. The `%w` verb is the recommended default for most cases, but `%v` is appropriate when you want to decouple callers from internal implementation errors that may change. When a wrapped error is part of a function's public contract (a known `var` or type), document and test it.

# Examples

**Wrapping with `%w` for matchable propagation:**

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf("new store: %w", err)
}
```

**Obfuscating with `%v`:**

```go
s, err := store.New()
if err != nil {
    return fmt.Errorf("new store: %v", err)
}
```

# Relationships

- **error-types**: Defines the original errors that wrapping propagates.
- **handle-errors-once**: Determines whether to wrap-and-return vs log-and-degrade.
- **error-naming**: Naming conventions for the errors being wrapped.

# Common Errors

1. Using "failed to" prefixes that pile up into unreadable error chains like `"failed to x: failed to y: failed to z: the error"`.
2. Always using `%w` without considering that it makes the underlying error part of the public API contract.
3. Wrapping errors that already have sufficient context, adding redundant information.

# Common Confusions

- **`%w` vs `%v`**: `%w` creates a wrapped error that preserves the chain for `errors.Is`/`errors.As`; `%v` converts the error to a string, breaking the chain. The choice is about API commitment, not formatting.
- **When to return as-is**: If the error message already identifies where it came from (e.g., a well-described sentinel), wrapping adds noise.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Error Wrapping" section.

# Verification Notes

Confidence: high. The three propagation options, the `%w` vs `%v` guidance, and the "failed to" anti-pattern are all directly stated in the source with explicit code examples.
