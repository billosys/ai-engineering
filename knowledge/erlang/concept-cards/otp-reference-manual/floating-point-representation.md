---
# === CORE IDENTIFICATION ===
concept: Floating-Point Representation
slug: floating-point-representation

# === CLASSIFICATION ===
category: data-types
subcategory: numeric
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Representation of Floating-Point Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - float representation
  - 64-bit float

# === TYPED RELATIONSHIPS ===
prerequisites:
  - float
extends:
  - float
related:
  - integer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
Erlang uses 64-bit base-2 floating-point representation, which means many base-10 decimal fractions cannot be represented exactly, and operations may produce unexpected results.

# Core Definition
Erlang uses 64-bit floats represented in a base-2 system, while printed floats use base-10. This fundamental mismatch means that many common decimal values (like 0.1 and 0.2) cannot be represented exactly. Additionally, Erlang's pretty printer may round displayed values, and a range of distinct float values may share the same internal representation. Erlang does not support IEEE 754 special values: operations that would produce NaN, +Inf, or -Inf raise a `badarith` exception instead (Data Types, "Representation of Floating-Point Numbers" section).

# Prerequisites
- **float** -- Understanding float representation requires knowing the basic float data type

# Key Properties
1. Uses 64 bits in base-2 internally
2. Printed representation uses base-10, causing representation mismatches
3. Real numbers like `0.1` and `0.2` cannot be represented exactly
4. Pretty printer may round values, making different internal values appear identical
5. A range of values may map to the same internal float (e.g., all values in `[36028797018963966.0, 36028797018963972.0]` are represented by `36028797018963968.0`)
6. Neither Inf nor NaN are supported; operations producing them raise `badarith`
7. Based floating-point notation (e.g., `16#ff.fe#e+6`) enables exact text representation

# Construction / Recognition
## To Construct/Create:
1. Any float literal creates a 64-bit float value
2. Use based notation for exact representation: `16#ff.fe#e+6`, `2#1.1#e3`

## To Identify/Recognize:
1. Arithmetic on floats that produces unexpected decimal results indicates representation limits
2. Operations resulting in division by zero or similar raise `badarith` rather than returning special values

# Context & Application
Understanding float representation is critical for any code performing numeric computation, comparison, or display of floating-point values. The manual recommends:
- For exact decimal fractions (e.g., money), use a dedicated library or work in the smallest integer unit (cents rather than dollars)
- For exact textual representation, use based floating-point notation (base 16 or base 2)
- For numeric float comparison, use `==` with `is_float/1` guards rather than `=:=`

# Examples
**Example 1** (Data Types, "Representation of Floating-Point Numbers" section): The classic `0.1 + 0.2` problem:
```erlang
1> 0.1+0.2.
0.30000000000000004
```

**Example 2** (Data Types, "Representation of Floating-Point Numbers" section): Pretty printer rounding:
```erlang
1> {36028797018963968.0, 36028797018963968 == 36028797018963968.0,
  36028797018963970.0, 36028797018963970 == 36028797018963970.0}.
{3.602879701896397e16, true,
 3.602879701896397e16, false}.
```
The value `36028797018963968` can be represented exactly, but the pretty printer rounds `36028797018963968.0` to `3.602879701896397e16`, which is actually `36028797018963970.0`.

**Example 3** (Data Types, "Representation of Floating-Point Numbers" section): Inf/NaN produce exceptions:
```erlang
1> 1.0 / 0.0.
** exception error: an error occurred when evaluating an arithmetic expression
2> 0.0 / 0.0.
** exception error: an error occurred when evaluating an arithmetic expression
```

# Relationships
## Builds Upon
- **float** -- This card elaborates on the representation details of the float type

## Enables
No direct dependents.

## Related
- **integer** -- Integers have arbitrary precision and do not suffer from representation issues

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Comparing computed float results for exact equality
  **Correction**: Use tolerance-based comparison or the `==` operator with type guards

- **Error**: Expecting `1.0 / 0.0` to return infinity
  **Correction**: Erlang raises `badarith`; handle division-by-zero explicitly

# Common Confusions
- **Confusion**: Believing that the pretty-printed value of a float is its exact value
  **Clarification**: The pretty printer rounds for display; multiple internal float values may print identically

- **Confusion**: Expecting Erlang to support IEEE 754 special values (Inf, NaN)
  **Clarification**: Erlang explicitly does not support these; operations that would produce them raise exceptions

# Source Reference
Data Types chapter, "Representation of Floating-Point Numbers" subsection. References external resources: "What Every Programmer Should Know About Floating-Point Arithmetic" and others.

# Verification Notes
- Definition source: Direct from source material
- Confidence rationale: High -- detailed explanation with examples in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
