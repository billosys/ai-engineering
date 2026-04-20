---
# === CORE IDENTIFICATION ===
concept: Number Type
slug: number-type

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Numbers"
chapter_number: 18
pdf_page: null
section: "Numbers are used for both floating point numbers and integers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "number"
  - "double"
  - "IEEE 754 double precision"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - ieee-754-floating-point
  - safe-integers
  - bigint-type
contrasts_with:
  - bigint-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

JavaScript's `number` type represents both integers and floating point numbers as 64-bit IEEE 754 double-precision floating point values.

# Core Definition

"Numbers are *doubles* -- 64-bit floating point numbers implemented according to the *IEEE Standard for Floating-Point Arithmetic* (IEEE 754)." The type is used for both floating point numbers and integers. Integer numbers are simply floating point numbers without a decimal fraction: `98 === 98.0` is `true` (Ch. 18, Section 18.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. 64-bit IEEE 754 double precision (ES1)
2. Used for both integers and floating point
3. `typeof` returns `'number'`
4. Integers are floats without decimal fractions: `98 === 98.0`
5. Safe integer range: plus/minus 53 bits

# Construction / Recognition

```js
98        // integer literal
123.45    // floating point literal
typeof 98 // 'number'
98 === 98.0 // true
```

# Context & Application

The number type is JavaScript's primary numeric type. For integers beyond 53 bits, use bigints instead.

# Examples

From the source text:

```js
123.45 // floating point number literal
98     // integer literal

> 98 === 98.0
true
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **number-literals** — syntax for writing numbers
- **nan-value** — error value within the number type
- **infinity-value** — error value within the number type
- **safe-integers** — integer subset of numbers

## Related
- **ieee-754-floating-point** — the standard behind the number type

## Contrasts With
- **bigint-type** — arbitrary-precision integers (separate type)

# Common Errors

- **Error**: Expecting JavaScript to have separate integer and float types
  **Correction**: There is only one numeric type (`number`). All numbers are 64-bit floats.

# Common Confusions

- **Confusion**: Thinking integer literals create a different type than float literals
  **Clarification**: Both `98` and `98.0` produce the same value of type `number`.

# Source Reference

Chapter 18: Numbers, Section 18.1, lines 79-111.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with IEEE 754 reference
- Cross-reference status: verified
