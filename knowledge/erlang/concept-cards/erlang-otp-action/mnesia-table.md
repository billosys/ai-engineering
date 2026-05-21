---
# === CORE IDENTIFICATION ===
concept: Mnesia Table
slug: mnesia-table

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
  - "mnesia:create_table"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-schema
extends: []
related:
  - mnesia-table-type
  - mnesia-storage-type
  - mnesia-record-mapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia table?"
  - "How do I create a Mnesia table?"
  - "What is the attributes option for?"
---

# Quick Definition

A Mnesia table is a collection of tagged tuples (typically Erlang records) created with `mnesia:create_table/2`; the `attributes` option names the record fields, and the first field is always the primary key.

# Core Definition

A Mnesia table stores a collection of tagged tuples — exactly what Erlang records are. Tables are created with `mnesia:create_table(Name, Options)`, where `Options` is a list of `{Name, Value}` pairs. The main option almost always needed is `attributes`, which assigns names to the fields of the records stored in the table; without it, Mnesia assumes records have just two fields named `key` and `val`. Regardless of how fields are named, *the first field of the record is always the primary key*. Mnesia does not know that a table relates to a `-record(...)` declaration of the same name — you connect them yourself, typically with `record_info(fields, RecordName)` to supply the field names. With only `attributes` specified, a table gets default settings: readable and writeable, `ram_copies` storage, records named the same as the table, `set` type, load priority 0, and `local_content` false (Ch. 9, Section 9.2.3).

# Prerequisites

- **mnesia** — Tables live inside a Mnesia database.
- **mnesia-schema** — The schema describes the tables.

# Key Properties

1. Stores tagged tuples, typically Erlang records.
2. Created with `mnesia:create_table(Name, Options)`.
3. The `attributes` option names the record fields.
4. The first field of the record is always the primary key.
5. Mnesia does not auto-link a table to a like-named record — you connect them.
6. Unspecified options default (e.g., `ram_copies`, `set` type).

# Construction / Recognition

## To Create a Table:
1. Define a record for the table entries.
2. Call `mnesia:create_table(Name, [{attributes, record_info(fields, Name)} | OtherOptions])`.
3. Optionally set `type`, storage type, or `index` options.

## To Recognize:
1. A `mnesia:create_table/2` call with an `attributes` option defines a Mnesia table.

# Context & Application

- **Typical contexts**: Defining the data model of a Mnesia database.
- **Common applications**: User/Project/Contributor tables; the cache's `key_to_pid` table.
- **Historical/stylistic notes**: `record_info/2` is resolved at compile time and cannot be called at runtime or from the shell.

# Examples

**Example 1** (Section 9.2.3, Listing 9.2): `mnesia:create_table(user, [{attributes, record_info(fields, user)}])` creates the User table.

**Example 2** (Section 9.3.1): `mnesia:create_table(key_to_pid, [{index, [pid]}, {attributes, record_info(fields, key_to_pid)}])` creates the cache's indexed key-to-pid table.

# Relationships

## Builds Upon
- **mnesia** — Tables are the storage units of Mnesia.
- **mnesia-schema** — The schema describes each table.

## Enables
- None.

## Related
- **mnesia-table-type** — Each table is a set, ordered_set, or bag.
- **mnesia-storage-type** — Each table has a storage type per node.
- **mnesia-record-mapping** — Tables map to Erlang records you connect manually.

## Contrasts With
- None.

# Common Errors

- **Error**: Omitting the `attributes` option and getting unexpected `key`/`val` fields.
  **Correction**: Always supply `attributes`, ideally via `record_info(fields, RecordName)`.

# Common Confusions

- **Confusion**: Assuming Mnesia automatically links a table to a record of the same name.
  **Clarification**: It does not; you must set up that connection yourself.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.3 "Creating the tables," Listing 9.2 and the "Mnesia tables and Erlang records" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 9.2.3.
- Confidence rationale: HIGH — the book explains table creation and defaults explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
