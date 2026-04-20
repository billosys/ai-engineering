---
concept: Nil Slices
slug: nil-slices-decisions
category: language
subcategory: slice-semantics
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Nil slices"
extraction_confidence: high
aliases:
  - nil vs empty slice
  - slice initialization
prerequisites:
  - go-slice-basics
related:
  - in-band-errors
  - literal-formatting
contrasts_with: []
answers_questions:
  - "Is there a difference between nil and empty slices in Go?"
  - "Should Go APIs distinguish between nil and empty slices?"
  - "How should empty slices be declared in Go?"
---

# Quick Definition

For most purposes, `nil` and empty slices are functionally equivalent -- `len`, `cap`, `range`, and `append` all work on nil slices. Prefer `var s []T` (nil) over `s := []T{}` (empty) for local variables, and do not design APIs that force callers to distinguish between nil and empty slices.

# Core Definition

> "For most purposes, there is no functional difference between `nil` and the empty slice. Built-in functions like `len` and `cap` behave as expected on `nil` slices." -- Google Go Style Guide, "Nil slices"

> "Do not create APIs that force their clients to make distinctions between nil and the empty slice." -- Google Go Style Guide, "Nil slices"

# Prerequisites

- Understanding of Go slices and their zero value
- Knowledge of `len`, `cap`, `append`, and `range`

# Key Properties

1. **Functional equivalence**: `len`, `cap`, `range`, and `append` all work correctly on nil slices.
2. **Prefer nil initialization**: Use `var t []string` instead of `t := []string{}` for local variables to reduce bugs.
3. **No API distinction**: APIs should not assign different meanings to nil vs. empty slices.
4. **Use `len` for emptiness**: Check `len(s) == 0` rather than `s == nil` to treat nil and empty slices the same.

# Construction / Recognition

**Good -- nil slice works with built-in functions:**

```go
var s []int         // nil

fmt.Println(s)      // []
fmt.Println(len(s)) // 0
fmt.Println(cap(s)) // 0
for range s {...}   // no-op

s = append(s, 42)
fmt.Println(s)      // [42]
```

**Good -- prefer nil initialization:**

```go
var t []string
```

**Bad -- unnecessary empty literal:**

```go
t := []string{}
```

**Good -- API that treats nil and empty the same:**

```go
// Ping pings its targets.
// Returns hosts that successfully responded.
func Ping(hosts []string) ([]string, error) { ... }
```

**Bad -- API that overloads nil with error semantics:**

```go
// nil signifies that a system error occurred.
func Ping(hosts []string) []string { ... }
```

**Good -- check length, not nil:**

```go
func describeInts(prefix string, s []int) {
    if len(s) == 0 {
        return
    }
    fmt.Println(prefix, s)
}
```

**Bad -- checking nil creates API coupling:**

```go
func describeInts(prefix string, s []int) {
    if s == nil {
        return
    }
    fmt.Println(prefix, s)
}
```

# Context & Application

The distinction between nil and empty slices is a subtle source of bugs. If an API uses nil to signal errors and empty to signal "no results," callers must understand and maintain this distinction. Using a separate error return and treating nil/empty the same eliminates this fragility. JSON marshaling is one area where the distinction matters: nil marshals to `null` while `[]T{}` marshals to `[]`.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **in-band-errors**: Overloading nil slices with error semantics is a form of in-band error.
- **literal-formatting**: Related guidance on composite literal initialization.

# Common Errors

1. Using `s := []T{}` when `var s []T` suffices.
2. Designing APIs where nil means "error" and empty means "no results."
3. Checking `s == nil` instead of `len(s) == 0`.

# Common Confusions

- **JSON marshaling difference**: `nil` marshals to `null`; `[]T{}` marshals to `[]`. This is a real difference but should not drive API design.
- **Append works on nil**: `append(nil, x)` works perfectly; no need to pre-initialize.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Nil slices" section.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
