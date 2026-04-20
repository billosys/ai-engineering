---
# === CORE IDENTIFICATION ===
concept: Negative Lookbehind Assertion
slug: negative-lookbehind

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
  - "(?<!...)"
  - negative lookbehind

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
  - lookaround-assertion
extends:
  - lookaround-assertion
related:
  - positive-lookbehind
  - negative-lookahead
contrasts_with:
  - positive-lookbehind

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lookbehind assertion in a regular expression?"
---

# Quick Definition

A negative lookbehind `(?<!«pattern»)` matches if the given pattern does NOT match what comes immediately before the current position in the input string, without consuming any characters.

# Core Definition

As defined in "Deep JavaScript" (Ch 17, Section 17.1): "Negative lookbehind: `(?<!«pattern»)` matches if `pattern` does not match what comes before the current location in the input string." Added in ES2018. Negative lookbehind acts as a "guard" that prevents matching at positions preceded by certain patterns.

# Prerequisites

- **Regular expression basics** — Pattern syntax.
- **Lookaround assertion** — The general concept.

# Key Properties

1. Syntax: `(?<!«pattern»)`.
2. Added in **ES2018**.
3. **Non-capturing** and **zero-width**.
4. Matches if pattern **does NOT** match what precedes.
5. Works at the **beginning of a string** — there is nothing before the position, so the negative check succeeds.

# Construction / Recognition

## To Construct/Create:
1. Write `(?<!` followed by the pattern that must NOT precede, then `)`.
2. Place it where you want the "must NOT be preceded by" constraint.

## To Identify/Recognize:
1. A group starting with `(?<!`.
2. The regex fails at positions preceded by the specified pattern.

# Context & Application

Negative lookbehind is used to exclude matches preceded by certain content. In Chapter 17, it is demonstrated for filtering import statements (excluding `.mjs` specifiers) and for smart quote conversion (handling escaped backslashes before quotes).

# Examples

**Example 1** (Ch 17): Filtering out `.mjs` imports with `(?<!\.mjs)`:
```js
const code = `
import {transform} from './util';
import {Person} from './person.mjs';
import {zip} from 'lodash';
`.trim();
assert.deepEqual(
  code.match(/^import .*? from '[^']+(?<!\.mjs)';$/umg),
  [
    "import {transform} from './util';",
    "import {zip} from 'lodash';",
  ]);
```

**Example 2** (Ch 17): Extracting unquoted words:
```js
> 'how "are" "you" doing'.match(/(?<!")\b[a-z]+\b(?!")/g)
[ 'how', 'doing' ]
```

# Relationships

## Builds Upon
- **Lookaround assertion** — Negative lookbehind is one of the four types.

## Enables
- **Pattern exclusion by context** — Reject matches preceded by specific patterns.
- **Guard patterns** — Act as "guards" that block matching at certain positions.

## Related
- **Negative lookahead** — The "after" counterpart.
- **Positive lookbehind** — The non-negated counterpart.

## Contrasts With
- **Positive lookbehind** — Positive requires the pattern before; negative rejects it.

# Common Errors

- **Error**: Naively converting positive to negative lookaround when extracting unquoted words.
  **Correction**: Simply swapping `(?<=")` to `(?<!") ` may match substrings within quoted words (e.g., the "r" in "are"). Combine with word boundary assertions `\b` or character class restrictions.

# Common Confusions

- **Confusion**: Thinking negative lookbehind fails at the start of a string.
  **Clarification**: At the start of a string, there is no preceding character, so `(?<!...)` succeeds (the pattern cannot match nothing).

# Source Reference

Chapter 17: Regular expressions: lookaround assertions by example, Sections 17.1, 17.4, 17.7, lines 7846-7971.

# Verification Notes

- Definition source: direct (from cheat sheet and worked examples)
- Confidence rationale: Explicitly defined with multiple practical demonstrations
- Cross-reference status: verified across Sections 17.4 and 17.7
