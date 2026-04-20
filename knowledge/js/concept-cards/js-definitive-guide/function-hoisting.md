---
# === CORE IDENTIFICATION ===
concept: Function Hoisting
slug: function-hoisting

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
  - "declaration hoisting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - function-expressions
  - class-keyword-syntax
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes function declarations from function expressions?"
  - "Why can I call a function before it appears in my code?"
---

# Quick Definition

Function declarations are "hoisted" to the top of the enclosing scope, meaning the function is available throughout the scope -- even in code that appears before the declaration.

# Core Definition

"Function declaration statements are 'hoisted' to the top of the enclosing script, function, or block so that functions defined in this way may be invoked from code that appears before the definition. Another way to say this is that all of the functions declared in a block of JavaScript code will be defined throughout that block, and they will be defined before the JavaScript interpreter begins to execute any of the code in that block." Function expressions are NOT hoisted. (Flanagan, p. 200)

# Prerequisites

- **function-declarations** — Hoisting applies specifically to declarations

# Key Properties

1. Only function declarations are hoisted, not function expressions
2. The entire function definition is hoisted (not just the name)
3. In ES6 strict mode, block-scoped declarations are hoisted only within the block
4. Class declarations are NOT hoisted (unlike function declarations)

# Construction / Recognition

```javascript
// This works because of hoisting:
greet();
function greet() { console.log("hello"); }

// This does NOT work:
// square(2);  // TypeError: square is not a function
// const square = function(x) { return x*x; };
```

# Context & Application

Hoisting allows organizing code with main logic first and helper functions later. Understanding hoisting is crucial for debugging reference errors.

# Examples

```javascript
// Valid: function declarations are hoisted
let result = factorial(5);  // Works!
function factorial(x) {
    if (x <= 1) return 1;
    return x * factorial(x-1);
}
```
(Flanagan, p. 200)

# Relationships

## Builds Upon
- **function-declarations** — Hoisting is a property of declarations

## Enables
- Flexible code organization

## Related
- **function-expressions** — Expressions are NOT hoisted
- **class-keyword-syntax** — Classes are NOT hoisted

## Contrasts With
- None specific (contrasts with non-hoisted forms)

# Common Errors

- **Error**: Assuming function expressions are hoisted.
  **Correction**: Only function declarations are hoisted. `const f = function(){}` is not available before that line.

# Common Confusions

- **Confusion**: `var f = function(){}` is hoisted like a function declaration.
  **Clarification**: The `var f` variable is hoisted (as undefined), but the function assignment is not. Calling `f()` before the assignment results in TypeError.

# Source Reference

Chapter 8: Functions, Section 8.1.1, page 200.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated
- Uncertainties: None
- Cross-reference status: Verified
