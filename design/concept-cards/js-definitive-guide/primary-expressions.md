---
# === CORE IDENTIFICATION ===
concept: Primary Expressions
slug: primary-expressions

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 79
section: "4.1 Primary Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "literal expressions"
  - "simple expressions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - object-and-array-initializers
  - function-definition-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Primary expressions are the simplest expressions in JavaScript that stand alone without including any simpler subexpressions. They include literals, keyword values, and variable references.

# Core Definition

"The simplest expressions, known as *primary expressions*, are those that stand alone — they do not include any simpler expressions. Primary expressions in JavaScript are constant or *literal* values, certain language keywords, and variable references." (Ch. 4, §4.1)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Literals are constant values embedded directly in source code: number literals, string literals, and regular expression literals.
2. Reserved-word primary expressions include `true`, `false`, `null`, and `this`.
3. Variable references (identifiers) evaluate to whatever value has been assigned; if no variable exists, a ReferenceError is thrown.
4. `this` is not a constant — it evaluates to different values depending on context.

# Construction / Recognition

A primary expression is any expression that cannot be broken down further: a number (`1.23`), a string (`"hello"`), a regex (`/pattern/`), a boolean (`true`/`false`), `null`, `this`, or a bare identifier (`i`, `sum`, `undefined`).

# Context & Application

Primary expressions are the building blocks from which all complex expressions are constructed. Every compound expression ultimately bottoms out in primary expressions.

# Examples

From the source text (§4.1, p. 79):

```js
1.23         // A number literal
"hello"      // A string literal
/pattern/    // A regular expression literal

true         // Evaluates to the boolean true value
false        // Evaluates to the boolean false value
null         // Evaluates to the null value
this         // Evaluates to the "current" object

i            // Evaluates to the value of the variable i.
sum          // Evaluates to the value of the variable sum.
undefined    // The value of the "undefined" property of the global object
```

# Relationships

## Builds Upon
- No prerequisites — this is the most fundamental expression type.

## Enables
- **object-and-array-initializers** — Built from primary expressions as subexpressions
- **property-access-expressions** — Operate on primary expressions

## Related
- **function-definition-expressions** — Function literals are sometimes called "function literals" analogous to other primary literals

## Contrasts With
- No direct contrast — primary expressions are the base case for all other expression types.

# Common Errors

- **Error**: Using an undeclared identifier as a primary expression.
  **Correction**: An attempt to evaluate a nonexistent variable throws a ReferenceError. Ensure variables are declared before use.

# Common Confusions

- **Confusion**: Believing `this` is a constant like `true` or `null`.
  **Clarification**: Unlike other keyword primary expressions, `this` evaluates to different values in different places in the program.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.1, pages 79-80.

# Verification Notes

- Definition source: Direct quote from §4.1
- Confidence rationale: High — clearly defined section with explicit enumeration
- Uncertainties: None
- Cross-reference status: Verified against §3.2, §3.3, §3.4, §3.5
