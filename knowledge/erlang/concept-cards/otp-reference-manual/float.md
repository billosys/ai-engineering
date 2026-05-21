---
# === CORE IDENTIFICATION ===
concept: Float
slug: float

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
aliases:
  - floating-point number

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - integer
  - erlang-term
  - floating-point-representation
  - numeric-notation
contrasts_with:
  - integer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A float is one of the two numeric literal types in Erlang, representing floating-point numbers using 64-bit IEEE 754 representation (without support for Inf or NaN).

# Core Definition
Floats are one of the two types of numeric literals in Erlang. They use 64-bit representation and must start with a digit and contain a decimal point -- literals such as `.01` and `1e6` are not valid and must be written as `0.01` and `1.0e6`. Erlang also supports based floating-point notation (e.g., `16#ff.fe#e+6`) for exact textual representation. Erlang's floats do not match IEEE 754 exactly: neither Inf nor NaN are supported, and any operation producing them raises a `badarith` exception (Data Types, "Number" and "Representation of Floating-Point Numbers" sections).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Uses 64-bit floating-point representation
2. Must start with a digit and contain a decimal point (`.01` is invalid; use `0.01`)
3. Supports scientific notation: `2.3e3`, `2.3e-3`
4. Supports based floating-point notation: `16#ff.fe#e+6`
5. Single underscores can be inserted between digits as visual separators
6. Does not support Inf or NaN -- operations producing them raise `badarith`
7. Has two representations for zero: `0.0` and `-0.0`, which are numerically equal (`==`) but not term-equivalent (`=:=`)
8. Shares a linear order with integers (`1 < 2.4`, `5 == 5.0`)

# Construction / Recognition
## To Construct/Create:
1. Write a decimal float literal: `2.3`, `0.01`
2. Use scientific notation: `2.3e3`, `2.3e-3`
3. Use based notation for exact representation: `16#ff.fe#e+6`
4. Use underscores: `1_234.333_333`

## To Identify/Recognize:
1. Use `is_float/1` BIF to test whether a term is a float
2. Float literals always contain a decimal point

# Context & Application
Floats are used for calculations requiring fractional values, scientific computation, and geometric operations. Due to the inherent imprecision of binary floating-point representation, care must be taken when comparing float values. For exact decimal arithmetic (e.g., financial calculations), the manual recommends using a dedicated library or working in the smallest unit (cents instead of dollars).

**Comparison caveat**: Since OTP 27, `0.0 =:= -0.0` evaluates to `false`. Code comparing against `0.0` should use `==` with `is_float/1` guards for numeric equality, or write `+0.0` to silence compiler warnings about the distinction.

# Examples
**Example 1** (Data Types, "Number" section):
```erlang
8> 2.3.
2.3
9> 2.3e3.
2.3e3
10> 2.3e-3.
0.0023
11> 1_234.333_333
1234.333333
```

**Example 2** (Data Types, "Comparisons" section):
```erlang
1> 0.0 =:= +0.0.
true
2> 0.0 =:= -0.0.
false
3> +0.0 =:= -0.0.
false
4> +0.0 == -0.0.
true
```

**Example 3** (Data Types, "Representation of Floating-Point Numbers" section):
```erlang
1> 0.1+0.2.
0.30000000000000004
```

**Example 4** (Data Types, "Representation of Floating-Point Numbers" section): Division by zero raises an exception:
```erlang
1> 1.0 / 0.0.
** exception error: an error occurred when evaluating an arithmetic expression
```

# Relationships
## Builds Upon
This is a foundational numeric type with no prerequisites.

## Enables
- **floating-point-representation** -- Understanding float limitations depends on knowing what floats are

## Related
- **erlang-term** -- Floats are a kind of term
- **integer** -- The other numeric type; shares a linear order with floats

## Contrasts With
- **integer** -- Integers have arbitrary precision and distinct representations; floats have limited precision and two representations for zero

# Common Errors
- **Error**: Writing `.01` or `1e6` as float literals
  **Correction**: Floats must start with a digit and contain a `.`. Write `0.01` and `1.0e6`.

- **Error**: Dividing by `0.0` expecting Inf
  **Correction**: Erlang raises `badarith` for operations that would produce Inf or NaN.

- **Error**: Using `=:=` to compare floats against zero
  **Correction**: Use `==` with `is_float/1` guards, since `0.0 =:= -0.0` is `false` as of OTP 27.

# Common Confusions
- **Confusion**: Expecting `0.1 + 0.2` to equal `0.3` exactly
  **Clarification**: Binary floating-point cannot represent `0.1` or `0.2` exactly, so the result is `0.30000000000000004`.

- **Confusion**: Assuming Erlang floats fully implement IEEE 754
  **Clarification**: Erlang floats do not support Inf or NaN. Any operation that would produce these values raises a `badarith` exception.

# Source Reference
Data Types chapter, "Number" section, "Comparisons" subsection, and "Representation of Floating-Point Numbers" subsection.

# Verification Notes
- Definition source: Direct from source material
- Confidence rationale: High -- explicit definition with detailed examples and caveats
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
