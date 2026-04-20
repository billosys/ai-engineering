---
# === CORE IDENTIFICATION ===
concept: Naming Principles
slug: naming-principles

# === CLASSIFICATION ===
category: naming
subcategory: general
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Core guidelines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Go naming guidelines"
  - "naming is art not science"
  - "name context awareness"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - mixedcaps-naming
  - clarity-principle
  - concision-principle
  - underscores-in-go-names
  - google-package-names
  - receiver-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the general naming guidelines for Go?"
  - "How long should Go names be?"
  - "Should names repeat context that is already clear?"
---

# Quick Definition

Go names tend to be shorter than in other languages. Names should not feel repetitive when used, should take context into consideration, and should not repeat concepts that are already clear from the surrounding code.

# Core Definition

Naming in Go is "more art than science." Go names tend to be shorter than in many other languages, but the same general guidelines apply. Names should: (1) not feel repetitive when they are used, (2) take the context into consideration, and (3) not repeat concepts that are already clear. This is a core guideline -- part of the foundational rules all Go code is expected to follow. More specific naming guidance is provided in the Style Decisions document.

# Prerequisites

- **Go package system** -- Understanding that package names qualify all exported identifiers (e.g., `http.Get`)
- **Go export rules** -- Understanding that capitalization controls visibility

# Key Properties

1. Naming is more art than science
2. Go names tend to be shorter than in other languages
3. Names should not feel repetitive when used
4. Names should take context into consideration
5. Names should not repeat concepts already clear from context
6. More specific guidance deferred to Style Decisions

# Construction / Recognition

## To Apply:
1. Consider how the name reads at the call site, not just at the declaration
2. Do not include the type name in a variable name when the type is obvious
3. Do not repeat the package name in exported identifiers (e.g., `http.HTTPServer` is redundant)
4. Keep names short when scope is small and context is clear
5. Use longer names when scope is large or context is ambiguous

## To Recognize:
1. Names that stutter with their package: `config.ConfigManager`
2. Variable names that include the type: `userString`, `countInt`
3. Names that are longer than necessary given their scope and usage context

# Context & Application

Go's naming philosophy is tightly connected to its package system. Since every exported identifier is qualified by its package name at the call site (`http.Get`, not just `Get`), names can be shorter without losing clarity. Repeating context that the package name already provides (like `http.HTTPClient`) creates noise. The general guidelines here are the foundation; the Style Decisions document provides detailed rules for specific categories (variables, receivers, packages, constants, etc.).

# Examples

**Example 1 -- Context-aware naming**:

```go
// Good: package name provides context
http.Client    // not http.HTTPClient
json.Encoder   // not json.JSONEncoder

// Bad: repeats the package context
http.HTTPClient
json.JSONEncoder
```

**Example 2 -- Short names for small scopes**:

In a three-line loop, `i` is perfectly clear. In a 50-line function, `userIndex` provides needed context.

# Relationships

## Related
- **mixedcaps-naming** -- The mechanical capitalization convention for all Go names
- **clarity-principle** -- Good naming is the primary mechanism for achieving clarity
- **concision-principle** -- Short, non-repetitive names support high signal-to-noise ratio
- **underscores-in-go-names** -- Specific rules about when underscores are allowed
- **google-package-names** -- Package-level naming conventions
- **receiver-names** -- Method receiver naming conventions

# Common Errors

- **Error**: Repeating the package name in exported identifiers (`config.ConfigManager`)
  **Correction**: Use `config.Manager` -- the package name already provides context

- **Error**: Using excessively long names in small scopes
  **Correction**: Match name length to scope size; short scopes warrant short names

# Common Confusions

- **Confusion**: Thinking Go names should be as descriptive as Java names
  **Clarification**: Go names are deliberately shorter because the package qualifier and context provide additional information

- **Confusion**: Believing shorter is always better
  **Clarification**: Names should be as short as clarity allows. In large scopes or ambiguous contexts, longer names are appropriate.

# Source Reference

Chapter 2: Guide, Section "Core guidelines" > "Naming".

# Verification Notes

- Definition source: Directly from the "Naming" section of Core guidelines
- Confidence rationale: HIGH -- explicit three-point guideline from the source
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
