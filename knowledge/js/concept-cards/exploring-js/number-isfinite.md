---
# === CORE IDENTIFICATION ===
concept: Number.isFinite()
slug: number-isfinite

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
section: "Checking for Infinity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isFinite()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - infinity-value
  - nan-value
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Number.isFinite(x)` returns `true` if `x` is a number that is neither `Infinity`, `-Infinity`, nor `NaN`.

# Core Definition

`Number.isFinite(x)` checks that a value is a finite number. It returns `false` for `Infinity`, `-Infinity`, `NaN`, and non-number values. Unlike checking `x === Infinity`, it also handles `-Infinity` and `NaN` in one call (Ch. 18, Section 18.5.2.2).

# Prerequisites

- **infinity-value** -- one of the values detected
- **nan-value** -- also detected as non-finite

# Key Properties

1. Returns `true` for finite numbers
2. Returns `false` for `Infinity`, `-Infinity`, `NaN`
3. Returns `false` for non-number values (unlike global `isFinite()` which coerces)

# Construction / Recognition

```js
const x = Infinity;
assert.equal(x === Infinity, true);
assert.equal(Number.isFinite(x), false);
assert.equal(Number.isFinite(42), true);
assert.equal(Number.isFinite(NaN), false);
```

# Context & Application

Use `Number.isFinite()` to validate computation results before using them, especially after division or exponentiation.

# Examples

From the source text:

```js
const x = Infinity;
assert.equal(x === Infinity, true);
assert.equal(Number.isFinite(x), false);
```

# Relationships

## Builds Upon
- **infinity-value** — detects infinite values
- **nan-value** — also detected as non-finite

## Enables
- Computation result validation

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using global `isFinite()` which coerces: `isFinite('42')` is `true`
  **Correction**: Use `Number.isFinite()` which returns `false` for non-numbers.

# Common Confusions

- **Confusion**: Thinking `Number.isFinite(NaN)` returns `true`
  **Clarification**: NaN is not considered finite. `Number.isFinite(NaN)` returns `false`.

# Source Reference

Chapter 18: Numbers, Section 18.5.2.2, lines 1129-1139.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
