---
# === CORE IDENTIFICATION ===
concept: Truthiness-Based Existence Checks
slug: truthiness-based-existence-checks

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Truthiness-based existence checks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - undefined-value
  - nullish-coalescing-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
---

# Quick Definition

Truthiness-based existence checks use boolean coercion to detect whether a value exists (is not `undefined`), but they are imprecise because they also reject other falsy values like `0`, `''`, and `false`.

# Core Definition

Since reading a missing parameter or property returns `undefined` (which is falsy), a truthiness check can serve as an existence check: `if (obj.prop) { ... }`. However, this is imprecise -- the body is skipped not only when `obj.prop` is missing but also when it is any falsy value such as `0`, `''`, or `null` (Ch. 17, Section 17.3).

# Prerequisites

- **falsy-and-truthy-values** -- understanding which values are falsy

# Key Properties

1. `if (x)` checks for truthiness, which includes existence but also other conditions
2. Pitfall: skips the body for `0`, `''`, `null`, `false`, `NaN`, `0n` -- not just missing values
3. Established pattern but imprecise
4. Alternatives: `x === undefined`, `'prop' in obj`, `??`

# Construction / Recognition

```js
// Parameter existence check (imprecise)
function func(x) {
  if (!x) {
    throw new Error('Missing parameter x');
  }
}

// Property existence check (imprecise)
if (obj.prop) {
  // obj has property .prop -- but also skips if .prop is 0, '', etc.
}
```

# Context & Application

This is a common JavaScript pattern. Be aware of its limitations when values like `0` or empty strings are valid inputs.

# Examples

From the source text:

```js
// Imprecise parameter check
function func(x) {
  if (!x) {
    throw new Error('Missing parameter x');
  }
}

// More precise check
if (x === undefined) {
  throw new Error('Missing parameter x');
}

// For properties, use the in operator for precision
if (! ('path' in fileDesc)) {
  throw new Error('Missing property: .path');
}
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — truthiness checks rely on boolean coercion

## Enables
- Quick parameter and property validation patterns

## Related
- **undefined-value** — the value returned for missing properties/parameters
- **nullish-coalescing-operator** — a more precise way to handle missing values

## Contrasts With
- None

# Common Errors

- **Error**: Using `if (count)` when `count` can legitimately be `0`
  **Correction**: `0` is falsy. Use `if (count !== undefined)` or `if (count != null)`.

# Common Confusions

- **Confusion**: Thinking truthiness checks only fail for `undefined`
  **Clarification**: They fail for all seven falsy values: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, `''`.

# Source Reference

Chapter 17: Booleans, Section 17.3, lines 335-440.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit discussion of pitfalls with alternatives
- Cross-reference status: verified
