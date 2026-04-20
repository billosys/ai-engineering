---
# === CORE IDENTIFICATION ===
concept: ToPrimitive
slug: toprimitive

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
section: "Converting values to primitives (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ToPrimitive algorithm"
  - "object-to-primitive conversion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - operator-coercion
extends: []
related:
  - symbol-toprimitive
  - converting-to-number
  - converting-to-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

ToPrimitive is the internal ECMAScript algorithm that converts objects to primitive values, used by operators when they need primitive operands.

# Core Definition

ToPrimitive is a spec-level operation that converts any value to a primitive. If the input is already primitive, it is returned unchanged. If the input is an object, ToPrimitive first checks for a `Symbol.toPrimitive` method; if absent, it falls back to `OrdinaryToPrimitive`, which calls `.toString()` or `.valueOf()` in an order determined by a preferred type hint (Ch. 15, Section 15.2).

# Prerequisites

- **operator-coercion** -- understanding why objects need to be converted to primitives

# Key Properties

1. If input is already primitive, returns it unchanged
2. Checks for `Symbol.toPrimitive` method first (only `Symbol.prototype` and `Date.prototype` define this)
3. Falls back to `OrdinaryToPrimitive` which tries `.toString()` and `.valueOf()`
4. With STRING hint: tries `.toString()` first, then `.valueOf()`
5. With NUMBER hint (or no hint): tries `.valueOf()` first, then `.toString()`
6. Throws `TypeError` if no primitive result can be obtained

# Construction / Recognition

ToPrimitive is invoked implicitly by operators. To customize it:

```js
const obj = {
  toString() { return '1'; },
  valueOf() { return 2; },
};
String(obj) // '1' -- STRING hint, calls toString() first
Number(obj) // 2   -- NUMBER hint, calls valueOf() first
```

# Context & Application

ToPrimitive is invoked whenever an operator needs a primitive value from an object operand. Understanding it explains why `String(obj)` and `Number(obj)` can produce different results for the same object.

# Examples

From the source text:

```js
const obj = {
  toString() { return '1'; },
  valueOf() { return 2; },
};
assert.equal(String(obj), '1'); // STRING hint
assert.equal(Number(obj), 2);  // NUMBER hint
```

Only `Symbol.prototype` and `Date.prototype` define `Symbol.toPrimitive` in the standard library.

# Relationships

## Builds Upon
- **operator-coercion** — ToPrimitive is the mechanism behind object-to-primitive coercion

## Enables
- **plus-operator** — uses ToPrimitive to convert object operands
- **loose-equality-operator** — uses ToPrimitive when comparing objects with primitives

## Related
- **symbol-toprimitive** — the well-known symbol that customizes ToPrimitive behavior

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `+` on objects always calls `.toString()`
  **Correction**: The default hint is NUMBER, so `.valueOf()` is tried first. Only if it returns an object does `.toString()` get called.

# Common Confusions

- **Confusion**: Thinking `Symbol.toPrimitive` is commonly used
  **Clarification**: Only `Symbol.prototype` and `Date.prototype` define it in the standard library. Most objects rely on `OrdinaryToPrimitive`.

# Source Reference

Chapter 15: Operators, Section 15.2, lines 111-215.

# Verification Notes

- Definition source: direct (algorithm code provided in source)
- Confidence rationale: The author provides a complete JavaScript implementation of the spec algorithm
- Cross-reference status: verified against ECMAScript specification link in source
