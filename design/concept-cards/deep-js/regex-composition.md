---
# === CORE IDENTIFICATION ===
concept: Regular Expression Composition
slug: regex-composition

# === CLASSIFICATION ===
category: regular-expressions
subcategory: composition
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Composing regular expressions via re-template-tag (bonus)"
chapter_number: 18
section: "18.3 Why is this useful?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex building blocks
  - composable regular expressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
extends: []
related:
  - re-template-tag
  - regex-fragment-reuse
  - named-capture-groups-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
---

# Quick Definition

Regular expression composition is the technique of building complex regex patterns by assembling them from smaller, documented, and reusable fragments using template literal tags.

# Core Definition

As explained in "Deep JavaScript" (Ch 18, Section 18.3), regex composition is useful because: "You can compose regular expressions from fragments and document the fragments via comments. That makes regular expressions easier to understand. You can define constants for regular expression fragments and reuse them. You can define plain text constants via strings and insert them into regular expressions and they are escaped as necessary."

# Prerequisites

- **Regular expression basics** — Understanding regex syntax and construction.

# Key Properties

1. Complex regex patterns are broken into **named fragments**.
2. Fragments can be **documented** with comments.
3. Fragments can be **reused** across multiple composed regexes.
4. String values inserted into regex compositions are **automatically escaped**.
5. Requires a **template tag** (like `re`) to assemble fragments into a valid RegExp.

# Construction / Recognition

## To Construct/Create:
1. Define regex fragments as separate `RegExp` objects or `re` template tag expressions.
2. Combine them using template literal syntax: `` re`/${FRAG1}-${FRAG2}/flags` ``.
3. Fragments' source patterns are extracted and composed.
4. Strings are escaped; RegExp objects contribute their source.

## To Identify/Recognize:
1. Multiple small regex fragments combined into a larger pattern.
2. Template literals or template tags used for assembly.
3. Named constants for regex parts.

# Context & Application

Regex composition addresses the readability and maintainability problems of complex regular expressions. By breaking patterns into named, documented fragments, the intent becomes clearer and fragments can be tested independently.

# Examples

**Example 1** (Ch 18): Composing a date regex from fragments:
```js
const RE_YEAR = /([0-9]{4})/;
const RE_MONTH = /([0-9]{2})/;
const RE_DAY = /([0-9]{2})/;
const RE_DATE = re`/^${RE_YEAR}-${RE_MONTH}-${RE_DAY}$/u`;
assert.equal(RE_DATE.source, '^([0-9]{4})-([0-9]{2})-([0-9]{2})$');
```

# Relationships

## Builds Upon
- **Regular expressions** — The patterns being composed.
- **Template literals** — The JavaScript feature enabling composition.

## Enables
- **Readable complex regexes** — Named fragments make intent clear.
- **Fragment reuse** — Define once, use in many patterns.
- **Automatic escaping** — Inserted strings are safely escaped.

## Related
- **`re` template tag** — The specific library that implements composition.
- **Named capture groups** — Work well with composition for self-documenting patterns.

## Contrasts With
- **Monolithic regex** — Writing the entire pattern as one long literal.
- **String concatenation** — Building regexes from strings (no automatic escaping, error-prone).

# Common Errors

- **Error**: Building regexes via string concatenation without escaping.
  **Correction**: Use a template tag like `re` which automatically escapes string interpolations. `re\`/-${'.'}-/u\`` produces `-\\.—` (escaped dot), not `-.-` (any character).

# Common Confusions

- **Confusion**: Thinking regex composition requires a specific library.
  **Clarification**: While `re-template-tag` provides a convenient implementation, the concept of building regexes from fragments is a general technique. The library is one implementation.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.3, lines 8414-8425.

# Verification Notes

- Definition source: direct (from "Why is this useful?" section)
- Confidence rationale: Explicitly listed benefits with worked examples
- Cross-reference status: verified against Section 18.1 and 18.2 examples
