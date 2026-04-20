---
# === CORE IDENTIFICATION ===
concept: Arrow Function Expressions
slug: arrow-function-expressions

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: basic-syntax
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.1.1.8 Arrow function expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - arrow functions
  - fat arrow functions
  - "=>"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expressions
extends: []
related:
  - function-declarations
  - closures
contrasts_with:
  - function-declarations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are arrow functions and how do they differ from regular functions?"
---

# Quick Definition

Arrow function expressions are a concise function syntax using `=>`, especially suited for callbacks. They have two body forms: block body with explicit `return`, and expression body with implicit return.

# Core Definition

"Arrow function expressions are used especially as arguments of function calls and method calls." (Ch. 9, &sect;9.1.1.8). ^ES6^: Arrow functions have two forms: block body `(a, b) => { return a + b }` with explicit return, and expression body `(a, b) => a + b` with implicit return. Their syntax was influenced by CoffeeScript (Ch. 4, &sect;4.1).

# Prerequisites

- **expressions** -- arrow functions are expressions

# Key Properties

1. ^ES6^: Introduced in ECMAScript 2015
2. Two body forms: block body (`{ return ... }`) and expression body (`=> expr`)
3. Expression body has implicit return
4. Commonly used as callbacks and method arguments
5. Not early-activated (unlike function declarations)
6. Syntax from CoffeeScript influence

# Construction / Recognition

```js
// Block body
const add2 = (a, b) => { return a + b };

// Expression body (implicit return)
const add3 = (a, b) => a + b;

// As callback
arr.map(x => x * 2);
```

# Context & Application

Arrow functions are the preferred syntax for callbacks, array methods, and short functions. They are not hoisted and must be declared before use.

# Examples

From the source text (Ch. 9, &sect;9.1.1.8):
```js
const add2 = (a, b) => { return a + b };
assert.equal(add2(5, 2), 7);

// Equivalent, expression body:
const add3 = (a, b) => a + b;
```

# Relationships

## Builds Upon
- **expressions** -- arrow functions are expressions

## Enables
- **closures** -- arrow functions create closures
- Concise callback patterns

## Related
- **function-declarations** -- the other main function syntax

## Contrasts With
- **function-declarations** -- arrow functions are not hoisted and have no `this` binding

# Common Errors

- **Error**: Returning an object literal without parentheses: `() => {a: 1}`.
  **Correction**: Wrap in parentheses: `() => ({a: 1})`. Without them, `{}` is a code block.

# Common Confusions

- **Confusion**: Thinking arrow functions and regular functions are interchangeable.
  **Clarification**: Arrow functions don't have their own `this`, `arguments`, or `super`. They inherit `this` from their enclosing scope.

# Source Reference

Chapter 9: Syntax, Section 9.1.1.8, lines 245-271.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with both forms shown
- Cross-reference status: verified
