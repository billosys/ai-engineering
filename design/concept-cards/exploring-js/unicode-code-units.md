---
# === CORE IDENTIFICATION ===
concept: Unicode Code Units
slug: unicode-code-units

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
section: "Code points vs. code units"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "code unit"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unicode-code-points
extends: []
related:
  - utf-16-encoding
  - utf-8-encoding
contrasts_with:
  - unicode-code-points

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A Unicode code unit is a fixed-size number (8, 16, or 32 bits depending on the encoding) used to encode code points for storage or transmission. One or more code units encode a single code point.

# Core Definition

"*Code units* are numbers that encode code points, to store or transmit Unicode text. One or more code units encode a single code point. Each code unit has the same size, which depends on the *encoding format* that is used" (Ch. 21, Section 21.1). UTF-8 uses 8-bit code units, UTF-16 uses 16-bit, and UTF-32 uses 32-bit.

# Prerequisites

- **unicode-code-points** -- code units encode code points

# Key Properties

1. Fixed size within an encoding format
2. UTF-8: 8-bit code units (1-4 per code point)
3. UTF-16: 16-bit code units (1-2 per code point)
4. UTF-32: 32-bit code units (always 1 per code point)
5. JavaScript strings use UTF-16 code units

# Construction / Recognition

```js
> '🙂'.length
2  // Two UTF-16 code units
> '🙂'.split('')
['\uD83D', '\uDE42']  // Two surrogate code units
```

# Context & Application

Each JavaScript string character is a UTF-16 code unit. Understanding code units explains why `.length` returns 2 for emojis and why `.split('')` can break surrogate pairs.

# Examples

From the source text:

```js
> '🙂'.length
2   // Two UTF-16 code units
> '🙂'.split('')
[ '\uD83D', '\uDE42' ]   // Surrogate pair split apart
> 'π'.length
1   // BMP character: one code unit
```

# Relationships

## Builds Upon
- **unicode-code-points** — code units encode code points

## Enables
- Understanding JavaScript string `.length` behavior

## Related
- **utf-16-encoding** — JavaScript uses UTF-16 code units
- **utf-8-encoding** — alternative encoding with 8-bit code units

## Contrasts With
- **unicode-code-points** — code points are logical characters; code units are encoding elements

# Common Errors

- **Error**: Using `.length` to count visible characters
  **Correction**: `.length` counts UTF-16 code units. Use `Array.from(str).length` for code points or `Intl.Segmenter` for grapheme clusters.

# Common Confusions

- **Confusion**: Thinking one character = one code unit in JavaScript
  **Clarification**: Astral plane characters (emojis, etc.) require two code units (a surrogate pair).

# Source Reference

Chapter 21: Unicode, Section 21.1, lines 39-53.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with size chart
- Cross-reference status: verified
