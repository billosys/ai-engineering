---
# === CORE IDENTIFICATION ===
concept: String Methods
slug: string-methods

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
pdf_page: 52
section: "3.3.3 Working with Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - string API
  - string operations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
extends: []
related:
  - primitive-immutability-vs-object-mutability
  - methods-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript provides a rich API of string methods for concatenation, searching, extracting substrings, comparison, case conversion, padding, and trimming — all returning new strings since strings are immutable.

# Core Definition

JavaScript provides a "rich API for working with strings." String concatenation uses the `+` operator. Strings "can be compared with the standard === equality and !== inequality operators: two strings are equal if and only if they consist of exactly the same sequence of 16-bit values." All string methods return new strings because "strings are immutable in JavaScript. Methods like replace() and toUpperCase() return new strings: they do not modify the string on which they are invoked." (pp. 52-53)

# Prerequisites

- **string-type** — Must understand the String type

# Key Properties

1. Concatenation: `+` operator
2. Length: `.length` property
3. Extraction: `substring()`, `slice()`, `split()`, `charAt()`, bracket notation `s[0]`
4. Searching: `indexOf()`, `lastIndexOf()`, `startsWith()` (ES6), `endsWith()` (ES6), `includes()` (ES6)
5. Modification (returns new string): `replace()`, `toLowerCase()`, `toUpperCase()`, `normalize()` (ES6)
6. Padding (ES2017): `padStart()`, `padEnd()`
7. Trimming: `trim()` (ES5), `trimStart()`, `trimEnd()` (ES2019)
8. Other: `concat()`, `repeat()` (ES6), `charCodeAt()`, `codePointAt()` (ES6)
9. Strings treated as read-only arrays: `s[0]` accesses first character

# Construction / Recognition

```javascript
let s = "Hello, world";
s.length              // => 12
s.substring(1,4)      // => "ell"
s.slice(-3)           // => "rld"
s.indexOf("l")        // => 2
s.startsWith("Hell")  // => true
s.includes("or")      // => true
s.replace("llo","ya") // => "Heya, world"
s.toUpperCase()       // => "HELLO, WORLD"
s[0]                  // => "H"
```

# Context & Application

String methods are used constantly in JavaScript for text processing, validation, formatting, and data manipulation. Understanding that they return new strings (not modifying the original) is essential.

# Examples

From the source text (pp. 52-54):
```javascript
let s = "Hello, world";
s.substring(1,4)         // => "ell": the 2nd, 3rd, and 4th characters
s.slice(-3)              // => "rld": last 3 characters
s.split(", ")            // => ["Hello", "world"]: split at delimiter
s.indexOf("l")           // => 2: position of first letter l
s.startsWith("Hell")     // => true: the string starts with these
s.includes("or")         // => true: s includes substring "or"
s.replace("llo", "ya")   // => "Heya, world"
s.toLowerCase()          // => "hello, world"
s.toUpperCase()          // => "HELLO, WORLD"
"x".padStart(3)          // => "  x"
" test ".trim()          // => "test"
"<>".repeat(5)           // => "<><><><><>"
```

# Relationships

## Builds Upon
- **string-type** — Methods operate on String values

## Enables
- Text processing and data manipulation

## Related
- **primitive-immutability-vs-object-mutability** — String methods always return new strings
- **methods-overview** — String methods are invoked on string values

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting `s.toUpperCase()` to modify `s`.
  **Correction**: String methods return new strings. Assign the result: `s = s.toUpperCase()`.

# Common Confusions

- **Confusion**: `substring()` and `slice()` are identical.
  **Clarification**: They behave similarly but differ in handling negative indices — `slice()` supports negative indices, `substring()` does not.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3.3, pages 52-54.

# Verification Notes

- Definition source: Direct quotes from pp. 52-53
- Confidence rationale: High — comprehensive list with examples
- Uncertainties: None
- Cross-reference status: Verified
