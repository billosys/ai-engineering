---
# === CORE IDENTIFICATION ===
concept: ToBoolean
slug: to-boolean

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
section: "2.2.1 Converting to primitive types and objects"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "ToBoolean()"
  - "Boolean()"
  - boolean conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - to-number
  - to-string
  - to-primitive
contrasts_with:
  - to-number
  - to-string

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

`ToBoolean()` is the ECMAScript specification operation that converts any value to a boolean, with `Boolean()` as its JavaScript analog.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.2.1): The specification uses `ToBoolean()` whenever a boolean is expected, and its JavaScript analog is `Boolean()`. Unlike other conversion operations, `ToBoolean()` does not call `ToPrimitive()` and does not involve coercion methods on objects. It is a simple lookup: certain values are falsy (`undefined`, `null`, `false`, `0`, `-0`, `NaN`, `0n`, `''`) and everything else is truthy.

# Prerequisites

- **Type coercion** — ToBoolean is one of the fundamental conversion operations in JavaScript's coercion system.

# Key Properties

1. Does **not** call `ToPrimitive()` — direct value mapping.
2. All objects are truthy, including empty arrays and empty objects.
3. Falsy values: `undefined`, `null`, `false`, `0`, `-0`, `NaN`, `0n`, `''`.
4. Everything else is truthy.
5. `Boolean()` is the JavaScript-accessible analog.

# Construction / Recognition

## To Construct/Create:
1. Call `Boolean(value)` for explicit conversion.
2. Use a value in a boolean context (e.g., `if`, `while`, `&&`, `||`, `!`).

## To Identify/Recognize:
1. Any context that expects a boolean triggers `ToBoolean()` internally.

# Context & Application

`ToBoolean()` is used in conditional statements (`if`, `while`), logical operators (`&&`, `||`, `!`), and the ternary operator. It is one of the simplest conversion operations because it does not depend on `ToPrimitive()`.

# Examples

**Example 1** (Ch 2): Using `Boolean()`:
```js
> Boolean(0)
false
> Boolean(1)
true
```

**Example 2** (Ch 2): Falsy vs. truthy:
```js
Boolean(undefined)  // false
Boolean(null)       // false
Boolean('')         // false
Boolean(0)          // false
Boolean(NaN)        // false
Boolean({})         // true (all objects are truthy)
Boolean([])         // true
```

# Relationships

## Builds Upon
- **Type coercion** — ToBoolean is a fundamental coercion operation.

## Enables
- **Conditional evaluation** — Powers `if`, `while`, `&&`, `||` behavior.

## Related
- **ToNumber** — Another primitive conversion operation, but with different rules.
- **ToString** — Another primitive conversion operation.

## Contrasts With
- **ToNumber** — ToNumber uses `ToPrimitive()` for objects; ToBoolean does not.
- **ToString** — ToString uses `ToPrimitive()` for objects; ToBoolean does not.

# Common Errors

- **Error**: Assuming empty objects `{}` or empty arrays `[]` are falsy.
  **Correction**: All objects are truthy in JavaScript, regardless of their contents.

# Common Confusions

- **Confusion**: `ToBoolean` calls `valueOf()` or `toString()` on objects.
  **Clarification**: Unlike other conversion operations, `ToBoolean` does not invoke any methods. It is a direct lookup: all objects are truthy.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.2.1, lines 217-245.

# Verification Notes

- Definition source: synthesized (mentioned in spec operations list, behavior well-known)
- Confidence rationale: Medium because chapter lists it but does not provide full algorithm; behavior is standard
- Cross-reference status: verified against standard ECMAScript behavior
