---
# === CORE IDENTIFICATION ===
concept: UTF-16 Encoding
slug: utf-16-encoding

# === CLASSIFICATION ===
category: primitive-types
subcategory: unicode
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Unicode -- a brief introduction (advanced)"
chapter_number: 21
pdf_page: null
section: "UTF-16"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "UTF-16"
  - "surrogate pairs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unicode-code-points
  - unicode-code-units
extends: []
related:
  - string-type
  - grapheme-clusters
contrasts_with:
  - utf-8-encoding

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

UTF-16 is the encoding format used by JavaScript strings, using 16-bit code units. BMP characters use one code unit; astral plane characters use two code units called a surrogate pair.

# Core Definition

UTF-16 uses 16-bit code units. BMP code points (0x0000-0xFFFF) are stored in single code units. Astral plane code points (0x10000-0x10FFFF) are encoded using two code units: a leading (high) surrogate (0xD800-0xDBFF) and a trailing (low) surrogate (0xDC00-0xDFFF). JavaScript strings are sequences of UTF-16 code units. A surrogate appearing without its partner is called a "lone surrogate" (Ch. 21, Section 21.1.2.2).

# Prerequisites

- **unicode-code-points** -- what is being encoded
- **unicode-code-units** -- the encoding elements

# Key Properties

1. 16-bit code units
2. BMP: 1 code unit per code point
3. Astral planes: 2 code units (surrogate pair) per code point
4. Leading surrogate: 0xD800-0xDBFF
5. Trailing surrogate: 0xDC00-0xDFFF
6. JavaScript source code and strings use UTF-16 internally

# Construction / Recognition

```js
> '🙂'.length
2
> '🙂' === '\uD83D\uDE42'
true
> 'π'.length
1
```

# Context & Application

Understanding UTF-16 is essential for correctly handling emojis and non-BMP characters in JavaScript strings. Many string methods operate on code units, not code points.

# Examples

From the source text:

```js
> '🙂'.codePointAt(0).toString(16)
'1f642'
> '🙂'.length
2
> '🙂'.split('')
[ '\uD83D', '\uDE42' ]

// Deriving surrogates from code point 0x1F642
> (0x1F642 - 0x10000).toString(2).padStart(20, '0')
'00001111011001000010'
> (0xD800 + 0b0000111101).toString(16)
'd83d'
> (0xDC00 + 0b1001000010).toString(16)
'de42'
```

# Relationships

## Builds Upon
- **unicode-code-points** — what UTF-16 encodes
- **unicode-code-units** — the building blocks of UTF-16

## Enables
- Understanding JavaScript string internals

## Related
- **string-type** — strings are UTF-16 sequences
- **grapheme-clusters** — user-perceived characters built from code points

## Contrasts With
- **utf-8-encoding** — alternative encoding used in files/network

# Common Errors

- **Error**: Splitting strings with `.split('')` and expecting emoji to stay intact
  **Correction**: `.split('')` splits into code units, breaking surrogate pairs. Use `Array.from(str)` for code-point-aware splitting.

# Common Confusions

- **Confusion**: Thinking surrogates are valid characters
  **Clarification**: Surrogates are encoding artifacts, not valid code points. A lone surrogate is malformed.

# Source Reference

Chapter 21: Unicode, Section 21.1.2.2, lines 116-192.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete encoding mechanics with bit-level example
- Cross-reference status: verified
