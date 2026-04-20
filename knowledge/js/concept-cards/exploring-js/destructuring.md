---
concept: Destructuring
slug: destructuring
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.1 A first taste of destructuring"
extraction_confidence: high
aliases:
  - "destructuring assignment"
  - "pattern matching"
prerequisites: []
extends: []
related:
  - object-destructuring
  - array-destructuring
contrasts_with: []
answers_questions:
  - "What is destructuring?"
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Destructuring is an ES6 syntax that extracts multiple values from data at once using patterns that mirror the structure of the data (object literals for objects, array literals for arrays).

# Core Definition

With destructuring, we can extract multiple pieces of data at the same time via patterns in locations that receive data. Destructuring patterns are syntactically similar to the literals used for construction but appear where data is received (e.g., left-hand side of assignments), not where data is created. Destructuring is the opposite of construction: construction creates compound data; destructuring extracts data from it.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Introduced in ES2015 (ES6)
2. Two kinds: object-destructuring and Array-destructuring
3. Can be used in variable declarations, assignments, and parameter definitions
4. Patterns can be nested to arbitrary depth
5. Supports default values
6. Supports rest elements/properties

# Construction / Recognition

```js
// Array destructuring
const [x, y] = ['a', 'b'];

// Object destructuring
const {first, last} = {first: 'Jane', last: 'Doe'};
```

# Context & Application

Destructuring is used extensively for extracting function return values, processing API responses, importing specific properties, and swapping variables.

# Examples

```js
// Extracting from an array
const arr = ['a', 'b', 'c'];
const [x, y] = arr;
assert.equal(x, 'a');
assert.equal(y, 'b');

// Extracting from an object
const {first: f, last: l} = {first: 'Jane', last: 'Doe'};
assert.equal(f, 'Jane');
```

(Chapter 40, Section 40.1-40.2, lines 64-157)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **object-destructuring** -- specific pattern type
- **array-destructuring** -- specific pattern type
- **destructuring-default-values** -- defaults for missing matches

## Related
- **spread-syntax** -- rest in destructuring is the complement of spread

## Contrasts With
- None

# Common Errors

- **Error**: Destructuring a non-iterable with array pattern, or `undefined`/`null` with object pattern.
  **Correction**: Array destructuring requires an iterable. Object destructuring throws on `undefined`/`null`.

# Common Confusions

- **Confusion**: Destructuring modifies the source data.
  **Clarification**: Destructuring only reads from the source; it does not modify it.

# Source Reference

Chapter 40: Destructuring, Section 40.1-40.2, lines 64-157.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined as chapter introduction
- Cross-reference status: verified
