---
# === CORE IDENTIFICATION ===
concept: const Declaration
slug: const-declaration

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
section: "13.2 const"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - const keyword
  - constant
  - immutable variable

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-binding
  - const-immutability
  - block-scoping
  - temporal-dead-zone
contrasts_with:
  - let-declaration
  - var-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a variable in JavaScript and how do `let`, `const`, and `var` differ?"
  - "What distinguishes `let` from `const` from `var`?"
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

`const` declares an immutable, block-scoped variable binding that must be initialized at declaration and cannot be reassigned, though the value itself may be mutable.

# Core Definition

"Variables declared via `const` are immutable. We must always initialize immediately." (Ch. 13, &sect;13.2). ^ES6^: `const` creates immutable bindings -- the association between variable name and value cannot change. However, "the value itself may be mutable" (Ch. 9, &sect;9.1.1.6). Attempting reassignment throws `TypeError: Assignment to constant variable.`

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. ^ES6^: Introduced in ECMAScript 2015
2. Immutable binding: cannot be reassigned after initialization
3. Must be initialized at declaration
4. Block-scoped: limited to innermost enclosing block
5. Subject to temporal dead zone (TDZ)
6. The value itself may be mutable (objects can be modified)
7. Recommended as the default declaration; use `let` only when needed

# Construction / Recognition

```js
const i = 0; // must initialize

// TypeError: Assignment to constant variable.
// i = i + 1;

// But object properties CAN be changed:
const obj = { prop: 0 };
obj.prop = 1; // OK!
```

# Context & Application

`const` is the recommended default for all variable declarations. Use `let` only when reassignment is needed.

# Examples

From the source text (Ch. 13, &sect;13.2):
```js
const i = 0; // must initialize
assert.throws(
  () => { i = i + 1 },
  { name: 'TypeError', message: 'Assignment to constant variable.' }
);
```

Using `const` with `for-of` (fresh binding per iteration):
```js
const arr = ['hello', 'world'];
for (const elem of arr) {
  console.log(elem);
}
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **const-immutability** -- understanding what const does and doesn't guarantee
- **block-scoping** -- const variables are block-scoped

## Related
- **variable-binding** -- const creates immutable bindings
- **temporal-dead-zone** -- const is subject to TDZ

## Contrasts With
- **let-declaration** -- let creates mutable bindings
- **var-declaration** -- var is function-scoped and partially hoisted

# Common Errors

- **Error**: Trying to use `const` without initializing: `const x;`
  **Correction**: `const` must be initialized at declaration: `const x = value;`

- **Error**: Thinking `const` makes the value immutable.
  **Correction**: `const` makes the *binding* immutable. Object properties can still be changed.

# Common Confusions

- **Confusion**: Thinking `const` prevents all modifications to objects.
  **Clarification**: `const obj = {a: 1}; obj.a = 2;` is legal. Only `obj = ...` would fail.

# Source Reference

Chapter 13: Variables and assignment, Section 13.2, lines 95-169.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with immutability nuance explained
- Cross-reference status: verified against Ch. 9 (&sect;9.1.1.6)
