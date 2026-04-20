---
# === CORE IDENTIFICATION ===
concept: Operator Coercion
slug: operator-coercion

# === CLASSIFICATION ===
category: types-values
subcategory: coercion
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Making sense of operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "implicit type conversion"
  - "type coercion"
  - "automatic type conversion"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - converting-to-number
  - converting-to-boolean
  - converting-to-string
  - toprimitive
contrasts_with:
  - strict-equality-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `==` (loose equality) and `===` (strict equality) relate to type coercion?"
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Operator coercion is JavaScript's automatic conversion of operands to the types an operator expects, rather than throwing an exception when types don't match.

# Core Definition

As Rauschmayer explains: "If an operator gets operands that don't have the proper types, it rarely throws an exception. Instead, it *coerces* (automatically converts) the operands so that it can work with them" (Ch. 15, Section 15.1.1). Most operators only work with primitive values, so objects are first coerced to primitives.

# Prerequisites

Foundational concept -- requires basic understanding of JavaScript types.

# Key Properties

1. Operators coerce their operands to appropriate types rather than throwing exceptions
2. Most operators only work with primitive values; objects are coerced to primitives first
3. The multiplication operator converts strings to numbers: `'7' * '3'` produces `21`
4. The square brackets operator coerces non-string/symbol keys to strings
5. Two key rules make operator behavior predictable: coercion to appropriate types, and primitive-only operation

# Construction / Recognition

Coercion is implicit -- it happens automatically when operators receive unexpected types. Recognize it when:
- Strings appear in arithmetic operations
- Objects appear where primitives are expected
- Arrays are used with the `+` operator

# Context & Application

Understanding coercion is essential for debugging unexpected results in JavaScript expressions. It explains why `[1,2,3] + [4,5,6]` produces `'1,2,34,5,6'` -- both arrays are coerced to strings via their `.toString()` method, then concatenated.

# Examples

From the source text:

```js
> '7' * '3'
21
// Multiplication coerces strings to numbers

> [1,2,3] + [4,5,6]
'1,2,34,5,6'
// Plus operator coerces arrays to primitives (strings), then concatenates
```

Property access coerces keys to strings:
```js
const obj = {};
obj['true'] = 123;
assert.equal(obj[true], 123); // true coerced to 'true'
```

# Relationships

## Builds Upon
- No strict prerequisites -- foundational concept

## Enables
- **loose-equality-operator** — loose equality uses coercion to compare different types
- **plus-operator** — understanding coercion explains plus operator's dual behavior

## Related
- **converting-to-number** — explicit version of numeric coercion
- **toprimitive** — the algorithm used to coerce objects to primitives

## Contrasts With
- **strict-equality-operator** — strict equality never coerces operands

# Common Errors

- **Error**: Expecting `[1,2,3] + [4,5,6]` to produce `[1,2,3,4,5,6]`
  **Correction**: The `+` operator coerces arrays to strings and concatenates them. Use `[...arr1, ...arr2]` or `.concat()` to combine arrays.

# Common Confusions

- **Confusion**: Thinking coercion only applies to `==`
  **Clarification**: Most operators perform coercion, including arithmetic operators, property access, and comparison operators.

# Source Reference

Chapter 15: Operators, Section 15.1, lines 45-110.

# Verification Notes

- Definition source: direct (explicit definition from source)
- Confidence rationale: The author provides a clear, explicit definition with examples
- Cross-reference status: verified against Ch. 18 (Number coercion) and Ch. 17 (Boolean coercion)
