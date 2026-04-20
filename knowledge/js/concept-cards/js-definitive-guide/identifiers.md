---
# === CORE IDENTIFICATION ===
concept: Identifiers
slug: identifiers

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 33
section: "2.4 Identifiers and Reserved Words"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - names
  - variable names

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - case-sensitivity
extends: []
related:
  - reserved-words
  - unicode-in-javascript
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

An identifier is a name used to label constants, variables, properties, functions, classes, and loop labels in JavaScript, which must begin with a letter, underscore, or dollar sign.

# Core Definition

"An identifier is simply a name. In JavaScript, identifiers are used to name constants, variables, properties, functions, and classes and to provide labels for certain loops in JavaScript code. A JavaScript identifier must begin with a letter, an underscore (_), or a dollar sign ($). Subsequent characters can be letters, digits, underscores, or dollar signs. (Digits are not allowed as the first character so that JavaScript can easily distinguish identifiers from numbers.)" (p. 33)

# Prerequisites

- **javascript-language-overview** — Identifiers are fundamental syntax
- **case-sensitivity** — Identifiers are case-sensitive

# Key Properties

1. Must begin with a letter, `_`, or `$`
2. Subsequent characters can be letters, digits, `_`, or `$`
3. Cannot begin with a digit
4. Are case-sensitive
5. Unicode letters and ideographs (but not emojis) are allowed in identifiers
6. Reserved words cannot be used as identifiers (with some exceptions)

# Construction / Recognition

```javascript
i
my_variable_name
v13
_dummy
$str
```

# Context & Application

Identifiers are the names given to everything in JavaScript — variables, functions, classes, and more. Following naming conventions (camelCase for variables, PascalCase for classes) improves code readability.

# Examples

From the source text (p. 34):
```javascript
i
my_variable_name
v13
_dummy
$str
```

Unicode identifiers (p. 35):
```javascript
const π = 3.14;
const sí = true;
```

# Relationships

## Builds Upon
- **case-sensitivity** — Identifiers are case-sensitive

## Enables
- **variables-overview** — Variables are named with identifiers
- **reserved-words** — Some identifiers are reserved by the language

## Related
- **reserved-words** — Reserved words restrict identifier naming
- **unicode-in-javascript** — Unicode characters can be used in identifiers

## Contrasts With
- None within this source

# Common Errors

- **Error**: Starting an identifier with a digit (e.g., `2ndPlace`).
  **Correction**: Identifiers cannot start with digits; use `secondPlace` or `_2ndPlace`.

# Common Confusions

- **Confusion**: Only ASCII letters can be used in identifiers.
  **Clarification**: Unicode letters, digits, and ideographs (but not emojis) are allowed in identifiers (p. 35).

# Source Reference

Chapter 2: Lexical Structure, Section 2.4, pages 33-34.

# Verification Notes

- Definition source: Direct quote from p. 33
- Confidence rationale: High — clearly defined with rules and examples
- Uncertainties: None
- Cross-reference status: Verified
