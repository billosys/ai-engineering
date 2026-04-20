---
# === CORE IDENTIFICATION ===
concept: Import Blank
slug: import-blank

# === CLASSIFICATION ===
category: imports
subcategory: side-effects
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Import \"blank\" (import _)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "blank import"
  - "side-effect import"
  - "import underscore"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - import-grouping-google
  - import-renaming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When can I use blank imports (import _) in Go?"
  - "Why should blank imports be avoided in library packages?"
  - "Where should side-effect imports be placed?"
---

# Quick Definition

Side-effect imports (`import _ "package"`) may only be used in main packages or tests. Avoid blank imports in library packages to keep dependencies controllable and prevent conflicts.

# Core Definition

Packages imported only for their side effects (using `import _ "package"`) may only be imported in a main package or in tests that require them. Blank imports in library packages should be avoided even if the library indirectly depends on the side-effect package. Constraining side-effect imports to main packages helps control dependencies and makes it possible to write tests that rely on different imports without conflict or wasted build costs. Two exceptions exist: blank imports to bypass the nogo static checker's disallowed import check, and blank imports of the `embed` package when using `//go:embed` compiler directives. If a library package indirectly depends on a side-effect import in production, this should be documented (Google Go Style Guide, "Style Decisions", "Import blank").

# Prerequisites

- **Go import side effects** -- Understanding that some packages register functionality via `init()` functions
- **Go main package** -- Understanding that `main` is the entry point where dependencies are assembled

# Key Properties

1. Blank imports only in `main` packages or test files
2. Never in library packages (even if the library depends on the side effect)
3. Exception: bypassing nogo static checker
4. Exception: `embed` package for `//go:embed` directive
5. Document indirect side-effect dependencies in library packages
6. Placed in the last import group (group 4)

# Construction / Recognition

## To Apply:
1. Place side-effect imports only in `main` or `_test.go` files
2. If a library needs a side effect, document it and let the main package handle the import
3. Place blank imports in the last import group, separated by a blank line

## To Recognize:
1. Look for `import _` in library packages (non-main, non-test) -- these should be removed
2. Look for undocumented indirect side-effect dependencies in libraries

# Context & Application

Side-effect imports execute `init()` functions that register drivers, codecs, or other global state. Restricting them to `main` packages follows the dependency inversion principle: libraries declare what they need, and the main package assembles the concrete implementations. This makes testing easier (tests can substitute different implementations) and keeps build costs predictable.

# Examples

**Example 1 -- Good: blank imports in main package** (Decisions, "Import blank"):

```go
// Good: in main package
package main

import (
    "fmt"
    "os"

    _ "time/tzdata"
    _ "image/jpeg"
)
```

**Example 2 -- Good: blank import of embed for go:embed directive**:

```go
// Good: embed exception
package config

import _ "embed"

//go:embed config.yaml
var defaultConfig string
```

**Example 3 -- Bad: blank import in a library package** (Decisions, "Import blank"):

```go
// Bad: library package should not have side-effect imports
package imageutil

import (
    _ "image/jpeg"
    _ "image/png"
)
```

# Relationships

## Related
- **import-grouping-google** -- Blank imports form the fourth (last) import group
- **import-renaming** -- A different form of non-standard import handling

# Common Errors

- **Error**: Adding blank imports in library packages for convenience
  **Correction**: Move the blank import to the main package or test file; document the dependency in the library

- **Error**: Forgetting to document indirect side-effect dependencies
  **Correction**: Add documentation explaining which side-effect import the main package needs to include

# Common Confusions

- **Confusion**: Thinking blank imports are needed everywhere a side effect is used
  **Clarification**: Only the main package or test needs the blank import; the library can use the registered functionality without importing the registering package

- **Confusion**: Believing the `embed` blank import violates this rule
  **Clarification**: The `embed` package is an explicit exception because `//go:embed` requires it in the same file

# Source Reference

Chapter 3: Style Decisions, Section "Import blank (import _)".

# Verification Notes

- Definition source: Directly from the "Import blank" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with listed exceptions
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
