---
# === CORE IDENTIFICATION ===
concept: let Declaration
slug: let-declaration

# === CLASSIFICATION ===
category: variables-scope
subcategory: variable-declarations
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.1 let"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - let keyword
  - mutable variable

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-binding
  - block-scoping
  - temporal-dead-zone
contrasts_with:
  - const-declaration
  - var-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a variable in JavaScript and how do `let`, `const`, and `var` differ?"
  - "What distinguishes `let` from `const` from `var`?"
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

`let` declares a mutable, block-scoped variable that can be reassigned after declaration and optionally initialized at declaration time.

# Core Definition

"Variables declared via `let` are mutable" (Ch. 13, &sect;13.1). ^ES6^: `let` was introduced as one of JavaScript's main ways of declaring variables. It creates mutable bindings (the variable can be reassigned). Variables can be declared without initialization and assigned later, or declared and initialized in a single statement. `let` is block-scoped and subject to the temporal dead zone.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. ^ES6^: Introduced in ECMAScript 2015
2. Mutable: can be reassigned after declaration
3. Block-scoped: limited to the innermost enclosing block
4. Subject to temporal dead zone (TDZ)
5. Cannot be redeclared in the same scope
6. Does not create a global object property when in global scope

# Construction / Recognition

```js
let i;        // declare without initializing
i = 0;        // assign later
i = i + 1;    // reassign

let z = 3 * 5; // declare and initialize
```

# Context & Application

Use `let` when the value of a variable needs to change, such as loop counters, accumulators, or values that are conditionally assigned.

# Examples

From the source text (Ch. 13, &sect;13.1):
```js
let i;
i = 0;
i = i + 1;
assert.equal(i, 1);

// Declare and assign:
let i = 0;
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **block-scoping** -- let variables are block-scoped
- **temporal-dead-zone** -- let is subject to TDZ

## Related
- **variable-binding** -- let creates mutable bindings

## Contrasts With
- **const-declaration** -- const creates immutable bindings
- **var-declaration** -- var is function-scoped and hoisted differently

# Common Errors

- **Error**: Trying to access a `let` variable before its declaration.
  **Correction**: `let` variables are in the temporal dead zone until their declaration; accessing them earlier throws `ReferenceError`.

# Common Confusions

- **Confusion**: Thinking `let` and `var` are interchangeable.
  **Clarification**: `let` is block-scoped; `var` is function-scoped. `let` has TDZ; `var` is partially hoisted with `undefined`.

# Source Reference

Chapter 13: Variables and assignment, Section 13.1, lines 74-93.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified against Ch. 9 (&sect;9.1.1.6)
