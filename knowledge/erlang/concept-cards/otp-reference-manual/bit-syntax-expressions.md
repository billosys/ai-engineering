---
# === CORE IDENTIFICATION ===
concept: Bit Syntax Expressions
slug: bit-syntax-expressions

# === CLASSIFICATION ===
category: data-types
subcategory: bit-strings
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Bit Syntax Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "binary syntax"
  - "bit string syntax"
  - "binary expressions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - bit-syntax-segments
  - binary-comprehension
  - guard-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct and match bit strings (binaries) in Erlang?"
  - "What is the bit syntax in Erlang?"
---

# Quick Definition

Bit syntax expressions construct and match bit strings using the `<<>>` notation. Each element specifies a segment with an optional size and type specifier list, enabling precise binary data manipulation.

# Core Definition

The bit syntax operates on bit strings, which are sequences of bits ordered from most significant to least significant. The syntax `<<E1,...,En>>` constructs or matches a bit string, where each element `Ei` specifies a segment. Each segment specification has the form `Value:Size/TypeSpecifierList`, where `Size` and `TypeSpecifierList` are optional. A bit string with a length that is a multiple of 8 bits is known as a binary. When constructing, `Value` must evaluate to an integer, float, or bit string. When matching, `Value` must be a variable, integer, float, or string. `Size` specifies the segment size in units; its default depends on the type (8 for integer, 64 for float, whole value for binary/bitstring). String literals like `<<"abc">>` are syntactic sugar for `<<$a,$b,$c>>` (Erlang Reference Manual, "Bit Syntax Expressions" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Empty bit string: `<<>>` (zero length).
2. Segment syntax: `Value`, `Value:Size`, `Value/TypeSpecifierList`, or `Value:Size/TypeSpecifierList`.
3. Default type is `integer` with default size 8 bits.
4. Default size for `float` is 64 bits; for `binary`/`bitstring`, it is the whole value.
5. In matching, the default size for binary/bitstring is only valid for the last element.
6. A binary is a bit string whose length is a multiple of 8 bits.
7. Bit string patterns cannot be nested.
8. `<<"abc">>` is syntactic sugar for `<<$a,$b,$c>>`.
9. Space is required after `=` before `<<`: `B = <<1>>` (not `B=<<1>>`, which parses as `B =< <1>`).

# Construction / Recognition

## To Construct a Bit String:
1. Start with `<<`.
2. Add segment specifications separated by commas.
3. Each segment: `Value:Size/TypeSpecifierList`.
4. End with `>>`.

## To Match a Bit String:
1. Use `<<Pattern:Size/TypeSpecifierList, ...>> = BitString`.
2. Ensure all elements except the last have explicit sizes.
3. Variables in Size must be already bound.

# Context & Application

Bit syntax is one of Erlang's most powerful features for systems programming. It enables parsing and constructing binary protocols, file formats, and network packets with a declarative syntax. The bit-level granularity makes it suitable for protocol implementations where fields may not align to byte boundaries.

# Examples

**Example 1** (Bit Syntax section): Matching segments:

```erlang
2> <<A:3/binary, B/binary>> = <<"abcde">>.
<<"abcde">>
3> A.
<<"abc">>
4> B.
<<"de">>
```

**Example 2** (Bit Syntax section): Integer segments with different sizes:

```erlang
3> Bin3 = <<1,17,42:16>>.
<<1,17,0,42>>
4> <<A,B,C:16>> = <<1,17,42:16>>.
<<1,17,0,42>>
5> C.
42
```

**Example 3** (Bit Syntax section): Binary and bitstring segments:

```erlang
9> <<G,H/binary>> = <<1,17,42:16>>.
<<1,17,0,42>>
10> H.
<<17,0,42>>
11> <<G,J/bitstring>> = <<1,17,42:12>>.
<<1,17,2,10:4>>
12> J.
<<17,2,10:4>>
```

**Example 4** (Bit Syntax section): UTF-8 encoding:

```erlang
13> <<1024/utf8>>.
<<208,128>>
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **bit-syntax-segments** — Detailed segment type specifiers build on the basic syntax.
- **binary-comprehensions** — Binary comprehensions use bit syntax for element construction and matching.

## Related
- **guard-expressions** — Bit string matching can be used in guards.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Writing `B=<<1>>` without a space after `=`.
  **Correction**: Write `B = <<1>>`; without the space, it parses as `B =< <1>` which is a syntax error.

- **Error**: Omitting size on non-final binary/bitstring segments in a pattern.
  **Correction**: All binary/bitstring segments except the last must have an explicit size.

# Common Confusions

- **Confusion**: Conflating bit strings and binaries.
  **Clarification**: A binary is a bit string whose length is a multiple of 8 bits. All binaries are bit strings, but not all bit strings are binaries.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Bit Syntax Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — extensive syntax and examples provided
- Uncertainties: None
- Cross-reference status: Related concepts verified against planned extractions
