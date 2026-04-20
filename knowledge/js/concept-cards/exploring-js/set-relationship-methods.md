---
concept: Set Relationship Methods (ES2025)
slug: set-relationship-methods
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.3 Checking Set relationships"
extraction_confidence: high
aliases:
  - "set.isSubsetOf()"
  - "set.isSupersetOf()"
  - "set.isDisjointFrom()"
prerequisites:
  - set-data-structure
extends: []
related:
  - set-operations
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

ES2025 adds three boolean Set relationship methods: `.isSubsetOf(other)` checks if all elements are in other, `.isSupersetOf(other)` checks if all of other's elements are in this, and `.isDisjointFrom(other)` checks if the sets share no elements.

# Core Definition

Three methods for checking relationships between Sets: `.isSubsetOf(other)` returns true if all elements of `this` are in `other`; `.isSupersetOf(other)` returns true if `this` contains all elements of `other`; `.isDisjointFrom(other)` returns true if `this` and `other` have no elements in common. All accept Set-like objects.

# Prerequisites

- **set-data-structure** -- operates on Sets

# Key Properties

1. Introduced in ES2025
2. All return booleans
3. Accept Set-like objects as parameters
4. `.isSubsetOf()` -- all mine are in other
5. `.isSupersetOf()` -- all of other's are in mine
6. `.isDisjointFrom()` -- no overlap

# Construction / Recognition

```js
new Set(['a', 'b']).isSubsetOf(new Set(['a', 'b', 'c'])); // true
new Set(['a', 'b', 'c']).isSupersetOf(new Set(['a', 'b'])); // true
new Set(['a', 'b']).isDisjointFrom(new Set(['x'])); // true
```

# Context & Application

These methods enable declarative Set relationship checks without manual iteration, useful in authorization, tagging, and filtering systems.

# Examples

```js
const required = new Set(['read', 'write']);
const permissions = new Set(['read', 'write', 'admin']);
required.isSubsetOf(permissions); // true -- user has all required permissions
```

(Chapter 38, Section 38.3, lines 265-321)

# Relationships

## Builds Upon
- **set-data-structure** -- checking relationships between Sets

## Enables
- Declarative permission/role checking

## Related
- **set-operations** -- combining Sets vs. checking relationships

## Contrasts With
- None

# Common Errors

- **Error**: Confusing `.isSubsetOf()` and `.isSupersetOf()` direction.
  **Correction**: `A.isSubsetOf(B)` means A is contained in B. `A.isSupersetOf(B)` means A contains B.

# Common Confusions

- **Confusion**: `.isDisjointFrom()` means they are equal.
  **Clarification**: Disjoint means no shared elements at all, not equality.

# Source Reference

Chapter 38: Sets (Set), Section 38.3, lines 265-321.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2025 markers
- Cross-reference status: verified
