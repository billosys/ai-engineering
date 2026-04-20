---
# === CORE IDENTIFICATION ===
concept: var Declaration
slug: var-declaration

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
section: "13.8.4 var: hoisting (partial early activation)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - var keyword

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
extends: []
related:
  - hoisting
  - global-object
contrasts_with:
  - let-declaration
  - const-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a variable in JavaScript and how do `let`, `const`, and `var` differ?"
  - "What distinguishes `let` from `const` from `var`?"
---

# Quick Definition

`var` is a legacy variable declaration that is function-scoped (not block-scoped), partially hoisted (initialized to `undefined` at scope start), and creates global object properties in global scope. Modern code should use `let`/`const` instead.

# Core Definition

"`var` is an older way of declaring variables that predates `const` and `let` (which are preferred now)." (Ch. 13, &sect;13.8.4). A `var` declaration has two parts: the declaration (scope is the innermost surrounding *function*, not block; active from scope start with value `undefined`) and the assignment (executed in place). `var` allows duplicate declarations and creates global object properties.

# Prerequisites

- **variable-scope** -- var uses function scope, not block scope

# Key Properties

1. Function-scoped (not block-scoped)
2. Hoisted: declaration moves to top of function, initialized to `undefined`
3. Assignment remains in place
4. Allows duplicate declarations in the same scope
5. Creates global object properties in global scope
6. No temporal dead zone (accessible before declaration, but undefined)
7. Considered legacy; use `let`/`const` instead

# Construction / Recognition

```js
function f() {
  assert.equal(x, undefined);  // hoisted, initialized to undefined
  if (true) {
    var x = 123;               // assignment in place
    assert.equal(x, 123);
  }
  assert.equal(x, 123);       // function-scoped, not block-scoped
}
```

# Context & Application

`var` appears in legacy code and some older patterns. Understanding it is necessary for reading and maintaining older JavaScript codebases.

# Examples

From the source text (Ch. 13, &sect;13.8.4):
```js
function f() {
  // Partial early activation:
  assert.equal(x, undefined);
  if (true) {
    var x = 123;
    // The assignment is executed in place:
    assert.equal(x, 123);
  }
  // Scope is function, not block:
  assert.equal(x, 123);
}
```

# Relationships

## Builds Upon
- **variable-scope** -- var has different scoping rules

## Enables
- **hoisting** -- var demonstrates partial early activation

## Related
- **global-object** -- var creates global object properties

## Contrasts With
- **let-declaration** -- block-scoped, TDZ, no hoisting to undefined
- **const-declaration** -- block-scoped, immutable, TDZ

# Common Errors

- **Error**: Expecting `var` to be block-scoped like `let`.
  **Correction**: `var` is function-scoped; the variable leaks out of blocks.

# Common Confusions

- **Confusion**: Thinking `var` creates a variable at the point of declaration.
  **Clarification**: The variable exists from the start of the function (with value `undefined`); only the assignment happens at the declaration point.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8.4, lines 1024-1060.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with clear demonstration of both hoisting and function scoping
- Cross-reference status: verified against declarations table in &sect;13.8
