---
# === CORE IDENTIFICATION ===
concept: splice() Method
slug: splice-method

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
  - slice-method
  - push-pop-shift-unshift
contrasts_with:
  - slice-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes splice() from slice()?"
  - "How do I insert or remove elements from the middle of an array?"
---

# Quick Definition

`splice()` is a general-purpose method that modifies an array in place by removing and/or inserting elements at a specified position, returning an array of the removed elements.

# Core Definition

"splice() is a general-purpose method for inserting or removing elements from an array. Unlike slice() and concat(), splice() modifies the array on which it is invoked." The first argument is the start position; the second is the number of elements to delete; additional arguments are elements to insert at that position. It "returns an array of the deleted elements, or an empty array if no elements were deleted." (Flanagan, p. 189-190)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Mutates the array in place
2. First arg: start position
3. Second arg: count of elements to delete (not end position!)
4. Additional args: elements to insert at that position
5. Returns array of deleted elements
6. Shifts remaining elements to maintain contiguity
7. Does not flatten array arguments (unlike concat)

# Construction / Recognition

```javascript
array.splice(start, deleteCount, ...items);
```

# Context & Application

The most versatile array mutation method. Handles insertion, deletion, and replacement in a single call.

# Examples

```javascript
let a = [1,2,3,4,5,6,7,8];
a.splice(4)           // => [5,6,7,8]; a is now [1,2,3,4]
a.splice(1,2)         // => [2,3]; a is now [1,4]
a.splice(1,1)         // => [4]; a is now [1]

let a = [1,2,3,4,5];
a.splice(2,0,"a","b") // => []; a is now [1,2,"a","b",3,4,5]
a.splice(2,2,[1,2],3) // => ["a","b"]; a is now [1,2,[1,2],3,3,4,5]
```
(Flanagan, p. 189-190)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype

## Enables
- In-place array modification (insert, delete, replace)

## Related
- **push-pop-shift-unshift** — Simpler add/remove at ends

## Contrasts With
- **slice-method** — slice does not mutate and its second arg is end position; splice mutates and its second arg is delete count

# Common Errors

- **Error**: Confusing splice()'s second argument (count) with slice()'s second argument (end position).
  **Correction**: splice(start, count) deletes `count` elements; slice(start, end) extracts up to (not including) `end`.

# Common Confusions

- **Confusion**: splice() flattens array arguments.
  **Clarification**: Unlike concat(), splice() inserts arrays as single elements.

# Source Reference

Chapter 7: Arrays, Section 7.8.5, pages 189-190.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with examples
- Uncertainties: None
- Cross-reference status: Verified
