---
# === CORE IDENTIFICATION ===
concept: Unicode Code Points
slug: unicode-code-points

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
section: "Code points"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "code point"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - unicode-code-units
  - grapheme-clusters
  - utf-16-encoding
contrasts_with:
  - unicode-code-units

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A Unicode code point is a 21-bit number representing an atomic part of Unicode text, such as a visible symbol, an accent modifier, or a control character.

# Core Definition

"*Code points* are numbers that represent the atomic parts of Unicode text. Most of them represent visible symbols but they can also have other meanings such as specifying an aspect of a symbol (the accent of a letter, the skin tone of an emoji, etc.)." Code points are 21 bits and partitioned into 17 planes of 16 bits each. Plane 0 (BMP, 0x0000-0xFFFF) contains most modern language characters. Planes 1-16 are supplementary (astral) planes (Ch. 21, Section 21.1.1).

# Prerequisites

Foundational Unicode concept with no prerequisites.

# Key Properties

1. 21 bits in size
2. 17 planes x 16 bits each
3. Plane 0: Basic Multilingual Plane (BMP) -- most common characters
4. Plane 1: Supplementary Multilingual Plane -- emojis, historic scripts
5. Access via `.codePointAt()`: `'A'.codePointAt(0)` is `0x41`

# Construction / Recognition

```js
> 'A'.codePointAt(0).toString(16)
'41'
> '🙂'.codePointAt(0).toString(16)
'1f642'   // astral plane (plane 1)
```

# Context & Application

Code points are the fundamental unit of Unicode text. Understanding them is essential for working with non-BMP characters (emojis, rare CJK characters) in JavaScript strings.

# Examples

From the source text:

```js
> 'A'.codePointAt(0).toString(16)
'41'
> 'ü'.codePointAt(0).toString(16)
'fc'
> 'π'.codePointAt(0).toString(16)
'3c0'
> '🙂'.codePointAt(0).toString(16)
'1f642'
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **utf-16-encoding** — encoding of code points
- **grapheme-clusters** — composed of one or more code points

## Related
- **unicode-code-units** — code units encode code points

## Contrasts With
- **unicode-code-units** — code units are encoding-level; code points are character-level

# Common Errors

- **Error**: Assuming every code point fits in 16 bits
  **Correction**: Astral plane code points (like emojis) require more than 16 bits and are encoded as two UTF-16 code units.

# Common Confusions

- **Confusion**: Thinking a code point equals a visible character
  **Clarification**: A visible character (grapheme cluster) may require multiple code points (e.g., flag emojis, combined characters).

# Source Reference

Chapter 21: Unicode, Section 21.1.1, lines 54-98.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with plane descriptions
- Cross-reference status: verified
