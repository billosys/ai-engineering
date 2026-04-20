---
# === CORE IDENTIFICATION ===
concept: Function length, name, and prototype Properties
slug: function-properties

# === CLASSIFICATION ===
category: functions
subcategory: function properties
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 226
section: "8.7.1-8.7.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - functions-as-values
extends: []
related:
  - constructor-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties do JavaScript function objects have?"
---

# Quick Definition

Function objects have `length` (number of declared parameters, excluding rest), `name` (the function's name or the variable it was assigned to), and `prototype` (an object used as prototype for instances created with `new`).

# Core Definition

"The read-only length property of a function specifies the arity of the function -- the number of parameters it declares in its parameter list." Rest parameters are not counted. "The read-only name property of a function specifies the name that was used when the function was defined." "All functions, except arrow functions, have a prototype property that refers to an object known as the prototype object. When a function is used as a constructor, the newly created object inherits properties from the prototype object." (Flanagan, p. 226-227)

# Prerequisites

- **functions-as-values** — Must understand that functions are objects with properties

# Key Properties

1. `length`: number of declared parameters (excludes rest parameter)
2. `name`: function name, or variable/property name for anonymous functions
3. `prototype`: the prototype object for constructor use
4. Arrow functions lack `prototype`
5. All three are read-only

# Construction / Recognition

```javascript
function f(a, b, ...rest) {}
f.length    // => 2 (rest not counted)
f.name      // => "f"
f.prototype // => {} (the prototype object)
```

# Context & Application

The `length` property is used by frameworks for introspection. The `name` property is useful for debugging. The `prototype` property is fundamental to class/constructor mechanics.

# Examples

```javascript
function f(a, b, ...rest) {}
f.length     // => 2
f.name       // => "f"

const g = function() {};
g.name       // => "g" (inferred from variable name)
```
(Flanagan, p. 226-227)

# Relationships

## Builds Upon
- **functions-as-values** — Functions as objects with properties

## Enables
- **constructor-functions** — prototype property is used by constructors

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Including rest parameters in the expected `length` count.
  **Correction**: Rest parameters are not counted in `f.length`.

# Common Confusions

- **Confusion**: Arrow functions have a prototype property.
  **Clarification**: Arrow functions do not have a prototype property and cannot be used as constructors.

# Source Reference

Chapter 8: Functions, Sections 8.7.1-8.7.3, pages 226-227.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
