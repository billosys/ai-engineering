---
# === CORE IDENTIFICATION ===
concept: Mnesia Index
slug: mnesia-index

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
section: "9.3.1 Switching from ETS to Mnesia"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "index"
  - "mnesia:dirty_index_read"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-table
extends: []
related:
  - mnesia-query
  - ets-to-mnesia-migration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia index?"
  - "What are the trade-offs of adding an index?"
  - "How do I read a table by an indexed field?"
---

# Quick Definition

A Mnesia index is an extra table that allows fast operations on a field other than the primary key, at the cost of extra space and slower writes.

# Core Definition

A Mnesia index is an extra table that allows speedy operations on fields other than the primary key. An index is requested with the `{index, [Field]}` option to `mnesia:create_table/2`. Indexes carry trade-offs: an index consumes additional space, and it is populated and kept up to date on every insertion into the primary table, which makes startup and writing slower — it is important to be aware of these trade-offs. Indexed lookups use special index-aware functions such as `mnesia:dirty_index_read/3`, whose arguments are the table name, the key to index on, and which index to search (a table may have several). The index column can be specified by column number using the `#recordname.fieldname` syntax, or by the field name atom — the latter being slightly slower (Ch. 9, Section 9.3.1).

# Prerequisites

- **mnesia-table** — An index is an auxiliary structure on a table.

# Key Properties

1. An extra table speeding operations on a non-key field.
2. Requested via the `{index, [Field]}` create-table option.
3. Consumes additional space.
4. Populated and kept current on every primary-table insertion, slowing writes/startup.
5. Read with index-aware functions like `dirty_index_read/3`.
6. The index is specified by `#recordname.fieldname` column number or by field-name atom.

# Construction / Recognition

## To Use an Index:
1. Add `{index, [Field]}` to the `create_table` options.
2. Read by the indexed field with `mnesia:dirty_index_read(Table, Key, IndexColumn)`.
3. Specify the index column as `#record.field` (faster) or the field atom (slower).

## To Recognize:
1. An `{index, [...]}` table option, or a `dirty_index_read/3` call, indicates index use.

# Context & Application

- **Typical contexts**: Tables queried frequently on a secondary field.
- **Common applications**: The cache's `key_to_pid` table indexed on `pid` so `delete/1` can find an entry by pid.
- **Historical/stylistic notes**: The book justifies the cache's index because deletion needs to find a key given only a pid.

# Examples

**Example 1** (Section 9.3.1): `mnesia:create_table(key_to_pid, [{index, [pid]}, ...])` adds a `pid` index so the table can be searched by pid as well as by key.

**Example 2** (Section 9.3.1): `delete/1` uses `mnesia:dirty_index_read/3` with the table name, the pid, and the `#key_to_pid.pid` index column to find the entry to delete.

# Relationships

## Builds Upon
- **mnesia-table** — An index is an auxiliary structure on a table.

## Enables
- None.

## Related
- **mnesia-query** — Indexes accelerate non-key queries.
- **ets-to-mnesia-migration** — The cache's pid index supports the converted `delete/1`.

## Contrasts With
- None.

# Common Errors

- **Error**: Adding indexes liberally without considering cost.
  **Correction**: Each index costs space and slows writes/startup; add one only when the speedup is justified.

# Common Confusions

- **Confusion**: Thinking an index is just metadata on the main table.
  **Clarification**: An index is itself an extra table that must be maintained on every insert.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.3.1 "Switching from ETS to Mnesia," subsections "Rewriting init/0" and "Rewriting delete/1."

# Verification Notes

- Definition source: Directly adapted from Section 9.3.1.
- Confidence rationale: HIGH — the book explains indexes, their cost, and `dirty_index_read`.
- Uncertainties: None.
- Cross-reference status: Verified.
