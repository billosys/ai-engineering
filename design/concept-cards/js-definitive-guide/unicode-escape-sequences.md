---
# === CORE IDENTIFICATION ===
concept: Unicode Escape Sequences
slug: unicode-escape-sequences

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
section: "2.5.1 Unicode Escape Sequences"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "\\u escape"
  - "Unicode escapes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unicode-in-javascript
extends: []
related:
  - escape-sequences
  - string-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Unicode escape sequences allow writing Unicode characters using only ASCII characters, using the `\u` prefix followed by four hex digits or curly-brace-enclosed hex digits.

# Core Definition

"JavaScript defines escape sequences that allow us to write Unicode characters using only ASCII characters. These Unicode escapes begin with the characters \u and are either followed by exactly four hexadecimal digits (using uppercase or lowercase letters A-F) or by one to six hexadecimal digits enclosed within curly braces." Unicode escapes "may appear in JavaScript string literals, regular expression literals, and identifiers (but not in language keywords)." (p. 35)

# Prerequisites

- **unicode-in-javascript** — Must understand Unicode character set support

# Key Properties

1. Two forms: `\uXXXX` (four hex digits) and `\u{X}` to `\u{XXXXXX}` (ES6, 1-6 hex digits)
2. Can appear in string literals, regex literals, and identifiers
3. Cannot appear in language keywords
4. The curly brace form (ES6) supports codepoints requiring more than 16 bits (e.g., emoji)
5. In comments, Unicode escapes are treated as ASCII and not interpreted

# Construction / Recognition

```javascript
let café = 1;
caf\u00e9           // => 1; access the variable using an escape sequence
caf\u{E9}           // => 1; another form of the same escape sequence
console.log("\u{1F600}");  // Prints a smiley face emoji
```

# Context & Application

Unicode escape sequences are used when working with systems that cannot display or input the full Unicode character set, or when source code must contain only ASCII characters. The ES6 curly brace form is needed for characters beyond the Basic Multilingual Plane (e.g., emoji).

# Examples

From the source text (p. 35):
```javascript
let café = 1;          // Define a variable using a Unicode character
caf\u00e9              // => 1; access the variable using an escape sequence
caf\u{E9}              // => 1; another form of the same escape sequence
```

ES6 curly brace form for emoji (p. 35):
```javascript
console.log("\u{1F600}");  // Prints a smiley face emoji
```

# Relationships

## Builds Upon
- **unicode-in-javascript** — Escape sequences are a way to write Unicode with ASCII

## Enables
- **escape-sequences** — String escape sequences include Unicode escapes

## Related
- **escape-sequences** — Unicode escapes are one type of escape sequence in strings
- **string-type** — Strings use Unicode (UTF-16)

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using Unicode escapes in language keywords.
  **Correction**: Unicode escapes cannot appear in keywords — only in string literals, regex literals, and identifiers.

# Common Confusions

- **Confusion**: The four-digit form `\uXXXX` can represent all Unicode characters.
  **Clarification**: Characters beyond the Basic Multilingual Plane (codepoints > 0xFFFF) require the ES6 curly brace form `\u{XXXXX}`.

# Source Reference

Chapter 2: Lexical Structure, Section 2.5.1, page 35.

# Verification Notes

- Definition source: Direct quote from p. 35
- Confidence rationale: High — clearly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
