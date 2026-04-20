---
# === CORE IDENTIFICATION ===
concept: Exponentiation Operator
slug: exponentiation-operator

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
section: "Binary arithmetic operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "**"
  - "Math.pow()"

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

The exponentiation operator (`**`) raises a base to a power: `4 ** 2` is 16. Introduced in ES2016, it is equivalent to `Math.pow()`.

# Core Definition

The `**` operator computes `x` raised to the power of `y`. It was introduced in ES2016 and is equivalent to `Math.pow(x, y)`. It also works with bigints (Ch. 18, Section 18.3.1).

# Prerequisites

- **number-type** -- operates on numbers

# Key Properties

1. `x ** y` computes x to the power of y (ES2016)
2. Equivalent to `Math.pow(x, y)` (ES1)
3. Right-associative: `2 ** 3 ** 2` is `2 ** 9` = `512`
4. Works with bigints: `2n ** 53n`

# Construction / Recognition

```js
4 ** 2    // 16
25 ** 0.5 // 5 (square root)
2 ** 53   // 9007199254740992
```

# Context & Application

The `**` operator is cleaner than `Math.pow()` for exponentiation and works with bigints.

# Examples

From the source text:

```js
> 4 ** 2
16
> Math.pow(2, 3)
8
> Math.pow(25, 0.5)
5
```

# Relationships

## Builds Upon
- **number-type** — operates on numbers

## Enables
- Power calculations

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `-2 ** 2` to be `4`
  **Correction**: This is a syntax error in JavaScript. Use `(-2) ** 2` for `4`.

# Common Confusions

- **Confusion**: Thinking `**` is left-associative like other arithmetic operators
  **Clarification**: `**` is right-associative: `2 ** 3 ** 2` equals `2 ** 9`, not `8 ** 2`.

# Source Reference

Chapter 18: Numbers, Section 18.3.1, lines 282-471.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit in operator table
- Cross-reference status: verified
