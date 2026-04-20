---
# === CORE IDENTIFICATION ===
concept: Object.keys()
slug: object-keys

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
section: "13.1.1 Operations that only consider enumerable properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - property-key
extends: []
related:
  - object-values
  - object-entries
contrasts_with:
  - reflect-own-keys
  - object-get-own-property-names

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
  - "What is enumerability?"
---

# Quick Definition

`Object.keys()` returns an array of the enumerable own string-keyed property keys of an object. It ignores symbol keys, inherited properties, and non-enumerable properties.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.keys()` [ES5] returns the keys of enumerable own string-keyed properties." Ch 13 also notes that "a better name for `Object.keys()` would now be `Object.names()`" since ES6 distinguishes between property names (strings) and property symbols.

# Prerequisites

- **Enumerability** — only returns enumerable properties
- **Property Key** — returns only string keys, not symbol keys

# Key Properties

1. Returns only enumerable properties
2. Returns only own properties (not inherited)
3. Returns only string keys (not symbols)
4. Introduced in ES5
5. Short name because ignoring non-enumerable is the common case

# Construction / Recognition

## To Construct/Create:
1. `Object.keys(obj)`

## To Identify/Recognize:
1. Returns an array of strings

# Context & Application

`Object.keys()` is the recommended replacement for `for-in` when iterating over own properties. Combined with `for-of`, it provides a clean way to iterate over an object's properties without inherited ones.

# Examples

**Example 1** (Ch 13):
```js
> Object.keys(obj)
[ 'objEnumStringKey' ]
```

# Relationships

## Builds Upon
- **enumerability** — filters by enumerable attribute
- **property-key** — returns only string keys

## Enables
- Clean iteration over own enumerable properties

## Related
- **object-values** — returns values instead of keys
- **object-entries** — returns key-value pairs

## Contrasts With
- **reflect-own-keys** — returns ALL own keys (string + symbol, enumerable + non-enumerable)
- **object-get-own-property-names** — returns all own string keys (including non-enumerable)

# Common Errors

- **Error**: Expecting `Object.keys()` to include symbol-keyed properties.
  **Correction**: `Object.keys()` only returns string keys. Use `Reflect.ownKeys()` for both strings and symbols.

# Common Confusions

- **Confusion**: Thinking `Object.keys()` includes inherited properties.
  **Clarification**: It only returns own properties. `for-in` includes inherited properties.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 122-128.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in the operations table.
- Cross-reference status: verified
