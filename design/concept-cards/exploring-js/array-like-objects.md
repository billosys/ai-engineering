---
concept: Array-Like Objects
slug: array-like-objects
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.5 Array-like objects"
extraction_confidence: high
aliases:
  - "ArrayLike"
prerequisites:
  - array-creation
extends: []
related:
  - array-from
contrasts_with:
  - iterable-interface
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

An Array-like object has a `.length` property and indexed elements (e.g., `[0]`, `[1]`), but is not an Array and typically lacks Array methods; `Array.from()` can convert it to a real Array.

# Core Definition

An Array-like value is an object with a `.length` property (holding the length) and numeric properties for elements (e.g., `[0]`). The TypeScript interface is `interface ArrayLike<T> { length: number; [n: number]: T; }`. Array-like objects used to be more common before ES6; now they are relatively rare in modern JavaScript.

# Prerequisites

- **array-creation** -- understanding what real arrays are

# Key Properties

1. Has `.length` property
2. Has numerically-indexed properties
3. Is not an actual Array
4. Lacks Array methods (`.map()`, `.filter()`, etc.)
5. `Array.from()` can convert Array-like objects to Arrays

# Construction / Recognition

```js
Array.from({}); // [] -- .length implicitly 0
Array.from({length: 2, 0: 'a', 1: 'b'}); // ['a', 'b']
```

# Context & Application

Array-like objects appear in older APIs (e.g., `arguments`, DOM collections). Modern code typically converts them to arrays via `Array.from()` or uses iterables instead.

# Examples

```js
const arrayLike = {length: 2, 0: 'a', 1: 'b'};
Array.from(arrayLike); // ['a', 'b']

// arguments is array-like
function f() { return Array.from(arguments); }
f('x', 'y'); // ['x', 'y']
```

(Chapter 34, Section 34.5, lines 804-857)

# Relationships

## Builds Upon
- **array-creation** -- contrasts with real arrays

## Enables
- Conversion to real arrays via Array.from()

## Related
- **array-from** -- the primary conversion method

## Contrasts With
- **iterable-interface** -- iterables use [Symbol.iterator](); array-like objects use .length and indices

# Common Errors

- **Error**: Calling `.map()` on a DOM NodeList directly.
  **Correction**: Convert first: `Array.from(nodeList).map(...)` or use iterator methods.

# Common Confusions

- **Confusion**: Array-like objects are iterables.
  **Clarification**: They are distinct concepts. Some objects are both (e.g., strings), but an object can be array-like without being iterable, or iterable without being array-like.

# Source Reference

Chapter 34: Arrays (Array), Section 34.5, lines 804-857.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with TypeScript interface
- Cross-reference status: verified
