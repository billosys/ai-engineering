---
# === CORE IDENTIFICATION ===
concept: Tuple
slug: tuple

# === CLASSIFICATION ===
category: data-types
subcategory: tuples
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.4 Tuples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - n-tuple
  - triple

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - tagged-tuple
  - list
  - pattern-matching
contrasts_with:
  - list

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tuple in Erlang?"
  - "How do you write a tuple?"
  - "When should you use a tuple instead of a list?"
---

# Quick Definition

A tuple is a fixed-length, ordered sequence of Erlang terms, written within curly braces. It is the main way to build compound data or return multiple values.

# Core Definition

"A *tuple* (or *n*-tuple, as generalized from triple, quadruple, and so on) is a fixed-length ordered sequence of other Erlang terms. Tuples are written within curly braces" (Chapter 2, section 2.2.4). A tuple can contain zero (`{}`), one (`{here}`), or more elements; elements may be of the same or wildly different types and may themselves be tuples or any other data. Tuples are "the main way of constructing compound data structures or returning multiple values in Erlang, like structs in C or objects in Java; but the entries aren't named, they're numbered (from 1 to N)." Accessing a tuple element is a constant-time operation. Tuples are meant for constant-length sequences; for varying-length sequences, lists are used.

# Prerequisites

- **Erlang term** — a tuple is a term, and contains terms.

# Key Properties

1. A tuple is a fixed-length, ordered sequence of terms.
2. It is written within curly braces: `{1, 2, 3}`.
3. It may have zero, one, or many elements, of any types.
4. Elements may be nested tuples or any other data.
5. Entries are numbered 1 to N, not named.
6. Accessing an element is a constant-time operation.
7. Tuples are for constant-length sequences; lists are for varying length.

# Construction / Recognition

## To Construct/Create:
1. Write the elements separated by commas inside curly braces.
2. Use the empty tuple `{}` or single-element `{here}` as needed.
3. Nest tuples freely for compound structures.

# Context & Application

- **Typical contexts**: Compound data structures, multiple return values.
- **Common applications**: Records (record syntax names tuple entries); standard-library abstract data types (arrays, sets, dictionaries) are mostly implemented with tuples.
- **Historical/stylistic notes**: Pattern matching makes it rare to access a tuple element directly by index.

# Examples

**Example 1** (section 2.2.4): `{1, 2, 3}`, `{one, two, three, four}`, `{from, "Russia", "with love"}`, `{complex, {nested, "structure", {here}}}`, and `{}` are all valid tuples.

**Example 2** (section 2.2.4): The book notes a standard convention of labelling tuples with an atom first element, as in `{size, 42}` or `{position, 5, 2}` — these are *tagged tuples*.

# Relationships

## Builds Upon
- **Erlang term** — a tuple holds terms and is itself a term.

## Enables
- **Tagged tuple** — a tuple with an atom tag as its first element.

## Related
- **Pattern matching** — makes it easy to refer to a tuple's parts by variable.

## Contrasts With
- **List** — tuples are fixed-length with constant-time element access; lists are variable-length chains of cons cells.

# Common Errors

- **Error**: Using a tuple to hold a varying number of items.
  **Correction**: Tuples are fixed-length; use a list for varying-length sequences.

# Common Confusions

- **Confusion**: Expecting tuple entries to have names.
  **Clarification**: Tuple entries are numbered 1 to N; the record syntax adds names on top of tuples.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.4 "Tuples."

# Verification Notes

- Definition source: Direct adaptation from section 2.2.4.
- Confidence rationale: HIGH — tuples are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `tagged-tuple` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
