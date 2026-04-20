---
# === CORE IDENTIFICATION ===
concept: Search Method
slug: search-method

# === CLASSIFICATION ===
category: text-processing
subcategory: string-manipulation
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "The search method"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - String.prototype.search

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - match-method
  - exec-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find the position of a regex match in a string?"
---

# Quick Definition
The string `search` method takes a regular expression and returns the index of the first match, or -1 if no match is found -- similar to `indexOf` but for patterns.

# Core Definition
Haverbeke explains: "there is another method, `search`, that does expect a regular expression. Like `indexOf`, it returns the first index on which the expression was found, or -1 when it wasn't found." (Ch 9, "The search method")

# Prerequisites
- **Regular expressions**: The search pattern

# Key Properties
1. Returns the index of the first match
2. Returns -1 if no match found
3. Similar to `indexOf` but accepts regex patterns
4. Cannot specify a starting offset

# Construction / Recognition
```javascript
"string".search(/pattern/)
```

# Context & Application
Use `search` when you need the position of a pattern match but not the matched text itself.

# Examples
```javascript
console.log("  word".search(/\S/));
// -> 2
console.log("    ".search(/\S/));
// -> -1
```
(Ch 9, "The search method", lines 892-897)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Position-based pattern searching
## Related
- match-method, exec-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting to specify a starting offset like `indexOf`
  **Correction**: "there is no way to indicate that the match should start at a given offset" (Ch 9)

# Common Confusions
- **Confusion**: `search` returns the matched text
  **Clarification**: `search` returns only the index number; use `match` or `exec` for the actual matched text

# Source Reference
Chapter 9: Regular Expressions, Section "The search method", lines 883-902.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
