---
# === CORE IDENTIFICATION ===
concept: Negative Lookahead Assertion
slug: negative-lookahead

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
  - "(?!...)"
  - negative lookahead

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
  - lookaround-assertion
extends:
  - lookaround-assertion
related:
  - positive-lookahead
  - negative-lookbehind
contrasts_with:
  - positive-lookahead

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lookahead assertion in a regular expression?"
  - "What distinguishes positive lookahead from negative lookahead?"
---

# Quick Definition

A negative lookahead `(?!«pattern»)` matches if the given pattern does NOT match what comes immediately after the current position in the input string, without consuming any characters.

# Core Definition

As defined in "Deep JavaScript" (Ch 17, Section 17.1): "Negative lookahead: `(?!«pattern»)` matches if `pattern` does not match what comes after the current location in the input string." Available since ECMAScript 3. Negative lookaround assertions are described as "a powerful tool and usually impossible to emulate via other regular expression means."

# Prerequisites

- **Regular expression basics** — Pattern syntax.
- **Lookaround assertion** — The general concept.

# Key Properties

1. Syntax: `(?!«pattern»)`.
2. Available since **ES3**.
3. **Non-capturing** and **zero-width**.
4. Matches if pattern **does NOT** match what follows.
5. "Negative lookaround assertions are a powerful tool and usually impossible to emulate via other regular expression means."

# Construction / Recognition

## To Construct/Create:
1. Write `(?!` followed by the pattern that must NOT follow, then `)`.
2. Place it in the regex where you want the "must NOT be followed by" constraint.

## To Identify/Recognize:
1. A group starting with `(?!`.
2. The regex succeeds only when the pattern inside does NOT match at that position.

# Context & Application

Negative lookahead is used to exclude matches based on what follows. In Chapter 17, it is demonstrated for: extracting unquoted words (Section 17.4), matching strings not starting with a prefix (Section 17.6), and skipping comment lines (Section 17.8). It commonly acts as a "guard" at the start of a pattern.

# Examples

**Example 1** (Ch 17): Skipping comment lines with `(?!#)`:
```js
const RE_SETTING = /^(?!#)([^:]*):(.*)$/;
// Matches 'indent: 2' but not '# Comment:'
```

**Example 2** (Ch 17): Matching strings not starting with 'abc':
```js
> /^(?!abc).*$/.exec('xyz')
{ 0: 'xyz', index: 0, input: 'xyz', groups: undefined }

> /^(?!abc).*$/.exec('abcd')
null
```

# Relationships

## Builds Upon
- **Lookaround assertion** — Negative lookahead is one of the four types.

## Enables
- **Pattern exclusion** — Reject matches based on what follows.
- **Guard patterns** — Prevent a regex from matching certain inputs.

## Related
- **Negative lookbehind** — The "before" counterpart.
- **Positive lookahead** — The non-negated counterpart.

## Contrasts With
- **Positive lookahead** — Positive requires the pattern to match; negative requires it to NOT match.

# Common Errors

- **Error**: Using `(?!abc)` alone without a consuming pattern, getting empty matches.
  **Correction**: "Assertions such as lookaround assertions don't expand the matched text." Add a consuming pattern like `.*$` after the assertion: `/^(?!abc).*$/`.

# Common Confusions

- **Confusion**: Thinking negative lookahead is the opposite of the entire match.
  **Clarification**: `(?!abc)` only checks the position where it appears. The rest of the regex still functions normally.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Sections 17.1, 17.4, 17.6, 17.8, lines 7846-7941.

# Verification Notes

- Definition source: direct (from cheat sheet and multiple worked examples)
- Confidence rationale: Explicitly defined with multiple practical examples
- Cross-reference status: verified across Sections 17.4, 17.6, and 17.8
