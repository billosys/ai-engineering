---
# === CORE IDENTIFICATION ===
concept: Remainder Operator
slug: remainder-operator

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Numbers"
chapter_number: 18
pdf_page: null
section: "% is a remainder operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "%"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript's `%` operator is a remainder operator (not modulo): its result has the sign of the first operand, which matters for negative numbers.

# Core Definition

"`%` is a remainder operator, not a modulo operator. Its result has the sign of the first operand" (Ch. 18, Section 18.3.1.1). For example, `5 % 3` is `2` but `-5 % 3` is `-2` (not `1` as a true modulo operation would produce).

# Prerequisites

- **number-type** -- operates on numbers

# Key Properties

1. Result sign matches the first (left) operand
2. Not a true modulo operation
3. ES1 feature

# Construction / Recognition

```js
> 5 % 3
2
> -5 % 3
-2
```

# Context & Application

The distinction between remainder and modulo matters when working with negative numbers in algorithms like circular buffer indexing or wrapping coordinates.

# Examples

From the source text:

```js
> 5 % 3
2
> -5 % 3
-2
```

# Relationships

## Builds Upon
- **number-type** — operates on numbers

## Enables
- Remainder calculations

## Related
- None

## Contrasts With
- None (a true modulo operation is not built into JavaScript)

# Common Errors

- **Error**: Expecting `%` to behave as mathematical modulo for negative numbers
  **Correction**: `-5 % 3` is `-2`, not `1`. For true modulo, use `((n % m) + m) % m`.

# Common Confusions

- **Confusion**: Calling `%` the "modulo operator"
  **Clarification**: JavaScript's `%` is technically a remainder operator. The difference only matters with negative operands.

# Source Reference

Chapter 18: Numbers, Section 18.3.1.1, lines 473-489.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit clarification with examples
- Cross-reference status: verified
