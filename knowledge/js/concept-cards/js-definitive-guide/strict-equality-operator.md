---
# === CORE IDENTIFICATION ===
concept: Strict Equality Operator (===)
slug: strict-equality-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 96
section: "4.9.1 Equality and Inequality Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "identity operator"
  - "triple equals"
  - "=== operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - comparison-operators
contrasts_with:
  - loose-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == from ===? (operator side)"
---

# Quick Definition

The strict equality operator (`===`) compares two values without any type conversion, returning `true` only if both values have the same type and the same value.

# Core Definition

"The === operator is known as the strict equality operator (or sometimes the identity operator), and it checks whether its two operands are 'identical' using a strict definition of sameness." It performs no type conversion. (Ch. 4, §4.9.1)

# Prerequisites

- **primary-expressions** — Operands of `===` are expressions that produce values.

# Key Properties

1. Different types are never equal: `1 === "1"` is `false`.
2. Both `null` and both `undefined` are equal to themselves: `null === null` is `true`.
3. `NaN` is not equal to anything, including itself: `NaN === NaN` is `false`. Use `x !== x` or `isNaN()` to test.
4. `0 === -0` is `true`.
5. Strings must have exactly the same 16-bit values in the same positions (no Unicode normalization).
6. Objects/arrays/functions are equal only if they are the same reference; identical contents are not enough.
7. `!==` is the strict inequality counterpart.

# Construction / Recognition

```js
value1 === value2   // Strict equality
value1 !== value2   // Strict inequality
```

# Context & Application

The strict equality operator should be preferred over `==` in virtually all cases. It is the recommended default comparison operator because it avoids the confusing implicit type conversions of `==`.

# Examples

From the source text (§4.9.1, pp. 96-98):

```js
1 === 1           // true
1 === "1"         // false (different types)
null === null     // true
null === undefined // false (different types)
NaN === NaN       // false (NaN is never equal to anything)
0 === -0          // true

// Objects compared by reference:
let a = {x: 1};
let b = {x: 1};
a === b           // false (different objects)
a === a           // true (same reference)
```

# Relationships

## Builds Upon
- **primary-expressions** — Compares values produced by expressions

## Enables
- **switch-case-statement** — `switch` uses `===` for case matching

## Related
- **comparison-operators** — Other relational operators for ordering

## Contrasts With
- **loose-equality-operator** — `==` allows type coercion; `===` does not

# Common Errors

- **Error**: Using `===` to test for NaN.
  **Correction**: `NaN === NaN` is `false`. Use `Number.isNaN(x)` or `x !== x` instead.

- **Error**: Expecting `===` to compare object contents.
  **Correction**: `===` compares references. Two distinct objects with identical properties are not `===`.

# Common Confusions

- **Confusion**: Believing `0` and `-0` are different under `===`.
  **Clarification**: `0 === -0` evaluates to `true`, despite being technically different values.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.9.1, pages 96-98.

# Verification Notes

- Definition source: Direct quote from §4.9.1
- Confidence rationale: High — detailed algorithm with complete rules
- Uncertainties: None
- Cross-reference status: Verified against §3.8 (reference comparison)
