---
# === CORE IDENTIFICATION ===
concept: Integer Literals
slug: integer-literals

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: literals
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 43
section: "3.2.1 Integer Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - numeric literals
  - hex literals
  - binary literals
  - octal literals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - literals
extends:
  - literals
related:
  - floating-point-literals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Integer literals in JavaScript can be written in base-10, hexadecimal (0x), binary (0b, ES6), or octal (0o, ES6), and may use underscores as visual separators.

# Core Definition

"In a JavaScript program, a base-10 integer is written as a sequence of digits." JavaScript also recognizes "hexadecimal (base-16) values. A hexadecimal literal begins with 0x or 0X." "In ES6 and later, you can also express integers in binary (base 2) or octal (base 8) using the prefixes 0b and 0o (or 0B and 0O) instead of 0x." Underscores can be used within numeric literals as separators. (pp. 43-44)

# Prerequisites

- **number-type** — Integer literals produce Number values
- **literals** — Integer literals are a specific kind of literal

# Key Properties

1. Base-10: plain digit sequence (0, 3, 10000000)
2. Hexadecimal: prefix `0x` or `0X` with digits 0-9 and A-F
3. Binary (ES6): prefix `0b` or `0B` with digits 0-1
4. Octal (ES6): prefix `0o` or `0O` with digits 0-7
5. Underscore separators: `1_000_000_000` for readability
6. Can be preceded by a minus sign (-) for negative numbers

# Construction / Recognition

```javascript
0                  // zero
3                  // three
10000000           // ten million
0xff               // => 255: hexadecimal
0xBADCAFE          // => 195939070
0b10101            // => 21: binary (ES6)
0o377              // => 255: octal (ES6)
1_000_000_000      // underscore separators
```

# Context & Application

Different bases are used for different purposes: hexadecimal for colors and byte values, binary for bit flags, octal for file permissions. Underscore separators improve readability of large numbers.

# Examples

From the source text (pp. 43-44):
```javascript
0xff               // => 255: (15*16 + 15)
0xBADCAFE          // => 195939070
0b10101            // => 21: (1*16 + 0*8 + 1*4 + 0*2 + 1*1)
0o377              // => 255: (3*64 + 7*8 + 7*1)

let billion = 1_000_000_000;    // Underscore as a thousands separator.
let bytes = 0x89_AB_CD_EF;      // As a bytes separator.
let bits = 0b0001_1101_0111;    // As a nibble separator.
```

# Relationships

## Builds Upon
- **number-type** — Integer literals produce Number values
- **literals** — Integer literals are a type of literal

## Enables
- Numeric computation with readable source code

## Related
- **floating-point-literals** — The other format for numeric literals

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `0` prefix for octal (e.g., `077`) in modern JavaScript.
  **Correction**: Use the explicit `0o` prefix: `0o77`. The legacy `0` prefix for octal is deprecated and forbidden in strict mode.

# Common Confusions

- **Confusion**: Different literal bases produce different types.
  **Clarification**: All integer literals (regardless of base) produce regular Number values. `0xff` and `255` are the same value.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.2.1, pages 43-44.

# Verification Notes

- Definition source: Direct quotes from pp. 43-44
- Confidence rationale: High — clearly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
