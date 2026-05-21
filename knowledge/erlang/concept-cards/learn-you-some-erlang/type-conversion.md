---
concept: Type Conversion
slug: type-conversion
category: data-types
subcategory: type-system
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Types (or Lack Thereof)"
chapter_number: 4
pdf_page: null
section: "Type Conversions"
extraction_confidence: high
aliases:
  - "casting"
  - "conversion BIF"
prerequisites:
  - strong-typing
extends: []
related:
  - type-test-bif
  - number-erlang
contrasts_with: []
answers_questions:
  - "What distinguishes dynamic typing from static typing?"
---

# Type Conversion

## Quick Definition

Type conversion in Erlang is done explicitly with BIFs named `TypeA_to_TypeB`, defined in the `erlang` module — for example, `list_to_integer/1` or `atom_to_list/1`.

## Core Definition

Erlang changes the type of a term by casting it into another with the help of BIFs, since many conversions could not be implemented in Erlang itself. Each conversion function takes the form `TypeA_to_TypeB` and is implemented in the `erlang` module (e.g., `list_to_integer/1`, `integer_to_list/1`, `list_to_binary/1`). This `Type_to_Type` scheme is a language wart: every time a new type is added, a whole set of conversion BIFs must be added too. The BIF `binary_to_term/2` with the `[safe]` option avoids decoding unknown atoms or anonymous functions, which could exhaust memory or be a security risk (Hébert, ch. 4, "Type Conversions").

## Prerequisites

- **Strong typing** — Explicit conversion exists because Erlang never coerces implicitly

## Key Properties

1. Conversion BIFs are named `TypeA_to_TypeB` and live in the `erlang` module.
2. Examples: `list_to_integer/1`, `integer_to_list/1`, `atom_to_list/1`, `list_to_binary/1`.
3. The scheme requires a new BIF for each pair of types — a language wart.
4. An invalid conversion (e.g., `list_to_integer("54.32")`) raises a bad argument error.
5. `binary_to_term/2` with `[safe]` blocks decoding unknown atoms / funs for safety.

## Construction / Recognition

To convert a term: call the BIF named `sourcetype_to_targettype`, e.g., `erlang:list_to_integer("54")`.

## Context & Application

Conversion BIFs are needed because strong typing forbids implicit coercion. They are used, for example, to turn strings into binary strings for storage or integers into floats.

## Examples

**Example** (ch. 4): `erlang:list_to_integer("54").` returns `54`; `erlang:integer_to_list(54).` returns `"54"`.

**Example** (ch. 4): `erlang:list_to_integer("54.32").` raises a bad argument error because the string is not an integer.

## Relationships

### Prerequisites

- **Strong typing** — No implicit coercion, so conversions are explicit

### Related

- **Type-test BIF** — Tests a term's type; conversion BIFs change it
- **Numbers in Erlang** — Conversions handle integer/float/list forms of numbers

## Common Errors

- **Error**: Passing a malformed string to a conversion BIF (e.g., `"54.32"` to `list_to_integer`)
  **Correction**: Use the correct BIF for the data (`list_to_float` for decimals)

## Common Confusions

- **Confusion**: Expecting automatic casting between types
  **Clarification**: Erlang never auto-casts; you must call the explicit conversion BIF

## Source Reference

Chapter 4: "Types (or Lack Thereof)," section "Type Conversions."

## Verification Notes

- Definition: Adapted from the "Type Conversions" section and BIF table
- Confidence: HIGH — explicit section
- Uncertainties: None
