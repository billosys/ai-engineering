---
# === CORE IDENTIFICATION ===
concept: Inward-Pointing Lookaround
slug: inward-pointing-lookaround

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
section: "17.5 Interlude: pointing lookaround assertions inward"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - inward-facing assertion
  - lookaround guard

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lookaround-assertion
  - negative-lookahead
extends:
  - lookaround-assertion
related:
  - negative-lookaround-guard
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can lookaround assertions restrict what is inside a match?"
---

# Quick Definition

Inward-pointing lookaround assertions are placed at the boundaries of a match pattern to restrict what the match itself can contain, rather than specifying external context around the match.

# Core Definition

As described in "Deep JavaScript" (Ch 17, Section 17.5): "All of the examples we have seen so far have in common that the lookaround assertions dictate what must come before or after the match but without including those characters in the match. The regular expressions shown in the remainder of this chapter are different: Their lookaround assertions point inward and restrict what's inside the match."

# Prerequisites

- **Lookaround assertion** — The general concept this extends.
- **Negative lookahead** — The most commonly used type for inward-pointing guards.

# Key Properties

1. Assertions placed at **match boundaries** (start or end) face "inward" toward the match content.
2. They **restrict** what the match pattern can capture, rather than requiring external context.
3. Typically use **negative** assertions (`(?!...)`, `(?<!...)`) to exclude certain match content.
4. The assertion and the consuming pattern **overlap** — they check the same region of input.

# Construction / Recognition

## To Construct/Create:
1. Place the assertion at the start or end of the match pattern.
2. The assertion pattern describes what you want to exclude from matching.
3. Follow with a consuming pattern that captures the actual text.

## To Identify/Recognize:
1. A lookaround assertion at the beginning or end of a pattern.
2. The assertion restricts the match content itself, not its surroundings.
3. Example: `/^(?!abc).*$/` — the `(?!abc)` restricts what `.*` can match.

# Context & Application

This technique is the focus of the second half of Chapter 17 (Sections 17.6-17.9). It transforms lookaround assertions from context checkers into content filters — for example, matching strings that don't start with a prefix, or matching lines that aren't comments.

# Examples

**Example 1** (Ch 17): Negative lookahead pointing inward to exclude prefix:
```js
> /^(?!abc).*$/.exec('xyz')
{ 0: 'xyz', ... }

> /^(?!abc).*$/.exec('abcd')
null
```

**Example 2** (Ch 17): Negative lookahead as guard to skip comment lines:
```js
const RE_SETTING = /^(?!#)([^:]*):(.*)$/;
// (?!#) points inward — restricts the first character of the match
```

# Relationships

## Builds Upon
- **Lookaround assertion** — Repurposed from external context checking to internal content restriction.

## Enables
- **Pattern exclusion** — Match everything except patterns starting with a specific prefix.
- **Guard patterns** — Prevent specific content from being matched.

## Related
- **Negative lookaround guard** — The specific use as a "guard" at a boundary.

## Contrasts With
- **Outward-pointing lookaround** — The more common usage where assertions check external context.

# Common Errors

- **Error**: Forgetting to add a consuming pattern after the inward-pointing assertion.
  **Correction**: `/^(?!abc)/` only produces empty matches. Add `.*$` to capture the content: `/^(?!abc).*$/`.

# Common Confusions

- **Confusion**: Thinking all lookaround assertions face outward.
  **Clarification**: The direction depends on placement. At the start of a pattern, a negative lookahead checks the beginning of the match content (inward). Between a consuming pattern and external context, it checks outward.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Section 17.5, lines 7983-7993.

# Verification Notes

- Definition source: direct (explicitly described as a distinct usage pattern)
- Confidence rationale: Author specifically marks this as a transition point in the chapter
- Cross-reference status: verified against Sections 17.6-17.9 examples
