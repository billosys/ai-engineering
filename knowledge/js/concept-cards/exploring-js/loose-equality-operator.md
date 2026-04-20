---
# === CORE IDENTIFICATION ===
concept: Loose Equality Operator
slug: loose-equality-operator

# === CLASSIFICATION ===
category: types-values
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Loose equality (== and !=)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "double equals"
  - "=="
  - "abstract equality"
  - "loose inequality (!=)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strict-equality-operator
  - operator-coercion
extends: []
related:
  - toprimitive
contrasts_with:
  - strict-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `==` (loose equality) and `===` (strict equality) relate to type coercion?"
---

# Quick Definition

The loose equality operator (`==`) compares values with type coercion: if the operands have different types, it attempts to convert them to a common type before comparing.

# Core Definition

Loose equality is defined by the `IsLooselyEqual` algorithm in the ECMAScript specification. When both operands have the same type, it behaves like strict equality. When types differ, it coerces operands: `undefined` and `null` are considered equal to each other; numbers and strings lead to string-to-number conversion; booleans are converted to numbers; objects are converted to primitives via ToPrimitive (Ch. 15, Section 15.5.2).

# Prerequisites

- **strict-equality-operator** -- understanding strict comparison provides the baseline
- **operator-coercion** -- loose equality is built on type coercion

# Key Properties

1. Same-type operands: behaves like strict equality
2. `undefined == null` is `true` (and vice versa)
3. Number vs string: string is converted to number
4. Boolean vs anything: boolean is converted to number first
5. Object vs primitive: object is converted via ToPrimitive
6. Rauschmayer recommends: "always use strict equality"

# Construction / Recognition

```js
'123' == 123     // true (string converted to number)
false == 0       // true (false converted to 0)
undefined == null // true (special case)
```

# Context & Application

Loose equality is considered a JavaScript quirk. The author explicitly recommends always using strict equality (`===`) to avoid unintuitive behavior. The only common use case for `==` is checking for `null` or `undefined` in one comparison.

# Examples

From the source text:

```js
// Sensible coercions
> '123' == 123
true
> false == 0
true

// Less sensible coercions
> 0 == '\r\n\t '  // whitespace-only string
true

// Objects coerced to primitives
> [1, 2, 3] == '1,2,3'
true

// undefined and null are equal to each other
> undefined == null
true

// Gotcha: 2 == true is false (true becomes 1, 2 !== 1)
> 2 == true
false
```

# Relationships

## Builds Upon
- **strict-equality-operator** — same-type comparison delegates to strict equality
- **operator-coercion** — cross-type comparison relies on coercion
- **toprimitive** — objects are converted to primitives for comparison

## Enables
- Nothing -- loose equality is generally discouraged

## Related
- **falsy-and-truthy-values** — loose equality with booleans is different from truthiness

## Contrasts With
- **strict-equality-operator** — strict equality never coerces

# Common Errors

- **Error**: Using `x == true` to check if `x` is truthy
  **Correction**: `2 == true` is `false` because `true` becomes `1`. Use `Boolean(x)` or truthiness checks instead.

- **Error**: Using `x == null` without documenting intent
  **Correction**: Prefer `x === undefined || x === null` for clarity, or use the nullish coalescing operator (`??`).

# Common Confusions

- **Confusion**: Thinking `==` converts both sides to the same type symmetrically
  **Clarification**: The coercion algorithm is asymmetric -- booleans are always converted to numbers first, and the order of conversion steps matters.

# Source Reference

Chapter 15: Operators, Section 15.5.2, lines 499-643.

# Verification Notes

- Definition source: direct (references ECMAScript spec `IsLooselyEqual`)
- Confidence rationale: Complete algorithm specification provided
- Cross-reference status: verified
