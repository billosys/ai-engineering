---
# === CORE IDENTIFICATION ===
concept: Reading and Writing Array Elements
slug: reading-writing-array-elements

# === CLASSIFICATION ===
category: arrays
subcategory: array access
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 176
section: "7.2 Reading and Writing Array Elements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "array element access"
  - "bracket notation for arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - array-length
  - sparse-arrays
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I access elements in a JavaScript array?"
---

# Quick Definition

Array elements are accessed using the `[]` operator with a nonnegative integer index, for both reading and writing. Accessing a nonexistent index returns `undefined` rather than throwing an error.

# Core Definition

"You access an element of an array using the [] operator." JavaScript "converts the numeric array index you specify to a string -- the index 1 becomes the string '1' -- then uses that string as a property name." Only property names that are nonnegative integers between 0 and 2^32-2 are true array indexes that affect the `length` property. Accessing a nonexistent index returns `undefined` with no "out of bounds" error. (Flanagan, p. 176-177)

# Prerequisites

- **array-fundamentals** — Must understand arrays as specialized objects

# Key Properties

1. `[]` operator for both reading and writing
2. Indexes are converted to strings internally
3. True array indexes (0 to 2^32-2) update the `length` property
4. Non-integer or negative indexes are treated as regular object properties
5. No "out of bounds" error; nonexistent elements return `undefined`

# Construction / Recognition

```javascript
let a = ["world"];
let value = a[0];       // Read element 0
a[1] = 3.14;            // Write element 1
a[a.length] = "new";    // Append to end
```

# Context & Application

Fundamental operation for working with arrays. Understanding that indexes are property names is key to understanding JavaScript arrays deeply.

# Examples

```javascript
let a = ["world"];
let value = a[0];      // Read element 0
a[1] = 3.14;           // Write element 1
let i = 2;
a[i] = 3;             // Write element 2
a[i + 1] = "hello";   // Write element 3
a.length               // => 4

a[-1.23] = true;       // Creates property named "-1.23" (not an index)
a["1000"] = 0;         // This is the 1001st element of the array
a[1.000] = 1;          // Same as a[1] = 1
```
(Flanagan, p. 176-177)

# Relationships

## Builds Upon
- **array-fundamentals** — Element access is the core array operation

## Enables
- **array-length** — Writing elements affects the length property

## Related
- **sparse-arrays** — Accessing gaps returns undefined

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting an "index out of bounds" error when accessing beyond the array.
  **Correction**: JavaScript simply returns `undefined` for nonexistent indexes.

# Common Confusions

- **Confusion**: Array indexes and object property names are different things.
  **Clarification**: Array indexes are just a special kind of property name (nonnegative integers < 2^32-1 that automatically update `length`).

# Source Reference

Chapter 7: Arrays, Section 7.2, pages 176-177.

# Verification Notes

- Definition source: Direct quote and synthesis from source text
- Confidence rationale: Clearly explained fundamental concept
- Uncertainties: None
- Cross-reference status: Verified
