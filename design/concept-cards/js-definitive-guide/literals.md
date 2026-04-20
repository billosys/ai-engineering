---
# === CORE IDENTIFICATION ===
concept: Literals
slug: literals

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
section: "2.3 Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - literal values
  - literal expressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
  - type-system-overview
extends: []
related:
  - integer-literals
  - floating-point-literals
  - string-literals
  - boolean-type
  - null-vs-undefined
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A literal is a data value that appears directly in program source code, such as numbers, strings, booleans, and null.

# Core Definition

"A literal is a data value that appears directly in a program." (p. 33) Literals include numeric values (12, 1.2), string values ("hello world", 'Hi'), boolean values (true, false), and the null value. Complete details on numeric and string literals are covered in Chapter 3.

# Prerequisites

- **javascript-language-overview** — Literals are basic language syntax
- **type-system-overview** — Literals represent values of specific types

# Key Properties

1. Numeric literals: integers (12) and floating-point (1.2)
2. String literals: enclosed in quotes ("hello world", 'Hi')
3. Boolean literals: true, false
4. Null literal: null
5. Initializer expressions use literal syntax for arrays ([]) and objects ({})

# Construction / Recognition

```javascript
12              // The number twelve
1.2             // The number one point two
"hello world"   // A string of text
'Hi'            // Another string
true            // A Boolean value
false           // The other Boolean value
null            // Absence of an object
```

# Context & Application

Literals are the most basic way to include data values in JavaScript programs. They are the building blocks from which more complex expressions are constructed.

# Examples

From the source text (p. 33):
```javascript
12              // The number twelve
1.2             // The number one point two
"hello world"   // A string of text
'Hi'            // Another string
true            // A Boolean value
false           // The other Boolean value
null            // Absence of an object
```

# Relationships

## Builds Upon
- **type-system-overview** — Each literal has a specific type

## Enables
- **integer-literals** — Detailed treatment of integer literal formats
- **floating-point-literals** — Detailed treatment of floating-point syntax
- **string-literals** — Detailed treatment of string literal syntax

## Related
- **boolean-type** — true and false are boolean literals
- **null-vs-undefined** — null is a literal; undefined is a global constant

## Contrasts With
- None within this source

# Common Errors

- **Error**: Confusing `null` the literal with `undefined` the global constant.
  **Correction**: `null` is a language keyword/literal; `undefined` is a predefined global constant, not a keyword.

# Common Confusions

- **Confusion**: Array and object literals are primitive literals.
  **Clarification**: Array ([]) and object ({}) literals create objects, not primitive values. They are "initializer expressions" (p. 23).

# Source Reference

Chapter 2: Lexical Structure, Section 2.3, page 33.

# Verification Notes

- Definition source: Direct quote from p. 33
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
