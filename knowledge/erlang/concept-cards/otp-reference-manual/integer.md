---
# === CORE IDENTIFICATION ===
concept: Integer
slug: integer

# === CLASSIFICATION ===
category: data-types
subcategory: numeric
tier: foundational

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - float
  - erlang-term
  - numeric-notation
contrasts_with:
  - float

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
---

# Quick Definition
An integer is one of the two numeric literal types in Erlang, representing whole numbers with arbitrary precision (no fixed size limit).

# Core Definition
Integers are one of the two types of numeric literals in Erlang (the other being floats). They support conventional decimal notation as well as three Erlang-specific notations: `$char` for character code points, `base#digits` for arbitrary-base integers (bases 2-36), and underscore separators for readability. Leading zeroes are ignored. Integers have a distinct representation for every number, making term equivalence (`=:=`) reliable for integer comparison (Data Types, "Number" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Arbitrary precision -- no fixed upper or lower bound
2. Support conventional decimal notation (e.g., `42`, `-1234567890`)
3. Support `$char` notation for ASCII/Unicode code points (e.g., `$A` yields `65`)
4. Support `base#digits` notation for bases 2-36 (e.g., `2#101` yields `5`, `16#1f` yields `31`)
5. Leading zeroes are ignored
6. Single underscores can be inserted between digits as visual separators (e.g., `-1_234_567_890`)
7. Each integer has a distinct representation, so `=:=` is reliable for comparison

# Construction / Recognition
## To Construct/Create:
1. Write a decimal literal: `42`, `-7`
2. Use character notation: `$A` (yields 65), `$\n` (yields 10)
3. Use base notation: `16#ff` (yields 255), `2#101` (yields 5)
4. Use underscores for readability: `1_000_000`

## To Identify/Recognize:
1. Use `is_integer/1` BIF to test whether a term is an integer
2. Integers have no decimal point in their representation

# Context & Application
Integers in Erlang are used for counting, indexing (1-based), bit manipulation, and representing character code points. Their arbitrary precision makes them suitable for cryptographic operations and large number arithmetic without overflow concerns. Integers share a linear order with floats (`1` compares less than `2.4`), and `5` is equal to `5.0` under numeric comparison (`==`).

# Examples
**Example 1** (Data Types, "Number" section):
```erlang
1> 42.
42
2> -1_234_567_890.
-1234567890
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
```

**Example 2** (Data Types, "Number" section): Base-36 notation: `36#helloworld` yields `1767707668033969`.

# Relationships
## Builds Upon
This is a foundational numeric type with no prerequisites.

## Enables
- **numeric-notation** -- Erlang-specific integer notations extend how integers are expressed
- **list** -- Strings in Erlang are lists of integer code points
- **string** -- Strings are syntactic sugar for lists of integers

## Related
- **erlang-term** -- Integers are a kind of term
- **float** -- The other numeric type; shares a linear order with integers

## Contrasts With
- **float** -- Floats have decimal points and limited precision; integers have arbitrary precision and distinct representations

# Common Errors
- **Error**: Writing `.01` or `1e6` expecting integer or float notation
  **Correction**: Floats must start with a digit and contain a `.`; `1e6` is not valid -- write `1.0e6`. Plain integers use no decimal point.

- **Error**: Using `0x` or `077` for hexadecimal or octal notation
  **Correction**: Erlang does not support C-style prefixes. Use `16#ff` for hex and `8#77` for octal.

# Common Confusions
- **Confusion**: Expecting integers and floats to behave differently under comparison operators
  **Clarification**: Integers and floats share the same linear order. `1 < 2.4` is true, and `5 == 5.0` is true. However, `5 =:= 5.0` is false because they are different types.

# Source Reference
Data Types chapter, "Number" section and "Comparisons" subsection.

# Verification Notes
- Definition source: Direct from source material
- Confidence rationale: High -- explicit definition and extensive examples in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
