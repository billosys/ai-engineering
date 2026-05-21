---
# === CORE IDENTIFICATION ===
concept: Terms
slug: terms

# === CLASSIFICATION ===
category: data-types
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Terms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "term"
  - "literal value"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - expression-evaluation
  - variables
  - patterns-in-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
  - "What is the simplest form of expression in Erlang?"
  - "What types of values exist in Erlang?"
---

# Quick Definition

A term is the simplest form of expression in Erlang: an integer, float, atom, string, list, map, or tuple. The return value of a term expression is the term itself.

# Core Definition

The Erlang Reference Manual defines: "The simplest form of expression is a term, that is, one of `integer`, `float`, `atom`, `string`, `list`, `map`, or `tuple`. The return value is the term itself." (Erlang Reference Manual, "Expressions", "Terms").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Terms are the simplest form of expression
2. The seven term types are: integer, float, atom, string, list, map, and tuple
3. A term evaluates to itself (self-evaluating)
4. Terms are the building blocks of all Erlang data
5. Patterns have the same structure as terms but can contain unbound variables

# Construction / Recognition

## To Construct/Create:
1. Integers: `42`, `-7`, `16#FF`
2. Floats: `3.14`, `-0.5`
3. Atoms: `hello`, `'with spaces'`
4. Strings: `"hello"` (which are actually lists of character codes)
5. Lists: `[1, 2, 3]`, `[H|T]`
6. Maps: `#{key => value}`
7. Tuples: `{ok, Value}`

## To Identify/Recognize:
1. Any literal value that evaluates to itself is a term
2. Terms appear as leaf nodes in expression trees

# Context & Application

Terms are fundamental to Erlang -- they are the values that all expressions evaluate to, the data that pattern matching operates on, and the messages that processes send to each other. The word "term" is used throughout the Erlang documentation to mean "any Erlang value."

# Examples

**Example 1** (Terms section): The seven term types enumerated: "one of `integer`, `float`, `atom`, `string`, `list`, `map`, or `tuple`."

**Example 2** (Terms section): "The return value is the term itself." -- meaning `42` evaluates to `42`, `{ok, done}` evaluates to `{ok, done}`.

# Relationships

## Enables
- **patterns-in-expressions** -- Patterns have the same structure as terms
- **variables** -- Variables evaluate to terms when bound
- **expression-evaluation** -- Terms are the base case of expression evaluation

## Related
- **pattern-matching** -- Terms are the right-hand side of pattern matching

# Common Errors

- **Error**: Confusing a string with an atom
  **Correction**: Strings are enclosed in double quotes and are lists of character codes; atoms are enclosed in single quotes (when quoting is needed) and are named constants

# Common Confusions

- **Confusion**: Thinking "term" refers to a specific data type
  **Clarification**: "Term" is a collective noun for any Erlang value -- it encompasses all seven listed types

# Source Reference

"Expressions" chapter, section "Terms."

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: HIGH -- explicit definition listing all term types
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
