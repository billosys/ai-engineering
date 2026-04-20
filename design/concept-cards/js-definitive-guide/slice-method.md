---
# === CORE IDENTIFICATION ===
concept: slice() Method
slug: slice-method

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 189
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
contrasts_with:
  - splice-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes splice() from slice()?"
---

# Quick Definition

`slice()` returns a new array containing a subarray (slice) from start index up to but not including end index, without modifying the original array.

# Core Definition

"The slice() method returns a slice, or subarray, of the specified array. Its two arguments specify the start and end of the slice to be returned. The returned array contains the element specified by the first argument and all subsequent elements up to, but not including, the element specified by the second argument." Negative arguments are relative to array length. "slice() does not modify the array on which it is invoked." (Flanagan, p. 189)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Returns new array (does not mutate)
2. First argument: start index (inclusive)
3. Second argument: end index (exclusive)
4. One argument: returns from that index to end
5. Negative arguments count from end (-1 = last element)

# Construction / Recognition

```javascript
let sub = array.slice(start, end);
let rest = array.slice(start);
let copy = array.slice();
```

# Context & Application

Used for extracting subarrays, copying arrays, and taking portions of data. A common idiom for shallow copying.

# Examples

```javascript
let a = [1,2,3,4,5];
a.slice(0,3);    // Returns [1,2,3]
a.slice(3);      // Returns [4,5]
a.slice(1,-1);   // Returns [2,3,4]
a.slice(-3,-2);  // Returns [3]
```
(Flanagan, p. 189)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype

## Enables
- Non-destructive subarray extraction

## Related
- **splice-method** — Similar name but very different operation

## Contrasts With
- **splice-method** — slice does not mutate; splice does. slice's second arg is end position; splice's is count.

# Common Errors

- **Error**: Confusing slice() with splice() due to similar names.
  **Correction**: slice() extracts without modifying; splice() inserts/removes and mutates the array.

# Common Confusions

- **Confusion**: The second argument to slice() is a count.
  **Clarification**: The second argument to slice() is an end position (exclusive), not a count. Compare with splice(), where the second argument is a count.

# Source Reference

Chapter 7: Arrays, Section 7.8.5, page 189.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
