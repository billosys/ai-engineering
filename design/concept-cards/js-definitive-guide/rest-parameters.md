---
# === CORE IDENTIFICATION ===
concept: Rest Parameters
slug: rest-parameters

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
pdf_page: 211
section: "8.3.2 Rest Parameters and Variable-Length Argument Lists"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "variadic parameters"
  - "varargs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - spread-in-function-calls
  - arguments-object
contrasts_with:
  - arguments-object
  - spread-in-function-calls

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a function that accepts any number of arguments?"
---

# Quick Definition

A rest parameter (`...name`) collects all remaining arguments into an array. It must be the last parameter and enables writing functions that accept variable numbers of arguments.

# Core Definition

"Rest parameters enable us to write functions that can be invoked with arbitrarily more arguments than parameters." "A rest parameter is preceded by three periods, and it must be the last parameter in a function declaration." The rest parameter is always an array (possibly empty, never undefined). Functions that accept any number of arguments are called "variadic functions" or "varargs." (Flanagan, p. 211-212)

# Prerequisites

- **function-declarations** — Must understand function parameters

# Key Properties

1. Syntax: `function f(first, ...rest) {}`
2. Must be the last parameter
3. Always an array (may be empty, never undefined)
4. Cannot have a default value
5. Replaces the legacy `arguments` object for new code

# Construction / Recognition

```javascript
function max(first=-Infinity, ...rest) {
    let maxValue = first;
    for (let n of rest) {
        if (n > maxValue) maxValue = n;
    }
    return maxValue;
}
```

# Context & Application

Use for functions that need to accept variable numbers of arguments. Preferred over the `arguments` object in modern code.

# Examples

```javascript
function max(first=-Infinity, ...rest) {
    let maxValue = first;
    for (let n of rest) {
        if (n > maxValue) maxValue = n;
    }
    return maxValue;
}
max(1, 10, 100, 2, 3, 1000, 4, 5, 6)  // => 1000
```
(Flanagan, p. 212)

# Relationships

## Builds Upon
- **function-declarations** — Extends parameter syntax

## Enables
- Variadic function definitions

## Related
- **spread-in-function-calls** — Same `...` syntax but opposite direction (gathering vs. spreading)
- **arguments-object** — Legacy way to access all arguments

## Contrasts With
- **arguments-object** — Rest gives a true array; arguments is array-like
- **spread-in-function-calls** — Rest gathers into array; spread expands array into args

# Common Errors

- **Error**: Placing a rest parameter before other parameters.
  **Correction**: Rest parameters must be the last parameter in the list.

# Common Confusions

- **Confusion**: Rest parameters and the spread operator are the same thing.
  **Clarification**: Rest gathers multiple arguments into an array (in definitions); spread expands an array into individual arguments (in calls).

# Source Reference

Chapter 8: Functions, Section 8.3.2, pages 211-212.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
