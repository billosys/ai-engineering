---
# === CORE IDENTIFICATION ===
concept: Mnesia Table Type
slug: mnesia-table-type

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
section: "9.2.3 Creating the tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "set"
  - "ordered_set"
  - "bag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-table
extends: []
related:
  - mnesia-storage-type
  - ets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What table types does Mnesia support?"
  - "What is the difference between a set and a bag in Mnesia?"
  - "What is an ordered_set?"
---

# Quick Definition

A Mnesia table type — `set`, `ordered_set`, or `bag` — determines how the table treats keys: `set` and `ordered_set` allow one record per key, while `bag` allows multiple records per key.

# Core Definition

A Mnesia table can be one of three types (Ch. 9, Section 9.2.3): a `set` treats keys as unique — inserting a record with the same primary key as an existing entry overwrites the old one; a `bag` can contain multiple records with the same key, as long as they differ in at least one field (inserting the exact same record twice has no effect); an `ordered_set` behaves the same as a `set` regarding key uniqueness, but whereas `set`s and `bag`s are implemented with hash tables, an `ordered_set` keeps records stored in the order of their primary keys, which is useful for traversing entries in order. The type is chosen with the `{type, Type}` option to `mnesia:create_table/2`; the default is `set`.

# Prerequisites

- **mnesia-table** — The type is a property chosen when creating a table.

# Key Properties

1. Three types: `set`, `ordered_set`, `bag`.
2. `set`: unique keys; a new record with an existing key overwrites it.
3. `bag`: multiple records per key, if they differ in at least one field.
4. `ordered_set`: like `set` but keeps records ordered by primary key.
5. `set` and `bag` use hash tables; `ordered_set` keeps sorted order.
6. The default type is `set`; chosen via the `{type, Type}` option.

# Construction / Recognition

## To Choose a Type:
1. Use `set` (the default) for unique-key key-value data.
2. Use `bag` when one key may have many associated records.
3. Use `ordered_set` when ordered traversal by key is needed.
4. Pass `{type, bag}` (etc.) in the `create_table` options.

## To Recognize:
1. A `{type, ...}` option in `mnesia:create_table/2` declares the table type.

# Context & Application

- **Typical contexts**: Choosing the structure of a Mnesia table.
- **Common applications**: A `bag` Contributor table; a `set` `key_to_pid` cache table.
- **Historical/stylistic notes**: `ordered_set` is not supported for disk-only tables.

# Examples

**Example 1** (Section 9.2.3): `mnesia:create_table(contributor, [{type, bag}, ...])` makes the Contributor table a `bag`, so one user ID key can hold many contributor records.

**Example 2** (Section 9.3.1): The cache's `key_to_pid` table is a normal `set` with unique keys.

# Relationships

## Builds Upon
- **mnesia-table** — The type is a per-table setting.

## Enables
- None.

## Related
- **mnesia-storage-type** — A separate, orthogonal table property.
- **ets** — ETS tables have similar but slightly different type options.

## Contrasts With
- None.

# Common Errors

- **Error**: Using a `set` table when multiple records per key are needed.
  **Correction**: Use a `bag` so several records can share a key.

# Common Confusions

- **Confusion**: Confusing table type with storage type.
  **Clarification**: Type (`set`/`ordered_set`/`bag`) governs key uniqueness; storage type governs RAM vs. disk.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.3 "Creating the tables," subsection "The different types of Mnesia tables."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.3.
- Confidence rationale: HIGH — the book explicitly defines all three types.
- Uncertainties: None.
- Cross-reference status: Verified; `ets` owned by Agent 2.
