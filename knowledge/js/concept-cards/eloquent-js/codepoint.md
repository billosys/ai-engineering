---
# === CORE IDENTIFICATION ===
concept: Code Point
slug: codepoint

# === CLASSIFICATION ===
category: higher-order-programming
subcategory: unicode
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Higher-Order Functions"
chapter_number: 5
pdf_page: null
section: "Strings and character codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - codepoints
  - Unicode code point
  - character code

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
  - code-unit
extends: []
related:
  - unicode-in-javascript
contrasts_with:
  - code-unit

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A code point is a full Unicode character number, accessed in JavaScript with `codePointAt()`, which may span one or two 16-bit code units in UTF-16 encoding.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 667-673 of 05-higher-order-functions.md): "JavaScript's `charCodeAt` method gives you a code unit, not a full character code. The `codePointAt` method, added later, does give a full Unicode character, so we could use that to get characters from a string. But the argument passed to `codePointAt` is still an index into the sequence of code units."

# Prerequisites

- **string**: Code points are character codes within strings.
- **code-unit**: Code points may span one or two code units.

# Key Properties

1. `codePointAt(0)` returns the full Unicode character code.
2. A code point may require one or two code units in UTF-16.
3. `for`/`of` loops iterate over code points (real characters), not code units.
4. Use `codePointAt(0)` on individual characters to get their code.

# Construction / Recognition

## To Construct/Create:
```javascript
let horse = "🐴";
console.log(horse.codePointAt(0));
// → 128052
```

## To Identify/Recognize:
- Use of `codePointAt()` method.
- `for`/`of` loop over a string iterates code points.

# Context & Application

Understanding code points is essential for correctly handling Unicode in JavaScript, especially when working with emoji, CJK characters, or any characters outside the Basic Multilingual Plane.

# Examples

**Example 1** (Ch 5, lines 653-664 of 05-higher-order-functions.md):
```javascript
let horseShoe = "🐴👟";
console.log(horseShoe.codePointAt(0));
// → 128052 (Actual code for horse emoji)
```

**Example 2** (Ch 5, lines 683-690) -- iterating code points:
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
- **string** -- Code points are accessed from strings.
- **code-unit** -- Code points may span multiple code units.

## Enables
- Correct character-by-character processing of Unicode strings.

## Related
- **unicode-in-javascript** -- The broader context.

## Contrasts With
- **code-unit** -- A code unit is a 16-bit piece; a code point is a complete character.

# Common Errors

- **Error**: Using `charCodeAt` for emoji or non-BMP characters.
  **Correction**: Use `codePointAt` to get the full Unicode code point.

# Common Confusions

- **Confusion**: `string[i]` gives a character.
  **Clarification**: `string[i]` gives a code unit, which may be only half of a multi-unit character.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Strings and character codes", lines 667-695 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (synthesized from lines 667-695)
- Confidence rationale: Explicit distinction between code units and code points
- Cross-reference status: verified within chapter
