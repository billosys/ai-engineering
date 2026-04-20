---
# === CORE IDENTIFICATION ===
concept: Test Method
slug: test-method

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
section: "Testing for matches"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - exec-method
  - match-method
contrasts_with:
  - exec-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I check if a string matches a pattern?"
---

# Quick Definition
The `test` method on a regular expression returns a Boolean indicating whether the string contains a match of the pattern.

# Core Definition
Haverbeke explains: "Regular expression objects have a number of methods. The simplest one is `test`. If you pass it a string, it will return a Boolean telling you whether the string contains a match of the pattern in the expression." (Ch 9, "Testing for matches")

# Prerequisites
- **Regular expressions**: `test` is called on a RegExp object

# Key Properties
1. Returns `true` if ANY part of the string matches (not necessarily the whole string)
2. Returns `false` if no match is found
3. Simplest way to check for a pattern
4. Does not provide match details (use `exec` for that)

# Construction / Recognition
```javascript
/pattern/.test(string)
```

# Context & Application
Use `test` for simple yes/no pattern matching. For extracting match details, use `exec` or string `match` instead.

# Examples
```javascript
console.log(/abc/.test("abcde"));
// -> true
console.log(/abc/.test("abxde"));
// -> false
```
(Ch 9, "Testing for matches", lines 98-103)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Pattern validation, conditional logic based on pattern matching
## Related
- exec-method, match-method
## Contrasts With
- exec-method (returns match details, not just boolean)

# Common Errors
- **Error**: Expecting `test` to match the entire string
  **Correction**: `test` returns true if the pattern matches anywhere in the string; use `^` and `$` anchors to match the whole string

# Common Confusions
- **Confusion**: `test` and `exec` do the same thing
  **Clarification**: `test` returns a boolean; `exec` returns a match object with captured groups and index information

# Source Reference
Chapter 9: Regular Expressions, Section "Testing for matches", lines 90-109.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
