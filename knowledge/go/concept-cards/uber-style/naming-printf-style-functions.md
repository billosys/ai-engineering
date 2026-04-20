---
concept: Naming Printf-style Functions
slug: naming-printf-style-functions
category: style
subcategory: naming-conventions
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Naming Printf-style Functions"
extraction_confidence: high
aliases:
  - Printf function naming
  - format function suffix
prerequisites: []
extends: []
related:
  - format-strings-outside-printf
contrasts_with: []
answers_questions:
  - "How should I name Printf-style functions in Go?"
  - "How does go vet detect custom Printf-style functions?"
---

# Quick Definition

End custom `Printf`-style function names with `f` (e.g., `Wrapf`, not `Wrap`) so that `go vet` can detect them and check their format strings. Predefined Printf-style names (like `Printf`, `Sprintf`) are checked by default.

# Core Definition

The Uber Go Style Guide requires that custom functions accepting format strings follow the Printf naming convention. `go vet` automatically checks predefined Printf-style function names. For custom functions, the name must end with `f` to enable `go vet` detection, either automatically or via the `-printfuncs` flag.

# Prerequisites

- Understanding of `go vet` and its Printf family check
- Knowledge of variadic functions and format string patterns

# Key Properties

1. **Predefined names checked by default**: `go vet` automatically checks functions named `Printf`, `Sprintf`, `Errorf`, etc.
2. **Custom names must end with `f`**: For example, `Wrapf`, `statusf`, not `Wrap` or `status`.
3. **`-printfuncs` flag**: Custom Printf-style function names can be registered with `go vet` via `-printfuncs=wrapf,statusf`.
4. **Enables static analysis**: Proper naming allows `go vet` to catch format string/argument mismatches in custom logging and error functions.

# Construction / Recognition

**Good -- name ends with f:**

```go
func Wrapf(format string, args ...interface{}) error {
  // ...
}
```

**Bad -- name does not end with f:**

```go
func Wrap(format string, args ...interface{}) error {
  // ...
}
```

**Registering custom names with go vet:**

```shell
go vet -printfuncs=wrapf,statusf
```

# Context & Application

This is relevant when writing custom logging, error wrapping, or debugging functions that accept format strings. Many popular Go libraries follow this convention (e.g., `fmt.Errorf`, `log.Printf`, `errors.Wrapf`). Consistent naming ensures tooling support across the codebase.

# Examples

See Construction / Recognition above.

# Relationships

- **format-strings-outside-printf**: Complementary guideline ensuring format strings stored in variables are declared as `const` for static analysis.

# Common Errors

1. Naming a Printf-style function without the `f` suffix -- `go vet` cannot detect or check it.
2. Forgetting to register non-standard names with `-printfuncs` when the name does end with `f` but is not one of the predefined names.

# Common Confusions

- **Predefined vs custom names**: `go vet` checks `Printf`, `Sprintf`, `Fprintf`, `Errorf`, etc. by default. Custom names ending in `f` may need explicit registration via `-printfuncs`.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Naming Printf-style Functions" section.

# Verification Notes

Confidence: high. The naming convention, go vet flag, and rationale are directly from the source text.
