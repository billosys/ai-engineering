---
# === CORE IDENTIFICATION ===
concept: Template Literal
slug: template-literal

# === CLASSIFICATION ===
category: fundamentals
subcategory: types
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - backtick-quoted string
  - template string

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string
  - expression
extends:
  - string
related:
  - type-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Template literals are backtick-quoted strings that can span multiple lines and embed expressions using `${}` syntax, with the embedded results automatically converted to strings.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 342-354 of 01-values-types-and-operators.md): "Backtick-quoted strings, usually called *template literals*, can do a few more tricks. Apart from being able to span lines, they can also embed other values." Further: "When you write something inside `${}` in a template literal, its result will be computed, converted to a string, and included at that position."

# Prerequisites

- **String** -- Template literals are a form of string.
- **Expression** -- Embedded `${}` can contain any expression.

# Key Properties

1. Quoted with **backticks** (`` ` ``), not single or double quotes.
2. Can **span multiple lines** (contain literal newlines) (lines 267-268, 344).
3. Can **embed expressions** inside `${}` (line 351).
4. Embedded expressions are **computed, converted to string**, and inserted (lines 351-354).

# Construction / Recognition

## To Construct/Create:
1. Enclose text in backticks: `` `hello` ``.
2. Embed expressions: `` `half of 100 is ${100 / 2}` ``.

## To Identify/Recognize:
1. String delimited by backtick characters.
2. May contain `${...}` interpolation syntax.

# Context & Application

Template literals provide a cleaner alternative to string concatenation when building strings that include dynamic values. They are widely used in modern JavaScript for constructing messages, HTML fragments, and any string that mixes static text with computed values.

# Examples

**Example 1** (Ch 1, lines 346-348): Embedding an expression:
```js
`half of 100 is ${100 / 2}`
```
This produces the string `"half of 100 is 50"`.

# Relationships

## Builds Upon
- **String** -- Template literals produce string values.
- **Expression** -- Any expression can be embedded inside `${}`.

## Enables
- Cleaner string construction than concatenation with `+`.

## Related
- **Type Coercion** -- Embedded expression results are converted to strings.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `${}` in single- or double-quoted strings.
  **Correction**: Expression interpolation only works in backtick-quoted template literals, not in `'...'` or `"..."` strings.

# Common Confusions

- **Confusion**: Template literals and regular strings are different types.
  **Clarification**: Template literals produce regular string values. The backtick syntax is just a different way to write strings, with additional features.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Strings", lines 340-354 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
