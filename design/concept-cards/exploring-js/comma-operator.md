---
# === CORE IDENTIFICATION ===
concept: Comma Operator
slug: comma-operator

# === CLASSIFICATION ===
category: types-values
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Comma operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The comma operator evaluates two operands from left to right and returns the value of the second operand. It is rarely used in modern JavaScript.

# Core Definition

"The comma operator has two operands, evaluates both of them and returns the second one" (Ch. 15, Section 15.7.1). It is one of JavaScript's least-used operators.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Evaluates both operands left to right
2. Returns the value of the second operand
3. Rarely used in modern JavaScript

# Construction / Recognition

```js
const result = (console.log('evaluated'), 'YES');
assert.equal(result, 'YES');
// Output: evaluated
```

# Context & Application

The comma operator is rarely needed. It was occasionally used in `for` loop headers to evaluate multiple expressions.

# Examples

From the source text:

```js
const result = (console.log('evaluated'), 'YES');
assert.equal(result, 'YES');
// Output: evaluated
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Nothing significant in modern code

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Confusing the comma operator with comma separators in array/object literals
  **Correction**: The comma operator only applies in expression contexts, not in literal declarations.

# Common Confusions

- **Confusion**: Thinking the comma operator returns an array of both values
  **Clarification**: It evaluates both but returns only the second value.

# Source Reference

Chapter 15: Operators, Section 15.7.1, lines 881-905.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
