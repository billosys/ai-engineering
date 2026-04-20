---
concept: For Loop
slug: for-loop
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.7 `for` loops"
extraction_confidence: high
aliases:
  - "C-style for loop"
  - "for statement"
prerequisites:
  - while-loop
extends: []
related:
  - for-of-loop
  - while-loop
contrasts_with:
  - for-of-loop
answers_questions:
  - "How do I loop a specific number of times in JavaScript?"
---

# Quick Definition

The `for` loop provides initialization, condition, and post-iteration expressions in its head, offering compact control over counted iteration.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, the `for` loop syntax is `for (initialization; condition; post_iteration) { statements }`. Each part of the head is optional. Variables declared via `let` or `const` in the initialization exist only inside the loop. Introduced in ES1.

# Prerequisites

- While loop (conceptual basis)

# Key Properties

1. Introduced in ES1.
2. Three-part head: initialization, condition, post-iteration (all optional).
3. Roughly equivalent to a `while` loop with initialization before and post-iteration at the end of the body.
4. Variables declared with `let`/`const` in initialization are scoped to the loop.
5. Omitting all three parts (`for (;;)`) creates an infinite loop.

# Construction / Recognition

```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

# Context & Application

Recommended for index-based iteration before ES6, or when a counter variable is needed. For iterating over collections, prefer `for-of`.

# Examples

From the source text (Ch. 25, section 25.7.1):

```js
const arr = ['a', 'b', 'c'];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

# Relationships

## Builds Upon
- **While Loop** -- `for` is syntactic sugar over `while` with structured initialization

## Contrasts With
- **For-Of Loop** -- `for-of` iterates over iterable values directly; `for` iterates via index

# Common Errors

- **Error**: Using `const` for the loop variable when it needs to be modified.
  **Correction**: Use `let` for loop counters in `for` loops since the variable is mutated.

# Common Confusions

- **Confusion**: Thinking `for` loops are the best way to iterate arrays.
  **Clarification**: `for-of` is preferred for iterating arrays and other iterables in modern JavaScript.

# Source Reference

Chapter 25: Control flow statements, Section 25.7, lines 606-683.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax and equivalence shown
- Cross-reference status: verified
