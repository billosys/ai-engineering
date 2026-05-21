---
# === CORE IDENTIFICATION ===
concept: Erlang Term
slug: erlang-term

# === CLASSIFICATION ===
category: data-types
subcategory: data-types-overview
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2 Data types in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - term
  - data value

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - number
  - binary
  - atom
  - tuple
  - list
  - string
  - pid
  - fun
  - comparing-terms
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
  - "What are Erlang's built-in data types?"
---

# Quick Definition

A term is any piece of data in Erlang. Erlang's built-in data types are numbers, binaries/bitstrings, atoms, tuples, lists (including strings), unique identifiers (pids, ports, references), and funs.

# Core Definition

"Data in Erlang is usually referred to as *terms*" (Chapter 2, section 2.2). Erlang's built-in data types are described as "straightforward and relatively few, but you can achieve a lot with them." The book lists them as: numbers (integers and floats), binaries/bitstrings, atoms, tuples, lists (and strings), unique identifiers (pids, ports, references), and funs. A defining property shared by all terms is that they can all be compared and ordered with the same comparison operators (section 2.2.9).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A term is any data value in Erlang.
2. The built-in types are: numbers, binaries/bitstrings, atoms, tuples, lists (and strings), identifiers (pids/ports/references), and funs.
3. The set of built-in types is small but expressive.
4. Any two terms can be compared and ordered with the same operators.

# Construction / Recognition

## To Identify/Recognize:
1. Any literal or value you can enter in the shell is a term.
2. Compound terms (tuples, lists) are built from other terms.
3. All terms share a single total ordering.

# Context & Application

- **Typical contexts**: All Erlang data — messages, function arguments, return values.
- **Common applications**: Building compound data structures from primitive terms.
- **Historical/stylistic notes**: The standard library provides higher-level abstract data types (arrays, sets, dictionaries) built from tuples and lists under the hood.

# Examples

**Example 1** (section 2.2): The book invites the reader to enter examples of terms in the shell while reading — numbers, atoms, tuples, lists, and so on.

**Example 2** (section 2.2.9): `lists:sort([b,3,a,"z",1,c,"x",2.5,"y"])` sorts a list of mixed terms of different types into a single well-defined order.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **Number**, **binary**, **atom**, **tuple**, **list**, **string**, **pid**, **fun** — the specific term types.

## Related
- **Comparing terms** — all terms share a total ordering.

## Contrasts With
- None — this is the umbrella concept for all data types.

# Common Errors

- **Error**: Expecting a large catalogue of primitive types as in some other languages.
  **Correction**: Erlang's built-in types are few; compound data is built from them.

# Common Confusions

- **Confusion**: Thinking strings are a distinct primitive type.
  **Clarification**: Strings are lists of character codes — a use of the list type, not a separate type.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2 "Data types in Erlang."

# Verification Notes

- Definition source: Direct adaptation from section 2.2.
- Confidence rationale: HIGH — the term concept and the list of built-in types are explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
