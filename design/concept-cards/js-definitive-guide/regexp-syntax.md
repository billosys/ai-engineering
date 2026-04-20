---
concept: Regular Expression Syntax and Flags
slug: regexp-syntax
category: standard-library
subcategory: pattern-matching
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 298
section: "11.3.1 Defining Regular Expressions"
extraction_confidence: high
aliases:
  - "RegExp"
  - "regex"
  - "regular expressions"
prerequisites: []
extends: []
related:
  - regexp-capture-groups
  - string-match-replace
  - regexp-test-exec
contrasts_with: []
answers_questions: []
---

# Quick Definition

JavaScript's pattern-matching language for text, using the RegExp class with literal syntax (`/pattern/flags`) or the `RegExp()` constructor, supporting six flags (`g`, `i`, `m`, `s`, `u`, `y`) that control matching behavior.

# Core Definition

"A regular expression is an object that describes a textual pattern" (p. 298). RegExp literals use `/pattern/flags` syntax. The six flags are: `g` (global), `i` (case-insensitive), `m` (multiline), `s` (dotAll), `u` (Unicode), `y` (sticky). Patterns include character classes (`\d`, `\w`, `\s`), repetition (`+`, `*`, `?`, `{n,m}`), alternation (`|`), grouping (`()`), and anchors (`^`, `$`, `\b`).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Literal syntax `/pattern/flags` or constructor `new RegExp("pattern", "flags")`
2. Six flags: `g` (global), `i` (ignore case), `m` (multiline anchors), `s` (dotAll), `u` (Unicode), `y` (sticky)
3. Character classes: `\d` (digit), `\w` (word), `\s` (whitespace), `[abc]`, `[^abc]`
4. Repetition: `*` (0+), `+` (1+), `?` (0-1), `{n,m}` (n to m times)
5. Non-greedy repetition: `*?`, `+?`, `??`
6. Anchors: `^` (start), `$` (end), `\b` (word boundary)
7. Lookahead `(?=...)` and `(?!...)`, lookbehind `(?<=...)` and `(?<!...)` (ES2018)

# Construction / Recognition

```js
let pattern = /s$/i;
let zipcode = new RegExp("\\d{5}", "g");
```

# Context & Application

Used throughout JavaScript for text search, validation, parsing, and replacement. The `u` flag should be used habitually for correct Unicode handling.

# Examples

From the source text (p. 299-309): `/\d{2,4}/` matches 2-4 digits. `/\s+java\s+/` matches "java" with surrounding whitespace. Non-greedy: `/a+?/` matches minimum a's. Lookahead: `/[Jj]ava([Ss]cript)?(?=\:)/` matches "JavaScript" only before a colon.

# Relationships

## Enables
- **Capture Groups** — Parenthesized groups within patterns
- **String match/replace** — String methods that use RegExp
- **RegExp test/exec** — RegExp methods for matching

# Common Errors

- **Error**: Forgetting to double backslashes when using `new RegExp("\\d+")`.
  **Correction**: String literals also use `\` as escape, so `\d` must be written as `"\\d"` in the constructor.

# Common Confusions

- **Confusion**: Expecting `/a*/` to fail on the string "bbbb".
  **Clarification**: `*` matches zero or more occurrences, so `/a*/` matches zero a's in "bbbb" — it matches the empty string at position 0.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.3.1, pages 298-309.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — extensive treatment
- Uncertainties: None
- Cross-reference status: Verified
