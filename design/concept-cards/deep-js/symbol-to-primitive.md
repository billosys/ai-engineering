---
# === CORE IDENTIFICATION ===
concept: Symbol.toPrimitive
slug: symbol-to-primitive

# === CLASSIFICATION ===
category: type-system
subcategory: conversion-algorithms
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.4.1.2 Which methods are called to convert objects to Primitives?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "[Symbol.toPrimitive]"
  - "@@toPrimitive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - to-primitive
  - type-coercion
extends: []
related:
  - ordinary-to-primitive
  - date-to-primitive
contrasts_with:
  - ordinary-to-primitive

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I perform type coercion using ToPrimitive?"
---

# Quick Definition

`Symbol.toPrimitive` is a well-known symbol that allows objects to override the default `ToPrimitive()` conversion by defining a method that directly controls how the object is converted to a primitive value.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.1): "ToPrimitive() lets objects override the conversion to primitive via `Symbol.toPrimitive`." When an object defines a method with the key `Symbol.toPrimitive`, that method receives the `hint` (`'string'`, `'number'`, or `'default'`) and must return a primitive value. If it returns an object, a `TypeError` is thrown. Only two standard library types override via this mechanism: `Symbol.prototype` and `Date.prototype`.

# Prerequisites

- **ToPrimitive** — Symbol.toPrimitive is the override mechanism within ToPrimitive.
- **Type coercion** — Understanding the broader coercion context.

# Key Properties

1. Method receives the `hint` parameter: `'string'`, `'number'`, or `'default'`.
2. Must return a primitive value; returning an object throws `TypeError`.
3. Takes priority over `valueOf()` and `toString()`.
4. Only `Symbol.prototype` and `Date.prototype` use it in the standard library.
5. `Symbol.prototype[Symbol.toPrimitive]` always returns the wrapped symbol.
6. `Date.prototype[Symbol.toPrimitive]` treats `'default'` as `'string'` (unlike the normal algorithm).

# Construction / Recognition

## To Construct/Create:
1. Define a method with key `Symbol.toPrimitive` on an object or prototype.
2. The method receives one argument: `hint`.

## To Identify/Recognize:
1. Check if an object has a `Symbol.toPrimitive` property that is callable.

# Context & Application

`Symbol.toPrimitive` allows fine-grained control over how objects are coerced. It is the most powerful override mechanism for primitive conversion, taking precedence over `toString()` and `valueOf()`. It is useful when an object needs to behave differently depending on whether a string or number is expected.

# Examples

**Example 1** (Ch 2): Date's override treats 'default' as 'string':
```js
Date.prototype[Symbol.toPrimitive] = function (hint) {
    let O = this;
    if (TypeOf(O) !== 'object') {
      throw new TypeError();
    }
    let tryFirst;
    if (hint === 'string' || hint === 'default') {
      tryFirst = 'string';
    } else if (hint === 'number') {
      tryFirst = 'number';
    } else {
      throw new TypeError();
    }
    return OrdinaryToPrimitive(O, tryFirst);
  };
```

**Example 2** (Ch 2): Date coercion with `==` (which uses default hint):
```js
const d = new Date('2222-03-27');
assert.equal(
  d == 'Wed Mar 27 2222 01:00:00 GMT+0100'
       + ' (Central European Standard Time)',
  true);
```

# Relationships

## Builds Upon
- **ToPrimitive** — Symbol.toPrimitive is checked as the first step within ToPrimitive.

## Enables
- **Date primitive conversion** — Dates use this to prefer strings for default hint.

## Related
- **OrdinaryToPrimitive** — The fallback when Symbol.toPrimitive is not defined.

## Contrasts With
- **OrdinaryToPrimitive** — OrdinaryToPrimitive uses valueOf/toString; Symbol.toPrimitive replaces them entirely.

# Common Errors

- **Error**: Returning an object from a `Symbol.toPrimitive` method.
  **Correction**: The method must return a primitive value. Returning an object throws `TypeError`.

# Common Confusions

- **Confusion**: `Symbol.toPrimitive` is called alongside `valueOf`/`toString`.
  **Clarification**: `Symbol.toPrimitive` completely overrides the normal conversion. If it is defined, `valueOf` and `toString` are not called by the coercion algorithm.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.1.2-2.4.1.3, lines 515-614.

# Verification Notes

- Definition source: direct (algorithm and explanation from source)
- Confidence rationale: Detailed coverage with Date example
- Cross-reference status: verified
