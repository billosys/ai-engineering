---
# === CORE IDENTIFICATION ===
concept: "JavaScript % Operator"
slug: javascript-percent-operator

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
section: "JavaScript's % operator computes the remainder"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "percent operator"
  - "JS modulo operator (misnomer)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - remainder-operator
extends:
  - remainder-operator
related:
  - rem-vs-mod-sign-behavior
  - truncating-division
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between the remainder operator and the modulo operator?"
---

# Quick Definition

JavaScript's `%` operator computes the remainder (not the modulus), using truncating division internally as specified by ECMAScript.

# Core Definition

As described in "Deep JavaScript" Ch 6, Section 6.6.1: "JavaScript's `%` operator computes the remainder." The ECMAScript specification confirms that `%` is computed via "truncating division." This means that for negative dividends, the result is negative -- unlike Python's `%`, which computes the modulus and yields non-negative results for positive divisors.

# Prerequisites

- **Remainder operator** -- JavaScript's `%` is an implementation of the remainder operation
- **Truncating division** -- the underlying integer division strategy

# Key Properties

1. `%` computes remainder, not modulo.
2. Result sign matches the dividend (first operand).
3. Equivalent to `dividend - divisor * Math.trunc(dividend / divisor)`.
4. The ECMAScript specification uses the term "truncating division."

# Construction / Recognition

## To Construct/Create:
1. Use the `%` infix operator: `dividend % divisor`.

## To Identify/Recognize:
1. Test with a negative dividend and positive divisor: `(-7) % 6` yields `-1` (not `5`).

# Context & Application

Understanding that `%` is remainder is essential for correct JavaScript programming with negative numbers. When modulo behavior is needed (e.g., cyclic array indexing), a custom function must be used.

# Examples

**Example 1** (Ch 6): JavaScript's `%` with negative dividend:
```js
> 7 % 6
1
> -7 % 6
-1
```

**Example 2** (Ch 6): ECMAScript uses modulo internally for `>>>`:
```js
> 2**32 >>> 0
0
> (2**32)+1 >>> 0
1
```

**Example 3** (Ch 6): Typed Array wrapping uses modulo semantics:
```js
const tarr = new Uint8Array(1);
tarr[0] = 256;
assert.equal(tarr[0], 0);   // 256 mod 256 = 0
tarr[0] = 257;
assert.equal(tarr[0], 1);   // 257 mod 256 = 1
```

# Relationships

## Builds Upon
- **Remainder operator** -- `%` is JavaScript's implementation of remainder
- **Truncating division** -- the rounding strategy used internally

## Enables
- **Custom modulo function** -- knowing `%` is remainder motivates implementing true modulo when needed

## Related
- **Rem vs mod sign behavior** -- explains when `%` and true modulo diverge

## Contrasts With
(none at this specificity level)

# Common Errors

- **Error**: Writing `index % length` expecting it to wrap negative indices into `[0, length)`.
  **Correction**: Use `((index % length) + length) % length` or a dedicated `mod` function.

# Common Confusions

- **Confusion**: The ECMAScript spec's internal use of "modulo" means `%` is modulo.
  **Clarification**: The spec uses modulo internally (e.g., for `>>>` and Typed Arrays), but the `%` operator exposed to developers is remainder, not modulo.

# Source Reference

Chapter 6: "% is a remainder operator, not a modulo operator (bonus)", Section 6.6.1, lines 2812-2898.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit statement in source and ECMAScript specification reference.
- Cross-reference status: verified against Ch 6 section 6.6
