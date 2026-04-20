---
# === CORE IDENTIFICATION ===
concept: Alternation
slug: alternation

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
section: "Choice patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - pipe operator
  - choice pattern
  - OR in regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - grouping
extends: []
related:
  - character-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match one of several alternative patterns?"
---

# Quick Definition
The pipe character (`|`) in a regex denotes a choice between the pattern to its left and the pattern to its right, matching if either alternative matches.

# Core Definition
Haverbeke explains: "The pipe character (`|`) denotes a choice between the pattern to its left and the pattern to its right." And: "Parentheses can be used to limit the part of the pattern to which the pipe operator applies, and you can put multiple such operators next to each other to express a choice between more than two alternatives." (Ch 9, "Choice patterns")

# Prerequisites
- **Regular expressions**: Alternation is a regex operator
- **Grouping**: Parentheses scope the alternation

# Key Properties
1. `a|b` matches either `a` or `b`
2. Parentheses limit the scope: `(pig|cow|chicken)` matches one of three words
3. Without parentheses, `|` applies to the entire expression on each side
4. The matcher tries the first alternative first; if it matches, later alternatives are not considered

# Construction / Recognition
```javascript
/\d+ (pig|cow|chicken)s?/
```

# Context & Application
Alternation is used when a pattern needs to match one of several possible forms.

# Examples
```javascript
let animalCount = /\d+ (pig|cow|chicken)s?/;
console.log(animalCount.test("15 pigs"));
// -> true
console.log(animalCount.test("15 pugs"));
// -> false
```
(Ch 9, "Choice patterns", lines 578-584)

# Relationships
## Builds Upon
- regular-expression, grouping
## Enables
- Complex multi-pattern matching
## Related
- character-class (for single-character alternation)
## Contrasts With
- N/A

# Common Errors
- **Error**: Forgetting to use parentheses to scope the alternation
  **Correction**: Without parentheses, `abc|def` matches "abc" OR "def" as complete alternatives, not "ab(c|d)ef"

# Common Confusions
- **Confusion**: `|` works like `||` in JavaScript (short-circuit OR)
  **Clarification**: In regex, `|` tries the first branch; if it matches, the second is ignored (but if the first fails, the second is tried)

# Source Reference
Chapter 9: Regular Expressions, Section "Choice patterns", lines 565-591.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
