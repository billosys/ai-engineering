---
# === CORE IDENTIFICATION ===
concept: Remainder Operator
slug: remainder-operator

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
section: "Remainder operator rem vs. modulo operator mod"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "rem"
  - "% operator (JavaScript)"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - modulo-operator
  - truncating-division
  - integer-division
contrasts_with:
  - modulo-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

The remainder operator (`rem`) computes the amount left over after dividing the dividend by the divisor, where the result has the same sign as the dividend.

# Core Definition

As described in "Deep JavaScript" Ch 6, the remainder operation repeatedly subtracts (or adds) the divisor from the dividend until the absolute value of the result is smaller than the absolute value of the divisor. The key distinguishing property is that **the result has the same sign as the dividend** (the first operand). JavaScript's `%` operator computes the remainder, not the modulus.

# Prerequisites

- **Integer division** -- understanding how dividing integers produces a quotient and leftover
- **Sign (positive/negative numbers)** -- the sign of the dividend determines the sign of the result

# Key Properties

1. The result always has the same sign as the dividend (first operand).
2. When both operands are positive, remainder and modulo produce the same result.
3. When operands have different signs, remainder and modulo differ.
4. JavaScript's `%` operator is a remainder operator, despite often being called "modulo."

# Construction / Recognition

## To Construct/Create:
1. Divide the dividend by the divisor.
2. Truncate the quotient toward zero using `Math.trunc()`.
3. Compute `dividend - (divisor * truncated_quotient)`.

## To Identify/Recognize:
1. If the result of `%` has the same sign as the first operand (dividend), it is a remainder operation.
2. JavaScript's `%` always behaves this way.

# Context & Application

The remainder operator is used whenever you need the leftover after division. In JavaScript, `%` is the built-in remainder operator. It is commonly mistaken for modulo, which matters when dealing with negative numbers.

# Examples

**Example 1** (Ch 6): Basic remainder with positive numbers:
```js
7 % 3 // 1
```

**Example 2** (Ch 6): Remainder with a negative dividend -- result is negative:
```js
-7 % 6 // -1
```

**Example 3** (Ch 6): Sign pattern mapping:
```
x:       -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7
x rem 3: -1  0 -2 -1  0 -2 -1  0  1  2  0  1  2  0  1
```

# Relationships

## Builds Upon
- **Integer division** -- remainder is defined in terms of integer division

## Enables
- **Truncating division** -- remainder uses truncating (toward zero) division internally

## Related
- **Integer division** -- the quotient and remainder together fully describe a division result

## Contrasts With
- **Modulo operator** -- modulo uses floor division and the result takes the sign of the divisor

# Common Errors

- **Error**: Assuming JavaScript's `%` works like Python's `%` (which is modulo).
  **Correction**: JavaScript's `%` is remainder; with negative dividends, it produces negative results, while Python's `%` would produce positive results.

# Common Confusions

- **Confusion**: Remainder and modulo are the same thing.
  **Clarification**: They differ when the dividend and divisor have different signs. Remainder takes the sign of the dividend; modulo takes the sign of the divisor.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Sections 6.1-6.2, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition and detailed examples provided in the source text.
- Cross-reference status: verified against Ch 6 sections 6.1, 6.2, and 6.4
