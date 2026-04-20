---
# === CORE IDENTIFICATION ===
concept: BigInt and Number Cannot Be Mixed
slug: bigint-no-mixing

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
section: "Reusing number operators for bigints (overloading)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bigint-type
  - number-type
extends: []
related:
  - strict-equality-operator
  - loose-equality-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Most JavaScript operators throw a `TypeError` if you mix bigints and numbers, because there is no lossless way to coerce between the types. Exceptions include comparison operators and loose equality.

# Core Definition

"With most operators, we are not allowed to mix bigints and numbers." Mixing throws `TypeError` because numbers cannot represent bigints beyond 53 bits, and bigints cannot represent fractions. However, ordering operators (`<`, `>`, etc.) can safely compare across types, and loose equality (`==`) coerces (e.g., `123n == 123` is `true`). Strict equality returns `false` for cross-type comparisons: `123n === 123` is `false` (Ch. 20, Section 20.4).

# Prerequisites

- **bigint-type** -- one of the mixed types
- **number-type** -- one of the mixed types

# Key Properties

1. Arithmetic operators throw `TypeError` on mixed types: `2n + 1` throws
2. Exception: string concatenation works: `6n + ' apples'` produces `'6 apples'`
3. Loose equality coerces: `123n == 123` is `true`
4. Strict equality: `123n === 123` is `false` (different types)
5. Ordering operators work across types: `3n > -1` is `true`

# Construction / Recognition

```js
> 2n + 1
TypeError: Cannot mix BigInt and other types

> 123n == 123
true
> 123n === 123
false
> 3n > -1
true
```

# Context & Application

This restriction prevents silent precision loss. When converting between types, use `BigInt()` or `Number()` explicitly.

# Examples

From the source text:

```js
> 2n + 1
TypeError: Cannot mix BigInt and other types, use explicit conversions

// But string concatenation works
> 6n + ' apples'
'6 apples'

// Loose equality
> 0n == false
true
> 123n == 123
true

// Strict equality
> 123n === 123
false

// Ordering works across types
> 3n > -1
true
```

# Relationships

## Builds Upon
- **bigint-type** — one type in the mix
- **number-type** — the other type

## Enables
- Understanding when explicit conversion is needed

## Related
- **strict-equality-operator** — cross-type comparison returns false
- **loose-equality-operator** — cross-type comparison with coercion

## Contrasts With
- None

# Common Errors

- **Error**: Writing `bigintValue + numberValue` expecting automatic conversion
  **Correction**: Convert explicitly: `bigintValue + BigInt(numberValue)` or `Number(bigintValue) + numberValue`.

# Common Confusions

- **Confusion**: Thinking `123n === 123` is `true`
  **Clarification**: Strict equality requires same type. Use `123n == 123` for cross-type comparison (but prefer explicit conversion).

# Source Reference

Chapter 20: Bigints, Section 20.4, lines 225-353.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit rules with examples
- Cross-reference status: verified
