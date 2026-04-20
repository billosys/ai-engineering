---
# === CORE IDENTIFICATION ===
concept: Regex Fragment Reuse
slug: regex-fragment-reuse

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
section: "18.2.1 Main features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - regex building blocks
  - reusable regex constants

# === TYPED RELATIONSHIPS ===
prerequisites:
  - re-template-tag
  - regex-composition
extends:
  - regex-composition
related:
  - named-capture-groups-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
---

# Quick Definition

Regex fragment reuse is the practice of defining regular expression parts as named constants and interpolating them into larger composed patterns, enabling DRY (Don't Repeat Yourself) regex development.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 18, Section 18.2.1): Regex fragments like `RE_YEAR`, `RE_MONTH`, and `RE_DAY` are defined as separate RegExp objects and composed into a date-matching pattern via the `re` template tag. The `re` tag extracts each fragment's `.source` property and assembles them into the final pattern. This enables "constants for regular expression fragments" that can be reused.

# Prerequisites

- **`re` template tag** — The mechanism for composing fragments.
- **Regex composition** — The general technique.

# Key Properties

1. Fragments are defined as **named constants** (RegExp objects or `re` expressions).
2. Each fragment can be **tested independently**.
3. Fragments are **interpolated** into composed patterns via `${}`.
4. The `re` tag extracts the fragment's `.source` for composition.
5. Changes to a fragment automatically propagate to all composed patterns.

# Construction / Recognition

## To Construct/Create:
1. Define each meaningful regex part as a named constant.
2. Give it a descriptive name (e.g., `RE_YEAR`, `RE_MONTH`).
3. Use `re` template tag to compose them: `` re`/^${RE_YEAR}-${RE_MONTH}-${RE_DAY}$/u` ``.

## To Identify/Recognize:
1. Multiple named RegExp constants.
2. A template tag that interpolates them into a larger pattern.
3. Comments documenting what each fragment matches.

# Context & Application

Fragment reuse is the key practical benefit of regex composition. It transforms regex development from writing one long inscrutable pattern to building from documented, tested, and reusable pieces.

# Examples

**Example 1** (Ch 18): Date regex from reusable fragments:
```js
const RE_YEAR = /([0-9]{4})/;
const RE_MONTH = /([0-9]{2})/;
const RE_DAY = /([0-9]{2})/;
const RE_DATE = re`/^${RE_YEAR}-${RE_MONTH}-${RE_DAY}$/u`;
assert.equal(RE_DATE.source, '^([0-9]{4})-([0-9]{2})-([0-9]{2})$');
```

# Relationships

## Builds Upon
- **`re` template tag** — The tool enabling fragment interpolation.
- **Regex composition** — The general approach.

## Enables
- **Maintainable regex** — Changes to a fragment update all patterns using it.
- **Documented regex** — Fragment names and comments explain the pattern.
- **Testable regex** — Individual fragments can be unit tested.

## Related
- **Named capture groups composition** — Named groups make fragments even more independent.

## Contrasts With
- **Monolithic regex** — A single long pattern without named parts.

# Common Errors

- **Error**: Defining fragments with conflicting flags.
  **Correction**: Fragments should generally be flag-free; flags are set on the composed pattern.

# Common Confusions

- **Confusion**: Thinking fragment RegExp objects' flags are preserved in composition.
  **Clarification**: Only the `.source` is extracted from fragment RegExp objects. Flags are set on the composed pattern, not inherited from fragments.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.2.1, lines 8364-8375.

# Verification Notes

- Definition source: direct (demonstrated with code examples)
- Confidence rationale: Core feature of the library, demonstrated with date regex example
- Cross-reference status: verified against Section 18.4 named groups example
