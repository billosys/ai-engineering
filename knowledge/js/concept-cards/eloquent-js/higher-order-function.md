---
# === CORE IDENTIFICATION ===
concept: Higher-Order Function
slug: higher-order-function

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: core-concepts
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Higher-order functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - higher-order functions
  - HOF

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - closure
  - arrow-function
  - abstraction
extends:
  - function-definition
related:
  - array-filter
  - array-map
  - array-reduce
  - array-foreach
  - composability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
  - "What must I know before understanding higher-order functions?"
---

# Quick Definition

Higher-order functions are functions that operate on other functions, either by taking them as arguments or by returning them.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 5, lines 216-222 of 05-higher-order-functions.md): "Functions that operate on other functions, either by taking them as arguments or by returning them, are called *higher-order functions*. Since we have already seen that functions are regular values, there is nothing particularly remarkable about the fact that such functions exist. The term comes from mathematics, where the distinction between functions and other values is taken more seriously."

Further (lines 225-226): "Higher-order functions allow us to abstract over *actions*, not just values."

# Prerequisites

- **function-definition**: Higher-order functions are functions that work with other functions.
- **closure**: Many higher-order functions create closures.
- **arrow-function**: Arrow functions are commonly used with higher-order functions.
- **abstraction**: Higher-order functions are a form of abstraction.

# Key Properties

1. Take functions as **arguments** (e.g., `repeat(3, console.log)`).
2. **Return** new functions (e.g., `greaterThan(10)` returns `m => m > 10`).
3. Can **change** other functions (e.g., `noisy(Math.min)` wraps with logging).
4. Can provide new types of **control flow** (e.g., `unless`, `forEach`).
5. Allow abstracting over **actions**, not just values.

# Construction / Recognition

## To Construct/Create:
```javascript
// Taking a function as argument:
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

// Returning a function:
function greaterThan(n) {
  return m => m > n;
}
```

## To Identify/Recognize:
- A function that accepts function arguments or returns a function.

# Context & Application

Higher-order functions are central to functional programming in JavaScript. The built-in array methods `forEach`, `filter`, `map`, `reduce`, `some`, `every`, and `find` are all higher-order functions. They allow writing code as a pipeline of data transformations.

# Examples

**Example 1** (Ch 5, lines 229-236 of 05-higher-order-functions.md) -- returning a function:
```javascript
function greaterThan(n) {
  return m => m > n;
}
let greaterThan10 = greaterThan(10);
console.log(greaterThan10(11));
// → true
```

**Example 2** (Ch 5, lines 243-254) -- wrapping a function:
```javascript
function noisy(f) {
  return (...args) => {
    console.log("calling with", args);
    let result = f(...args);
    console.log("called with", args, ", returned", result);
    return result;
  };
}
noisy(Math.min)(3, 2, 1);
// → calling with [3, 2, 1]
// → called with [3, 2, 1] , returned 1
```

**Example 3** (Ch 5, lines 260-272) -- new control flow:
```javascript
function unless(test, then) {
  if (!test) then();
}
repeat(3, n => {
  unless(n % 2 == 1, () => {
    console.log(n, "is even");
  });
});
// → 0 is even
// → 2 is even
```

# Relationships

## Builds Upon
- **function-definition** -- Higher-order functions are functions.
- **closure** -- Returned functions often close over parameters.
- **abstraction** -- Higher-order functions are a powerful form of abstraction.

## Enables
- **array-filter**, **array-map**, **array-reduce** -- Standard higher-order array methods.
- **composability** -- Combining operations into pipelines.

## Related
- **array-foreach** -- A higher-order method for iteration.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Calling the function argument instead of passing it: `repeat(3, console.log())`.
  **Correction**: Pass the function itself: `repeat(3, console.log)`.

# Common Confusions

- **Confusion**: Higher-order functions are inherently complex.
  **Clarification**: "Since we have already seen that functions are regular values, there is nothing particularly remarkable about the fact that such functions exist."

# Source Reference

Chapter 5: Higher-Order Functions, Section "Higher-order functions", lines 213-283 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 216-222)
- Confidence rationale: Explicit definition with italicized term "higher-order functions"
- Cross-reference status: verified against array method sections
