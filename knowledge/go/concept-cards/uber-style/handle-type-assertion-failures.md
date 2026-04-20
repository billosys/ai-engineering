---
concept: Handle Type Assertion Failures
slug: handle-type-assertion-failures
category: code-safety
subcategory: type-safety
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Handle Type Assertion Failures"
extraction_confidence: high
aliases:
  - comma-ok type assertion
  - safe type assertion
prerequisites:
  - go-interfaces
related:
  - dont-panic
  - error-types
contrasts_with: []
answers_questions:
  - "How should type assertions be performed safely in Go?"
---

# Quick Definition

Always use the two-value "comma ok" form of type assertions (`t, ok := i.(string)`) instead of the single-value form (`t := i.(string)`). The single-value form panics on an incorrect type, while the two-value form returns a boolean indicating success.

# Core Definition

> "The single return value form of a type assertion will panic on an incorrect type. Therefore, always use the 'comma ok' idiom." -- Uber Go Style Guide, "Handle Type Assertion Failures"

# Prerequisites

- Understanding of Go interfaces and interface values
- Knowledge of Go's type assertion syntax

# Key Properties

1. **Single-value form panics**: `t := i.(string)` panics at runtime if `i` does not hold a `string`.
2. **Two-value form is safe**: `t, ok := i.(string)` sets `ok` to `false` and `t` to the zero value if the assertion fails.
3. **Universal rule**: The guide states this should be done "always" -- there are no stated exceptions.

# Construction / Recognition

**Bad -- single-value form (panics on wrong type):**

```go
t := i.(string)
```

**Good -- comma-ok form (safe):**

```go
t, ok := i.(string)
if !ok {
  // handle the error gracefully
}
```

# Context & Application

Type assertions are common when working with `interface{}` (or `any`) values, such as those from JSON unmarshaling, generic containers, or middleware chains. A runtime panic from a failed type assertion can crash a production service. The comma-ok idiom converts what would be a crash into a handleable condition.

# Examples

See Construction / Recognition above for the source examples.

# Relationships

- **dont-panic**: Type assertion panics are one source of panics that this pattern prevents.
- **error-types**: After detecting a failed type assertion via comma-ok, you may need to return a proper error.

# Common Errors

1. Using the single-value form in production code, creating a latent panic risk that only manifests when unexpected types appear.
2. Checking `ok` but not handling the failure case (e.g., silently proceeding with the zero value when that is not appropriate).

# Common Confusions

- **Type assertion vs type switch**: A type switch (`switch v := i.(type)`) is inherently safe and does not panic. The comma-ok guidance applies specifically to individual type assertions.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Handle Type Assertion Failures" section.

# Verification Notes

Confidence: high. The guidance is explicit and concise in the source, with a clear bad/good code comparison. No synthesis required.
