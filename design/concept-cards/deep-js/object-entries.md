---
# === CORE IDENTIFICATION ===
concept: Object.entries()
slug: object-entries

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
extends: []
related:
  - object-keys
  - object-values
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

`Object.entries()` returns an array of `[key, value]` pairs for enumerable own string-keyed properties of an object. Introduced in ES2017.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.entries()` [ES2017] returns key-value pairs for enumerable own string-keyed properties." The book also notes: "`Object.fromEntries()` does accept symbols as keys, but only creates enumerable properties."

# Prerequisites

- **Enumerability** — only returns entries for enumerable properties

# Key Properties

1. Returns `[key, value]` pairs as arrays
2. Only enumerable own string-keyed properties
3. Useful for converting objects to Maps: `new Map(Object.entries(obj))`
4. Introduced in ES2017

# Construction / Recognition

## To Construct/Create:
1. `Object.entries(obj)`

## To Identify/Recognize:
1. Returns an array of `[string, any]` pairs

# Context & Application

Useful for iterating with both key and value, converting objects to Maps, or transforming objects via `Object.fromEntries()`.

# Examples

**Example 1** (Ch 13):
```js
> Object.entries(obj)
[ [ 'objEnumStringKey', 'objEnumStringKeyValue' ] ]
```

# Relationships

## Builds Upon
- **enumerability** — filters by enumerable attribute

## Enables
- Object-to-Map conversion
- Key-value iteration

## Related
- **object-keys** — returns only keys
- **object-values** — returns only values

## Contrasts With
- None

# Common Errors

- **Error**: Expecting symbol-keyed entries to be included.
  **Correction**: Only string-keyed enumerable own properties are included.

# Common Confusions

- **Confusion**: Thinking `Object.entries()` and `Object.fromEntries()` are perfect inverses.
  **Clarification**: `Object.fromEntries()` accepts symbols as keys and creates enumerable properties, while `Object.entries()` only outputs string keys.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 138-145.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table.
- Cross-reference status: verified
