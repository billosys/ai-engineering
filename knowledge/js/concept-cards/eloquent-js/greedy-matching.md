---
# === CORE IDENTIFICATION ===
concept: Greedy Matching
slug: greedy-matching

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
  - greedy quantifier

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - repetition-operators
extends: []
related:
  - lazy-matching
  - backtracking
contrasts_with:
  - lazy-matching

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is greedy matching in regular expressions?"
  - "Why does my regex match more than expected?"
---

# Quick Definition
Greedy matching is the default behavior of repetition operators (`+`, `*`, `?`, `{}`), where they match as much text as possible and backtrack only when the rest of the pattern fails.

# Core Definition
Haverbeke explains: "the repetition operators (`+`, `*`, `?`, and `{}`) are *greedy*, meaning they match as much as they can and backtrack from there." This can lead to unexpected matches when a pattern consumes too much text. (Ch 9, "Greed")

# Prerequisites
- **Regular expressions**: Greedy behavior applies to regex repetition
- **Repetition operators**: Understanding `+`, `*`, `?`, `{}`

# Key Properties
1. Default behavior for `+`, `*`, `?`, `{}`
2. Matches the maximum possible text first
3. Backtracks if the rest of the pattern fails
4. Can cause incorrect matches when not carefully considered

# Construction / Recognition
Greedy is the default -- no special syntax needed. Recognized when a pattern matches more text than intended.

# Context & Application
Understanding greedy behavior is crucial for writing correct regex. Many bugs come from unintentionally greedy operators.

# Examples
```javascript
// Greedy: matches too much
function stripComments(code) {
  return code.replace(/\/\/.*|\/\*[^]*\*\//g, "");
}
console.log(stripComments("1 /* a */+/* b */ 1"));
// -> 1  1  (WRONG -- matched from first /* to last */)
```
The `[^]*` greedily matches everything, including `*/+/*`, only stopping at the LAST `*/`. (Ch 9, "Greed", lines 778-812)

# Relationships
## Builds Upon
- regular-expression, repetition-operators
## Enables
- Understanding of regex matching behavior
## Related
- backtracking
## Contrasts With
- lazy-matching (matches minimum instead)

# Common Errors
- **Error**: Using greedy operators when lazy ones are needed
  **Correction**: "A lot of bugs in regular expression programs can be traced to unintentionally using a greedy operator where a nongreedy one would work better." (Ch 9)

# Common Confusions
- **Confusion**: Greedy matching always causes problems
  **Clarification**: Greedy matching is correct for many patterns; it only causes issues when you want the shortest possible match

# Source Reference
Chapter 9: Regular Expressions, Section "Greed", lines 771-839.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with concrete example of the problem
- Cross-reference status: verified
