---
# === CORE IDENTIFICATION ===
concept: Smart Quotes Regex
slug: smart-quotes-regex

# === CLASSIFICATION ===
category: regular-expressions
subcategory: lookaround
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions: lookaround assertions by example"
chapter_number: 17
section: "17.9 Example: smart quotes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - curly quotes conversion
  - typographic quotes regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-lookbehind
  - negative-lookbehind
  - greedy-vs-reluctant-quantifier
extends: []
related:
  - negative-lookaround-guard
  - inward-pointing-lookaround
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use lookaround assertions for complex text transformation?"
---

# Quick Definition

The smart quotes regex is a worked example that progressively builds a regular expression using lookbehind assertions and reluctant quantifiers to convert straight double quotes to curly (typographic) quotes, handling edge cases like escaped quotes and backslashes.

# Core Definition

As developed in "Deep JavaScript" (Ch 17, Section 17.9): The example starts with a naive approach using reluctant matching `"(.*?)"` and progressively adds complexity. Backslash-escaped quotes are handled with `(?<!\\)` lookbehind guards. Double-escaped backslashes (e.g., `\\`) before quotes require a more sophisticated guard: `(?<=[^\\](?:\\\\)*)`. Finally, the pattern is adjusted to handle quotes at the start of strings with `(?<=[^\\](?:\\\\)*|^)`.

# Prerequisites

- **Positive lookbehind** — Used in the advanced guard pattern.
- **Negative lookbehind** — Used to skip escaped quotes.
- **Greedy vs. reluctant quantifiers** — `*?` for matching between nearest quote pairs.

# Key Properties

1. Progressive complexity: each version handles one more edge case.
2. Reluctant `.*?` correctly matches individual quoted phrases.
3. `(?<!\\)` guards against escaped quotes.
4. `(?<=[^\\](?:\\\\)*)` handles escaped backslashes before quotes.
5. `(?<=[^\\](?:\\\\)*|^)` also handles quotes at string start.

# Construction / Recognition

## To Construct/Create:
1. Start: `/"(.*?)"/g` — reluctant matching between quotes.
2. Add escape handling: `/(?<!\\)"(.*?)(?<!\\)"/g`.
3. Handle escaped backslashes: `/(?<=[^\\](?:\\\\)*)"(.*?)(?<=[^\\](?:\\\\)*)"/g`.
4. Handle start of string: `/(?<=[^\\](?:\\\\)*|^)"(.*?)(?<=[^\\](?:\\\\)*)"/g`.

## To Identify/Recognize:
1. A regex that pairs straight quotes and replaces them with curly quotes.
2. Lookbehind assertions used to handle backslash escaping.

# Context & Application

This is the most complex worked example in Chapter 17, demonstrating how real-world regex development proceeds iteratively. Each edge case motivates adding another lookaround assertion, showcasing the practical power of these constructs.

# Examples

**Example 1** (Ch 17): Basic smart quotes with reluctant matching:
```js
> `The words "must" and "should".`.replace(/"(.*?)"/g, '\u201C$1\u201D')
'The words \u201Cmust\u201D and \u201Cshould\u201D.'
```

**Example 2** (Ch 17): Handling escaped quotes:
```js
> const regExp = /(?<!\\)"(.*?)(?<!\\)"/g;
> String.raw`\"straight\" and "curly"`.replace(regExp, '\u201C$1\u201D')
'\\"straight\\" and \u201Ccurly\u201D'
```

**Example 3** (Ch 17): Handling escaped backslashes:
```js
> const regExp = /(?<=[^\\](?:\\\\)*|^)"(.*?)(?<=[^\\](?:\\\\)*)"/g;
> `"abc"`.replace(regExp, '\u201C$1\u201D')
'\u201Cabc\u201D'
```

# Relationships

## Builds Upon
- **Negative lookbehind** — Guards against escaped quotes.
- **Positive lookbehind** — Advanced guard for escaped backslashes.
- **Reluctant quantifiers** — Correctly matches between nearest quote pairs.

## Enables
- **Text processing** — Typographic improvements to plain text.
- **Iterative regex development** — Demonstrates a methodology for building complex regexes.

## Related
- **Negative lookaround guard** — The technique used extensively here.
- **Inward-pointing lookaround** — The assertions face inward, restricting what can be a quote.

## Contrasts With
- **Proper parsing** — The chapter warns that "regular expressions aren't always the best solution. Another technique, such as proper parsing, may be a better choice."

# Common Errors

- **Error**: Forgetting that `\\` before a quote means the backslash is escaped, not the quote.
  **Correction**: The `(?<=[^\\](?:\\\\)*)` guard allows pairs of backslashes before quotes, correctly interpreting `\\"` as an escaped backslash followed by a real quote.

# Common Confusions

- **Confusion**: Thinking the simple `(?<!\\)` guard handles all escape cases.
  **Clarification**: It fails when there's an escaped backslash before the quote (`\\"`). The guard sees the second backslash and thinks the quote is escaped, but actually the two backslashes escape each other.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.9, lines 8143-8230.

# Verification Notes

- Definition source: direct (complete worked example from source)
- Confidence rationale: Step-by-step development shown with code at each stage
- Cross-reference status: verified through progressive examples in source
