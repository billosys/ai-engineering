---
# === CORE IDENTIFICATION ===
concept: Primitive Values
slug: primitive-values

# === CLASSIFICATION ===
category: types-values
subcategory: primitives
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.4 Primitive values vs. objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - primitives

# === TYPED RELATIONSHIPS ===
prerequisites:
  - specification-types
extends: []
related:
  - primitives-are-immutable
  - primitives-passed-by-value
  - primitives-compared-by-value
contrasts_with:
  - objects-overview

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Primitive values are the atomic building blocks of JavaScript data, belonging to seven types: `undefined`, `null`, `boolean`, `number`, `bigint`, `string`, and `symbol`. They are immutable, passed by value, and compared by value.

# Core Definition

"*Primitive values* are the elements of the types `undefined`, `null`, `boolean`, `number`, `bigint`, `string`, `symbol`." (Ch. 14, &sect;14.4). "Primitive values: are atomic building blocks of data in JavaScript. They are *passed by value*: when primitive values are assigned to variables or passed to functions, their contents are copied. They are *compared by value*: when comparing two primitive values, their contents are compared." (Ch. 14, &sect;14.4).

# Prerequisites

- **specification-types** -- primitives are seven of the eight spec types

# Key Properties

1. Seven types: undefined, null, boolean, number, bigint, string, symbol
2. Immutable: cannot change, add, or remove properties
3. Passed by value: contents are copied on assignment
4. Compared by value: contents are compared with `===`
5. Not second-class citizens (unlike in Java)
6. Have properties (via prototype chain) and can be used in same locations as objects

# Construction / Recognition

```js
// Primitive values:
undefined
null
true, false
42, 3.14
123n
'hello'
Symbol('desc')
```

# Context & Application

Understanding primitives is essential for predicting comparison behavior, understanding immutability, and knowing when values can be shared safely.

# Examples

From the source text (Ch. 14, &sect;14.4, 14.5):
```js
// Immutable:
const str = 'abc';
assert.equal(str.length, 3);
// str.length = 1; // TypeError

// Compared by value:
assert.equal(123 === 123, true);
assert.equal('abc' === 'abc', true);
```

# Relationships

## Builds Upon
- **specification-types** -- primitives are seven of eight types

## Enables
- **primitives-are-immutable** -- key primitive property
- **primitives-passed-by-value** -- how primitives are handled
- **primitives-compared-by-value** -- how primitives are compared

## Related
- No additional

## Contrasts With
- **objects-overview** -- objects are mutable, passed/compared by identity

# Common Errors

- **Error**: Trying to add properties to primitive values.
  **Correction**: Primitives are immutable; properties cannot be added or changed.

# Common Confusions

- **Confusion**: Thinking primitives don't have properties.
  **Clarification**: Primitives do have properties (like `'abc'.length`) via the prototype chain, but you can't modify them.

# Source Reference

Chapter 14: Values, Section 14.4-14.5, lines 119-211.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Comprehensive definition with three key properties
- Cross-reference status: verified
