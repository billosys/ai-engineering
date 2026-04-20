---
# === CORE IDENTIFICATION ===
concept: Reflect.ownKeys()
slug: reflect-own-keys

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-key
  - enumerability
extends: []
related:
  - object-get-own-property-names
  - object-get-own-property-symbols
contrasts_with:
  - object-keys

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
---

# Quick Definition

`Reflect.ownKeys(obj)` returns an array of all own property keys of an object, including both string and symbol keys, regardless of enumerability. It is the most comprehensive key-listing operation.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Reflect.ownKeys()` [ES6] lists the keys of all own properties." It returns both string keys and symbol keys, both enumerable and non-enumerable. The book notes that `Reflect` methods "deviate from" the naming convention (where short names skip non-enumerable) "because `Reflect` provides operations that are more 'meta' and related to Proxies."

# Prerequisites

- **Property Key** — returns both string and symbol keys
- **Enumerability** — ignores enumerability (returns all)

# Key Properties

1. Returns ALL own keys (string + symbol)
2. Ignores enumerability (returns both enumerable and non-enumerable)
3. Own properties only (not inherited)
4. Introduced in ES6
5. Most comprehensive key-listing operation

# Construction / Recognition

## To Construct/Create:
1. `Reflect.ownKeys(obj)`

## To Identify/Recognize:
1. Returns an array that may contain both strings and symbols

# Context & Application

`Reflect.ownKeys()` is the go-to method when you need a complete picture of an object's own properties. It is useful for metaprogramming, debugging, and when you need to see non-enumerable or symbol-keyed properties.

# Examples

**Example 1** (Ch 13):
```js
> Reflect.ownKeys(obj)
[
  'objEnumStringKey',
  'objNonEnumStringKey',
  objEnumSymbolKey,
  objNonEnumSymbolKey
]
```

# Relationships

## Builds Upon
- **property-key** — returns all key types
- **enumerability** — ignores this attribute

## Enables
- Complete property introspection

## Related
- **object-get-own-property-names** — only string keys (enum + non-enum)
- **object-get-own-property-symbols** — only symbol keys (enum + non-enum)

## Contrasts With
- **object-keys** — only enumerable own string keys

# Common Errors

- **Error**: Expecting `Reflect.ownKeys()` to include inherited properties.
  **Correction**: It only returns own properties. For inherited properties, traverse the prototype chain.

# Common Confusions

- **Confusion**: Thinking `Object.keys()` and `Reflect.ownKeys()` return the same results.
  **Clarification**: `Object.keys()` returns only enumerable string keys; `Reflect.ownKeys()` returns ALL own keys.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.2, lines 225-235. Section 13.1.3, lines 287-289.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table with comparison.
- Cross-reference status: verified
