---
# === CORE IDENTIFICATION ===
concept: Mnesia Match Specification
slug: mnesia-match-specification

# === CLASSIFICATION ===
category: distribution
subcategory: mnesia
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.2.5 Do some basic queries on your data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "match specification"
  - "mnesia:select"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-query
extends: []
related:
  - mnesia-qlc
  - mnesia-transaction
contrasts_with:
  - mnesia-qlc

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia match specification?"
  - "How do I use mnesia:select/2?"
  - "What do the $1, $_, $$ atoms mean in a match specification?"
---

# Quick Definition

A match specification is a 3-tuple `{Head, Conditions, Results}` passed to `mnesia:select/2` to query a table flexibly — `Head` is a pattern with `'$N'` variables, and `Results` describes what to return per match.

# Core Definition

A match specification is the query form used by `mnesia:select/2`, whose first argument is the table to search and whose second is a list of match specifications. Each match specification is a 3-tuple `{Head, Conditions, Results}` (Ch. 9, Section 9.2.5):

- **Head** — an Erlang term representing a pattern, where single-quoted atoms of the form `'$1'`, `'$2'`, … represent variables.
- **Conditions** — additional constraints on a match; often just an empty list.
- **Results** — what terms to generate for each match, using the same `'$1'` etc., which are replaced by the matched values.

Special atoms have meaning: `'_'` (in `Head` only) matches any value; `'$_'` (in `Results`/`Conditions`) is the entire matching record; `'$$'` (in `Results`/`Conditions`) is the same as `'$1', '$2', …` for all bound variables. `select/2` is run inside a transaction; the result inside `{atomic, Data}` is a list with a value per matching record.

# Prerequisites

- **mnesia-query** — Match specifications are an advanced form of Mnesia querying.

# Key Properties

1. Used by `mnesia:select/2` for flexible, non-key queries.
2. A match specification is a `{Head, Conditions, Results}` 3-tuple.
3. `Head` is a pattern using `'$1'`, `'$2'`, … as variables.
4. `Conditions` adds constraints; often an empty list.
5. `Results` shapes the per-match output.
6. Special atoms: `'_'`, `'$_'`, `'$$'` have defined meanings.

# Construction / Recognition

## To Use a Match Specification:
1. Build a record pattern as `Head`, with `'$N'` atoms for fields you want bound.
2. Add `Conditions` (often `[]`) and a `Results` list (e.g., `['$1']`).
3. Call `mnesia:select(Table, [{Head, Conditions, Results}])` inside a transaction.

## To Recognize:
1. A `mnesia:select/2` call with a `{Head, [], Results}` tuple uses a match specification.

# Context & Application

- **Typical contexts**: Querying Mnesia tables on non-key fields.
- **Common applications**: Selecting all user IDs whose name field equals a given atom.
- **Historical/stylistic notes**: Match specifications can be complicated; QLC is the more readable alternative. The ERTS User's Guide has full details.

# Examples

**Example 1** (Section 9.2.5): `mnesia:select(user, [{#user{id = '$1', name = martin}, [], ['$1']}])` finds `#user` records named `martin` and returns their `id` field; wrapped in a transaction it yields `{atomic, [1]}`.

**Example 2** (Section 9.2.5): A `Results` spec like `[{'$1', '$2', '$3'}]` or `['$$']` extracts several fields from each matching record.

# Relationships

## Builds Upon
- **mnesia-query** — Match specifications extend basic querying.

## Enables
- None.

## Related
- **mnesia-transaction** — `select/2` runs inside a transaction.

## Contrasts With
- **mnesia-qlc** — QLC is a more expressive, readable query interface than raw match specifications.

# Common Errors

- **Error**: Using `'$_'` or `'$$'` in the `Head` part.
  **Correction**: `'$_'` and `'$$'` are valid only in `Results`/`Conditions`; `'_'` is the `Head`-only wildcard.

# Common Confusions

- **Confusion**: Thinking `'$1'` is a real Erlang variable.
  **Clarification**: It is a single-quoted atom that the match-specification engine treats as a variable placeholder.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.5 "Do some basic queries on your data," subsection "Using select with match specifications."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.5.
- Confidence rationale: HIGH — the book explains the 3-tuple structure and special atoms explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
