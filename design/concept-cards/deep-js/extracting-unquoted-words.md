---
# === CORE IDENTIFICATION ===
concept: Extracting Unquoted Words with Negative Lookaround
slug: extracting-unquoted-words

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
section: "17.4 Example: Specifying what does not come before or after a match (negative lookaround)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - negative-lookahead
  - negative-lookbehind
  - lookaround-assertion
extends: []
related:
  - no-simple-alternative-to-negative-lookaround
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use negative lookaround to exclude matches by context?"
---

# Quick Definition

Extracting unquoted words is a worked example demonstrating the subtleties of negative lookaround: naively swapping positive for negative lookaround fails because partial matches within quoted words can satisfy the assertion.

# Core Definition

As developed in "Deep JavaScript" (Ch 17, Section 17.4): Converting the quoted-word regex from positive to negative lookaround doesn't work as expected. The naive regex `(?<!")[a-z]+(?!")` incorrectly matches substrings like "r" from "are" because the character before "r" is "a" (not a quote). The fix is to also exclude letters in the assertion: `(?<!["a-z])[a-z]+(?!["a-z"])`, or to use word boundaries: `(?<!")\b[a-z]+\b(?!")`.

# Prerequisites

- **Negative lookahead** — `(?!...)` syntax.
- **Negative lookbehind** — `(?<!...)` syntax.
- **Lookaround assertion** — General concept.

# Key Properties

1. Naive negation of positive lookaround **fails** for partial matches.
2. Fix: also exclude the **word characters** themselves in the assertion.
3. Alternative fix: use **word boundaries** `\b` alongside the assertions.
4. Negative lookaround works at **string boundaries** (beginning/end) automatically.

# Construction / Recognition

## To Construct/Create:
1. Start with the positive lookaround version.
2. Swap to negative assertions.
3. Test for partial-match problems.
4. Add character class restrictions or word boundaries to fix.

## To Identify/Recognize:
1. A negative lookaround regex producing unexpected partial matches.
2. The fix involves broadening the assertion pattern or adding boundary assertions.

# Context & Application

This example demonstrates a common pitfall when first using negative lookaround. It teaches that negative lookaround assertions must account for the broader context, not just the specific delimiter character.

# Examples

**Example 1** (Ch 17): Naive approach fails:
```js
> 'how "are" "you" doing'.match(/(?<!")[a-z]+(?!")/g)
[ 'how', 'r', 'o', 'doing' ]
// 'r' from 'are' matches because it's preceded by 'a', not '"'
```

**Example 2** (Ch 17): Fixed with broader exclusion:
```js
> 'how "are" "you" doing'.match(/(?<!["a-z])[a-z]+(?!["a-z])/g)
[ 'how', 'doing' ]
```

**Example 3** (Ch 17): Fixed with word boundaries:
```js
> 'how "are" "you" doing'.match(/(?<!")\b[a-z]+\b(?!")/g)
[ 'how', 'doing' ]
```

# Relationships

## Builds Upon
- **Negative lookahead/lookbehind** — The assertions used.
- **Word boundaries** — `\b` used as an alternative fix.

## Enables
- **Understanding negative lookaround pitfalls** — Teaches careful assertion design.

## Related
- **No simple alternative to negative lookaround** — Discussed immediately after this example.

## Contrasts With
- **Extracting quoted words (positive lookaround)** — The simpler, positive version from Section 17.3.

# Common Errors

- **Error**: Simply replacing `(?<=")` with `(?<!") ` and expecting correct results.
  **Correction**: Negative assertions match when the pattern is absent at that position. A character inside a word (like "r" in "are") is not preceded by a quote — it's preceded by another letter.

# Common Confusions

- **Confusion**: Thinking negative lookaround checks the entire surrounding word.
  **Clarification**: Lookaround only checks at the exact position where it appears. It does not scan the entire surrounding context. This is why partial matches within quoted words can slip through.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.4, lines 7915-7979.

# Verification Notes

- Definition source: direct (complete worked example from source)
- Confidence rationale: Step-by-step development with failing and fixed versions
- Cross-reference status: verified against Section 17.3 positive version
