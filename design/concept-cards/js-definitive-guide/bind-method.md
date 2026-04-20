---
# === CORE IDENTIFICATION ===
concept: bind() Method
slug: bind-method

# === CLASSIFICATION ===
category: functions
subcategory: invocation
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 228
section: "8.7.5 The bind() Method"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - this-keyword-binding
  - call-and-apply
extends: []
related:
  - partial-application-currying
  - arrow-function-this-inheritance
contrasts_with:
  - call-and-apply

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does call() relate to apply() and bind()?"
---

# Quick Definition

`bind()` returns a new function that, when called, has its `this` permanently set to the specified object and optionally has some arguments pre-filled (partial application).

# Core Definition

"The primary purpose of bind() is to bind a function to an object. When you invoke the bind() method on a function f and pass an object o, the method returns a new function. Invoking the new function (as a function) invokes the original function f as a method of o." "The bind() method does more than just bind a function to an object, however. It can also perform partial application: any arguments you pass to bind() after the first are bound along with the this value." Arrow functions cannot have their `this` overridden by bind(). "The name property of the function returned by bind() is the name property of the function that bind() was called on, prefixed with the word 'bound'." (Flanagan, p. 228-229)

# Prerequisites

- **this-keyword-binding** — Must understand `this` binding
- **call-and-apply** — bind() is related to call/apply but returns a function instead of invoking

# Key Properties

1. Returns a new function (does not invoke immediately)
2. `this` is permanently bound -- even as a method of another object
3. Additional arguments after the first are pre-filled (partial application)
4. Partial application works even with arrow functions
5. Does not work to override `this` on arrow functions
6. Bound function's name is prefixed with "bound"

# Construction / Recognition

```javascript
let bound = f.bind(obj);
let partial = f.bind(obj, arg1, arg2);
let noThis = f.bind(null, arg1);  // just partial application
```

# Context & Application

Used to fix `this` for callbacks extracted from objects, and for partial application of functions.

# Examples

```javascript
function f(y) { return this.x + y; }
let o = { x: 1 };
let g = f.bind(o);
g(2)              // => 3
let p = { x: 10, g };
p.g(2)            // => 3: g is still bound to o, not p

// Partial application:
let sum = (x,y) => x + y;
let succ = sum.bind(null, 1);
succ(2)           // => 3: x is bound to 1, y is 2

function f(y,z) { return this.x + y + z; }
let g = f.bind({x: 1}, 2);
g(3)              // => 6: this.x=1, y=2, z=3
```
(Flanagan, p. 228-229)

# Relationships

## Builds Upon
- **this-keyword-binding** — bind() creates permanent `this` binding
- **call-and-apply** — bind is the deferred version of call/apply

## Enables
- **partial-application-currying** — bind() performs partial application
- Safe callback extraction from objects

## Related
- **arrow-function-this-inheritance** — Arrow functions achieve similar `this` fixing

## Contrasts With
- **call-and-apply** — call/apply invoke immediately; bind returns a new function

# Common Errors

- **Error**: Expecting bind() to modify the original function.
  **Correction**: bind() returns a new function; the original is unchanged.

# Common Confusions

- **Confusion**: bind() can change `this` for arrow functions.
  **Clarification**: Arrow functions have lexically fixed `this`. bind() on an arrow function only does partial application; the first argument (this) is ignored.

# Source Reference

Chapter 8: Functions, Section 8.7.5, pages 228-229.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with examples
- Uncertainties: None
- Cross-reference status: Verified
