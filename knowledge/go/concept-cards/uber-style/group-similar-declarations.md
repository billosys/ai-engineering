---
# === CORE IDENTIFICATION ===
concept: Group Similar Declarations
slug: group-similar-declarations

# === CLASSIFICATION ===
category: style
subcategory: organization
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Group Similar Declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "declaration grouping"
  - "grouped const/var/type"
  - "parenthesized declarations"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - be-consistent
  - avoid-overly-long-lines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I group const, var, type, and import declarations in Go?"
  - "Should unrelated declarations be grouped together?"
  - "Can grouped declarations be used inside functions?"
---

# Quick Definition

Group related `const`, `var`, `type`, and `import` declarations using Go's parenthesized declaration syntax. Only group declarations that are related; do not mix unrelated items in the same group. This also applies inside functions for adjacent variable declarations.

# Core Definition

Go supports grouping similar declarations using parenthesized syntax (`const (...)`, `var (...)`, `type (...)`, `import (...)`). The Uber style guide recommends using this syntax to visually organize related declarations together. However, only **related** declarations should be grouped -- unrelated items should remain in separate groups or standalone declarations.

An exception applies to variable declarations inside functions: adjacent variables should be grouped together using `var (...)` even if they are unrelated, because their proximity already signals they belong to the same scope.

# Prerequisites

Understanding of Go's declaration syntax for `const`, `var`, `type`, and `import`.

# Key Properties

1. **Related items only** -- Group declarations that are logically related. Do not mix unrelated constants or variables in the same group.
2. **Applies to all declaration types** -- Constants, variables, type definitions, and imports all support grouping.
3. **Works inside functions** -- Grouped declarations are not limited to package-level scope; they can be used within function bodies.
4. **Exception for adjacent locals** -- Inside functions, adjacent variable declarations should be grouped even if unrelated, for visual cleanliness.

# Construction / Recognition

## To Construct/Create:
1. Use `import (...)` for imports (standard practice).
2. Use `const (...)` for related constants (e.g., enum values for the same type).
3. Use `var (...)` for related package-level variables.
4. Use `type (...)` for related type definitions.
5. Keep unrelated declarations in separate groups.

## To Identify/Recognize:
1. Multiple standalone `const`, `var`, or `import` declarations that could be grouped.
2. A single parenthesized group mixing unrelated items (e.g., enum values mixed with environment variable names).

# Context & Application

- **Typical contexts**: Package-level declarations, enum definitions, import organization, local variable blocks in functions.
- **Common applications**: Organizing related constants, grouping configuration variables, declaring related types together.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 4): Group imports:

Bad:
```go
import "a"
import "b"
```

Good:
```go
import (
  "a"
  "b"
)
```

**Example 2** (source: Uber Go Style Guide, Ch 4): Group related declarations:

Bad:
```go
const a = 1
const b = 2

var a = 1
var b = 2

type Area float64
type Volume float64
```

Good:
```go
const (
  a = 1
  b = 2
)

var (
  a = 1
  b = 2
)

type (
  Area float64
  Volume float64
)
```

**Example 3** (source: Uber Go Style Guide, Ch 4): Do not group unrelated declarations:

Bad:
```go
type Operation int

const (
  Add Operation = iota + 1
  Subtract
  Multiply
  EnvVar = "MY_ENV"
)
```

Good:
```go
type Operation int

const (
  Add Operation = iota + 1
  Subtract
  Multiply
)

const EnvVar = "MY_ENV"
```

**Example 4** (source: Uber Go Style Guide, Ch 4): Group adjacent variables inside functions:

Bad:
```go
func (c *client) request() {
  caller := c.name
  format := "json"
  timeout := 5*time.Second
  var err error

  // ...
}
```

Good:
```go
func (c *client) request() {
  var (
    caller  = c.name
    format  = "json"
    timeout = 5*time.Second
    err error
  )

  // ...
}
```

# Relationships

- **Related to** `be-consistent`: Grouping conventions should be applied consistently throughout a package.
- **Related to** `avoid-overly-long-lines`: Grouping declarations can sometimes help keep the code compact and readable.

# Common Errors

1. **Mixing unrelated constants in one group** -- Grouping enum values with environment variable names or unrelated configuration constants reduces clarity.
2. **Not grouping at all** -- Using individual `import`, `const`, or `var` statements when grouping would improve readability.
3. **Over-grouping** -- Forcing unrelated package-level variables into a single `var (...)` block when they serve different purposes.

# Common Confusions

1. **"Group everything" vs. "group related things"** -- The rule is to group related items. At the package level, unrelated items should be in separate groups. Inside functions, adjacent variables are the exception.
2. **Grouping vs. import ordering** -- Grouping is about using parenthesized syntax. Import ordering (stdlib first, then external) is a separate concern addressed in the "Import Group Ordering" section.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Style" (Ch 4)
- Section: "Group Similar Declarations"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with multiple Bad/Good examples covering imports, constants, variables, types, and function-local declarations.
