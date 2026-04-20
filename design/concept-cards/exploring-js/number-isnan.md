---
# === CORE IDENTIFICATION ===
concept: Number.isNaN()
slug: number-isnan

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
section: "Checking for NaN"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "isNaN()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nan-value
extends: []
related:
  - object-is
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`Number.isNaN(x)` returns `true` only if `x` is exactly `NaN`. Unlike the global `isNaN()`, it does not coerce its argument to number first.

# Core Definition

`Number.isNaN(x)` is the preferred way to check for `NaN`. It returns `true` only if `x` is the value `NaN`. Unlike the legacy global `isNaN()` function, `Number.isNaN()` does not coerce its argument, so `Number.isNaN('abc')` returns `false` while `isNaN('abc')` returns `true` (Ch. 18, Section 18.5.1.1).

# Prerequisites

- **nan-value** -- the value being checked for

# Key Properties

1. `Number.isNaN(NaN)` returns `true`
2. `Number.isNaN(123)` returns `false`
3. `Number.isNaN('abc')` returns `false` (no coercion)
4. Global `isNaN('abc')` returns `true` (coerces to `Number('abc')` which is `NaN`)
5. Preferred over `isNaN()` for accuracy

# Construction / Recognition

```js
const x = NaN;
assert.equal(Number.isNaN(x), true);  // preferred
assert.equal(Object.is(x, NaN), true); // alternative
assert.equal(x !== x, true);           // quirky alternative
```

# Context & Application

Always use `Number.isNaN()` instead of the global `isNaN()` to avoid false positives from coercion.

# Examples

From the source text:

```js
const x = NaN;
assert.equal(Number.isNaN(x), true); // preferred
assert.equal(Object.is(x, NaN), true);
assert.equal(x !== x, true);
```

# Relationships

## Builds Upon
- **nan-value** — checks for this specific value

## Enables
- Accurate NaN detection

## Related
- **object-is** — `Object.is(x, NaN)` is an alternative

## Contrasts With
- None

# Common Errors

- **Error**: Using global `isNaN()` which coerces its argument
  **Correction**: Use `Number.isNaN()` which only returns `true` for actual `NaN` values.

# Common Confusions

- **Confusion**: Thinking `isNaN('hello')` means the string is NaN
  **Clarification**: Global `isNaN()` coerces to number first: `Number('hello')` is `NaN`, so `isNaN('hello')` is `true`. Use `Number.isNaN()` for precise checking.

# Source Reference

Chapter 18: Numbers, Section 18.5.1.1, lines 1026-1047.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit comparison between Number.isNaN and global isNaN
- Cross-reference status: verified
