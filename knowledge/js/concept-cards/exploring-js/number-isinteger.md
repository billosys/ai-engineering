---
# === CORE IDENTIFICATION ===
concept: Number.isInteger()
slug: number-isinteger

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
section: "Integer numbers in JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isInteger()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - safe-integers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Number.isInteger(x)` returns `true` if `x` is a number with no fractional part. Since JavaScript integers are just floats without decimal fractions, `1.0` is considered an integer.

# Core Definition

Integer numbers in JavaScript are floating point numbers without decimal fractions. `Number.isInteger()` checks this property. Since `1 === 1.0` is `true`, `Number.isInteger(1.0)` returns `true`. It does not coerce non-number values (Ch. 18, Section 18.9).

# Prerequisites

- **number-type** -- integers are a subset of numbers

# Key Properties

1. `Number.isInteger(1.0)` is `true` (integers are floats without fractions)
2. `Number.isInteger(1.5)` is `false`
3. Does not coerce: `Number.isInteger('1')` is `false`
4. Different from `Number.isSafeInteger()` which also checks range

# Construction / Recognition

```js
> Number.isInteger(1.0)
true
> Number.isInteger(1.5)
false
> 1 === 1.0
true
```

# Context & Application

Use to validate that a number has no fractional part before using it in integer-only contexts (array indices, bitwise operations).

# Examples

From the source text:

```js
> 1 === 1.0
true
> Number.isInteger(1.0)
true
> Number.isInteger(123.0)
true
```

# Relationships

## Builds Upon
- **number-type** — operates on numbers

## Enables
- Integer validation

## Related
- **safe-integers** — `Number.isSafeInteger()` checks both integer-ness and safe range

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Number.isInteger(1e300)` to be `false`
  **Correction**: Very large numbers have no fractional part representable in IEEE 754, so they are technically integers.

# Common Confusions

- **Confusion**: Thinking `Number.isInteger()` and `Number.isSafeInteger()` are the same
  **Clarification**: `isInteger()` only checks for no fraction. `isSafeInteger()` also checks that the value is within the safe range.

# Source Reference

Chapter 18: Numbers, Section 18.9, lines 1397-1455.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples provided
- Cross-reference status: verified
