---
concept: Non-Destructive Prepending and Appending
slug: array-nondestructive-prepend-append
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.12.2 Non-destructively prepending and appending elements"
extraction_confidence: high
aliases: []
prerequisites:
  - array-creation
  - array-spreading
extends: []
related:
  - array-push-pop-shift-unshift
contrasts_with:
  - array-push-pop-shift-unshift
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Spread elements enable non-destructive prepending (`['x', ...arr]`) and appending (`[...arr, 'x']`) by creating a new Array with added elements while leaving the original unchanged.

# Core Definition

Spread elements in Array literals provide non-destructive prepending and appending. `['x', 'y', ...arr]` prepends elements; `[...arr, 'x', 'y']` appends elements. The original array is never modified. This is the functional/immutable alternative to `.unshift()` and `.push()`.

# Prerequisites

- **array-creation** -- creating new arrays
- **array-spreading** -- the spread mechanism

# Key Properties

1. `['x', ...arr]` -- prepend (non-destructive)
2. `[...arr, 'x']` -- append (non-destructive)
3. Original array is unchanged
4. Creates a new array each time

# Construction / Recognition

```js
const arr = ['a', 'b'];
const prepended = ['x', 'y', ...arr]; // ['x', 'y', 'a', 'b']
const appended = [...arr, 'x', 'y']; // ['a', 'b', 'x', 'y']
// arr is still ['a', 'b']
```

# Context & Application

Preferred in functional programming and React state updates where immutability is required.

# Examples

```js
const arr = ['a', 'b'];
assert.deepEqual(['x', ...arr], ['x', 'a', 'b']);
assert.deepEqual([...arr, 'x'], ['a', 'b', 'x']);
assert.deepEqual(arr, ['a', 'b']); // unchanged
```

(Chapter 34, Section 34.12.2, lines 1601-1640)

# Relationships

## Builds Upon
- **array-creation** -- creates new arrays
- **array-spreading** -- uses spread elements

## Enables
- Immutable array patterns

## Related
- **array-push-pop-shift-unshift** -- destructive equivalents

## Contrasts With
- **array-push-pop-shift-unshift** -- mutate original vs. create new

# Common Errors

- **Error**: Expecting spread prepending to modify the original array.
  **Correction**: Spreading always creates a new array. The original is unchanged.

# Common Confusions

- **Confusion**: Non-destructive operations are slower than destructive ones.
  **Clarification**: They do create new arrays (more allocations), but the performance difference is negligible for most use cases.

# Source Reference

Chapter 34: Arrays (Array), Section 34.12.2, lines 1601-1640.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
