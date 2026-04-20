---
# === CORE IDENTIFICATION ===
concept: Strict Equality Operator
slug: strict-equality-operator

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
section: "Strict equality (=== and !==)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "triple equals"
  - "==="
  - "strict inequality (!==)"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - object-is
  - nan-value
contrasts_with:
  - loose-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `==` (loose equality) and `===` (strict equality) relate to type coercion?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

The strict equality operator (`===`) compares two values without type coercion: values must be the same type and the same value (or same identity for objects and symbols) to be equal.

# Core Definition

"Two values are only strictly equal if they have the same type. Strict equality never coerces." Primitive values (excluding symbols) are compared by value. Objects and symbols are compared by identity -- they are only equal to themselves. Notably, `NaN === NaN` is `false` (Ch. 15, Section 15.5.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Never performs type coercion (ES1)
2. Primitives (except symbols) are compared by value
3. Objects and symbols are compared by identity (reference equality)
4. `NaN === NaN` is `false` (NaN is not equal to itself)
5. Rauschmayer recommends always using `===` over `==`

# Construction / Recognition

```js
// Same type, same value -- true
3 === 3           // true
'c' === 'c'       // true

// Different types -- always false
undefined === null // false

// Objects compared by identity
{} === {}          // false (different objects)
const obj = {};
obj === obj        // true (same reference)
```

# Context & Application

Strict equality is the recommended comparison operator in JavaScript. It avoids the unintuitive coercion rules of loose equality and makes code easier to understand and reason about.

# Examples

From the source text:

```js
> undefined === null
false
> 3 === 3
true
> 'c' === 'c'
true

// Objects compared by identity
> {} === {}
false
> const obj = {};
> obj === obj
true

// Symbols compared by identity
> Symbol() === Symbol()
false

// NaN is not strictly equal to itself
> NaN === NaN
false
```

# Relationships

## Builds Upon
- No strict prerequisites

## Enables
- **object-is** — even stricter comparison that handles NaN and -0

## Related
- **nan-value** — NaN's self-inequality is a key strict equality edge case

## Contrasts With
- **loose-equality-operator** — loose equality coerces operands before comparing

# Common Errors

- **Error**: Using `=== NaN` to check for NaN
  **Correction**: `NaN === NaN` is `false`. Use `Number.isNaN(x)` instead.

# Common Confusions

- **Confusion**: Thinking `===` compares objects by their contents
  **Clarification**: `===` compares objects by identity (reference), not by structural equality. Two objects with identical properties are not `===`.

# Source Reference

Chapter 15: Operators, Section 15.5.1, lines 430-497.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comprehensive examples
- Cross-reference status: verified
