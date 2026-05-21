---
# === CORE IDENTIFICATION ===
concept: Numeric Notation
slug: numeric-notation

# === CLASSIFICATION ===
category: data-types
subcategory: numeric
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Number"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erlang-specific numeric literals
  - "base#digits notation"
  - "$char notation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integer
  - float
extends:
  - integer
  - float
related:
  - erlang-term
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
Erlang provides three special notations for numeric literals beyond conventional decimal: `$char` for character code points, `base#digits` for arbitrary-base integers, and `base#digits.digits#eExponent` for based floating-point numbers.

# Core Definition
In addition to standard decimal notation, Erlang supports three specific notations for numeric literals. `$char` yields the ASCII value or Unicode code point of the character. `base#digits` represents an integer in a base from 2 to 36, using digits 0-9 and letters A-Z (case-insensitive). `base#digits.digits#eexponent` represents a based floating-point number for exact textual representation. Leading zeroes are ignored, and single underscore characters can be inserted between digits as visual separators (Data Types, "Number" section).

# Prerequisites
- **integer** -- The `$char` and `base#digits` notations produce integers
- **float** -- The based floating-point notation produces floats

# Key Properties
1. `$char` -- yields the ASCII value or Unicode code point of `char`
2. `$\escape` -- works with escape sequences (e.g., `$\n` yields 10)
3. `base#digits` -- integer in base 2-36; digits are 0-9 plus A-Z (upper or lowercase)
4. `base#digits.digits#eexponent` -- based floating-point; exponent is always decimal
5. Erlang does NOT support C-style prefixes (`0x` for hex, `077` for octal)
6. Leading zeroes are ignored
7. Single underscores between digits serve as visual separators

# Construction / Recognition
## To Construct/Create:
1. Character code: `$A` (65), `$\n` (10), `$\t` (9)
2. Binary integer: `2#101` (5), `2#1111_0000` (240)
3. Octal integer: `8#77` (63)
4. Hexadecimal integer: `16#1f` (31), `16#FF` (255)
5. Base-36: `36#helloworld` (1767707668033969)
6. Based float: `16#ff.fe#e+6`
7. With separators: `16#4865_316F_774F_6C64`

## To Identify/Recognize:
1. `$` prefix indicates character notation
2. `#` between base and digits indicates based notation
3. Digits beyond 0-9 (A-Z) indicate a base higher than 10

# Context & Application
The `$char` notation is commonly used when working with string processing, as Erlang strings are lists of integer code points. The based notation is particularly useful in systems programming for hexadecimal and binary representations. The Ada-style `base#digits` notation replaces the more common `0x` and `0b` prefixes found in other languages. Based floating-point notation using base 16 or 2 enables exact textual representation of float values.

# Examples
**Example 1** (Data Types, "Number" section):
```erlang
3> $A.
65
4> $\n.
10
5> 2#101.
5
6> 16#1f.
31
7> 16#4865_316F_774F_6C64.
5216630098191412324
12> 36#helloworld.
1767707668033969
```

# Relationships
## Builds Upon
- **integer** -- `$char` and `base#digits` produce integer values
- **float** -- Based floating-point produces float values

## Enables
- **string** -- Understanding `$char` notation is essential for working with Erlang strings as lists of code points

## Related
- **erlang-term** -- Numeric notations produce terms
- **escape-sequence** -- `$\escape` uses escape sequences to produce character codes

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Using `0xFF` or `0b101` for hexadecimal or binary notation
  **Correction**: Erlang uses `base#digits` notation: `16#FF` and `2#101`

- **Error**: Using a base larger than 36
  **Correction**: The base must be an integer in the range 2 through 36

# Common Confusions
- **Confusion**: Expecting `$A` to return the character 'A' as an atom or string
  **Clarification**: `$A` returns the integer 65 (the code point). Characters are integers in Erlang.

# Source Reference
Data Types chapter, "Number" section.

# Verification Notes
- Definition source: Direct from source material
- Confidence rationale: High -- explicit description with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
