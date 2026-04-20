---
# === CORE IDENTIFICATION ===
concept: Exec Method
slug: exec-method

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
section: "Matches and groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - execute method

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - grouping
extends: []
related:
  - test-method
  - match-method
contrasts_with:
  - test-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I extract match information from a regular expression?"
---

# Quick Definition
The `exec` method on a RegExp returns `null` if no match is found, or an array-like object containing the matched string, captured groups, and an `index` property indicating where the match starts.

# Core Definition
Haverbeke explains: "Regular expressions also have an `exec` (execute) method that will return `null` if no match was found and return an object with information about the match otherwise." The returned object "looks like (and in fact is) an array of strings, whose first element is the string that was matched." It also has an `index` property. (Ch 9, "Matches and groups")

# Prerequisites
- **Regular expressions**: `exec` is a RegExp method
- **Grouping**: Captured groups appear in the result array

# Key Properties
1. Returns `null` on no match
2. Returns an array with the full match as element 0
3. Subsequent elements contain captured group matches
4. Has an `index` property indicating match position
5. With `g` flag, updates `lastIndex` on the regex object

# Construction / Recognition
```javascript
let match = /\d+/.exec("one two 100");
console.log(match);       // -> ["100"]
console.log(match.index);  // -> 8
```

# Context & Application
Use `exec` when you need match details: position, captured groups, or iterating through multiple matches.

# Examples
```javascript
let match = /\d+/.exec("one two 100");
console.log(match);       // -> ["100"]
console.log(match.index); // -> 8

// With groups
let quotedText = /'([^']*)'/;
console.log(quotedText.exec("she said 'hello'"));
// -> ["'hello'", "hello"]
```
(Ch 9, "Matches and groups", lines 360-397)

# Relationships
## Builds Upon
- regular-expression, grouping
## Enables
- Pattern extraction, parsing
## Related
- match-method, test-method
## Contrasts With
- test-method (boolean only)

# Common Errors
- **Error**: Not checking for `null` before accessing match properties
  **Correction**: Always check if `exec` returned `null` before accessing `index` or group elements

# Common Confusions
- **Confusion**: `exec` with `g` flag is stateless
  **Clarification**: With the `g` flag, `exec` updates `lastIndex` on the regex, which affects subsequent calls

# Source Reference
Chapter 9: Regular Expressions, Section "Matches and groups", lines 351-411.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
