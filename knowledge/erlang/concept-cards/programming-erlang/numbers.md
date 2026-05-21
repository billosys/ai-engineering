---
# === CORE IDENTIFICATION ===
concept: Numbers
slug: numbers

# === CLASSIFICATION ===
category: data-types
subcategory: atomic-data
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - integer
  - float
  - "base K integer"
  - "$ syntax"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - arithmetic-expressions
  - escape-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What number types does Erlang have?"
  - "How do I write integers in other bases?"
  - "What does the $ syntax mean?"
---

# Quick Definition

Erlang numbers are either integers or floats. Integer arithmetic is exact and arbitrary-precision; floats are IEEE 754 64-bit.

# Core Definition

"Numbers in Erlang are either integers or floats" ("The Rest of Sequential Erlang", *Numbers*). Integer arithmetic is exact, and the number of digits in an integer "is limited only by available memory." Integers have three syntaxes: conventional decimal (`12`, `-23427`); base-K integers written `K#Digits` (e.g. `2#00101010` in binary, `16#af6bfa23` in hex; for bases above ten the letters `abc...` mean 10, 11, 12, ...; the highest base is 36); and `$` syntax, where `$C` is the integer code for character `C` (e.g. `$a` is `97`, `$\n` is `10`). A floating-point number has an optional sign, a whole part, a decimal point, a fractional part, and an optional exponent (`1.0`, `3.14159`, `-2.3e+6`); floats are represented internally in IEEE 754 64-bit format.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Numbers are either integers or floats.
2. Integer arithmetic is exact; integer size is limited only by available memory (bignums).
3. Integers have three syntaxes: conventional, base-K (`K#Digits`), and `$C` character codes.
4. The highest integer base is 36; letters represent digit values from 10 upward.
5. A float has an optional sign, whole part, decimal point, fractional part, and optional exponent.
6. Floats are stored as IEEE 754 64-bit; magnitudes roughly 10^-323 to 10^308 are representable.
7. After `$`, escape sequences may be used — `$\n` is `10`.

# Construction / Recognition

## To Construct/Create:
1. Write decimals: `12`, `-65`.
2. Write base-K integers: `2#010001110`, `16#fe34`, `36#wow`.
3. Write character codes: `$a`, `$1`, `$\n`.
4. Write floats: `3.14159`, `-2.3e+6`.

## To Identify/Recognize:
1. A `K#` prefix marks a base-K integer; a leading `$` marks a character-code integer.

# Context & Application

- **Typical contexts**: all numeric data in sequential Erlang.
- **Common applications**: hex/binary literals for bit-syntax and protocol code; `$C` for ASCII codes.
- **Historical/stylistic notes**: `36#wow` evaluates to `42368` — the example values given are `0, -65, 142, -255, 65076, 65076, 42368`.

# Examples

**Example 1** (*Numbers*): integer literals in all three forms — `0`, `-65`, `2#010001110`, `-8#377`, `16#fe34`, `16#FE34`, `36#wow` — have values `0`, `-65`, `142`, `-255`, `65076`, `65076`, `42368`.

**Example 2** (*Numbers*): float literals — `1.0`, `3.14159`, `-2.3e+6`, `23.56E-27`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Arithmetic expressions** — Operators act on integers and floats.
- **Escape sequences** — `$\n` and similar combine the `$` syntax with escape sequences.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Writing a base-K integer with a base above 36.
  **Correction**: The highest integer base is 36.

# Common Confusions

- **Confusion**: Assuming integer arithmetic overflows like fixed-width integers in other languages.
  **Clarification**: Erlang integers are arbitrary-precision — size is limited only by available memory.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Numbers" (Integers, Floats).

# Verification Notes

- Definition source: Direct adaptation of the *Numbers* section.
- Confidence rationale: HIGH — the source explicitly describes integer syntaxes, float structure, and representation.
- Uncertainties: None.
- Cross-reference status: Slugs `arithmetic-expressions`, `escape-sequences` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
