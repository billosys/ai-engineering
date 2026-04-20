---
# === CORE IDENTIFICATION ===
concept: Function Definition
slug: function-definition

# === CLASSIFICATION ===
category: functions
subcategory: core-concepts
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
  - defining a function
  - function creation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - value
  - expression
extends: []
related:
  - function-expression
  - function-declaration
  - arrow-function
  - parameters
  - return-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
  - "How do I define and call a function?"
---

# Quick Definition

A function definition is a regular binding where the value of the binding is a function -- a piece of program wrapped in a value.

# Core Definition

As stated in "Eloquent JavaScript" (Ch 3, line 54 of 03-functions.md): "A function definition is a regular binding where the value of the binding is a function." Functions are "one of the most central tools in JavaScript programming. The concept of wrapping a piece of program in a value has many uses. It gives us a way to structure larger programs, to reduce repetition, to associate names with subprograms, and to isolate these subprograms from each other."

# Prerequisites

- **binding**: A function definition is a binding whose value is a function.
- **value**: Functions are values that can be stored, passed, and returned.
- **expression**: The `function` keyword creates a function value via an expression.

# Key Properties

1. A function is created with an expression that starts with the keyword `function`.
2. Functions have a set of **parameters** and a **body** containing statements.
3. The body must always be wrapped in braces (even for a single statement) when using `function` keyword syntax.
4. A function can have multiple parameters or no parameters at all.

# Construction / Recognition

## To Construct/Create:
```javascript
const square = function(x) {
  return x * x;
};
```

## To Identify/Recognize:
- The `function` keyword followed by a parameter list in parentheses and a body in braces.
- A binding assigned a function value.

# Context & Application

Function definitions are the primary means of structuring JavaScript programs. They enable code reuse, abstraction, and modularity. Every JavaScript program of any size relies heavily on function definitions.

# Examples

**Example 1** (Ch 3, lines 59-66 of 03-functions.md):
```javascript
const square = function(x) {
  return x * x;
};
console.log(square(12));
// → 144
```

**Example 2** (Ch 3, lines 82-97 of 03-functions.md):
```javascript
const makeNoise = function() {
  console.log("Pling!");
};
makeNoise();
// → Pling!

const roundTo = function(n, step) {
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
};
console.log(roundTo(23, 10));
// → 20
```

# Relationships

## Builds Upon
- **binding** -- A function definition stores a function value in a binding.
- **value** -- Functions are values in JavaScript.

## Enables
- **function-expression** -- One form of function definition.
- **function-declaration** -- Another form of function definition.
- **arrow-function** -- A concise form of function definition.
- **closure** -- Functions that reference outer scope bindings.
- **recursion** -- Functions that call themselves.
- **higher-order-function** -- Functions that operate on other functions.

## Related
- **parameters** -- Input to a function.
- **return-value** -- Output from a function.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Forgetting that a function expression assigned to a `const` binding requires a semicolon after the closing brace.
  **Correction**: `const f = function() { ... };` -- the semicolon terminates the statement, not the function.

# Common Confusions

- **Confusion**: Confusing the function with its name.
  **Clarification**: As stated in Ch 3: "A function binding usually simply acts as a name for a specific piece of the program... But the two are different." The function value and the binding holding it are separate things.

# Source Reference

Chapter 3: Functions, Section "Defining a function", lines 51-113 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from source, lines 54-56)
- Confidence rationale: Explicit definition provided in opening section
- Cross-reference status: verified within chapter
