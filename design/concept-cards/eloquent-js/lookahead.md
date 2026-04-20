---
# === CORE IDENTIFICATION ===
concept: Lookahead
slug: lookahead

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-syntax
tier: advanced

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
aliases:
  - look-ahead test
  - positive lookahead
  - negative lookahead

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - anchors
extends: []
related:
  - grouping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I assert what follows a match without including it?"
---

# Quick Definition
Lookahead tests (`(?=...)` for positive, `(?!...)` for negative) check whether a pattern matches ahead of the current position without consuming characters or including the lookahead content in the match.

# Core Definition
Haverbeke explains: "*Look-ahead* tests do something similar [to boundaries]. They provide a pattern and will make the match fail if the input doesn't match that pattern, but don't actually move the match position forward. They are written between `(?=` and `)`." The `(?!...)` notation "expresses a *negative* look-ahead. This matches only if the pattern in the parentheses *doesn't* match." (Ch 9, "Boundaries and look-ahead")

# Prerequisites
- **Regular expressions**: Lookaheads are part of regex syntax
- **Anchors**: Lookaheads are zero-width assertions like anchors

# Key Properties
1. `(?=pattern)` positive lookahead: succeeds if pattern matches ahead
2. `(?!pattern)` negative lookahead: succeeds if pattern does NOT match ahead
3. Zero-width: does not consume characters
4. The lookahead content is not part of the matched string

# Construction / Recognition
```javascript
/a(?=e)/   // matches 'a' only when followed by 'e'
/a(?! )/   // matches 'a' only when NOT followed by space
```

# Context & Application
Lookaheads enable conditional matching based on context without including the context in the match result.

# Examples
```javascript
console.log(/a(?=e)/.exec("braeburn"));
// -> ["a"]
console.log(/a(?! )/.exec("a b"));
// -> null
```
"The `e` in the first example is necessary to match, but is not part of the matched string." (Ch 9, "Boundaries and look-ahead", lines 546-563)

# Relationships
## Builds Upon
- regular-expression, anchors
## Enables
- Context-sensitive matching
## Related
- grouping
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting lookahead content to appear in the match result
  **Correction**: Lookaheads are zero-width; they assert but don't consume or capture

# Common Confusions
- **Confusion**: `(?=...)` and `(...)` behave the same
  **Clarification**: Regular groups capture and consume; lookaheads only assert without consuming

# Source Reference
Chapter 9: Regular Expressions, Section "Boundaries and look-ahead", lines 545-563.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
