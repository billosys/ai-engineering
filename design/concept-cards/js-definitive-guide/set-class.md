---
# === CORE IDENTIFICATION ===
concept: Set Class
slug: set-class

# === CLASSIFICATION ===
category: standard-library
subcategory: collections
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 286
section: "11.1.1 The Set Class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - map-class
  - weak-set
contrasts_with:
  - map-class

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `Set` from `Array`?"
---

# Quick Definition

An ES6 collection class that stores unique values of any type, optimized for fast membership testing with the `has()` method, unlike arrays which require linear-time `includes()` checks.

# Core Definition

"A set is a collection of values, like an array is. Unlike arrays, however, sets are not ordered or indexed, and they do not allow duplicates: a value is either a member of a set or it is not a member" (p. 286). Sets use strict equality (`===`) for membership comparison, meaning objects are compared by identity, not by value.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. No duplicates — adding a value already present has no effect
2. Membership testing with `has()` is O(1), unlike Array's `includes()` which is O(n)
3. Uses strict equality (`===`) for comparisons — objects compared by identity
4. Iterable — works with `for/of`, spread operator, and destructuring
5. Maintains insertion order during iteration
6. `size` property (not `length`) gives the number of elements

# Construction / Recognition

```js
let s = new Set();                           // Empty set
let t = new Set([1, s]);                     // From array
let unique = new Set("Mississippi");          // => {"M","i","s","p"}
```

Key methods: `add()`, `delete()`, `has()`, `clear()`, `forEach()`.

# Context & Application

Use Set when you need to track unique values, test membership efficiently, or remove duplicates from an array: `[...new Set(array)]`.

# Examples

From the source text (p. 286-288): `new Set("Mississippi")` creates a Set with 4 elements: "M", "i", "s", "p". Membership test: `oneDigitPrimes.has(2)` returns `true`. Converting to array: `[...oneDigitPrimes]` returns `[2,3,5,7]`. Note that `s.delete([1,2,3])` returns `false` because the array in the set is a different object (identity comparison).

# Relationships

## Enables
- **Iteration with for/of** — Sets are iterable

## Related
- **Map Class** — Another ES6 collection; Map stores key-value pairs, Set stores values only
- **WeakSet** — A variant that allows garbage collection of its members

## Contrasts With
- **Array** — Arrays are ordered and indexed, allow duplicates, and have O(n) membership testing. Sets are unindexed, disallow duplicates, and have O(1) membership testing.

# Common Errors

- **Error**: Expecting `add()` to accept multiple arguments or an array of values.
  **Correction**: `add()` takes a single argument. To add multiple values, chain calls: `s.add('a').add('b').add('c')`.

# Common Confusions

- **Confusion**: Expecting two different objects with identical properties to be treated as the same Set member.
  **Clarification**: Set uses identity comparison (like `===`), so two distinct objects are always different members, even if they have the same properties.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.1.1, pages 286-289.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — thoroughly described
- Uncertainties: None
- Cross-reference status: Verified
