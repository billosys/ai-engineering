---
# === CORE IDENTIFICATION ===
concept: Regular Expression
slug: regular-expression

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex
  - regexp

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - object
extends: []
related:
  - regexp-literal
  - regexp-constructor
  - test-method
  - exec-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a regular expression?"
  - "What must I know before writing regular expressions?"
---

# Quick Definition
Regular expressions are objects that describe patterns in string data, forming a small separate language for inspecting and processing strings.

# Core Definition
Haverbeke introduces: "regular expressions are a way to describe patterns in string data. They form a small, separate language that is part of JavaScript and many other languages and systems." He adds: "Regular expressions are both terribly awkward and extremely useful. Their syntax is cryptic and the programming interface JavaScript provides for them is clumsy. But they are a powerful tool for inspecting and processing strings." (Ch 9)

# Prerequisites
- **Values**: Regular expressions are a type of value/object
- **Objects**: Regexp is a type of object with methods

# Key Properties
1. A type of object that represents a pattern
2. Can be created with literal notation (`/pattern/`) or the `RegExp` constructor
3. Has methods: `test`, `exec`
4. Works with string methods: `match`, `search`, `replace`, `matchAll`
5. Supports flags: `i` (case-insensitive), `g` (global), `y` (sticky), `u` (unicode)

# Construction / Recognition
```javascript
let re1 = new RegExp("abc");
let re2 = /abc/;
```
Both represent the same pattern.

# Context & Application
Regular expressions are used for validation, search, extraction, and transformation of text data. They appear throughout programming for tasks like parsing config files, validating input, and text processing.

# Examples
```javascript
console.log(/abc/.test("abcde"));
// -> true
console.log(/abc/.test("abxde"));
// -> false
```
(Ch 9, "Testing for matches", lines 98-103)

The chapter summary provides a complete reference table of regex syntax. (Ch 9, "Summary", lines 1178-1198)

# Relationships
## Builds Upon
- value, object
## Enables
- regexp-literal, regexp-constructor, test-method, exec-method, all pattern matching
## Related
- replace-method, match-method, search-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Overusing regex for complex parsing tasks
  **Correction**: "Part of knowing how to use them is resisting the urge to try to shoehorn things into them that they cannot cleanly express." (Ch 9)

# Common Confusions
- **Confusion**: Regular expressions are just for simple string matching
  **Clarification**: They support complex patterns including character classes, repetition, grouping, lookahead, and backreferences

# Source Reference
Chapter 9: Regular Expressions, opening section, lines 30-49.

# Verification Notes
- Definition source: direct
- Confidence rationale: Core topic of the chapter, extensively defined
- Cross-reference status: verified
