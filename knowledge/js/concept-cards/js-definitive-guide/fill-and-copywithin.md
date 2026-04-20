---
# === CORE IDENTIFICATION ===
concept: fill() and copyWithin()
slug: fill-and-copywithin

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 190
section: "7.8.5 Subarrays with slice(), splice(), fill(), and copyWithin()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - splice-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I fill an array with a specific value?"
---

# Quick Definition

`fill()` sets elements of an array (or a slice) to a specified value in place. `copyWithin()` copies a slice of the array to another position within the same array, also in place.

# Core Definition

"The fill() method sets the elements of an array, or a slice of an array, to a specified value. It mutates the array it is called on, and also returns the modified array." fill(value, start, end) fills from start up to but not including end. "copyWithin() copies a slice of an array to a new position within the array. It modifies the array in place and returns the modified array, but it will not change the length of the array." (Flanagan, p. 190-191)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Both mutate the array in place and return the modified array
2. fill(value, start, end): fills from start up to (not including) end
3. copyWithin(dest, srcStart, srcEnd): copies elements within the array
4. Both support negative indexes (relative to end)
5. copyWithin works correctly even with overlapping source/destination

# Construction / Recognition

```javascript
array.fill(value, start, end);
array.copyWithin(destIndex, srcStart, srcEnd);
```

# Context & Application

fill() is useful for initializing arrays. copyWithin() is a high-performance method particularly useful with typed arrays.

# Examples

```javascript
let a = new Array(5);
a.fill(0)          // => [0,0,0,0,0]
a.fill(9, 1)       // => [0,9,9,9,9]
a.fill(8, 2, -1)   // => [0,9,8,8,9]

let a = [1,2,3,4,5];
a.copyWithin(1)        // => [1,1,2,3,4]
a.copyWithin(2, 3, 5)  // => [1,1,3,4,4]
a.copyWithin(0, -2)    // => [4,4,3,4,4]
```
(Flanagan, p. 190-191)

# Relationships

## Builds Upon
- **array-fundamentals** — Methods of Array.prototype

## Enables
- Efficient array initialization and in-place manipulation

## Related
- **splice-method** — Another in-place mutation method

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting fill() to return a new array.
  **Correction**: fill() mutates and returns the same array.

# Common Confusions

- **Confusion**: copyWithin() changes the array's length.
  **Clarification**: copyWithin() never changes the length; it only overwrites existing elements.

# Source Reference

Chapter 7: Arrays, Section 7.8.5, pages 190-191.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
