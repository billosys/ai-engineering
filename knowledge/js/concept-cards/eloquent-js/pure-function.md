---
# === CORE IDENTIFICATION ===
concept: Pure Function
slug: pure-function

# === CLASSIFICATION ===
category: functions
subcategory: function-design
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Functions and side effects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - return-value
  - side-effects
extends: []
related:
  - higher-order-function
contrasts_with:
  - side-effects

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
---

# Quick Definition

A pure function is a value-producing function that has no side effects and does not rely on side effects from other code, always producing the same value for the same arguments.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 3, lines 902-912 of 03-functions.md): "A *pure* function is a specific kind of value-producing function that not only has no side effects but also doesn't rely on side effects from other code -- for example, it doesn't read global bindings whose value might change. A pure function has the pleasant property that, when called with the same arguments, it always produces the same value (and doesn't do anything else). A call to such a function can be substituted by its return value without changing the meaning of the code."

# Prerequisites

- **function-definition**: Pure functions are functions.
- **return-value**: Pure functions produce values.
- **side-effects**: Purity is defined by the absence of side effects.

# Key Properties

1. Has **no side effects** (does not modify external state).
2. Does **not rely** on external mutable state.
3. Given the same arguments, **always returns the same value**.
4. A call can be **substituted by its return value** without changing program behavior.
5. Easier to test: "you can test it by simply calling it and know that if it works in that context, it will work in any context."

# Construction / Recognition

## To Construct/Create:
```javascript
function zeroPad(number, width) {
  let string = String(number);
  while (string.length < width) {
    string = "0" + string;
  }
  return string;
}
```

## To Identify/Recognize:
- No `console.log`, no modification of external bindings, no I/O.
- Same inputs always yield same output.

# Context & Application

Pure functions are more reusable and testable than impure ones. The `zeroPad` function (a pure function) is "useful in more situations" than `printZeroPaddedWithLabel` (a side-effect function). Pure functions are central to functional programming patterns in Ch 5.

# Examples

**Example 1** (Ch 3, lines 844-851 of 03-functions.md):
```javascript
function zeroPad(number, width) {
  let string = String(number);
  while (string.length < width) {
    string = "0" + string;
  }
  return string;
}
```

# Relationships

## Builds Upon
- **return-value** -- Pure functions produce values.
- **side-effects** -- Defined by their absence.

## Enables
- **higher-order-function** -- Pure functions compose well in higher-order patterns.
- Easier testing, reasoning, and composition.

## Related
- **array-filter** -- The `filter` function in Ch 5 is described as "pure."

## Contrasts With
- **side-effects** -- Impure functions have side effects.

# Common Errors

- **Error**: Thinking every function must be pure.
  **Correction**: "There's no need to feel bad when writing functions that are not pure. Side effects are often useful."

# Common Confusions

- **Confusion**: Pure functions cannot use variables inside their body.
  **Clarification**: Pure functions can use local variables. They just cannot read or modify external mutable state.

# Source Reference

Chapter 3: Functions, Section "Functions and side effects", lines 902-919 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 902-912)
- Confidence rationale: Explicit definition with italicized term "pure"
- Cross-reference status: verified within chapter
