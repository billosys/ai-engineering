---
# === CORE IDENTIFICATION ===
concept: Positive Lookahead Assertion
slug: positive-lookahead

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
section: "17.1 Cheat sheet: lookaround assertions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "(?=...)"
  - positive lookahead

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
  - lookaround-assertion
extends:
  - lookaround-assertion
related:
  - negative-lookahead
  - positive-lookbehind
contrasts_with:
  - negative-lookahead
  - positive-lookbehind

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lookahead assertion in a regular expression?"
  - "What distinguishes positive lookahead from negative lookahead?"
---

# Quick Definition

A positive lookahead `(?=«pattern»)` matches if the given pattern matches what comes immediately after the current position in the input string, without consuming any characters.

# Core Definition

As defined in "Deep JavaScript" (Ch 17, Section 17.1): "Positive lookahead: `(?=«pattern»)` matches if `pattern` matches what comes after the current location in the input string." It has been available since ECMAScript 3. The assertion is non-capturing and zero-width — it constrains but does not expand the match.

# Prerequisites

- **Regular expression basics** — Pattern syntax.
- **Lookaround assertion** — The general concept.

# Key Properties

1. Syntax: `(?=«pattern»)`.
2. Available since **ES3**.
3. **Non-capturing** and **zero-width**.
4. Matches if pattern **does** match what follows.
5. Often used to specify what must follow a match without including it in the result.

# Construction / Recognition

## To Construct/Create:
1. Write `(?=` followed by the pattern that must follow, then `)`.
2. Place it in the regex where you want the "must be followed by" constraint.

## To Identify/Recognize:
1. A group starting with `(?=`.
2. The matched text after does not appear in the match result.

# Context & Application

Positive lookahead is commonly used to extract text that appears before a known delimiter or marker, without including the delimiter in the match. In Chapter 17, it is demonstrated extracting quoted words where the closing quote must follow but is not captured.

# Examples

**Example 1** (Ch 17): Extracting quoted words — `(?=")` ensures each word is followed by a quote:
```js
> 'how "are" "you" doing'.match(/(?<=")[a-z]+(?=")/g)
[ 'are', 'you' ]
```
Here `(?=")` means "must be followed by a quote."

**Example 2** (Ch 17): Without lookahead, quotes are included:
```js
> 'how "are" "you" doing'.match(/"([a-z]+)"/g)
[ '"are"', '"you"' ]
```

# Relationships

## Builds Upon
- **Lookaround assertion** — Positive lookahead is one of the four types.

## Enables
- **Clean extraction** — Match content without including delimiters.

## Related
- **Positive lookbehind** — The "before" counterpart.
- **Negative lookahead** — The negated counterpart.

## Contrasts With
- **Negative lookahead** — Positive requires the pattern to match; negative requires it to not match.
- **Positive lookbehind** — Lookahead checks after the current position; lookbehind checks before.

# Common Errors

- **Error**: Forgetting that lookahead does not consume characters.
  **Correction**: If you need the lookahead content in the match, use a capturing group instead of a lookahead.

# Common Confusions

- **Confusion**: Confusing `(?=...)` (positive lookahead) with `(?<=...)` (positive lookbehind).
  **Clarification**: Lookahead uses `=`, lookbehind uses `<=`. The `<` points backward, indicating "look behind."

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Sections 17.1 and 17.3, lines 7846-7913.

# Verification Notes

- Definition source: direct (from cheat sheet and examples)
- Confidence rationale: Explicitly defined with syntax and worked examples
- Cross-reference status: verified against Section 17.3 usage examples
