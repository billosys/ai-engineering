---
# === CORE IDENTIFICATION ===
concept: const and Loops
slug: const-and-loops

# === CLASSIFICATION ===
category: variables-scope
subcategory: variable-declarations
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.2.2 const and loops"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - const-declaration
  - block-scoping
extends:
  - const-declaration
related:
  - let-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

`const` can be used in `for-of` and `for-in` loops because each iteration creates a fresh binding. Plain `for` loops with changing counters require `let`.

# Core Definition

"We can use `const` with `for-of` loops, where a fresh binding is created for each iteration." (Ch. 13, &sect;13.2.2). In `for-of` loops, each iteration gets a new `const` binding initialized to the current element. In plain `for` loops, the counter variable must use `let` because it is reassigned each iteration.

# Prerequisites

- **const-declaration** -- understanding const's immutable binding
- **block-scoping** -- each iteration creates a new block scope

# Key Properties

1. `for-of` with `const`: fresh binding per iteration (OK)
2. `for-in` with `const`: fresh binding per iteration (OK)
3. Plain `for` with counter: must use `let` (counter changes)
4. Inside loop body, `const` can be used for iteration-local variables

# Construction / Recognition

```js
// const OK in for-of:
for (const elem of ['hello', 'world']) {
  console.log(elem);
}

// let needed in for:
for (let i = 0; i < arr.length; i++) {
  const elem = arr[i]; // const OK here
}
```

# Context & Application

This pattern is very common in JavaScript. Using `const` in `for-of` is the idiomatic approach.

# Examples

From the source text (Ch. 13, &sect;13.2.2):
```js
const arr = ['hello', 'world'];
for (const elem of arr) {
  console.log(elem);
}

// Plain for needs let:
for (let i = 0; i < arr.length; i++) {
  const elem = arr[i];
  console.log(elem);
}
```

# Relationships

## Builds Upon
- **const-declaration** -- understanding what const allows
- **block-scoping** -- each iteration = new scope

## Enables
- Idiomatic loop patterns in modern JavaScript

## Related
- **let-declaration** -- required for `for` loop counters

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `const` for a `for` loop counter: `for (const i = 0; ...)`.
  **Correction**: The counter is reassigned; use `let i = 0`.

# Common Confusions

- **Confusion**: Thinking `const` can't be used in any loop.
  **Clarification**: `const` works perfectly in `for-of` and `for-in` because each iteration creates a fresh binding.

# Source Reference

Chapter 13: Variables and assignment, Section 13.2.2, lines 141-169.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with both loop types demonstrated
- Cross-reference status: verified
