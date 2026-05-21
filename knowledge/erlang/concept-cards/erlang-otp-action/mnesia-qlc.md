---
# === CORE IDENTIFICATION ===
concept: Query List Comprehensions (QLC)
slug: mnesia-qlc

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
  - "QLC"
  - "qlc:q"
  - "Query List Comprehensions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-query
extends: []
related:
  - mnesia-match-specification
  - mnesia-transaction
contrasts_with:
  - mnesia-match-specification

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Query List Comprehensions?"
  - "How do I query Mnesia with QLC?"
  - "Why is QLC more readable than match specifications?"
---

# Quick Definition

Query List Comprehensions (QLC) are a generic, list-comprehension-style query interface for table-like data sources such as Mnesia and ETS; queries are wrapped in `qlc:q(...)` and evaluated with `qlc:eval/1`.

# Core Definition

Query List Comprehensions (QLC) are a more expressive way to query Mnesia, a more recent addition to Erlang/OTP. Superficially they look like normal list comprehensions, but they are wrapped in what looks like a call to `qlc:q(...)`, which is a marker telling the compiler to handle the expression specially. For QLC to work, the module's source must include the line `-include_lib("stdlib/include/qlc.hrl")` (the Erlang shell allows `qlc:q(...)` directly, since it has no include files). The value produced by `qlc:q(...)` is a query handle, whose results are fetched with `qlc:eval(Handle)`. QLC is a generic query interface to anything table-like — ETS tables, Mnesia tables, and custom table implementations with a QLC adapter. `mnesia:table(TableName)` creates a handle representing a Mnesia table as QLC input; from there, normal list-comprehension syntax filters and aggregates. QLC is considerably more elegant and readable than `select` with match specifications, and can be mixed with other Mnesia functions inside a transaction (Ch. 9, Section 9.2.5).

# Prerequisites

- **mnesia-query** — QLC is an advanced Mnesia query mechanism.

# Key Properties

1. List-comprehension-style query syntax wrapped in `qlc:q(...)`.
2. Requires `-include_lib("stdlib/include/qlc.hrl")` in module source.
3. `qlc:q(...)` yields a query handle; `qlc:eval/1` fetches results.
4. A generic interface to table-like sources: Mnesia, ETS, custom adapters.
5. `mnesia:table(TableName)` adapts a Mnesia table as QLC input.
6. More readable than match specifications; usable inside transactions.

# Construction / Recognition

## To Query with QLC:
1. Add `-include_lib("stdlib/include/qlc.hrl")` to the module.
2. Get a table handle with `mnesia:table(TableName)`.
3. Build a query with `qlc:q([...])` using list-comprehension syntax.
4. Evaluate with `qlc:eval(Handle)`, typically inside a transaction.

## To Recognize:
1. A `qlc:q([...])` expression or a `qlc:eval/1` call indicates QLC use.

# Context & Application

- **Typical contexts**: Readable, expressive queries over Mnesia or ETS.
- **Common applications**: Selecting fields from records matching a predicate.
- **Historical/stylistic notes**: The `qlc` module of stdlib documents QLC in detail.

# Examples

**Example 1** (Section 9.2.5): Inside a transaction, `Table = mnesia:table(user)`, `QueryHandle = qlc:q([U#user.id || U <- Table, U#user.name =:= martin])`, `qlc:eval(QueryHandle)` returns the `id`s of users named `martin` — the same result as the equivalent `select`.

# Relationships

## Builds Upon
- **mnesia-query** — QLC extends Mnesia's query capabilities.

## Enables
- None.

## Related
- **mnesia-transaction** — QLC queries can run inside transactions.

## Contrasts With
- **mnesia-match-specification** — Match specifications are lower-level and harder to read; QLC is the more elegant alternative.

# Common Errors

- **Error**: Using `qlc:q(...)` in a module without including `qlc.hrl`.
  **Correction**: Add `-include_lib("stdlib/include/qlc.hrl")` so the special QLC compilation triggers.

# Common Confusions

- **Confusion**: Thinking `qlc:q(...)` is an ordinary function call.
  **Clarification**: It is a compile-time marker that makes the compiler treat the list comprehension specially.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.5 "Do some basic queries on your data," subsection "Using Query List Comprehensions (QLC)."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.5.
- Confidence rationale: HIGH — the book explains QLC with a worked example.
- Uncertainties: None.
- Cross-reference status: Verified.
