---
concept: "Array .every() and .some()"
slug: array-every-some
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.13 Array methods that accept element callbacks"
extraction_confidence: high
aliases:
  - ".every()"
  - ".some()"
  - "Array.prototype.every"
  - "Array.prototype.some"
prerequisites:
  - array-creation
  - array-element-callbacks
extends: []
related:
  - array-filter
  - array-finding-elements
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.every(callback)` returns `true` if the callback returns `true` for every element (universal quantifier), while `.some(callback)` returns `true` if the callback returns `true` for at least one element (existential quantifier).

# Core Definition

`.every()` and `.some()` are summary methods that test whether elements satisfy a predicate. `.every()` short-circuits to `false` on the first failing element; `.some()` short-circuits to `true` on the first passing element. Both are useful for validation and condition checking.

# Prerequisites

- **array-creation** -- operates on arrays
- **array-element-callbacks** -- uses the standard callback pattern

# Key Properties

1. `.every()` -- true if all pass (AND logic)
2. `.some()` -- true if any pass (OR logic)
3. Both short-circuit for efficiency
4. Callback receives (value, index, array)
5. Empty array: `.every()` returns true; `.some()` returns false

# Construction / Recognition

```js
[1, 2, 3].every(x => x > 0); // true
[1, 2, 3].some(x => x > 2);  // true
```

# Context & Application

Use `.every()` for validation (are all inputs valid?) and `.some()` for existence checks (does any element match?).

# Examples

```js
[1, 2, 3].every(x => x > 0); // true
[1, -2, 3].every(x => x > 0); // false

[1, 2, 3].some(x => x === 2); // true
[1, 2, 3].some(x => x === 5); // false

// Edge cases
[].every(x => false); // true (vacuous truth)
[].some(x => true);   // false
```

(Chapter 34, Section 34.13, lines 1642-1702)

# Relationships

## Builds Upon
- **array-creation** -- operates on arrays
- **array-element-callbacks** -- callback pattern

## Enables
- Array validation and condition checking

## Related
- **array-filter** -- `.filter()` returns matching elements; `.some()`/`.every()` return booleans
- **array-finding-elements** -- `.find()` returns first match; `.some()` returns boolean

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `.every()` on an empty array to return `false`.
  **Correction**: `.every()` on an empty array returns `true` (vacuous truth).

# Common Confusions

- **Confusion**: `.every()` and `.some()` visit all elements.
  **Clarification**: Both short-circuit: `.every()` stops at the first `false`; `.some()` stops at the first `true`.

# Source Reference

Chapter 34: Arrays (Array), Section 34.13, lines 1642-1702.

# Verification Notes

- Definition source: direct
- Confidence rationale: Mentioned in callback methods list
- Cross-reference status: verified
