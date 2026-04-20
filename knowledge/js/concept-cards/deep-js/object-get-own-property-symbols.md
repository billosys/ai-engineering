---
# === CORE IDENTIFICATION ===
concept: Object.getOwnPropertySymbols()
slug: object-get-own-property-symbols

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: "13.1.2 Operations that consider both enumerable and non-enumerable properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "getOwnPropertySymbols"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - property-key
extends: []
related:
  - object-get-own-property-names
  - reflect-own-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
---

# Quick Definition

`Object.getOwnPropertySymbols(obj)` returns an array of all own symbol-keyed property keys, regardless of enumerability.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.getOwnPropertySymbols()` [ES6] lists the keys of all own symbol-keyed properties."

# Prerequisites

- **Enumerability** — this operation ignores enumerability
- **Property Key** — returns only symbol keys

# Key Properties

1. Returns all own symbol keys (enumerable + non-enumerable)
2. Does not include string keys
3. Own properties only
4. Introduced in ES6

# Construction / Recognition

## To Construct/Create:
1. `Object.getOwnPropertySymbols(obj)`

## To Identify/Recognize:
1. Returns an array of symbols

# Context & Application

Symbol-keyed properties are invisible to most operations (`Object.keys()`, `for-in`, `JSON.stringify()`). This method is one of the few ways to discover them.

# Examples

**Example 1** (Ch 13):
```js
> Object.getOwnPropertySymbols(obj)
[ objEnumSymbolKey, objNonEnumSymbolKey ]
```

# Relationships

## Builds Upon
- **enumerability** — ignores this attribute
- **property-key** — returns only symbol keys

## Enables
- Discovery of symbol-keyed properties

## Related
- **object-get-own-property-names** — the string-key counterpart
- **reflect-own-keys** — returns both string + symbol keys

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Object.keys()` to include symbol-keyed properties.
  **Correction**: `Object.keys()` only returns string keys. Use `Object.getOwnPropertySymbols()` or `Reflect.ownKeys()`.

# Common Confusions

- **Confusion**: Thinking symbol-keyed properties are truly private.
  **Clarification**: `Object.getOwnPropertySymbols()` and `Reflect.ownKeys()` can discover them. They are hidden from many operations but not inaccessible.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.2, lines 217-223.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table.
- Cross-reference status: verified
