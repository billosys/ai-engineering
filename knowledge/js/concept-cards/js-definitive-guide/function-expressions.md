---
# === CORE IDENTIFICATION ===
concept: Function Expressions
slug: function-expressions

# === CLASSIFICATION ===
category: functions
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 201
section: "8.1.2 Function Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "anonymous function"
  - "function literal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - arrow-functions
  - iifes
contrasts_with:
  - function-declarations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes function declarations from function expressions?"
---

# Quick Definition

A function expression defines a function within the context of a larger expression; the name is optional, the function is not hoisted, and the value must be assigned to a variable to be referenced later.

# Core Definition

"Function expressions look a lot like function declarations, but they appear within the context of a larger expression or statement, and the name is optional." "A function declaration actually declares a variable and assigns a function object to it. A function expression, on the other hand, does not declare a variable." Functions defined as expressions "do not exist until the expression that defines them are actually evaluated." It is "a good practice to use const with function expressions so you don't accidentally overwrite your functions." (Flanagan, p. 201-202)

# Prerequisites

- **function-declarations** — Must understand declarations for contrast

# Key Properties

1. Name is optional (usually omitted)
2. Not hoisted -- cannot be called before definition
3. Must be assigned to a variable or used inline
4. If named, the name is only accessible within the function body (for recursion)
5. Best practice to use `const` for the variable assignment

# Construction / Recognition

```javascript
const square = function(x) { return x*x; };
const f = function fact(x) { if (x <= 1) return 1; else return x*fact(x-1); };
[3,2,1].sort(function(a,b) { return a-b; });
```

# Context & Application

Used when functions need to be assigned to variables, passed as arguments, or defined conditionally. Arrow functions are now often preferred for inline expressions.

# Examples

```javascript
const square = function(x) { return x*x; };
// Named expression (name only visible inside):
const f = function fact(x) { if (x <= 1) return 1; else return x*fact(x-1); };
// As argument:
[3,2,1].sort(function(a,b) { return a-b; });
// Immediately invoked:
let tensquared = (function(x) {return x*x;}(10));
```
(Flanagan, p. 201)

# Relationships

## Builds Upon
- **function-declarations** — Same syntax but different semantics

## Enables
- **iifes** — Function expressions can be immediately invoked
- **closures** — Often used to create closures

## Related
- **arrow-functions** — More compact expression syntax

## Contrasts With
- **function-declarations** — Declarations are hoisted and require a name

# Common Errors

- **Error**: Calling a function expression before it is defined.
  **Correction**: Function expressions are not hoisted. The variable must be defined before it is called.

# Common Confusions

- **Confusion**: Named function expressions create a variable in the outer scope.
  **Clarification**: The name of a named function expression is only bound within the function's own scope, not in the enclosing scope.

# Source Reference

Chapter 8: Functions, Section 8.1.2, pages 201-202.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with examples
- Uncertainties: None
- Cross-reference status: Verified
