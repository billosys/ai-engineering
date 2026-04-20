---
# === CORE IDENTIFICATION ===
concept: Abstract Equality Comparison
slug: abstract-equality-comparison

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
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "loose equality"
  - "== operator"
  - double equals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - to-primitive
  - to-number
contrasts_with:
  - strict-equality-comparison
related:
  - to-primitive
  - to-number
extends: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Abstract Equality Comparison (`==`) is JavaScript's loose equality operator that performs type coercion before comparing, converting operands to common types through a complex set of rules.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.5.2): The `==` operator follows a multi-step algorithm. If operands have the same type, it delegates to strict equality (`===`). Otherwise, it applies a series of coercion rules: `null == undefined` is `true`; numbers vs. strings converts the string to a number; booleans are converted to numbers before comparison; objects vs. primitives converts the object via `ToPrimitive()` with default hint; bigints vs. strings/numbers have special handling.

# Prerequisites

- **Type coercion** — `==` is the primary example of coercion-heavy operations.
- **ToPrimitive** — Used when comparing objects with primitives.
- **ToNumber** — Used for string-to-number and boolean-to-number conversions.

# Key Properties

1. Same types: delegates to strict equality (`===`).
2. `null == undefined` is `true` (and vice versa).
3. Number vs. string: string is converted via `Number()`.
4. Booleans are converted to numbers first (`true` becomes `1`, `false` becomes `0`).
5. Objects vs. primitives: object is converted via `ToPrimitive()` with `'default'` hint.
6. Bigints have special comparison rules with strings and numbers.

# Construction / Recognition

## To Construct/Create:
1. Use the `==` operator between two values.

## To Identify/Recognize:
1. The `==` operator (double equals) always triggers abstract equality comparison.
2. If operands are of different types, coercion occurs.

# Context & Application

The `==` operator is generally discouraged in modern JavaScript due to its surprising coercion behavior. The `===` operator is preferred because it does not perform type coercion. However, `== null` is a common idiomatic pattern to check for both `null` and `undefined`.

# Examples

**Example 1** (Ch 2): The algorithm (abbreviated) in JavaScript form:
```js
function abstractEqualityComparison(x, y) {
  if (TypeOf(x) === TypeOf(y)) {
    return strictEqualityComparison(x, y);
  }

  // null and undefined are equal to each other
  if (x === null && y === undefined) return true;
  if (x === undefined && y === null) return true;

  // Comparing a number and a string
  if (TypeOf(x) === 'number' && TypeOf(y) === 'string') {
    return abstractEqualityComparison(x, Number(y));
  }
  if (TypeOf(x) === 'string' && TypeOf(y) === 'number') {
    return abstractEqualityComparison(Number(x), y);
  }

  // Comparing a boolean with a non-boolean
  if (TypeOf(x) === 'boolean') {
    return abstractEqualityComparison(Number(x), y);
  }
  if (TypeOf(y) === 'boolean') {
    return abstractEqualityComparison(x, Number(y));
  }

  // Comparing an object with a primitive
  if (['string', 'number', 'bigint', 'symbol'].includes(TypeOf(x))
    && TypeOf(y) === 'object') {
      return abstractEqualityComparison(x, ToPrimitive(y));
    }
  // ...
  return false;
}
```

**Example 2** (Ch 2): Date coercion with `==`:
```js
const d = new Date('2222-03-27');
assert.equal(
  d == 'Wed Mar 27 2222 01:00:00 GMT+0100'
       + ' (Central European Standard Time)',
  true);
```

# Relationships

## Builds Upon
- **ToPrimitive** — Used to convert objects when compared against primitives.
- **ToNumber** — Strings and booleans are converted to numbers during comparison.

## Enables
- **Null/undefined checking** — `x == null` is an idiomatic way to check for both null and undefined.

## Related
- **Addition operator coercion** — Also uses ToPrimitive with default hint.

## Contrasts With
- **Strict equality comparison** — `===` does not perform type coercion.

# Common Errors

- **Error**: Expecting `[] == false` to be `false` (since arrays are truthy).
  **Correction**: `[] == false` is `true` because: `false` becomes `0`, `[]` becomes `''` via ToPrimitive, `''` becomes `0`, and `0 == 0` is `true`.

- **Error**: Expecting `== null` to match falsy values like `0` or `''`.
  **Correction**: `== null` only matches `null` and `undefined`, not other falsy values.

# Common Confusions

- **Confusion**: `==` checks if values are "similar" or "equivalent."
  **Clarification**: `==` follows a precise algorithm with specific coercion steps. The results can be counterintuitive because of the order and type of conversions applied.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.5.2, lines 951-1032.

# Verification Notes

- Definition source: direct (full algorithm quoted from source)
- Confidence rationale: Complete algorithm provided
- Cross-reference status: verified against ECMAScript spec reference in source
