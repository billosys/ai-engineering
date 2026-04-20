---
# === CORE IDENTIFICATION ===
concept: OrdinaryToPrimitive
slug: ordinary-to-primitive

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
  - "OrdinaryToPrimitive()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - to-primitive
extends:
  - to-primitive
related:
  - symbol-to-primitive
  - to-string
  - to-number
contrasts_with:
  - symbol-to-primitive

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform type coercion using ToPrimitive?"
---

# Quick Definition

`OrdinaryToPrimitive()` is the default algorithm for converting objects to primitives, calling `toString()` and `valueOf()` in an order determined by the hint.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.1): When `ToPrimitive()` processes an object that does not define `Symbol.toPrimitive`, it delegates to `OrdinaryToPrimitive()`. This function tries two methods on the object — `toString` and `valueOf` — in an order determined by the hint. With `hint === 'string'`, it tries `toString` first; with `hint === 'number'`, it tries `valueOf` first. It returns the first result that is a primitive, or throws a `TypeError` if neither method produces a primitive.

# Prerequisites

- **ToPrimitive** — OrdinaryToPrimitive is the fallback within ToPrimitive.
- **valueOf and toString methods** — These are the object methods that OrdinaryToPrimitive calls.

# Key Properties

1. Called only when `Symbol.toPrimitive` is not defined on the object.
2. With `hint === 'string'`: tries `toString` first, then `valueOf`.
3. With `hint === 'number'`: tries `valueOf` first, then `toString`.
4. Returns the first result that is a primitive value.
5. Throws `TypeError` if neither method returns a primitive.

# Construction / Recognition

## To Construct/Create:
1. Define `toString()` and/or `valueOf()` methods on an object.
2. These are called by the coercion system when the object needs to become a primitive.

## To Identify/Recognize:
1. When an object without `Symbol.toPrimitive` is coerced, `OrdinaryToPrimitive` is the mechanism at work.

# Context & Application

Most JavaScript objects use `OrdinaryToPrimitive` for their primitive conversion, since only `Date` and `Symbol` instances override via `Symbol.toPrimitive` in the standard library. Custom objects can define `toString()` and `valueOf()` to control how they convert.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function OrdinaryToPrimitive(O, hint) {
  let methodNames;
  if (hint === 'string') {
    methodNames = ['toString', 'valueOf'];
  } else {
    methodNames = ['valueOf', 'toString'];
  }
  for (let name of methodNames) {
    let method = O[name];
    if (IsCallable(method)) {
      let result = method.call(O);
      if (TypeOf(result) !== 'object') {
        return result;
      }
    }
  }
  throw new TypeError();
}
```

**Example 2** (Ch 2): Observing method call order:
```js
const obj = {
  toString() { return 'a' },
  valueOf() { return 1 },
};

// String() prefers strings -> toString called first
assert.equal(String(obj), 'a');

// Number() prefers numbers -> valueOf called first
assert.equal(Number(obj), 1);
```

# Relationships

## Builds Upon
- **ToPrimitive** — OrdinaryToPrimitive is the default path within ToPrimitive.

## Enables
- **ToString** — For objects, ToString calls ToPrimitive which typically calls OrdinaryToPrimitive.
- **ToNumber** — For objects, ToNumber calls ToPrimitive which typically calls OrdinaryToPrimitive.

## Related
- **Symbol.toPrimitive** — The override mechanism that bypasses OrdinaryToPrimitive.

## Contrasts With
- **Symbol.toPrimitive** — Objects with `Symbol.toPrimitive` skip OrdinaryToPrimitive entirely.

# Common Errors

- **Error**: Assuming `valueOf()` is always called first.
  **Correction**: The order depends on the hint. With `'string'` hint, `toString()` is tried first.

# Common Confusions

- **Confusion**: Overriding `toString()` is sufficient for all coercion scenarios.
  **Clarification**: Numeric coercion calls `valueOf()` first. Both methods may need to be defined for consistent behavior across different coercion contexts.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.1, lines 461-480.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with explanation
- Cross-reference status: verified
