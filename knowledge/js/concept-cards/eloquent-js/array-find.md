---
# === CORE IDENTIFICATION ===
concept: Array find
slug: array-find

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: array-methods
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Recognizing text"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - find
  - Array.prototype.find

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - higher-order-function
  - predicate-function
extends:
  - higher-order-function
related:
  - array-filter
  - array-some
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The `find` method returns the first element in an array for which a test function returns `true`, or `undefined` if no such element exists.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 732-735 of 05-higher-order-functions.md): "It uses another array method, `find`, which goes over the elements in the array and returns the first one for which a function returns true. It returns `undefined` when it finds no such element."

The summary (lines 792-793): "`find` finds the first element that matches a predicate."

# Prerequisites

- **array**: `find` is an array method.
- **higher-order-function**: `find` takes a test function.
- **predicate-function**: The test function returns true/false.

# Key Properties

1. Returns the **first** element that passes the test.
2. Returns `undefined` if no element passes.
3. Stops iterating after finding the first match.
4. Unlike `filter`, returns a single element (not an array).

# Construction / Recognition

## To Construct/Create:
```javascript
let known = counts.find(c => c.name == name);
```

## To Identify/Recognize:
- `.find(callback)` on an array.

# Context & Application

`find` is used when you need a single element matching a condition, not all of them. It is used in the `countBy` function in Ch 5 to locate existing group entries.

# Examples

**Example 1** (Ch 5, lines 706-718 of 05-higher-order-functions.md) -- used in countBy:
```javascript
function countBy(items, groupName) {
  let counts = [];
  for (let item of items) {
    let name = groupName(item);
    let known = counts.find(c => c.name == name);
    if (!known) {
      counts.push({name, count: 1});
    } else {
      known.count++;
    }
  }
  return counts;
}
```

# Relationships

## Builds Upon
- **array** -- Method of arrays.
- **higher-order-function** -- Takes a function as argument.

## Enables
- Locating specific elements in collections.

## Related
- **array-filter** -- Returns all matches; `find` returns only the first.
- **array-some** -- Returns boolean; `find` returns the element itself.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Assuming `find` returns an array.
  **Correction**: `find` returns a single element (or `undefined`), not an array.

# Common Confusions

- **Confusion**: `find` and `filter` are interchangeable.
  **Clarification**: `find` returns the first matching element; `filter` returns all matching elements in an array.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Recognizing text", lines 732-735 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 732-735)
- Confidence rationale: Explicit description with usage example
- Cross-reference status: verified against summary
