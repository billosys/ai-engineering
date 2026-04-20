---
# === CORE IDENTIFICATION ===
concept: Return Value
slug: return-value

# === CLASSIFICATION ===
category: functions
subcategory: function-outputs
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Defining a function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - return statement
  - function return

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - expression
  - statement
extends: []
related:
  - parameters
  - side-effects
contrasts_with:
  - side-effects

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
---

# Quick Definition

A `return` statement determines the value a function produces. When control reaches a `return`, it immediately exits the function and gives the returned value to the calling code.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 102-108 of 03-functions.md): "A `return` statement determines the value the function returns. When control comes across such a statement, it immediately jumps out of the current function and gives the returned value to the code that called the function. A `return` keyword without an expression after it will cause the function to return `undefined`. Functions that don't have a `return` statement at all, such as `makeNoise`, similarly return `undefined`."

# Prerequisites

- **function-definition**: Return values are part of function behavior.
- **expression**: The expression after `return` is evaluated to produce the return value.
- **statement**: `return` is a statement within the function body.

# Key Properties

1. The `return` keyword immediately exits the current function.
2. The expression after `return` becomes the function's produced value.
3. `return` without an expression returns `undefined`.
4. Functions without any `return` statement also return `undefined`.
5. Functions that produce values can be used in expressions; those that don't are called for side effects.

# Construction / Recognition

## To Construct/Create:
```javascript
function square(x) {
  return x * x;
}
```

## To Identify/Recognize:
- The `return` keyword inside a function body, optionally followed by an expression.

# Context & Application

Return values allow functions to produce results that can be used in expressions, assigned to bindings, or passed to other functions. This is fundamental to composing complex operations from simpler ones.

# Examples

**Example 1** (Ch 3, lines 59-66 of 03-functions.md):
```javascript
const square = function(x) {
  return x * x;
};
console.log(square(12));
// → 144
```

**Example 2** (Ch 3, lines 82-88 of 03-functions.md) -- function without return value:
```javascript
const makeNoise = function() {
  console.log("Pling!");
};
makeNoise();
// → Pling!
```

# Relationships

## Builds Upon
- **function-definition** -- Return values are part of function definitions.
- **expression** -- The value to return is specified by an expression.

## Enables
- **closure** -- Returning functions from functions.
- **recursion** -- Recursive calls use return values from sub-calls.
- **higher-order-function** -- Functions can return other functions.

## Related
- **parameters** -- Parameters are inputs; return values are outputs.

## Contrasts With
- **side-effects** -- Functions either produce values via return or cause side effects (or both).

# Common Errors

- **Error**: Expecting a function with no `return` statement to produce a useful value.
  **Correction**: A function without `return` produces `undefined`.

# Common Confusions

- **Confusion**: Thinking `console.log` inside a function is a return value.
  **Clarification**: `console.log` is a side effect (printing to output). The return value is what follows the `return` keyword.

# Source Reference

Chapter 3: Functions, Section "Defining a function", lines 100-113 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 102-108)
- Confidence rationale: Explicit explanation of return behavior
- Cross-reference status: verified within chapter
