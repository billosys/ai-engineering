---
concept: Binary Comprehension
slug: binary-comprehension
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Binary Comprehensions"
extraction_confidence: high
aliases:
  - "binary generator"
prerequisites:
  - bit-syntax
  - list-comprehension
extends:
  - list-comprehension
related: []
contrasts_with:
  - list-comprehension
answers_questions:
  - "How does a list comprehension relate to a binary comprehension?"
  - "What distinguishes a list comprehension from a binary comprehension?"
---

# Binary Comprehension

## Quick Definition

A binary comprehension is to bit syntax what a list comprehension is to lists: a concise way to build or transform binaries. It uses `<=` for binary generators and `<<>>` brackets.

## Core Definition

Binary comprehensions are to bit syntax what list comprehensions are to lists — a way to make code short and concise when dealing with binaries. They are used the same way as list comprehensions, with two syntactic changes: the generator arrow `<-` becomes `<=` for binary generators, and binaries (`<<>>`) are used instead of lists (`[]`). By default Erlang assumes binary values are unsigned 8-bit integers, so a binary generator that produces binaries must have its element type declared explicitly (Hébert, ch. 1, "Binary Comprehensions").

## Prerequisites

- **Bit syntax** — Binary comprehensions build and consume binary data
- **List comprehension** — Binary comprehensions reuse the comprehension structure

## Key Properties

1. `<=` is the binary generator arrow (vs. `<-` for lists).
2. Results and generators use `<<>>` instead of `[]`.
3. Generators and conditions work as in list comprehensions.
4. A list generator may feed a binary result and vice versa.
5. Erlang assumes unsigned 8-bit integers by default; binary-valued elements need an explicit type (e.g., `Bin/binary`).

## Construction / Recognition

To build a binary comprehension:

1. Write the result expression between `<<` and `>>`.
2. Use `<<Pattern>> <= <<Binary>>` for binary generators (or `Pattern <- List`).
3. Declare an explicit type if generator elements are themselves binaries.

## Context & Application

Binary comprehensions provide a cleaner alternative to repetitive binary pattern matching — for example, extracting RGB tuples from many pixels in a single line.

## Examples

**Example** (ch. 1): `<< <<X>> || <<X>> <= <<1,2,3,4,5>>, X rem 2 == 0>>.` returns `<<2,4>>`.

**Example** (ch. 1): `[ {R,G,B} || <<R:8,G:8,B:8>> <= Pixels ]` converts a pixel binary into a list of RGB tuples.

**Example** (ch. 1): `<< <<Bin/binary>> || Bin <- [<<3,7,5,4,7>>] >>` works only because `binary` is declared explicitly.

## Relationships

### Prerequisites

- **Bit syntax** — Provides the binary segment notation
- **List comprehension** — Provides the comprehension structure

### Builds Upon

- **List comprehension** — Same idea applied to binaries

### Contrasts With

- **List comprehension** — Uses `<-` and lists; binary comprehensions use `<=` and binaries

## Common Errors

- **Error**: Writing `<<Bin>>` when `Bin` holds a binary
  **Correction**: Declare the type as `<<Bin/binary>>`; the default is an 8-bit integer

## Common Confusions

- **Confusion**: Using `<-` for a binary generator
  **Clarification**: Binary generators use `<=`; `<-` is for list generators

## Source Reference

Chapter 1: "Starting Out," section "Binary Comprehensions."

## Verification Notes

- Definition: Adapted from the "Binary Comprehensions" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
