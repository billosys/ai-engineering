---
# === CORE IDENTIFICATION ===
concept: Functions as First-Class Values
slug: functions-as-values

# === CLASSIFICATION ===
category: functions
subcategory: functional patterns
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 217
section: "8.4 Functions as Values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "first-class functions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - higher-order-functions
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean that functions are first-class in JavaScript?"
---

# Quick Definition

In JavaScript, functions are objects that can be assigned to variables, stored in object properties or array elements, passed as arguments, and returned from other functions -- making them first-class values.

# Core Definition

"In JavaScript, functions are not only syntax but also values, which means they can be assigned to variables, stored in the properties of objects or the elements of arrays, passed as arguments to functions, and so on." A function can even be assigned to another variable and still work the same way. Functions can have their own properties. (Flanagan, p. 217-218)

# Prerequisites

- **function-declarations** — Must understand functions as syntax first

# Key Properties

1. Can be assigned to variables
2. Can be stored in object properties (methods) or array elements
3. Can be passed as arguments to other functions
4. Can be returned from functions
5. Functions are objects and can have properties
6. `typeof` returns "function" for function values

# Construction / Recognition

```javascript
let s = square;       // assign function to another variable
s(4)                  // => 16
let o = {square: function(x) { return x*x; }};
let a = [x => x*x, 20];
a[0](a[1])            // => 400
```

# Context & Application

This property is the foundation of functional programming in JavaScript and enables callbacks, higher-order functions, and closures.

# Examples

```javascript
function square(x) { return x*x; }
let s = square;
square(4)     // => 16
s(4)          // => 16

let o = {square: function(x) { return x*x; }};
let y = o.square(16);  // y == 256

let a = [x => x*x, 20];
a[0](a[1])    // => 400

// Functions can have properties:
uniqueInteger.counter = 0;
function uniqueInteger() {
    return uniqueInteger.counter++;
}
```
(Flanagan, p. 217-220)

# Relationships

## Builds Upon
- **function-declarations** — Functions as objects extend beyond syntax

## Enables
- **higher-order-functions** — Functions that operate on functions
- **closures** — Functions returned from functions
- **partial-application-currying** — Building new functions from existing ones

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Treating functions as special constructs that can't be manipulated like other values.
  **Correction**: Functions are objects. They can be stored, passed, and have properties.

# Common Confusions

- **Confusion**: Assigning a function to a variable creates a copy.
  **Clarification**: It creates another reference to the same function object.

# Source Reference

Chapter 8: Functions, Section 8.4, pages 217-220.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with examples
- Uncertainties: None
- Cross-reference status: Verified
