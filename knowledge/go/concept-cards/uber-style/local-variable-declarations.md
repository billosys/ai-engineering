---
concept: Local Variable Declarations
slug: local-variable-declarations
category: style
subcategory: variable-declaration
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Local Variable Declarations"
extraction_confidence: high
aliases:
  - short variable declarations
  - ":= vs var"
prerequisites: []
extends: []
related:
  - nil-is-a-valid-slice
  - reduce-scope-of-variables
  - initializing-structs
contrasts_with: []
answers_questions:
  - "What distinguishes `:=` from `var` for variable declarations?"
  - "When should I use `:=` versus `var` in Go?"
---

# Quick Definition

Use short variable declarations (`:=`) when setting a variable to an explicit value. Use `var` when declaring a variable that will take its zero value, making the intent to use the zero value clear.

# Core Definition

Go provides two forms for local variable declarations: the short variable declaration (`:=`) and the `var` keyword. The Uber Go Style Guide recommends using `:=` when the variable is being assigned an explicit value, and `var` when the variable should start at its type's zero value. This convention signals intent to the reader -- `:=` means "initialized with a specific value," while `var` means "zero-valued by design."

# Prerequisites

- Understanding of Go's zero values for each type (0, "", nil, false)
- Basic Go variable declaration syntax

# Key Properties

1. **`:=` for explicit values**: When a variable is set to a known value at declaration time, use the short form.
2. **`var` for zero values**: When the variable intentionally starts at its zero value (empty string, nil slice, zero int), use `var` to signal that intent.
3. **Consistency with slice declarations**: This convention aligns with the Go community's recommendation for declaring empty slices with `var` rather than `:=`.

# Construction / Recognition

**Use `:=` with explicit values:**

```go
s := "foo"
```

**Use `var` for zero values:**

```go
var filtered []int
```

**Not recommended -- `var` with explicit value:**

```go
var s = "foo"
```

**Not recommended -- `:=` with empty slice literal:**

```go
filtered := []int{}
```

# Context & Application

This convention applies to local variables inside functions. For top-level (package-scope) variables, `var` is always used since `:=` is not available at package scope. The distinction helps readers quickly understand whether a variable is intentionally zero-valued or initialized with meaningful data.

# Examples

**Good -- `:=` for explicit value:**

```go
s := "foo"
```

**Good -- `var` for zero-value slice used with append:**

```go
func f(list []int) {
  var filtered []int
  for _, v := range list {
    if v > 10 {
      filtered = append(filtered, v)
    }
  }
}
```

**Bad -- `:=` with empty slice literal obscures zero-value intent:**

```go
func f(list []int) {
  filtered := []int{}
  for _, v := range list {
    if v > 10 {
      filtered = append(filtered, v)
    }
  }
}
```

# Relationships

- **nil-is-a-valid-slice**: Explains why `var` is preferred for slice declarations that start empty.
- **reduce-scope-of-variables**: Both conventions contribute to clear, minimal-scope variable declarations.
- **initializing-structs**: The `var` convention for zero-value structs mirrors this pattern.

# Common Errors

1. Using `var s = "foo"` instead of `s := "foo"` -- unnecessarily verbose when an explicit value is provided.
2. Using `filtered := []int{}` instead of `var filtered []int` -- obscures that the intent is a zero-value (nil) slice.

# Common Confusions

- **`:=` creates a new variable vs `=` assigns**: `:=` declares and initializes; `=` assigns to an existing variable. This guideline is about when to use `:=` versus `var` for declarations, not about `:=` versus `=`.
- **`var` with explicit value at package scope**: At the top level, `var` is required even with explicit values since `:=` is unavailable. This guideline applies specifically to local variables.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Local Variable Declarations" section.

# Verification Notes

Confidence: high. The rules and code examples are directly stated in the source text with explicit Bad/Good comparisons.
