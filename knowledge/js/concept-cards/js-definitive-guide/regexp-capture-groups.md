---
concept: Capture Groups and Named Capture Groups
slug: regexp-capture-groups
category: standard-library
subcategory: pattern-matching
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 304
section: "11.3.1 Defining Regular Expressions"
extraction_confidence: high
aliases:
  - "capturing groups"
  - "named groups"
  - "backreferences"
prerequisites:
  - regexp-syntax
extends: []
related:
  - string-match-replace
contrasts_with: []
answers_questions: []
---

# Quick Definition

Parenthesized subexpressions in regular expressions that capture matched text for later reference — either by number (`\1`, `$1`) or by name (`\k<name>`, `$<name>`) using ES2018 named capture syntax `(?<name>...)`.

# Core Definition

Parentheses in regular expressions serve three roles: grouping for repetition operators, capturing matched text for backreferences, and defining named captures. Numbered references use `\1`, `\2`, etc. within the pattern and `$1`, `$2` in replacement strings. Non-capturing groups `(?:...)` group without capturing. ES2018 named groups use `(?<name>...)` syntax with `\k<name>` backreferences.

# Prerequisites

- **regexp-syntax** — Capture groups are part of regular expression syntax

# Key Properties

1. `()` captures and groups; `(?:)` groups without capturing
2. Numbered by counting left parentheses from left to right
3. `\1`, `\2` backreferences within the pattern refer to matched text (not pattern)
4. Named captures: `(?<city>\w+)` accessed via `match.groups.city`
5. Named backreferences: `\k<quote>` refers back to `(?<quote>...)`

# Construction / Recognition

```js
/(?<city>\w+) (?<state>[A-Z]{2}) (?<zipcode>\d{5})(?<zip9>-\d{4})?/
/(?<quote>['"])[^'"]*\k<quote>/
```

# Context & Application

Essential for extracting structured data from text, enforcing consistency (matching quotes), and building readable patterns with named groups.

# Examples

From the source text (p. 304-306): Matching quotes: `/(['"])[^'"]*\1/` ensures opening and closing quotes match. Named capture for URL parsing: `/(?<protocol>\w+):\/\/(?<host>[\w.]+)\/(?<path>\S*)/` allows `match.groups.protocol`. Named backreference: `/(?<quote>['"])[^'"]*\k<quote>/`.

# Relationships

## Builds Upon
- **RegExp Syntax** — Capture groups are part of regular expression grammar

## Enables
- **String match/replace** — Captured groups appear in match results and replacement strings

# Common Errors

- **Error**: Using a backreference inside a character class: `/(['"])[^\1]*\1/`.
  **Correction**: Backreferences are not allowed inside character classes `[...]`.

# Common Confusions

- **Confusion**: Thinking `\1` refers to the pattern of the first group.
  **Clarification**: `\1` refers to the *text* that was matched by the first group, not the pattern. This enforces that the same text appears again.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.3.1, pages 304-306.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — well explained with examples
- Uncertainties: None
- Cross-reference status: Verified
