---
# === CORE IDENTIFICATION ===
concept: Mnesia Record Mapping
slug: mnesia-record-mapping

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
  - "record_info(fields, ...)"
  - "table-record connection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-table
extends: []
related:
  - mnesia-schema
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Mnesia table relate to an Erlang record?"
  - "What does record_info(fields, RecordName) do?"
  - "Why use record_info instead of hardcoding field names?"
---

# Quick Definition

Mnesia record mapping is the manually established connection between a Mnesia table and an Erlang record; the `attributes` option, typically supplied via `record_info(fields, RecordName)`, names the table's fields.

# Core Definition

To Mnesia, a table is just a bunch of tagged tuples — exactly what Erlang's records are. But Mnesia cannot know that a table has anything to do with a `-record(...)` declaration of the same name; you must set up this connection yourself. The link is made through the `attributes` table option, which lists the field (column) names. You could hardcode them — `{attributes, [title, description]}` — but it is better to use `record_info(fields, RecordName)`, which lists the field names automatically, so the table stays correct if you later change the record declaration. `record_info/2` is not a real function: it is resolved at compile time (just like the `#` record syntax) and cannot be called at runtime or from the Erlang shell. The book also notes it can sometimes be useful *not* to be forced into a table-record connection, even when they share a name (Ch. 9, Section 9.2.3).

# Prerequisites

- **mnesia-table** — Record mapping is how a table's fields are defined.

# Key Properties

1. Mnesia stores tagged tuples; Erlang records are tagged tuples.
2. Mnesia does not auto-link a table to a like-named record.
3. The connection is made via the `attributes` table option.
4. `record_info(fields, RecordName)` lists field names automatically.
5. `record_info/2` is compile-time only — not callable at runtime or in the shell.
6. Using `record_info` keeps the table in sync if the record changes.

# Construction / Recognition

## To Map a Record to a Table:
1. Define the `-record(name, {...})` for the table entries.
2. Create the table with `{attributes, record_info(fields, name)}`.
3. Insert and read using the record syntax `#name{...}`.

## To Recognize:
1. A `record_info(fields, ...)` call inside `create_table` options establishes the mapping.

# Context & Application

- **Typical contexts**: Every Mnesia table definition.
- **Common applications**: User/Project/Contributor tables; the `key_to_pid` table.
- **Historical/stylistic notes**: Records are typically kept in a separate header file included by the module.

# Examples

**Example 1** (Section 9.2.3, Listing 9.2): `mnesia:create_table(user, [{attributes, record_info(fields, user)}])` maps the `user` record to the `user` table.

**Example 2** (Section 9.2.3, sidebar): Hardcoding `{attributes, [title, description]}` is possible but inferior to `record_info(fields, project)`.

# Relationships

## Builds Upon
- **mnesia-table** — Record mapping defines a table's fields.

## Enables
- None.

## Related
- **mnesia-schema** — The schema records the attributes set up by the mapping.

## Contrasts With
- None.

# Common Errors

- **Error**: Trying to call `record_info/2` at runtime or from the shell.
  **Correction**: `record_info` is resolved at compile time; it cannot run dynamically.

# Common Confusions

- **Confusion**: Expecting Mnesia to know a table's structure from a like-named record automatically.
  **Clarification**: You must explicitly supply the `attributes` option to connect them.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.3 "Creating the tables," the "Mnesia tables and Erlang records" sidebar.

# Verification Notes

- Definition source: Directly adapted from the Section 9.2.3 sidebar.
- Confidence rationale: HIGH — the book explicitly explains the table-record connection.
- Uncertainties: None.
- Cross-reference status: Verified.
