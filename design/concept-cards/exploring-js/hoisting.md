---
# === CORE IDENTIFICATION ===
concept: Hoisting
slug: hoisting

# === CLASSIFICATION ===
category: variables-scope
subcategory: activation
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
  - variable hoisting
  - partial early activation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - var-declaration
  - variable-scope
extends: []
related:
  - early-activation
  - temporal-dead-zone
contrasts_with:
  - temporal-dead-zone

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `let` from `const` from `var`?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Hoisting is `var`'s partial early activation: the variable declaration is moved to the top of its function scope and initialized to `undefined`, while the assignment stays in place.

# Core Definition

`var` declarations are split into two parts at execution: "Declaration `var x`: The scope of a `var`-declared variable is the innermost surrounding function [...]. Such a variable is already active at the beginning of its scope and initialized with `undefined`. Assignment `x = 123`: The assignment is always executed in place." (Ch. 13, &sect;13.8.4). This partial early activation is called hoisting.

# Prerequisites

- **var-declaration** -- hoisting is a property of var
- **variable-scope** -- hoisting affects when variables are accessible

# Key Properties

1. Only applies to `var` (not `let`/`const`)
2. Declaration hoisted to top of function; initialized to `undefined`
3. Assignment remains at original location
4. No ReferenceError before declaration (unlike TDZ) -- just `undefined`
5. Function declarations are fully hoisted (both declaration and body)

# Construction / Recognition

```js
function f() {
  console.log(x); // undefined (hoisted, not ReferenceError)
  var x = 123;
  console.log(x); // 123 (assignment executed)
}
```

# Context & Application

Hoisting is a legacy concept that explains surprising `var` behavior. Modern `let`/`const` with TDZ replaced this pattern with more predictable behavior.

# Examples

From the source text (Ch. 13, &sect;13.8.4):
```js
function f() {
  // Partial early activation:
  assert.equal(x, undefined);  // hoisted
  if (true) {
    var x = 123;
    assert.equal(x, 123);    // assignment in place
  }
  assert.equal(x, 123);      // function-scoped
}
```

Equivalent interpretation:
```js
function f() {
  var x;  // declaration hoisted, x = undefined
  assert.equal(x, undefined);
  if (true) {
    x = 123;  // assignment in place
    assert.equal(x, 123);
  }
  assert.equal(x, 123);
}
```

# Relationships

## Builds Upon
- **var-declaration** -- hoisting is a var behavior
- **variable-scope** -- hoisting affects scope behavior

## Enables
- Understanding legacy JavaScript code

## Related
- **early-activation** -- full hoisting for function declarations

## Contrasts With
- **temporal-dead-zone** -- TDZ throws errors; hoisting gives undefined

# Common Errors

- **Error**: Expecting `var` to throw an error when accessed before declaration.
  **Correction**: `var` returns `undefined` before its assignment (hoisting), unlike `let`/`const` which throw ReferenceError (TDZ).

# Common Confusions

- **Confusion**: Thinking hoisting moves the entire statement to the top.
  **Clarification**: Only the declaration is hoisted (with `undefined`); the assignment stays in place.

# Source Reference

Chapter 13: Variables and assignment, Section 13.8.4, lines 1024-1060.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with step-by-step breakdown
- Cross-reference status: verified
