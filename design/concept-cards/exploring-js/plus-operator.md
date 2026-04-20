---
# === CORE IDENTIFICATION ===
concept: Plus Operator
slug: plus-operator

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
section: "The plus operator (+)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "binary plus"
  - "addition operator"
  - "string concatenation operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - operator-coercion
  - toprimitive
extends: []
related:
  - string-concatenation
  - converting-to-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

The JavaScript `+` operator has two modes: if either operand is a string after coercion to primitive, it concatenates strings; otherwise, it adds numbers.

# Core Definition

As Rauschmayer describes: "First, it converts both operands to primitive values (by default, conversion to primitive prefers numbers). Then it switches to one of two modes: String mode: If one of the two primitive values is a string, then it converts the other one to a string, concatenates both strings, and returns the result. Number mode: Otherwise, It converts both operands to numbers, adds them, and returns the result" (Ch. 15, Section 15.3).

# Prerequisites

- **operator-coercion** -- understanding how operands are automatically converted
- **toprimitive** -- the algorithm converting objects to primitives

# Key Properties

1. Operands are first converted to primitives (default hint: NUMBER)
2. If either primitive is a string, switches to string concatenation mode
3. Otherwise, converts both to numbers and adds
4. ES1 feature

# Construction / Recognition

```js
// String mode
'There are ' + 3 + ' items' // 'There are 3 items'

// Number mode
4 + true // 5 (Number(true) is 1)
```

# Context & Application

The dual behavior of `+` is one of JavaScript's most common sources of confusion. Template literals (backtick strings) are now preferred for string assembly to avoid ambiguity.

# Examples

From the source text:

```js
> 'There are ' + 3 + ' items'
'There are 3 items'

> 4 + true
5
// Number(true) is 1
```

# Relationships

## Builds Upon
- **operator-coercion** — the plus operator coerces its operands
- **toprimitive** — objects are converted to primitives before the mode is chosen

## Enables
- **string-concatenation** — `+` is one way to concatenate strings

## Related
- **converting-to-number** — number mode uses numeric conversion

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `[] + []` to produce an empty array
  **Correction**: Both arrays are coerced to empty strings, so the result is `''`.

# Common Confusions

- **Confusion**: Thinking `+` always does addition
  **Clarification**: If either operand (after ToPrimitive) is a string, `+` does string concatenation instead.

# Source Reference

Chapter 15: Operators, Section 15.3, lines 216-251.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit algorithm description in source
- Cross-reference status: verified
