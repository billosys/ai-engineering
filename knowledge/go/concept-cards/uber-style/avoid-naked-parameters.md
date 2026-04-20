---
concept: Avoid Naked Parameters
slug: avoid-naked-parameters
category: style
subcategory: function-design
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Avoid Naked Parameters"
extraction_confidence: high
aliases:
  - naked parameters
  - C-style parameter comments
prerequisites: []
extends: []
related:
  - functional-options
contrasts_with: []
answers_questions:
  - "What is a naked parameter?"
  - "How do I make boolean function parameters more readable?"
---

# Quick Definition

Naked parameters are function arguments (especially booleans) whose meaning is unclear at the call site. Add C-style inline comments (`/* paramName */`) to clarify ambiguous parameters, or better yet, replace bare `bool` parameters with custom types for type-safe, self-documenting code.

# Core Definition

The Uber Go Style Guide warns that naked parameters in function calls hurt readability. When a function takes multiple boolean or similarly opaque arguments, the call site becomes difficult to understand without consulting the function signature.

The guide recommends two mitigations:
1. Add C-style comments at the call site to name the parameters.
2. Replace `bool` parameters with custom types that make the meaning explicit and allow future expansion beyond two states.

# Prerequisites

- Understanding of Go's `iota` for constant enumeration
- Familiarity with custom type definitions

# Key Properties

1. **C-style comments as a quick fix**: Use `/* paramName */` inline comments to annotate unclear parameters at the call site.
2. **Custom types as the better solution**: Define named types (e.g., `Region`, `Status`) with `iota` constants to replace bare booleans.
3. **Future extensibility**: Custom types allow adding more than two states later without changing the function signature.
4. **Type safety**: Custom types prevent accidentally swapping parameter positions.

# Construction / Recognition

**Bad -- naked boolean parameters:**

```go
// func printInfo(name string, isLocal, done bool)

printInfo("foo", true, true)
```

**Better -- C-style comments:**

```go
// func printInfo(name string, isLocal, done bool)

printInfo("foo", true /* isLocal */, true /* done */)
```

**Best -- custom types:**

```go
type Region int

const (
  UnknownRegion Region = iota
  Local
)

type Status int

const (
  StatusReady Status = iota + 1
  StatusDone
  // Maybe we will have a StatusInProgress in the future.
)

func printInfo(name string, region Region, status Status)
```

# Context & Application

This guideline applies whenever a function takes parameters whose meaning is not obvious from the value alone. Booleans are the most common offender, but numeric parameters or string parameters with special meanings can also be "naked." The functional options pattern is a related approach for constructor functions with many optional parameters.

# Examples

See Construction / Recognition above for the complete progression from bad to best.

# Relationships

- **functional-options**: For constructors with many optional parameters, the functional options pattern provides an alternative to naked parameters.

# Common Errors

1. Passing multiple `true`/`false` arguments without any annotation -- readers cannot determine which parameter is which.
2. Using C-style comments inconsistently -- annotate all ambiguous parameters or none to maintain consistency.

# Common Confusions

- **C-style comments vs Go doc comments**: The `/* ... */` syntax is Go's block comment, used here inline for parameter annotation. This is distinct from `//` line comments used for documentation.
- **When to use custom types vs comments**: Comments are a quick improvement; custom types are the preferred long-term solution. Use custom types when modifying the function signature is feasible.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Avoid Naked Parameters" section.

# Verification Notes

Confidence: high. The guideline, examples, and custom type recommendation are all directly from the source text.
