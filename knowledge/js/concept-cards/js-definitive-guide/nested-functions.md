---
# === CORE IDENTIFICATION ===
concept: Nested Functions
slug: nested-functions

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
pdf_page: 203
section: "8.1.4 Nested Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "inner functions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

In JavaScript, functions may be nested within other functions and can access the variables and parameters of all enclosing functions -- the basis for closures.

# Core Definition

"In JavaScript, functions may be nested within other functions." "The interesting thing about nested functions is their variable scoping rules: they can access the parameters and variables of the function (or functions) they are nested within." (Flanagan, p. 203)

# Prerequisites

- **function-declarations** — Must understand basic function definition

# Key Properties

1. Inner functions can access outer function variables and parameters
2. This scoping rule is the foundation for closures
3. The inner function's scope includes all enclosing function scopes

# Construction / Recognition

```javascript
function outer(a, b) {
    function inner(x) { return x*x; }
    return Math.sqrt(inner(a) + inner(b));
}
```

# Context & Application

Nested functions enable closures and are used for helper functions, encapsulation, and functional patterns.

# Examples

```javascript
function hypotenuse(a, b) {
    function square(x) { return x*x; }
    return Math.sqrt(square(a) + square(b));
}
```
(Flanagan, p. 203)

# Relationships

## Builds Upon
- **function-declarations** — Functions defined within functions

## Enables
- **closures** — Nested functions that outlive their enclosing function create closures

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Assuming nested functions have their own independent scope with no access to outer variables.
  **Correction**: Nested functions inherit the scope of all enclosing functions.

# Common Confusions

- **Confusion**: Nested functions share the `this` value of their enclosing function.
  **Clarification**: Non-arrow nested functions define their own `this` value. Only arrow functions inherit `this` from the enclosing scope.

# Source Reference

Chapter 8: Functions, Section 8.1.4, page 203.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated
- Uncertainties: None
- Cross-reference status: Verified
