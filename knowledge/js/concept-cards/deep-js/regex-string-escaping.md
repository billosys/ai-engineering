---
# === CORE IDENTIFICATION ===
concept: Automatic String Escaping in Regex Composition
slug: regex-string-escaping

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
  - regex escaping
  - safe string interpolation in regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - re-template-tag
extends:
  - re-template-tag
related:
  - regex-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
  - "How do I safely insert literal strings into a regex?"
---

# Quick Definition

When a string is interpolated into a `re` template tag expression, special regex characters in the string are automatically escaped, ensuring the string is matched literally rather than interpreted as a regex pattern.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 18, Section 18.2.1): "Any strings you insert are escaped properly." The example shows that interpolating `'.'` (which in regex means "any character") produces `\\.` in the resulting regex source, ensuring it matches a literal dot. This prevents accidental regex injection and eliminates the need for manual escaping.

# Prerequisites

- **`re` template tag** — The composition mechanism that provides this feature.

# Key Properties

1. Interpolated **strings** are escaped; interpolated **RegExp objects** are not.
2. Regex metacharacters (`.`, `*`, `+`, `?`, `(`, `)`, `[`, etc.) become literal.
3. Eliminates the need for manual `escapeRegExp()` utility functions.
4. Prevents **regex injection** — user-provided strings cannot alter pattern behavior.

# Construction / Recognition

## To Construct/Create:
1. Interpolate a string value with `${}` in a `re` template tag.
2. The string is automatically escaped in the resulting regex.

## To Identify/Recognize:
1. A string interpolation in a `re` template tag.
2. The resulting `.source` shows escaped metacharacters.

# Context & Application

Automatic escaping is particularly useful when regex patterns need to match user-provided text, file paths, or other strings that may contain regex metacharacters. It is listed as one of the three key benefits of regex composition.

# Examples

**Example 1** (Ch 18): Dot is escaped:
```js
assert.equal(re`/-${'.'}-/u`.source, '-\\.-');
// The '.' string becomes '\\.' — matches a literal dot
```

# Relationships

## Builds Upon
- **`re` template tag** — Provides the escaping behavior.

## Enables
- **Safe string insertion** — User-provided strings can be safely inserted into regexes.
- **Literal matching** — Ensures strings match exactly, not as patterns.

## Related
- **Regex composition** — String escaping is part of the composition workflow.

## Contrasts With
- **`new RegExp(string)`** — No automatic escaping; metacharacters are interpreted as regex.

# Common Errors

- **Error**: Expecting a string interpolation to be interpreted as a regex pattern.
  **Correction**: Strings are always escaped. If you want the interpolation to be a regex pattern, use a RegExp object instead of a string.

# Common Confusions

- **Confusion**: Thinking RegExp interpolations are also escaped.
  **Clarification**: Only strings are escaped. RegExp objects contribute their `.source` as-is, preserving their pattern semantics.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.2.1, lines 8377-8381.

# Verification Notes

- Definition source: direct (from source example with assertion)
- Confidence rationale: Explicitly demonstrated with clear before/after
- Cross-reference status: verified against Section 18.3 benefits list
