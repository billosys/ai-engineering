---
concept: Destructuring Multiple Return Values
slug: destructuring-multiple-return-values
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.6.3 Object-destructuring: multiple return values"
extraction_confidence: high
aliases:
  - "multiple return values"
prerequisites:
  - object-destructuring
  - array-destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Destructuring enables functions to effectively return multiple values by returning an object or array, which the caller destructures to extract individual named or positional values.

# Core Definition

Destructuring is very useful if a function returns multiple values packaged as an object or array. Using object destructuring, the caller can extract only the values they need, in any order, using property names. Using array destructuring, values are extracted by position. Object return values are preferred when the caller might only need some values.

# Prerequisites

- **object-destructuring** -- extracting named return values
- **array-destructuring** -- extracting positional return values

# Key Properties

1. Function returns an object or array with multiple values
2. Caller destructures to extract what's needed
3. Object return values: order-independent, selectively extractable
4. Array return values: position-dependent (e.g., regex `.exec()`)

# Construction / Recognition

```js
function findElement(arr, predicate) {
  for (let index = 0; index < arr.length; index++) {
    const value = arr[index];
    if (predicate(value)) return {value, index};
  }
  return {value: undefined, index: -1};
}

const {value, index} = findElement([7, 8, 6], x => x % 2 === 0);
```

# Context & Application

This pattern is ubiquitous in modern JavaScript: React's `useState()`, regex match results, iterator results, and any function needing to return compound data.

# Examples

```js
const arr = [7, 8, 6];
const {value, index} = findElement(arr, x => x % 2 === 0);
assert.equal(value, 8);
assert.equal(index, 1);

// Extract only what you need
const {value: v} = findElement(arr, x => x % 2 === 0);
const {index: i} = findElement(arr, x => x % 2 === 0);
```

(Chapter 40, Section 40.6.3, lines 457-529)

# Relationships

## Builds Upon
- **object-destructuring** -- for named values
- **array-destructuring** -- for positional values

## Enables
- Clean multi-value function APIs

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Destructuring array return values by name.
  **Correction**: Array destructuring is positional: `const [a, b] = func()`, not `const {a, b}`.

# Common Confusions

- **Confusion**: Object and array return patterns are interchangeable.
  **Clarification**: Object returns allow selective extraction by name; array returns require knowing the position.

# Source Reference

Chapter 40: Destructuring, Section 40.6.3, lines 457-529.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with findElement example
- Cross-reference status: verified
