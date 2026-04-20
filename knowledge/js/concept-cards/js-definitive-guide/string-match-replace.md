---
concept: String Pattern Matching Methods
slug: string-match-replace
category: standard-library
subcategory: pattern-matching
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 309
section: "11.3.2 String Methods for Pattern Matching"
extraction_confidence: high
aliases:
  - "String.match()"
  - "String.replace()"
  - "String.search()"
  - "String.matchAll()"
  - "String.split()"
prerequisites:
  - regexp-syntax
extends: []
related:
  - regexp-test-exec
  - regexp-capture-groups
contrasts_with: []
answers_questions: []
---

# Quick Definition

The String methods `search()`, `replace()`, `match()`, `matchAll()`, and `split()` that use regular expressions for pattern matching, searching, replacing, and splitting text.

# Core Definition

Five String methods work with regular expressions: `search()` returns the index of the first match; `replace()` performs search-and-replace; `match()` returns match results (behavior differs with/without `g` flag); `matchAll()` (ES2020) returns an iterator of all match objects; `split()` breaks a string using a regexp delimiter.

# Prerequisites

- **regexp-syntax** — Understanding regular expressions is needed to use these methods

# Key Properties

1. `search()` — returns index of first match or -1; ignores `g` flag
2. `replace()` — replaces first match (or all with `g` flag); supports `$1`, `$<name>` in replacement
3. `match()` with `g` — returns array of all matching strings
4. `match()` without `g` — returns detailed match object with groups and index
5. `matchAll()` (ES2020) — returns iterator of match objects; requires `g` flag; never modifies `lastIndex`
6. `replace()` accepts a function as second argument for computed replacements

# Construction / Recognition

```js
"JavaScript".search(/script/ui)               // => 4
"7 plus 8 equals 15".match(/\d+/g)            // => ["7", "8", "15"]
text.replace(/javascript/gi, "JavaScript")
s.replace(/\d+/gu, n => parseInt(n).toString(16))
for(let word of text.matchAll(words)) { ... }
"1, 2, 3".split(/\s*,\s*/)                    // => ["1","2","3"]
```

# Context & Application

These are the primary methods for text processing in JavaScript. `matchAll()` is the preferred modern approach for iterating over all matches, replacing the older `exec()` loop pattern.

# Examples

From the source text (p. 310-314): `replace()` with capture groups: `'He said "stop"'.replace(/"([^"]*)"/, '<<$1>>')`. Named capture replacement: `'He said "stop"'.replace(/"(?<quotedText>[^"]*)"/, '<<$<quotedText>>>')`. Function replacement: `s.replace(/\d+/gu, n => parseInt(n).toString(16))` converts decimal to hex.

# Relationships

## Builds Upon
- **RegExp Syntax** — These methods take RegExp arguments

## Related
- **RegExp test/exec** — RegExp-side methods for matching
- **Capture Groups** — Captured text available in match results and replacements

# Common Errors

- **Error**: Expecting `match()` with the `g` flag to return capture group information.
  **Correction**: With `g`, `match()` only returns an array of full match strings. Use `matchAll()` to get capture groups for each match.

# Common Confusions

- **Confusion**: Thinking `match()` and `matchAll()` return the same type.
  **Clarification**: `match()` with `g` returns a simple array of strings. `matchAll()` returns an iterator of detailed match objects (like non-global `match()` results).

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.3.2, pages 309-314.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — thorough coverage
- Uncertainties: None
- Cross-reference status: Verified
