---
# === CORE IDENTIFICATION ===
concept: Iolist
slug: iolist

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - io list
  - I/O list

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binary
extends: []
related:
  - binary-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an iolist?"
  - "What can list_to_binary take as input?"
---

# Quick Definition

An iolist is a recursively defined list whose elements are integers in 0..255, binaries, or other iolists; `list_to_binary` flattens an iolist into a single binary.

# Core Definition

The book defines an iolist while describing `list_to_binary`: "`list_to_binary` returns a binary constructed by flattening (*flattening* means removing all the list parentheses) all the elements in the *iolist* `L`. An *iolist* is defined recursively as a list whose elements are integers in `0..255`, binaries, or iolists" ("Binaries and the Bit Syntax", *Working with Binaries*). The recursive definition means an iolist may nest arbitrarily — a list containing binaries, byte-valued integers, and further iolists in any arrangement.

# Prerequisites

- **Binary** — Iolists are used to build binaries and may themselves contain binaries.

# Key Properties

1. Defined recursively: each element is an integer in 0..255, a binary, or an iolist.
2. May be arbitrarily nested.
3. "Flattening" an iolist removes all the list parentheses, yielding a flat byte sequence.
4. The standard way to feed an iolist into a binary is `list_to_binary/1`.

# Construction / Recognition

## To Construct/Create:
1. Build a nested list of byte integers and binaries, e.g. `[Bin1,1,[2,3,Bin2],4|Bin3]`.

## To Identify/Recognize:
1. A list that contains only byte-valued integers, binaries, and nested such lists is an iolist.

# Context & Application

- **Typical contexts**: assembling output buffers (e.g. for I/O) without repeatedly concatenating binaries.
- **Common applications**: passing an iolist to `list_to_binary` to produce one binary in a single step.
- **Historical/stylistic notes**: the name reflects its use for I/O — output functions accept iolists directly.

# Examples

**Example 1** (*Working with Binaries*): flattening a nested iolist into a binary:

```erlang
1> Bin1 = <<1,2,3>>.
2> Bin2 = <<4,5>>.
3> Bin3 = <<6>>.
4> list_to_binary([Bin1,1,[2,3,Bin2],4|Bin3]).
<<1,2,3,1,2,3,4,5,4,6>>
```

The nested list — containing binaries, integers, and a sublist — is flattened into a single binary.

# Relationships

## Builds Upon
- This is a small data-shape concept depending on binaries.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Binary BIFs** — `list_to_binary/1` is the BIF that flattens an iolist.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Putting an integer outside 0..255 into an iolist.
  **Correction**: Iolist integer elements must be byte values (0..255); larger integers belong in a bit syntax segment instead.

# Common Confusions

- **Confusion**: Thinking an iolist is just a flat list of bytes.
  **Clarification**: An iolist may nest arbitrarily — it can contain binaries and other iolists, not only integers.

# Source Reference

Chapter 7: "Binaries and the Bit Syntax", section "Working with Binaries" (the `list_to_binary` description).

# Verification Notes

- Definition source: Direct quotation of the recursive iolist definition in *Working with Binaries*.
- Confidence rationale: MEDIUM — the source defines iolists precisely but only in passing, within the `list_to_binary` description, with a single example.
- Uncertainties: The source does not discuss iolist use in I/O functions beyond the name.
- Cross-reference status: Slug `binary` exists; `binary-bifs` extracted in scope.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
