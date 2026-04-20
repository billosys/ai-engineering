---
concept: Function Declaration vs Expression
slug: function-declaration-vs-expression
category: functions
subcategory: function-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.2.2 Terminology: function definitions and function expressions"
extraction_confidence: high
aliases:
  - "function definition"
  - "named function expression"
prerequisites:
  - ordinary-function
extends: []
related:
  - arrow-function
contrasts_with: []
answers_questions:
  - "What is the difference between a function declaration and a function expression?"
---

# Quick Definition

A function declaration is a statement that creates a named ordinary function with early activation (hoisting), while a function expression is an expression that creates a function value and is not hoisted.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, a function definition is syntax that creates functions. Function declarations are statements, activated early (can be called before their position in code). Function expressions produce a value and are not activated early. Named function expressions have a name accessible only inside the function body, useful for self-recursion. In modern code, function expressions are almost always arrow functions.

# Prerequisites

- Ordinary function

# Key Properties

1. Function declarations are hoisted; function expressions are not.
2. Named function expressions have a name accessible only inside the body.
3. Functions created via variable declarations inherit the variable name.
4. Named functions show their names in stack traces.
5. In modern code, function expressions are almost always arrow functions.

# Construction / Recognition

```js
// Function declaration (hoisted)
function add(x, y) { return x + y; }

// Anonymous function expression
const add2 = function (x, y) { return x + y; };

// Named function expression
const add3 = function myAdd(x, y) { return x + y; };
```

# Context & Application

Use function declarations for named stand-alone functions where hoisting is useful. Use arrow function expressions for callbacks and inline functions.

# Examples

From the source text (Ch. 27, section 27.2.1):

```js
const func = function funcExpr() { return funcExpr };
assert.equal(func(), func);

// funcExpr only accessible inside:
assert.throws(() => funcExpr(), ReferenceError);
```

# Relationships

## Related
- **Arrow Function** -- the preferred expression form in modern JavaScript

# Common Confusions

- **Confusion**: Thinking `const f = function() {}` and `function f() {}` behave the same.
  **Clarification**: The declaration is hoisted; the expression is not.

# Source Reference

Chapter 27: Callable values, Section 27.2.1-27.2.2, lines 122-212.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit terminology section
- Cross-reference status: verified
