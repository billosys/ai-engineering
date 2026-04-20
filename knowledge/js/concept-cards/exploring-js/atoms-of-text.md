---
# === CORE IDENTIFICATION ===
concept: Atoms of Text
slug: atoms-of-text

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
section: "Atoms of text: code points, JavaScript characters, grapheme clusters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - unicode-code-points
  - unicode-code-units
  - grapheme-clusters
extends: []
related:
  - utf-16-encoding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript text has three levels of granularity: JavaScript characters (16-bit UTF-16 code units), Unicode code points (21-bit, encoded by 1-2 code units), and grapheme clusters (user-perceived characters, composed of 1+ code points).

# Core Definition

Three levels of text atoms in JavaScript: (1) JavaScript characters are 16-bit UTF-16 code units -- `.length` and `str[i]` operate at this level; (2) Unicode code points are 21-bit, accessed via `codePointAt()` and iteration (`for...of`, `Array.from()`); (3) grapheme clusters are user-perceived characters requiring 1+ code points, handled by `Intl.Segmenter` (Ch. 22, Section 22.7).

# Prerequisites

- **string-type** -- strings contain these atoms
- **unicode-code-points** -- the intermediate level
- **unicode-code-units** -- the lowest level (JavaScript characters)
- **grapheme-clusters** -- the highest level

# Key Properties

1. Code unit: 16 bits, accessed via `str[i]`, counted by `.length`
2. Code point: 21 bits, 1-2 code units, accessed via `codePointAt()`, iterated via `for...of`
3. Grapheme cluster: 1+ code points, accessed via `Intl.Segmenter`
4. `'abc'.length` is 3 (3 code units = 3 code points = 3 grapheme clusters)
5. `'🙂'.length` is 2 (2 code units, 1 code point, 1 grapheme cluster)

# Construction / Recognition

```js
// 3 code points, 3 JavaScript characters
assert.equal('abc'.length, 3);

// 1 code point, 2 JavaScript characters
assert.equal('🙂'.length, 2);

// Code-point-aware splitting
Array.from('A🙂') // ['A', '🙂']

// Code-unit splitting (breaks surrogates)
'A🙂'.split('') // ['A', '\uD83D', '\uDE42']
```

# Context & Application

Understanding these three levels is essential for correctly processing international text and emojis. Most built-in string methods operate on code units, but iteration (`for...of`) and `Array.from()` work with code points.

# Examples

From the source text:

```js
// str.split('') splits by code units
> 'A🙂'.split('')
[ 'A', '\uD83D', '\uDE42' ]

// Array.from splits by code points
> Array.from('A🙂')
[ 'A', '🙂' ]

// Grapheme clusters can span multiple code points
'😵‍💫'.length  // 5 JavaScript characters
Array.from('😵‍💫')  // ['😵', '\u200D', '💫'] -- 3 code points, 1 grapheme cluster
```

# Relationships

## Builds Upon
- **string-type** — strings contain these atoms
- **unicode-code-points** — the code point level
- **unicode-code-units** — the code unit level
- **grapheme-clusters** — the grapheme cluster level

## Enables
- Correct text processing for international content

## Related
- **utf-16-encoding** — determines the code unit structure

## Contrasts With
- None

# Common Errors

- **Error**: Using `.split('')` on strings with emojis
  **Correction**: Use `Array.from(str)` or `[...str]` for code-point-aware splitting.

# Common Confusions

- **Confusion**: Conflating the three levels of text atoms
  **Clarification**: `.length` counts code units; iteration counts code points; user-perceived characters are grapheme clusters.

# Source Reference

Chapter 22: Strings, Section 22.7, lines 1465-1599.

# Verification Notes

- Definition source: synthesized (combines three concepts from the section)
- Confidence rationale: Clear table and examples in source
- Cross-reference status: verified against Ch. 21
