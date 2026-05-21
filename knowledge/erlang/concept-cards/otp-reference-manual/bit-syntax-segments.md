---
# === CORE IDENTIFICATION ===
concept: Bit Syntax Segment Types
slug: bit-syntax-segments

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
  - "type specifier list"
  - "bit syntax type specifiers"
  - "segment specifiers"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bit-syntax-expressions
extends:
  - bit-syntax-expressions
related:
  - guard-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What type specifiers are available in Erlang's bit syntax?"
  - "How do endianness and signedness work in bit syntax?"
  - "How do I specify segment types in bit string construction and matching?"
---

# Quick Definition

Bit syntax segments have a type specifier list controlling the type, signedness, endianness, and unit of each segment. The specifiers are separated by hyphens and include types like `integer`, `float`, `binary`, `bitstring`, and the Unicode types `utf8`, `utf16`, `utf32`.

# Core Definition

`TypeSpecifierList` is a list of type specifiers in any order, separated by hyphens. It controls four dimensions: Type (`integer` | `float` | `binary` | `bytes` | `bitstring` | `bits` | `utf8` | `utf16` | `utf32`, default `integer`), Signedness (`signed` | `unsigned`, default `unsigned`, only for matching integers), Endianness (`big` | `little` | `native`, default `big`), and Unit (`unit:IntegerLiteral`, range 1-256, default 1 for integer/float/bitstring, 8 for binary). The segment size in bits equals `Size * Unit`. For `utf8`/`utf16`/`utf32` types, size must not be given as it is implicitly determined. When constructing integer segments, if the size is too small, the most significant bits are silently discarded. Float segments must be 16, 32, or 64 bits (Erlang Reference Manual, "Bit Syntax Expressions" section).

# Prerequisites

- **bit-syntax-expressions** — Must understand the basic `<<>>` syntax before learning segment specifiers.

# Key Properties

1. **Type**: `integer` (default), `float`, `binary`/`bytes`, `bitstring`/`bits`, `utf8`, `utf16`, `utf32`.
2. **Signedness**: `signed` or `unsigned` (default). Only relevant for matching integers.
3. **Endianness**: `big` (default), `little`, or `native`. Only relevant for `integer`, `float`, `utf16`, `utf32`.
4. **Unit**: `unit:N` where N is 1-256. Default is 1 for integer/float/bitstring, 8 for binary.
5. Segment size in bits = `Size * Unit`.
6. Float segments must be exactly 16, 32, or 64 bits.
7. Integer truncation: if segment size is too small, MSBs are silently discarded (e.g., `<<16#ff:4>>` becomes `<<15:4>>`).
8. UTF types have implicit sizes: `utf8` = 1-4 bytes, `utf16` = 2 or 4 bytes, `utf32` = 4 bytes.
9. `bytes` is shorthand for `binary`; `bits` is shorthand for `bitstring`.
10. Binary segments without size match only if the remaining bits are evenly divisible by the unit.

# Construction / Recognition

## To Specify a Segment:
1. Start with the value: `Value`.
2. Optionally add size: `Value:Size`.
3. Optionally add type specifiers: `Value:Size/Type-Signedness-Endianness-Unit`.
4. Specifiers can be in any order, separated by hyphens.

## To Recognize:
1. Look for the `/` separator after the value or size in a bit string element.
2. Specifiers are hyphen-separated keywords.

# Context & Application

Segment type specifiers are essential for working with binary protocols and data formats. Endianness control enables parsing of network protocols (big-endian) and Intel-format data (little-endian). The Unicode types simplify encoding and decoding of Unicode text. Unit specifiers enable matching of bit strings with specific alignment requirements.

# Examples

**Example 1** (Bit Syntax section): Little-endian matching:

```erlang
<<16#1234:16/little>> = <<16#3412:16>> = <<16#34:8, 16#12:8>>
```

**Example 2** (Bit Syntax section): Binary segment matching with unit:

```erlang
1> <<_/binary-unit:16>> = <<"">>.
<<>>
2> <<_/binary-unit:16>> = <<"a">>.
** exception error: no match of right hand side value <<"a">>
3> <<_/binary-unit:16>> = <<"ab">>.
<<"ab">>
```

**Example 3** (Bit Syntax section): Unicode segment:

```erlang
13> <<1024/utf8>>.
<<208,128>>
```

**Example 4** (Bit Syntax section): Integer truncation:

```erlang
<<16#ff:4>>  % results in <<15:4>>
```

# Relationships

## Builds Upon
- **bit-syntax-expressions** — Segment types refine the basic bit syntax.

## Enables
- No directly dependent concepts in this extraction.

## Related
- **guard-expressions** — Bit string matching with type specifiers can appear in guards.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Specifying a size for UTF types.
  **Correction**: UTF types (`utf8`, `utf16`, `utf32`) have implicit sizes; do not specify a `Size`.

- **Error**: Using a float segment size that is not 16, 32, or 64.
  **Correction**: Float segments must be exactly 16, 32, or 64 bits.

- **Error**: Expecting integer truncation to raise an error.
  **Correction**: When an integer is too large for its segment, bits are silently discarded from the most significant end.

# Common Confusions

- **Confusion**: Thinking `binary` and `bitstring` are the same type specifier.
  **Clarification**: `binary` (or `bytes`) has a default unit of 8 (byte-aligned), while `bitstring` (or `bits`) has a default unit of 1 (bit-aligned).

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Bit Syntax Expressions" section (TypeSpecifierList, Integer segments, Float segments, Binary segments, Unicode segments subsections).

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — complete type specifier list with defaults and constraints explicitly provided
- Uncertainties: None
- Cross-reference status: Prerequisites verified
