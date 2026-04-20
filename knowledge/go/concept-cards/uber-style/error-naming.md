---
concept: Error Naming
slug: error-naming
category: error-handling
subcategory: naming-conventions
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Error Naming"
extraction_confidence: high
aliases:
  - error naming conventions
  - Err prefix
  - Error suffix
prerequisites:
  - error-types
related:
  - error-wrapping
  - handle-errors-once
  - avoid-using-built-in-names
contrasts_with: []
answers_questions:
  - "How do error naming conventions differ for sentinel errors vs. custom error types?"
---

# Quick Definition

Sentinel error variables use the prefix `Err` (exported) or `err` (unexported). Custom error types use the suffix `Error` (exported) or `error` (unexported). This convention lets developers immediately distinguish error values from error types by name.

# Core Definition

The Uber Go Style Guide specifies two distinct naming patterns based on the kind of error being declared:

> "For error values stored as global variables, use the prefix `Err` or `err` depending on whether they're exported." -- Uber Go Style Guide, "Error Naming"

> "For custom error types, use the suffix `Error` instead." -- Uber Go Style Guide, "Error Naming"

This guidance explicitly supersedes the general rule about prefixing unexported globals with underscore.

# Prerequisites

- Understanding of Go export rules (uppercase = exported)
- Knowledge of sentinel errors vs custom error types (see error-types)
- Familiarity with `errors.Is` and `errors.As`

# Key Properties

1. **Sentinel error variables**: prefix with `Err` (exported) or `err` (unexported).
2. **Custom error types**: suffix with `Error` (exported) or `error` (unexported).
3. **Supersedes underscore convention**: Error variable naming takes priority over the general unexported-globals-with-underscore rule.
4. **API visibility signal**: The exported/unexported choice determines whether external packages can match the error.

# Construction / Recognition

**Sentinel error variables:**

```go
var (
  // Exported -- users match with errors.Is
  ErrBrokenLink = errors.New("link is broken")
  ErrCouldNotOpen = errors.New("could not open")

  // Unexported -- internal use with errors.Is
  errNotFound = errors.New("not found")
)
```

**Custom error types:**

```go
// Exported -- users match with errors.As
type NotFoundError struct {
  File string
}

func (e *NotFoundError) Error() string {
  return fmt.Sprintf("file %q not found", e.File)
}

// Unexported -- internal use with errors.As
type resolveError struct {
  Path string
}

func (e *resolveError) Error() string {
  return fmt.Sprintf("resolve %q", e.Path)
}
```

# Context & Application

These naming conventions make error declarations self-documenting. When reading code, the `Err` prefix signals a sentinel value to be checked with `errors.Is`, while the `Error` suffix signals a struct type to be checked with `errors.As`. This distinction helps code reviewers and consumers quickly understand the intended usage pattern.

# Examples

See Construction / Recognition above for the complete source examples.

# Relationships

- **error-types**: Defines when to use sentinel variables vs custom types; this card covers how to name them.
- **avoid-using-built-in-names**: Related concern about not shadowing Go's built-in `error` identifier.

# Common Errors

1. Naming a sentinel error variable `NotFoundErr` instead of `ErrNotFound` -- the `Err` prefix convention exists so all sentinel errors sort together and are recognizable at a glance.
2. Naming a custom error type `ErrNotFound` (the sentinel prefix) instead of `NotFoundError` (the type suffix).
3. Using the underscore prefix (`_errNotFound`) for unexported error variables -- the guide explicitly supersedes this convention for errors.

# Common Confusions

- **Prefix vs suffix**: Sentinel *values* get the `Err`/`err` *prefix*; custom *types* get the `Error`/`error` *suffix*. The asymmetry exists because variables conventionally prefix their category while types suffix their category in Go.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Error Naming" section.

# Verification Notes

Confidence: high. Both naming conventions (prefix for sentinels, suffix for types) are explicitly stated with code examples directly in the source.
