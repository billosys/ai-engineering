---
# === CORE IDENTIFICATION ===
concept: RegExp Constructor
slug: regexp-constructor

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
section: "Creating a regular expression"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - RegExp function
  - dynamic regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - regexp-literal
  - regexp-flags
contrasts_with:
  - regexp-literal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a regular expression dynamically?"
---

# Quick Definition
The `RegExp` constructor creates regular expressions from strings, allowing patterns to be built dynamically at runtime, with the second argument specifying flags.

# Core Definition
Haverbeke explains: "When using the `RegExp` constructor, the pattern is written as a normal string, so the usual rules apply for backslashes." The constructor is useful "in some cases you may not know the exact pattern you need to match against when you are writing your code." (Ch 9)

# Prerequisites
- **Regular expressions**: Understanding regex patterns

# Key Properties
1. Takes a pattern string and optional flags string
2. Backslashes in the string must be doubled (`\\s` instead of `\s`)
3. Useful for dynamic pattern construction
4. Second argument specifies flags: `"gi"` for global + case-insensitive

# Construction / Recognition
```javascript
let re1 = new RegExp("abc");
let name = "harry";
let regexp = new RegExp("(^|\\s)" + name + "($|\\s)", "gi");
```

# Context & Application
Use `RegExp` constructor when patterns need to incorporate variables or are built from user input.

# Examples
```javascript
let name = "harry";
let regexp = new RegExp("(^|\\s)" + name + "($|\\s)", "gi");
console.log(regexp.test("Harry is a dodgy character."));
// -> true

// Escaping special characters in dynamic input
let name = "dea+hl[]rd";
let escaped = name.replace(/[\\[.+*?(){|^$]/g, "\\$&");
let regexp = new RegExp("(^|\\s)" + escaped + "($|\\s)", "gi");
```
(Ch 9, "Dynamically creating RegExp objects", lines 841-881)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Dynamic pattern matching
## Related
- regexp-literal, regexp-flags
## Contrasts With
- regexp-literal (for static patterns)

# Common Errors
- **Error**: Forgetting to double backslashes in the pattern string
  **Correction**: Use `\\s` not `\s` in strings passed to `RegExp`; `\s` is just `s` in a regular string

# Common Confusions
- **Confusion**: Dynamic patterns with special characters in user input are safe
  **Clarification**: User input must be escaped before inclusion in a pattern; special regex characters like `+`, `*`, `[` will break the pattern

# Source Reference
Chapter 9: Regular Expressions, Sections "Creating a regular expression" and "Dynamically creating RegExp objects", lines 51-88, 841-881.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with dynamic construction examples
- Cross-reference status: verified
