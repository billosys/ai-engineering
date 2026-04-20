---
# === CORE IDENTIFICATION ===
concept: First-Class Functions
slug: first-class-functions

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 24
section: "1.3 A Tour of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - functions as values
  - function expressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - variables-overview
extends: []
related:
  - arrow-functions
  - type-system-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

In JavaScript, functions are first-class values — they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures, just like numbers or strings.

# Core Definition

As introduced in Chapter 1, JavaScript "derives its first-class functions from Scheme" (p. 18). Functions are "values and can be assigned to vars" (p. 24). "Like any JavaScript value that is not a primitive value, functions and classes are a specialized kind of object" (p. 41). A function is "a named and parameterized block of JavaScript code that you define once, and can then invoke over and over again" (p. 24).

# Prerequisites

- **javascript-language-overview** — Functions are a core language feature
- **variables-overview** — Functions can be assigned to variables

# Key Properties

1. Functions can be assigned to variables
2. Functions can be passed as arguments to other functions
3. Functions can be returned from other functions
4. Functions are a specialized kind of object
5. Two definition syntaxes: `function` declarations and arrow functions (`=>`)
6. Functions derive from the Scheme programming language tradition

# Construction / Recognition

```javascript
// Function declaration
function plus1(x) { return x + 1; }

// Function expression assigned to variable
let square = function(x) { return x * x; };

// Arrow function (ES6)
const plus1 = x => x + 1;
```

# Context & Application

First-class functions are the foundation for JavaScript's functional programming capabilities, enabling patterns like callbacks, higher-order functions, and closures. Understanding that functions are values is essential before learning closures.

# Examples

From the source text (p. 24-25):
```javascript
function plus1(x) {
    return x + 1;
}
plus1(y)                  // => 4: y is 3, so this invocation returns 3+1

let square = function(x) {
    return x * x;
};
square(plus1(y))          // => 16: invoke two functions in one expression
```

Arrow function syntax (p. 25):
```javascript
const plus1 = x => x + 1;
const square = x => x * x;
plus1(y)                  // => 4
square(plus1(y))          // => 16
```

# Relationships

## Builds Upon
- **javascript-language-overview** — First-class functions are a defining language feature
- **variables-overview** — Functions are stored in variables

## Enables
- Closures (covered in Chapter 8)
- Callbacks and higher-order functions (covered in later chapters)

## Related
- **arrow-functions** — ES6 shorthand syntax for function expressions
- **type-system-overview** — Functions are a specialized kind of object

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting the parentheses when invoking a function, resulting in a reference to the function rather than its return value.
  **Correction**: `square` references the function; `square(4)` invokes it and returns 16.

# Common Confusions

- **Confusion**: Functions in JavaScript work like functions in C or Java.
  **Clarification**: JavaScript functions are values (objects), not just code blocks — they can be manipulated like any other value.

# Source Reference

Chapter 1: Introduction to JavaScript, Section 1.3, pages 18, 24-25.

# Verification Notes

- Definition source: Direct quotes from pp. 18, 24, 41
- Confidence rationale: High — clearly introduced with examples
- Uncertainties: Full function treatment deferred to Chapter 8
- Cross-reference status: Verified
