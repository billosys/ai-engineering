---
concept: Array Destructuring
slug: array-destructuring
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.5 Array-destructuring"
extraction_confidence: high
aliases:
  - "array pattern"
  - "iterable destructuring"
prerequisites:
  - destructuring
  - iterable-interface
extends: []
related:
  - object-destructuring
  - rest-elements
contrasts_with:
  - object-destructuring
answers_questions:
  - "What is destructuring?"
  - "How do I use destructuring to extract values from objects and arrays?"
  - "How does `for-of` relate to the iteration protocol?"
---

# Quick Definition

Array destructuring uses patterns that look like array literals (`[a, b]`) to extract values by position from any iterable (not just arrays), supporting holes to skip elements and rest elements to collect remaining values.

# Core Definition

Array-destructuring lets us batch-extract values of Array elements via patterns that look like Array literals. Crucially, it works with any iterable, not just Arrays -- Sets, Maps, strings, and generators can all be Array-destructured. Elements can be skipped by putting holes (commas) in the pattern. Uses the iteration protocol under the hood.

# Prerequisites

- **destructuring** -- the general concept
- **iterable-interface** -- Array destructuring uses iteration

# Key Properties

1. Introduced in ES2015 (ES6)
2. Works with any iterable (not just Arrays)
3. Matches by position (not key)
4. Skip elements with holes: `const [, x, y] = arr`
5. Supports rest elements: `const [x, ...rest] = arr`
6. Fails on non-iterable values (throws TypeError)

# Construction / Recognition

```js
const [x, y] = ['a', 'b'];
const [, second] = ['a', 'b', 'c']; // skip first
const [first, ...rest] = [1, 2, 3]; // rest element
```

# Context & Application

Array destructuring is used for extracting regex match groups, swapping variables, processing function return arrays, and iterating with `for (const [i, e] of arr.entries())`.

# Examples

```js
// Works with any iterable
const [a, b] = new Set(['fee', 'fi', 'fo']);
assert.equal(a, 'fee');

const [a2, b2] = 'hello';
assert.equal(a2, 'h');

// Swapping variables
let x = 'a', y = 'b';
[x, y] = [y, x];
assert.equal(x, 'b');

// Regex match groups
const [, year, month, day] =
  /^(\d{4})-(\d{2})-(\d{2})$/.exec('2999-12-31');
```

(Chapter 40, Section 40.5-40.6, lines 346-529)

# Relationships

## Builds Upon
- **destructuring** -- specific pattern type
- **iterable-interface** -- uses iteration protocol

## Enables
- **rest-elements** -- collecting remaining elements

## Related
- **object-destructuring** -- the other pattern type
- **for-of-loop** -- often combined with array destructuring

## Contrasts With
- **object-destructuring** -- array patterns match by position; object patterns match by key

# Common Errors

- **Error**: Array-destructuring a non-iterable value.
  **Correction**: `const [x] = 123` throws TypeError. The value must be iterable.

# Common Confusions

- **Confusion**: Array destructuring only works with Arrays.
  **Clarification**: It works with any iterable: Sets, Maps, strings, generators, etc.

# Source Reference

Chapter 40: Destructuring, Section 40.5, lines 346-420.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with iterable examples
- Cross-reference status: verified
