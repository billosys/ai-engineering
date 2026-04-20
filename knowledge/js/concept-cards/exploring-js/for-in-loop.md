---
concept: For-In Loop
slug: for-in-loop
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.10 `for-in` loops (avoid)"
extraction_confidence: high
aliases:
  - "for...in"
prerequisites:
  - for-loop
extends: []
related:
  - for-of-loop
contrasts_with:
  - for-of-loop
answers_questions:
  - "Why should I avoid `for-in` loops for arrays?"
---

# Quick Definition

The `for-in` loop visits all enumerable property keys (own and inherited) of an object. It is generally recommended to avoid, especially for arrays.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, `for-in` visits all own and inherited enumerable property keys of an object. When used with arrays, it visits property keys (strings, not numbers), includes non-element properties, and is therefore rarely a good choice. Introduced in ES1.

# Prerequisites

- For loop
- Object properties (conceptual)

# Key Properties

1. Introduced in ES1.
2. Iterates over property keys (strings), not values.
3. Includes inherited enumerable properties.
4. Array indices appear as strings, not numbers.
5. The author recommends avoiding `for-in` for arrays.

# Construction / Recognition

```js
for (const key in obj) {
  console.log(key);
}
```

# Context & Application

Historically used for iterating over object properties. In modern JavaScript, prefer `Object.keys()`, `Object.entries()`, or `for-of` with `Object.entries()`.

# Examples

From the source text (Ch. 25, section 25.10):

```js
const arr = ['a', 'b', 'c'];
arr.propKey = 'property value';
for (const key in arr) {
  console.log(key);
}
// Output: 0, 1, 2, propKey
```

# Relationships

## Contrasts With
- **For-Of Loop** -- `for-of` iterates values of iterables; `for-in` iterates property keys of objects

# Common Errors

- **Error**: Using `for-in` to iterate over an Array expecting values.
  **Correction**: Use `for-of` for array values or `for-of` with `.entries()` for index-value pairs.

# Common Confusions

- **Confusion**: `for-in` and `for-of` are interchangeable.
  **Clarification**: `for-in` iterates property keys (including inherited ones); `for-of` iterates iterable values. Don't use `for-in` for arrays.

# Source Reference

Chapter 25: Control flow statements, Section 25.10, lines 802-847.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with "avoid" recommendation
- Cross-reference status: verified
