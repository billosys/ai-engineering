---
# === CORE IDENTIFICATION ===
concept: Array Literals
slug: array-literals

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
pdf_page: 172
section: "7.1.1 Array Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "array literal syntax"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - spread-operator-in-arrays
  - sparse-arrays
contrasts_with:
  - array-constructor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create arrays in JavaScript?"
---

# Quick Definition

An array literal is a comma-separated list of values within square brackets, representing the simplest way to create an array in JavaScript.

# Core Definition

"By far the simplest way to create an array is with an array literal, which is simply a comma-separated list of array elements within square brackets." Values need not be constants; they may be arbitrary expressions, and can include object literals or other array literals. An optional trailing comma is allowed. Multiple consecutive commas create a sparse array. (Flanagan, p. 172-173)

# Prerequisites

- **array-fundamentals** — Must understand what arrays are

# Key Properties

1. Values enclosed in square brackets `[]`
2. Elements separated by commas
3. Values can be arbitrary expressions, not just constants
4. Trailing comma is permitted
5. Consecutive commas create sparse arrays (missing elements)

# Construction / Recognition

```javascript
let empty = [];
let primes = [2, 3, 5, 7, 11];
let misc = [1.1, true, "a",];  // trailing comma OK
let nested = [[1, {x: 1}], [2, {x: 3}]];
let sparse = [1,,3];  // sparse: no element at index 1
```

# Context & Application

Array literals are the most common way to create arrays in JavaScript code. They are preferred over the Array() constructor for clarity and simplicity.

# Examples

```javascript
let base = 1024;
let table = [base, base+1, base+2, base+3];  // expressions as values
let count = [1,,3];  // Elements at indexes 0 and 2. No element at index 1
let undefs = [,,];   // An array with no elements but a length of 2
```
(Flanagan, p. 172-173)

# Relationships

## Builds Upon
- **array-fundamentals** — Array literals create array instances

## Enables
- **spread-operator-in-arrays** — Spread can be used within array literals
- **sparse-arrays** — Consecutive commas in literals create sparse arrays

## Related
- **array-constructor** — Alternative way to create arrays

## Contrasts With
- **array-constructor** — Literals are simpler and preferred over the constructor

# Common Errors

- **Error**: Assuming `[,,]` has a length of 3.
  **Correction**: Array literal syntax allows a trailing comma, so `[,,]` has a length of 2, not 3.

# Common Confusions

- **Confusion**: Omitted values in array literals create `undefined` elements.
  **Clarification**: Omitted values create truly nonexistent elements (sparse), not `undefined` values. The array is sparse and the elements do not exist.

# Source Reference

Chapter 7: Arrays, Section 7.1.1, pages 172-173.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
