---
# === CORE IDENTIFICATION ===
concept: Repetition Operators
slug: repetition-operators

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
section: "Repeating parts of a pattern"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - quantifiers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - character-class
extends: []
related:
  - greedy-matching
  - lazy-matching
  - grouping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match repeated patterns?"
  - "What do +, *, and ? mean in regex?"
---

# Quick Definition
Repetition operators (`+`, `*`, `?`, `{n,m}`) specify how many times the preceding element can occur in a match: one-or-more, zero-or-more, optional, or a specific count range.

# Core Definition
Haverbeke explains: "`+` after something in a regular expression... indicates that the element may be repeated more than once." The star (`*`) "also allows the pattern to match zero times." The question mark (`?`) "makes a part of a pattern *optional*, meaning it may occur zero times or one time." Braces specify exact counts: "`{4}` after an element... requires it to occur exactly four times" and "`{2,4}` means the element must occur at least twice and at most four times." (Ch 9, "Repeating parts of a pattern")

# Prerequisites
- **Regular expressions**: Operators apply to regex elements
- **Character classes**: Often repeated with these operators

# Key Properties
1. `+` : one or more times
2. `*` : zero or more times
3. `?` : zero or one time (optional)
4. `{n}` : exactly n times
5. `{n,m}` : n to m times
6. `{n,}` : n or more times
7. By default, operators are greedy (match as much as possible)

# Construction / Recognition
```javascript
/\d+/     // one or more digits
/\d*/     // zero or more digits
/colou?r/ // optional u
/\d{4}/   // exactly 4 digits
/\d{1,2}/ // 1 or 2 digits
```

# Context & Application
Repetition operators are essential for matching variable-length patterns like numbers, words, or repeated structures.

# Examples
```javascript
console.log(/'\d+'/.test("'123'"));  // -> true
console.log(/'\d+'/.test("''"));     // -> false
console.log(/'\d*'/.test("'123'"));  // -> true
console.log(/'\d*'/.test("''"));     // -> true

let neighbor = /neighbou?r/;
console.log(neighbor.test("neighbour")); // -> true
console.log(neighbor.test("neighbor"));  // -> true

let dateTime = /\d{1,2}-\d{1,2}-\d{4} \d{1,2}:\d{2}/;
console.log(dateTime.test("1-30-2003 8:45"));
// -> true
```
(Ch 9, "Repeating parts of a pattern", lines 258-323)

# Relationships
## Builds Upon
- regular-expression, character-class
## Enables
- greedy-matching, lazy-matching
## Related
- grouping (operators can apply to groups)
## Contrasts With
- N/A

# Common Errors
- **Error**: Confusing `+` (one or more) with `*` (zero or more)
  **Correction**: Use `+` when at least one occurrence is required; `*` when the element is entirely optional

# Common Confusions
- **Confusion**: `{5,}` means exactly 5
  **Clarification**: `{5,}` means 5 or MORE times; `{5}` means exactly 5

# Source Reference
Chapter 9: Regular Expressions, Section "Repeating parts of a pattern", lines 258-323.

# Verification Notes
- Definition source: direct
- Confidence rationale: Each operator explicitly defined with examples
- Cross-reference status: verified against summary table
