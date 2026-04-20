---
# === CORE IDENTIFICATION ===
concept: Symbol.toPrimitive
slug: symbol-toprimitive

# === CLASSIFICATION ===
category: primitive-types
subcategory: symbols
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "Converting values to primitives (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "@@toPrimitive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-type
  - publicly-known-symbols
  - toprimitive
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol and when would you use one?"
---

# Quick Definition

`Symbol.toPrimitive` is a well-known symbol used as a method key that customizes how an object is converted to a primitive value, receiving a hint of `'string'`, `'number'`, or `'default'`.

# Core Definition

When an object is being converted to a primitive, the ToPrimitive algorithm first checks for a method keyed by `Symbol.toPrimitive`. If present, it is called with a hint (`'string'`, `'number'`, or `'default'`). In the standard library, only `Symbol.prototype` and `Date.prototype` define this method (Ch. 15, Section 15.2).

# Prerequisites

- **symbol-type** -- `Symbol.toPrimitive` is a symbol
- **publicly-known-symbols** -- it is a well-known symbol
- **toprimitive** -- it is part of the ToPrimitive algorithm

# Key Properties

1. Method key: `Symbol.toPrimitive`
2. Receives hint: `'string'`, `'number'`, or `'default'`
3. Must return a primitive value (or `TypeError` is thrown)
4. Only `Symbol.prototype` and `Date.prototype` define it in the standard library
5. Takes priority over `.toString()` and `.valueOf()` in ToPrimitive

# Construction / Recognition

```js
const obj = {
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return 42;
    if (hint === 'string') return 'hello';
    return true; // default
  }
};
```

# Context & Application

Use `Symbol.toPrimitive` to fully control how custom objects are converted to primitives in different contexts (numeric vs string vs default).

# Examples

From the source text, the ToPrimitive algorithm checks for `Symbol.toPrimitive` first:

```js
const exoticToPrim = input[Symbol.toPrimitive]; // (A)
if (exoticToPrim !== undefined) {
  // Call it with the appropriate hint
  const result = exoticToPrim.apply(input, [hint]);
  if (!isObject(result)) return result;
  throw new TypeError();
}
```

# Relationships

## Builds Upon
- **symbol-type** — uses symbol as method key
- **publicly-known-symbols** — one of the well-known symbols
- **toprimitive** — integrated into the ToPrimitive algorithm

## Enables
- Custom primitive conversion behavior

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Returning an object from `Symbol.toPrimitive`
  **Correction**: The method must return a primitive value. Returning an object throws `TypeError`.

# Common Confusions

- **Confusion**: Thinking `Symbol.toPrimitive` is commonly needed
  **Clarification**: Most objects use the default `.valueOf()` and `.toString()` methods. Only define `Symbol.toPrimitive` for special conversion needs.

# Source Reference

Chapter 15: Operators, Section 15.2, lines 111-196.

# Verification Notes

- Definition source: direct
- Confidence rationale: Algorithm code in source shows its role
- Cross-reference status: verified against Ch. 24 (publicly known symbols)
