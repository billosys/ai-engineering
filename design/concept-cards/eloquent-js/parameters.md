---
# === CORE IDENTIFICATION ===
concept: Parameters
slug: parameters

# === CLASSIFICATION ===
category: functions
subcategory: function-inputs
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
  - function parameters
  - arguments

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - function-definition
extends: []
related:
  - return-value
  - default-parameters
  - rest-parameters
  - optional-arguments
  - scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
---

# Quick Definition

Parameters are bindings listed in a function's definition whose initial values are provided by the caller of the function.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 70-74 of 03-functions.md): "Functions have a set of *parameters* (in this case, only `x`) and a *body*, which contains the statements that are to be executed when the function is called." Further (lines 111-113): "Parameters to a function behave like regular bindings, but their initial values are given by the *caller* of the function, not the code in the function itself."

# Prerequisites

- **binding**: Parameters behave like regular bindings within the function body.
- **function-definition**: Parameters are part of a function's definition.

# Key Properties

1. Parameters are listed in parentheses after the `function` keyword (or before `=>` in arrow functions).
2. They behave like local bindings within the function body.
3. Their values are supplied by the caller at invocation time.
4. A function can have **zero or more** parameters.
5. Each function call creates **new instances** of parameter bindings.

# Construction / Recognition

## To Construct/Create:
```javascript
function roundTo(n, step) {
  // n and step are parameters
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
}
```

## To Identify/Recognize:
- Names listed between parentheses in a function definition.

# Context & Application

Parameters are the primary mechanism for passing data into functions. They enable functions to be general-purpose by accepting different inputs for each call.

# Examples

**Example 1** (Ch 3, lines 59-66 of 03-functions.md) -- single parameter:
```javascript
const square = function(x) {
  return x * x;
};
```

**Example 2** (Ch 3, lines 82-97 of 03-functions.md) -- zero and two parameters:
```javascript
const makeNoise = function() {
  console.log("Pling!");
};

const roundTo = function(n, step) {
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
};
```

# Relationships

## Builds Upon
- **binding** -- Parameters are a special kind of binding.

## Enables
- **default-parameters** -- Parameters can have default values.
- **rest-parameters** -- A parameter that collects extra arguments.
- **optional-arguments** -- JavaScript's flexible argument handling.

## Related
- **return-value** -- Parameters are inputs; return values are outputs.
- **scope** -- Parameters are local to the function.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming missing parameters cause an error.
  **Correction**: In JavaScript, missing parameters are assigned `undefined`, not an error.

# Common Confusions

- **Confusion**: Parameters and arguments are the same thing.
  **Clarification**: Parameters are the names listed in the function definition; arguments are the actual values passed when calling the function.

# Source Reference

Chapter 3: Functions, Section "Defining a function", lines 70-113 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 70-74 and 111-113)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
