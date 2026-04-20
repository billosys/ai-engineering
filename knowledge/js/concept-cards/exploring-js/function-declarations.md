---
# === CORE IDENTIFICATION ===
concept: Function Declarations
slug: function-declarations

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
section: "9.1.1.7 Ordinary function declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - function statement
  - ordinary function declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statements
extends: []
related:
  - arrow-function-expressions
  - early-activation
  - ambiguous-syntax
contrasts_with:
  - arrow-function-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you declare a function in JavaScript?"
---

# Quick Definition

A function declaration uses the `function` keyword to create a named function that is hoisted (early-activated) and available throughout its containing scope.

# Core Definition

Function declarations are statements using the `function` keyword with a name, parameters, and body (Ch. 9, &sect;9.1.1.7). They are early-activated: "A function declaration is always executed when entering its scope, regardless of where it is located within that scope." (Ch. 13, &sect;13.8.2). In strict mode, function declarations are block-scoped.

# Prerequisites

- **statements** -- function declarations are statements

# Key Properties

1. Syntax: `function name(params) { body }`
2. Early-activated (hoisted): can be called before the declaration
3. Block-scoped in strict mode; function-scoped in sloppy mode
4. Creates a property on the global object when in global script scope
5. Allows duplicate declarations in the same scope

# Construction / Recognition

```js
function add1(a, b) {
  return a + b;
}
assert.equal(add1(5, 2), 7);
```

# Context & Application

Function declarations are one of two main ways to define functions (the other being arrow functions). They are preferred when hoisting is desired.

# Examples

From the source text (Ch. 9, &sect;9.1.1.7):
```js
function add1(a, b) {
  return a + b;
}
assert.equal(add1(5, 2), 7);
```

From Ch. 13, &sect;13.8.2 (early activation):
```js
assert.equal(funcDecl(), 123); // OK -- called before declaration
function funcDecl() { return 123; }
```

# Relationships

## Builds Upon
- **statements** -- function declarations are statements

## Enables
- **early-activation** -- function declarations are early-activated
- **closures** -- functions create closures

## Related
- **ambiguous-syntax** -- `function` at start of statement is always a declaration

## Contrasts With
- **arrow-function-expressions** -- not hoisted, different `this` binding

# Common Errors

- **Error**: Relying on early activation while accessing `const`/`let` variables before their declaration.
  **Correction**: Ensure all variables used in early-activated functions are also available.

# Common Confusions

- **Confusion**: Thinking function declarations and function expressions are the same.
  **Clarification**: Declarations are statements (hoisted); expressions are values assigned to variables (not hoisted).

# Source Reference

Chapter 9: Syntax, Section 9.1.1.7, lines 233-243. Chapter 13: Section 13.8.2, lines 886-985.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with examples in multiple sections
- Cross-reference status: verified across Ch. 9 and Ch. 13
