---
concept: Bitwise Operations
slug: bitwise-operations
category: core-idioms
subcategory: operators
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Bitwise Binary Operations"
extraction_confidence: high
aliases:
  - "bitwise binary operations"
  - "bit shift"
  - "bsl"
  - "bsr"
prerequisites:
  - number-erlang
extends: []
related:
  - bit-syntax
contrasts_with: []
answers_questions:
  - "What are the basic data types in Erlang?"
---

# Bitwise Operations

## Quick Definition

Erlang provides standard bitwise operators for shifting and combining the bits of integers: `bsl`, `bsr`, `band`, `bor`, `bxor`, and `bnot`.

## Core Definition

The standard binary operations — shifting bits left and right, and binary `and`, `or`, `xor`, and `not` — exist in Erlang as the operators `bsl` (bit shift left), `bsr` (bit shift right), `band`, `bor`, `bxor`, and `bnot`. Combined with bit syntax, these make parsing and pattern matching binary data straightforward (Hébert, ch. 1, "Bitwise Binary Operations").

## Prerequisites

- **Numbers in Erlang** — Bitwise operators act on integers, often written in base-2 notation

## Key Properties

1. `bsl` shifts bits left; `bsr` shifts bits right.
2. `band`, `bor`, `bxor` are bitwise and, or, xor.
3. `bnot` is bitwise not.
4. Operands are integers, commonly written in base notation like `2#00100`.

## Construction / Recognition

To shift or combine bits, place the operator between two integer operands: `2#00010 bsl 1`.

## Context & Application

Bitwise operations together with bit syntax make low-level binary parsing — protocol implementations, image and video formats — concise in Erlang.

## Examples

**Example** (ch. 1): `2#00010 bsl 1.` equals `2#00100`.

**Example** (ch. 1): `2#10001 bor 2#00101.` equals `2#10101`.

## Relationships

### Prerequisites

- **Numbers in Erlang** — Bitwise operators work on integers

### Related

- **Bit syntax** — Bitwise operations complement bit syntax for binary parsing

## Common Errors

- **Error**: Using the Boolean operators `and`/`or` to combine integer bits
  **Correction**: Use `band`/`bor` for bitwise combination of integers

## Common Confusions

- **Confusion**: Confusing `bsl`/`bsr` with arithmetic operators
  **Clarification**: They shift bit patterns, not perform multiplication or division semantically

## Source Reference

Chapter 1: "Starting Out," section "Bitwise Binary Operations."

## Verification Notes

- Definition: Adapted from the brief "Bitwise Binary Operations" section
- Confidence: HIGH — explicit section, short but clear
- Uncertainties: None
