---
# === CORE IDENTIFICATION ===
concept: Partial Application and Currying
slug: partial-application-currying

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
pdf_page: 233
section: "8.8.3 Partial Application of Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "currying"
  - "partial application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closures
  - bind-method
  - higher-order-functions
extends: []
related:
  - memoization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is partial application of functions?"
---

# Quick Definition

Partial application creates a new function from an existing one by pre-filling some arguments. JavaScript's `bind()` performs left-partial application; custom functions can do right-partial or template-based partial application.

# Core Definition

"The bind() method of a function f returns a new function that invokes f in a specified context and with a specified set of arguments. We say that it binds the function to an object and partially applies the arguments." The text defines `partialLeft()`, `partialRight()`, and `partial()` (with undefined placeholders) functions for flexible partial application. This technique "is sometimes called currying." (Flanagan, p. 233-235)

# Prerequisites

- **closures** — Partially applied functions are closures
- **bind-method** — bind() performs left-partial application
- **higher-order-functions** — Partial application produces new functions

# Key Properties

1. bind() does left-partial application (binds leading arguments)
2. Custom partialRight() binds trailing arguments
3. Custom partial() uses undefined as placeholder for unfilled positions
4. Creates specialized functions from general ones
5. Central technique in functional programming

# Construction / Recognition

```javascript
// Using bind for partial application:
let succ = sum.bind(null, 1);

// Custom partial application:
function partialLeft(f, ...outerArgs) {
    return function(...innerArgs) {
        let args = [...outerArgs, ...innerArgs];
        return f.apply(this, args);
    };
}
```

# Context & Application

Used to specialize general functions, create pipelines, and build domain-specific functions from primitives.

# Examples

```javascript
let sum = (x,y) => x + y;
let succ = sum.bind(null, 1);
succ(2)  // => 3

const f = function(x,y,z) { return x * (y - z); };
partialLeft(f, 2)(3,4)              // => -2: 2 * (3 - 4)
partialRight(f, 2)(3,4)             // => 6:  3 * (4 - 2)
partial(f, undefined, 2)(3,4)       // => -6: 3 * (2 - 4)

const increment = partialLeft(sum, 1);
const cuberoot = partialRight(Math.pow, 1/3);
cuberoot(increment(26))  // => 3
```
(Flanagan, p. 233-235)

# Relationships

## Builds Upon
- **closures** — Partially applied functions are closures over bound arguments
- **bind-method** — bind() is the built-in way to do partial application
- **higher-order-functions** — Partial application is a higher-order function pattern

## Enables
- Function composition chains
- Specialized functions from general ones

## Related
- **memoization** — Another functional programming technique

## Contrasts With
- None specific

# Common Errors

- **Error**: Confusing partial application with currying.
  **Correction**: Currying transforms a function of N arguments into N nested functions of 1 argument each. Partial application pre-fills some arguments but can leave multiple remaining.

# Common Confusions

- **Confusion**: bind() is only for `this` binding.
  **Clarification**: bind() also performs partial application. Arguments after the first are bound as leading arguments.

# Source Reference

Chapter 8: Functions, Section 8.8.3, pages 233-235.

# Verification Notes

- Definition source: Direct quote and synthesis from source text
- Confidence rationale: Well-documented with detailed examples
- Uncertainties: None
- Cross-reference status: Verified
