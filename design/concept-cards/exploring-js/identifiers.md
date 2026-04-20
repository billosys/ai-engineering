---
# === CORE IDENTIFICATION ===
concept: Identifiers
slug: identifiers

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.4 Identifiers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - variable names
  - property names

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - reserved-words
  - naming-conventions
  - let-declaration
  - const-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are valid variable and property names in JavaScript?"
---

# Quick Definition

Identifiers are the names used for variables and properties in JavaScript, composed of Unicode letters, digits, `$`, and `_`, where the first character cannot be a digit.

# Core Definition

"The grammatical category of variable names and property names is called *identifier*." (Ch. 9, &sect;9.1.5). Valid identifiers have a first character that is a Unicode letter (including accented and non-Latin characters), `$`, or `_`. Subsequent characters may also include Unicode digits and certain Unicode marks/punctuations. (Ch. 9, &sect;9.4.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. First character: Unicode letter, `$`, or `_`
2. Subsequent characters: above plus Unicode digits
3. Unicode letters include accented chars (`e`, `u`), non-Latin (`alpha`), etc.
4. Cannot start with a digit
5. Reserved words cannot be variable names but can be property names

# Construction / Recognition

```js
const epsilon = 0.0001;  // Greek letter
let _tmp = 0;        // underscore prefix
const $foo2 = true;  // dollar sign
```

# Context & Application

Identifiers are used everywhere: variable declarations, function names, property keys, class names.

# Examples

From the source text (Ch. 9, &sect;9.4.1):
```js
const epsilon = 0.0001;
const stroka = '';
let _tmp = 0;
const $foo2 = true;
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **let-declaration** -- uses identifiers as variable names
- **const-declaration** -- uses identifiers as variable names

## Related
- **reserved-words** -- words that cannot be used as identifiers
- **naming-conventions** -- conventions for how identifiers should be styled

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Starting a variable name with a digit (`2fast`).
  **Correction**: Variable names cannot start with digits. Use `fast2` or `_2fast`.

# Common Confusions

- **Confusion**: Thinking only ASCII letters are valid in identifiers.
  **Clarification**: Unicode letters from any script (Greek, Cyrillic, etc.) are valid.

# Source Reference

Chapter 9: Syntax, Section 9.4.1, lines 597-620.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit rules with examples
- Cross-reference status: verified
