---
concept: Map vs. Object
slug: map-vs-object
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.7.1 When should I use a Map, and when should I use an object?"
extraction_confidence: high
aliases: []
prerequisites:
  - map-data-structure
extends: []
related:
  - map-converting-to-from-objects
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Use a Map when keys are not strings/symbols or when the key set changes at runtime; use an object when keys are fixed and known at development time.

# Core Definition

If we need keys that are not strings or symbols, we must use a Map. For string/symbol keys: use an object when the set of keys is fixed (known at development time) with fixed-key access (`obj.key`); use a Map when the key set changes at runtime with dynamic-key access (`map.get(theKey)`).

# Prerequisites

- **map-data-structure** -- understanding Maps

# Key Properties

1. Objects: fixed keys, direct property access, JSON-compatible
2. Maps: dynamic keys, any key type, guaranteed order, `.size`
3. Maps have no prototype pollution issues
4. Objects support destructuring; Maps do not
5. Maps use `.size`; Arrays use `.length`

# Construction / Recognition

```js
// Fixed keys -> use object
const value = obj.key;

// Dynamic keys -> use Map
const theKey = 123;
map.get(theKey);
```

# Context & Application

This is a fundamental design decision. Most configuration-like data uses objects. Runtime-populated dictionaries, caches, and frequency counters benefit from Maps.

# Examples

```js
// Object: fixed keys
const person = { first: 'Jane', last: 'Doe' };

// Map: dynamic keys
const charCounts = new Map();
for (const ch of 'hello') {
  charCounts.set(ch, (charCounts.get(ch) ?? 0) + 1);
}
```

(Chapter 36, Section 36.7.1, lines 811-840)

# Relationships

## Builds Upon
- **map-data-structure** -- comparing Maps to objects

## Enables
- Informed collection choice

## Related
- **map-converting-to-from-objects** -- conversion between the two

## Contrasts With
- None

# Common Errors

- **Error**: Using objects as dictionaries with user-provided string keys (risk of prototype property collision).
  **Correction**: Use a Map, or create objects with `Object.create(null)`.

# Common Confusions

- **Confusion**: Maps are always better than objects.
  **Clarification**: Objects are simpler for fixed-key structures, support JSON, and allow destructuring.

# Source Reference

Chapter 36: Maps (Map), Section 36.7.1, lines 811-840.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly addressed as FAQ
- Cross-reference status: verified
