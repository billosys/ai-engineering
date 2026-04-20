---
# === CORE IDENTIFICATION ===
concept: sort() and reverse()
slug: sort-and-reverse

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
pdf_page: 192
section: "7.8.6 Array Searching and Sorting Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - functions-as-values
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I sort an array in JavaScript?"
---

# Quick Definition

`sort()` sorts array elements in place (alphabetically by default, or by a custom comparator function) and returns the sorted array. `reverse()` reverses element order in place.

# Core Definition

"sort() sorts the elements of an array in place and returns the sorted array. When sort() is called with no arguments, it sorts the array elements in alphabetical order (temporarily converting them to strings)." A comparison function can be passed that returns negative, zero, or positive to control ordering. "The reverse() method reverses the order of the elements of an array and returns the reversed array. It does this in place." (Flanagan, p. 192-193)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Both mutate the array in place and return the same array
2. sort() without arguments sorts alphabetically (as strings)
3. Comparison function: return < 0 for a before b, > 0 for b before a, 0 for equal
4. undefined elements are sorted to the end
5. reverse() simply reverses element order

# Construction / Recognition

```javascript
array.sort();
array.sort((a, b) => a - b);  // numeric ascending
array.reverse();
```

# Context & Application

sort() is essential for ordering data. The comparison function pattern demonstrates functions as values.

# Examples

```javascript
let a = [33, 4, 1111, 222];
a.sort();                     // [1111, 222, 33, 4]; alphabetical!
a.sort((a,b) => a-b);        // [4, 33, 222, 1111]; numerical
a.sort((a,b) => b-a);        // [1111, 222, 33, 4]; reverse numerical

// Case-insensitive sort:
let a = ["ant", "Bug", "cat", "Dog"];
a.sort((s,t) => {
    let a = s.toLowerCase(), b = t.toLowerCase();
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
});  // ["ant","Bug","cat","Dog"]

let a = [1,2,3];
a.reverse();  // a == [3,2,1]
```
(Flanagan, p. 192-193)

# Relationships

## Builds Upon
- **array-fundamentals** — Methods of Array.prototype

## Enables
- Ordered data presentation

## Related
- **functions-as-values** — Comparison functions demonstrate functions as arguments

## Contrasts With
- None specific

# Common Errors

- **Error**: Sorting numbers without a comparison function, expecting numerical order.
  **Correction**: Default sort converts to strings, so `[33, 4, 1111]` sorts as `[1111, 33, 4]`. Use `sort((a,b) => a-b)` for numerical sorting.

# Common Confusions

- **Confusion**: sort() returns a new sorted array.
  **Clarification**: sort() mutates in place and returns the same (now sorted) array.

# Source Reference

Chapter 7: Arrays, Section 7.8.6, pages 192-193.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with examples
- Uncertainties: None
- Cross-reference status: Verified
