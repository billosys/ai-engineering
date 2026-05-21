---
# === CORE IDENTIFICATION ===
concept: Binary
slug: binary

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bit-string
extends:
  - bit-string
related:
  - erlang-term
  - string
contrasts_with:
  - bit-string
  - string

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary and a bitstring?"
  - "What is an Erlang term?"
---

# Quick Definition
A binary is a bit string whose number of bits is evenly divisible by eight, making it a sequence of whole bytes. Binaries are the most common form of bit strings in Erlang.

# Core Definition
The Erlang Reference Manual defines binaries as: "Bit strings that consist of a number of bits that are evenly divisible by eight are called _binaries_." Binaries are tested with the `is_binary/1` BIF. They are expressed using the bit syntax and are the standard way to handle byte-oriented data such as file contents, network packets, and UTF-8 encoded strings (Data Types, "Bit Strings and Binaries" section).

# Prerequisites
- **bit-string** -- A binary is a specialized bit string; understanding bit strings is necessary

# Key Properties
1. A bit string whose bit count is evenly divisible by 8 (byte-aligned)
2. Expressed using the bit syntax: `<<10,20>>`, `<<"hello">>`
3. Tested with `is_binary/1` BIF (returns `true` only for byte-aligned bit strings)
4. Every binary is also a bit string (`is_bitstring/1` returns `true` for binaries)
5. Can represent byte sequences, file data, and UTF-8 encoded text

# Construction / Recognition
## To Construct/Create:
1. Use byte-value syntax: `<<10,20>>` creates a 2-byte binary
2. Use string shorthand: `<<"ABC">>` creates a binary from a string
3. Convert from list: `list_to_binary("hello")` produces `<<104,101,108,108,111>>`
4. Convert from other types: `integer_to_binary(77)`, `float_to_binary(7.0)`, `term_to_binary({a,b,c})`

## To Identify/Recognize:
1. Use `is_binary/1` BIF to test for binaries specifically
2. Use `is_bitstring/1` BIF to test more broadly (includes non-byte-aligned bit strings)

# Context & Application
Binaries are Erlang's primary data type for handling byte-oriented data. They are used extensively for:
- File I/O (reading and writing files)
- Network communication (TCP/UDP packets)
- UTF-8 encoded strings (via sigils like `~b"..."` or `<<"...">>`)
- Binary protocol parsing and construction
- Inter-node communication (term serialization)

Binaries are stored as contiguous byte sequences and can be shared between processes without copying (for binaries larger than 64 bytes on the heap).

# Examples
**Example 1** (Data Types, "Bit Strings and Binaries" section):
```erlang
1> <<10,20>>.
<<10,20>>
2> <<"ABC">>.
<<"ABC">>
3> is_binary(<<42>>).
true
```

**Example 2** (Data Types, "Type Conversions" section):
```erlang
3> binary_to_list(<<"hello">>).
"hello"
5> list_to_binary("hello").
<<104,101,108,108,111>>
12> term_to_binary({a,b,c}).
<<131,104,3,100,0,1,97,100,0,1,98,100,0,1,99>>
13> binary_to_term(<<131,104,3,100,0,1,97,100,0,1,98,100,0,1,99>>).
{a,b,c}
```

# Relationships
## Builds Upon
- **bit-string** -- A binary is a byte-aligned bit string

## Enables
- **sigil** -- The `~b` and `~B` sigils create UTF-8 encoded binaries

## Related
- **erlang-term** -- Binaries are a kind of term
- **string** -- Binaries can represent text (especially UTF-8); strings are lists of integers

## Contrasts With
- **bit-string** -- A bit string may have any number of bits; a binary must have a multiple of 8
- **string** -- Strings are lists of integers; binaries are contiguous byte sequences

# Common Errors
- **Error**: Assuming `is_binary/1` returns `true` for any bit string
  **Correction**: `is_binary/1` returns `false` for bit strings whose bit count is not a multiple of 8; use `is_bitstring/1` for the broader test

# Common Confusions
- **Confusion**: Confusing binary strings (`<<"hello">>`) with Erlang strings (`"hello"`)
  **Clarification**: `<<"hello">>` is a binary (sequence of bytes); `"hello"` is a list of integers `[104,101,108,108,111]`. They are different types with different APIs.

# Source Reference
Data Types chapter, "Bit Strings and Binaries" section and "Type Conversions" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
