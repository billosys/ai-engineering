---
# === CORE IDENTIFICATION ===
concept: ToPropertyKey
slug: to-property-key

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
section: "2.4.3 ToPropertyKey()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ToPropertyKey()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - to-primitive
  - to-string
extends: []
related:
  - to-primitive
  - to-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ToPrimitive relate to ToString and ToNumber?"
---

# Quick Definition

`ToPropertyKey()` is the ECMAScript specification operation that converts a value to a valid property key (string or symbol) by first calling `ToPrimitive()` with hint `'string'`, then returning the result if it is a symbol or converting it to a string via `ToString()`.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.3): `ToPropertyKey()` converts its argument to a string or symbol suitable for use as a property key. It is used by the bracket operator `[]`, computed property keys in object literals, the `in` operator, and various `Object` and `Reflect` methods.

# Prerequisites

- **ToPrimitive** — First step converts the argument to a primitive with hint `'string'`.
- **ToString** — Non-symbol primitives are converted to strings.

# Key Properties

1. Returns either a string or a symbol.
2. First calls `ToPrimitive(argument, 'string')`.
3. If the result is a symbol, returns it directly.
4. Otherwise, converts to string via `ToString()`.
5. Used by: bracket operator `[]`, computed property keys, `in` operator, `Object.defineProperty()`, etc.

# Construction / Recognition

## To Construct/Create:
1. Triggered internally when accessing properties with `[]` or using computed property keys.

## To Identify/Recognize:
1. Any dynamic property access or computed key invokes `ToPropertyKey()`.

# Context & Application

`ToPropertyKey()` explains why objects can use non-string, non-symbol values as property keys in bracket notation — they are automatically converted. For example, `obj[1]` converts `1` to the string `'1'`.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function ToPropertyKey(argument) {
  let key = ToPrimitive(argument, 'string');
  if (TypeOf(key) === 'symbol') {
    return key;
  }
  return ToString(key);
}
```

# Relationships

## Builds Upon
- **ToPrimitive** — Uses ToPrimitive with hint `'string'` as first step.
- **ToString** — Converts non-symbol primitives to strings.

## Enables
- **Dynamic property access** — Powers the `[]` operator and computed property keys.

## Related
- **ToPrimitive** — Key intermediate step.
- **ToString** — Final conversion for non-symbol results.

## Contrasts With
- None in immediate taxonomy.

# Common Errors

- **Error**: Assuming numeric array indices are stored as numbers.
  **Correction**: Array indices are property keys, which are strings. `arr[0]` accesses property `'0'`.

# Common Confusions

- **Confusion**: Only strings can be property keys.
  **Clarification**: Both strings and symbols can be property keys. `ToPropertyKey()` preserves symbols and converts everything else to strings.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.3, lines 842-860.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided
- Cross-reference status: verified
