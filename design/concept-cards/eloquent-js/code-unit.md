---
# === CORE IDENTIFICATION ===
concept: Code Unit
slug: code-unit

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
  - code units
  - UTF-16 code unit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
extends: []
related:
  - codepoint
  - unicode-in-javascript
contrasts_with:
  - codepoint

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Code units are 16-bit numbers that make up JavaScript strings in UTF-16 encoding. Most characters use one code unit, but some (like emoji) require two.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 626-634 of 05-higher-order-functions.md): "JavaScript strings are encoded as a sequence of 16-bit numbers. These are called *code units*. A Unicode character code was initially supposed to fit within such a unit (which gives you a little over 65,000 characters). When it became clear that wasn't going to be enough, many people balked at the need to use more memory per character. To address these concerns, UTF-16, the format also used by JavaScript strings, was invented. It describes most common characters using a single 16-bit code unit but uses a pair of two such units for others."

# Prerequisites

- **string**: Code units are the internal representation of strings.

# Key Properties

1. JavaScript strings are sequences of 16-bit code units.
2. Most common characters use **one** code unit.
3. Some characters (emoji, rare CJK characters) use **two** code units (a surrogate pair).
4. `string.length` counts code units, not characters.
5. `string[i]` and `charCodeAt` operate on code units, not full characters.

# Construction / Recognition

## To Construct/Create:
Code units are implicit in string representation. They become visible when:
```javascript
let horseShoe = "🐴👟";
console.log(horseShoe.length);     // → 4 (4 code units, 2 characters)
console.log(horseShoe.charCodeAt(0)); // → 55357 (half-character code unit)
```

## To Identify/Recognize:
- When `string.length` returns a larger number than the visible character count.
- When bracket access returns half of a character.

# Context & Application

Understanding code units is essential for correctly processing strings that contain emoji or characters from some non-Latin scripts.

# Examples

**Example 1** (Ch 5, lines 653-664 of 05-higher-order-functions.md):
```javascript
let horseShoe = "🐴👟";
console.log(horseShoe.length);
// → 4
console.log(horseShoe[0]);
// → (Invalid half-character)
console.log(horseShoe.charCodeAt(0));
// → 55357 (Code of the half-character)
console.log(horseShoe.codePointAt(0));
// → 128052 (Actual code for horse emoji)
```

# Relationships

## Builds Upon
- **string** -- Code units compose strings.

## Enables
- Understanding why `string.length` can be surprising.

## Related
- **codepoint** -- The actual character code (may span two code units).
- **unicode-in-javascript** -- The broader topic of Unicode handling.

## Contrasts With
- **codepoint** -- A codepoint is a full character; a code unit is a 16-bit piece.

# Common Errors

- **Error**: Assuming `string.length` equals the number of visible characters.
  **Correction**: `length` counts code units. Emoji and some characters use two code units.

# Common Confusions

- **Confusion**: `charCodeAt` gives the character's Unicode code point.
  **Clarification**: "`charCodeAt` gives you a code unit, not a full character code. The `codePointAt` method, added later, does give a full Unicode character."

# Source Reference

Chapter 5: Higher-Order Functions, Section "Strings and character codes", lines 626-695 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: direct (quoted from lines 626-634)
- Confidence rationale: Explicit definition with italicized term "code units"
- Cross-reference status: verified within chapter
