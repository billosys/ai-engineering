---
concept: Binary String
slug: binary-string
category: data-types
subcategory: binaries
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Binary Strings"
extraction_confidence: high
aliases:
  - "binary"
prerequisites:
  - bit-syntax
extends: []
related:
  - binary-comprehension
contrasts_with:
  - list
  - atom
answers_questions:
  - "What are the basic data types in Erlang?"
---

# Binary String

## Quick Definition

A binary string stores text as a tightly packed block of memory, using the syntax `<<"text">>`. It is much more space-efficient than a list-based string.

## Core Definition

Binary strings are bolted onto the language the same way list strings are, but are much more efficient in space: normal lists are like linked lists (one node per letter plus a reference), while binary strings are like C arrays (a tightly packed block of memory). They use the syntax `<<"this is a binary string!">>`. The trade-off is a loss of simplicity in pattern matching and manipulation, so binary strings suit text that won't be manipulated much or when space efficiency matters (Hébert, ch. 1, "Binary Strings").

## Prerequisites

- **Bit syntax** — Binary strings are a special case of binary data written with `<<` and `>>`

## Key Properties

1. Syntax: `<<"text">>`.
2. Stored as a contiguous block of memory, like a C array.
3. Far more space-efficient than list-based strings (no per-letter node).
4. Harder to pattern match and manipulate than lists.
5. Compared in linear time (proportional to length).

## Construction / Recognition

To write a binary string, enclose the text in double quotes between `<<` and `>>`: `<<"hello">>`.

## Context & Application

Binary strings are used for storing text that won't be manipulated heavily, or when space efficiency is a real concern. They should not be used to *tag* values — atoms are better there because atoms compare in constant time regardless of length.

## Examples

**Example** (ch. 1): `<<"this is a binary string!">>` is the binary-string form of a piece of text.

**Example** (ch. 1): The book warns against `{<<"temperature">>,50}` — use the atom `{temperature,50}` instead.

## Relationships

### Prerequisites

- **Bit syntax** — Binary strings are written with binary syntax

### Related

- **Binary comprehension** — Used to process binary data including binary strings

### Contrasts With

- **List** — A list-based string uses one node per character; a binary string is packed memory
- **Atom** — Atoms, not binary strings, should be used to tag values

## Common Errors

- **Error**: Using binary strings as tags for values
  **Correction**: Use atoms for tags; binaries are compared in linear time

## Common Confusions

- **Confusion**: Thinking binary strings are interchangeable with list strings for manipulation
  **Clarification**: They are less convenient to pattern match and manipulate; choose based on need

## Source Reference

Chapter 1: "Starting Out," section "Binary Strings."

## Verification Notes

- Definition: Adapted from the "Binary Strings" section and its note
- Confidence: HIGH — explicit section
- Uncertainties: None
