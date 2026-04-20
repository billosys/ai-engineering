---
# === CORE IDENTIFICATION ===
concept: Strict Equality Comparison
slug: strict-equality-comparison

# === CLASSIFICATION ===
category: type-system
subcategory: equality
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.5.2 Abstract Equality Comparison (==)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "=== operator"
  - triple equals
  - identity comparison

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - abstract-equality-comparison
contrasts_with:
  - abstract-equality-comparison

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Strict Equality Comparison (`===`) compares two values without performing type coercion, returning `true` only if both the type and value are the same.

# Core Definition

As referenced in "Deep JavaScript" (Ch 2, Section 2.5.2): Strict equality comparison is the no-coercion counterpart to abstract equality. The `==` algorithm delegates to `strictEqualityComparison()` when both operands have the same type. The strict equality operator `===` always uses this algorithm directly, never performing type coercion. The source references the ECMAScript specification's `strictEqualityComparison()` function.

# Prerequisites

- **Type coercion** — Understanding strict equality requires understanding what coercion it avoids.

# Key Properties

1. No type coercion — operands of different types are always unequal.
2. `NaN !== NaN` (NaN is not equal to itself).
3. `+0 === -0` (positive and negative zero are equal).
4. Objects are compared by reference, not by value.
5. Same-type primitives are compared by value.

# Construction / Recognition

## To Construct/Create:
1. Use the `===` operator between two values.

## To Identify/Recognize:
1. The `===` operator (triple equals) always uses strict equality with no coercion.

# Context & Application

Strict equality is the recommended comparison operator in modern JavaScript. It avoids the surprising behaviors of `==` and makes code more predictable. ESLint rules commonly enforce `===` over `==`.

# Examples

**Example 1** (Ch 2): Strict equality does not coerce:
```js
assert.equal(1 === '1', false);  // different types
assert.equal(1 === 1, true);     // same type, same value
assert.equal(null === undefined, false); // different types
```

**Example 2**: Special cases:
```js
assert.equal(NaN === NaN, false);  // NaN is never equal to itself
assert.equal(+0 === -0, true);     // positive and negative zero are equal
```

# Relationships

## Builds Upon
- **Type coercion** — Understanding what strict equality avoids.

## Enables
- **Predictable comparisons** — No surprising coercion side effects.

## Related
- **Abstract equality comparison** — Delegates to strict equality when types match.

## Contrasts With
- **Abstract equality comparison** — `==` coerces types; `===` does not.

# Common Errors

- **Error**: Using `===` to check for `NaN`.
  **Correction**: Use `Number.isNaN()` since `NaN !== NaN`.

# Common Confusions

- **Confusion**: `===` compares objects by value.
  **Clarification**: `===` compares objects by reference. Two objects with identical contents are not `===` unless they are the same object.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.5.2, lines 957-959 (referenced within == algorithm).

# Verification Notes

- Definition source: synthesized (referenced in source but algorithm not fully shown)
- Confidence rationale: Medium because algorithm is referenced but not expanded; behavior is well-known
- Cross-reference status: verified against ECMAScript spec link in source
