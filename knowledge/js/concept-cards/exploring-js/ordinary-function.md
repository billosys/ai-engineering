---
concept: Ordinary Function
slug: ordinary-function
category: functions
subcategory: function-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.2 Ordinary functions"
extraction_confidence: high
aliases:
  - "function declaration"
  - "function expression"
  - "traditional function"
prerequisites: []
extends: []
related:
  - arrow-function
  - function-declaration-vs-expression
contrasts_with:
  - arrow-function
  - specialized-function
answers_questions:
  - "What is a traditional function in JavaScript?"
  - "What distinguishes an arrow function from a traditional function?"
---

# Quick Definition

An ordinary function is a multi-purpose callable created via function declarations or (non-arrow) function expressions that can serve as a real function, method, or constructor.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, an ordinary function can play three roles: real function (invoked via function call), method (stored in a property, invoked via method call), or constructor function (invoked via `new`). It has its own `this` binding (set dynamically by how it is called) and supports early activation when created via function declarations.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. Can play three roles: real function, method, constructor.
2. Has its own dynamic `this` (set by how it's called).
3. Function declarations are activated early (hoisted).
4. Function expressions are not activated early.
5. In strict mode, `this` is `undefined` when function-called.

# Construction / Recognition

```js
// Function declaration
function add(x, y) {
  return x + y;
}

// Anonymous function expression
const add2 = function (x, y) {
  return x + y;
};

// Named function expression
const add3 = function myAdd(x, y) {
  return x + y;
};
```

# Context & Application

Still widely used for named stand-alone functions (declarations) where early activation is useful. For anonymous inline functions, arrow functions are preferred in modern JavaScript.

# Examples

From the source text (Ch. 27, section 27.2.4):

```js
function add(x, y) { return x + y; }

// As real function:
assert.equal(add(2, 1), 3);

// As method:
const obj = { addAsMethod: add };
assert.equal(obj.addAsMethod(2, 4), 6);

// As constructor:
const inst = new add();
assert.equal(inst instanceof add, true);
```

# Relationships

## Enables
- **Arrow Function** -- specialized alternative for the "real function" role
- **Class** -- specialized alternative for the "constructor" role

## Contrasts With
- **Arrow Function** -- arrow functions have lexical `this`; ordinary functions have dynamic `this`
- **Specialized Function** -- specialized functions are restricted to one role each

# Common Errors

- **Error**: Using an ordinary function as a callback inside a method, losing access to the method's `this`.
  **Correction**: Use an arrow function for callbacks inside methods.

# Common Confusions

- **Confusion**: Thinking function declarations and function expressions behave identically.
  **Clarification**: Function declarations are hoisted (activated early); function expressions are not.

# Source Reference

Chapter 27: Callable values, Section 27.2, lines 93-338.

# Verification Notes

- Definition source: direct
- Confidence rationale: Thorough coverage with role taxonomy
- Cross-reference status: verified
