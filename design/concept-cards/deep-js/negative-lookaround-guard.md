---
# === CORE IDENTIFICATION ===
concept: Negative Lookaround as Guard
slug: negative-lookaround-guard

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
section: "17.7-17.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex guard pattern
  - assertion guard

# === TYPED RELATIONSHIPS ===
prerequisites:
  - negative-lookahead
  - negative-lookbehind
  - inward-pointing-lookaround
extends:
  - inward-pointing-lookaround
related:
  - lookaround-assertion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use lookaround to exclude certain patterns from matching?"
---

# Quick Definition

A negative lookaround guard is a negative assertion placed at a strategic position in a regex to prevent the overall pattern from matching inputs that contain a specific unwanted substring at that position.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 17, Sections 17.7-17.8): Negative lookaround assertions can act as "guards" that prevent a regex from matching at positions where an unwanted pattern appears. In Section 17.7, `(?<!\.mjs)` acts as a guard preventing matches for `.mjs` import specifiers. In Section 17.8, `(?!#)` acts as a guard preventing matches for comment lines. The author uses the term "guard" explicitly: "We can fix that by prefixing `(?!#)` as a guard."

# Prerequisites

- **Negative lookahead** — One type of guard (`(?!...)`).
- **Negative lookbehind** — Another type of guard (`(?<!...)`).
- **Inward-pointing lookaround** — The technique of using assertions to restrict match content.

# Key Properties

1. Guards **prevent** the overall regex from matching at certain positions.
2. Can appear at **any position** in the pattern — start, middle, or end.
3. At the start: prevents matching lines/strings starting with a pattern.
4. At the end: prevents matching strings ending with a pattern.
5. The guard itself consumes **no characters**.

# Construction / Recognition

## To Construct/Create:
1. Start with the regex that matches too much.
2. Identify the position where the unwanted pattern occurs.
3. Insert a negative lookahead (`(?!...)`) or negative lookbehind (`(?<!...)`) at that position.

## To Identify/Recognize:
1. A negative assertion inserted into an existing pattern.
2. The assertion's purpose is to exclude specific inputs rather than to match context.

# Context & Application

Guard patterns are a practical technique for refining regexes. When a regex matches more than desired, adding a guard at the right position can exclude the unwanted matches without restructuring the entire regex.

# Examples

**Example 1** (Ch 17): Guard at end — excluding `.mjs` imports:
```js
code.match(/^import .*? from '[^']+(?<!\.mjs)';$/umg)
// (?<!\.mjs) guards against module specifiers ending in .mjs
```

**Example 2** (Ch 17): Guard at start — skipping comment lines:
```js
const RE_SETTING = /^(?!#)([^:]*):(.*)$/;
// Without guard: /^([^:]*):(.*)$/.test('# Comment:') // true (wrong!)
// With guard:    /^(?!#)([^:]*):(.*)$/.test('# Comment:') // false (correct!)
```

# Relationships

## Builds Upon
- **Negative lookahead/lookbehind** — The assertion types used as guards.
- **Inward-pointing lookaround** — The general technique.

## Enables
- **Refined matching** — Fix over-broad regexes without rewriting them.
- **Exclusion patterns** — Reject specific inputs at specific positions.

## Related
- **Lookaround assertion** — The general mechanism.

## Contrasts With
- **Rewriting the regex** — An alternative to guards that restructures the entire pattern.

# Common Errors

- **Error**: Placing the guard at the wrong position in the pattern.
  **Correction**: The guard must be placed exactly where the unwanted text would appear. At the end for suffix exclusion (`(?<!\.mjs)` before the closing quote), at the start for prefix exclusion (`(?!#)` after `^`).

# Common Confusions

- **Confusion**: Thinking a guard prevents the entire string from matching anywhere.
  **Clarification**: The guard only prevents matching at the specific position where it's placed. It doesn't globally search for the unwanted pattern.

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Sections 17.7-17.8, lines 8045-8141.

# Verification Notes

- Definition source: direct (author uses "guard" terminology explicitly)
- Confidence rationale: Demonstrated with two worked examples using "guard" term
- Cross-reference status: verified across Sections 17.7 and 17.8
