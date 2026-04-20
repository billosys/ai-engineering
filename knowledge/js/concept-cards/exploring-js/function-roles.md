---
concept: Function Roles
slug: function-roles
category: functions
subcategory: function-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.2.4 Roles played by ordinary functions"
extraction_confidence: high
aliases:
  - "real function"
  - "method role"
  - "constructor role"
prerequisites:
  - ordinary-function
extends: []
related:
  - specialized-function
contrasts_with: []
answers_questions:
  - "What roles can functions play in JavaScript?"
---

# Quick Definition

In JavaScript, functions can play three roles: real function (invoked via function call), method (invoked via method call on an object), or constructor (invoked via `new`).

# Core Definition

As described in "Exploring JavaScript" Ch. 27, an ordinary function can play three roles: real function (standalone call), method (called as a property of an object, receiving the object as `this`), and constructor function (called with `new`). Specialized functions (ES6) are restricted to one role each: arrow functions are real functions, method definitions are methods, classes are constructors.

# Prerequisites

- Ordinary function

# Key Properties

1. Three roles: real function, method, constructor.
2. Ordinary functions can play all three.
3. Specialized functions play exactly one.
4. The role determines how `this` is set.
5. Real function call: `this === undefined` (strict mode).
6. Method call: `this` is the receiver.
7. Constructor call: `this` is the new instance.

# Construction / Recognition

```js
function add(x, y) { return x + y; }
add(2, 1);                    // real function
const obj = { m: add };
obj.m(2, 1);                  // method
new add();                    // constructor
```

# Context & Application

Understanding roles helps choose the right function type (arrow, method, class) for each situation.

# Examples

From the source text (Ch. 27, section 27.2.4):

```js
// Real function
assert.equal(add(2, 1), 3);

// Method
const obj = { addAsMethod: add };
assert.equal(obj.addAsMethod(2, 4), 6);

// Constructor
const inst = new add();
assert.equal(inst instanceof add, true);
```

# Relationships

## Builds Upon
- **Ordinary Function** -- ordinary functions can play all roles

## Related
- **Specialized Function** -- each restricted to one role

# Source Reference

Chapter 27: Callable values, Section 27.2.4-27.2.5, lines 261-338.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit three-role taxonomy
- Cross-reference status: verified
