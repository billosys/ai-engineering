---
# === CORE IDENTIFICATION ===
concept: Unicode Planes
slug: unicode-planes

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
  - "Basic Multilingual Plane"
  - "BMP"
  - "astral planes"
  - "supplementary planes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unicode-code-points
extends: []
related:
  - utf-16-encoding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Unicode organizes its 21-bit code point space into 17 planes of 65,536 code points each. Plane 0 (BMP) contains most common characters; Planes 1-16 (astral/supplementary planes) contain emojis, historic scripts, and rare characters.

# Core Definition

Unicode's 21-bit code points are partitioned into 17 planes of 16 bits each. Plane 0 is the Basic Multilingual Plane (BMP, 0x0000-0xFFFF) containing characters for almost all modern languages and many symbols. Plane 1 is the Supplementary Multilingual Plane (SMP) with historic scripts, emojis, and symbols. Planes 1-16 are called supplementary or "astral" planes (Ch. 21, Section 21.1.1).

# Prerequisites

- **unicode-code-points** -- planes organize code points

# Key Properties

1. 17 planes total (0-16)
2. Plane 0 (BMP): 0x0000-0xFFFF -- most modern characters
3. Plane 1 (SMP): 0x10000-0x1FFFF -- emojis, historic scripts
4. Plane 2 (SIP): 0x20000-0x2FFFF -- additional CJK ideographs
5. Planes 3-13: unassigned
6. Plane 14: special-purpose
7. Planes 15-16: private use areas
8. Planes 1-16 called "astral" or "supplementary" planes

# Construction / Recognition

```js
// BMP character (plane 0)
> 'A'.codePointAt(0).toString(16)
'41'

// Astral character (plane 1)
> '🙂'.codePointAt(0).toString(16)
'1f642'
```

# Context & Application

Understanding planes explains why some characters (BMP) need one UTF-16 code unit while others (astral) need two (surrogate pairs). This directly affects JavaScript string handling.

# Examples

From the source text:

```js
> 'A'.codePointAt(0).toString(16)
'41'        // plane 0 (BMP)
> 'ü'.codePointAt(0).toString(16)
'fc'        // plane 0 (BMP)
> '🙂'.codePointAt(0).toString(16)
'1f642'     // plane 1 (SMP/astral)
```

# Relationships

## Builds Upon
- **unicode-code-points** — planes organize code points

## Enables
- Understanding surrogate pairs and `.length` behavior

## Related
- **utf-16-encoding** — BMP uses 1 code unit, astral uses 2

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all characters are in the BMP
  **Correction**: Emojis and many CJK characters are in astral planes and require surrogate pairs in UTF-16.

# Common Confusions

- **Confusion**: Thinking "astral" refers to something exotic or rare
  **Clarification**: Astral planes include commonly used emojis. Any string with emojis contains astral plane characters.

# Source Reference

Chapter 21: Unicode, Section 21.1.1, lines 54-79.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete plane listing provided
- Cross-reference status: verified
