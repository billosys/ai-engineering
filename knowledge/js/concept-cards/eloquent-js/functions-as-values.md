---
# === CORE IDENTIFICATION ===
concept: Functions as Values
slug: functions-as-values

# === CLASSIFICATION ===
category: functions
subcategory: core-concepts
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Functions as values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - first-class functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - binding
  - value
extends: []
related:
  - higher-order-function
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
  - "What must I know before understanding higher-order functions?"
---

# Quick Definition

In JavaScript, a function value can do all the things that other values can do -- it can be stored in bindings, passed as an argument, and returned from other functions.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 223-228 of 03-functions.md): "A function value can do all the things that other values can do -- you can use it in arbitrary expressions, not just call it. It is possible to store a function value in a new binding, pass it as an argument to a function, and so on. Similarly, a binding that holds a function is still just a regular binding and can, if not constant, be assigned a new value."

# Prerequisites

- **function-definition**: Functions are the values being discussed.
- **binding**: Functions are stored in bindings.
- **value**: Functions are first-class values.

# Key Properties

1. Functions can be stored in bindings (variables).
2. Functions can be passed as arguments to other functions.
3. Functions can be returned from other functions.
4. A binding holding a function can be reassigned (if not `const`).
5. The function and its name (binding) are separate things.

# Construction / Recognition

## To Construct/Create:
```javascript
let launchMissiles = function() {
  missileSystem.launch("now");
};
if (safeMode) {
  launchMissiles = function() {/* do nothing */};
}
```

## To Identify/Recognize:
- A function being assigned to a variable, passed as an argument, or returned from another function.

# Context & Application

This concept is foundational to JavaScript's functional programming capabilities. It makes higher-order functions, callbacks, and closures possible. Chapter 5 builds entirely on this principle.

# Examples

**Example 1** (Ch 3, lines 231-238 of 03-functions.md):
```javascript
let launchMissiles = function() {
  missileSystem.launch("now");
};
if (safeMode) {
  launchMissiles = function() {/* do nothing */};
}
```

# Relationships

## Builds Upon
- **function-definition** -- Functions are the values.
- **value** -- Functions behave like other values.

## Enables
- **higher-order-function** -- Passing/returning functions.
- **closure** -- Returning functions that capture bindings.

## Related
- **binding** -- Functions are held in bindings.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Confusing calling a function (`f()`) with referencing it (`f`).
  **Correction**: `f` is the function value; `f()` invokes it and produces its return value.

# Common Confusions

- **Confusion**: Functions are fundamentally different from other values.
  **Clarification**: "Since we have already seen that functions are regular values, there is nothing particularly remarkable about the fact that such functions exist" (Ch 5, line 219).

# Source Reference

Chapter 3: Functions, Section "Functions as values", lines 214-243 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 223-228)
- Confidence rationale: Explicit section on functions as values
- Cross-reference status: verified against Ch 5 higher-order functions
