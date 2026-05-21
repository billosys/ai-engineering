---
# === CORE IDENTIFICATION ===
concept: Upgrading Records
slug: upgrading-records

# === CLASSIFICATION ===
category: data-types
subcategory: records
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Upgrading Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - record format change
  - record migration
  - "mnesia:transform_table"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-change-callback
extends: []
related:
  - software-upgrade
  - release-upgrade
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I change a record format during a live software upgrade?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Upgrading records means migrating a changed record format across a live upgrade. Because the BEAM has no native record type, records are tuples, so a format change must be handled via the tuple representation in `code_change`.

# Core Definition

The BEAM virtual machine does not have a data structure to specifically represent a record in a database sense; instead, records are represented as tuples where the first element is an atom representing the record name and the other fields are tuple entries in the same order as they are defined (Cesarini & Vinoski, p. 342, pdf p. 336). If a record format changes during a live software upgrade, the only way to update the format is using the tuple representation of records. This problem does not occur if maps are used instead of tuples. For records stored in a Mnesia table, the `mnesia:transform_table/3,4` functions atomically apply a fun to all objects in the table to perform the transformation.

# Prerequisites

- **Code change callback** — Record migration is implemented inside `code_change`; that callback is required first.

# Key Properties

1. The BEAM has no native record type; records are tuples (`{RecordName, Field1, Field2, ...}`).
2. A record-format change during a live upgrade must be handled via the tuple representation.
3. The migration logic lives in the `code_change/3` function.
4. Both upgrade and downgrade clauses adjust the tuple shape.
5. Using maps instead of tuple-records avoids the problem entirely.
6. For Mnesia tables, `mnesia:transform_table/3,4` atomically applies a transformation fun to all objects.
7. `mnesia:transform_table` can also change the record name (not the table name) and update attributes.

# Construction / Recognition

## To Upgrade a Record Format:
1. Define the new record with the added/removed fields.
2. In `code_change/3`, match the old tuple shape and return the new tuple shape (e.g. append a default for a new field).
3. Add a `{down, Vsn}` clause that reverses the transformation for downgrades.
4. For Mnesia-stored records, call `mnesia:transform_table/3,4` with a transformation fun.

## To Recognize It:
1. A `code_change` clause that pattern-matches and rebuilds a tuple of a record's shape.
2. A `mnesia:transform_table` call in upgrade code.

# Context & Application

- **Typical contexts**: Live upgrades that add, remove, or reorder record fields.
- **Common applications**: Migrating a server's loop-data record; migrating records persisted in a Mnesia table.
- **Historical/stylistic notes**: The book recommends maps over tuple-records precisely because they sidestep this migration difficulty.

# Examples

**Example 1** (p. 342): A frequency-server record `-record(freq, {free, allocated})` has tuple representation `{freq, [5,6,7,8], []}`. Adding a `blocked` field gives `-record(freq, {free, allocated, blocked})`, migrated in `code_change/3`:

```erlang
code_change('1.0', {freq, Free, Alloc}, _Extra) ->
 {ok, {freq, Free, Alloc, []}};
code_change({down, '1.0'}, {freq, Free, Alloc, Blocked}, _Extra) ->
 {ok, {freq, Free++Blocked, Alloc}}.
```

**Example 2** (p. 342): For a Mnesia table, `mnesia:transform_table/3,4` atomically applies a transformation fun to every object, and can also change the record name and update attributes.

# Relationships

## Builds Upon
- **Code change callback** — Record migration is implemented inside `code_change`.

## Related
- **Software upgrade** — Record upgrades occur as part of a software upgrade.
- **Release upgrade** — Record migration is one of the state changes a release upgrade may require.

# Common Errors

- **Error**: Trying to migrate a record by its record syntax rather than its tuple form.
  **Correction**: The runtime sees records only as tuples; pattern-match and rebuild the tuple in `code_change`.

- **Error**: Editing Mnesia-stored records field-by-field outside a transaction.
  **Correction**: Use `mnesia:transform_table/3,4`, which applies the transformation atomically to all objects.

# Common Confusions

- **Confusion**: Thinking the BEAM stores records as a distinct data structure.
  **Clarification**: Records are tuples whose first element is the record-name atom; there is no native record type.

- **Confusion**: Believing record upgrades are unavoidable complexity.
  **Clarification**: Using maps instead of tuple-records avoids the format-migration problem entirely.

# Source Reference

Chapter 11: Release Upgrades, section "Upgrading Records," page 342 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of p. 342.
- Confidence rationale: HIGH — the source explicitly explains record-as-tuple migration and the `mnesia:transform_table` approach.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
