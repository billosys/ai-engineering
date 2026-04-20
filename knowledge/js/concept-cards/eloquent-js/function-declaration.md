---
# === CORE IDENTIFICATION ===
concept: Function Declaration
slug: function-declaration

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
section: "Declaration notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - declaration notation
  - function statement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - function-definition
extends: []
related:
  - function-expression
  - arrow-function
  - hoisting
contrasts_with:
  - function-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
  - "What distinguishes a function declaration from a function expression?"
---

# Quick Definition

A function declaration is a statement that defines a binding and points it at a function, using the `function` keyword at the start of a statement. It is hoisted to the top of its scope.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 258-262 of 03-functions.md): "This is a function *declaration*. The statement defines the binding `square` and points it at the given function. It is slightly easier to write and doesn't require a semicolon after the function."

# Prerequisites

- **binding**: A function declaration creates a binding and assigns it a function value.
- **function-definition**: The general concept of creating functions.

# Key Properties

1. The `function` keyword is used at the **start of a statement**.
2. The function name is required (appears between `function` and the parameter list).
3. Does **not** require a semicolon after the closing brace.
4. Function declarations are **hoisted** -- they can be used before they appear in the code.

# Construction / Recognition

## To Construct/Create:
```javascript
function square(x) {
  return x * x;
}
```

## To Identify/Recognize:
- A statement beginning with the `function` keyword, followed by a name, parameters, and body.

# Context & Application

Function declarations are the most common way to define named functions in JavaScript. Because they are hoisted, they offer flexibility in code ordering -- you can call a function before its declaration appears in the source text.

# Examples

**Example 1** (Ch 3, lines 252-256 of 03-functions.md):
```javascript
function square(x) {
  return x * x;
}
```

**Example 2** (Ch 3, lines 268-274 of 03-functions.md) -- demonstrating hoisting:
```javascript
console.log("The future says:", future());

function future() {
  return "You'll never have flying cars";
}
```
"The preceding code works, even though the function is defined *below* the code that uses it."

**Example 3** (Ch 3, summary lines 936-939):
```javascript
// Declare g to be a function
function g(a, b) {
  return a * b * 3.5;
}
```

# Relationships

## Builds Upon
- **binding** -- Declarations create a named binding.

## Enables
- **hoisting** -- Declarations are moved conceptually to the top of their scope.
- **recursion** -- Named declarations make self-reference straightforward.

## Related
- **function-expression** -- An alternative syntax for creating functions.
- **arrow-function** -- Another alternative syntax.

## Contrasts With
- **function-expression** -- Expressions are not hoisted; declarations are. Expressions can be anonymous; declarations require a name.

# Common Errors

- **Error**: Adding a semicolon after a function declaration body.
  **Correction**: Unlike function expressions in assignment statements, declarations do not need a trailing semicolon.

# Common Confusions

- **Confusion**: Believing all `function` uses are equivalent.
  **Clarification**: When `function` is at the start of a statement, it creates a declaration (hoisted). In any other position, it creates an expression (not hoisted).

# Source Reference

Chapter 3: Functions, Section "Declaration notation", lines 245-284 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 258-262)
- Confidence rationale: Explicit definition with italicized term "declaration"
- Cross-reference status: verified against function-expression and summary
