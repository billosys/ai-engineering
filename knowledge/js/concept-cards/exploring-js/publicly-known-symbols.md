---
# === CORE IDENTIFICATION ===
concept: Publicly Known Symbols
slug: publicly-known-symbols

# === CLASSIFICATION ===
category: primitive-types
subcategory: symbols
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Symbols"
chapter_number: 24
pdf_page: null
section: "Publicly known symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "well-known symbols"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-type
  - symbols-as-property-keys
extends: []
related:
  - symbol-toprimitive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Symbol and when would you use one?"
---

# Quick Definition

Publicly known symbols are special symbol values defined by ECMAScript (like `Symbol.iterator`, `Symbol.hasInstance`, `Symbol.toStringTag`) that serve as protocol keys for customizing language behavior.

# Core Definition

"Symbols that play special roles within ECMAScript are called *publicly known symbols*." They include `Symbol.iterator` (makes objects iterable), `Symbol.hasInstance` (customizes `instanceof`), and `Symbol.toStringTag` (influences default `.toString()` output). These are predefined symbol values stored as properties of the `Symbol` constructor (Ch. 24, Section 24.4).

# Prerequisites

- **symbol-type** -- publicly known symbols are symbol values
- **symbols-as-property-keys** -- these symbols are used as property keys

# Key Properties

1. `Symbol.iterator`: key for the iteration protocol
2. `Symbol.hasInstance`: customizes `instanceof` behavior
3. `Symbol.toStringTag`: customizes `[object ...]` string representation
4. `Symbol.toPrimitive`: customizes object-to-primitive conversion
5. All are predefined, unique symbol values

# Construction / Recognition

```js
// Symbol.hasInstance example
const PrimitiveNull = {
  [Symbol.hasInstance](x) {
    return x === null;
  }
};
assert.equal(null instanceof PrimitiveNull, true);

// Symbol.toStringTag example
> String({ [Symbol.toStringTag]: 'is no money' })
'[object is no money]'
```

# Context & Application

Publicly known symbols are the mechanism by which ECMAScript defines extensible protocols. Implementing `Symbol.iterator` makes an object work with `for...of`; implementing `Symbol.toPrimitive` controls type conversion.

# Examples

From the source text:

```js
// Symbol.hasInstance
const PrimitiveNull = {
  [Symbol.hasInstance](x) {
    return x === null;
  }
};
assert.equal(null instanceof PrimitiveNull, true);

// Symbol.toStringTag
> String({})
'[object Object]'
> String({ [Symbol.toStringTag]: 'is no money' })
'[object is no money]'
```

# Relationships

## Builds Upon
- **symbol-type** — publicly known symbols are symbol values
- **symbols-as-property-keys** — used as property keys for protocols

## Enables
- Custom iteration protocols
- Custom type checking
- Custom string representations

## Related
- **symbol-toprimitive** — `Symbol.toPrimitive` is a well-known symbol used in ToPrimitive

## Contrasts With
- None

# Common Errors

- **Error**: Trying to create custom well-known symbols that integrate with language features
  **Correction**: Only ECMAScript-defined publicly known symbols affect language behavior. Custom symbols are for application-level protocols only.

# Common Confusions

- **Confusion**: Thinking `Symbol.toStringTag` replaces `.toString()`
  **Clarification**: `Symbol.toStringTag` only affects the default `Object.prototype.toString()` output. The author notes "It's usually better to override `.toString()`."

# Source Reference

Chapter 24: Symbols, Section 24.4, lines 312-360.

# Verification Notes

- Definition source: direct
- Confidence rationale: Three examples of well-known symbols provided
- Cross-reference status: verified against Ch. 15 (Symbol.toPrimitive)
