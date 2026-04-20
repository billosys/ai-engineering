---
# === CORE IDENTIFICATION ===
concept: ToNumeric
slug: to-numeric

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
  - "ToNumeric()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - to-primitive
  - to-number
extends: []
related:
  - to-number
  - to-primitive
contrasts_with:
  - to-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ToPrimitive relate to ToString and ToNumber?"
---

# Quick Definition

`ToNumeric()` is the ECMAScript specification operation that converts a value to either a number or a bigint, using `ToPrimitive()` as an intermediate step and then delegating to `ToNumber()` for non-bigint values.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.4): `ToNumeric()` was introduced after bigints were added to JavaScript, replacing many uses of `ToNumber()` in the specification. It first calls `ToPrimitive(value, 'number')` to get a primitive, then returns the value directly if it is a bigint, or delegates to `ToNumber()` otherwise. It is used by the `*` operator, `++`/`--` operators, and other numeric operations.

# Prerequisites

- **ToPrimitive** — ToNumeric uses ToPrimitive as a first step.
- **ToNumber** — ToNumeric delegates to ToNumber for non-bigint primitives.
- **Type coercion** — ToNumeric is part of the coercion system.

# Key Properties

1. First calls `ToPrimitive(value, 'number')`.
2. If the result is a bigint, returns it directly.
3. Otherwise, delegates to `ToNumber()`.
4. Used by `*`, `++`, `--`, and other numeric operators.
5. Introduced to handle the bigint/number distinction.

# Construction / Recognition

## To Construct/Create:
1. Triggered internally by numeric operators.

## To Identify/Recognize:
1. Any numeric operator that works with both numbers and bigints uses `ToNumeric()`.

# Context & Application

`ToNumeric()` replaced `ToNumber()` in many specification algorithms when bigints were introduced. The distinction matters because bigints and numbers cannot be mixed in arithmetic operations — if the types differ after conversion, a `TypeError` is thrown.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function ToNumeric(value) {
  let primValue = ToPrimitive(value, 'number');
  if (TypeOf(primValue) === 'bigint') {
    return primValue;
  }
  return ToNumber(primValue);
}
```

# Relationships

## Builds Upon
- **ToPrimitive** — Uses ToPrimitive with hint `'number'`.
- **ToNumber** — Delegates to ToNumber for non-bigint values.

## Enables
- **Arithmetic operators** — `*`, `/`, `-`, `++`, `--` use ToNumeric.

## Related
- **ToNumber** — The pre-bigint version; still used as a sub-step.

## Contrasts With
- **ToNumber** — ToNumber only produces numbers; ToNumeric can also produce bigints.

# Common Errors

- **Error**: Assuming numeric operators always produce numbers.
  **Correction**: With bigint operands, numeric operators produce bigints. Mixing types throws `TypeError`.

# Common Confusions

- **Confusion**: `ToNumeric` and `ToNumber` are interchangeable.
  **Clarification**: `ToNumeric` is the bigint-aware successor. It delegates to `ToNumber` only for non-bigint primitives.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.4, lines 862-876.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm and context provided
- Cross-reference status: verified
