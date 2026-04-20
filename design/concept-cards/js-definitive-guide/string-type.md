---
# === CORE IDENTIFICATION ===
concept: String Type
slug: string-type

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 49
section: "3.3 Text"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - String
  - text

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
extends: []
related:
  - string-literals
  - string-methods
  - template-literals
  - escape-sequences
  - primitive-immutability-vs-object-mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

The String type represents immutable ordered sequences of 16-bit values (UTF-16), where the length is the number of 16-bit values and characters beyond the Basic Multilingual Plane require two elements (a surrogate pair).

# Core Definition

"The JavaScript type for representing text is the string. A string is an immutable ordered sequence of 16-bit values, each of which typically represents a Unicode character. The length of a string is the number of 16-bit values it contains." JavaScript "uses the UTF-16 encoding of the Unicode character set, and JavaScript strings are sequences of unsigned 16-bit values." Characters beyond the BMP are "encoded using the rules of UTF-16 as a sequence (known as a 'surrogate pair') of two 16-bit values." (pp. 49-50)

# Prerequisites

- **primitive-vs-object-types** — String is a primitive type

# Key Properties

1. Immutable — string methods return new strings, never modify the original
2. UTF-16 encoded sequences of 16-bit values
3. Zero-based indexing
4. Length is count of 16-bit values, not characters (surrogate pairs count as 2)
5. Empty string has length 0
6. No separate character type — a single character is a string of length 1
7. Strings are iterable in ES6 (for/of iterates actual characters, not 16-bit values)
8. Strings can be compared with `===` and relational operators

# Construction / Recognition

Strings are created with single quotes, double quotes, or backticks:
```javascript
"hello"
'world'
`template`
```

# Context & Application

Strings are one of the most commonly used types in JavaScript, representing all textual data. Understanding UTF-16 encoding is important when working with emoji and other characters outside the Basic Multilingual Plane.

# Examples

From the source text (pp. 49-50):
```javascript
let euro = "€";
let love = "❤";
euro.length     // => 1: this character has one 16-bit element
love.length     // => 2: UTF-16 encoding of ❤ is "\ud83d\udc99"
```

String immutability (p. 53):
```javascript
let s = "hello";
s.toUpperCase();  // Returns "HELLO", but doesn't alter s
s                 // => "hello": the original string has not changed
```

# Relationships

## Builds Upon
- **primitive-vs-object-types** — String is a primitive type

## Enables
- **string-literals** — How to write string values
- **string-methods** — Operations on strings
- **template-literals** — ES6 string interpolation syntax
- **escape-sequences** — Special characters in strings

## Related
- **primitive-immutability-vs-object-mutability** — Strings are immutable

## Contrasts With
- None explicitly, though contrasts with mutable arrays implicitly

# Common Errors

- **Error**: Assuming `string.length` counts characters for emoji/CJK text.
  **Correction**: Length counts 16-bit values. Characters outside the BMP (like many emoji) have length 2 due to surrogate pairs.

# Common Confusions

- **Confusion**: String methods modify the string in place.
  **Clarification**: "Strings are immutable in JavaScript. Methods like replace() and toUpperCase() return new strings: they do not modify the string on which they are invoked" (p. 53).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3, pages 49-55.

# Verification Notes

- Definition source: Direct quotes from pp. 49-50
- Confidence rationale: High — thoroughly defined
- Uncertainties: None
- Cross-reference status: Verified
