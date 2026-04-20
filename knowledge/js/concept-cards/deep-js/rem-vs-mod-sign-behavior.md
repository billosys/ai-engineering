---
# === CORE IDENTIFICATION ===
concept: Remainder vs Modulo Sign Behavior
slug: rem-vs-mod-sign-behavior

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
section: "Similarities and differences between rem and mod"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "rem vs mod with negative numbers"
  - "sign rule for remainder and modulo"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - remainder-operator
  - modulo-operator
extends: []
related:
  - truncating-division
  - floor-division
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

Remainder and modulo only differ when the dividend and divisor have different signs: remainder takes the sign of the dividend, modulo takes the sign of the divisor.

# Core Definition

As described in "Deep JavaScript" Ch 6, Section 6.4: "rem and mod are quite similar -- they only differ if dividend and divisor have different signs." With `rem`, the result has the same sign as the dividend (first operand). With `mod`, the result has the same sign as the divisor (second operand). When both operands share the same sign, `rem` and `mod` produce identical results.

# Prerequisites

- **Remainder operator** -- understanding of how `rem` computes results
- **Modulo operator** -- understanding of how `mod` computes results

# Key Properties

1. When dividend and divisor have the same sign, `rem` and `mod` produce identical results.
2. When they differ in sign, the results differ.
3. `rem` result sign = dividend sign (first operand).
4. `mod` result sign = divisor sign (second operand).

# Construction / Recognition

## To Construct/Create:
1. Check if dividend and divisor have the same sign.
2. If yes, `rem` and `mod` give the same answer.
3. If no, apply the sign rule: `rem` follows dividend, `mod` follows divisor.

## To Identify/Recognize:
1. Given `a op b`, check the sign of the result relative to `a` (dividend) and `b` (divisor).
2. If result sign matches `a`, it is remainder. If it matches `b`, it is modulo.

# Context & Application

This distinction is critical when porting algorithms between languages (e.g., JavaScript to Python or vice versa) or when implementing cyclic indexing with negative values.

# Examples

**Example 1** (Ch 6): Complete comparison table:
```js
// rem: result sign follows dividend
 5 rem  4 //  1
-5 rem  4 // -1
 5 rem -4 //  1
-5 rem -4 // -1

// mod: result sign follows divisor
 5 mod  4 //  1
-5 mod  4 //  3
 5 mod -4 // -3
-5 mod -4 // -1
```

**Example 2** (Ch 6): JavaScript vs Python:
```js
// JavaScript (remainder): -7 % 6 = -1
// Python (modulo):        -7 % 6 = 5
```

# Relationships

## Builds Upon
- **Remainder operator** -- one of the two operations being compared
- **Modulo operator** -- the other operation being compared

## Enables
- **Cross-language arithmetic porting** -- knowing the sign rule prevents bugs when moving code between languages

## Related
- **Truncating division** -- underlies remainder's sign behavior
- **Floor division** -- underlies modulo's sign behavior

## Contrasts With
(none -- this card describes the contrast itself)

# Common Errors

- **Error**: Assuming JavaScript's `%` with a negative dividend will wrap into a positive range.
  **Correction**: JavaScript's `%` is remainder and preserves the dividend's sign. Use a manual `mod` function for wrapping behavior.

# Common Confusions

- **Confusion**: The difference between `rem` and `mod` only matters for edge cases.
  **Clarification**: Any negative dividend with a positive divisor (a common scenario in cyclic computations) will produce different results between `rem` and `mod`.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Section 6.4, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit comparison table with all four sign combinations provided in source.
- Cross-reference status: verified against Ch 6 sections 6.4 and 6.6
