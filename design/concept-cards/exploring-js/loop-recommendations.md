---
concept: Loop Recommendations
slug: loop-recommendations
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.11 Recommendations for looping"
extraction_confidence: high
aliases: []
prerequisites:
  - for-of-loop
  - for-loop
  - for-in-loop
  - for-await-of-loop
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Which loop should I use in JavaScript?"
---

# Quick Definition

The recommended loop hierarchy is: `for-await-of` for async iterables, `for-of` for sync iterables (including arrays), `.forEach()` for arrays (ES5+), plain `for` for pre-ES5, and never `for-in` for arrays.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, the recommendations are: use `for-await-of` for async iterables (ES2018+), `for-of` for synchronous iterables including arrays (ES6+), `.forEach()` for arrays (ES5+), plain `for` for pre-ES5 code, and never use `for-in` to loop over arrays.

# Prerequisites

- For-of loop
- For loop
- For-in loop
- For-await-of loop

# Key Properties

1. `for-await-of` for async iterables.
2. `for-of` for any sync iterable (recommended default).
3. `.forEach()` for ES5+ arrays.
4. `for` for index-based or pre-ES5 iteration.
5. Never `for-in` for arrays.

# Construction / Recognition

```js
for (const item of collection) { /* preferred */ }
```

# Context & Application

Follow these guidelines to write clear, correct, and idiomatic JavaScript loops.

# Examples

From the source text (Ch. 25, section 25.11):

```js
// Best for most cases (ES6+)
for (const elem of arr) { /* ... */ }
```

# Relationships

## Related
- All loop types in Chapter 25

# Source Reference

Chapter 25: Control flow statements, Section 25.11, lines 837-847.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit ranked recommendations
- Cross-reference status: verified
