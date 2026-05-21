---
# === CORE IDENTIFICATION ===
concept: Bit Syntax
slug: bit-syntax

# === CLASSIFICATION ===
category: data-types
subcategory: binary-data
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Binaries and the Bit Syntax"
chapter_number: 7
pdf_page: null
section: "The Bit Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bit syntax expression
  - segment syntax
  - "TypeSpecifierList"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
  - pattern-matching
extends:
  - binary
related:
  - bitstring
  - binary-pattern-matching
  - macro
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the bit syntax?"
  - "How do I pack and unpack bits with the bit syntax?"
  - "What is a segment and a type specifier list?"
---

# Quick Definition

The bit syntax is the `<<...>>` notation for packing and extracting individual bits or sequences of bits in binary data, where each element is a segment described by a value, size, and type specifier.

# Core Definition

"The bit syntax is a notation used for extracting and packing individual bits or sequences of bits in binary data" ("Binaries and the Bit Syntax", *The Bit Syntax*). A bit syntax expression has the form `<<>>` or `<<E1, E2, ..., En>>`, where each element `Ei` specifies a single *segment*. Each segment has one of four forms: `Value`, `Value:Size`, `Value/TypeSpecifierList`, or `Value:Size/TypeSpecifierList`. If the total number of bits is evenly divisible by 8, the result is a binary; otherwise it is a bitstring. `Size` gives the segment size; the `TypeSpecifierList` is a hyphen-separated list of `End-Sign-Type-Unit` items (any may be omitted, in any order). The total size of a segment is `Size × Unit` bits. The bit syntax was developed for protocol programming and "produces highly efficient code for manipulating binary data."

# Prerequisites

- **Binary** — The bit syntax constructs and destructures binaries (and bitstrings).
- **Pattern matching** — Unpacking bits is a pattern matching operation.

# Key Properties

1. Written `<<E1, ..., En>>`, each `Ei` a segment.
2. A segment is `Value`, `Value:Size`, `Value/TypeSpecifierList`, or `Value:Size/TypeSpecifierList`.
3. `End` is `big | little | native`; default `big` (network byte order).
4. `Sign` is `signed | unsigned` (used only in matching); default `unsigned`.
5. `Type` is `integer | float | binary | bytes | bitstring | bits | utf8 | utf16 | utf32`; default `integer`.
6. `Unit` is `unit:1..256`; default 1 for integer/float/bitstring, 8 for binary; segment size is `Size × Unit` bits.
7. Default `Size` is 8 for integer, 64 for float, the binary's size for binary.
8. A `Size` can be taken from a value unpacked earlier in the same pattern.
9. The compiler turns bit syntax patterns into highly optimized field-extraction code.

# Construction / Recognition

## To Construct/Create:
1. Pack values: `Mem = <<Red:5, Green:6, Blue:5>>` builds a 16-bit binary.
2. Add type info per segment: `<<X:32/big>>`, `<<X:32/little>>`, `<<C:4/binary, _/binary>>`.

## To Identify/Recognize:
1. Unpack with a pattern: `<<R1:5, G1:6, B1:5>> = Mem`.
2. A leading literal bit pattern such as `2#11111111111:11` matches a fixed bit prefix.

# Context & Application

- **Typical contexts**: low-level protocol and file-format programming where data is not byte-aligned.
- **Common applications**: the book's real-world examples — finding the MPEG audio sync frame, unpacking Microsoft COFF data, and parsing an IPv4 datagram header in a single pattern match.
- **Historical/stylistic notes**: the book advises experimenting in the shell until the pattern is right, then pasting it into the program.

# Examples

**Example 1** (*Packing and Unpacking 16-Bit Colors*): packing an RGB triplet:

```erlang
4> Mem = <<Red:5, Green:6, Blue:5>>.
<<23,180>>
5> <<R1:5, G1:6, B1:5>> = Mem.
```

**Example 2** (*Finding the Synchronization Frame in MPEG Data*): a single-pattern MPEG header decode:

```erlang
decode_header(<<2#11111111111:11,B:2,C:2,_D:1,E:4,F:2,G:1,Bits:9>>) ->
```

`2#11111111111` is a base-2 integer matching eleven consecutive 1 bits, then `B:2`, `C:2`, and so on.

## Worked Example

A variable-size segment whose length comes from an earlier field (*Bit Syntax Expressions*):

```erlang
<<Size:4, Data:Size/binary, ...>>
```

The value of `Size` is unpacked from the first four bits and then used as the size of the next segment.

# Relationships

## Builds Upon
- **Binary** — The bit syntax is the primary notation for binaries.

## Enables
- **Binary pattern matching** — Bit syntax patterns destructure binaries.
- **Bitstring** — When the total bit count is not a multiple of 8, the bit syntax yields a bitstring.

## Related
- **Macro** — Macros like `?DWORD` expand to `32/unsigned-little-integer` type specifier text to keep the semantic gap small.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Forgetting to specify endianness when exchanging integers between machines.
  **Correction**: Use the correct `End` (`big`/`little`/`native`) specifier when packing or unpacking integers across endian boundaries.

- **Error**: Giving a binary-typed segment a size not divisible by 8.
  **Correction**: A segment of type `binary` must have a size that is evenly divisible by 8.

# Common Confusions

- **Confusion**: Believing every bit syntax expression yields a binary.
  **Clarification**: It yields a binary only when the total bit count is divisible by 8; otherwise the result is a bitstring.

- **Confusion**: Thinking `Size` is always a fixed literal.
  **Clarification**: In a pattern, `Size` can be a bound variable whose value was unpacked from an earlier segment.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", sections "The Bit Syntax", "Packing and Unpacking 16-Bit Colors", "Bit Syntax Expressions", "Real-World Bit Syntax Examples" (MPEG sync, COFF, IPv4 datagram).

# Verification Notes

- Definition source: Direct quotation and adaptation from *The Bit Syntax* and *Bit Syntax Expressions*.
- Confidence rationale: HIGH — the source fully specifies the syntax, segment forms, and type specifiers with multiple real-world examples.
- Uncertainties: None.
- Cross-reference status: Slugs `binary` exists; `bitstring`, `binary-pattern-matching`, `macro` extracted in scope; `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
