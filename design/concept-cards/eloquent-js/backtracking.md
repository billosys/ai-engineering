---
# === CORE IDENTIFICATION ===
concept: Backtracking
slug: backtracking

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-behavior
tier: advanced

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "Backtracking"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - repetition-operators
  - alternation
extends: []
related:
  - greedy-matching
  - lazy-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the regex engine handle multiple possible matches?"
  - "Why can some regular expressions be extremely slow?"
---

# Quick Definition
Backtracking is the regex engine's process of remembering decision points and returning to try alternative paths when the current path fails to produce a match.

# Core Definition
Haverbeke explains: "the matcher *backtracks*. When entering a branch, it remembers its current position... so that it can go back and try another branch if the current one does not work out." Backtracking also occurs with repetition operators: "If you match `/^.*x/` against `\"abcxe\"`, the `.*` part will first try to consume the whole string. The engine will then realize that it needs an `x` to match the pattern... so it backtracks again." (Ch 9, "Backtracking")

# Prerequisites
- **Regular expressions**: Backtracking is a regex engine behavior
- **Repetition operators**: Trigger backtracking when they consume too much
- **Alternation**: Branches trigger backtracking when a branch fails

# Key Properties
1. Engine remembers positions at choice points (branches, repetitions)
2. When current path fails, returns to last choice point and tries next option
3. First successful full match is returned
4. Catastrophic backtracking can occur with nested repetition: `/([01]+)+b/`
5. The amount of work can double with each additional character in bad patterns

# Construction / Recognition
Backtracking is an internal engine behavior, but its effects are visible when patterns are slow or match unexpectedly.

# Context & Application
Understanding backtracking is essential for writing efficient regex and avoiding catastrophic performance. Nested repetition operators are particularly dangerous.

# Examples
```javascript
// Catastrophic backtracking example
// /([01]+)+b/ on a long string of 0s and 1s with no trailing b
// will try every possible way to split the digits between inner
// and outer loops -- the work DOUBLES with each character

// Backtracking with greedy operators
// /^.*x/ against "abcxe":
// .* first matches "abcxe" (greedy)
// No x after that, backtrack to "abcx"
// No x after that, backtrack to "abc"
// Found x! Match "abcx"
```
(Ch 9, "Backtracking", lines 616-682)

# Relationships
## Builds Upon
- regular-expression, repetition-operators, alternation
## Enables
- Understanding of regex performance characteristics
## Related
- greedy-matching, lazy-matching
## Contrasts With
- N/A

# Common Errors
- **Error**: Writing patterns with nested repetition like `(a+)+`
  **Correction**: Avoid nested quantifiers that can match the same text in exponentially many ways

# Common Confusions
- **Confusion**: Regex matching is always fast
  **Clarification**: Poorly written patterns can cause catastrophic backtracking with exponential time complexity

# Source Reference
Chapter 9: Regular Expressions, Section "Backtracking", lines 616-682.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with detailed explanation and performance warning
- Cross-reference status: verified
