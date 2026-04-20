---
# === CORE IDENTIFICATION ===
concept: Use any Over interface{}
slug: use-any

# === CLASSIFICATION ===
category: language
subcategory: type-aliases
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Use any"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "any type alias"
  - "empty interface alias"
  - "interface{} replacement"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I use any or interface{} in Go?"
  - "What is the any type in Go?"
  - "When was any introduced in Go?"
  - "Is any equivalent to interface{}?"
---

# Quick Definition

Prefer `any` over `interface{}` as the alias for the empty interface in new Go code. Introduced in Go 1.18, `any` is equivalent to `interface{}` and is more concise.

# Core Definition

Go 1.18 introduced `any` as a type alias for `interface{}`. Because it is an alias, `any` is equivalent to `interface{}` in many situations and in others it is easily interchangeable via an explicit conversion. The style guidance is to prefer `any` in new code for brevity and readability.

# Prerequisites

- **Go 1.18 or later** -- The `any` alias was introduced in Go 1.18
- **Understanding of the empty interface** -- `interface{}` accepts any type in Go

# Key Properties

1. **Type alias**: `any` is a language-level alias for `interface{}`, not a new type
2. **Full equivalence**: The two are interchangeable in nearly all contexts
3. **Explicit conversion**: Where they are not directly interchangeable, an explicit conversion suffices
4. **Preferred in new code**: Style guidance favors `any` for conciseness

# Construction / Recognition

## To Apply:
1. Use `any` wherever you would have written `interface{}` in new code
2. When updating existing code, replace `interface{}` with `any` where practical

## To Recognize:
1. Code using `interface{}` in Go 1.18+ codebases could be updated to use `any`
2. Code using `any` is following current style guidance

# Context & Application

This is a straightforward modernization preference. Since `any` is shorter and reads more naturally, it reduces visual noise in function signatures and type declarations. Existing code using `interface{}` does not need to be changed urgently but should be updated when convenient.

# Examples

**Example 1 -- Preferred usage**:

```go
// Good:
func process(v any) string {
    return fmt.Sprintf("%v", v)
}
```

**Example 2 -- Older style**:

```go
// Acceptable but less preferred in new code:
func process(v interface{}) string {
    return fmt.Sprintf("%v", v)
}
```

# Relationships

(No specific related cards in this extraction batch.)

# Common Errors

- **Error**: Using `interface{}` in new Go 1.18+ code out of habit
  **Correction**: Use `any` for cleaner, more modern code.

# Common Confusions

- **Confusion**: Thinking `any` is a new type distinct from `interface{}`
  **Clarification**: `any` is a type alias, not a new type. They are semantically identical.

# Source Reference

Chapter 3: Style Decisions, Section "Use any".

# Verification Notes

- Definition source: Directly from the "Use any" section of the Style Decisions document
- Confidence rationale: HIGH -- the guidance is explicit and brief
- Uncertainties: None
- Cross-reference status: Standalone concept
