---
# === CORE IDENTIFICATION ===
concept: "Function .name Property"
slug: function-name-property

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.1 Names of functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Function.name"
  - ".name property"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - named-function-expression
  - anonymous-function-expression
  - arrow-function-naming
  - configurable-name-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

The `.name` property of a function contains the function's name as a string, used in stack traces and metaprogramming tasks, standardized in ES6.

# Core Definition

From "Deep JavaScript" (Ch 21.1): "The property `.name` of a function contains the function's name." And: "Prior to ECMAScript 6, this property was already supported by most engines. With ES6, it became part of the language standard. The language has become surprisingly good at finding names for functions, even when they are initially anonymous (e.g., arrow functions)."

# Prerequisites

None -- foundational concept for function naming.

# Key Properties

1. Every function has a `.name` property (string)
2. Standardized in ES6
3. Used in stack traces for debugging
4. The property is non-writable but configurable
5. JavaScript infers names for anonymous functions from context (variable name, property key, etc.)
6. Subject to minification -- names may change in production

# Construction / Recognition

## To Construct/Create:
1. Function declarations: name from the declaration
2. Named function expressions: name from the expression
3. Anonymous functions: name inferred from context (variable, property, etc.)

## To Identify/Recognize:
1. Access via `func.name`

# Context & Application

Function names improve debugging by appearing in stack traces. They also enable metaprogramming tasks like picking functions by name. The name is set at creation time and not updated by later assignments.

# Examples

**Example 1** (Ch 21):
```js
function myBeautifulFunction() {}
assert.equal(myBeautifulFunction.name, 'myBeautifulFunction');
```

**Example 2** (Ch 21): Stack trace with missing name:
```js
// The arrow function at line 11 has no name, shown as blank in stack trace:
//     at ch_function-names.mjs:11:18
```

# Relationships

## Enables
- **Stack trace debugging** — Names appear in error stack traces
- **Metaprogramming** — Picking functions by name

## Related
- **Named function expression** — Expression that explicitly sets `.name`
- **Configurable name property** — `.name` can be changed via `Object.defineProperty`

# Common Errors

- **Error**: Assigning to `.name` directly to change a function's name
  **Correction**: `.name` is non-writable; use `Object.defineProperty()` to change it

# Common Confusions

- **Confusion**: Minified function names are the same as development names
  **Clarification**: "Function names are subject to minification, which means that they will usually change in minified code"

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.1, lines 11437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Central concept of the entire chapter
- Cross-reference status: verified
