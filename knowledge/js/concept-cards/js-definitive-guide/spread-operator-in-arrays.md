---
# === CORE IDENTIFICATION ===
concept: Spread Operator in Arrays
slug: spread-operator-in-arrays

# === CLASSIFICATION ===
category: arrays
subcategory: array creation
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 174
section: "7.1.2 The Spread Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "spread syntax"
  - "three-dot syntax in arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-literals
extends: []
related:
  - spread-in-function-calls
  - rest-parameters
contrasts_with:
  - rest-parameters

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I merge or copy arrays in JavaScript?"
---

# Quick Definition

The spread operator (`...`) within an array literal expands an iterable object's elements into individual elements of the enclosing array.

# Core Definition

"In ES6 and later, you can use the 'spread operator,' `...`, to include the elements of one array within an array literal." The spread operator works on any iterable object (not just arrays) and creates a shallow copy. It "is not a true operator because it can only be used in array literals and function invocations." (Flanagan, p. 174)

# Prerequisites

- **array-literals** — Spread is used within array literal syntax

# Key Properties

1. Uses the `...` syntax before an iterable
2. Works on any iterable object (arrays, strings, Sets, etc.)
3. Creates a shallow copy of elements
4. Can be used to deduplicate via `[...new Set(array)]`

# Construction / Recognition

```javascript
let a = [1, 2, 3];
let b = [0, ...a, 4];  // b == [0, 1, 2, 3, 4]
let copy = [...original];  // shallow copy
let chars = [..."hello"];  // ["h","e","l","l","o"]
```

# Context & Application

Used to copy arrays, merge arrays, convert iterables to arrays, and remove duplicates (with Set).

# Examples

```javascript
let a = [1, 2, 3];
let b = [0, ...a, 4];  // b == [0, 1, 2, 3, 4]

let original = [1,2,3];
let copy = [...original];
copy[0] = 0;
original[0]  // => 1  (copy does not affect original)

let letters = [..."hello world"];
[...new Set(letters)]  // => ["h","e","l","o"," ","w","r","d"]
```
(Flanagan, p. 174)

# Relationships

## Builds Upon
- **array-literals** — Spread is used within array literal syntax

## Enables
- **spread-in-function-calls** — Same syntax used in function calls

## Related
- **rest-parameters** — Same `...` syntax but opposite effect (gathers vs. spreads)

## Contrasts With
- **rest-parameters** — Spread expands; rest gathers

# Common Errors

- **Error**: Expecting spread to create a deep copy of nested arrays/objects.
  **Correction**: Spread creates only a shallow copy; nested references are shared.

# Common Confusions

- **Confusion**: The `...` is a general-purpose operator.
  **Clarification**: It is special syntax that can only be used in array literals and function invocations, not as a standalone operator.

# Source Reference

Chapter 7: Arrays, Section 7.1.2, page 174.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly explained with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
