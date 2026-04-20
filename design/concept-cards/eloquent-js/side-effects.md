---
# === CORE IDENTIFICATION ===
concept: Side Effects
slug: side-effects

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
aliases:
  - function side effects
  - impure functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - return-value
extends: []
related:
  - pure-function
contrasts_with:
  - pure-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
---

# Quick Definition

Side effects are observable actions a function performs other than returning a value, such as printing to the screen, modifying external state, or writing to a file.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 888-891 of 03-functions.md): "Functions can be roughly divided into those that are called for their side effects and those that are called for their return value (though it is also possible to both have side effects and return a value)." Functions that create values are "easier to combine in new ways than functions that directly perform side effects" (lines 898-899).

# Prerequisites

- **function-definition**: Side effects are a property of function behavior.
- **return-value**: Side effects contrast with pure return-value computation.

# Key Properties

1. Side effects include printing, modifying variables outside the function, writing to files, etc.
2. Functions can be called for side effects, for return values, or both.
3. Functions that produce return values are easier to combine and reuse.
4. Side effects are sometimes necessary (`console.log` is a side effect).

# Construction / Recognition

## To Construct/Create:
```javascript
const makeNoise = function() {
  console.log("Pling!"); // side effect
};
```

## To Identify/Recognize:
- A function that changes something observable outside itself (prints, modifies a global variable, etc.).

# Context & Application

Understanding the distinction between side effects and return values helps in writing more modular, testable code. Pure functions (no side effects) are easier to test and reuse, but side effects are unavoidable for I/O.

# Examples

**Example 1** (Ch 3, lines 893-899 of 03-functions.md):
The `printZeroPaddedWithLabel` function is called for its side effect (printing). The `zeroPad` function is called for its return value. "It is no coincidence that the second is useful in more situations than the first."

# Relationships

## Builds Upon
- **function-definition** -- Side effects are an aspect of function behavior.
- **return-value** -- The alternative to side effects.

## Enables
- Understanding of pure vs impure function design.

## Related
- **pure-function** -- Functions without side effects.

## Contrasts With
- **pure-function** -- Pure functions have no side effects.

# Common Errors

- **Error**: Treating a side-effect-only function's return value as meaningful.
  **Correction**: Functions like `console.log` return `undefined`; their purpose is the side effect.

# Common Confusions

- **Confusion**: Side effects are always bad.
  **Clarification**: "There's no need to feel bad when writing functions that are not pure. Side effects are often useful."

# Source Reference

Chapter 3: Functions, Section "Functions and side effects", lines 885-919 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: synthesized from lines 888-899
- Confidence rationale: Explicit section dedicated to topic
- Cross-reference status: verified within chapter
