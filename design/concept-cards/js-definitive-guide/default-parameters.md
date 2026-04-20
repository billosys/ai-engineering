---
# === CORE IDENTIFICATION ===
concept: Default Parameters
slug: default-parameters

# === CLASSIFICATION ===
category: functions
subcategory: parameters
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 210
section: "8.3.1 Optional Parameters and Defaults"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "parameter defaults"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - rest-parameters
  - destructuring-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define optional function parameters in JavaScript?"
---

# Quick Definition

ES6 default parameters allow specifying default values directly in the function parameter list using `=` syntax. Defaults are evaluated at call time, not definition time, and can reference earlier parameters.

# Core Definition

"In ES6 and later, you can define a default value for each of your function parameters directly in the parameter list of your function. Simply follow the parameter name with an equals sign and the default value." "Parameter default expressions are evaluated when your function is called, not when it is defined." Defaults can reference preceding parameters. (Flanagan, p. 211)

# Prerequisites

- **function-declarations** — Must understand function parameters

# Key Properties

1. Syntax: `function f(x, y = defaultValue) {}`
2. Evaluated at call time, not definition time
3. Can reference earlier parameters
4. Can use variables or function calls as defaults
5. Optional parameters should be at the end of the parameter list
6. Works with arrow functions and all function forms

# Construction / Recognition

```javascript
function f(x, a = []) { ... }
const rectangle = (width, height=width*2) => ({width, height});
```

# Context & Application

Replaces the older `a = a || []` pattern and `if (a === undefined)` checks for optional parameters.

# Examples

```javascript
function getPropertyNames(o, a = []) {
    for (let property in o) a.push(property);
    return a;
}

// Default referencing earlier parameter:
const rectangle = (width, height=width*2) => ({width, height});
rectangle(1)  // => { width: 1, height: 2 }
```
(Flanagan, p. 211)

# Relationships

## Builds Upon
- **function-declarations** — Extends parameter syntax

## Enables
- Clean optional parameter handling

## Related
- **rest-parameters** — Another ES6 parameter feature
- **destructuring-parameters** — Can combine with defaults

## Contrasts With
- None specific

# Common Errors

- **Error**: Placing optional parameters before required ones.
  **Correction**: Optional parameters should be last so callers don't need to pass `undefined` for them.

# Common Confusions

- **Confusion**: Default values are shared across calls (like Python mutable defaults).
  **Clarification**: Defaults are re-evaluated on each call. A new `[]` is created each time.

# Source Reference

Chapter 8: Functions, Section 8.3.1, pages 210-211.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
