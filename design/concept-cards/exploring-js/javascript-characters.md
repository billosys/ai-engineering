---
# === CORE IDENTIFICATION ===
concept: JavaScript Characters
slug: javascript-characters

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "Accessing JavaScript characters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "string characters"
  - "UTF-16 code units in strings"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - unicode-code-units
extends: []
related:
  - utf-16-encoding
  - grapheme-clusters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript has no dedicated character type. A "character" in a JavaScript string is a 16-bit UTF-16 code unit, accessed via bracket notation (`str[i]`) or `.at()`, and always represented as a string of length 1.

# Core Definition

"JavaScript has no extra data type for characters -- characters are always represented as strings." Characters are UTF-16 code units, accessed via `str[index]` or counted by `.length`. Grapheme clusters displayed on screen may consist of multiple JavaScript characters, especially emojis: `'🙂'.length` is `2` (Ch. 22, Section 22.3).

# Prerequisites

- **string-type** -- characters are elements of strings
- **unicode-code-units** -- characters are UTF-16 code units

# Key Properties

1. No separate character type (characters are length-1 strings)
2. Accessed via `str[index]` or `str.at(index)`
3. `.at()` supports negative indices (ES2022)
4. `.length` counts code units, not visible characters
5. `'🙂'.length` is `2` (two code units for one emoji)

# Construction / Recognition

```js
const str = 'abc';
assert.equal(str[1], 'b');
assert.equal(str.at(-1), 'c');
assert.equal(str.length, 3);
assert.equal('🙂'.length, 2);
```

# Context & Application

Understanding that JavaScript characters are code units (not grapheme clusters) is essential for correctly processing strings containing emojis, accented characters, and non-Latin scripts.

# Examples

From the source text:

```js
const str = 'abc';
assert.equal(str[1], 'b');
assert.equal(str.length, 3);

> '🙂'.length
2
```

# Relationships

## Builds Upon
- **string-type** — characters are string elements
- **unicode-code-units** — each character is a UTF-16 code unit

## Enables
- String indexing and iteration

## Related
- **utf-16-encoding** — explains why some characters need two units
- **grapheme-clusters** — visible characters may span multiple code units

## Contrasts With
- None

# Common Errors

- **Error**: Using `str.length` to limit user input to N visible characters
  **Correction**: Emojis may use 2+ code units. Use `Intl.Segmenter` for accurate character counting.

# Common Confusions

- **Confusion**: Expecting `'🙂'[0]` to return the emoji
  **Clarification**: It returns `'\uD83D'` -- the first half of the surrogate pair, which is not a valid character on its own.

# Source Reference

Chapter 22: Strings, Section 22.3, lines 299-328.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit statement with emoji example
- Cross-reference status: verified against Ch. 21
