---
# === CORE IDENTIFICATION ===
concept: Value
slug: value

# === CLASSIFICATION ===
category: fundamentals
subcategory: data
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - number
  - string
  - boolean
  - undefined-value
  - null-value
  - binding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A value is a chunk of bits in a JavaScript environment that represents a piece of information, with a type that determines its role.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 1, lines 71-77 of 01-values-types-and-operators.md): "In a JavaScript environment, those chunks are called *values*. Though all values are made of bits, they play different roles. Every value has a type that determines its role. Some values are numbers, some values are pieces of text, some values are functions, and so on."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. All values are **made of bits** but differ in their type and role.
2. Every value has a **type** that determines its role (number, string, Boolean, etc.).
3. Values are created by invoking their name or writing their literal form.
4. Values that are no longer used are **garbage collected** -- their bits are recycled (lines 87-89).
5. Values are the atomic elements of JavaScript programs (line 93).

# Construction / Recognition

## To Construct/Create:
1. Write a literal value: `13`, `"hello"`, `true`, `null`.
2. Compute a value using operators: `5 + 3`.
3. Call a function that returns a value.

## To Identify/Recognize:
1. Any piece of data that can be stored, manipulated, or passed around in a program.

# Context & Application

Values are the most fundamental building block in JavaScript. Every expression produces a value. Understanding values and their types is prerequisite to understanding operators, bindings, functions, and all higher-level concepts.

# Examples

**Example 1** (Ch 1, lines 103-105): A number value:
```js
13
```
"Using that in a program will cause the bit pattern for the number 13 to come into existence inside the computer's memory."

**Example 2** (Ch 1, lines 250-254): String values:
```js
`Down on the sea`
"Lie on the ocean"
'Float on the ocean'
```

**Example 3** (Ch 1, summary lines 695-698): "Such values are created by typing in their name (`true`, `null`) or value (`13`, `"abc"`)."

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **Number** -- A type of value.
- **String** -- A type of value.
- **Boolean** -- A type of value.
- **Binding** -- Bindings hold references to values.
- **Expression** -- Expressions produce values.

## Related
- **Type Coercion** -- Values can be implicitly converted between types.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Thinking values are "created from thin air" without cost.
  **Correction**: Each value is stored somewhere in memory. Using a gigantic number simultaneously could exhaust memory, though unused values are garbage collected (lines 83-89).

# Common Confusions

- **Confusion**: Values and bindings are the same thing.
  **Clarification**: Values are the data itself; bindings are names that refer to (grasp) values. Two bindings can refer to the same value.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Values", lines 62-94 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term in dedicated section
- Cross-reference status: verified within chapter
