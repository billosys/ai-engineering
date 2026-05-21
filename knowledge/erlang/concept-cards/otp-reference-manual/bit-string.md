---
# === CORE IDENTIFICATION ===
concept: Bit String
slug: bit-string

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Bit Strings and Binaries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - bitstring

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - binary
  - erlang-term
contrasts_with:
  - binary

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary and a bitstring?"
  - "What is an Erlang term?"
---

# Quick Definition
A bit string is used to store an area of untyped memory in Erlang. It is expressed using the bit syntax and can have any number of bits.

# Core Definition
The Erlang Reference Manual states: "A bit string is used to store an area of untyped memory." Bit strings are expressed using the bit syntax. A bit string whose number of bits is evenly divisible by eight is called a binary. The `is_bitstring/1` BIF tests whether a term is a bit string (Data Types, "Bit Strings and Binaries" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Stores an area of untyped memory
2. Expressed using the bit syntax: `<<...>>`
3. Can have any number of bits (not necessarily a multiple of 8)
4. A bit string with a bit count evenly divisible by 8 is a binary
5. All binaries are bit strings, but not all bit strings are binaries
6. Tested with `is_bitstring/1` BIF

# Construction / Recognition
## To Construct/Create:
1. Use bit syntax: `<<10,20>>` creates a 16-bit binary
2. Use string shorthand: `<<"ABC">>` creates a binary from string
3. Use bit-level specification: `<<1:1,0:1>>` creates a 2-bit bit string

## To Identify/Recognize:
1. Use `is_bitstring/1` to test if a term is a bit string (includes binaries)
2. Use `is_binary/1` to test if a term is specifically a binary (multiple of 8 bits)

# Context & Application
Bit strings and binaries are central to Erlang's strengths in network programming and protocol implementation. The bit syntax provides pattern matching on binary data at the bit level, making it easy to parse and construct protocol packets, file formats, and other binary data. Bit strings that are not byte-aligned (not a multiple of 8 bits) are less common but useful when working with bit-level protocols.

# Examples
**Example 1** (Data Types, "Bit Strings and Binaries" section):
```erlang
1> <<10,20>>.
<<10,20>>
2> <<"ABC">>.
<<"ABC">>
3> <<1:1,0:1>>.
<<2:2>>
```

**Example 2** (Data Types, "Bit Strings and Binaries" section): Testing with BIFs:
```erlang
1> is_bitstring(<<1:1>>).
true
2> is_binary(<<1:1>>).
false
3> is_binary(<<42>>).
true
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
- **binary** -- Binaries are a specialized subset of bit strings (evenly divisible by 8)

## Related
- **erlang-term** -- Bit strings are a kind of term

## Contrasts With
- **binary** -- A binary is a bit string whose bit count is evenly divisible by 8. `is_binary(<<1:1>>)` returns `false`, while `is_bitstring(<<1:1>>)` returns `true`.

# Common Errors
- **Error**: Using `is_binary/1` when you mean to accept any bit string
  **Correction**: Use `is_bitstring/1` if the data does not need to be byte-aligned

# Common Confusions
- **Confusion**: Treating "bit string" and "binary" as synonyms
  **Clarification**: All binaries are bit strings, but a bit string with a non-multiple-of-8 bit count is not a binary. `<<1:1>>` is a bit string but not a binary.

# Source Reference
Data Types chapter, "Bit Strings and Binaries" section.

# Verification Notes
- Definition source: Direct quote from source ("A bit string is used to store an area of untyped memory.")
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
