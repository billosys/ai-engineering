---
# === CORE IDENTIFICATION ===
concept: Unicode in JavaScript
slug: unicode-in-javascript

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
  - UTF-16 in JavaScript

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
  - code-unit
  - codepoint
extends: []
related:
  - array-some
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript strings use UTF-16 encoding, which represents most characters as single 16-bit code units but requires two code units (a surrogate pair) for characters with code points above 65,535, creating pitfalls with string length and indexing.

# Core Definition

As described in "Eloquent JavaScript" (Ch 5, lines 637-645 of 05-higher-order-functions.md): "UTF-16 is generally considered a bad idea today. It seems almost intentionally designed to invite mistakes. It's easy to write programs that pretend code units and characters are the same thing. And if your language doesn't use two-unit characters, that will appear to work just fine. But as soon as someone tries to use such a program with some less common Chinese characters, it breaks. Fortunately, with the advent of emoji, everybody has started using two-unit characters, and the burden of dealing with such problems is more fairly distributed."

# Prerequisites

- **string**: Unicode encoding affects string behavior.
- **code-unit**: Understanding 16-bit code units.
- **codepoint**: Understanding full character codes.

# Key Properties

1. `string.length` counts **code units**, not characters.
2. `string[i]` accesses **code units**, not necessarily full characters.
3. `for`/`of` iterates over **code points** (real characters).
4. `codePointAt()` gives full Unicode character codes; `charCodeAt()` gives code units.
5. UTF-16 uses surrogate pairs for characters above U+FFFF.

# Construction / Recognition

## To Construct/Create:
Not constructed directly -- UTF-16 is implicit in all JavaScript strings.

## To Identify/Recognize:
- Surprising `length` values for strings with emoji.
- Invalid "half-characters" when indexing into emoji strings.

# Context & Application

This knowledge is essential for any program that processes text containing emoji, mathematical symbols, or characters from scripts like CJK that may use surrogate pairs. The `for`/`of` loop and `codePointAt` are the correct tools for character-by-character processing.

# Examples

**Example 1** (Ch 5, lines 653-664 of 05-higher-order-functions.md):
```javascript
let horseShoe = "🐴👟";
console.log(horseShoe.length);
// → 4
console.log(horseShoe[0]);
// → (Invalid half-character)
```

**Example 2** (Ch 5, lines 683-690) -- correct iteration:
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
- **string** -- Unicode encoding is fundamental to strings.
- **code-unit** -- The 16-bit building blocks.
- **codepoint** -- Full character codes that may span code units.

## Enables
- Correct text processing for international and emoji-rich content.

## Related
- **array-some** -- Used in `characterScript` to identify scripts by code ranges.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `string.length` to count visible characters in emoji-containing strings.
  **Correction**: Use `[...string].length` to count code points, or iterate with `for`/`of`.

# Common Confusions

- **Confusion**: JavaScript handles all Unicode characters transparently.
  **Clarification**: Many string operations work on code units, not characters. Only `for`/`of` and `codePointAt` handle multi-unit characters correctly.

# Source Reference

Chapter 5: Higher-Order Functions, Section "Strings and character codes", lines 586-695 of 05-higher-order-functions.md (book.md line 4807).

# Verification Notes

- Definition source: synthesized from lines 626-695
- Confidence rationale: Detailed discussion with multiple examples
- Cross-reference status: verified within chapter
