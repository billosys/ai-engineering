---
# === CORE IDENTIFICATION ===
concept: Date Primitive Conversion
slug: date-to-primitive

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
section: "2.4.1.3 Date.prototype[Symbol.toPrimitive]()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Date.prototype[Symbol.toPrimitive]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-to-primitive
  - to-primitive
  - ordinary-to-primitive
extends:
  - symbol-to-primitive
related:
  - addition-operator-coercion
  - abstract-equality-comparison
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform type coercion using ToPrimitive?"
---

# Quick Definition

`Date.prototype[Symbol.toPrimitive]` overrides the default primitive conversion so that the `'default'` hint is treated as `'string'` (instead of `'number'`), making Dates prefer string representation in contexts like `+` and `==`.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.1.3): "The only difference with the default algorithm is that `'default'` becomes `'string'` (and not `'number'`)." Date is one of only two standard library types (along with Symbol) that override `Symbol.toPrimitive`. This means operations that use a `'default'` hint (like `==` and `+`) will get a string representation of the Date rather than a numeric timestamp.

# Prerequisites

- **Symbol.toPrimitive** — Date uses this mechanism to override default conversion.
- **ToPrimitive** — Date's override is checked first within ToPrimitive.
- **OrdinaryToPrimitive** — Date's override delegates to OrdinaryToPrimitive with adjusted hint.

# Key Properties

1. Overrides the `'default'` hint to behave as `'string'`.
2. `'number'` hint still produces numeric (timestamp) values.
3. `'string'` hint produces string date representation (unchanged).
4. Affects `==` and `+` operators (which use default hint).
5. Only Date and Symbol override `Symbol.toPrimitive` in the standard library.

# Construction / Recognition

## To Construct/Create:
1. Any Date object automatically has this behavior.

## To Identify/Recognize:
1. When a Date is used with `+` or `==` and produces a string instead of a number.

# Context & Application

Date's override explains why `someDate + ""` produces a date string, and why `someDate == dateString` compares the string representation. Without this override, the default hint would resolve to `'number'`, and dates would produce timestamps in these contexts.

# Examples

**Example 1** (Ch 2): Date with `==` (default hint → string):
```js
const d = new Date('2222-03-27');
assert.equal(
  d == 'Wed Mar 27 2222 01:00:00 GMT+0100'
       + ' (Central European Standard Time)',
  true);
```

**Example 2** (Ch 2): Date with `+` (default hint → string):
```js
const d = new Date('2222-03-27');
assert.equal(
  123 + d,
  '123Wed Mar 27 2222 01:00:00 GMT+0100'
    + ' (Central European Standard Time)');
```

# Relationships

## Builds Upon
- **Symbol.toPrimitive** — Date uses this override mechanism.
- **OrdinaryToPrimitive** — Date's implementation delegates to it with adjusted hint.

## Enables
- **String-first Date coercion** — Dates produce strings in default-hint contexts.

## Related
- **Addition operator coercion** — Uses default hint, affected by Date's override.
- **Abstract equality comparison** — Uses default hint, affected by Date's override.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting `date + 0` to produce a timestamp number.
  **Correction**: `+` uses default hint, which Date converts to `'string'`. The result is string concatenation. Use `date.getTime()` or `Number(date)` for the timestamp.

# Common Confusions

- **Confusion**: Dates always convert to numbers.
  **Clarification**: With `'number'` hint (e.g., `Number(date)`, unary `+date`), yes. But with `'default'` hint (e.g., `date + x`, `date == x`), Date overrides to prefer strings.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.1.3, lines 558-614.

# Verification Notes

- Definition source: direct (algorithm and examples from source)
- Confidence rationale: Full algorithm provided with behavioral examples
- Cross-reference status: verified
