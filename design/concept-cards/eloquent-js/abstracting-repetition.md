---
# === CORE IDENTIFICATION ===
concept: Abstracting Repetition
slug: abstracting-repetition

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: patterns
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Abstracting repetition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - abstracting over actions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - functions-as-values
  - abstraction
extends:
  - abstraction
related:
  - higher-order-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
  - "What must I know before understanding higher-order functions?"
---

# Quick Definition

Abstracting repetition means writing functions that take actions (function values) as parameters, allowing "doing something N times" or "doing something with each element" to become reusable patterns.

# Core Definition

As demonstrated in "Eloquent JavaScript" (Ch 5, lines 143-145 of 05-higher-order-functions.md): "Plain functions, as we've seen them so far, are a good way to build abstractions. But sometimes they fall short." The solution is to pass actions as function values (lines 173-175): "Since 'doing something' can be represented as a function and functions are just values, we can pass our action as a function value."

# Prerequisites

- **function-definition**: The abstraction is a function.
- **functions-as-values**: Actions are passed as function values.
- **abstraction**: This is a specific application of abstraction.

# Key Properties

1. Instead of hardcoding the action inside a loop, pass it as a parameter.
2. The calling code can provide any action (function value).
3. Function values can be created on the spot (inline arrow functions).
4. This is the conceptual bridge from functions to higher-order functions.

# Construction / Recognition

## To Construct/Create:
```javascript
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}
```

## To Identify/Recognize:
- A function that accepts another function as a parameter and calls it.

# Context & Application

This pattern is the gateway to understanding higher-order functions. It demonstrates that "doing something" can be represented as a value, which is the core insight of Chapter 5.

# Examples

**Example 1** (Ch 5, lines 177-188 of 05-higher-order-functions.md):
```javascript
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}
repeat(3, console.log);
// → 0
// → 1
// → 2
```

**Example 2** (Ch 5, lines 196-202) -- creating a function on the spot:
```javascript
let labels = [];
repeat(5, i => {
  labels.push(`Unit ${i + 1}`);
});
console.log(labels);
// → ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]
```

# Relationships

## Builds Upon
- **functions-as-values** -- Relies on passing functions as values.
- **abstraction** -- A specific form of abstraction.

## Enables
- **higher-order-function** -- This pattern IS a higher-order function.

## Related
- **array-foreach** -- The built-in version of this pattern for arrays.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Trying to pass a function call (`f()`) instead of the function itself (`f`).
  **Correction**: Pass the function reference, not its return value: `repeat(3, console.log)`, not `repeat(3, console.log())`.

# Common Confusions

- **Confusion**: You need a named function to pass as an argument.
  **Clarification**: You can create a function on the spot: `repeat(5, i => { labels.push(i); })`.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Abstracting repetition", lines 140-211 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: synthesized from lines 143-188
- Confidence rationale: Explicit section demonstrating the concept
- Cross-reference status: verified against higher-order functions section
