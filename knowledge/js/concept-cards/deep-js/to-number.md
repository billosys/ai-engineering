---
# === CORE IDENTIFICATION ===
concept: ToNumber
slug: to-number

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
section: "2.4.4 ToNumeric() and related operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ToNumber()"
  - "Number()"
  - number conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - to-primitive
extends: []
related:
  - to-numeric
  - to-string
  - to-boolean
  - to-primitive
contrasts_with:
  - to-string
  - to-boolean

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "How does ToPrimitive relate to ToString and ToNumber?"
---

# Quick Definition

`ToNumber()` is the ECMAScript specification operation that converts any value to a number, using `ToPrimitive()` as an intermediate step for objects.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.4.1): `ToNumber()` converts values to numbers following specific rules for each type. For `undefined` it returns `NaN`, for `null` it returns `+0`, `true` becomes `1`, `false` becomes `+0`, strings are parsed, and symbols/bigints throw `TypeError`. For objects, it first calls `ToPrimitive(argument, 'number')` then recursively applies `ToNumber()` to the result. The JavaScript analog is `Number()`.

# Prerequisites

- **Type coercion** — ToNumber is a core conversion algorithm.
- **ToPrimitive** — Objects are first converted to primitives before numeric conversion.

# Key Properties

1. `undefined` returns `NaN`.
2. `null` returns `+0`.
3. `true` returns `1`, `false` returns `+0`.
4. Strings are parsed as numeric literals.
5. Symbols and bigints throw `TypeError`.
6. Objects: calls `ToPrimitive(argument, 'number')` first, then `ToNumber()` on the result.

# Construction / Recognition

## To Construct/Create:
1. Call `Number(value)` for explicit conversion.
2. Use unary `+` operator: `+value`.
3. Use arithmetic operators that trigger `ToNumber`/`ToNumeric` internally.

## To Identify/Recognize:
1. Arithmetic operations (except `+` with strings) trigger ToNumber/ToNumeric.

# Context & Application

`ToNumber()` is used by `ToNumeric()`, which in turn is used by multiplication, subtraction, division, and other numeric operators. It is the fundamental algorithm that determines how non-numeric values become numbers. Understanding its rules explains why `null * 5 === 0` but `undefined * 5` is `NaN`.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function ToNumber(argument) {
  if (argument === undefined) {
    return NaN;
  } else if (argument === null) {
    return +0;
  } else if (argument === true) {
    return 1;
  } else if (argument === false) {
    return +0;
  } else if (TypeOf(argument) === 'number') {
    return argument;
  } else if (TypeOf(argument) === 'string') {
    return parseTheString(argument);
  } else if (TypeOf(argument) === 'symbol') {
    throw new TypeError();
  } else if (TypeOf(argument) === 'bigint') {
    throw new TypeError();
  } else {
    // argument is an object
    let primValue = ToPrimitive(argument, 'number');
    return ToNumber(primValue);
  }
}
```

**Example 2** (Ch 2): JavaScript analog usage:
```js
> Number('123')
123

assert.equal(Number(undefined), NaN);
assert.equal(Number(null), 0);
assert.equal(Number(true), 1);
assert.equal(Number('xyz'), NaN);
```

# Relationships

## Builds Upon
- **ToPrimitive** — Uses ToPrimitive with hint `'number'` for objects.
- **Type coercion** — ToNumber is a core coercion mechanism.

## Enables
- **ToNumeric** — ToNumeric delegates to ToNumber for non-bigint values.
- **Arithmetic operators** — Subtraction, multiplication, division use ToNumeric/ToNumber.

## Related
- **ToString** — Parallel conversion algorithm for strings, with similar structure.
- **ToBoolean** — Another conversion algorithm, but simpler (no ToPrimitive step).

## Contrasts With
- **ToString** — ToString uses hint `'string'` for ToPrimitive; ToNumber uses `'number'`.
- **ToBoolean** — ToBoolean does not use ToPrimitive at all.

# Common Errors

- **Error**: Expecting `Number(null)` to return `NaN`.
  **Correction**: `Number(null)` returns `0`, not `NaN`. Only `undefined` returns `NaN`.

- **Error**: Expecting `Number(symbol)` to return some number.
  **Correction**: Converting a symbol to a number throws a `TypeError`.

# Common Confusions

- **Confusion**: `Number()` and `parseInt()` behave the same way.
  **Clarification**: `Number()` implements the spec's `ToNumber()`, which parses the whole string. `parseInt()` parses from the beginning and stops at the first non-numeric character.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.4.1, lines 878-911.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided
- Cross-reference status: verified
