---
# === CORE IDENTIFICATION ===
concept: Floor Division
slug: floor-division

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
section: "Implementing mod"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Math.floor() division"
  - "rounding toward negative infinity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integer-division
extends:
  - integer-division
related:
  - modulo-operator
contrasts_with:
  - truncating-division

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

Floor division performs floating-point division and then rounds the quotient toward negative infinity using `Math.floor()`.

# Core Definition

As described in "Deep JavaScript" Ch 6, floor division is the form of integer division used by the modulo operator. It computes the quotient by dividing the dividend by the divisor and applying `Math.floor()` to the result. This is what distinguishes modulo from remainder: modulo uses floor division, remainder uses truncating division.

# Prerequisites

- **Integer division** -- floor division is one specific way to perform integer division
- **Math.floor()** -- the JavaScript built-in that rounds toward negative infinity

# Key Properties

1. Always rounds the quotient toward negative infinity.
2. `Math.floor(7/3)` = 2; `Math.floor(-7/3)` = -3.
3. Underlies the modulo (`mod`) operation.
4. Python's `//` operator is floor division.

# Construction / Recognition

## To Construct/Create:
1. Perform floating-point division: `dividend / divisor`.
2. Apply `Math.floor()` to the result.

## To Identify/Recognize:
1. The quotient is always rounded down (toward negative infinity), regardless of sign.

# Context & Application

Floor division is needed to implement modulo in JavaScript, since the language only provides the remainder operator natively. Understanding floor division explains why Python's `%` and JavaScript's `%` differ for negative numbers.

# Examples

**Example 1** (Ch 6): Implementation of `mod` using floor division:
```js
function mod(dividend, divisor) {
  const quotient = Math.floor(dividend / divisor);
  return dividend - (divisor * quotient);
}
```

**Example 2** (Ch 6): Floor vs truncating for negative quotients:
```js
Math.floor(-7 / 3)  // -3  (toward negative infinity)
Math.trunc(-7 / 3)  // -2  (toward zero)
```

# Relationships

## Builds Upon
- **Integer division** -- floor division is a specific form of integer division

## Enables
- **Modulo operator** -- the modulo operation is defined using floor division

## Related
- **Math.floor()** -- the JavaScript function that implements the floor rounding

## Contrasts With
- **Truncating division** -- truncating rounds toward zero, producing different results for negative quotients

# Common Errors

- **Error**: Assuming `Math.floor()` and `Math.trunc()` are interchangeable.
  **Correction**: They differ for negative numbers: `Math.floor(-1.5)` is `-2`, `Math.trunc(-1.5)` is `-1`.

# Common Confusions

- **Confusion**: Floor division and truncating division are the same.
  **Clarification**: They agree for positive quotients but diverge for negative quotients, which is exactly why `rem` and `mod` produce different results for mixed-sign operands.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Section 6.5.3, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit implementation with Math.floor() provided in source code.
- Cross-reference status: verified against Ch 6 section 6.5.3
