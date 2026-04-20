---
# === CORE IDENTIFICATION ===
concept: Property Key
slug: property-key

# === CLASSIFICATION ===
category: object-model
subcategory: property-structure
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Property attributes: an introduction"
chapter_number: 10
section: "10.1.2 Property keys"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "property name"
  - "property symbol"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - property-attributes
  - property-descriptor
contrasts_with:
  - string-key
  - symbol-key

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
---

# Quick Definition

A property key is either a string or a symbol. It uniquely identifies a property within an object.

# Core Definition

As described in "Deep JavaScript" Ch 10, "The key of a property is either: A string [or] A symbol." Ch 13 further clarifies the terminology introduced in ES6: "Property keys are either strings or symbols. Property names are property keys that are strings. Property symbols are property keys that are symbols."

# Prerequisites

No prerequisites — this is a foundational concept.

# Key Properties

1. Always either a string or a symbol (never any other type)
2. Uniquely identifies a property within an object
3. String keys are sometimes called "property names"
4. Symbol keys are sometimes called "property symbols"
5. Different operations treat string keys and symbol keys differently

# Construction / Recognition

## To Construct/Create:
1. String keys: use string literals or computed property names
2. Symbol keys: use `Symbol()` or well-known symbols like `Symbol.iterator`

## To Identify/Recognize:
1. If it is used to look up a property on an object, it is a property key
2. `typeof key === 'string'` or `typeof key === 'symbol'`

# Context & Application

The distinction between string keys and symbol keys matters for many property-listing operations. `Object.keys()` only returns string keys; `Object.getOwnPropertySymbols()` only returns symbol keys; `Reflect.ownKeys()` returns both. The `for-in` loop only traverses string keys.

# Examples

**Example 1** (Ch 13):
```js
// String key
const obj = { myProp: 'value' };

// Symbol key
const sym = Symbol('mySymbol');
const obj2 = { [sym]: 'value' };
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **property-descriptor** — descriptors are associated with a specific key
- **object-keys** — returns enumerable own string keys
- **reflect-own-keys** — returns all own keys (both string and symbol)

## Related
- **property-attributes** — each property key maps to a set of attributes

## Contrasts With
- **string-key** — a property key that is specifically a string
- **symbol-key** — a property key that is specifically a symbol

# Common Errors

- **Error**: Assuming property keys can be numbers.
  **Correction**: Numeric keys (like array indices) are converted to strings. Property keys are always strings or symbols.

# Common Confusions

- **Confusion**: `Object.keys()` returns all property keys.
  **Clarification**: `Object.keys()` only returns enumerable own string keys. A better name (noted in Ch 13) would be `Object.names()`. Use `Reflect.ownKeys()` for all own keys.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.2, lines 130-137. Chapter 13: Section 13.1.3, lines 291-297.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in the source text.
- Cross-reference status: verified across Ch 10 and Ch 13
