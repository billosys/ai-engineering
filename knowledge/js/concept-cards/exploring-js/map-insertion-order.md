---
concept: Map Insertion Order
slug: map-insertion-order
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.2.2 Listed in insertion order: entries, keys, values"
extraction_confidence: high
aliases: []
prerequisites:
  - map-data-structure
extends: []
related:
  - set-data-structure
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Maps preserve the order in which entries were created, honoring that order when listing keys, values, or entries; this makes iteration deterministic and testing easier.

# Core Definition

Maps record in which order entries were created and honor that order when listing keys, values or entries. Two Maps with the same entries added in different orders will iterate in different orders. This has two benefits: Maps can be used when insertion order matters, and results become more deterministic and easier to check in testing.

# Prerequisites

- **map-data-structure** -- order is a property of Maps

# Key Properties

1. Entries listed in insertion order
2. Keys listed in insertion order
3. Values listed in insertion order
4. Order is deterministic (aids testing)
5. In principle, Map entries are unordered -- ordering is for determinism

# Construction / Recognition

```js
const map1 = new Map([['a', 1], ['b', 2]]);
// keys: 'a', 'b'
const map2 = new Map([['b', 2], ['a', 1]]);
// keys: 'b', 'a' -- different order
```

# Context & Application

Insertion order matters for reproducible output, testing, and any use case where entry sequence is significant.

# Examples

```js
const map1 = new Map([['a', 1], ['b', 2]]);
for (const key of map1.keys()) console.log(key);
// 'a', 'b'

const map2 = new Map([['b', 2], ['a', 1]]);
for (const key of map2.keys()) console.log(key);
// 'b', 'a'
```

(Chapter 36, Section 36.2.2, lines 239-283)

# Relationships

## Builds Upon
- **map-data-structure** -- property of Maps

## Enables
- Deterministic iteration and testing

## Related
- **set-data-structure** -- Sets also preserve insertion order

## Contrasts With
- None

# Common Errors

- **Error**: Assuming Map iteration order is alphabetical or random.
  **Correction**: Map iteration is always in insertion order.

# Common Confusions

- **Confusion**: Updating an existing key changes its position in the order.
  **Clarification**: Updating a key's value does not change its position. It remains at its original insertion position.

# Source Reference

Chapter 36: Maps (Map), Section 36.2.2, lines 239-283.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained
- Cross-reference status: verified
