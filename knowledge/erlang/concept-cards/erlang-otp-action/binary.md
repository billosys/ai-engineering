---
# === CORE IDENTIFICATION ===
concept: Binary
slug: binary

# === CLASSIFICATION ===
category: data-types
subcategory: binaries
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.2 Binaries and bitstrings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bitstring
  - binary data

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - number
  - string
  - list
contrasts_with:
  - list

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary in Erlang?"
  - "What is the difference between a binary and a bitstring?"
  - "How do you write a binary literal?"
---

# Quick Definition

A binary is a sequence of unsigned 8-bit bytes for storing and processing chunks of data. A bitstring is a generalized binary whose bit length need not be a multiple of 8.

# Core Definition

"A *binary* is a sequence of unsigned 8-bit bytes, used for storing and processing chunks of data (often data that comes from a file or has been received over a network protocol)" (Chapter 2, section 2.2.2). "A *bitstring* is a generalized binary whose length in bits isn't necessarily a multiple of 8; it can, for instance, be 12 bits long, consisting of one and a half bytes." Whole-byte binaries are long-standing; arbitrary bitstrings are a more recent addition. The basic syntax is a comma-separated list of integers 0–255 enclosed in `<<` ... `>>`, with no space between the delimiter characters; `<<>>` is an empty binary. Strings may also be used to build a binary, as in `<<"hello", 32, "dude">>`, equivalent to the 8-bit character codes — useful for text-based protocols.

# Prerequisites

- **Erlang term** — a binary is one kind of term.

# Key Properties

1. A binary is a sequence of unsigned 8-bit bytes.
2. A bitstring is a generalized binary; its bit length need not be a multiple of 8.
3. Binary syntax is `<< ... >>` with no space between the delimiter characters.
4. A binary literal is a comma-separated list of integers in the range 0–255.
5. `<<>>` is the empty binary.
6. Strings can appear inside binary syntax, expanding to 8-bit character codes.

# Construction / Recognition

## To Construct/Create:
1. Write integers 0–255 separated by commas inside `<< >>`, e.g. `<<0, 1, 2, 255>>`.
2. Or include strings: `<<"hello", 32, "dude">>`.
3. For non-byte-aligned data, use the more advanced bitstring construction syntax.

# Context & Application

- **Typical contexts**: Storing and processing chunks of data from files or network protocols.
- **Common applications**: Binary protocols, text-based protocols, large constant string storage.
- **Historical/stylistic notes**: Because the name *binary* is so ingrained, people rarely say *bitstring* unless emphasizing non-byte-aligned length. Binaries are recommended for long-term storage of large constant string data, in preference to lists.

# Examples

**Example 1** (section 2.2.2): `<<0, 1, 2, ..., 255>>` — a comma-separated list of integers 0–255 enclosed in `<<` ... `>>`.

**Example 2** (section 2.2.2): `<<"hello", 32, "dude">>` builds a binary from strings plus the byte value 32, equivalent to the sequence of 8-bit character codes.

# Relationships

## Builds Upon
- **Erlang term** — a binary is a term.

## Enables
- Efficient storage and processing of byte-oriented data.

## Related
- **String** — strings can be embedded in binary syntax; binaries store large string data efficiently.
- **List** — lists are good for temporary data, binaries for long-term constant string storage.

## Contrasts With
- **List** — a list of integers is a chain of cons cells; a binary is a contiguous byte sequence, more compact for large data.

# Common Errors

- **Error**: Putting a space between the delimiter characters, as in `< < ... > >`.
  **Correction**: There must be no space — write `<<` and `>>`.

- **Error**: Putting integers outside 0–255 in a byte-binary literal.
  **Correction**: A proper (whole-byte) binary literal uses integers in the range 0–255.

# Common Confusions

- **Confusion**: Believing binaries and bitstrings are different data types.
  **Clarification**: A bitstring is just a binary whose bit length is not a multiple of 8; the syntax and name are shared.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.2 "Binaries and bitstrings."

# Verification Notes

- Definition source: Direct adaptation from section 2.2.2.
- Confidence rationale: HIGH — binaries and bitstrings are explicitly defined.
- Uncertainties: The advanced bit-syntax for matching/constructing is deferred by the book to section 2.10 (outside this card's scope).
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
