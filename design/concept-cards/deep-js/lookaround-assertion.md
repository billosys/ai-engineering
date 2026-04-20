---
# === CORE IDENTIFICATION ===
concept: Lookaround Assertion
slug: lookaround-assertion

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
  - lookaround
  - zero-width lookaround

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
extends: []
related:
  - positive-lookahead
  - negative-lookahead
  - positive-lookbehind
  - negative-lookbehind
  - zero-width-assertion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lookahead assertion in a regular expression?"
  - "What distinguishes positive lookahead from negative lookahead?"
---

# Quick Definition

A lookaround assertion is a non-capturing regex construct that checks whether a pattern matches (or does not match) what comes before or after the current position in the input string, without consuming any characters.

# Core Definition

As defined in "Deep JavaScript" (Ch 17, introduction): "A lookaround assertion is non-capturing and must match (or not match) what comes before (or after) the current location in the input string." There are four types: positive lookahead `(?=...)`, negative lookahead `(?!...)`, positive lookbehind `(?<=...)`, and negative lookbehind `(?<!...)`. Lookahead assertions have been available since ES3; lookbehind assertions were added in ES2018.

# Prerequisites

- **Regular expression basics** — Pattern syntax, quantifiers, character classes.

# Key Properties

1. **Non-capturing** — lookaround assertions do not capture input characters.
2. **Zero-width** — they do not advance the match position in the input string.
3. Four types: **positive/negative** crossed with **lookahead/lookbehind**.
4. Lookahead is **ES3**; lookbehind is **ES2018**.
5. They **constrain** the match without expanding it.

# Construction / Recognition

## To Construct/Create:
1. Determine if you need to check before (lookbehind) or after (lookahead) the match.
2. Determine if the pattern must match (positive) or must not match (negative).
3. Use the appropriate syntax: `(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`.

## To Identify/Recognize:
1. A group starting with `(?=`, `(?!`, `(?<=`, or `(?<!`.
2. The assertion does not appear in the match result (unless combined with other patterns).

# Context & Application

Lookaround assertions are especially useful with `.match()` in `/g` mode, which returns whole matches. They allow specifying context requirements without including that context in the match. They can also act as "guards" at specific positions in a pattern.

# Examples

**Example 1** (Ch 17): Overview of all four types:

| Pattern | Name | Since |
|---|---|---|
| `(?=«pattern»)` | Positive lookahead | ES3 |
| `(?!«pattern»)` | Negative lookahead | ES3 |
| `(?<=«pattern»)` | Positive lookbehind | ES2018 |
| `(?<!«pattern»)` | Negative lookbehind | ES2018 |

# Relationships

## Builds Upon
- **Regular expressions** — Lookaround extends the basic regex pattern language.

## Enables
- **Context-sensitive matching** — Match patterns based on surrounding context.
- **Inward-pointing guards** — Restrict what a broader pattern can match.

## Related
- **Positive lookahead** — `(?=...)` variant.
- **Negative lookahead** — `(?!...)` variant.
- **Positive lookbehind** — `(?<=...)` variant.
- **Negative lookbehind** — `(?<!...)` variant.

## Contrasts With
- **Capturing groups** — Capture and consume characters; lookaround does neither.

# Common Errors

- **Error**: Expecting lookaround assertions to capture text.
  **Correction**: "Assertions such as lookaround assertions don't expand the matched text. That is, they don't capture input characters, they only make demands about the current location."

# Common Confusions

- **Confusion**: Thinking lookaround assertions advance the match position.
  **Clarification**: They are zero-width — after a lookaround assertion, the regex engine is still at the same position in the input.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.1, lines 7837-7873.

# Verification Notes

- Definition source: direct (from chapter introduction and cheat sheet)
- Confidence rationale: Explicitly defined with complete taxonomy
- Cross-reference status: verified against all four assertion type descriptions
