---
concept: Arrow Function
slug: arrow-function
category: functions
subcategory: function-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.3.2 Arrow functions"
extraction_confidence: high
aliases:
  - "fat arrow function"
  - "lambda"
  - "=>"
prerequisites:
  - ordinary-function
extends: []
related:
  - this-keyword
  - specialized-function
contrasts_with:
  - ordinary-function
answers_questions:
  - "What is an arrow function?"
  - "What distinguishes an arrow function from a traditional function?"
---

# Quick Definition

An arrow function is a specialized function (ES6) designed solely for the "real function" role, with concise syntax and lexical `this` binding that makes it ideal for callbacks and inline functions.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, arrow functions were added for two reasons: more concise syntax and lexical `this`. Unlike ordinary functions, arrow functions do not have their own `this`; they treat `this` like any other variable and access it from the surrounding scope. Arrow functions cannot be used as constructors (no `new`) and cannot be methods (no dynamic `this`). Introduced in ES6.

# Prerequisites

- Ordinary function (to understand what arrow functions replace)

# Key Properties

1. Introduced in ES6.
2. Lexical `this` -- accesses `this` from the enclosing scope.
3. Cannot be used as constructors (no `new`).
4. Cannot serve as methods (no dynamic `this`).
5. Concise syntax: expression body (`=> expr`) or block body (`=> { ... }`).
6. Single parameter without destructuring can omit parentheses: `x => x`.
7. Always expressions (never declarations).

# Construction / Recognition

```js
// Block body
const f = (x, y) => { return x + y; };

// Expression body
const g = (x, y) => x + y;

// Single parameter
const id = x => x;
```

# Context & Application

Preferred for anonymous inline functions (callbacks, `.map()`, `.filter()`, etc.) and any function inside a method that needs access to the method's `this`. Use function declarations for named stand-alone functions when early activation is needed.

# Examples

From the source text (Ch. 27, section 27.3.2.1):

```js
const f = (x, y, z) => 123;

// Single parameter
const id = x => x;

// Concise callbacks
[1, 2, 3].map(x => x + 1); // [2, 3, 4]
```

Syntax pitfall -- returning object literals:

```js
const func1 = () => ({a: 1}); // correct
const func2 = () => {a: 1};   // wrong: block with label
```

# Relationships

## Builds Upon
- **Ordinary Function** -- arrow function is a specialized replacement

## Enables
- **Lexical This** -- solves `this`-shadowing problems in callbacks

## Contrasts With
- **Ordinary Function** -- ordinary functions have dynamic `this`; arrow functions have lexical `this`

# Common Errors

- **Error**: Trying to use an arrow function as a constructor with `new`.
  **Correction**: Arrow functions cannot be constructors. Use classes or ordinary functions.

- **Error**: Returning an object literal without parentheses: `() => {a: 1}`.
  **Correction**: Wrap in parentheses: `() => ({a: 1})`.

# Common Confusions

- **Confusion**: Thinking arrow functions are just shorter ordinary functions.
  **Clarification**: The key difference is `this` binding: arrow functions have lexical `this`, ordinary functions have dynamic `this`. This fundamentally affects their use in methods and callbacks.

# Source Reference

Chapter 27: Callable values, Section 27.3.2, lines 531-631.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with two stated design reasons
- Cross-reference status: verified with Ch. 30 (this keyword)
