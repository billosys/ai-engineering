---
# === CORE IDENTIFICATION ===
concept: Number
slug: number

# === CLASSIFICATION ===
category: data-types
subcategory: numbers
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.1 Numbers and arithmetic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - integer
  - float
  - bignum
  - arithmetic

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - comparing-terms
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What numeric types does Erlang have?"
  - "How does integer division differ from float division in Erlang?"
  - "Can Erlang integers overflow?"
---

# Quick Definition

Erlang has two numeric types: integers, which are of arbitrary size and never overflow, and floats, which use 64-bit IEEE 754 double precision.

# Core Definition

"Erlang has two numerical data types: integers and floating-point numbers (floats). Conversion is done automatically by most of the arithmetic operations" (Chapter 2, section 2.2.1). Integers can be of arbitrary size: small ones fit in a machine word; larger ones (*bignums*) automatically allocate the space they need — "you never need to worry about truncation or wraparound effects." Integers can be written in any base 2–36 using `Base#Digits` notation, and `$`-prefix notation yields a character's code point. Floats use 64-bit IEEE 754-1985 double precision; Erlang requires a float to start with a digit (`0.01`, not `.01`), and there are no single-precision floats. The `/` operator always yields a float; integer (truncating) division uses `div` and the remainder uses `rem`. Bitwise operators include `bsl`, `bsr`, `band`, `bor`, `bxor`, and `bnot`.

# Prerequisites

- **Erlang term** — numbers are one kind of term.

# Key Properties

1. Two numeric types: integers and floats.
2. Integers are arbitrary precision; large ones become bignums automatically — no overflow or wraparound.
3. Integers can be written in any base 2–36 via `Base#Digits`; `$c` gives a character's code.
4. Floats are 64-bit IEEE 754 double precision; there is no single precision.
5. A float literal must start with a digit (`0.01`, not `.01`).
6. `/` always yields a float; `div` is integer division; `rem` is the remainder.
7. Bitwise integer operators: `bsl`, `bsr`, `band`, `bor`, `bxor`, `bnot`.

# Construction / Recognition

## To Construct/Create:
1. Write an integer (`101`, `-101`, `16#FFff`, `$z`) or a float (`3.14`, `6.022137e23`).
2. Apply arithmetic operators; integers are coerced to float as needed.
3. Use `div`/`rem` for integer division, `/` for float division.

# Context & Application

- **Typical contexts**: All numeric computation.
- **Common applications**: Counters, sizes, byte values, character codes.
- **Historical/stylistic notes**: The `Base#Digits` notation was borrowed from the Ada programming language. Float math functions live in the standard `math` module.

# Examples

**Example 1** (section 2.2.1): `2 * 3.14` yields the float `6.28`; `4/2` yields `2.0`; `7 div 2` yields `3`; `15 rem 4` yields `3`.

**Example 2** (section 2.2.1): `16#FFffFFff`, `2#10101`, and `36#ZZ` show integers written in bases 16, 2, and 36; `$9`, `$z`, `$\n` give character codes.

# Relationships

## Builds Upon
- **Erlang term** — a number is a term.

## Enables
- Arithmetic computation throughout Erlang programs.

## Related
- **Comparing terms** — numbers have arithmetic and exact comparison operators.
- **Built-in function** — arithmetic operators are BIFs in the `erlang` module.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Writing a float as `.01`.
  **Correction**: Erlang requires a float to start with a digit: `0.01`.

- **Error**: Expecting `/` to do integer division.
  **Correction**: `/` always yields a float; use `div` for truncating integer division.

# Common Confusions

- **Confusion**: Expecting integer overflow or wraparound as in C/Java.
  **Clarification**: Erlang integers are arbitrary precision; they grow into bignums automatically.

- **Confusion**: Thinking `float` means single precision (as in C/C++/Java).
  **Clarification**: All Erlang floats are 64-bit double precision; there is no single precision.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.1 "Numbers and arithmetic" (Integers, Floats, and Arithmetic and bitwise operations subsections).

# Verification Notes

- Definition source: Direct adaptation from section 2.2.1.
- Confidence rationale: HIGH — numeric types and operators are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
