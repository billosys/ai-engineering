---
# === CORE IDENTIFICATION ===
concept: Function Definition Expressions
slug: function-definition-expressions

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 80
section: "4.3 Function Definition Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "function literals"
  - "function expressions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - invocation-expressions
  - object-and-array-initializers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

A function definition expression defines a JavaScript function and evaluates to the newly created function object. It is analogous to a "function literal."

# Core Definition

"A *function definition expression* defines a JavaScript function, and the value of such an expression is the newly defined function. In a sense, a function definition expression is a 'function literal' in the same way that an object initializer is an 'object literal.'" (Ch. 4, §4.3)

# Prerequisites

- **primary-expressions** — Function expressions build on the concept of expressions that produce values.

# Key Properties

1. Consists of the `function` keyword, a comma-separated parameter list in parentheses, and a function body in curly braces.
2. Can optionally include a name for the function.
3. In ES6+, arrow function syntax provides a compact alternative.
4. Functions can also be defined via function declaration statements (not expressions).

# Construction / Recognition

```js
let square = function(x) { return x * x; };
```

# Context & Application

Function expressions are used to create functions inline, often as arguments to other functions or as property values. Understanding function expressions is a prerequisite for closures, callbacks, and higher-order programming.

# Examples

From the source text (§4.3, p. 81):

```js
// This function returns the square of the value passed to it.
let square = function(x) { return x * x; };
```

# Relationships

## Builds Upon
- **primary-expressions** — Function expressions are built from simpler expression concepts

## Enables
- **invocation-expressions** — Function expressions create the functions that invocation expressions call

## Related
- **object-and-array-initializers** — Analogous "literal" expressions for other types

## Contrasts With
- No direct contrast within this chapter; function declarations are covered in Ch. 8

# Common Errors

- **Error**: Confusing function expressions with function declarations.
  **Correction**: A function expression is part of a larger expression (e.g., assignment); a function declaration is a standalone statement that is hoisted.

# Common Confusions

- **Confusion**: Believing function expressions are hoisted like function declarations.
  **Clarification**: Function expressions are not hoisted — the variable holding them may be hoisted (if `var`), but the function value is not assigned until the expression is evaluated.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.3, pages 80-81.

# Verification Notes

- Definition source: Direct quote from §4.3
- Confidence rationale: High — brief but clear section
- Uncertainties: Full coverage deferred to Chapter 8
- Cross-reference status: Verified
