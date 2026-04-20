---
# === CORE IDENTIFICATION ===
concept: String
slug: string

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
  - string value
  - string type
  - text

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - template-literal
  - type-coercion
contrasts_with:
  - number
  - boolean

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Strings are values that represent text, written by enclosing content in quotes (single, double, or backtick), and modeled internally as sequences of Unicode character codes using 16-bit elements.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 1, lines 246-248 of 01-values-types-and-operators.md): "The next basic data type is the *string*. Strings are used to represent text. They are written by enclosing their content in quotes." Internally, JavaScript models strings using the Unicode standard with 16-bit elements per character position (lines 306-312).

# Prerequisites

- **Value** -- Strings are a type of value.

# Key Properties

1. Can be quoted with **single quotes** (`'...'`), **double quotes** (`"..."`), or **backticks** (`` `...` ``).
2. Support **escape sequences**: `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (escaped quote).
3. Only backtick-quoted strings can contain **literal newlines** (line 267-268).
4. The `+` operator **concatenates** strings (lines 324-327).
5. Modeled as sequences of 16-bit Unicode elements; some characters (like emoji) take two positions (lines 316-321).
6. Have associated **methods** for performing operations on them (lines 334-337).

# Construction / Recognition

## To Construct/Create:
1. Enclose text in matching quotes: `"hello"`, `'hello'`, `` `hello` ``.
2. Concatenate with `+`: `"con" + "cat"`.
3. Use template literals with embedded expressions: `` `half of 100 is ${100 / 2}` ``.

## To Identify/Recognize:
1. `typeof` returns `"string"`.
2. Text enclosed in quotes in source code.

# Context & Application

Strings are essential for representing text data in JavaScript -- from user messages to data processing. Understanding quoting styles, escape sequences, and string concatenation is fundamental to working with text.

# Examples

**Example 1** (Ch 1, lines 250-254): Three quoting styles:
```js
`Down on the sea`
"Lie on the ocean"
'Float on the ocean'
```

**Example 2** (Ch 1, lines 280-282): Escape sequences:
```js
"This is the first line\nAnd this is the second"
```

**Example 3** (Ch 1, lines 329-331): String concatenation:
```js
"con" + "cat" + "e" + "nate"
```
This produces the string `"concatenate"`.

# Relationships

## Builds Upon
- **Value** -- Strings are a type of value.

## Enables
- **Template Literal** -- A special form of string with embedded expressions.
- **String concatenation** -- The `+` operator applied to strings.

## Related
- **Type Coercion** -- Strings interact with other types through coercion (e.g., `"5" + 1` produces `"51"`).

## Contrasts With
- **Number** -- Numeric values; `+` means addition for numbers but concatenation for strings.
- **Boolean** -- Only two values; strings can hold arbitrary text.

# Common Errors

- **Error**: Using unmatched quote types (e.g., starting with `"` and ending with `'`).
  **Correction**: "The quotes at the start and the end of the string match" (lines 258-259).

- **Error**: Trying to include a literal newline in a single- or double-quoted string.
  **Correction**: Newlines can be included literally only in backtick-quoted strings. Use `\n` in other quote types.

# Common Confusions

- **Confusion**: The `+` operator always performs addition.
  **Clarification**: When applied to strings, `+` performs concatenation, not addition. This interacts with type coercion in potentially surprising ways.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Strings", lines 243-354 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition using italicized term
- Cross-reference status: verified within chapter
