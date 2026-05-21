---
# === CORE IDENTIFICATION ===
concept: Boolean
slug: boolean

# === CLASSIFICATION ===
category: data-types
subcategory: atomic-data
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Booleans"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "true"
  - "false"
  - boolean literal

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
extends: []
related:
  - boolean-expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a boolean in Erlang?"
  - "Is there a distinct boolean type in Erlang?"
  - "Why should my functions return booleans?"
---

# Quick Definition

Erlang has no distinct boolean type; the atoms `true` and `false` are given special interpretation and used as boolean literals.

# Core Definition

"There is no distinct boolean type in Erlang; instead, the atoms `true` and `false` are given a special interpretation and are used to represent boolean literals" ("The Rest of Sequential Erlang", *Booleans*). When a function returns one of two atomic values, the book recommends making it return a boolean and naming it accordingly — e.g. preferring `is_file_open(File)` returning `true`/`false` over `file_state(File)` returning `open`/`closed`. The reason is library interoperability: "There are a large number of functions in the standard libraries that work on functions that return booleans", so boolean-returning functions compose directly with them.

# Prerequisites

- **Atom** — Booleans are just the atoms `true` and `false`, so the atom concept is required.

# Key Properties

1. There is no separate boolean data type.
2. `true` and `false` are ordinary atoms with special interpretation.
3. Functions that return one of two atomic values should return a boolean.
4. Boolean-returning functions are conventionally named to make that clear (e.g. `is_...`).
5. Boolean-returning functions compose with the many standard-library functions that expect them.

# Construction / Recognition

## To Construct/Create:
1. Return the atom `true` or `false` from a predicate function.

## To Identify/Recognize:
1. A value of the atom `true` or `false` is being used as a boolean.

# Context & Application

- **Typical contexts**: predicates and conditions.
- **Common applications**: `lists:partition(fun is_file_open/1, L)` works directly when the predicate returns a boolean.
- **Historical/stylistic notes**: returning non-boolean atoms (e.g. `open`/`closed`) forces a conversion wrapper before calling standard library routines.

# Examples

**Example 1** (*Booleans*): a boolean-returning predicate composes cleanly with the standard library:

```erlang
lists:partition(fun is_file_open/1, L)
```

A `file_state/1` returning `open`/`closed` instead would need a `case` conversion wrapper before `lists:partition` could use it.

# Relationships

## Builds Upon
- **Atom** — Booleans are special-interpreted atoms.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Boolean expressions** — `and`, `or`, `not`, `xor` operate on boolean values.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Inventing pairs of atoms (`open`/`closed`, `yes`/`no`) for two-valued results.
  **Correction**: Return `true`/`false` so the function composes with boolean-consuming library functions.

# Common Confusions

- **Confusion**: Believing Erlang has a dedicated boolean type.
  **Clarification**: `true` and `false` are just atoms; there is no separate boolean type.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Booleans".

# Verification Notes

- Definition source: Direct quotation from *Booleans*.
- Confidence rationale: HIGH — the source explicitly states there is no boolean type and that `true`/`false` are atoms.
- Uncertainties: None.
- Cross-reference status: Slug `atom` assumed canonical; `boolean-expressions` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
