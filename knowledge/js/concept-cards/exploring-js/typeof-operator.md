---
# === CORE IDENTIFICATION ===
concept: typeof Operator
slug: typeof-operator

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
section: "14.7.1 typeof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - typeof

# === TYPED RELATIONSHIPS ===
prerequisites:
  - specification-types
extends: []
related:
  - instanceof-operator
contrasts_with:
  - instanceof-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `typeof` operator and what does it return for each type?"
---

# Quick Definition

The `typeof` operator returns a string indicating the type of a value, roughly corresponding to the specification's seven types but with two known quirks: `typeof null` returns `'object'` and `typeof function` returns `'function'`.

# Core Definition

`typeof` "distinguishes the 7 types of the specification (minus one omission, plus one addition)." (Ch. 14, &sect;14.7). Results: `undefined` -> `'undefined'`, `null` -> `'object'` (bug), Boolean -> `'boolean'`, Number -> `'number'`, Bigint -> `'bigint'`, String -> `'string'`, Symbol -> `'symbol'`, Function -> `'function'`, all other objects -> `'object'`. Rule of thumb: "`typeof` is for primitive values; `instanceof` is for objects." (Ch. 14, &sect;14.7).

# Prerequisites

- **specification-types** -- typeof maps to spec types (with quirks)

# Key Properties

1. Returns a string
2. `typeof null === 'object'` -- a historical bug that can't be fixed
3. `typeof function` returns `'function'` -- not a spec type, but a special case
4. Works for all seven primitive types (except null quirk)
5. Returns `'object'` for all non-function objects
6. Rule: typeof for primitives, instanceof for objects

# Construction / Recognition

```js
typeof undefined    // 'undefined'
typeof null         // 'object' (bug!)
typeof true         // 'boolean'
typeof 123          // 'number'
typeof 123n         // 'bigint'
typeof 'abc'        // 'string'
typeof Symbol()     // 'symbol'
typeof function(){} // 'function'
typeof {}           // 'object'
typeof []           // 'object'
```

# Context & Application

`typeof` is the primary way to check primitive types at runtime. For objects, use `instanceof` or other checks.

# Examples

From the source text (Ch. 14, &sect;14.7.1):
```js
> typeof undefined
'undefined'
> typeof 123n
'bigint'
> typeof 'abc'
'string'
> typeof {}
'object'
```

# Relationships

## Builds Upon
- **specification-types** -- typeof reports spec types

## Enables
- Runtime type checking for primitives

## Related
- No additional

## Contrasts With
- **instanceof-operator** -- instanceof checks class membership, not spec types

# Common Errors

- **Error**: Using `typeof x === 'null'` to check for null.
  **Correction**: `typeof null` returns `'object'`. Use `x === null` instead.

- **Error**: Using `typeof` to check for arrays.
  **Correction**: `typeof []` returns `'object'`. Use `Array.isArray()` instead.

# Common Confusions

- **Confusion**: Expecting `typeof null` to return `'null'`.
  **Clarification**: This is a well-known bug. TC39 considered fixing it but it would break existing code.

- **Confusion**: Thinking `typeof` can distinguish between different object types.
  **Clarification**: `typeof` returns `'object'` for all non-function objects. Use `instanceof` for class checking.

# Source Reference

Chapter 14: Values, Section 14.7.1, lines 424-583.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Complete result table provided
- Cross-reference status: verified
