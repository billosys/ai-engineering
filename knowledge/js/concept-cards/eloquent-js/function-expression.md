---
# === CORE IDENTIFICATION ===
concept: Function Expression
slug: function-expression

# === CLASSIFICATION ===
category: functions
subcategory: function-forms
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
  - anonymous function
  - function literal

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - expression
  - function-definition
extends: []
related:
  - function-declaration
  - arrow-function
contrasts_with:
  - function-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
  - "What distinguishes a function declaration from a function expression?"
---

# Quick Definition

A function expression creates a function value using the `function` keyword within an expression context, typically assigned to a binding.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 69-74 of 03-functions.md): "A function is created with an expression that starts with the keyword `function`. Functions have a set of *parameters* (in this case, only `x`) and a *body*, which contains the statements that are to be executed when the function is called." The chapter summary (line 925-927) clarifies: "The `function` keyword, when used as an expression, can create a function value."

# Prerequisites

- **binding**: Function expressions are typically assigned to bindings.
- **expression**: A function expression is an expression that produces a function value.
- **function-definition**: The general concept of creating functions.

# Key Properties

1. Uses the `function` keyword in an expression position (not at the start of a statement).
2. Produces a function value that can be assigned to a binding, passed as an argument, etc.
3. The body must always be wrapped in braces.
4. Requires a semicolon after the closing brace when used in an assignment statement.
5. Is **not** hoisted -- the binding is `undefined` until the expression is evaluated.

# Construction / Recognition

## To Construct/Create:
```javascript
const square = function(x) {
  return x * x;
};
```

## To Identify/Recognize:
- The `function` keyword appears in an expression context (e.g., right side of `=`).
- Often anonymous (no name between `function` and the parameter list).

# Context & Application

Function expressions are commonly used when assigning functions to variables, passing functions as arguments to other functions, or creating functions conditionally. They are one of three main ways to create functions in JavaScript (alongside declarations and arrow functions).

# Examples

**Example 1** (Ch 3, lines 59-66 of 03-functions.md):
```javascript
const square = function(x) {
  return x * x;
};
console.log(square(12));
// → 144
```

**Example 2** (Ch 3, lines 231-238 of 03-functions.md) -- reassigning a function binding:
```javascript
let launchMissiles = function() {
  missileSystem.launch("now");
};
if (safeMode) {
  launchMissiles = function() {/* do nothing */};
}
```

**Example 3** (Ch 3, summary lines 930-934):
```javascript
// Define f to hold a function value
const f = function(a) {
  console.log(a + 2);
};
```

# Relationships

## Builds Upon
- **binding** -- Function expressions are assigned to bindings.
- **expression** -- A function expression is a type of expression.

## Enables
- **closure** -- Function expressions that capture outer bindings.
- **higher-order-function** -- Passing function expressions as arguments.

## Related
- **function-declaration** -- An alternative syntax for creating functions.
- **arrow-function** -- A more concise function expression syntax.

## Contrasts With
- **function-declaration** -- Declarations are hoisted; expressions are not. Declarations use the `function` keyword at the start of a statement.

# Common Errors

- **Error**: Calling a function expression before it is defined in the code.
  **Correction**: Unlike declarations, function expressions are not hoisted. The binding must be assigned before the function is called.

# Common Confusions

- **Confusion**: Thinking function expressions and function declarations behave identically.
  **Clarification**: Function declarations are hoisted to the top of their scope and can be used before they appear in the code. Function expressions are evaluated when control reaches them.

# Source Reference

Chapter 3: Functions, Section "Defining a function", lines 51-113 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (synthesized from lines 69-74 and summary at 925-927)
- Confidence rationale: Explicit description of function keyword as expression
- Cross-reference status: verified against function-declaration and arrow-function sections
