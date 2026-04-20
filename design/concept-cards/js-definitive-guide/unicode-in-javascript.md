---
# === CORE IDENTIFICATION ===
concept: Unicode in JavaScript
slug: unicode-in-javascript

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 35
section: "2.5 Unicode"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Unicode character set
  - UTF-16

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - identifiers
extends: []
related:
  - unicode-escape-sequences
  - string-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript programs are written using the Unicode character set, allowing Unicode characters in strings, comments, and identifiers (including non-English letters and mathematical symbols).

# Core Definition

"JavaScript programs are written using the Unicode character set, and you can use any Unicode characters in strings and comments. For portability and ease of editing, it is common to use only ASCII letters and digits in identifiers. But this is a programming convention only, and the language allows Unicode letters, digits, and ideographs (but not emojis) in identifiers." (p. 35)

# Prerequisites

- **javascript-language-overview** — Unicode support is a language property
- **identifiers** — Unicode characters can be used in identifiers

# Key Properties

1. JavaScript source code uses the Unicode character set
2. Unicode characters allowed in strings, comments, and identifiers
3. Unicode letters, digits, and ideographs allowed in identifiers (not emojis)
4. ASCII is the convention for portability, but not a requirement
5. JavaScript does not perform Unicode normalization on source code
6. Different Unicode encodings of the same character are treated as different identifiers

# Construction / Recognition

```javascript
const π = 3.14;
const sí = true;
```

# Context & Application

Unicode support enables JavaScript programs to use identifiers and strings in any language. However, normalization issues can cause subtle bugs when using non-ASCII characters.

# Examples

From the source text (p. 35):
```javascript
const π = 3.14;
const sí = true;
```

Unicode normalization pitfall (p. 36):
```javascript
const café = 1;  // This constant is named "caf\u{e9}"
const café = 2;  // This constant is different: "cafe\u{301}"
café             // => 1: this constant has one value
café             // => 2: this indistinguishable constant has a different value
```

# Relationships

## Builds Upon
- **identifiers** — Unicode extends what characters can be used in identifiers

## Enables
- **unicode-escape-sequences** — Escape sequences for representing Unicode characters
- **string-type** — Strings use UTF-16 encoding

## Related
- **unicode-escape-sequences** — How to write Unicode characters with ASCII

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using two visually identical but differently encoded Unicode identifiers.
  **Correction**: Ensure your editor normalizes Unicode source code to prevent visually identical but semantically different identifiers.

# Common Confusions

- **Confusion**: JavaScript normalizes Unicode identifiers automatically.
  **Clarification**: "JavaScript assumes that the source code it is interpreting has already been normalized and does not do any normalization on its own" (p. 36).

# Source Reference

Chapter 2: Lexical Structure, Section 2.5, pages 35-36.

# Verification Notes

- Definition source: Direct quote from p. 35
- Confidence rationale: High — clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
