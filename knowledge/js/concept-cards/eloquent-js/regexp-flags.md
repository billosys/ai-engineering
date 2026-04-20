---
# === CORE IDENTIFICATION ===
concept: RegExp Flags
slug: regexp-flags

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
section: "Summary"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex options
  - regex modifiers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - regexp-literal
  - regexp-constructor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What flags can I use with regular expressions?"
  - "What does the g flag do?"
---

# Quick Definition
RegExp flags are options written after the closing slash of a regex literal (or as the second argument to `RegExp`) that modify matching behavior: `i` for case-insensitive, `g` for global, `y` for sticky, and `u` for Unicode mode.

# Core Definition
Haverbeke summarizes: "The `i` option makes the match case insensitive. The `g` option makes the expression *global*, which, among other things, causes the `replace` method to replace all instances instead of just the first. The `y` option makes an expression sticky, which means that it will not search ahead and skip part of the string when looking for a match. The `u` option turns on Unicode mode, which enables `\\p` syntax and fixes a number of problems around the handling of characters that take up two code units." (Ch 9, "Summary")

# Prerequisites
- **Regular expressions**: Flags modify regex behavior

# Key Properties
1. `i` : case-insensitive matching
2. `g` : global matching (find all matches, not just the first)
3. `y` : sticky (match must start at `lastIndex` exactly)
4. `u` : Unicode mode (correct handling of multi-code-unit characters, enables `\p`)
5. Multiple flags can be combined: `/pattern/giu`

# Construction / Recognition
```javascript
/pattern/i    // case-insensitive
/pattern/g    // global
/pattern/gi   // global + case-insensitive
/pattern/u    // unicode mode
```

# Context & Application
Flags are essential for controlling regex behavior. The `g` flag is critical for `replace` to replace all occurrences, and `u` is important for correct Unicode handling.

# Examples
```javascript
let cartoonCrying = /boo+(hoo+)+/i;
console.log(cartoonCrying.test("Boohoooohoohooo"));
// -> true (case-insensitive matches uppercase B)

console.log("Borobudur".replace(/[ou]/g, "a"));
// -> Barabadar (global replaces ALL matches)

console.log(/🍎{3}/u.test("🍎🍎🍎"));
// -> true (u flag handles multi-code-unit characters)
```
(Ch 9, various sections)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Global replacement, case-insensitive matching, Unicode support
## Related
- regexp-literal, regexp-constructor
## Contrasts With
- N/A

# Common Errors
- **Error**: Forgetting `g` flag with `replace` and expecting all matches to be replaced
  **Correction**: Without `g`, only the first match is replaced

# Common Confusions
- **Confusion**: The `g` flag on `exec` is stateless
  **Clarification**: With `g`, `exec` updates `lastIndex` after each call, which can cause bugs if the regex is reused

# Source Reference
Chapter 9: Regular Expressions, Section "Summary", lines 1215-1223.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly summarized in the chapter summary
- Cross-reference status: verified
