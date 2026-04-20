---
# === CORE IDENTIFICATION ===
concept: Composability
slug: composability

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: design-principles
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Composability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - function composition
  - pipeline

# === TYPED RELATIONSHIPS ===
prerequisites:
  - higher-order-function
  - array-filter
  - array-map
  - array-reduce
extends:
  - abstraction
related:
  - pure-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
---

# Quick Definition

Composability is the ability to combine simple higher-order operations (filter, map, reduce) into readable pipelines that express complex computations as a series of transformations.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 528-531 of 05-higher-order-functions.md): "The abstractions these functions provide really shine when you need to *compose* operations. As an example, let's write code that finds the average year of origin for living and dead scripts in the dataset."

# Prerequisites

- **higher-order-function**: Composability builds on higher-order functions.
- **array-filter**, **array-map**, **array-reduce**: The primary composable operations.

# Key Properties

1. Operations chain together: `array.filter(...).map(...).reduce(...)`.
2. Each step produces a new value that feeds into the next.
3. Code reads as a **pipeline**: start with data, apply transformations.
4. More readable but potentially less efficient than manual loops (creates intermediate arrays).

# Construction / Recognition

## To Construct/Create:
```javascript
function average(array) {
  return array.reduce((a, b) => a + b) / array.length;
}
Math.round(average(
  SCRIPTS.filter(s => s.living).map(s => s.year)));
```

## To Identify/Recognize:
- Chained method calls: `.filter(...).map(...).reduce(...)`.
- A sequence of transformations on data.

# Context & Application

Composability is the key benefit of higher-order functions. It allows complex data processing to be expressed as a readable pipeline, where each step is a simple, understandable operation.

# Examples

**Example 1** (Ch 5, lines 533-544 of 05-higher-order-functions.md):
```javascript
function average(array) {
  return array.reduce((a, b) => a + b) / array.length;
}
console.log(Math.round(average(
  SCRIPTS.filter(s => s.living).map(s => s.year))));
// → 1165
console.log(Math.round(average(
  SCRIPTS.filter(s => !s.living).map(s => s.year))));
// → 204
```
"You can see it as a pipeline: we start with all scripts, filter out the living (or dead) ones, take the years from those, average them, and round the result."

**Contrast** (Ch 5, lines 559-569) -- the equivalent loop:
```javascript
let total = 0, count = 0;
for (let script of SCRIPTS) {
  if (script.living) {
    total += script.year;
    count += 1;
  }
}
console.log(Math.round(total / count));
```
"However, it is harder to see what was being computed and how."

# Relationships

## Builds Upon
- **higher-order-function** -- Composability depends on higher-order functions.
- **array-filter**, **array-map**, **array-reduce** -- The composable building blocks.

## Enables
- Readable, declarative data processing.
- Separation of concerns (each step does one thing).

## Related
- **pure-function** -- Pure functions compose more reliably.
- **abstraction** -- Composability is a consequence of good abstractions.

## Contrasts With
- None within this source (implicitly contrasts with imperative loop style).

# Common Errors

- **Error**: Overusing composition to the point of poor performance with huge arrays.
  **Correction**: "If you're processing huge arrays and doing so many times, the less abstract style might be worth the extra speed." Profile before optimizing.

# Common Confusions

- **Confusion**: Composed pipelines are always better than loops.
  **Clarification**: Both approaches have merits. Pipelines are more readable; loops can be more efficient. "You can usually afford the readable approach."

# Source Reference

Chapter 5: Higher-Order Functions, Section "Composability", lines 503-584 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 528-531)
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified against filter, map, reduce sections
