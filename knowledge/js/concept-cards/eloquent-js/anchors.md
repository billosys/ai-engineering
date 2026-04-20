---
# === CORE IDENTIFICATION ===
concept: Anchors
slug: anchors

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
section: "Boundaries and look-ahead"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - boundary markers
  - start/end markers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - word-boundary
  - lookahead
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match the start or end of a string?"
  - "How do I ensure a regex matches the whole string?"
---

# Quick Definition
The caret (`^`) matches the start of the input string and the dollar sign (`$`) matches the end, allowing patterns to be anchored to specific positions.

# Core Definition
Haverbeke explains: "The caret matches the start of the input string, whereas the dollar sign matches the end. Thus `/^\\d+$/` matches a string consisting entirely of one or more digits." He adds: "these boundary markers don't match any actual characters. They just enforce that a given condition holds at the place where it appears in the pattern." (Ch 9, "Boundaries and look-ahead")

# Prerequisites
- **Regular expressions**: Anchors are regex syntax elements

# Key Properties
1. `^` matches start of input
2. `$` matches end of input
3. They don't consume any characters (zero-width)
4. `/^\d+$/` matches a string consisting entirely of digits
5. `/^!/` matches strings starting with `!`
6. `/x^/` never matches (nothing can precede the start)

# Construction / Recognition
```javascript
/^\d+$/  // entire string is digits
/^!/     // starts with !
```

# Context & Application
Anchors are essential when you need to match the entire string or ensure patterns appear at specific positions. The INI parser example uses them extensively.

# Examples
```javascript
// Ensuring whole-line matching in the INI parser
if (match = line.match(/^(\w+)=(.*)$/)) {
  section[match[1]] = match[2];
} else if (match = line.match(/^\[(.*)\]$/)) {
  section = result[match[1]] = {};
}
```
"Note the recurring use of `^` and `$` to make sure the expression matches the whole line, not just part of it." (Ch 9, "Parsing an INI file", lines 1115-1118)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Whole-string matching, position-specific matching
## Related
- word-boundary, lookahead
## Contrasts With
- N/A

# Common Errors
- **Error**: Omitting anchors when matching should span the whole string
  **Correction**: "Leaving these out results in code that mostly works but behaves strangely for some input, which can be a difficult bug to track down." (Ch 9)

# Common Confusions
- **Confusion**: `^` inside `[...]` means start of string
  **Clarification**: Inside character classes, `^` means negation (`[^0-9]`); outside, it means start of string

# Source Reference
Chapter 9: Regular Expressions, Section "Boundaries and look-ahead", lines 516-543.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified against INI parser example
