---
# === CORE IDENTIFICATION ===
concept: Replace Method
slug: replace-method

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
section: "The replace method"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - String.prototype.replace

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
  - grouping
  - regexp-flags
extends: []
related:
  - match-method
  - search-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I replace text using regular expressions?"
---

# Quick Definition
The string `replace` method replaces matches of a pattern (string or regex) with a replacement string or function, supporting group references (`$1`, `$2`) and global replacement with the `g` flag.

# Core Definition
Haverbeke explains: "String values have a `replace` method that can be used to replace part of the string with another string." With regex: "The first argument can also be a regular expression, in which case the first match of the regular expression is replaced. When a `g` option (for *global*) is added... *all* matches in the string will be replaced." (Ch 9, "The replace method")

# Prerequisites
- **Regular expressions**: Used as the first argument for pattern-based replacement
- **Grouping**: Captured groups can be referenced in the replacement
- **RegExp flags**: `g` flag enables global replacement

# Key Properties
1. First match only by default; all matches with `g` flag
2. `$1`, `$2` etc. reference captured groups in the replacement string
3. `$&` references the whole match
4. A function can be used as the second argument for complex replacements
5. The function receives the full match and captured groups as arguments

# Construction / Recognition
```javascript
"string".replace(/pattern/g, "replacement")
"string".replace(/(\w+), (\w+)/g, "$2 $1")
"string".replace(/pattern/g, function(match) { ... })
```

# Context & Application
`replace` is one of the most powerful string manipulation tools, combining pattern matching with transformation.

# Examples
```javascript
console.log("Borobudur".replace(/[ou]/g, "a"));
// -> Barabadar

// Group references
console.log(
  "Liskov, Barbara\nMcCarthy, John\nMilner, Robin"
    .replace(/(\p{L}+), (\p{L}+)/gu, "$2 $1"));
// -> Barbara Liskov
//    John McCarthy
//    Robin Milner

// Function replacement
let stock = "1 lemon, 2 cabbages, and 101 eggs";
function minusOne(match, amount, unit) {
  amount = Number(amount) - 1;
  if (amount == 1) unit = unit.slice(0, unit.length - 1);
  else if (amount == 0) amount = "no";
  return amount + " " + unit;
}
console.log(stock.replace(/(\d+) (\p{L}+)/gu, minusOne));
// -> no lemon, 1 cabbage, and 100 eggs
```
(Ch 9, "The replace method", lines 684-769)

# Relationships
## Builds Upon
- regular-expression, grouping, regexp-flags
## Enables
- Text transformation, parsing, formatting
## Related
- match-method, search-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Forgetting the `g` flag when all occurrences should be replaced
  **Correction**: Without `g`, only the first match is replaced

# Common Confusions
- **Confusion**: `$1` in the replacement string is a JavaScript variable
  **Clarification**: `$1` is special replacement syntax, not a JavaScript expression; it references the first captured group

# Source Reference
Chapter 9: Regular Expressions, Section "The replace method", lines 684-769.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with multiple examples
- Cross-reference status: verified
