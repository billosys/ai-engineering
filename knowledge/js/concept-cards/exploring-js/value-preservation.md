---
# === CORE IDENTIFICATION ===
concept: Value-Preservation
slug: value-preservation

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Value-preservation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - logical-and-operator
  - logical-or-operator
  - short-circuiting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Value-preservation means that JavaScript's logical operators (`&&`, `||`) interpret operands as booleans for decision-making but return the original operand values unchanged, not boolean conversions.

# Core Definition

"*Value-preservation* means that operands are interpreted as booleans but returned unchanged" (Ch. 17, Section 17.5.1). This is why `12 || 'hello'` returns `12` (not `true`) and `0 || 'hello'` returns `'hello'` (not the boolean conversion).

# Prerequisites

- **falsy-and-truthy-values** -- operands are interpreted as booleans

# Key Properties

1. Operands are checked for truthiness/falsiness
2. The actual operand value is returned, not a boolean
3. Applies to `&&`, `||`, and `??`

# Construction / Recognition

```js
> 12 || 'hello'
12         // not true
> 0 || 'hello'
'hello'    // not true
```

# Context & Application

Value-preservation is what makes `||` and `??` useful for default values -- they return the actual value, not a boolean.

# Examples

From the source text:

```js
> 12 || 'hello'
12
> 0 || 'hello'
'hello'
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — decision is based on truthiness

## Enables
- Default value patterns using `||` and `??`

## Related
- **logical-and-operator** — value-preserving
- **logical-or-operator** — value-preserving
- **short-circuiting** — complementary property

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `0 || 'default'` to return `false`
  **Correction**: It returns `'default'` because `0` is falsy, so the second operand is returned unchanged.

# Common Confusions

- **Confusion**: Thinking `&&` and `||` return booleans
  **Clarification**: They return one of their operand values unchanged. Use `Boolean()` or `!!` for explicit boolean conversion.

# Source Reference

Chapter 17: Booleans, Section 17.5.1, lines 497-511.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
