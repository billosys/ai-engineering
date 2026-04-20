---
# === CORE IDENTIFICATION ===
concept: String Properties
slug: string-properties

# === CLASSIFICATION ===
category: data-structures
subcategory: string-operations
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Strings and their properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - string methods

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
  - property
  - method
extends: []
related:
  - array
  - array-methods
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Strings have built-in properties and methods including `length`, `slice`, `indexOf`, `trim`, `padStart`, `split`, `join`, and `repeat`, but unlike objects, new properties cannot be added to them because strings are immutable.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 932-948 of 04-data-structures-objects-and-arrays.md): "We can read properties like `length` and `toUpperCase` from string values. But if we try to add a new property, it doesn't stick." And: "Values of type string, number, and Boolean are not objects, and though the language doesn't complain if you try to set new properties on them, it doesn't actually store those properties. As mentioned earlier, such values are immutable and cannot be changed."

# Prerequisites

- **string**: These properties belong to strings.
- **property**: Understanding property access.
- **method**: String methods are functions accessed as properties.

# Key Properties

1. Strings have `length`, `slice`, `indexOf`, `toUpperCase`, `toLowerCase`, `trim`, `padStart`, `split`, `repeat`.
2. String `indexOf` can search for multi-character substrings (unlike array `indexOf`).
3. Strings are **immutable** -- you cannot add new properties.
4. Individual characters can be accessed with bracket notation: `string[1]`.

# Construction / Recognition

## To Construct/Create:
String methods are built-in. They are called using dot notation on string values.

## To Identify/Recognize:
- Method calls on string values (e.g., `"hello".toUpperCase()`).

# Context & Application

String methods are essential for text processing. Many string methods have the same names as array methods (`slice`, `indexOf`) but with slightly different behavior.

# Examples

**Example 1** (Ch 4, lines 956-961):
```javascript
console.log("coconuts".slice(4, 7));
// → nut
console.log("coconut".indexOf("u"));
// → 5
```

**Example 2** (Ch 4, lines 978-981):
```javascript
console.log("  okay \n ".trim());
// → okay
```

**Example 3** (Ch 4, lines 998-1004):
```javascript
let sentence = "Secretarybirds specialize in stomping";
let words = sentence.split(" ");
console.log(words);
// → ["Secretarybirds", "specialize", "in", "stomping"]
console.log(words.join(". "));
// → Secretarybirds. specialize. in. stomping
```

**Example 4** (Ch 4, lines 936-941) -- immutability:
```javascript
let kim = "Kim";
kim.age = 88;
console.log(kim.age);
// → undefined
```

# Relationships

## Builds Upon
- **string** -- These methods operate on strings.
- **property** -- String methods are accessed as properties.

## Enables
- Text processing and manipulation.

## Related
- **array-methods** -- Many methods share names with array methods.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting to add custom properties to strings.
  **Correction**: Strings are immutable and do not store custom properties.

# Common Confusions

- **Confusion**: String `indexOf` and array `indexOf` behave identically.
  **Clarification**: "A string's `indexOf` can search for a string containing more than one character, whereas the corresponding array method looks only for a single element."

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Strings and their properties", lines 929-1029 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: synthesized from multiple descriptions in section
- Confidence rationale: Explicit section with multiple examples
- Cross-reference status: verified within chapter
