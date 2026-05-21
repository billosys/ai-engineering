---
concept: Bit Syntax
slug: bit-syntax
category: data-types
subcategory: binaries
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Bit Syntax"
extraction_confidence: high
aliases:
  - "binary syntax"
  - "binary segments"
  - "type specifier list"
prerequisites:
  - number-erlang
  - pattern-matching
extends: []
related:
  - bitwise-operations
  - binary-string
  - binary-comprehension
contrasts_with: []
answers_questions:
  - "What is the bit syntax?"
---

# Bit Syntax

## Quick Definition

Erlang's bit syntax encloses binary data between `<<` and `>>` and splits it into readable segments. It makes constructing and pattern matching raw binary data easy.

## Core Definition

Bit syntax encloses binary data between `<<` and `>>` and splits it into segments separated by commas; each segment is a sequence of bits (not necessarily byte-aligned). A segment can take any of the forms `Value`, `Value:Size`, `Value/TypeSpecifierList`, or `Value:Size/TypeSpecifierList`. `Size` is in bits when no type list is given. The `TypeSpecifierList` (hyphen-separated) selects the *Type* (`integer`, `float`, `binary`, `bytes`, `bitstring`, `bits`, `utf8`, `utf16`, `utf32`; default `integer`), *Signedness* (`signed`/`unsigned`, default `unsigned`), *Endianness* (`big`/`little`/`native`, default `big`), and *Unit* (`unit:Integer`). The `Rest/binary` notation captures whatever remains, mirroring `[Head|Tail]` for lists (Hébert, ch. 1, "Bit Syntax").

## Prerequisites

- **Numbers in Erlang** — Binary segments hold integers and use base notation
- **Pattern matching** — Binaries are unpacked via pattern matching

## Key Properties

1. Binary literals are enclosed in `<<` and `>>`.
2. A segment may be `Value`, `Value:Size`, `Value/TypeSpecifierList`, or `Value:Size/TypeSpecifierList`.
3. `Size` is measured in bits when no type list is present.
4. Type specifiers cover type, signedness, endianness, and unit.
5. `Size * Unit` gives total bits, which must be divisible by 8.
6. `Rest/binary` captures the remainder of a binary, analogous to a list tail.
7. Pattern matching against a binary fails unless the segment sizes account for all the data.

## Construction / Recognition

To store a value in a binary segment:

1. Write `Value:Size` to specify bit width.
2. Optionally append `/TypeSpecifierList` for type, signedness, endianness, or unit.

## Context & Application

Bit syntax makes parsing and constructing protocol data (TCP segments, image headers, video encoding) clean and readable, which was a key requirement for Erlang's telecom origins. Endianness matters for integers, floats, and utf16/utf32.

## Examples

**Example** (ch. 1): `Color = 16#F09A29.` then `Pixel = <<Color:24>>.` produces `<<240,154,41>>`.

**Example** (ch. 1): `<<Pix1:24, Pix2:24, Pix3:24, Pix4:24>> = Pixels.` unpacks four 24-bit pixels.

**Example** (ch. 1): `<<25:4/unit:8>>` encodes 25 as a 4-byte integer `<<0,0,0,25>>`.

## Relationships

### Prerequisites

- **Numbers in Erlang** — Segments store integers
- **Pattern matching** — Binaries are decomposed by matching

### Related

- **Bitwise operations** — Operate on the integers held in binaries
- **Binary string** — A binary used to store text
- **Binary comprehension** — Comprehensions over binaries built with bit syntax

## Common Errors

- **Error**: Matching `<<Pix1,Pix2,Pix3,Pix4>>` against 12 bytes of data
  **Correction**: Specify segment sizes (e.g., `Pix1:24`) so they account for all bits

## Common Confusions

- **Confusion**: Assuming `Size` is in bytes
  **Clarification**: `Size` is in bits unless a type/unit changes the unit size

## Source Reference

Chapter 1: "Starting Out," section "Bit Syntax."

## Verification Notes

- Definition: Adapted from the "Bit Syntax" section and type-specifier list
- Confidence: HIGH — explicit, detailed section
- Uncertainties: None
