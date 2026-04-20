---
concept: Spread Syntax
slug: spread-syntax
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.3.4 Iterating via iteration-based language constructs"
extraction_confidence: high
aliases:
  - "spread element"
  - "spread operator"
  - "..."
prerequisites:
  - iterable-interface
extends: []
related:
  - for-of-loop
  - array-destructuring
  - rest-elements
contrasts_with:
  - rest-elements
answers_questions:
  - "How do rest parameters and spread syntax relate to each other?"
---

# Quick Definition

Spread syntax (`...`) expands any iterable into individual elements within Array literals or function call arguments, using the iteration protocol internally.

# Core Definition

Inside an Array literal, a spread element consists of three dots (`...`) followed by an expression. The expression is evaluated and then iterated over, with each iterated value becoming an additional Array element. Spreading uses the iteration protocol, so it only works with iterable values.

# Prerequisites

- **iterable-interface** -- spread relies on iteration

# Key Properties

1. Introduced in ES2015 (ES6)
2. Works in Array literals: `[...iterable]`
3. Works in function calls: `func(...iterable)`
4. Only works with iterable values (throws TypeError for non-iterables)
5. Creates shallow copies when spreading into a new Array

# Construction / Recognition

```js
const iterable = ['b', 'c'];
['a', ...iterable, 'd']; // ['a', 'b', 'c', 'd']

// In function calls
func('a', ...iterable, 'd');
```

# Context & Application

Spread is used for copying arrays, concatenating iterables, converting iterables to arrays, and passing iterable elements as individual function arguments. It provides a concise, non-destructive way to combine data.

# Examples

```js
// Concatenating arrays
const arr1 = ['a', 'b'];
const arr2 = ['c', 'd'];
const concatenated = [...arr1, ...arr2, 'e'];
// ['a', 'b', 'c', 'd', 'e']

// Converting Set to Array
const set = new Set(['x', 'y']);
[...set]; // ['x', 'y']

// Copying an Array
const copy = [...arr1];

// Non-iterable values throw
// [...123] // TypeError: 123 is not iterable
```

(Chapter 32, Section 32.3.4-32.3.5, lines 313-371; Chapter 34, Section 34.3.5, lines 586-647)

# Relationships

## Builds Upon
- **iterable-interface** -- spread requires iterability

## Enables
- Non-destructive array concatenation
- Converting any iterable to an Array

## Related
- **for-of-loop** -- another iteration consumer
- **array-destructuring** -- also consumes iterables

## Contrasts With
- **rest-elements** -- rest collects into an array; spread expands from an iterable

# Common Errors

- **Error**: Spreading a non-iterable value like a number or plain object.
  **Correction**: Only iterable values (arrays, strings, sets, etc.) can be spread.

# Common Confusions

- **Confusion**: Spread and rest are the same operator.
  **Clarification**: Spread (`...x` in array literals/function calls) expands values; rest (`...x` in patterns/parameters) collects values. They use the same syntax but serve opposite purposes.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.3.4, lines 313-322; Chapter 34, Section 34.3.5, lines 586-647.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined and demonstrated across multiple chapters
- Cross-reference status: verified
