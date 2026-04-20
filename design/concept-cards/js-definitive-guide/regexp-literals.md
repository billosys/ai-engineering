---
# === CORE IDENTIFICATION ===
concept: RegExp Literals
slug: regexp-literals

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
pdf_page: 55
section: "3.3.5 Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regular expression literals
  - regex literals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - literals
extends: []
related:
  - string-methods
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

RegExp literals are patterns enclosed between forward slashes (`/pattern/flags`) that describe text patterns for matching, searching, and replacing in strings.

# Core Definition

"JavaScript defines a datatype known as a regular expression (or RegExp) for describing and matching patterns in strings of text." "Text between a pair of slashes constitutes a regular expression literal. The second slash in the pair can also be followed by one or more letters, which modify the meaning of the pattern." RegExps "are not one of the fundamental datatypes in JavaScript, but they have a literal syntax like numbers and strings do." (p. 55)

# Prerequisites

- **string-type** — RegExp operates on strings
- **literals** — RegExp has a literal syntax

# Key Properties

1. Syntax: `/pattern/flags`
2. Not a primitive type — RegExps are objects
3. Has a literal syntax like numbers and strings
4. Flags modify behavior (e.g., `i` for case-insensitive, `g` for global)
5. RegExp objects have methods: `test()`
6. Strings have RegExp-accepting methods: `search()`, `match()`, `replace()`, `split()`

# Construction / Recognition

```javascript
/^HTML/            // Match "HTML" at start of string
/[1-9][0-9]*/      // Match a nonzero digit followed by any digits
/\bjavascript\b/i  // Match "javascript" as a word, case-insensitive
```

# Context & Application

Regular expressions are powerful tools for text processing, validation, and data extraction. They are used extensively for pattern matching in strings.

# Examples

From the source text (pp. 55-56):
```javascript
/^HTML/;                        // Match the letters H T M L at the start of a string
/[1-9][0-9]*/;                  // Match a nonzero digit, followed by any # of digits
/\bjavascript\b/i;              // Match "javascript" as a word, case-insensitive

let text = "testing: 1, 2, 3";
let pattern = /\d+/g;           // Matches all instances of one or more digits
pattern.test(text)              // => true: a match exists
text.search(pattern)            // => 9: position of first match
text.match(pattern)             // => ["1", "2", "3"]: array of all matches
text.replace(pattern, "#")      // => "testing: #, #, #"
text.split(/\D+/)               // => ["","1","2","3"]: split on nondigits
```

# Relationships

## Builds Upon
- **string-type** — RegExps operate on strings
- **literals** — RegExps have literal syntax

## Enables
- Pattern matching and text processing

## Related
- **string-methods** — Strings have methods that accept RegExp arguments

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting the `g` flag when using `match()` to find all occurrences.
  **Correction**: Without `g`, `match()` returns only the first match. Use `/pattern/g` for all matches.

# Common Confusions

- **Confusion**: RegExp is a primitive type because it has literal syntax.
  **Clarification**: RegExps are objects, not primitives. They just happen to have a convenient literal syntax.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3.5, pages 55-56.

# Verification Notes

- Definition source: Direct quotes from p. 55
- Confidence rationale: High — clearly introduced with examples
- Uncertainties: Full treatment deferred to §11.3
- Cross-reference status: Verified
