---
# === CORE IDENTIFICATION ===
concept: Prefix Unexported Globals with Underscore
slug: prefix-unexported-globals-with-underscore

# === CLASSIFICATION ===
category: style
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Prefix Unexported Globals with _"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "underscore prefix for globals"
  - "unexported global naming"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - top-level-variable-declarations
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should I prefix unexported top-level variables with an underscore?"
  - "How do I distinguish package-level variables from local variables?"
  - "What is the exception for error variable naming?"
---

# Quick Definition

Prefix unexported top-level `var`s and `const`s with `_` to visually distinguish them as global symbols and prevent accidental shadowing.

# Core Definition

Unexported top-level `var`s and `const`s should be prefixed with `_` to make it clear at every usage site that they are global (package-scoped) symbols. Top-level variables and constants have package scope, and using a generic name without the prefix makes it easy to accidentally shadow them with a local variable of the same name in a different file. The `_` prefix provides a visual marker that immediately signals "this is a package-level symbol" (Uber Go Style Guide, "Prefix Unexported Globals with _").

Exception: unexported error values may use the prefix `err` without the underscore (e.g., `errNotFound`).

# Prerequisites

- **Go package scope** -- Understanding that top-level declarations are visible to all files in the package
- **Go variable shadowing** -- Understanding that a local variable can shadow a package-level variable without a compile error

# Key Properties

1. Prefix unexported top-level `var`s and `const`s with `_` (e.g., `_defaultPort`)
2. The prefix visually distinguishes globals from locals at every usage site
3. Prevents accidental shadowing by local variables with the same name
4. Exception: error values use `err` prefix instead (e.g., `errNotFound`)
5. Does not apply to exported identifiers (they start with uppercase)

# Construction / Recognition

## To Apply:
1. For every unexported package-level `var` or `const`, add a `_` prefix
2. Use `_defaultPort` instead of `defaultPort`, `_maxRetries` instead of `maxRetries`
3. For error values, use `err` prefix instead: `errNotFound`, `errTimeout`

## To Recognize:
1. Look for unexported top-level variables without the `_` prefix -- these risk accidental shadowing
2. Look for local variables that share a name with a package-level variable -- the `_` prefix would have prevented this

# Context & Application

This naming convention solves a subtle but real problem in Go. Because Go allows variable shadowing without warning, a developer in one file might declare `defaultPort := 9090` without realizing that `defaultPort` is already a package-level constant in another file. If the local declaration is later removed, the code silently starts using the package-level value -- a bug that is hard to detect. The `_` prefix makes the distinction obvious: `_defaultPort` is clearly a global, and a local `defaultPort` clearly is not.

# Examples

**Example 1 -- Bad** (Style, "Prefix Unexported Globals with _"):

Without prefix, shadowing goes unnoticed:

```go
// foo.go

const (
  defaultPort = 8080
  defaultUser = "user"
)

// bar.go

func Bar() {
  defaultPort := 9090
  ...
  fmt.Println("Default port", defaultPort)

  // We will not see a compile error if the first line of
  // Bar() is deleted.
}
```

**Example 2 -- Good** (Style, "Prefix Unexported Globals with _"):

With prefix, globals are clearly distinguished:

```go
// foo.go

const (
  _defaultPort = 8080
  _defaultUser = "user"
)
```

# Relationships

## Related
- **top-level-variable-declarations** -- Governs how top-level variables are declared; the underscore prefix is applied on top of those declarations
- **package-names** -- Both conventions address naming at the package level

# Common Errors

- **Error**: Omitting the `_` prefix on unexported package-level variables
  **Correction**: Add the `_` prefix: `_defaultTimeout` instead of `defaultTimeout`

- **Error**: Applying the `_` prefix to error values
  **Correction**: Error values use the `err` prefix instead: `errNotFound`, not `_notFound`

- **Error**: Applying the `_` prefix to local variables inside functions
  **Correction**: The `_` prefix is only for package-level (top-level) declarations, not function-local variables

# Common Confusions

- **Confusion**: Thinking the `_` prefix means "unused" (like the blank identifier `_`)
  **Clarification**: The `_` prefix is a naming convention for globals, not the blank identifier. `_defaultPort` is a usable variable; `_` alone is the blank identifier that discards values.

- **Confusion**: Wondering if this applies to unexported functions
  **Clarification**: This convention applies only to top-level `var`s and `const`s, not to functions or types

# Source Reference

Chapter 4: Style, Section "Prefix Unexported Globals with _".

# Verification Notes

- Definition source: Directly from the "Prefix Unexported Globals with _" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides explicit guidance with a bad/good example and states the exception for error values
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
