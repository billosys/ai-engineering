---
# === CORE IDENTIFICATION ===
concept: Util Packages
slug: util-packages

# === CLASSIFICATION ===
category: naming
subcategory: package-naming
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Util packages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "helper packages"
  - "common packages"
  - "generic package names"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package-names
extends: []
related:
  - package-size
  - import-renaming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should I avoid naming Go packages 'util' or 'helper'?"
  - "What is the problem with generic package names in Go?"
  - "How should I name packages instead of using 'common' or 'util'?"
---

# Quick Definition

Avoid naming Go packages `util`, `helper`, `common`, or similar generic names. These uninformative names make code harder to read and can cause import conflicts. Instead, name packages after what they provide.

# Core Definition

Go package names should be related to what the package provides. Names like `util`, `helper`, and `common` are poor choices because they convey no information about the package's purpose. These names make call sites harder to read since the reader cannot infer what a function does from the package qualifier. Additionally, broadly-used generic names are liable to cause import conflicts. The package name matters more for readability than the import path, because it appears at every call site. Consider what the call site will look like: `spannertest.NewDatabaseFromFile(...)` is far more informative than `test.NewDatabaseFromFile(...)`.

# Prerequisites

- **package-names** -- Understanding Go package naming conventions from the Decisions chapter

# Key Properties

1. Package names should describe what the package provides
2. Generic names like `util`, `helper`, `common` convey no useful information
3. Generic names used broadly cause import conflicts
4. The package name appears at every call site, so readability matters
5. Generic words can be used as *part* of a name (e.g., `testutil`) but not as the entire name

# Construction / Recognition

## To Apply:
1. Name the package after its domain or functionality (e.g., `spannertest`, `elliptic`)
2. Imagine reading the call site -- can you tell what the function does from the package name?
3. If you find yourself creating a `util` package, reconsider the package boundaries

## To Recognize:
1. Call sites read clearly: `elliptic.Marshal(curve, x, y)` vs `helper.Marshal(curve, x, y)`
2. Package name immediately suggests the domain

# Context & Application

This guidance reflects Go's design philosophy that package names are an integral part of the API. Since Go uses the package name as a qualifier at every call site, a descriptive package name acts as free documentation. When multiple teams or projects use generic names, import renaming becomes necessary, adding friction. The standard library exemplifies this: packages like `bytes`, `strings`, `crypto`, and `io` all have domain-specific names.

# Examples

**Example 1 -- Good descriptive package names**:

```go
// Good:
db := spannertest.NewDatabaseFromFile(...)
_, err := f.Seek(0, io.SeekStart)
b := elliptic.Marshal(curve, x, y)
```

**Example 2 -- Bad generic package names**:

```go
// Bad:
db := test.NewDatabaseFromFile(...)
_, err := f.Seek(0, common.SeekStart)
b := helper.Marshal(curve, x, y)
```

# Relationships

## Related
- **package-size** -- Proper package sizing helps avoid the temptation to create catch-all util packages
- **import-renaming** -- Generic names are more likely to require import renaming

## Contrasts With
(none)

# Common Errors

- **Error**: Creating a `util` or `helpers` package as a dumping ground for miscellaneous functions
  **Correction**: Group functions by domain and name packages accordingly

- **Error**: Using `common` as a shared package name across a large codebase
  **Correction**: Identify the specific functionality and name the package after it

# Common Confusions

- **Confusion**: Thinking the import path matters more than the package name
  **Clarification**: The package name appears at every call site; the import path is only visible in the import block

- **Confusion**: Believing this forbids words like "test" or "util" entirely
  **Clarification**: These words can be part of a name (e.g., `spannertest`, `testutil`) but should not be the whole name

# Source Reference

Chapter 4: Best Practices, Section "Naming" > "Util packages".

# Verification Notes

- Definition source: Directly from the "Util packages" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with clear examples
- Uncertainties: None
- Cross-reference status: References decisions#package-names, decisions#import-renaming
