---
# === CORE IDENTIFICATION ===
concept: Binary Pattern Matching
slug: binary-pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Binaries and the Bit Syntax"
chapter_number: 7
pdf_page: null
section: "Bit Syntax Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - binary matching
  - unpacking binaries

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
  - bit-syntax
  - pattern-matching
extends:
  - pattern-matching
related:
  - bitstring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match on binaries with the bit syntax?"
  - "How do I unpack a protocol packet in one pattern?"
  - "What rules govern Size in a binary pattern?"
---

# Quick Definition

Binary pattern matching uses bit syntax expressions on the left of a match to destructure a binary into named fields, extracting bit- and byte-level structure in a single operation.

# Core Definition

When a bit syntax expression is used in a match, it destructures a binary. "When used in a pattern matching operation, `Value` can be a bound or unbound variable, integer, literal string, float, or binary" ("Binaries and the Bit Syntax", *Bit Syntax Expressions*). `Size` "must be an integer or a bound variable whose value is an integer... at the point in the pattern where the value is needed" — and crucially, "the value of the `Size` can be obtained from earlier pattern matches in the binary." This means a length field unpacked from the front of a binary can drive the size of a later segment. The Erlang compiler turns binary patterns into highly optimized field-extraction code.

# Prerequisites

- **Binary** — Binary patterns destructure binary values.
- **Bit syntax** — Binary patterns are bit syntax expressions used in match position.
- **Pattern matching** — This is a specialized form of Erlang pattern matching.

# Key Properties

1. A binary pattern is a `<<...>>` bit syntax expression on the left of `=` (or in a function/`case` head).
2. Pattern segments may contain bound or unbound variables, integers, literal strings, floats, or binaries.
3. `Size` in a pattern must be an integer or a bound variable; the default size is valid only for the last element.
4. A `Size` may be a variable bound by an earlier segment in the same binary.
5. The `signed`/`unsigned` specifier matters only in matching; default `unsigned`.
6. Patterns can extract fields that do not fall on byte boundaries.
7. The compiler generates optimal field-extraction code from binary patterns.

# Construction / Recognition

## To Construct/Create:
1. Unpack with a literal-size pattern: `<<R1:5, G1:6, B1:5>> = Mem`.
2. Use an earlier field as a later size: `<<Size:4, Data:Size/binary, ...>>`.
3. Match a fixed bit prefix with a literal: `<<2#11111111111:11, B:2, ...>>`.

## To Identify/Recognize:
1. A `<<...>>` form in match position is a binary pattern.

# Context & Application

- **Typical contexts**: parsing protocol packets and binary file formats.
- **Common applications**: the IPv4 datagram example matches the whole header — including the 3-bit `Flags` and 13-bit `FragOff` fields — in one pattern; `get_word` uses `<<C:4/binary, _/binary>>` to take the first four bytes.
- **Historical/stylistic notes**: a guard can refine a binary match, e.g. `when HLen >= 5, 4*HLen =< DgramSize`.

# Examples

**Example 1** (*Packing and Unpacking 16-Bit Colors*): unpacking an RGB triplet:

```erlang
5> <<R1:5, G1:6, B1:5>> = Mem.
```

**Example 2** (*Unpacking the Header of an IPv4 Datagram*): matching a datagram header in one pattern:

```erlang
case Dgram of
    <<?IP_VERSION:4, HLen:4, SrvcType:8, TotLen:16,
      ID:16, Flags:3, FragOff:13,
      TTL:8, Proto:8, HdrChkSum:16,
      SrcIP:32,
      DestIP:32, RestDgram/binary>> when HLen >= 5, 4*HLen =< DgramSize ->
        OptsLen = 4*(HLen - ?IP_MIN_HDR_LEN),
        <<Opts:OptsLen/binary, Data/binary>> = RestDgram,
        ...
```

The non-byte-aligned `Flags` (3 bits) and `FragOff` (13 bits) are extracted directly; `Opts` uses a runtime-computed size.

# Relationships

## Builds Upon
- **Pattern matching** — Binary matching is a kind of Erlang pattern matching.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Bitstring** — Bit-level patterns may match or produce bitstrings.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Using an unbound variable as a segment `Size` in a pattern.
  **Correction**: `Size` must be an integer or a variable already bound — possibly from an earlier segment in the same binary.

- **Error**: Omitting the size on a non-final segment expecting a default.
  **Correction**: The default size applies only to the very last element of a pattern.

# Common Confusions

- **Confusion**: Thinking binary patterns can only extract whole bytes.
  **Clarification**: They extract arbitrary bit fields, including ones that do not fall on byte boundaries.

- **Confusion**: Believing the size of every field must be known at compile time.
  **Clarification**: A size can be a variable bound by an earlier field, enabling variable-length segments.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", sections "Bit Syntax Expressions", "Packing and Unpacking 16-Bit Colors", "Unpacking the Header of an IPv4 Datagram".

# Verification Notes

- Definition source: Direct adaptation of the pattern-matching rules in *Bit Syntax Expressions* and the IPv4 example.
- Confidence rationale: HIGH — the source explicitly states the matching rules and demonstrates them on real protocol data.
- Uncertainties: None.
- Cross-reference status: Slugs `binary` exists; `bit-syntax`, `bitstring` extracted in scope; `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
