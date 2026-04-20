---
# === CORE IDENTIFICATION ===
concept: Immediately Invoked Function Expressions (IIFEs)
slug: iifes

# === CLASSIFICATION ===
category: functions
subcategory: functional patterns
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 220
section: "8.5 Functions as Namespaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "IIFE"
  - "self-invoking function"
  - "immediately invoked function expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-expressions
  - functions-as-values
extends: []
related:
  - closures
  - closure-based-private-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an IIFE and why is it used?"
---

# Quick Definition

An IIFE is a function expression that is defined and immediately invoked in a single expression, commonly used to create a private scope and avoid polluting the global namespace.

# Core Definition

"This technique of defining and invoking a function in a single expression is used frequently enough that it has become idiomatic and has been given the name 'immediately invoked function expression.'" The open parenthesis before `function` distinguishes it from a function declaration. "This use of functions as namespaces becomes really useful when we define one or more functions inside the namespace function using variables within that namespace, but then pass them back out as the return value of the namespace function. Functions like this are known as closures." (Flanagan, p. 220-221)

# Prerequisites

- **function-expressions** — IIFEs are function expressions
- **functions-as-values** — Functions as values enable immediate invocation

# Key Properties

1. Wrapping parentheses required: `(function() { ... }())`
2. Creates a private scope for variables
3. Variables inside are not visible outside
4. Often used with closures to create private state
5. Less necessary with ES6 `let`/`const` block scoping, but still used

# Construction / Recognition

```javascript
(function() {
    // Private scope
}());

// or
(function() {
    // Private scope
})();
```

# Context & Application

Used to create private namespaces, especially in pre-ES6 code. Still useful for creating closures with private state.

# Examples

```javascript
(function() {
    // Chunk of code goes here
    // Variables are local, not global
}());

// IIFE creating a closure:
let uniqueInteger = (function() {
    let counter = 0;
    return function() { return counter++; };
}());
uniqueInteger()  // => 0
uniqueInteger()  // => 1
```
(Flanagan, p. 220-222)

# Relationships

## Builds Upon
- **function-expressions** — IIFEs are function expressions
- **functions-as-values** — Functions as invocable values

## Enables
- **closures** — IIFEs often return closures
- **closure-based-private-state** — Classic pattern combining IIFE + closure

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Omitting the wrapping parentheses around the function expression.
  **Correction**: Without parens, JavaScript parses `function` as a declaration statement. The IIFE must be wrapped in parentheses.

# Common Confusions

- **Confusion**: IIFEs are obsolete with ES6 modules and block scoping.
  **Clarification**: While less necessary for namespace isolation, IIFEs remain useful for creating closures with private state.

# Source Reference

Chapter 8: Functions, Section 8.5, pages 220-221.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented idiomatic pattern
- Uncertainties: None
- Cross-reference status: Verified
