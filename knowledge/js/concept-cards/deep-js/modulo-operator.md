---
# === CORE IDENTIFICATION ===
concept: Modulo Operator
slug: modulo-operator

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
section: "An intuitive understanding of the modulo operation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "mod"
  - "modulus operation"
  - "% operator (Python)"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - remainder-operator
  - floor-division
  - integer-division
contrasts_with:
  - remainder-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

The modulo operator (`mod`) maps a dividend into a range determined by the divisor, where the result always has the same sign as the divisor.

# Core Definition

As described in "Deep JavaScript" Ch 6, the modulo operation `x mod n` maps `x` into the range `[0, n)` (for positive `n`). The range repeats cyclically over all integers, including negative ones. The key property is that **the result has the same sign as the divisor** (the second operand). JavaScript does not have a built-in modulo operator; its `%` computes the remainder instead.

# Prerequisites

- **Integer division** -- modulo is defined in terms of integer division
- **Sign (positive/negative numbers)** -- the sign of the divisor determines the sign of the result

# Key Properties

1. The result always has the same sign as the divisor (second operand).
2. For a positive divisor `n`, the result is always in the range `[0, n)`.
3. When both operands are positive, modulo and remainder produce the same result.
4. JavaScript's `%` is NOT a modulo operator (Python's `%` is).

# Construction / Recognition

## To Construct/Create:
1. Divide the dividend by the divisor.
2. Floor the quotient using `Math.floor()`.
3. Compute `dividend - (divisor * floored_quotient)`.

## To Identify/Recognize:
1. If the result always falls in `[0, divisor)` for positive divisors regardless of dividend sign, it is modulo.
2. If the result has the same sign as the second operand (divisor), it is modulo.

# Context & Application

Modulo is used for cyclic/wrapping computations (e.g., clock arithmetic, array index wrapping, converting to Typed Array ranges). The ECMAScript specification uses modulo internally (e.g., `x mod 2**32` for the `>>>` operator), even though the `%` operator exposed to programmers is remainder.

# Examples

**Example 1** (Ch 6): Modulo mapping for positive and negative integers:
```
x:       -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7
x mod 3:  2  0  1  2  0  1  2  0  1  2  0  1  2  0  1
```

**Example 2** (Ch 6): Modulo with different sign combinations:
```js
 5 mod  4 //  1
-5 mod  4 //  3
 5 mod -4 // -3
-5 mod -4 // -1
```

**Example 3** (Ch 6): ECMAScript uses modulo for `>>>` operator:
```js
2**32 >>> 0           // 0  (2**32 mod 2**32 = 0)
(2**32)+1 >>> 0       // 1
(-1 >>> 0) === (2**32)-1  // true
```

# Relationships

## Builds Upon
- **Integer division** -- modulo is defined as the leftover after floor-based integer division

## Enables
- **Cyclic index computation** -- modulo maps arbitrary integers into a fixed range

## Related
- **Floor division** -- modulo relies on floor division internally

## Contrasts With
- **Remainder operator** -- remainder uses truncating division and result takes dividend's sign

# Common Errors

- **Error**: Using JavaScript's `%` operator expecting modulo behavior with negative numbers.
  **Correction**: Implement modulo manually: `function mod(n, d) { return ((n % d) + d) % d; }` or use `Math.floor`-based division.

# Common Confusions

- **Confusion**: JavaScript's `%` is a modulo operator.
  **Clarification**: JavaScript's `%` is a remainder operator. The ECMAScript specification itself notes that `%` is computed via "truncating division," which produces remainder, not modulo.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Sections 6.3-6.4, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with detailed examples and sign-behavior tables provided in the source.
- Cross-reference status: verified against Ch 6 sections 6.3, 6.4, and 6.6
