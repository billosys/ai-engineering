---
# === CORE IDENTIFICATION ===
concept: ToPrimitive
slug: to-primitive

# === CLASSIFICATION ===
category: type-system
subcategory: conversion-algorithms
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.4.1 ToPrimitive()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ToPrimitive()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - ordinary-to-primitive
  - to-string
  - to-number
  - to-numeric
  - symbol-to-primitive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ToPrimitive relate to ToString and ToNumber?"
  - "How do I perform type coercion using ToPrimitive?"
---

# Quick Definition

`ToPrimitive()` is an ECMAScript specification operation that converts an arbitrary value to a primitive value, serving as an intermediate step for many coercion algorithms.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.1): "The operation `ToPrimitive()` is an intermediate step for many coercion algorithms. It converts an arbitrary values to primitive values." It accepts a `hint` parameter (`'string'`, `'number'`, or `'default'`) indicating the preferred result type. If the input is already primitive, it is returned unchanged. For objects, it first checks for a `Symbol.toPrimitive` method; if absent, it delegates to `OrdinaryToPrimitive()`.

# Prerequisites

- **Type coercion** — ToPrimitive is a core mechanism within JavaScript's coercion system.
- **JavaScript primitives** — Understanding what constitutes a primitive value (string, number, boolean, symbol, bigint, null, undefined).

# Key Properties

1. Accepts a `hint` parameter: `'string'`, `'number'`, or `'default'`.
2. If input is already primitive, returns it unchanged.
3. Objects can override conversion via `Symbol.toPrimitive`.
4. If no `Symbol.toPrimitive`, delegates to `OrdinaryToPrimitive()`.
5. Default hint (`'default'`) is treated as `'number'` unless overridden (only `Symbol` and `Date` override this).

# Construction / Recognition

## To Construct/Create:
1. Called internally by spec operations like `ToString()`, `ToNumber()`, `ToNumeric()`, addition operator, and `==`.
2. Not directly callable by user code, but `Symbol.toPrimitive` allows customization.

## To Identify/Recognize:
1. Any operation that needs to convert an object to a primitive uses `ToPrimitive()` as an intermediate step.

# Context & Application

`ToPrimitive()` is used pervasively in the specification. Operations that use `hint === 'number'` include `ToNumeric()`, `ToNumber()`, and relational comparison (`<`). Operations using `hint === 'string'` include `ToString()` and `ToPropertyKey()`. Operations using `hint === 'default'` include `==` and the `+` operator.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function ToPrimitive(input, hint = 'default') {
    if (TypeOf(input) === 'object') {
      let exoticToPrim = input[Symbol.toPrimitive];
      if (exoticToPrim !== undefined) {
        let result = exoticToPrim.call(input, hint);
        if (TypeOf(result) !== 'object') {
          return result;
        }
        throw new TypeError();
      }
      if (hint === 'default') {
        hint = 'number';
      }
      return OrdinaryToPrimitive(input, hint);
    } else {
      // input is already primitive
      return input;
    }
  }
```

**Example 2** (Ch 2): How hint affects method call order:
```js
const obj = {
  toString() { return 'a' },
  valueOf() { return 1 },
};

// String() uses hint 'string' -> calls toString first
assert.equal(String(obj), 'a');

// Number() uses hint 'number' -> calls valueOf first
assert.equal(Number(obj), 1);
```

# Relationships

## Builds Upon
- **Type coercion** — ToPrimitive is the primary mechanism for object-to-primitive coercion.

## Enables
- **ToString** — Uses ToPrimitive with hint `'string'` for objects.
- **ToNumber** — Uses ToPrimitive with hint `'number'` for objects.
- **ToNumeric** — Uses ToPrimitive with hint `'number'` for objects.
- **Addition operator coercion** — Calls ToPrimitive with default hint on both operands.
- **Abstract equality comparison** — Calls ToPrimitive when comparing objects to primitives.

## Related
- **OrdinaryToPrimitive** — Fallback when no `Symbol.toPrimitive` is defined.
- **Symbol.toPrimitive** — Allows objects to customize their ToPrimitive behavior.

## Contrasts With
- None directly; ToPrimitive is a foundational building block.

# Common Errors

- **Error**: Assuming `ToPrimitive` always returns a string or number.
  **Correction**: It returns whatever primitive the object's methods produce; it could be a boolean or other primitive.

- **Error**: Forgetting that the default hint is treated as `'number'`.
  **Correction**: Unless overridden (as `Date` and `Symbol` do), `'default'` resolves to `'number'`, meaning `valueOf()` is tried first.

# Common Confusions

- **Confusion**: `ToPrimitive` and `ToString`/`ToNumber` are the same operation.
  **Clarification**: `ToPrimitive` converts objects to *any* primitive. `ToString` and `ToNumber` use `ToPrimitive` as an intermediate step, then further convert the primitive result to a string or number.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.1, lines 414-615.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with detailed explanation
- Cross-reference status: verified against ECMAScript spec link in source
