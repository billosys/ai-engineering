---
# === CORE IDENTIFICATION ===
concept: Sparse Arrays
slug: sparse-arrays

# === CLASSIFICATION ===
category: arrays
subcategory: array structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 177
section: "7.3 Sparse Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - reading-writing-array-elements
extends: []
related:
  - array-length
  - array-literals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when JavaScript arrays have gaps?"
---

# Quick Definition

A sparse array is one in which elements do not have contiguous indexes starting at 0, so the `length` property is greater than the actual number of elements.

# Core Definition

"A sparse array is one in which the elements do not have contiguous indexes starting at 0. Normally, the length property of an array specifies the number of elements in the array. If the array is sparse, the value of the length property is greater than the number of elements." Sparse arrays can be created with the Array() constructor, by assigning to an index beyond current length, with the `delete` operator, or via omitted values in array literals. (Flanagan, p. 177-178)

# Prerequisites

- **array-fundamentals** — Understanding of basic array structure
- **reading-writing-array-elements** — How elements are stored

# Key Properties

1. `length` is greater than the number of defined elements
2. Nonexistent elements return `undefined` when queried
3. Nonexistent elements differ from elements explicitly set to `undefined`
4. The `in` operator distinguishes existing-but-undefined from nonexistent
5. Sparse arrays are typically slower and more memory-efficient than dense arrays

# Construction / Recognition

```javascript
let a = new Array(5);     // length 5, no elements
let b = [];  b[1000] = 0; // length 1001, one element
let c = [1,,3];            // sparse from literal
```

# Context & Application

Most practical JavaScript arrays are dense. Sparse arrays are important to understand but rarely intentionally created.

# Examples

```javascript
let a1 = [,];           // No elements, length 1
let a2 = [undefined];   // One undefined element
0 in a1                 // => false: a1 has no element at index 0
0 in a2                 // => true: a2 has the undefined value at index 0
```
(Flanagan, p. 178)

# Relationships

## Builds Upon
- **array-fundamentals** — Sparse arrays are a feature of JavaScript's array model
- **reading-writing-array-elements** — Gaps in indexes create sparseness

## Enables
- Understanding iterator behavior (forEach skips gaps; for/of returns undefined)

## Related
- **array-length** — Length is always greater than the highest index

## Contrasts With
- None specific (dense arrays are the default/normal case)

# Common Errors

- **Error**: Treating omitted array literal values as `undefined` elements.
  **Correction**: Omitted values create truly nonexistent elements; `0 in [,]` is `false`.

# Common Confusions

- **Confusion**: `[1,,3]` and `[1, undefined, 3]` are the same.
  **Clarification**: The first is sparse (no element at index 1); the second has an explicit `undefined` element at index 1. The `in` operator reveals the difference.

# Source Reference

Chapter 7: Arrays, Section 7.3, pages 177-178.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-explained with demonstrative examples
- Uncertainties: None
- Cross-reference status: Verified
