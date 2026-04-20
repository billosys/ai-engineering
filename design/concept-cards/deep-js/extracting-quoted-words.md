---
# === CORE IDENTIFICATION ===
concept: Extracting Quoted Words with Positive Lookaround
slug: extracting-quoted-words

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
section: "17.3 Example: Specifying what comes before or after a match (positive lookaround)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-lookahead
  - positive-lookbehind
extends: []
related:
  - extracting-unquoted-words
  - lookaround-assertion
contrasts_with:
  - extracting-unquoted-words

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I extract text between delimiters without including the delimiters?"
---

# Quick Definition

Extracting quoted words is a worked example demonstrating positive lookaround: `(?<=")[a-z]+(?=")` matches words between quotes without including the quotes in the match result.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 17, Section 17.3): Using positive lookbehind `(?<=")` and positive lookahead `(?=")` to extract words between quotes. "Lookaround assertions are especially convenient for `.match()` in `/g` mode, which returns whole matches (capture group 0). Whatever the pattern of a lookaround assertion matches is not captured." Without lookaround, quotes appear in the match results.

# Prerequisites

- **Positive lookahead** — `(?=")` "must be followed by a quote."
- **Positive lookbehind** — `(?<=")` "must be preceded by a quote."

# Key Properties

1. `(?<=")` ensures the match is **preceded by** a quote.
2. `(?=")` ensures the match is **followed by** a quote.
3. Neither quote is **captured** in the result.
4. Works cleanly with `.match()` and `/g` flag.
5. Without lookaround, the quotes are **included** in the match.

# Construction / Recognition

## To Construct/Create:
1. Use `(?<=delimiter)` before the content pattern.
2. Use `(?=delimiter)` after the content pattern.
3. The content pattern matches only the desired text between delimiters.

## To Identify/Recognize:
1. Lookbehind and lookahead bracketing a content pattern.
2. The match result contains only the content, not the delimiters.

# Context & Application

This is the first worked example in Chapter 17, introducing the core benefit of lookaround: matching based on context without including context in the result. It sets up the contrast with negative lookaround in Section 17.4.

# Examples

**Example 1** (Ch 17): With lookaround (clean result):
```js
> 'how "are" "you" doing'.match(/(?<=")[a-z]+(?=")/g)
[ 'are', 'you' ]
```

**Example 2** (Ch 17): Without lookaround (quotes in result):
```js
> 'how "are" "you" doing'.match(/"([a-z]+)"/g)
[ '"are"', '"you"' ]
```

# Relationships

## Builds Upon
- **Positive lookahead/lookbehind** — The assertions used.

## Enables
- **Delimiter-free extraction** — Extract content without surrounding markers.

## Related
- **Extracting unquoted words** — The negative-lookaround counterpart.

## Contrasts With
- **Extracting unquoted words** — Uses negative assertions to find words NOT between quotes.

# Common Errors

- **Error**: Using `.match()` without the `/g` flag and expecting multiple results.
  **Correction**: Without `/g`, `.match()` returns only the first match with capture groups. With `/g`, it returns all matches as an array.

# Common Confusions

- **Confusion**: Thinking you need capturing groups to extract content between delimiters.
  **Clarification**: Lookaround eliminates the need for capturing groups when using `.match()` with `/g`. The match itself is delimiter-free.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.3, lines 7889-7913.

# Verification Notes

- Definition source: direct (from worked example with before/after comparison)
- Confidence rationale: First example in chapter, explicitly contrasted with non-lookaround version
- Cross-reference status: verified against Section 17.4 negative version
