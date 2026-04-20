---
# === CORE IDENTIFICATION ===
concept: Grouping
slug: grouping

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
section: "Grouping subexpressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - capturing group
  - subexpression
  - parenthesized group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - repetition-operators
extends: []
related:
  - exec-method
  - backreference
  - alternation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I group parts of a regex pattern?"
  - "How do I capture matched substrings?"
---

# Quick Definition
Parentheses in a regex create groups that allow operators to apply to multiple elements as a unit and capture the matched text for extraction.

# Core Definition
Haverbeke explains: "To use an operator like `*` or `+` on more than one element at a time, you must use parentheses. A part of a regular expression that is enclosed in parentheses counts as a single element as far as the operators following it are concerned." Groups also capture their matched text: "When the regular expression contains subexpressions grouped with parentheses, the text that matched those groups will also show up in the array." (Ch 9, "Grouping subexpressions" and "Matches and groups")

# Prerequisites
- **Regular expressions**: Grouping is a regex feature
- **Repetition operators**: Groups allow operators to apply to sequences

# Key Properties
1. `(abc)` makes `abc` a single element for operators
2. Captured group text appears in `exec`/`match` results
3. First group is index 1, second is index 2, etc.
4. `(?:...)` creates a non-capturing group
5. Unmatched optional groups produce `undefined` in results
6. Multiply-matched groups (with `+`) capture only the last match

# Construction / Recognition
```javascript
let cartoonCrying = /boo+(hoo+)+/i;
let quotedText = /'([^']*)'/;
let nonCapturing = /(?:na)+/;
```

# Context & Application
Groups are essential for both structuring complex patterns and extracting specific parts of matched text.

# Examples
```javascript
let cartoonCrying = /boo+(hoo+)+/i;
console.log(cartoonCrying.test("Boohoooohoohooo"));
// -> true

// Capturing groups
let quotedText = /'([^']*)'/;
console.log(quotedText.exec("she said 'hello'"));
// -> ["'hello'", "hello"]

// Non-capturing group
console.log(/(?:na)+/.exec("banana"));
// -> ["nana"]

// Unmatched optional group
console.log(/bad(ly)?/.exec("bad"));
// -> ["bad", undefined]
```
(Ch 9, "Grouping subexpressions" and "Matches and groups", lines 325-421)

# Relationships
## Builds Upon
- regular-expression, repetition-operators
## Enables
- backreference, pattern extraction, alternation scoping
## Related
- exec-method, replace-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting multiply-matched groups to capture all matches
  **Correction**: "When a group is matched multiple times (for example, when followed by a `+`), only the last match ends up in the array." (Ch 9)

# Common Confusions
- **Confusion**: All parentheses create capturing groups
  **Clarification**: Use `(?:...)` for grouping without capturing

# Source Reference
Chapter 9: Regular Expressions, Section "Grouping subexpressions", lines 325-350, and "Matches and groups", lines 351-421.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with multiple examples
- Cross-reference status: verified
