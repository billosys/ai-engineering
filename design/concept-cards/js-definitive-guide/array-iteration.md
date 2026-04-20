---
# === CORE IDENTIFICATION ===
concept: Array Iteration
slug: array-iteration

# === CLASSIFICATION ===
category: arrays
subcategory: iteration
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 179
section: "7.6 Iterating Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "looping through arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - foreach-method
  - map-method
  - sparse-arrays
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the different ways to iterate over a JavaScript array?"
---

# Quick Definition

JavaScript provides multiple ways to iterate arrays: `for/of` loops (ES6, preferred), `forEach()` method, traditional `for` loops, and `for/in` (generally avoided for arrays).

# Core Definition

"As of ES6, the easiest way to loop through each of the elements of an array (or any iterable object) is with the for/of loop." The built-in iterator returns elements in ascending order and returns `undefined` for nonexistent sparse elements. The `entries()` method provides `[index, value]` pairs. `forEach()` offers a functional approach, skipping nonexistent elements in sparse arrays. Traditional `for` loops provide full control. `for/in` should generally be avoided for arrays. (Flanagan, p. 179-181)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. `for/of` is preferred for simple iteration (ES6+)
2. `for/of` returns `undefined` for sparse array gaps
3. `entries()` gives `[index, value]` pairs with `for/of`
4. `forEach()` skips nonexistent elements in sparse arrays
5. `forEach()` has no `break` equivalent
6. Traditional `for` loop offers most control

# Construction / Recognition

```javascript
for (let element of array) { ... }
for (let [index, element] of array.entries()) { ... }
array.forEach(element => { ... });
for (let i = 0; i < array.length; i++) { ... }
```

# Context & Application

Array iteration is one of the most common operations in JavaScript. Choose the method based on whether you need indexes, need to break early, or need to handle sparse arrays specially.

# Examples

```javascript
let letters = [..."Hello world"];
let string = "";
for (let letter of letters) {
    string += letter;
}
string  // => "Hello world"

// With index:
for (let [index, letter] of letters.entries()) {
    if (index % 2 === 0) everyother += letter;
}

// forEach (functional):
letters.forEach(letter => { uppercase += letter.toUpperCase(); });
```
(Flanagan, p. 179-180)

# Relationships

## Builds Upon
- **array-fundamentals** — Iterates over array elements

## Enables
- **foreach-method** — Functional iteration approach
- **map-method** — Transformative iteration

## Related
- **sparse-arrays** — Different iteration methods handle gaps differently

## Contrasts With
- None specific

# Common Errors

- **Error**: Using `for/in` to iterate arrays.
  **Correction**: `for/in` iterates property names (including inherited and non-index properties) and should be avoided for arrays. Use `for/of` or `forEach()`.

# Common Confusions

- **Confusion**: `for/of` and `forEach()` handle sparse arrays the same way.
  **Clarification**: `for/of` returns `undefined` for gaps; `forEach()` skips them entirely.

# Source Reference

Chapter 7: Arrays, Section 7.6, pages 179-181.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: Multiple methods clearly documented
- Uncertainties: None
- Cross-reference status: Verified
