---
# === CORE IDENTIFICATION ===
concept: Cooked vs. Raw Template Strings
slug: cooked-vs-raw-template-strings

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Using template literals and tagged templates"
chapter_number: 23
pdf_page: null
section: "Cooked vs. raw template strings (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tagged-template
extends: []
related:
  - string-raw
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Tag functions receive two interpretations of template strings: the "cooked" version where backslash sequences are processed (e.g., `\t` becomes a tab), and the "raw" version where backslashes are literal (e.g., `\t` stays as two characters).

# Core Definition

Tag functions get two interpretations: a *cooked interpretation* (the first argument array) where backslashes have special meaning, and a *raw interpretation* (`.raw` property of the first argument) where backslashes are literal. If a cooked string has an invalid escape sequence, it is `undefined` while the raw version remains verbatim. This change was made in ES2018 to support tagged templates for text that was previously illegal (Ch. 23, Section 23.3.1).

# Prerequisites

- **tagged-template** -- cooked/raw distinction applies to tag functions

# Key Properties

1. Cooked: backslashes processed (`\t` -> tab character)
2. Raw: backslashes literal (`\t` -> backslash + t)
3. Invalid escapes: cooked is `undefined`, raw is verbatim (ES2018)
4. Raw accessed via `templateStrings.raw`

# Construction / Recognition

```js
function cookedRaw(templateStrings, ...substitutions) {
  return {
    cooked: Array.from(templateStrings),
    raw: templateStrings.raw,
    substitutions,
  };
}
cookedRaw`\tab${'subst'}\newline\\`
// {
//   cooked: ['\tab', '\newline\\'],
//   raw:    ['\\tab', '\\newline\\\\'],
//   substitutions: ['subst'],
// }
```

# Context & Application

The raw interpretation enables use cases like `String.raw` for Windows paths and regex patterns, and allows tagged templates for LaTeX and other backslash-heavy languages.

# Examples

From the source text:

```js
assert.deepEqual(
  cookedRaw`\u{54}\u0065\x78t`,
  {
    cooked: ['Text'],
    raw:    ['\\u{54}\\u0065\\x78t'],
    substitutions: [],
  }
);

// Invalid escapes: cooked is undefined
assert.deepEqual(
  cookedRaw`\uu\xx ${1} after`,
  {
    cooked: [undefined, ' after'],
    raw:    ['\\uu\\xx ', ' after'],
    substitutions: [1],
  }
);
```

# Relationships

## Builds Upon
- **tagged-template** — only tag functions receive both interpretations

## Enables
- **string-raw** — uses the raw interpretation
- DSLs for backslash-heavy text (LaTeX, Windows paths)

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Expecting invalid escape sequences to always throw errors in tagged templates
  **Correction**: Since ES2018, invalid escapes in tagged templates produce `undefined` for the cooked value but the raw value is preserved.

# Common Confusions

- **Confusion**: Thinking cooked and raw are always different
  **Clarification**: For strings without backslash sequences, cooked and raw are identical.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.3.1, lines 188-265.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples showing both interpretations
- Cross-reference status: verified
