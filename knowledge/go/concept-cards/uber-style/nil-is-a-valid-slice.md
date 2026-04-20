---
concept: Nil Is a Valid Slice
slug: nil-is-a-valid-slice
category: data-structures
subcategory: slices
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "nil is a valid slice"
extraction_confidence: high
aliases:
  - nil slice
  - empty slice vs nil slice
prerequisites: []
extends: []
related:
  - local-variable-declarations
  - initializing-structs
contrasts_with: []
answers_questions:
  - "How should I return an empty slice in Go?"
  - "How should I check if a slice is empty?"
  - "What is the difference between a nil slice and an empty slice?"
---

# Quick Definition

A `nil` slice is a valid slice of length 0 in Go. Return `nil` instead of an empty slice literal, check emptiness with `len(s) == 0` rather than `s == nil`, and declare zero-value slices with `var` since they are immediately usable without `make()`.

# Core Definition

Go's nil slice is fully functional: it has length 0, capacity 0, and supports `append`. The Uber Go Style Guide codifies three rules around this property to produce consistent, idiomatic code.

> "`nil` is a valid slice of length 0." -- Uber Go Style Guide, "nil is a valid slice"

The guide also notes: "while it is a valid slice, a nil slice is not equivalent to an allocated slice of length 0 -- one is nil and the other is not -- and the two may be treated differently in different situations (such as serialization)."

# Prerequisites

- Understanding of Go slice internals (pointer, length, capacity)
- Knowledge of `append` behavior with nil slices

# Key Properties

1. **Return nil, not empty literal**: When returning a zero-length slice, return `nil` rather than `[]int{}`.
2. **Check length, not nil**: Use `len(s) == 0` to test emptiness, because both nil and allocated empty slices should be treated as empty.
3. **`var` declares a usable nil slice**: A `var`-declared slice is nil but immediately usable with `append`, without needing `make()`.
4. **Serialization caveat**: A nil slice and an allocated empty slice may serialize differently (e.g., JSON `null` vs `[]`).

# Construction / Recognition

**Return nil, not empty slice:**

```go
// Good
if x == "" {
  return nil
}

// Bad
if x == "" {
  return []int{}
}
```

**Check emptiness with len:**

```go
// Good
func isEmpty(s []string) bool {
  return len(s) == 0
}

// Bad
func isEmpty(s []string) bool {
  return s == nil
}
```

**Use var for nil slice:**

```go
// Good
var nums []int

if add1 {
  nums = append(nums, 1)
}

// Bad
nums := []int{}
// or, nums := make([]int)

if add1 {
  nums = append(nums, 1)
}
```

# Context & Application

This convention applies whenever you create or return slices that start empty and may be populated later. It produces cleaner code and avoids unnecessary allocations. The serialization caveat is important for JSON APIs where the distinction between `null` and `[]` may matter to clients.

# Examples

**Idiomatic nil slice usage:**

```go
var nums []int

if add1 {
  nums = append(nums, 1)
}

if add2 {
  nums = append(nums, 2)
}
```

# Relationships

- **local-variable-declarations**: The `var` form for zero-value slices is a specific application of the broader `:=` vs `var` convention.
- **initializing-structs**: The preference for `var` with zero values mirrors the struct initialization convention.

# Common Errors

1. Returning `[]int{}` when `nil` would suffice -- creates an unnecessary allocation.
2. Checking `s == nil` to determine emptiness -- misses allocated empty slices and is not idiomatic.
3. Using `make([]int, 0)` or `[]int{}` when a `var` declaration would suffice.

# Common Confusions

- **nil slice vs empty slice in serialization**: `encoding/json` marshals a nil slice as `null` and an allocated empty slice as `[]`. If API contracts require `[]`, an explicit empty allocation is needed.
- **nil slice is usable**: Unlike nil maps (which panic on write), nil slices support `append` and all read operations.

# Source Reference

Uber Go Style Guide, "Style" chapter, "nil is a valid slice" section.

# Verification Notes

Confidence: high. All three rules and code examples are directly quoted from the source with explicit Bad/Good comparisons.
