---
# === CORE IDENTIFICATION ===
concept: ToString
slug: to-string

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
section: "2.4.2 ToString() and related operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ToString()"
  - string conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - to-primitive
extends: []
related:
  - to-number
  - to-boolean
  - to-primitive
  - string-function
contrasts_with:
  - to-number
  - string-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "How does ToPrimitive relate to ToString and ToNumber?"
---

# Quick Definition

`ToString()` is the ECMAScript specification operation that converts any value to a string, using `ToPrimitive()` with hint `'string'` as an intermediate step for objects.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.2): `ToString()` converts each type according to specific rules: `undefined` becomes `'undefined'`, `null` becomes `'null'`, booleans become `'true'`/`'false'`, numbers use `Number.toString()`, strings pass through, symbols throw `TypeError`, bigints use `BigInt.toString()`, and objects are first converted via `ToPrimitive(argument, 'string')` before recursively applying `ToString()`. Notably, `ToString()` throws on symbols, while `String()` does not.

# Prerequisites

- **Type coercion** — ToString is a core conversion algorithm.
- **ToPrimitive** — Objects are first converted to primitives with hint `'string'`.

# Key Properties

1. `undefined` returns `'undefined'`, `null` returns `'null'`.
2. Booleans return `'true'` or `'false'`.
3. Symbols throw `TypeError` (unlike `String()` which handles them).
4. Objects: calls `ToPrimitive(argument, 'string')` first, then `ToString()` on the result.
5. The structure is parallel to `ToNumber()`.

# Construction / Recognition

## To Construct/Create:
1. Template literals trigger `ToString()` on embedded expressions.
2. The `+` operator triggers `ToString()` when one operand is a string.

## To Identify/Recognize:
1. String concatenation and template literals use `ToString()` internally.

# Context & Application

`ToString()` is used whenever the spec needs a string representation. It is a building block for `String()`, template literals, and string concatenation via `+`. The distinction between `ToString()` (throws on symbols) and `String()` (handles symbols) is important when working with symbols.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function ToString(argument) {
  if (argument === undefined) {
    return 'undefined';
  } else if (argument === null) {
    return 'null';
  } else if (argument === true) {
    return 'true';
  } else if (argument === false) {
    return 'false';
  } else if (TypeOf(argument) === 'number') {
    return Number.toString(argument);
  } else if (TypeOf(argument) === 'string') {
    return argument;
  } else if (TypeOf(argument) === 'symbol') {
    throw new TypeError();
  } else if (TypeOf(argument) === 'bigint') {
    return BigInt.toString(argument);
  } else {
    // argument is an object
    let primValue = ToPrimitive(argument, 'string');
    return ToString(primValue);
  }
}
```

**Example 2** (Ch 2): Symbol behavior difference:
```js
const sym = Symbol('sym');

// ToString() throws (used by template literals):
> `${sym}`
TypeError: Cannot convert a Symbol value to a string

// String() handles symbols:
> String(sym)
'Symbol(sym)'
```

# Relationships

## Builds Upon
- **ToPrimitive** — Uses ToPrimitive with hint `'string'` for objects.
- **Type coercion** — ToString is a core coercion mechanism.

## Enables
- **String() function** — String() builds on ToString() with special symbol handling.
- **Template literal coercion** — Template literals use ToString() internally.
- **Addition operator** — When `+` concatenates strings, it uses ToString().

## Related
- **ToNumber** — Parallel conversion algorithm for numbers, with similar structure.
- **Object.prototype.toString** — The default `.toString()` method used during OrdinaryToPrimitive.

## Contrasts With
- **String() function** — String() handles symbols (returns `'Symbol(...)'`); ToString() throws TypeError on symbols.
- **ToNumber** — Similar structure but produces numbers; uses hint `'number'` with ToPrimitive.

# Common Errors

- **Error**: Using template literals with symbols expecting them to convert.
  **Correction**: Template literals use `ToString()` which throws on symbols. Use `String(sym)` instead.

# Common Confusions

- **Confusion**: `ToString()` and `String()` are identical.
  **Clarification**: `String()` has special handling for symbols (returns descriptive string) and for `undefined` when called as constructor. `ToString()` throws a `TypeError` for symbols.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.2, lines 617-839.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with detailed explanation
- Cross-reference status: verified
