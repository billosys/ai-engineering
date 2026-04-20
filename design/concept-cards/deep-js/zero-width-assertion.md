---
# === CORE IDENTIFICATION ===
concept: Zero-Width Assertion
slug: zero-width-assertion

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
section: "17.6 Example: match strings not starting with 'abc'"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - zero-width match
  - non-consuming assertion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
extends: []
related:
  - lookaround-assertion
  - positive-lookahead
  - negative-lookahead
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does a lookaround assertion produce an empty match?"
---

# Quick Definition

A zero-width assertion is a regex construct that checks a condition at a position in the input without consuming any characters, meaning it does not advance the match position or contribute to the matched text.

# Core Definition

As explained in "Deep JavaScript" (Ch 17, Section 17.6): "The problem is that assertions such as lookaround assertions don't expand the matched text. That is, they don't capture input characters, they only make demands about the current location in the input." This is why `/^(?!abc)/.exec('xyz')` produces an empty string match — the assertion succeeds but consumes nothing.

# Prerequisites

- **Regular expression basics** — Understanding of match positions and consumption.

# Key Properties

1. Zero-width assertions **check conditions** but consume no input.
2. All four lookaround assertions are zero-width.
3. Other zero-width assertions include `^`, `$`, `\b` (word boundary).
4. Using only zero-width assertions produces **empty string matches**.
5. Must combine with consuming patterns (like `.*`) to capture actual text.

# Construction / Recognition

## To Construct/Create:
1. Use a lookaround assertion for the zero-width check.
2. Combine with a consuming pattern to capture the actual text you want.

## To Identify/Recognize:
1. A regex that produces empty string matches unexpectedly.
2. The regex contains only assertions without consuming patterns.

# Context & Application

Understanding zero-width behavior is crucial for using lookaround assertions effectively. A common mistake is writing a regex with only assertions, expecting it to match text. The fix is always to add a consuming pattern alongside the assertion.

# Examples

**Example 1** (Ch 17): Zero-width assertion produces empty match:
```js
> /^(?!abc)/.exec('xyz')
{ 0: '', index: 0, input: 'xyz', groups: undefined }
```

**Example 2** (Ch 17): Adding a consuming pattern after the assertion:
```js
> /^(?!abc).*$/.exec('xyz')
{ 0: 'xyz', index: 0, input: 'xyz', groups: undefined }
```

# Relationships

## Builds Upon
- **Regular expression match mechanics** — How the regex engine advances through input.

## Enables
- **Conditional matching** — Check conditions without affecting what gets matched.

## Related
- **Lookaround assertion** — The primary zero-width constructs.
- **Word boundary `\b`** — Another common zero-width assertion.
- **Anchors `^` and `$`** — Zero-width position assertions.

## Contrasts With
- **Consuming patterns** — Patterns like `[a-z]+` and `.*` that consume input characters.

# Common Errors

- **Error**: Using only a lookaround assertion and expecting a non-empty match.
  **Correction**: Add a consuming pattern (like `.*$`) to capture the text you want. The assertion constrains the position; the consuming pattern captures the text.

# Common Confusions

- **Confusion**: Thinking zero-width means "matches nothing" or "fails."
  **Clarification**: Zero-width means "matches at a position" without advancing. The match succeeds (returns an empty string), but no characters are consumed.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.6, lines 7995-8043.

# Verification Notes

- Definition source: direct (from source explanation about assertions not expanding matched text)
- Confidence rationale: Explicitly explained with example of empty match
- Cross-reference status: verified against Section 17.6 worked example
