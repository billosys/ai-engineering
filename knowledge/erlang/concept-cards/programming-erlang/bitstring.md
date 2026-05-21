---
# === CORE IDENTIFICATION ===
concept: Bitstring
slug: bitstring

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
section: "Bitstrings: Processing Bit-Level Data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bit string
  - bit-level data

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
  - bit-syntax
extends:
  - binary
related:
  - binary-comprehension
contrasts_with:
  - binary

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bitstring?"
  - "How does a bitstring differ from a binary?"
  - "Why can't I write a bitstring to a file?"
---

# Quick Definition

A bitstring is a sequence of bits whose total length is not an exact multiple of 8; it is the general form of which a binary (a byte-multiple) is the special case.

# Core Definition

"If the number of bits is not exactly divisible by 8, we use the name *bitstring* to refer to the data. When we say bitstring, it is to emphasize the fact that the number of bits in the data is not an exact multiple of 8" ("Binaries and the Bit Syntax", chapter introduction). Pattern matching on bitstrings works at the bit level, so a sequence of bits can be packed and unpacked in a single operation — useful for data not aligned to 8-bit boundaries or for variable-length data measured in bits. In Erlang "the least addressable unit of storage is a bit," so individual bit sequences within a bitstring can be accessed directly without shifting and masking.

# Prerequisites

- **Binary** — A bitstring is the generalization of a binary; the binary concept comes first.
- **Bit syntax** — Bitstrings are constructed and matched with the bit syntax `<<...>>`.

# Key Properties

1. A bitstring's total bit length is *not* a multiple of 8.
2. A binary is a special case of a bitstring whose bit length *is* a multiple of 8.
3. `is_bitstring(B)` is true for both binaries and bitstrings; `is_binary(B)` is true only for byte-multiple data.
4. `bit_size(B)` gives the length in bits; `byte_size(B)` gives the size of the containing binary.
5. A bitstring cannot be written to a file or socket, since those work in units of bytes.
6. Pattern matching on a bitstring operates at the bit level.

# Construction / Recognition

## To Construct/Create:
1. Use the bit syntax with a non-byte-multiple total: `B2 = <<1:17>>` is a 17-bit bitstring.

## To Identify/Recognize:
1. `is_bitstring(B2)` returns `true` while `is_binary(B2)` returns `false`.
2. `bit_size(B2)` returns `17` for the example above.

# Context & Application

- **Typical contexts**: bit-level protocol data, variable-length fields measured in bits.
- **Common applications**: extracting the individual bits of a byte via a bit comprehension.
- **Historical/stylistic notes**: in most languages the least addressable unit is an 8-bit char; Erlang's least addressable unit is a single bit, which makes bitstring code free of masking and shifting.

# Examples

**Example 1** (*Bitstrings: Processing Bit-Level Data*): a 17-bit bitstring versus an 8-bit binary:

```erlang
1> B1 = <<1:8>>.
<<1>>
3> is_binary(B1).
true
5> B2 = <<1:17>>.
<<0,0,1:1>>
6> is_binary(B2).
false
7> is_bitstring(B2).
true
9> bit_size(B2).
17
```

`B2` prints as `<<0,0,1:1>>` — a binary literal whose third segment is a 1-bit bitstring.

# Relationships

## Builds Upon
- **Binary** — A bitstring generalizes a binary to non-byte-multiple lengths.

## Enables
- **Binary comprehension** — Bit comprehensions iterate over bitstrings and binaries.

## Related
- **Binary comprehension** — Used in the source to extract the bits of a byte into a list or binary.

## Contrasts With
- **Binary** — A binary's bit count is a multiple of 8 and can be written to files/sockets; a bitstring's is not and cannot.

# Common Errors

- **Error**: Trying to write a bitstring to a file or socket.
  **Correction**: Files and sockets work in bytes; only byte-multiple binaries can be written.

- **Error**: Using `is_binary/1` to test for bit-level data.
  **Correction**: Use `is_bitstring/1`; `is_binary/1` is false for non-byte-multiple data.

# Common Confusions

- **Confusion**: Believing bitstrings and binaries are unrelated types.
  **Clarification**: A binary is a bitstring whose length happens to be a multiple of 8; bitstring is the general term.

- **Confusion**: Thinking `byte_size` of a bitstring equals its bit length divided by 8 exactly.
  **Clarification**: `byte_size` returns the size of the *containing* binary (e.g. 3 for a 17-bit bitstring); `bit_size` gives the true bit length.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", chapter introduction and section "Bitstrings: Processing Bit-Level Data" (including the "Bit-Level Storage" sidebar).

# Verification Notes

- Definition source: Direct quotation from the chapter introduction and *Bitstrings: Processing Bit-Level Data*.
- Confidence rationale: HIGH — the source explicitly defines bitstrings and contrasts them with binaries using worked shell examples.
- Uncertainties: None.
- Cross-reference status: Slugs `binary` exists; `bit-syntax`, `binary-comprehension` extracted in scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
