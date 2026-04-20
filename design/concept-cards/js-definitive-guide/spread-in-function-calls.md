---
# === CORE IDENTIFICATION ===
concept: Spread Operator in Function Calls
slug: spread-in-function-calls

# === CLASSIFICATION ===
category: functions
subcategory: invocation
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 213
section: "8.3.4 The Spread Operator for Function Calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "spread arguments"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - spread-operator-in-arrays
extends: []
related:
  - rest-parameters
contrasts_with:
  - rest-parameters

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I pass array elements as individual function arguments?"
---

# Quick Definition

The spread operator `...` in a function call expands an iterable into individual arguments, the inverse of rest parameters which gather arguments into an array.

# Core Definition

"The spread operator ... is used to unpack, or 'spread out,' the elements of an array (or any other iterable object) in a context where individual values are expected." In function calls, it "is not a true operator in the sense that it cannot be evaluated to produce a value. Instead, it is a special JavaScript syntax." (Flanagan, p. 213)

# Prerequisites

- **function-declarations** — Must understand function calls
- **spread-operator-in-arrays** — Same syntax used in array literals

# Key Properties

1. Expands iterable elements into individual arguments
2. Works with any iterable (arrays, strings, etc.)
3. Can be combined with rest parameters for argument forwarding
4. Not a true operator; special syntax for function calls and array literals

# Construction / Recognition

```javascript
let numbers = [5, 2, 10, -1, 9, 100, 1];
Math.min(...numbers)  // => -1
f(...args)            // spread array into individual arguments
```

# Context & Application

Use to pass array elements as individual arguments. Commonly used with Math.min/max and for argument forwarding in wrapper functions.

# Examples

```javascript
let numbers = [5, 2, 10, -1, 9, 100, 1];
Math.min(...numbers)  // => -1

// Argument forwarding with rest + spread:
function timed(f) {
    return function(...args) {
        let startTime = Date.now();
        try { return f(...args); }
        finally { console.log(`${Date.now()-startTime}ms`); }
    };
}
```
(Flanagan, p. 213-214)

# Relationships

## Builds Upon
- **function-declarations** — Used in function calls
- **spread-operator-in-arrays** — Same syntax in different context

## Enables
- Argument forwarding patterns

## Related
- **rest-parameters** — Same `...` syntax, opposite direction

## Contrasts With
- **rest-parameters** — Spread expands; rest gathers

# Common Errors

- **Error**: Using spread with non-iterable values.
  **Correction**: Spread requires iterables. Plain objects are not iterable.

# Common Confusions

- **Confusion**: Spread and rest parameters are the same feature.
  **Clarification**: Spread (in calls) unpacks iterables into arguments; rest (in definitions) gathers arguments into an array.

# Source Reference

Chapter 8: Functions, Section 8.3.4, pages 213-214.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
