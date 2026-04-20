---
concept: Spreading into Array Literals
slug: array-spreading
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.3.5 Spreading into Array literals"
extraction_confidence: high
aliases:
  - "array spread"
  - "spread element in arrays"
prerequisites:
  - array-creation
  - iterable-interface
extends:
  - spread-syntax
related:
  - array-copying
contrasts_with: []
answers_questions:
  - "How do rest parameters and spread syntax relate to each other?"
---

# Quick Definition

A spread element (`...expr`) inside an Array literal evaluates the expression, iterates over it, and inserts each iterated value as an individual Array element, enabling concatenation, copying, and conversion of iterables.

# Core Definition

Inside an Array literal, a spread element consists of three dots (`...`) followed by an expression. It results in the expression being evaluated and then iterated over. Each iterated value becomes an additional Array element. Since spreading uses iteration, it only works if the value is iterable. Spreading is convenient for concatenating arrays and converting any iterable to an Array.

# Prerequisites

- **array-creation** -- spread is used within array literals
- **iterable-interface** -- the spread target must be iterable

# Key Properties

1. Introduced in ES2015 (ES6)
2. Only works with iterable values
3. Creates shallow copies
4. Can be used to concatenate arrays
5. Can convert any iterable to an array

# Construction / Recognition

```js
const iterable = ['b', 'c'];
['a', ...iterable, 'd']; // ['a', 'b', 'c', 'd']
[...arr]; // shallow copy
[...arr1, ...arr2]; // concatenation
```

# Context & Application

Array spreading is the idiomatic way to non-destructively combine arrays and convert iterables. It replaces `.concat()` in most cases.

# Examples

```js
const arr1 = ['a', 'b'];
const arr2 = ['c', 'd'];
const concatenated = [...arr1, ...arr2, 'e'];
// ['a', 'b', 'c', 'd', 'e']

[...'abc']; // ['a', 'b', 'c'] -- string is iterable
// [...123]; // TypeError: 123 is not iterable
```

(Chapter 34, Section 34.3.5, lines 586-647)

# Relationships

## Builds Upon
- **spread-syntax** -- array-specific application
- **iterable-interface** -- requires iterability

## Enables
- **array-copying** -- via `[...arr]`
- Non-destructive array operations

## Related
- **array-copying** -- one of five copying techniques

## Contrasts With
- None

# Common Errors

- **Error**: Spreading a non-iterable value like a number.
  **Correction**: Only iterables (arrays, strings, sets, etc.) can be spread.

# Common Confusions

- **Confusion**: Spreading creates a deep copy.
  **Clarification**: Spreading creates a shallow copy -- elements themselves are shared, not cloned.

# Source Reference

Chapter 34: Arrays (Array), Section 34.3.5, lines 586-647.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
