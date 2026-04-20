---
# === CORE IDENTIFICATION ===
concept: RegExp Literal
slug: regexp-literal

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-matching
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "Creating a regular expression"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex literal
  - slash notation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - regexp-constructor
  - character-escape
contrasts_with:
  - regexp-constructor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a regular expression literal?"
  - "How do I write a regular expression to match a pattern?"
---

# Quick Definition
A regexp literal is written by enclosing a pattern between forward slash (`/`) characters, with backslashes treated as part of the pattern rather than string escape sequences.

# Core Definition
Haverbeke explains that a regular expression "can be either constructed with the `RegExp` constructor or written as a literal value by enclosing a pattern in forward slash (`/`) characters." In the literal notation, "backslashes that aren't part of special character codes (like `\\n`) will be *preserved*, rather than ignored as they are in strings, and change the meaning of the pattern." (Ch 9, "Creating a regular expression")

# Prerequisites
- **Regular expressions**: Understanding what patterns are

# Key Properties
1. Enclosed in forward slashes: `/pattern/`
2. Forward slashes in the pattern must be escaped: `\/`
3. Backslashes are preserved (unlike in strings)
4. Special characters must be escaped: `\+`, `\?`, `\*`, etc.
5. Flags appear after the closing slash: `/pattern/gi`

# Construction / Recognition
```javascript
let re = /abc/;
let aPlus = /A\+/;
let dateTime = /\d{1,2}-\d{1,2}-\d{4}/;
```

# Context & Application
Regexp literals are preferred when the pattern is known at write time. Use the `RegExp` constructor when the pattern needs to be built dynamically.

# Examples
```javascript
let re2 = /abc/;
let aPlus = /A\+/;  // matches literal "A+"
```
(Ch 9, "Creating a regular expression", lines 59-88)

# Relationships
## Builds Upon
- regular-expression
## Enables
- All pattern matching operations
## Related
- character-escape
## Contrasts With
- regexp-constructor (for dynamic patterns)

# Common Errors
- **Error**: Forgetting to escape forward slashes inside the pattern
  **Correction**: Use `\/` for literal forward slashes in regexp literals

# Common Confusions
- **Confusion**: Backslash escaping works the same as in strings
  **Clarification**: In regexp literals, backslashes are preserved and treated as pattern syntax, not string escapes

# Source Reference
Chapter 9: Regular Expressions, Section "Creating a regular expression", lines 51-88.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
