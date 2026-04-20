---
# === CORE IDENTIFICATION ===
concept: Optional Arguments
slug: optional-arguments

# === CLASSIFICATION ===
category: functions
subcategory: function-inputs
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Optional Arguments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - flexible arguments
  - argument flexibility

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parameters
  - function-definition
extends: []
related:
  - default-parameters
  - rest-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
---

# Quick Definition

JavaScript is extremely flexible about the number of arguments passed to a function: extra arguments are ignored, and missing parameters are assigned the value `undefined`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 431-434 of 03-functions.md): "JavaScript is extremely broad-minded about the number of arguments you can pass to a function. If you pass too many, the extra ones are ignored. If you pass too few, the missing parameters are assigned the value `undefined`."

# Prerequisites

- **parameters**: Understanding function parameters and how they receive values.
- **function-definition**: Arguments are passed when calling functions.

# Key Properties

1. Passing **too many** arguments: extras are silently ignored.
2. Passing **too few** arguments: missing parameters are `undefined`.
3. No error is thrown for mismatched argument counts.
4. This enables functions that accept different numbers of arguments.

# Construction / Recognition

## To Construct/Create:
```javascript
function minus(a, b) {
  if (b === undefined) return -a;
  else return a - b;
}
console.log(minus(10));    // → -10
console.log(minus(10, 5)); // → 5
```

## To Identify/Recognize:
- A function called with more or fewer arguments than its parameter list.

# Context & Application

This feature enables flexible APIs where some parameters are optional. However, it can also mask bugs -- accidentally passing the wrong number of arguments produces no error.

# Examples

**Example 1** (Ch 3, lines 418-422 of 03-functions.md):
```javascript
function square(x) { return x * x; }
console.log(square(4, true, "hedgehog"));
// → 16
```

**Example 2** (Ch 3, lines 446-455 of 03-functions.md):
```javascript
function minus(a, b) {
  if (b === undefined) return -a;
  else return a - b;
}
console.log(minus(10));
// → -10
console.log(minus(10, 5));
// → 5
```

# Relationships

## Builds Upon
- **parameters** -- Optional arguments are about flexible parameter handling.

## Enables
- **default-parameters** -- A cleaner way to handle optional arguments.

## Related
- **rest-parameters** -- Another way to handle variable numbers of arguments.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Accidentally passing the wrong number of arguments and getting no error.
  **Correction**: "The downside of this is that it is possible -- likely, even -- that you'll accidentally pass the wrong number of arguments to functions. And no one will tell you about it."

# Common Confusions

- **Confusion**: JavaScript will throw an error for wrong argument counts like some other languages.
  **Clarification**: JavaScript silently ignores extra arguments and assigns `undefined` to missing ones.

# Source Reference

Chapter 3: Functions, Section "Optional Arguments", lines 412-487 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 431-434)
- Confidence rationale: Explicit section dedicated to topic
- Cross-reference status: verified within chapter
