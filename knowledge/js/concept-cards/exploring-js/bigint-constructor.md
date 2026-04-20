---
# === CORE IDENTIFICATION ===
concept: BigInt Constructor Function
slug: bigint-constructor

# === CLASSIFICATION ===
category: primitive-types
subcategory: bigints
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Bigints -- arbitrary-precision integers (advanced)"
chapter_number: 20
pdf_page: null
section: "The wrapper constructor BigInt"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "BigInt()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
extends: []
related:
  - converting-to-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`BigInt(x)` converts values to bigint: integers and parsable strings succeed, while `undefined`, `null`, symbols, and non-integer numbers throw errors. `new BigInt()` throws `TypeError`.

# Core Definition

`BigInt(x)` converts values to bigint with strict rules: `undefined` and `null` throw `TypeError`; booleans become `0n`/`1n`; integers convert directly but non-integers throw `RangeError`; parsable strings convert but unparsable ones throw `SyntaxError`; symbols throw `TypeError`; objects are configurable via `.valueOf()`. `new BigInt()` is not allowed (throws `TypeError`) (Ch. 20, Section 20.5).

# Prerequisites

- **bigint-type** -- the target type

# Key Properties

1. `new BigInt()` throws `TypeError` (not a constructor)
2. `BigInt(undefined)` and `BigInt(null)` throw `TypeError`
3. `BigInt(123)` -> `123n` (integer numbers ok)
4. `BigInt(123.45)` throws `RangeError` (non-integers not ok)
5. `BigInt('123')` -> `123n` (string parsing, supports hex/binary/octal)
6. `BigInt('123n')` throws `SyntaxError` (suffix not allowed in strings)
7. `BigInt.asIntN(width, val)` and `BigInt.asUintN(width, val)` for bit-width casting

# Construction / Recognition

```js
BigInt(123)     // 123n
BigInt('0xFF')  // 255n
BigInt(123.45)  // RangeError
BigInt('abc')   // SyntaxError
```

# Context & Application

Use `BigInt()` for runtime conversion of values to bigints. For compile-time constants, use bigint literals (`123n`).

# Examples

From the source text:

```js
> BigInt(undefined)
TypeError: Cannot convert undefined to a BigInt
> BigInt(null)
TypeError: Cannot convert null to a BigInt
> BigInt('abc')
SyntaxError: Cannot convert abc to a BigInt
> BigInt('123n')
SyntaxError: Cannot convert 123n to a BigInt

> BigInt('123')
123n
> BigInt('0xFF')
255n
> BigInt('0b1101')
13n

> BigInt(123.45)
RangeError: The number 123.45 cannot be converted to a BigInt
> BigInt(123)
123n
```

# Relationships

## Builds Upon
- **bigint-type** — target type of conversion

## Enables
- Runtime bigint conversion

## Related
- **converting-to-number** — similar conversion function for numbers

## Contrasts With
- None

# Common Errors

- **Error**: Including the `n` suffix in string argument: `BigInt('123n')`
  **Correction**: The `n` suffix is only for literals. Use `BigInt('123')`.

# Common Confusions

- **Confusion**: Expecting `BigInt(1.5)` to truncate to `1n`
  **Clarification**: Non-integer numbers throw `RangeError`. Truncate first: `BigInt(Math.trunc(1.5))`.

# Source Reference

Chapter 20: Bigints, Section 20.5, lines 504-765.

# Verification Notes

- Definition source: direct (conversion table provided)
- Confidence rationale: Complete conversion rules with error types
- Cross-reference status: verified
