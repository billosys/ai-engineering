---
concept: Rest Elements in Destructuring
slug: rest-elements
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.5.2 Rest elements"
extraction_confidence: high
aliases:
  - "rest element"
  - "...rest in destructuring"
prerequisites:
  - array-destructuring
extends: []
related:
  - rest-properties
  - spread-syntax
contrasts_with:
  - spread-syntax
answers_questions:
  - "How do rest parameters and spread syntax relate to each other?"
---

# Quick Definition

A rest element (`...variable`) in an Array destructuring pattern collects all remaining elements into a new Array, and must appear last in the pattern.

# Core Definition

In Array patterns, rest elements (which must come last) collect all remaining, unmatched elements into a new Array. The syntax `[x, y, ...remaining]` assigns the first two elements to `x` and `y`, and all subsequent elements to `remaining` as an Array.

# Prerequisites

- **array-destructuring** -- rest elements are used in array patterns

# Key Properties

1. Introduced in ES2015 (ES6)
2. Must be last in the pattern
3. Collects remaining elements into an Array
4. Complement of spread syntax (spread expands; rest collects)

# Construction / Recognition

```js
const [x, y, ...remaining] = ['a', 'b', 'c', 'd'];
// x === 'a', y === 'b', remaining === ['c', 'd']
```

# Context & Application

Rest elements are used when you need the first few elements individually and the remainder as a group, common in recursive algorithms and head/tail processing.

# Examples

```js
const [x, y, ...remaining] = ['a', 'b', 'c', 'd'];
assert.equal(x, 'a');
assert.equal(y, 'b');
assert.deepEqual(remaining, ['c', 'd']);
```

(Chapter 40, Section 40.5.2, lines 402-420)

# Relationships

## Builds Upon
- **array-destructuring** -- used within array patterns

## Enables
- Head/tail processing patterns

## Related
- **rest-properties** -- object equivalent
- **spread-syntax** -- opposite operation

## Contrasts With
- **spread-syntax** -- spread expands; rest collects

# Common Errors

- **Error**: Placing a rest element in the middle of a pattern.
  **Correction**: Rest elements must be last: `[...rest, last]` is a syntax error.

# Common Confusions

- **Confusion**: Rest and spread are the same.
  **Clarification**: Rest (`...x` in patterns) collects; spread (`...x` in literals/calls) expands. Same syntax, opposite operations.

# Source Reference

Chapter 40: Destructuring, Section 40.5.2, lines 402-420.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
