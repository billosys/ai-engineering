---
# === CORE IDENTIFICATION ===
concept: Mnesia Table
slug: mnesia-table

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Database Queries / Creating Tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - table
  - "Mnesia table definition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-schema
  - record
extends: []
related:
  - mnesia-table-types
  - mnesia-transaction
  - mnesia-query-qlc
contrasts_with:
  - ets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Mnesia table?"
  - "How do I create an Mnesia table?"
  - "How do records relate to Mnesia tables?"
---

# Quick Definition

An Mnesia table is a set or bag of rows where each row is an Erlang record. Tables are created with `mnesia:create_table/2`, and their columns are defined by a record definition.

# Core Definition

"A table in Mnesia is a set or bag of rows, where each row is an Erlang record" ("Database Queries"). To represent a table you need a record definition that defines its columns. Tables are created with `mnesia:create_table(Name, ArgS)`, where `ArgS` is a list of `{Key, Val}` tuples; `create_table` returns `{atomic, ok}` on success or `{aborted, Reason}` on failure. By convention, the table `Name` is the name of an Erlang record, and table rows are instances of that record. The first column is the table's primary key.

# Prerequisites

- **Mnesia** — Tables live inside an Mnesia database.
- **Mnesia schema** — The schema must exist before tables can be created.
- **Record** — Each row is a record; the table's columns come from a record definition via `record_info(fields, ...)`.

# Key Properties

1. A table is a set or bag of rows; each row is an Erlang record.
2. Created with `mnesia:create_table(Name, ArgS)`; returns `{atomic, ok}` or `{aborted, Reason}`.
3. The table name (an atom) is, by convention, the name of the record stored in it.
4. The `{attributes, AtomList}` argument names the columns; commonly given as `{attributes, record_info(fields, xxx)}`.
5. The first column is the primary key; writing a record with an existing key overwrites that row (in a `set` table).
6. Tables can store arbitrary Erlang terms, including arbitrary terms as keys.
7. Table definitions are loaded once per Erlang session before the database is used.

# Construction / Recognition

## To Create a Table:
1. Define a record describing the columns, e.g. `-record(shop, {item, quantity, cost}).`
2. With the schema created and Mnesia started, call `mnesia:create_table(shop, [{attributes, record_info(fields, shop)}])`.
3. Optionally pass type and storage options (`{type, ...}`, `{disc_copies, ...}`, etc.).
4. Confirm the call returns `{atomic, ok}`.

## To Recognize:
1. Look for `mnesia:create_table/2` calls.
2. Look for a record whose name matches the table name.

# Context & Application

Mnesia tables hold all persistent or replicated data in an Erlang system.

- **Typical contexts**: Modeling domain entities (`shop`, `cost`, `design`) as records and storing them.
- **Common applications**: One `create_table` call per entity, run once at setup time.
- **Historical/stylistic notes**: The book's `shop` table holds item/quantity/cost rows; the `cost` table holds name/price rows.

# Examples

**Example 1** ("Database Queries"): The `shop` table is created from the `shop` record.

```erlang
mnesia:create_table(shop, [{attributes, record_info(fields, shop)}])
```

**Example 2** ("Adding a Row"): A new `shop` record is written; because the table is a `set` and `item` is the primary key, an existing `item` row is overwritten.

```erlang
add_shop_item(Name, Quantity, Cost) ->
    Row = #shop{item=Name, quantity=Quantity, cost=Cost},
    F = fun() -> mnesia:write(Row) end,
    mnesia:transaction(F).
```

# Relationships

## Builds Upon
- **Mnesia schema** — Tables are created within an existing schema.

## Enables
- **Mnesia query (QLC)** — Queries iterate over tables via `mnesia:table/1`.
- **Mnesia transaction** — Reads and writes to tables happen inside transactions.

## Related
- **Mnesia table types** — A table's behavior depends on its type and storage configuration.
- **Record** — Rows are records.

## Contrasts With
- **ETS** — ETS tables also store tuples/records but are single-node, non-transactional, and not queried with QLC by default.

# Common Errors

- **Error**: Creating a table before the schema exists or before `mnesia:start()`.
  **Correction**: Create the schema, start Mnesia, then create tables.

- **Error**: Mismatching the `attributes` list with the record fields.
  **Correction**: Use `{attributes, record_info(fields, xxx)}` so the columns always match the record.

# Common Confusions

- **Confusion**: Believing table rows are plain tuples unrelated to records.
  **Clarification**: Rows are Erlang records; the table name conventionally equals the record name.

- **Confusion**: Thinking a new write always adds a row.
  **Clarification**: In a `set` table, writing a record with an existing primary key overwrites the existing row.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", sections "Database Queries", "Adding and Removing Data in the Database", and "Creating Tables".

# Verification Notes

- Definition source: Direct quote from "Database Queries"; create_table behavior from "Creating Tables".
- Confidence rationale: HIGH — tables, their creation, and primary-key behavior are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
