---
concept: Mnesia Table Type
slug: mnesia-table-type
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "From Record to Table"
extraction_confidence: high
aliases:
  - "table type"
  - "set, bag, ordered_set"
prerequisites:
  - mnesia
  - ets-table
related:
  - mnesia-table-storage-type
  - mnesia-schema
contrasts_with:
  - mnesia-table-storage-type
answers_questions:
  - "What table types does Mnesia support?"
  - "What distinguishes set, bag, and ordered_set Mnesia tables?"
---

# Mnesia Table Type

## Quick Definition

An Mnesia table type — `set`, `ordered_set`, or `bag` — defines how keyed records behave in the table, sharing the same semantics as the corresponding ETS/DETS types.

## Core Definition

Because of how ETS and DETS work, every Mnesia table needs a type, and the available types bear the same definitions as their ETS and DETS counterparts. The options are `set`, `bag`, and `ordered_set`, set via the `{type, Type}` option to `mnesia:create_table/2`. For `set` and `ordered_set` tables, writing a record with an existing primary key replaces the old record; for `bag` tables, the whole record must be identical to be considered a duplicate, so multiple records may share a key. Note that `ordered_set` is not supported for `disc_only_copies` tables, and `duplicate_bag` is not available for any storage type (Chapter 29, "From Record to Table" and "Of Mnesia Schemas and Tables").

## Prerequisites

- **Mnesia** — Table type is an Mnesia table property
- **ETS table** — The types are identical to ETS's; understanding ETS types transfers directly

## Key Properties

1. Three types are available: `set`, `ordered_set`, `bag`
2. `set` / `ordered_set`: at most one record per primary key; a write with an existing key replaces
3. `bag`: multiple records may share a primary key, distinguished by the full record value
4. `ordered_set` is not supported for `disc_only_copies` tables
5. `duplicate_bag` is not available for any Mnesia storage type
6. Set with the `{type, Type}` option of `mnesia:create_table/2`
7. Type is orthogonal to storage type (RAM vs. disk)

## Construction / Recognition

## To Choose a Table Type

1. Use `set` (or `ordered_set` for sorted iteration) when each key identifies at most one record
2. Use `bag` when multiple distinct records can legitimately share a key
3. Pass `{type, Type}` to `mnesia:create_table/2`

## Context & Application

In the `mafiapp` example, the `mafiapp_services` table is declared as `bag` because it is possible to have multiple services with the same sender and receiver — a `set` would allow only unique senders. The `mafiapp_friends` table uses the default `set` because each friend's name is unique.

## Examples

**Example** (Chapter 29, "Installing the Database"): `mnesia:create_table(mafiapp_services, [..., {type, bag}])` — multiple services between the same pair of friends are kept.

## Relationships

## Builds Upon

- **Mnesia** — Table type is configured when creating an Mnesia table

## Related

- **Mnesia schema** — Tables (and their types) are created against a schema
- **Mnesia table storage type** — A separate, orthogonal choice (RAM/disk)

## Contrasts With

- **Mnesia table storage type** — Table type governs key/record semantics; storage type governs where data physically lives

## Common Errors

- **Error**: Declaring an `ordered_set` table with `disc_only_copies`
  **Correction**: `ordered_set` is not supported for `disc_only_copies`; use a different type or storage

## Common Confusions

- **Confusion**: Expecting `duplicate_bag` to be available as in ETS
  **Clarification**: Mnesia does not support `duplicate_bag` for any storage type

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, sections "From Record to Table" and "Of Mnesia Schemas and Tables" (the `{type, Type}` option).

## Verification Notes

- Definition: Direct adaptation from "From Record to Table"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly enumerated with the `bag` example
- Cross-references: `ets-table` is a shared slug from Agent 4
