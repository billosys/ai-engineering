---
# === CORE IDENTIFICATION ===
concept: Word Boundary
slug: word-boundary

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "Boundaries and look-ahead"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - anchors
extends: []
related:
  - character-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match at word boundaries?"
---

# Quick Definition
The `\b` marker matches positions where a word character is adjacent to a non-word character, enabling matching at the edges of words without consuming characters.

# Core Definition
Haverbeke explains: "There is also a `\\b` marker that matches *word boundaries*, positions that have a word character on one side, and a nonword character on the other." He cautions: "these use the same simplistic concept of word characters as `\\w` and are therefore not very reliable." (Ch 9, "Boundaries and look-ahead")

# Prerequisites
- **Regular expressions**: Word boundaries are regex syntax
- **Anchors**: Word boundaries are a type of zero-width assertion

# Key Properties
1. `\b` matches positions between word and non-word characters
2. Does not consume any characters (zero-width)
3. Uses the same definition as `\w` (Latin letters, digits, underscore)
4. Not reliable for international text

# Construction / Recognition
```javascript
/\bword\b/  // matches "word" as a whole word
```

# Context & Application
Word boundaries are useful for matching whole words, preventing partial word matches (e.g., matching "cat" without matching "concatenate").

# Examples
The text notes that `\b` uses the same word character definition as `\w`, which only covers Latin characters. For more robust word boundary matching with international text, other approaches may be needed. (Ch 9, "Boundaries and look-ahead", lines 534-538)

# Relationships
## Builds Upon
- regular-expression, anchors
## Enables
- Whole-word matching
## Related
- character-class
## Contrasts With
- N/A

# Common Errors
- **Error**: Relying on `\b` for international text
  **Correction**: `\b` uses the simplistic `\w` definition; it won't correctly identify boundaries around non-Latin characters

# Common Confusions
- **Confusion**: `\b` matches a space character
  **Clarification**: `\b` matches a POSITION between characters, not an actual character; it's zero-width

# Source Reference
Chapter 9: Regular Expressions, Section "Boundaries and look-ahead", lines 534-543.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with caveats
- Cross-reference status: verified
