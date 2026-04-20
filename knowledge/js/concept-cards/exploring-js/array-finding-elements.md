---
concept: Array Finding Methods
slug: array-finding-elements
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.1.2 The most commonly used Array methods"
extraction_confidence: high
aliases:
  - ".find()"
  - ".findIndex()"
  - ".findLast()"
  - ".findLastIndex()"
  - ".includes()"
  - ".indexOf()"
prerequisites:
  - array-creation
extends: []
related:
  - array-filter
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Arrays provide multiple search methods: `.includes()` checks membership, `.indexOf()`/`.lastIndexOf()` find by value equality, and `.find()`/`.findIndex()`/`.findLast()`/`.findLastIndex()` find by predicate callback.

# Core Definition

Array search methods: `.includes(value)` returns boolean; `.indexOf(value)`/`.lastIndexOf(value)` return the first/last index (or -1); `.find(callback)` returns the first matching element (or undefined); `.findIndex(callback)` returns its index (or -1); `.findLast()` and `.findLastIndex()` search from the end.

# Prerequisites

- **array-creation** -- operates on arrays

# Key Properties

1. `.includes()` -- boolean membership test
2. `.indexOf()` / `.lastIndexOf()` -- index by value equality
3. `.find()` / `.findLast()` -- element by predicate
4. `.findIndex()` / `.findLastIndex()` -- index by predicate
5. `.find()` returns `undefined` if not found; `.findIndex()` returns `-1`

# Construction / Recognition

```js
['a', 'b', 'c'].includes('b'); // true
['a', 'b', 'c'].indexOf('b'); // 1
['a', 'bb', 'ccc'].find(s => s.length >= 2); // 'bb'
['a', 'bb', 'ccc'].findIndex(s => s.length >= 2); // 1
```

# Context & Application

Use `.includes()` for simple membership checks. Use `.find()` when you need the element itself. Use `.findIndex()` when you need the position for later operations.

# Examples

```js
['■', '●', '■'].includes('■'); // true
['■', '●', '■'].indexOf('■');  // 0
['■', '●', '■'].lastIndexOf('■'); // 2
['●', '', '▲'].find(x => x.length > 0); // '●'
['●', '', '▲'].findLast(x => x.length > 0); // '▲'
```

(Chapter 34, Section 34.1.2, lines 301-319)

# Relationships

## Builds Upon
- **array-creation** -- searching within arrays

## Enables
- Element lookup patterns

## Related
- **array-filter** -- returns all matches vs. first match

## Contrasts With
- None

# Common Errors

- **Error**: Using `.indexOf()` to check membership and comparing with `0` instead of `-1`.
  **Correction**: `.indexOf()` returns `-1` for not found, not `0`. Use `.includes()` for boolean checks.

# Common Confusions

- **Confusion**: `.find()` and `.filter()` serve the same purpose.
  **Clarification**: `.find()` returns the first matching element; `.filter()` returns all matching elements in an array.

# Source Reference

Chapter 34: Arrays (Array), Section 34.1.2, lines 301-319.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
