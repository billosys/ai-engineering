---
# === CORE IDENTIFICATION ===
concept: Higher-Order Functions
slug: higher-order-functions

# === CLASSIFICATION ===
category: functions
subcategory: functional patterns
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 232
section: "8.8.2 Higher-Order Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "HOF"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - functions-as-values
  - closures
extends: []
related:
  - partial-application-currying
  - memoization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
---

# Quick Definition

A higher-order function is a function that operates on other functions: it takes one or more functions as arguments and/or returns a new function.

# Core Definition

"A higher-order function is a function that operates on functions, taking one or more functions as arguments and returning a new function." Examples include `not()` (negating a predicate), `mapper()` (creating array mapping functions), and `compose()` (function composition). (Flanagan, p. 232)

# Prerequisites

- **functions-as-values** — Functions must be passable as arguments and returnable
- **closures** — Returned functions typically form closures

# Key Properties

1. Takes function(s) as arguments and/or returns functions
2. Creates new behavior by combining existing functions
3. Central to functional programming style
4. Array methods like map, filter, reduce are higher-order functions

# Construction / Recognition

```javascript
function not(f) {
    return function(...args) {
        let result = f.apply(this, args);
        return !result;
    };
}

function compose(f, g) {
    return function(...args) {
        return f.call(this, g.apply(this, args));
    };
}
```

# Context & Application

Higher-order functions enable function composition, abstraction over behavior, and the functional programming style in JavaScript.

# Examples

```javascript
function not(f) {
    return function(...args) {
        let result = f.apply(this, args);
        return !result;
    };
}
const even = x => x % 2 === 0;
const odd = not(even);
[1,1,3,5,5].every(odd)  // => true

function compose(f, g) {
    return function(...args) {
        return f.call(this, g.apply(this, args));
    };
}
const sum = (x,y) => x+y;
const square = x => x*x;
compose(square, sum)(2,3)  // => 25
```
(Flanagan, p. 232-233)

# Relationships

## Builds Upon
- **functions-as-values** — Functions as arguments and return values
- **closures** — Returned functions capture enclosing scope

## Enables
- **partial-application-currying** — A specific higher-order function pattern
- **memoization** — Caching via higher-order functions
- Function composition

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Forgetting to preserve `this` when wrapping functions.
  **Correction**: Use `f.apply(this, args)` or `f.call(this, ...)` to forward the invocation context.

# Common Confusions

- **Confusion**: Higher-order functions are just callbacks.
  **Clarification**: Callbacks are one use of higher-order functions. HOFs also include function factories and combinators that return new functions.

# Source Reference

Chapter 8: Functions, Section 8.8.2, pages 232-233.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with examples
- Uncertainties: None
- Cross-reference status: Verified
