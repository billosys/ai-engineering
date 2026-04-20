---
# === CORE IDENTIFICATION ===
concept: Positive Lookbehind Assertion
slug: positive-lookbehind

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
  - "(?<=...)"
  - positive lookbehind

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
  - lookaround-assertion
extends:
  - lookaround-assertion
related:
  - negative-lookbehind
  - positive-lookahead
contrasts_with:
  - negative-lookbehind
  - positive-lookahead

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lookbehind assertion in a regular expression?"
---

# Quick Definition

A positive lookbehind `(?<=«pattern»)` matches if the given pattern matches what comes immediately before the current position in the input string, without consuming any characters.

# Core Definition

As defined in "Deep JavaScript" (Ch 17, Section 17.1): "Positive lookbehind: `(?<=«pattern»)` matches if `pattern` matches what comes before the current location in the input string." Added in ECMAScript 2018, lookbehind assertions "are a relatively new feature that may not be supported by all JavaScript engines."

# Prerequisites

- **Regular expression basics** — Pattern syntax.
- **Lookaround assertion** — The general concept.

# Key Properties

1. Syntax: `(?<=«pattern»)`.
2. Added in **ES2018**.
3. **Non-capturing** and **zero-width**.
4. Matches if pattern **does** match what precedes the current position.
5. May not be supported by **older JavaScript engines**.

# Construction / Recognition

## To Construct/Create:
1. Write `(?<=` followed by the pattern that must precede, then `)`.
2. Place it in the regex where you want the "must be preceded by" constraint.

## To Identify/Recognize:
1. A group starting with `(?<=`.
2. The matched text before does not appear in the match result.

# Context & Application

Positive lookbehind is used to match patterns that must be preceded by specific content without including that content in the match. In Chapter 17, it is demonstrated extracting words between quotes — `(?<=")` ensures each word is preceded by a quote.

# Examples

**Example 1** (Ch 17): Extracting quoted words — `(?<=")` ensures each word is preceded by a quote:
```js
> 'how "are" "you" doing'.match(/(?<=")[a-z]+(?=")/g)
[ 'are', 'you' ]
```
Here `(?<=")` means "must be preceded by a quote."

# Relationships

## Builds Upon
- **Lookaround assertion** — Positive lookbehind is one of the four types.

## Enables
- **Context-aware extraction** — Match content based on preceding context.

## Related
- **Positive lookahead** — The "after" counterpart.
- **Negative lookbehind** — The negated counterpart.

## Contrasts With
- **Negative lookbehind** — Positive requires the pattern to match; negative requires it to not match.
- **Positive lookahead** — Lookbehind checks before; lookahead checks after.

# Common Errors

- **Error**: Using lookbehind patterns that are too complex for the engine.
  **Correction**: Some engines impose restrictions on lookbehind pattern complexity (e.g., fixed-length only). JavaScript (V8) supports variable-length lookbehind.

# Common Confusions

- **Confusion**: Confusing `(?<=...)` (positive lookbehind) with `(?=...)` (positive lookahead).
  **Clarification**: The `<` in `(?<=...)` points backward, indicating "look behind." Without `<`, it's "look ahead."

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Sections 17.1 and 17.3, lines 7846-7913.

# Verification Notes

- Definition source: direct (from cheat sheet and examples)
- Confidence rationale: Explicitly defined with syntax and ES2018 notation
- Cross-reference status: verified against Section 17.3 usage examples
