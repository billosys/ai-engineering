---
concept: Set Operations (ES2025)
slug: set-operations
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.2 Combining Sets: union, intersection, difference, symmetric difference"
extraction_confidence: high
aliases:
  - "set.union()"
  - "set.intersection()"
  - "set.difference()"
  - "set.symmetricDifference()"
prerequisites:
  - set-data-structure
extends: []
related:
  - set-relationship-methods
  - set-like-objects
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

ES2025 adds four Set combination methods: `.union(other)`, `.intersection(other)`, `.difference(other)`, and `.symmetricDifference(other)`, all returning new Sets and accepting Set-like objects as parameters.

# Core Definition

ES2025 introduces four methods for combining Sets: `.union(other)` returns elements in either set; `.intersection(other)` returns elements in both; `.difference(other)` returns elements only in `this`; `.symmetricDifference(other)` returns elements in one but not both. All return new Sets (non-destructive) and accept Set-like objects, not just Sets.

# Prerequisites

- **set-data-structure** -- operates on Sets

# Key Properties

1. Introduced in ES2025
2. All return new Sets (non-destructive)
3. Accept Set-like objects (not just Sets)
4. `.union()` -- elements in either
5. `.intersection()` -- elements in both
6. `.difference()` -- elements only in this
7. `.symmetricDifference()` -- elements in one but not both

# Construction / Recognition

```js
new Set(['a', 'b']).union(new Set(['b', 'c']));
// Set {'a', 'b', 'c'}

new Set(['a', 'b']).intersection(new Set(['b', 'c']));
// Set {'b'}

new Set(['a', 'b']).difference(new Set(['b', 'c']));
// Set {'a'}

new Set(['a', 'b']).symmetricDifference(new Set(['b', 'c']));
// Set {'a', 'c'}
```

# Context & Application

These methods eliminate the need for manual Set operations using spread and filter, making Set algebra concise and readable.

# Examples

```js
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

a.union(b);                // Set {1, 2, 3, 4}
a.intersection(b);         // Set {2, 3}
a.difference(b);           // Set {1}
a.symmetricDifference(b);  // Set {1, 4}
```

(Chapter 38, Section 38.2, lines 160-263)

# Relationships

## Builds Upon
- **set-data-structure** -- operates on Sets

## Enables
- Set algebra (mathematical set operations)

## Related
- **set-relationship-methods** -- subset, superset, disjoint checks
- **set-like-objects** -- parameters can be Set-like

## Contrasts With
- None

# Common Errors

- **Error**: Expecting Set operations to mutate the original Set.
  **Correction**: All four methods return new Sets; the original is unchanged.

# Common Confusions

- **Confusion**: `.symmetricDifference()` is the same as `.difference()`.
  **Clarification**: `.difference(other)` is one-directional (only in `this`). `.symmetricDifference()` is bidirectional (in one but not both).

# Source Reference

Chapter 38: Sets (Set), Section 38.2, lines 160-263.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2025 markers and diagrams
- Cross-reference status: verified
