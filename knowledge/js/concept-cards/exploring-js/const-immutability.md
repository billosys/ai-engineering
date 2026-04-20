---
# === CORE IDENTIFICATION ===
concept: const and Immutability
slug: const-immutability

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
section: "13.2.1 const and immutability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - immutable binding vs immutable value

# === TYPED RELATIONSHIPS ===
prerequisites:
  - const-declaration
  - variable-binding
extends:
  - const-declaration
related:
  - primitives-are-immutable
  - objects-are-mutable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a variable in JavaScript and how do `let`, `const`, and `var` differ?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

`const` makes the variable *binding* immutable (the variable can't be reassigned), but the *value* itself may be mutable -- object properties can still be changed.

# Core Definition

"In JavaScript, `const` only means that the *binding* (the association between variable name and variable value) is immutable. The value itself may be mutable, like `obj` in the following example." (Ch. 13, &sect;13.2.1). Changing properties of a const object is allowed; reassigning the const variable is not.

# Prerequisites

- **const-declaration** -- the declaration this concept extends
- **variable-binding** -- understanding bindings vs values

# Key Properties

1. `const` = immutable binding, not immutable value
2. Object properties can be changed via const reference
3. Reassigning the variable throws TypeError
4. To make an object truly immutable, use `Object.freeze()`

# Construction / Recognition

```js
const obj = { prop: 0 };

obj.prop = obj.prop + 1; // Allowed!
assert.equal(obj.prop, 1);

// obj = {};  // TypeError: Assignment to constant variable.
```

# Context & Application

This distinction is one of the most important nuances for JavaScript beginners. It explains why `const` is recommended even for objects -- it prevents accidental reassignment while still allowing mutation.

# Examples

From the source text (Ch. 13, &sect;13.2.1):
```js
const obj = { prop: 0 };

// Allowed: changing properties of `obj`
obj.prop = obj.prop + 1;
assert.equal(obj.prop, 1);

// Not allowed: assigning to `obj`
assert.throws(
  () => { obj = {} },
  { name: 'TypeError', message: 'Assignment to constant variable.' }
);
```

# Relationships

## Builds Upon
- **const-declaration** -- this explains what const actually guarantees
- **variable-binding** -- binding vs value distinction

## Enables
- Correct mental model of const behavior

## Related
- **primitives-are-immutable** -- primitives are always immutable regardless of const
- **objects-are-mutable** -- objects remain mutable even with const

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting `const arr = [1,2,3]` to prevent `arr.push(4)`.
  **Correction**: `const` prevents `arr = [...]`; it doesn't prevent `arr.push()`, `arr[0] = ...`, etc.

# Common Confusions

- **Confusion**: Thinking `const` means the value cannot change at all.
  **Clarification**: `const` prevents reassignment of the variable; the value's own properties can still change.

# Source Reference

Chapter 13: Variables and assignment, Section 13.2.1, lines 115-139.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with demonstration code
- Cross-reference status: verified
