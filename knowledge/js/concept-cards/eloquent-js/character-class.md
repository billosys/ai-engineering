---
# === CORE IDENTIFICATION ===
concept: Character Class
slug: character-class

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
section: "Sets of characters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - character set
  - bracket expression

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - dot-character
  - character-escape
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match any character from a set?"
  - "How do I write a regular expression to match a pattern?"
---

# Quick Definition
A character class matches any single character from a defined set, written with square brackets (`[...]`), supporting ranges (`[a-z]`), negation (`[^...]`), and built-in shortcuts (`\d`, `\w`, `\s`).

# Core Definition
Haverbeke explains: "putting a set of characters between square brackets makes that part of the expression match any of the characters between the brackets." Ranges use hyphens: "a hyphen (`-`) between two characters can be used to indicate a range of characters." Negation uses caret: "to express that you want to match any character *except* the ones in the set---you can write a caret (`^`) character after the opening bracket." (Ch 9, "Sets of characters")

# Prerequisites
- **Regular expressions**: Character classes are part of regex pattern syntax

# Key Properties
1. `[abc]` matches any of a, b, or c
2. `[0-9]` matches any digit (range syntax)
3. `[^01]` matches any character NOT 0 or 1 (negation)
4. Built-in shortcuts: `\d` (digit), `\w` (word char), `\s` (whitespace)
5. Uppercase shortcuts negate: `\D` (non-digit), `\W` (non-word), `\S` (non-whitespace)
6. `.` (dot) matches any character except newline
7. Unicode property groups: `\p{L}` (any letter, requires `u` flag)

# Construction / Recognition
```javascript
/[0-9]/      // any digit
/[^01]/      // any non-binary character
/\d/         // shortcut for digits
/[\d.]/      // digit or period
/\p{L}/u     // any Unicode letter
```

# Context & Application
Character classes are fundamental to building regex patterns. They define what individual characters a pattern position can match.

# Examples
```javascript
console.log(/[0123456789]/.test("in 1992"));
// -> true
console.log(/[0-9]/.test("in 1992"));
// -> true

let nonBinary = /[^01]/;
console.log(nonBinary.test("1100100010100110"));
// -> false
console.log(nonBinary.test("0111010112101001"));
// -> true

// Unicode property groups
console.log(/\p{L}/u.test("a"));  // -> true
console.log(/\p{L}/u.test("!"));  // -> false
```
(Ch 9, "Sets of characters", lines 111-250)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Pattern matching for specific character types
## Related
- dot-character, character-escape
## Contrasts With
- N/A

# Common Errors
- **Error**: Using `\w` for international text
  **Correction**: `\w` only matches Latin letters, digits, and underscore; use `\p{L}` with the `u` flag for international text

# Common Confusions
- **Confusion**: Special characters inside `[...]` retain their special meaning
  **Clarification**: Inside brackets, most special characters (like `.` and `+`) lose their special meaning; only `]`, `\`, `^` (at start), and `-` (between chars) are special

# Source Reference
Chapter 9: Regular Expressions, Section "Sets of characters", lines 111-257.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with many examples
- Cross-reference status: verified
