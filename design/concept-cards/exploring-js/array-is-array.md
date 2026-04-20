---
concept: "Array.isArray()"
slug: array-is-array
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.3.7 Checking if a value is an Array"
extraction_confidence: high
aliases:
  - "Array.isArray"
prerequisites:
  - array-creation
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`Array.isArray()` reliably checks if a value is an Array, working across realms (e.g., iframes), unlike `instanceof Array` which fails for Arrays from different JavaScript environments.

# Core Definition

`Array.isArray()` checks if a value is an Array. While `instanceof Array` also works, it fails when a value comes from another realm (e.g., same-origin iframes in browsers). `Array.isArray()` does not have this limitation. `typeof` returns `'object'` for arrays and is therefore not useful for array detection.

# Prerequisites

- **array-creation** -- checking array identity

# Key Properties

1. `Array.isArray([])` returns `true`
2. Works across realms (unlike `instanceof`)
3. `typeof []` returns `'object'` (not useful)
4. `instanceof Array` fails for cross-realm arrays

# Construction / Recognition

```js
Array.isArray([]); // true
Array.isArray({}); // false
Array.isArray('abc'); // false
```

# Context & Application

Use `Array.isArray()` whenever you need to verify a value is an Array, especially in library code that may receive values from different contexts.

# Examples

```js
assert.equal(Array.isArray([]), true);
assert.equal([] instanceof Array, true);
assert.equal(typeof [], 'object'); // not useful!
```

(Chapter 34, Section 34.3.7, lines 711-743)

# Relationships

## Builds Upon
- **array-creation** -- checking if values are arrays

## Enables
- Reliable type checking in library code

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using `typeof arr === 'array'` to check for arrays.
  **Correction**: `typeof` returns `'object'` for arrays. Use `Array.isArray()`.

# Common Confusions

- **Confusion**: `instanceof Array` always works.
  **Clarification**: `instanceof` fails for arrays from other realms (iframes, workers).

# Source Reference

Chapter 34: Arrays (Array), Section 34.3.7, lines 711-743.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with cross-realm explanation
- Cross-reference status: verified
