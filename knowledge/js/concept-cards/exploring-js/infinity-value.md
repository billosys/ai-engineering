---
# === CORE IDENTIFICATION ===
concept: Infinity Value
slug: infinity-value

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
section: "Error value: Infinity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Infinity"
  - "-Infinity"
  - "positive infinity"
  - "negative infinity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related:
  - nan-value
  - number-isfinite
contrasts_with:
  - nan-value

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Infinity` is a numeric error value returned when a number is too large to represent or when dividing by zero. It comes in positive (`Infinity`) and negative (`-Infinity`) variants.

# Core Definition

`Infinity` is returned when a number is too large (`Math.pow(2, 1024)`) or when dividing by zero (`5 / 0`). It is larger than all other numbers (except `NaN`), making it a useful default for minimum-finding algorithms. Check with `x === Infinity` or `Number.isFinite(x)` (Ch. 18, Section 18.5.2).

# Prerequisites

- **number-type** -- Infinity is a value of the number type

# Key Properties

1. Returned for overflow: `Math.pow(2, 1024)` -> `Infinity`
2. Returned for division by zero: `5 / 0` -> `Infinity`, `-5 / 0` -> `-Infinity`
3. Larger than all other numbers (except NaN)
4. Useful as initial value in min-finding algorithms
5. Check: `x === Infinity` or `Number.isFinite(x)`
6. `Math.min()` with no arguments returns `Infinity`

# Construction / Recognition

```js
Math.pow(2, 1024) // Infinity
5 / 0             // Infinity
-5 / 0            // -Infinity
```

# Context & Application

`Infinity` serves as a useful sentinel value for algorithms that search for minimums. `Number.isFinite()` checks that a value is a finite number.

# Examples

From the source text:

```js
> Math.pow(2, 1023)
8.98846567431158e+307
> Math.pow(2, 1024)
Infinity
> -Math.pow(2, 1024)
-Infinity

> 5 / 0
Infinity
> -5 / 0
-Infinity

// As a default value
function findMinimum(numbers) {
  let min = Infinity;
  for (const n of numbers) {
    if (n < min) min = n;
  }
  return min;
}
assert.equal(findMinimum([5, -1, 2]), -1);
assert.equal(findMinimum([]), Infinity);

> Math.min()
Infinity
```

# Relationships

## Builds Upon
- **number-type** — Infinity is a number value

## Enables
- Sentinel values in min/max algorithms

## Related
- **nan-value** — the other numeric error value
- **number-isfinite** — check for finite numbers

## Contrasts With
- **nan-value** — NaN represents unparsable/impossible operations; Infinity represents overflow

# Common Errors

- **Error**: Not checking for Infinity before using a division result
  **Correction**: Division by zero silently returns `Infinity` in JavaScript. Check with `Number.isFinite()`.

# Common Confusions

- **Confusion**: Expecting division by zero to throw an error
  **Clarification**: JavaScript returns `Infinity` (or `-Infinity`) instead of throwing.

# Source Reference

Chapter 18: Numbers, Section 18.5.2, lines 1074-1139.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with checking methods
- Cross-reference status: verified
