---
# === CORE IDENTIFICATION ===
concept: Truncating Division
slug: truncating-division

# === CLASSIFICATION ===
category: language-mechanics
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "% is a remainder operator, not a modulo operator (bonus)"
chapter_number: 6
section: "Implementing rem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Math.trunc() division"
  - "rounding toward zero"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integer-division
extends:
  - integer-division
related:
  - remainder-operator
contrasts_with:
  - floor-division

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

Truncating division performs floating-point division and then rounds the quotient toward zero using `Math.trunc()`, discarding any fractional part.

# Core Definition

As described in "Deep JavaScript" Ch 6, truncating division is the form of integer division used by the remainder operator. It computes the quotient by dividing the dividend by the divisor and applying `Math.trunc()` to the result. The ECMAScript specification notes that JavaScript's `%` is computed via "truncating division."

# Prerequisites

- **Integer division** -- truncating division is one specific way to perform integer division
- **Math.trunc()** -- the JavaScript built-in that rounds toward zero

# Key Properties

1. Always rounds the quotient toward zero (not toward negative infinity).
2. `Math.trunc(7/3)` = 2; `Math.trunc(-7/3)` = -2.
3. Underlies the remainder (`rem`) operation.
4. Different from `Math.floor()`, which rounds toward negative infinity.

# Construction / Recognition

## To Construct/Create:
1. Perform floating-point division: `dividend / divisor`.
2. Apply `Math.trunc()` to the result.

## To Identify/Recognize:
1. The quotient is always the integer closest to zero.
2. Positive quotients are rounded down; negative quotients are rounded up (toward zero).

# Context & Application

Truncating division is the mechanism behind JavaScript's `%` operator. Understanding it is essential to predicting how `%` behaves with negative numbers.

# Examples

**Example 1** (Ch 6): Implementation of `rem` using truncating division:
```js
function rem(dividend, divisor) {
  const quotient = Math.trunc(dividend / divisor);
  return dividend - (divisor * quotient);
}
```

**Example 2** (Ch 6): Truncating vs floor for negative numbers:
```js
Math.trunc(-7 / 3)  // -2  (toward zero)
Math.floor(-7 / 3)  // -3  (toward negative infinity)
```

# Relationships

## Builds Upon
- **Integer division** -- truncating division is a specific form of integer division

## Enables
- **Remainder operator** -- the remainder operation is defined using truncating division

## Related
- **Math.trunc()** -- the JavaScript function that implements the truncation

## Contrasts With
- **Floor division** -- floor division rounds toward negative infinity, producing different results for negative quotients

# Common Errors

- **Error**: Confusing `Math.trunc()` with `Math.floor()` for negative numbers.
  **Correction**: `Math.trunc(-2.7)` is `-2` (toward zero); `Math.floor(-2.7)` is `-3` (toward negative infinity).

# Common Confusions

- **Confusion**: Truncating and flooring produce the same results.
  **Clarification**: They agree for positive numbers but differ for negative numbers. This difference is exactly why remainder and modulo diverge for negative operands.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Section 6.5.2, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit implementation with Math.trunc() provided in source code.
- Cross-reference status: verified against Ch 6 section 6.5.2
