---
concept: Array Indices as Property Keys
slug: array-indices-as-property-keys
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.10.1 Array indices are (slightly special) property keys"
extraction_confidence: high
aliases:
  - "array indices"
  - "arrays as dictionaries"
prerequisites:
  - array-creation
extends: []
related:
  - array-holes
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Array elements are stored as properties with string keys; indices are string-valued property keys where `ToString(ToUint32(str)) === str`, meaning arrays are internally dictionaries from string indices to values.

# Core Definition

Array elements are (almost) normal properties. The bracket operator `[]` coerces any non-symbol value to a string, so `arr[0]` and `arr['0']` access the same element. A string is an index if converting it to a 32-bit unsigned integer and back produces the original string. Internally, engines optimize arrays as sequential storage but may switch to dictionary representation for sparse arrays.

# Prerequisites

- **array-creation** -- understanding arrays

# Key Properties

1. Array elements are properties with string keys
2. `arr[0]` and `arr['0']` are equivalent
3. Non-index properties can be added but are separate from elements
4. `.keys()` returns numeric indices; `Object.keys()` returns string keys (including non-index properties)
5. Engines optimize dense arrays internally

# Construction / Recognition

```js
const arr = ['a', 'b'];
arr.prop = 123;
Object.keys(arr); // ['0', '1', 'prop']
arr.keys().toArray(); // [0, 1] -- only indices
```

# Context & Application

This knowledge explains why `.length` is highest index + 1, why arrays can have non-element properties, and why holes exist.

# Examples

```js
const arr = ['a', 'b'];
arr.prop = 123;
assert.equal(arr[0], 'a');
assert.equal(arr['0'], 'a');
Object.keys(arr); // ['0', '1', 'prop']
```

(Chapter 34, Section 34.10.1, lines 1186-1271)

# Relationships

## Builds Upon
- **array-creation** -- internal mechanism

## Enables
- Understanding array holes and length behavior

## Related
- **array-holes** -- possible because arrays are dictionaries

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `arr[0]` uses a numeric key.
  **Correction**: The bracket operator converts `0` to `'0'` (a string) before property access.

# Common Confusions

- **Confusion**: Arrays only have element properties.
  **Clarification**: Arrays can have arbitrary non-index properties (e.g., `arr.prop`), which are ignored by `.keys()`, `.map()`, etc.

# Source Reference

Chapter 34: Arrays (Array), Section 34.10.1, lines 1186-1271.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with specification reference
- Cross-reference status: verified
