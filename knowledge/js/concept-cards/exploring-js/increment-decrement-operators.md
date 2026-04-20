---
# === CORE IDENTIFICATION ===
concept: Increment and Decrement Operators
slug: increment-decrement-operators

# === CLASSIFICATION ===
category: primitive-types
subcategory: numbers
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Numbers"
chapter_number: 18
pdf_page: null
section: "Incrementing (++) and decrementing (--)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "++"
  - "--"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The increment (`++`) and decrement (`--`) operators destructively add or subtract 1 from their operand. Prefix versions (`++v`, `--v`) return the new value; suffix versions (`v++`, `v--`) return the old value.

# Core Definition

The increment operator `++` adds one to its operand and the decrement operator `--` subtracts one. Both exist in prefix and suffix forms. Prefix (`++v`) changes then returns the new value. Suffix (`v++`) returns the old value then changes. They can be applied to variables, object properties, and array elements (Ch. 18, Section 18.3.3).

# Prerequisites

- **number-type** -- operates on numbers

# Key Properties

1. Prefix `++v`: increment, return new value (ES1)
2. Suffix `v++`: return old value, increment (ES1)
3. Prefix `--v`: decrement, return new value (ES1)
4. Suffix `v--`: return old value, decrement (ES1)
5. Works on variables, properties, array elements

# Construction / Recognition

```js
let foo = 3;
assert.equal(++foo, 4); // prefix: returns new
assert.equal(foo, 4);

let bar = 3;
assert.equal(bar++, 3); // suffix: returns old
assert.equal(bar, 4);
```

# Context & Application

Common in loops and counters. Suffix form is more common but prefix is slightly more predictable.

# Examples

From the source text:

```js
let foo = 3;
assert.equal(++foo, 4);  // prefix increment
assert.equal(foo, 4);

let bar = 3;
assert.equal(bar--, 3);  // suffix decrement
assert.equal(bar, 2);

// Works on properties
const obj = { a: 1 };
++obj.a;
assert.equal(obj.a, 2);

// Works on array elements
const arr = [ 4 ];
arr[0]++;
assert.deepEqual(arr, [5]);
```

# Relationships

## Builds Upon
- **number-type** — operates on numbers

## Enables
- Loop counters and iteration

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Confusing prefix and suffix return values
  **Correction**: Prefix returns the new value; suffix returns the old value.

# Common Confusions

- **Confusion**: Thinking `++` only works on variables
  **Clarification**: It works on any assignable storage location: variables, properties, array elements.

# Source Reference

Chapter 18: Numbers, Section 18.3.3, lines 590-776.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete table of all four forms
- Cross-reference status: verified
