---
concept: "Array .push(), .pop(), .shift(), .unshift()"
slug: array-push-pop-shift-unshift
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.12.1 Destructively adding and removing elements at either end"
extraction_confidence: high
aliases:
  - "push"
  - "pop"
  - "shift"
  - "unshift"
  - "stack methods"
  - "queue methods"
prerequisites:
  - array-creation
extends: []
related:
  - array-destructive-vs-nondestructive
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.push()` appends elements to the end, `.pop()` removes the last element, `.unshift()` prepends elements to the start, and `.shift()` removes the first element -- all mutating the array in place.

# Core Definition

JavaScript Arrays support four destructive methods for adding/removing at either end: `.push(...items)` appends at end, `.pop()` removes and returns last element, `.unshift(...items)` prepends at start, `.shift()` removes and returns first element. `.push()` is the most commonly used; `.shift()` is useful for consuming arrays queue-style. Using spread arguments (`...arr`) with `.push()` or `.unshift()` appends/prepends entire arrays.

# Prerequisites

- **array-creation** -- must have arrays

# Key Properties

1. All four are destructive (mutate the original array)
2. `.push()` and `.unshift()` accept multiple arguments
3. `.push()` / `.pop()` operate on the end (stack pattern)
4. `.shift()` / `.unshift()` operate on the beginning
5. `.push()` and `.unshift()` accept spread arguments

# Construction / Recognition

```js
const arr = ['a', 'b'];
arr.push('c');     // arr is ['a', 'b', 'c']
arr.pop();         // returns 'c', arr is ['a', 'b']
arr.unshift('x');  // arr is ['x', 'a', 'b']
arr.shift();       // returns 'x', arr is ['a', 'b']
```

# Context & Application

`.push()` is the most frequently used for building output arrays. `.shift()` consumes elements queue-style. For non-destructive prepending/appending, use spread: `['x', ...arr]` or `[...arr, 'x']`.

# Examples

```js
const arr = ['a', 'b'];
arr.push('x', 'y');
assert.deepEqual(arr, ['a', 'b', 'x', 'y']);

arr.push(...['z', 'w']); // spread to push array
assert.deepEqual(arr, ['a', 'b', 'x', 'y', 'z', 'w']);

assert.equal(arr.shift(), 'a');
assert.equal(arr.pop(), 'w');
```

(Chapter 34, Section 34.12.1, lines 1514-1599)

# Relationships

## Builds Upon
- **array-creation** -- array manipulation

## Enables
- Stack and queue patterns with arrays

## Related
- **array-destructive-vs-nondestructive** -- these are destructive methods

## Contrasts With
- None

# Common Errors

- **Error**: Using `.push()` expecting it to return the new array.
  **Correction**: `.push()` returns the new length, not the array. Use spreading for non-destructive appending.

# Common Confusions

- **Confusion**: `.unshift()` and `.push()` behave identically.
  **Clarification**: `.push()` adds to the end; `.unshift()` adds to the beginning.

# Source Reference

Chapter 34: Arrays (Array), Section 34.12.1, lines 1514-1599.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with mnemonic tips
- Cross-reference status: verified
