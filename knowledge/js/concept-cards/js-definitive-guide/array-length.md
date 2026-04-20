---
# === CORE IDENTIFICATION ===
concept: Array Length Property
slug: array-length

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
pdf_page: 178
section: "7.4 Array Length"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - sparse-arrays
  - reading-writing-array-elements
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the length property of a JavaScript array work?"
---

# Quick Definition

Every array has a `length` property that is automatically maintained: it is always one more than the highest index. Setting `length` to a smaller value truncates the array.

# Core Definition

"Every array has a length property, and it is this property that makes arrays different from regular JavaScript objects." For dense arrays, length equals the number of elements. For sparse arrays, length is greater than the element count. Two special behaviors maintain the invariant: assigning to an index >= length updates length to index+1; setting length to a smaller value deletes elements at indexes >= the new length. (Flanagan, p. 178)

# Prerequisites

- **array-fundamentals** — Must understand basic array structure

# Key Properties

1. Always one more than the highest index
2. Automatically updated when elements are added
3. Setting to a smaller value truncates (deletes elements)
4. Setting to a larger value creates sparse area (no new elements added)

# Construction / Recognition

```javascript
[].length              // => 0
["a","b","c"].length   // => 3

a = [1,2,3,4,5];
a.length = 3;          // a is now [1,2,3]
a.length = 0;          // Delete all elements
a.length = 5;          // Length 5, but no elements (sparse)
```

# Context & Application

The length property is fundamental to array iteration and manipulation. Understanding its auto-update and truncation behavior is essential.

# Examples

```javascript
a = [1,2,3,4,5];
a.length = 3;   // a is now [1,2,3]
a.length = 0;   // Delete all elements. a is [].
a.length = 5;   // Length is 5, but no elements, like new Array(5)
```
(Flanagan, p. 178)

# Relationships

## Builds Upon
- **array-fundamentals** — Length is the defining feature that distinguishes arrays from objects

## Enables
- **array-iteration** — Loops use length to determine bounds
- **push-pop-shift-unshift** — These methods modify length

## Related
- **sparse-arrays** — Length may be greater than element count in sparse arrays

## Contrasts With
- None specific

# Common Errors

- **Error**: Setting `a.length = 5` expecting it to create 5 elements.
  **Correction**: It creates a sparse region; no elements are actually added.

# Common Confusions

- **Confusion**: Length always equals the number of elements.
  **Clarification**: Only true for dense arrays. For sparse arrays, length can be much larger.

# Source Reference

Chapter 7: Arrays, Section 7.4, page 178.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated with examples
- Uncertainties: None
- Cross-reference status: Verified
