---
# === CORE IDENTIFICATION ===
concept: var Declarations and Hoisting
slug: var-declarations

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 73
section: "3.10.2 Variable Declarations with var"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - var keyword
  - function-scoped variables
  - variable hoisting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables-overview
  - let-and-const-declarations
extends:
  - variables-overview
related:
  - hoisting
  - global-object
  - strict-mode
contrasts_with:
  - let-and-const-declarations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do `let`/`const` relate to `var` in terms of scoping?"
  - "What is hoisting?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

`var` is the pre-ES6 variable declaration keyword that is function-scoped (not block-scoped), allows redeclaration, creates global object properties when used at top level, and exhibits "hoisting" where the declaration is moved to the top of the enclosing function.

# Core Definition

"In versions of JavaScript before ES6, the only way to declare a variable is with the var keyword." Key differences from `let`: (1) "Variables declared with var do not have block scope. Instead, they are scoped to the body of the containing function." (2) Global `var` declarations "are implemented as properties of the global object." (3) "It is legal to declare the same variable multiple times with var." (4) "One of the most unusual features of var declarations is known as hoisting. When a variable is declared with var, the declaration is lifted up (or 'hoisted') to the top of the enclosing function." (pp. 73-74)

# Prerequisites

- **variables-overview** — Must understand variables conceptually
- **let-and-const-declarations** — Must understand modern declarations to appreciate var's differences

# Key Properties

1. Function-scoped, not block-scoped
2. Global `var` declarations become properties of the global object (`globalThis`)
3. Global `var` properties cannot be deleted with `delete`
4. Legal to redeclare the same variable multiple times
5. Hoisting: declaration moves to top of function; initialization stays in place
6. Using a hoisted variable before initialization yields `undefined` (not ReferenceError)
7. No `const` equivalent existed before ES6
8. Cannot declare constants with `var`

# Construction / Recognition

```javascript
var x;
var data = [], count = data.length;
for(var i = 0; i < count; i++) console.log(data[i]);
```

# Context & Application

`var` is legacy syntax that still appears in older codebases. Understanding `var` is essential for reading pre-ES6 code and understanding hoisting-related bugs. Modern code should use `let` and `const` instead.

# Examples

From the source text (pp. 73-74):
```javascript
var x;
var data = [], count = data.length;
for(var i = 0; i < count; i++) console.log(data[i]);

// Function scope, not block scope:
// var i declared in a for loop is visible throughout the entire function

// Hoisting example:
// When you write:
function f() {
    console.log(x);  // undefined, not ReferenceError
    var x = 5;
    console.log(x);  // 5
}
// JavaScript interprets as:
function f() {
    var x;            // Declaration hoisted
    console.log(x);   // undefined
    x = 5;            // Initialization stays here
    console.log(x);   // 5
}
```

Global var as global object property (p. 73):
```javascript
// var x = 2; outside a function is like:
// globalThis.x = 2;
// But the property cannot be deleted
```

# Relationships

## Builds Upon
- **variables-overview** — var is the original variable declaration keyword

## Enables
- **hoisting** — var declarations exhibit hoisting behavior
- Understanding legacy JavaScript code

## Related
- **global-object** — Global var declarations become properties of the global object
- **strict-mode** — Strict mode prevents accidental global variable creation

## Contrasts With
- **let-and-const-declarations** — let/const are block-scoped, not hoisted in the same way, and cannot be redeclared

# Common Errors

- **Error**: Expecting `var` in a for loop to be scoped to the loop body.
  **Correction**: `var` is function-scoped, so `var i` in a `for` loop is visible throughout the entire function, not just the loop.

- **Error**: Relying on a `var` variable before it's initialized and expecting an error.
  **Correction**: Due to hoisting, the variable exists (as `undefined`) from the start of the function — no error is thrown.

# Common Confusions

- **Confusion**: `var` hoisting means the entire declaration including initialization is moved.
  **Clarification**: Only the declaration is hoisted. "The initialization of the variable remains where you wrote it, but the definition of the variable moves to the top of the function." (p. 74)

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.2, pages 73-74.

# Verification Notes

- Definition source: Direct quotes from pp. 73-74
- Confidence rationale: High — thoroughly explained with four key differences listed
- Uncertainties: None
- Cross-reference status: Verified
