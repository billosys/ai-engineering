---
# === CORE IDENTIFICATION ===
concept: Function Declarations
slug: function-declarations

# === CLASSIFICATION ===
category: functions
subcategory: declarations
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 199
section: "8.1.1 Function Declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "function statement"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - function-expressions
  - arrow-functions
  - function-hoisting
contrasts_with:
  - function-expressions
  - arrow-functions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes function declarations from function expressions?"
---

# Quick Definition

A function declaration uses the `function` keyword followed by a required name, parameter list, and body. Declarations are hoisted, making the function available throughout the enclosing scope before the declaration appears in code.

# Core Definition

"Function declarations consist of the function keyword, followed by these components: An identifier that names the function (required), a pair of parentheses around parameter names, and a pair of curly braces with the function body." "Function declaration statements are 'hoisted' to the top of the enclosing script, function, or block so that functions defined in this way may be invoked from code that appears before the definition." (Flanagan, p. 199-201)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Name is required
2. Hoisted to top of enclosing scope
3. Can be called before the declaration in code
4. In ES6 strict mode, declarations within blocks are scoped to that block
5. Without return statement, returns undefined

# Construction / Recognition

```javascript
function name(params) {
    // body
}
```

# Context & Application

The primary way to define named, reusable functions. Hoisting allows organizing code with function calls before definitions.

# Examples

```javascript
function distance(x1, y1, x2, y2) {
    let dx = x2 - x1;
    let dy = y2 - y1;
    return Math.sqrt(dx*dx + dy*dy);
}

function factorial(x) {
    if (x <= 1) return 1;
    return x * factorial(x-1);
}

// Can be called before declaration due to hoisting:
printprops({x: 1});
function printprops(o) {
    for (let p in o) {
        console.log(`${p}: ${o[p]}\n`);
    }
}
```
(Flanagan, p. 199-200)

# Relationships

## Builds Upon
- No prerequisites within scope

## Enables
- **function-hoisting** — Declarations are hoisted
- **closures** — Functions can be nested and form closures
- **constructor-functions** — Constructor functions use declarations

## Related
- **function-expressions** — Alternative form without hoisting
- **arrow-functions** — Compact alternative (ES6)

## Contrasts With
- **function-expressions** — Expressions are not hoisted; name is optional
- **arrow-functions** — Arrow functions have no `this` binding

# Common Errors

- **Error**: Omitting the function name in a declaration.
  **Correction**: The name is required in declarations. Use a function expression for anonymous functions.

# Common Confusions

- **Confusion**: Function declarations and function expressions behave the same.
  **Clarification**: Declarations are hoisted; expressions are not. Declarations require a name; expressions don't.

# Source Reference

Chapter 8: Functions, Section 8.1.1, pages 199-201.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Fundamental concept, clearly stated
- Uncertainties: None
- Cross-reference status: Verified
