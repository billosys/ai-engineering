---
# === CORE IDENTIFICATION ===
concept: Growing Functions
slug: growing-functions

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
section: "Growing functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - function design
  - refactoring into functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - parameters
  - return-value
extends: []
related:
  - pure-function
  - side-effects
  - abstraction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
---

# Quick Definition

Functions are introduced into programs in two ways: noticing repeated code and extracting it, or identifying a needed concept and naming it as a function. Good function design isolates a single concept with a clear name.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 742-758 of 03-functions.md): "There are two more or less natural ways for functions to be introduced into programs. The first occurs when you find yourself writing similar code multiple times... The second way is that you find you need some functionality that you haven't written yet and that sounds like it deserves its own function."

Further (lines 761-763): "How difficult it is to find a good name for a function is a good indication of how clear a concept it is that you're trying to wrap."

# Prerequisites

- **function-definition**: This is about how to design functions.
- **parameters**: Good function design involves choosing the right parameters.
- **return-value**: Pure return-value functions are more reusable.

# Key Properties

1. Extract repeated code into functions.
2. Name functions based on single, clear concepts.
3. "A useful principle is to refrain from adding cleverness unless you are absolutely sure you're going to need it" (line 879).
4. Functions that return values are more reusable than side-effect functions.

# Construction / Recognition

## To Construct/Create:
The chapter shows evolution from `printZeroPaddedWithLabel` (conflates three things) to `zeroPad` (isolates one concept):
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
- Functions with clear, single-purpose names.
- Functions that return values rather than performing side effects directly.

# Context & Application

Understanding function design principles is essential for writing maintainable code. This section teaches the art of creating well-scoped, reusable functions.

# Examples

**Example 1** (Ch 3, lines 815-860 of 03-functions.md) -- evolution:
First attempt conflates concerns:
```javascript
function printZeroPaddedWithLabel(number, label) {
  let numberString = String(number);
  while (numberString.length < 3) { numberString = "0" + numberString; }
  console.log(`${numberString} ${label}`);
}
```
Better version isolates a single concept:
```javascript
function zeroPad(number, width) {
  let string = String(number);
  while (string.length < width) { string = "0" + string; }
  return string;
}
```

# Relationships

## Builds Upon
- **function-definition** -- About designing functions well.

## Enables
- **pure-function** -- Well-designed functions tend to be pure.
- **abstraction** -- Good functions create meaningful abstractions.

## Related
- **side-effects** -- The section contrasts side-effect and return-value functions.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Creating overly clever, general "framework" functions.
  **Correction**: "Resist that urge. You won't get any real work done -- you'll be too busy writing code that you never use."

# Common Confusions

- **Confusion**: Functions should always be as general as possible.
  **Clarification**: Functions should be as general as they need to be, not more. Over-generalization adds complexity without benefit.

# Source Reference

Chapter 3: Functions, Section "Growing functions", lines 739-883 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: synthesized from lines 742-863
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified within chapter
