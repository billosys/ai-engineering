---
concept: "Map .size vs Array .length"
slug: map-size
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.7.4 Why do Maps have a .size, while Arrays have a .length?"
extraction_confidence: high
aliases:
  - ".size"
prerequisites:
  - map-data-structure
  - array-length
extends: []
related: []
contrasts_with:
  - array-length
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Indexable sequences (Arrays, strings) use `.length` (highest index + 1), while unindexed collections (Maps, Sets) use `.size` (actual element count).

# Core Definition

In JavaScript, `.length` is based on indices and is always the highest index plus one. `.size` counts the number of elements in a collection. This distinction reflects the fundamental difference between indexed sequences and unindexed collections.

# Prerequisites

- **map-data-structure** -- Maps use .size
- **array-length** -- Arrays use .length

# Key Properties

1. `.length`: Array, String -- index-based
2. `.size`: Map, Set -- element count
3. `.length` can exceed actual elements (due to holes)
4. `.size` always reflects exact count

# Construction / Recognition

```js
new Map([['a', 1], ['b', 2]]).size; // 2
['a', 'b'].length; // 2
```

# Context & Application

This naming convention helps distinguish indexed sequences from collections in the JavaScript standard library.

# Examples

```js
const map = new Map().set('a', 1).set('b', 2);
assert.equal(map.size, 2);

const arr = ['a', 'b'];
assert.equal(arr.length, 2);
```

(Chapter 36, Section 36.7.4, lines 856-865)

# Relationships

## Builds Upon
- **map-data-structure** -- Maps use .size
- **array-length** -- Arrays use .length

## Enables
- Understanding API naming conventions

## Related
- None

## Contrasts With
- **array-length** -- index-based vs count-based

# Common Errors

- **Error**: Accessing `.length` on a Map.
  **Correction**: Maps use `.size`, not `.length`.

# Common Confusions

- **Confusion**: `.size` and `.length` mean the same thing.
  **Clarification**: `.length` = highest index + 1; `.size` = element count. They differ for sparse arrays.

# Source Reference

Chapter 36: Maps (Map), Section 36.7.4, lines 856-865.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained as FAQ
- Cross-reference status: verified
