---
# === CORE IDENTIFICATION ===
concept: Greedy vs. Reluctant Quantifiers
slug: greedy-vs-reluctant-quantifier

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
  - greedy vs lazy matching
  - eager vs reluctant quantifier

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
extends: []
related:
  - smart-quotes-regex
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between greedy and reluctant quantifiers in regex?"
---

# Quick Definition

A greedy quantifier (`*`, `+`) matches as many characters as possible, while a reluctant quantifier (`*?`, `+?`) matches as few characters as possible; the difference is critical when a pattern could match multiple substrings.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 17, Section 17.9): When using `"(.*)"` to match quoted text, the greedy `*` matches everything between the first and last quote in the string, producing `"must" and "should"`. Adding `?` to make it reluctant — `"(.*?)"` — causes the quantifier to match as little as possible, correctly identifying `"must"` and `"should"` as separate matches.

# Prerequisites

- **Regular expression basics** — Quantifiers (`*`, `+`, `?`).

# Key Properties

1. **Greedy** (`*`, `+`): matches as much as possible, then backtracks.
2. **Reluctant** (`*?`, `+?`): matches as little as possible, then expands.
3. The `?` suffix converts a greedy quantifier to a reluctant one.
4. Both match the **same set of strings** but differ in **which part** they capture.
5. Choice between them affects correctness, not just performance.

# Construction / Recognition

## To Construct/Create:
1. Start with the greedy quantifier: `.*`, `.+`.
2. If it matches too much, append `?` to make it reluctant: `.*?`, `.+?`.

## To Identify/Recognize:
1. A quantifier followed by `?` is reluctant.
2. A quantifier without `?` is greedy (by default).
3. The behavior difference is visible when there are multiple possible match endpoints.

# Context & Application

In Chapter 17, the greedy/reluctant distinction arises in the smart quotes example. When converting straight quotes to curly quotes, the greedy `.*` matches across multiple quoted phrases, while the reluctant `.*?` correctly matches each quoted phrase individually.

# Examples

**Example 1** (Ch 17): Greedy — matches too much:
```js
> `The words "must" and "should".`.replace(/"(.*)"/g, '\u201C$1\u201D')
'The words \u201Cmust" and "should\u201D.'
```

**Example 2** (Ch 17): Reluctant — matches correctly:
```js
> `The words "must" and "should".`.replace(/"(.*?)"/g, '\u201C$1\u201D')
'The words \u201Cmust\u201D and \u201Cshould\u201D.'
```

# Relationships

## Builds Upon
- **Quantifiers** — Greedy/reluctant modifies existing quantifier behavior.

## Enables
- **Smart quote conversion** — Reluctant matching enables correct paired-quote replacement.
- **Delimiter-based extraction** — Match between nearest delimiters, not farthest.

## Related
- **Smart quotes regex** — The worked example that demonstrates this distinction.

## Contrasts With
- **Possessive quantifiers** — (Not covered in source) A third mode that never backtracks.

# Common Errors

- **Error**: Using `"(.*)"` to match individual quoted strings when the input has multiple quoted sections.
  **Correction**: Use `"(.*?)"` with the reluctant quantifier to match each quoted section separately.

# Common Confusions

- **Confusion**: Thinking reluctant quantifiers are always "better" than greedy ones.
  **Clarification**: Greedy is correct when you want the longest possible match. Reluctant is correct when you want the shortest. The choice depends on the use case.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.9, lines 8143-8169.

# Verification Notes

- Definition source: direct (demonstrated with before/after examples)
- Confidence rationale: Explicit comparison with clear behavioral difference shown
- Cross-reference status: verified against smart quotes example
