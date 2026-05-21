---
# === CORE IDENTIFICATION ===
concept: Mnesia Query
slug: mnesia-query

# === CLASSIFICATION ===
category: distribution
subcategory: mnesia
tier: intermediate

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
  - "mnesia:read"
  - "basic Mnesia query"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-table
extends: []
related:
  - mnesia-match-specification
  - mnesia-qlc
  - mnesia-transaction
  - mnesia-dirty-operation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I do a basic query on a Mnesia table?"
  - "What does mnesia:read return?"
  - "How does a bag table affect read results?"
---

# Quick Definition

A basic Mnesia query retrieves records by primary key with `mnesia:read/2` (inside a transaction) or `mnesia:dirty_read/2` (outside one); both return a list of matching records.

# Core Definition

The most basic Mnesia query looks up records by their primary key. Inside a transaction you use `mnesia:read/2`; outside a transaction you can use the dirty variant `mnesia:dirty_read/2`. Both `read` and `dirty_read` return a *list* of matching records — all records with the given key in the named table — and an empty list if none are found. For a `bag` table, more than one record may share a key, so the read returns all of them; for a normal `set` table a read returns either an empty list or a list with a single element. For lookups beyond the primary key, Mnesia offers more flexible operations: `select/2` with match specifications, and Query List Comprehensions (QLC) (Ch. 9, Section 9.2.5).

# Prerequisites

- **mnesia-table** — Queries read from Mnesia tables.

# Key Properties

1. Basic queries look up records by primary key.
2. `mnesia:read/2` is used inside a transaction; `dirty_read/2` outside one.
3. Both return a list of matching records (empty list if none).
4. A `bag` table read can return many records for one key.
5. A `set` table read returns zero or one record.
6. More expressive querying uses `select/2` or QLC.

# Construction / Recognition

## To Query by Key:
1. Inside a transaction, call `mnesia:read(Table, Key)`.
2. Outside a transaction, call `mnesia:dirty_read(Table, Key)`.
3. Pattern-match the resulting list of records.

## To Recognize:
1. A `mnesia:read/2` or `mnesia:dirty_read/2` call performs a basic key query.

# Context & Application

- **Typical contexts**: Looking up entries in a Mnesia database.
- **Common applications**: The cache's `lookup/1` using `dirty_read` on the `key_to_pid` table.
- **Historical/stylistic notes**: The book introduces `select` and QLC as richer alternatives for non-key queries.

# Examples

**Example 1** (Section 9.2.5): `mnesia:dirty_read(contributor, 1)` returns `[{contributor, 1, simple_cache}]` — a list of all records with key `1` in the Contributor table.

**Example 2** (Section 9.3.1): The cache's `lookup/1` calls `mnesia:dirty_read(key_to_pid, Key)` and matches `[{key_to_pid, Key, Pid}]` or `[]`.

# Relationships

## Builds Upon
- **mnesia-table** — Queries read from tables.

## Enables
- None.

## Related
- **mnesia-match-specification** — `select/2` offers richer matching.
- **mnesia-qlc** — Query List Comprehensions are a more expressive query interface.
- **mnesia-transaction** / **mnesia-dirty-operation** — `read` runs in transactions; `dirty_read` outside them.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting `read` to return a single record rather than a list.
  **Correction**: It always returns a list — empty, or with one element (`set`), or several (`bag`).

# Common Confusions

- **Confusion**: Thinking `read` and `dirty_read` are interchangeable everywhere.
  **Clarification**: `read` belongs inside a transaction; `dirty_read` is for use outside transactions.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.5 "Do some basic queries on your data."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.5.
- Confidence rationale: HIGH — the book demonstrates basic queries explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
