---
# === CORE IDENTIFICATION ===
concept: call() and apply() Methods
slug: call-and-apply

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
pdf_page: 227
section: "8.7.4 The call() and apply() Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "indirect invocation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - this-keyword-binding
  - invocation-patterns
extends: []
related:
  - bind-method
contrasts_with:
  - bind-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does call() relate to apply() and bind()?"
---

# Quick Definition

`call()` and `apply()` invoke a function with an explicitly specified `this` value. `call()` passes arguments individually; `apply()` passes them as an array.

# Core Definition

"call() and apply() allow you to indirectly invoke a function as if it were a method of some other object. The first argument to both call() and apply() is the object on which the function is to be invoked; this argument is the invocation context and becomes the value of the this keyword." "Any arguments to call() after the first invocation context argument are the values that are passed to the function." "The apply() method is like the call() method, except that the arguments to be passed to the function are specified as an array." Arrow functions ignore the first argument (their `this` cannot be overridden). (Flanagan, p. 227-228)

# Prerequisites

- **this-keyword-binding** — Must understand `this` binding
- **invocation-patterns** — call/apply is indirect invocation

# Key Properties

1. First argument becomes `this` inside the function
2. call(): subsequent arguments are individual values
3. apply(): second argument is an array of values
4. Arrow functions ignore the `this` argument
5. Can invoke any function as if it were a method of any object
6. ES6 spread operator often replaces apply() for argument spreading

# Construction / Recognition

```javascript
f.call(obj, arg1, arg2);
f.apply(obj, [arg1, arg2]);
```

# Context & Application

Used for method borrowing, invoking array methods on array-like objects, and setting `this` explicitly. apply() is especially useful for passing arrays as individual arguments (pre-ES6).

# Examples

```javascript
f.call(o);       // Invoke f as method of o
f.apply(o);      // Same thing

f.call(o, 1, 2);       // Pass individual args
f.apply(o, [1, 2]);    // Pass args as array

// Pre-ES6 way to find max in array:
let biggest = Math.max.apply(Math, arrayOfNumbers);
// ES6 equivalent:
let biggest = Math.max(...arrayOfNumbers);

// Method borrowing for array-like objects:
Array.prototype.slice.call(arraylike, 0);
```
(Flanagan, p. 227-228)

# Relationships

## Builds Upon
- **this-keyword-binding** — call/apply explicitly set `this`
- **invocation-patterns** — Indirect invocation pattern

## Enables
- Method borrowing
- Explicit `this` control

## Related
- **bind-method** — bind returns a new function with fixed `this`; call/apply invoke immediately

## Contrasts With
- **bind-method** — call/apply invoke immediately; bind creates a new function

# Common Errors

- **Error**: Using call/apply on arrow functions expecting to change `this`.
  **Correction**: Arrow functions inherit `this` from their definition scope; call/apply cannot override it.

# Common Confusions

- **Confusion**: call() and apply() are the same.
  **Clarification**: They differ in how arguments are passed: call() takes individual args, apply() takes an array.

# Source Reference

Chapter 8: Functions, Section 8.7.4, pages 227-228.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with clear examples
- Uncertainties: None
- Cross-reference status: Verified
