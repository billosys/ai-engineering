---
# === CORE IDENTIFICATION ===
concept: Integer
slug: integer

# === CLASSIFICATION ===
category: data-types
subcategory: primitive-types
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Simple Integer Arithmetic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bignum
  - arbitrary-precision integer

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - term
  - string
contrasts_with:
  - float

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an integer in Erlang?"
  - "Does Erlang integer arithmetic overflow?"
---

# Quick Definition

An Erlang integer is an arbitrary-sized, exact whole number. Integer arithmetic never overflows, so very large numbers can be computed directly.

# Core Definition

"Erlang uses arbitrary-sized integers for performing integer arithmetic. In Erlang, integer arithmetic is exact, so you don't have to worry about arithmetic overflows or not being able to represent an integer in a certain word size" (Chapter 3, "Simple Integer Arithmetic"). Erlang follows "the normal rules for arithmetic expressions," so `2 + 3 * 4` means `2 + (3 * 4)`. Integers can be entered in several notations, including base notation: `16#cafe` is a hexadecimal integer and `32#sugar` a base-32 integer. Integer division uses the operators `div` and `rem`: "`N div M` divides `N` by `M` and discards the remainder. `N rem M` is the remainder left after dividing `N` by `M`" (Chapter 3, "Floating-Point Numbers"). The `$` dollar syntax also produces an integer — the codepoint of a character.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Integers are of arbitrary size — no fixed word-size limit.
2. Integer arithmetic is exact and never overflows.
3. Standard precedence applies: `2 + 3 * 4` equals `14`.
4. Base notation `Base#Digits` is supported (e.g., `16#cafe`, `32#sugar`).
5. `div` performs integer division (discarding the remainder); `rem` gives the remainder.
6. Dividing two integers with `/` yields a float, not an integer.
7. `$c` dollar syntax yields the integer codepoint of character `c`.

# Construction / Recognition

## To Write an Integer:
1. Write digits directly, e.g. `123456789`.
2. For other bases, use `Base#Digits`, e.g. `16#cafe`.
3. For a character code, use `$c`.

## For Integer Division:
1. Use `div` for the quotient and `rem` for the remainder; do not use `/`, which yields a float.

## To Recognize It:
1. A whole number with no decimal point.

# Context & Application

- **Typical contexts**: Counting, indexing, arithmetic, character codes.
- **Common applications**: Exact computation with very large numbers; building string codepoints.
- **Historical/stylistic notes**: Armstrong invites the reader to "impress your friends by calculating with very large numbers" — exact bignum arithmetic is built in.

# Examples

**Example 1** (Chapter 3, "Simple Integer Arithmetic"): `123456789 * 987654321 * 112233445566778899 * 998877665544332211.` evaluates exactly to a 53-digit integer.

**Example 2** (Chapter 3, "Floating-Point Numbers"): `5 div 3` is `1` and `5 rem 3` is `2` — integer division and remainder.

# Relationships

## Builds Upon
- This is a foundational data type and does not build upon another card in this source.

## Enables
- **String** — A string-as-list is built from integer codepoints.

## Related
- **Term** — An integer is a primitive term.
- **String** — Strings are lists of integer codepoints.

## Contrasts With
- **Float** — Integers are exact and arbitrary-sized; floats are 64-bit IEEE 754 with rounding error. Dividing integers with `/` produces a float; `4/2` is `2.0`, not `2`.

# Common Errors

- **Error**: Using `/` and expecting an integer result.
  **Correction**: `/` always yields a float; use `div` for integer division.

- **Error**: Worrying about overflow when multiplying large integers.
  **Correction**: Erlang integers are arbitrary-sized and exact; there is no overflow.

# Common Confusions

- **Confusion**: Thinking Erlang integers have a fixed word-size limit like C `int`.
  **Clarification**: They are arbitrary-sized; arithmetic is exact regardless of magnitude.

- **Confusion**: Believing `4/2` gives the integer `2`.
  **Clarification**: Integer division with `/` yields a float — `4/2` is `2.0`.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Simple Integer Arithmetic" and "Floating-Point Numbers." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation from Chapter 3, "Simple Integer Arithmetic."
- Confidence rationale: HIGH — arbitrary-size, exact arithmetic is explicitly stated.
- Uncertainties: The book points to a later "Integers" section for full base-notation detail; this card covers the Chapter 3 treatment.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
