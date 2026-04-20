---
# === CORE IDENTIFICATION ===
concept: instanceof Operator
slug: instanceof-operator

# === CLASSIFICATION ===
category: types-values
subcategory: type-checking
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.7.2 instanceof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - instanceof

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-overview
extends: []
related:
  - typeof-operator
  - constructor-functions
contrasts_with:
  - typeof-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `typeof` operator and what does it return for each type?"
  - "How do I check if a value is an instance of a class?"
---

# Quick Definition

The `instanceof` operator checks whether a value was created by a specific class, returning `true` if so. It is used for objects; primitive values are never instances of anything.

# Core Definition

"`instanceof` tests which class created a given value." (Ch. 14, &sect;14.7). Syntax: `x instanceof C`. It answers: "has a value `x` been created by a class `C`?" (Ch. 14, &sect;14.7.2). Primitive values are not instances of anything: `123 instanceof Number` is `false`. Rule of thumb: "`typeof` is for primitive values; `instanceof` is for objects." Technically, `instanceof` checks if `C.prototype` is in the prototype chain of `x`.

# Prerequisites

- **objects-overview** -- instanceof operates on objects

# Key Properties

1. Checks if a value was created by a specific class
2. Returns boolean
3. Primitive values always return `false`
4. Works with class inheritance (subclasses pass)
5. Rule: typeof for primitives, instanceof for objects

# Construction / Recognition

```js
(function() {}) instanceof Function  // true
({}) instanceof Object               // true
[] instanceof Array                   // true
123 instanceof Number                 // false (primitive!)
'' instanceof String                  // false (primitive!)
```

# Context & Application

Use `instanceof` to check which class created an object. For primitives, use `typeof`.

# Examples

From the source text (Ch. 14, &sect;14.7.2):
```js
> (function() {}) instanceof Function
true
> ({}) instanceof Object
true
> [] instanceof Array
true

// Primitives are not instances:
> 123 instanceof Number
false
> '' instanceof String
false
> '' instanceof Object
false
```

# Relationships

## Builds Upon
- **objects-overview** -- instanceof operates on objects

## Enables
- Runtime class/type checking for objects

## Related
- **constructor-functions** -- the classes that instanceof checks against

## Contrasts With
- **typeof-operator** -- typeof checks spec types; instanceof checks classes

# Common Errors

- **Error**: Using `instanceof` to check primitive types.
  **Correction**: Primitives are never instances; use `typeof` instead.

# Common Confusions

- **Confusion**: Expecting `'abc' instanceof String` to be true.
  **Clarification**: String primitives are not instances of `String`. Use `typeof x === 'string'` instead.

# Source Reference

Chapter 14: Values, Section 14.7.2, lines 597-643.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with positive and negative examples
- Cross-reference status: verified
