---
# === CORE IDENTIFICATION ===
concept: Lazy Matching
slug: lazy-matching

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-behavior
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "Greed"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - nongreedy matching
  - lazy quantifier
  - reluctant quantifier

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - repetition-operators
  - greedy-matching
extends: []
related:
  - backtracking
contrasts_with:
  - greedy-matching

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a regex match as little as possible?"
---

# Quick Definition
Lazy (nongreedy) matching is activated by adding `?` after a repetition operator (`+?`, `*?`, `??`, `{}?`), making it match as little as possible and expanding only when the rest of the pattern doesn't fit.

# Core Definition
Haverbeke explains: "If you put a question mark after them (`+?`, `*?`, `??`, `{}?`), they become nongreedy and start by matching as little as possible, matching more only when the remaining pattern does not fit the smaller match." He advises: "When using a repetition operator, prefer the nongreedy variant." (Ch 9, "Greed")

# Prerequisites
- **Regular expressions**: Lazy matching is a regex feature
- **Repetition operators**: Lazy modifies repetition behavior
- **Greedy matching**: Understanding why the default is problematic

# Key Properties
1. `+?` : one or more, but as few as possible
2. `*?` : zero or more, but as few as possible
3. `??` : zero or one, preferring zero
4. `{}?` : specified range, preferring minimum
5. Expands only when necessary

# Construction / Recognition
```javascript
/[^]*?/   // matches as little as possible
/\d+?/    // matches fewest digits
```

# Context & Application
Lazy matching solves the common problem of greedy operators matching too much text, especially in nested or repeated delimiters.

# Examples
```javascript
// Fixed comment stripping with lazy matching
function stripComments(code) {
  return code.replace(/\/\/.*|\/\*[^]*?\*\//g, "");
}
console.log(stripComments("1 /* a */+/* b */ 1"));
// -> 1 + 1  (CORRECT)
```
By using `[^]*?` instead of `[^]*`, each `/* ... */` is matched individually. (Ch 9, "Greed", lines 827-833)

# Relationships
## Builds Upon
- regular-expression, repetition-operators, greedy-matching
## Enables
- Precise pattern matching with repeated delimiters
## Related
- backtracking
## Contrasts With
- greedy-matching (matches maximum instead of minimum)

# Common Errors
- **Error**: Using lazy matching everywhere unnecessarily
  **Correction**: Use lazy matching specifically when you need the shortest match; greedy is appropriate and often faster for many patterns

# Common Confusions
- **Confusion**: `??` is the same as `?`
  **Clarification**: `?` is greedy optional (prefer matching); `??` is lazy optional (prefer NOT matching)

# Source Reference
Chapter 9: Regular Expressions, Section "Greed", lines 815-839.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined as the solution to greedy matching problems
- Cross-reference status: verified
