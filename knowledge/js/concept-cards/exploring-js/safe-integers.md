---
# === CORE IDENTIFICATION ===
concept: Safe Integers
slug: safe-integers

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
section: "Safe integers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Number.MAX_SAFE_INTEGER"
  - "Number.MIN_SAFE_INTEGER"
  - "Number.isSafeInteger()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ieee-754-floating-point
extends: []
related:
  - bigint-type
  - integer-ranges
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A safe integer is one that is represented by exactly one JavaScript number, within the range [-(2^53)+1, 2^53-1]. Beyond this range, multiple mathematical integers map to the same JavaScript number.

# Core Definition

"An integer is *safe* if it is represented by exactly one JavaScript number." The safe range is [-(2^53)+1, 2^53-1]. Beyond safe integers, there are gaps between representable numbers: for example, `2**53` and `2**53 + 1` produce the same JavaScript number. Use `Number.isSafeInteger()`, `Number.MAX_SAFE_INTEGER` (2^53 - 1), and `Number.MIN_SAFE_INTEGER` (-(2^53 - 1)) to work with safe integers (Ch. 18, Section 18.9.4).

# Prerequisites

- **ieee-754-floating-point** -- safe integers are limited by the 52-bit fraction

# Key Properties

1. Range: [-(2^53)+1, 2^53-1]
2. `Number.MAX_SAFE_INTEGER` = 9007199254740991 (2^53 - 1)
3. `Number.MIN_SAFE_INTEGER` = -9007199254740991
4. `Number.isSafeInteger()` checks safety (returns `false` for non-integers and strings)
5. Beyond safe range, gaps appear between representable integers
6. A computation `a op b` is correct only if `isSafeInteger(a) && isSafeInteger(b) && isSafeInteger(a op b)`

# Construction / Recognition

```js
assert.equal(Number.MAX_SAFE_INTEGER, (2 ** 53) - 1);
assert.equal(Number.isSafeInteger(5), true);
assert.equal(Number.isSafeInteger(5.1), false);
assert.equal(Number.isSafeInteger(Number.MAX_SAFE_INTEGER + 1), false);
```

# Context & Application

Safe integers matter when dealing with large IDs (e.g., database IDs, Twitter/X post IDs), financial calculations, or cryptographic values. For values beyond 53 bits, use bigints.

# Examples

From the source text:

```js
> 2**53      // can be represented but same as next number
9007199254740992
> 2**53 + 1  // wrong!
9007199254740992

assert.equal(Number.MAX_SAFE_INTEGER, (2 ** 53) - 1);
assert.equal(Number.MIN_SAFE_INTEGER, -Number.MAX_SAFE_INTEGER);
assert.equal(Number.isSafeInteger(5), true);
assert.equal(Number.isSafeInteger('5'), false);
assert.equal(Number.isSafeInteger(Number.MAX_SAFE_INTEGER), true);
assert.equal(Number.isSafeInteger(Number.MAX_SAFE_INTEGER+1), false);
```

Safe computation rule:
```js
// Result is correct only if:
isSafeInteger(a) && isSafeInteger(b) && isSafeInteger(a op b)
```

# Relationships

## Builds Upon
- **ieee-754-floating-point** — the 52-bit fraction limits integer precision

## Enables
- Knowing when to switch to bigints

## Related
- **bigint-type** — use for integers beyond safe range
- **integer-ranges** — safe integers are one of several integer ranges

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all integers up to 2^64 are precise
  **Correction**: Only integers in the range [-(2^53)+1, 2^53-1] are safe. Beyond that, gaps exist.

# Common Confusions

- **Confusion**: Thinking `Number.isSafeInteger()` just checks if a value is an integer
  **Clarification**: It also checks that the integer is within the safe range. `Number.isInteger()` only checks for integer-ness.

# Source Reference

Chapter 18: Numbers, Section 18.9.4, lines 1542-1640.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with range and checking functions
- Cross-reference status: verified against Ch. 20 (bigints motivation)
