---
# === CORE IDENTIFICATION ===
concept: Object.values()
slug: object-values

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
  - object-entries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

`Object.values()` returns an array of the values of enumerable own string-keyed properties of an object. Introduced in ES2017.

# Core Definition

As described in "Deep JavaScript" Ch 13, "`Object.values()` [ES2017] returns the values of enumerable own string-keyed properties."

# Prerequisites

- **Enumerability** — only returns values of enumerable properties

# Key Properties

1. Returns only values of enumerable properties
2. Returns only own properties (not inherited)
3. Only considers string-keyed properties (not symbol-keyed)
4. Introduced in ES2017

# Construction / Recognition

## To Construct/Create:
1. `Object.values(obj)`

## To Identify/Recognize:
1. Returns an array of values (any type)

# Context & Application

Useful for iterating over all own property values without needing the keys. Complements `Object.keys()` and `Object.entries()`.

# Examples

**Example 1** (Ch 13):
```js
> Object.values(obj)
[ 'objEnumStringKeyValue' ]
```

# Relationships

## Builds Upon
- **enumerability** — filters by enumerable attribute

## Enables
- Value-focused iteration over objects

## Related
- **object-keys** — returns keys instead of values
- **object-entries** — returns key-value pairs

## Contrasts With
- None

# Common Errors

- **Error**: Expecting symbol-keyed property values to be included.
  **Correction**: Only string-keyed enumerable own properties are considered.

# Common Confusions

- **Confusion**: Thinking `Object.values()` works on iterables.
  **Clarification**: It works on objects, returning property values. For iterables, use `Array.from()` or spreading.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.1, lines 130-136.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the operations table.
- Cross-reference status: verified
