---
# === CORE IDENTIFICATION ===
concept: Match Method
slug: match-method

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
section: "Matches and groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - String.prototype.match

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - exec-method
  - search-method
  - replace-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use string match with regular expressions?"
---

# Quick Definition
The string `match` method tests a string against a regex and returns a match result similar to `exec`, or with the `g` flag returns an array of all matched strings.

# Core Definition
Haverbeke explains: "String values have a `match` method that behaves similarly [to exec]." With the global flag, "instead of returning an array similar to that returned by `exec`, `match` will find *all* matches of the pattern in the string and return an array containing the matched strings." (Ch 9)

# Prerequisites
- **Regular expressions**: The argument to match

# Key Properties
1. Without `g`: returns result like `exec` (with groups and index)
2. With `g`: returns array of all matched strings (no groups or index)
3. `matchAll` returns an array of match arrays (with groups), requires `g`

# Construction / Recognition
```javascript
"string".match(/pattern/)
"string".match(/pattern/g)
```

# Context & Application
Use `match` for simple pattern extraction from strings.

# Examples
```javascript
console.log("one two 100".match(/\d+/));
// -> ["100"]

console.log("Banana".match(/an/g));
// -> ["an", "an"]

// matchAll for detailed global matching
let input = "A string with 3 numbers in it... 42 and 88.";
let matches = input.matchAll(/\d+/g);
for (let match of matches) {
  console.log("Found", match[0], "at", match.index);
}
// -> Found 3 at 14
// -> Found 42 at 33
// -> Found 88 at 40
```
(Ch 9, lines 380-383, 979-1004)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Pattern extraction, text search
## Related
- exec-method, search-method, replace-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting group captures when using `g` flag with `match`
  **Correction**: With `g`, `match` returns only matched strings without groups; use `matchAll` for groups with global matching

# Common Confusions
- **Confusion**: `match` and `exec` always return the same thing
  **Clarification**: With the `g` flag, `match` returns all matches as strings, while `exec` returns one detailed match at a time

# Source Reference
Chapter 9: Regular Expressions, Section "Matches and groups", lines 377-383, and "The lastIndex property", lines 972-1009.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
