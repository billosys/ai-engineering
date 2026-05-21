---
# === CORE IDENTIFICATION ===
concept: Binary BIFs
slug: binary-bifs

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
section: "Working with Binaries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "term_to_binary"
  - "binary_to_term"
  - "list_to_binary"
  - binary module functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
extends: []
related:
  - iolist
  - bit-syntax
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build and take apart binaries with BIFs?"
  - "How do I serialize an Erlang term to a binary?"
  - "What does list_to_binary do?"
---

# Quick Definition

Binary BIFs are built-in functions for building, splitting, sizing, and serializing binaries — including `list_to_binary`, `split_binary`, `term_to_binary`, `binary_to_term`, and `byte_size`.

# Core Definition

Binaries can be manipulated using BIFs and functions from the `binary` module, many of which are implemented as native code ("Binaries and the Bit Syntax", *Working with Binaries*). The most important ones are: `list_to_binary(L) -> B`, which returns a binary built by flattening all elements of the iolist `L`; `split_binary(Bin, Pos) -> {Bin1, Bin2}`, which splits a binary into two parts at `Pos`; `term_to_binary(Term) -> Bin`, which converts any Erlang term into a binary in the "external term format"; `binary_to_term(Bin) -> Term`, the inverse of `term_to_binary`; and `byte_size(Bin) -> Size`, which returns the number of bytes in the binary. The book calls `term_to_binary` and `binary_to_term` "incredibly useful" — a term converted to a binary can be sent over a socket or stored in a file and reconstructed later.

# Prerequisites

- **Binary** — These BIFs operate on or produce binaries.

# Key Properties

1. `list_to_binary/1` flattens an iolist (integers 0..255, binaries, nested iolists) into one binary.
2. `split_binary/2` splits a binary into a two-element tuple at a byte position.
3. `term_to_binary/1` serializes any term to the Erlang external term format.
4. `binary_to_term/1` reconstructs the original term from such a binary.
5. `byte_size/1` returns the byte count of a binary.
6. `term_to_binary`/`binary_to_term` correctly handle integer/float endianness across machines.
7. Many `binary`-module functions are implemented in native code for speed.

# Construction / Recognition

## To Construct/Create:
1. Flatten an iolist: `list_to_binary([Bin1,1,[2,3,Bin2],4|Bin3])`.
2. Serialize a term: `term_to_binary({binaries,"are",useful})`.

## To Identify/Recognize:
1. `byte_size(Bin)` reports the byte count.
2. `binary_to_term(B)` recovers a term previously produced by `term_to_binary`.

# Context & Application

- **Typical contexts**: serializing data for files and network messages; assembling output buffers from iolists.
- **Common applications**: `term_to_binary`/`binary_to_term` underpin distributed Erlang and are used internally in many databases.
- **Historical/stylistic notes**: a binary literal assignment needs spaces around `=` — without them the tokenizer reads `=<` (the equal-or-less-than operator).

# Examples

**Example 1** (*Working with Binaries*): flattening an iolist:

```erlang
1> Bin1 = <<1,2,3>>.
4> list_to_binary([Bin1,1,[2,3,<<4,5>>],4|<<6>>]).
<<1,2,3,1,2,3,4,5,4,6>>
```

**Example 2** (*Working with Binaries*): round-tripping a term:

```erlang
1> B = term_to_binary({binaries,"are", useful}).
2> binary_to_term(B).
{binaries,"are",useful}
```

**Example 3** (*Working with Binaries*): `split_binary(<<1,2,3,4,5,6,7,8,9,10>>, 3)` returns `{<<1,2,3>>,<<4,5,6,7,8,9,10>>}`.

# Relationships

## Builds Upon
- This is a utility concept depending on binaries.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **iolist** — `list_to_binary` flattens an iolist into a binary.
- **Bit syntax** — An alternative, lower-level way to build and match binaries.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Passing a list with integers outside 0..255 to `list_to_binary`.
  **Correction**: An iolist's integer elements must be in the range 0..255 (one byte each).

- **Error**: Writing `Bin = <<1,2,3>>` without the space before `<<`.
  **Correction**: Omitting the space makes the tokenizer read `=<`; always put a space before a binary literal after `=`.

# Common Confusions

- **Confusion**: Thinking the binary produced by `term_to_binary` is human-readable.
  **Clarification**: It is the Erlang external term format — opaque bytes meant to be reconstructed by `binary_to_term`.

- **Confusion**: Believing endianness corrupts integers serialized across machines.
  **Clarification**: `term_to_binary`/`binary_to_term` "do the right thing" — integers survive transfer between big- and little-endian machines.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", section "Working with Binaries".

# Verification Notes

- Definition source: Direct adaptation of the BIF descriptions in *Working with Binaries*.
- Confidence rationale: HIGH — the source defines each BIF explicitly with worked shell examples.
- Uncertainties: None.
- Cross-reference status: Slug `binary` exists; `iolist`, `bit-syntax` extracted/related in scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
