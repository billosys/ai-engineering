---
concept: Map Key Equality (SameValueZero)
slug: map-key-equality
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.5.1 What keys are considered equal?"
extraction_confidence: high
aliases:
  - "SameValueZero"
prerequisites:
  - map-data-structure
extends: []
related:
  - set-element-equality
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Map keys are compared using the internal SameValueZero algorithm, which works like `===` but treats `NaN` as equal to itself, allowing `NaN` to be used as a Map key.

# Core Definition

Most Map operations check key equality via SameValueZero, which works like `===` but considers `NaN` to be equal to itself. This means `NaN` can be a Map key. Different objects are always different keys (identity semantics); configuring key equality is on TC39's long-term roadmap but not yet available.

# Prerequisites

- **map-data-structure** -- key equality governs Map behavior

# Key Properties

1. Like `===` but NaN equals NaN
2. Objects compared by identity (reference), not value
3. Two different `{}` are two different keys
4. Cannot be customized (yet)
5. Same algorithm used by Sets for element equality

# Construction / Recognition

```js
const map = new Map();
map.set(NaN, 123);
map.get(NaN); // 123 -- NaN is a valid key

new Map().set({}, 1).set({}, 2).size; // 2 -- different objects
```

# Context & Application

Understanding key equality is essential to avoid surprises when using objects as Map keys. Since objects are compared by identity, using object literals as keys creates unretrievable entries unless the same reference is used.

# Examples

```js
const map = new Map();
map.set(NaN, 123);
assert.equal(map.get(NaN), 123);

// Objects use identity
const key1 = {};
const key2 = {};
map.set(key1, 'a');
map.set(key2, 'b');
map.size; // 2 (key1 !== key2)
```

(Chapter 36, Section 36.5.1, lines 517-544)

# Relationships

## Builds Upon
- **map-data-structure** -- governs key behavior

## Enables
- Predictable key lookup

## Related
- **set-element-equality** -- Sets use the same algorithm

## Contrasts With
- None

# Common Errors

- **Error**: Using object literals as Map keys and expecting to retrieve values with a new literal.
  **Correction**: `map.set({}, 'a'); map.get({})` returns `undefined` because the two `{}` are different objects.

# Common Confusions

- **Confusion**: `NaN` cannot be a Map key because `NaN !== NaN`.
  **Clarification**: Maps use SameValueZero, not `===`. `NaN` is treated as equal to itself in Maps.

# Source Reference

Chapter 36: Maps (Map), Section 36.5.1, lines 517-544.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with specification reference
- Cross-reference status: verified
