---
# === CORE IDENTIFICATION ===
concept: Binary
slug: binary

# === CLASSIFICATION ===
category: data-types
subcategory: binary-data
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Binaries and the Bit Syntax"
chapter_number: 7
pdf_page: null
section: "Binaries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "<<>>"
  - binary data structure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
related:
  - bit-syntax
  - bitstring
  - binary-bifs
  - iolist
contrasts_with:
  - bitstring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary?"
  - "How are binaries written and printed?"
  - "When should I use a binary?"
---

# Quick Definition

A binary is a data structure for storing large quantities of raw data space-efficiently. It is written and printed as a sequence of integers or strings inside `<<` and `>>` brackets.

# Core Definition

A binary is a data structure designed for storing large quantities of raw data in a space-efficient manner. The Erlang VM is optimized for the efficient input, output, and message passing of binaries. Binaries should be used whenever possible for storing the contents of large quantities of unstructured data, such as large strings or the contents of files. Binaries are written and printed as sequences of integers or strings, enclosed in double less-than and greater-than brackets (`<<` and `>>`). In most circumstances the number of bits in a binary is exactly divisible by 8 and so corresponds to a sequence of bytes; when integers are used in a binary, each must be in the range 0 to 255. If the content is a printable string, the shell prints the binary as a string; otherwise it prints it as a sequence of integers ("Binaries and the Bit Syntax," chapter introduction; *Binaries*).

# Prerequisites

- **Pattern matching** — Binaries are constructed and taken apart using pattern matching (and the bit syntax).

# Key Properties

1. Written with `<<` ... `>>` brackets.
2. Stores raw, unstructured data space-efficiently.
3. Integer elements must be in the range 0..255 (one byte each).
4. The number of bits is normally exactly divisible by 8 (a whole number of bytes).
5. Printable-string content is shown by the shell as a string; otherwise as integers.
6. The Erlang VM is optimized for binary input, output, and message passing.
7. `<<"cat">>` is shorthand for `<<99,97,116>>` — the ASCII codes of the characters.

# Construction / Recognition

## To Construct/Create:
1. Write a literal such as `<<5,10,20>>` or `<<"hello">>`.
2. Or build one with a BIF such as `list_to_binary/1` or `term_to_binary/1`, or with the bit syntax.

## To Identify/Recognize:
1. Use the guard test `is_binary(B)`.
2. `byte_size(B)` returns the number of bytes; a binary's bit count is divisible by 8.

# Context & Application

- **Typical contexts**: Storing large strings, file contents, or protocol packets.
- **Common applications**: `file:read_file/1` reads an entire file into a binary; `term_to_binary` serializes a term for storage or network transfer.
- **Historical/stylistic notes**: Binaries, bitstrings, and bit-level pattern matching were introduced to simplify network programming.

# Examples

**Example 1** (*Binaries*): Binary literals printed by the shell.

```erlang
<<5,10,20>>.
%% => <<5,10,20>>
<<"hello">>.
%% => <<"hello">>
<<65,66,67>>.
%% => <<"ABC">>
```

**Example 2** (*Working with Binaries*): Constructing a binary by flattening an iolist.

```erlang
Bin1 = <<1,2,3>>.
list_to_binary([Bin1,1,[2,3,<<4,5>>],4|<<6>>]).
%% => <<1,2,3,1,2,3,4,5,4,6>>
```

# Relationships

## Builds Upon
- **Pattern matching** — Binaries are unpacked by matching.

## Enables
- **Bit syntax** — The notation for constructing and matching binaries.
- **Binary BIFs** — `list_to_binary`, `term_to_binary`, etc., operate on binaries.

## Related
- **iolist** — A nested list of integers, binaries, and iolists that `list_to_binary` flattens.

## Contrasts With
- **Bitstring** — A bitstring's bit count is *not* a multiple of 8; a binary's is.

# Common Errors

- **Error**: Placing an integer outside 0..255 in a binary.
  **Correction**: Each integer element of a binary occupies one byte and must be 0..255.

- **Error**: Omitting spaces around `=` when assigning a binary literal, e.g. `Bin1=<<1,2,3>>`.
  **Correction**: Without the space the tokenizer reads `=<` (the equal-to-or-less-than operator); write `Bin1 = <<1,2,3>>`.

# Common Confusions

- **Confusion**: Thinking every binary is exactly a sequence of bytes.
  **Clarification**: A binary's bit count is a multiple of 8; when it is not, the data is a bitstring.

- **Confusion**: Believing the shell's string display means the binary "is" a string.
  **Clarification**: The shell prints printable content as a string for convenience; the underlying data is raw bytes.

# Source Reference

Chapter 7: Binaries and the Bit Syntax, chapter introduction and section "Binaries" (including "Working with Binaries"). EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and the "Binaries" section.
- Confidence rationale: HIGH — the source explicitly defines binaries and their representation.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
