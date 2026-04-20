---
# === CORE IDENTIFICATION ===
concept: For/Of Loop
slug: for-of-loop

# === CLASSIFICATION ===
category: data-structures
subcategory: iteration
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Array loops"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - for-of loop
  - for...of

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array
  - for-loop
extends:
  - for-loop
related:
  - array-foreach
  - unicode-in-javascript
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and manipulate an array?"
---

# Quick Definition

The `for`/`of` loop iterates over the elements of an iterable value (arrays, strings, etc.) directly, without needing an index counter.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 710-724 of 04-data-structures-objects-and-arrays.md): "There is a simpler way to write such loops in modern JavaScript." And: "When a `for` loop uses the word `of` after its variable definition, it will loop over the elements of the value given after `of`. This works not only for arrays but also for strings and some other data structures."

# Prerequisites

- **array**: `for`/`of` commonly iterates over arrays.
- **for-loop**: `for`/`of` is a modern variant of the `for` loop.

# Key Properties

1. Syntax: `for (let element of array) { ... }`.
2. Iterates directly over **elements**, not indices.
3. Works with arrays, strings, and other iterable data structures.
4. When used on strings, iterates over code points (real characters), not code units.

# Construction / Recognition

## To Construct/Create:
```javascript
for (let entry of JOURNAL) {
  console.log(`${entry.events.length} events.`);
}
```

## To Identify/Recognize:
- `for (let x of iterable)` pattern.

# Context & Application

`for`/`of` is the preferred way to iterate over arrays and strings in modern JavaScript. It is simpler than index-based loops and handles Unicode correctly for strings.

# Examples

**Example 1** (Ch 4, lines 713-717 of 04-data-structures-objects-and-arrays.md):
```javascript
for (let entry of JOURNAL) {
  console.log(`${entry.events.length} events.`);
}
```

**Example 2** (Ch 5, lines 683-690 of 05-higher-order-functions.md) -- iterating string code points:
```javascript
let roseDragon = "🌹🐉";
for (let char of roseDragon) {
  console.log(char);
}
// → 🌹
// → 🐉
```

# Relationships

## Builds Upon
- **for-loop** -- A more concise variant.
- **array** -- Commonly used with arrays.

## Enables
- Simple iteration patterns.

## Related
- **array-foreach** -- Another way to iterate (as a method).
- **unicode-in-javascript** -- `for`/`of` on strings iterates code points.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Confusing `for`/`of` with `for`/`in` (which iterates over property names).
  **Correction**: Use `for`/`of` for values; `for`/`in` iterates over keys/property names (and should be avoided for arrays).

# Common Confusions

- **Confusion**: `for`/`of` and `forEach` are identical.
  **Clarification**: `for`/`of` is a language statement supporting `break`/`continue`; `forEach` is a method that does not.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Array loops", lines 690-724 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 710-724)
- Confidence rationale: Explicit section with examples
- Cross-reference status: verified against Ch 5 string iteration
