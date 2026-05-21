---
concept: Mnesia Table Storage Type
slug: mnesia-table-storage-type
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
  - "ram_copies"
  - "disc_copies"
  - "disc_only_copies"
  - "storage strategy"
prerequisites:
  - mnesia
  - ets-table
related:
  - mnesia-table-type
  - mnesia-schema
  - mnesia-replication
contrasts_with:
  - mnesia-table-type
answers_questions:
  - "What storage strategies does Mnesia offer for tables?"
  - "What distinguishes ram_copies, disc_copies, and disc_only_copies?"
---

# Mnesia Table Storage Type

## Quick Definition

An Mnesia table's storage type — `ram_copies`, `disc_copies`, or `disc_only_copies` — decides whether the table lives in memory, on disk, or both, per node.

## Core Definition

Because Mnesia is built on ETS and DETS, it offers two means of storage — in memory or on disk — and you must pick a strategy per table. The three storage options are: `ram_copies` (data only in ETS, in memory, theoretically limited to ~4GB on 32-bit VMs); `disc_only_copies` (data only in DETS, on disk, limited to DETS's 2GB per table); and `disc_copies` (data in both ETS and on disk, not restricted by DETS limits because Mnesia uses transaction logs and checkpoints). These are given as the `{disc_copies, NodeList}`, `{disc_only_copies, NodeList}`, and `{ram_copies, NodeList}` options to `mnesia:create_table/2`, and more than one may be present at once (Chapter 29, "From Record to Table" and "Of Mnesia Schemas and Tables").

## Prerequisites

- **Mnesia** — Storage type is an Mnesia table configuration
- **ETS table** — The in-memory side reuses ETS; the on-disk side reuses DETS

## Key Properties

1. `ram_copies`: in-memory only (ETS); fast, but volatile and memory-bounded
2. `disc_only_copies`: on-disk only (DETS); persistent, but bound by DETS's 2GB-per-table limit
3. `disc_copies`: both memory and disk; persistent and fast, not bound by the DETS limit
4. Each option takes a node list, so a table's storage can differ per node (e.g., disc+RAM on a master, RAM-only on slaves, disk-only on a backup)
5. Multiple storage options can be combined for one table across different nodes
6. A disk schema is required before disk-based tables (`disc_copies`, `disc_only_copies`) can be created
7. `mnesia:change_table_copy_type/3` moves a table to a different storage type at runtime

## Construction / Recognition

## To Choose a Storage Type

1. Use `ram_copies` for transient, performance-critical, memory-bounded data
2. Use `disc_only_copies` for persistent data that need not be in memory and stays under 2GB
3. Use `disc_copies` for long-lasting data that should also be fast to query in memory
4. Pass the chosen option (with a node list) to `mnesia:create_table/2`

## Context & Application

The `mafiapp` example uses `disc_copies` for both tables because friendship data must be long-lasting (surviving power failures) yet fast for somewhat complex queries that benefit from in-memory copies. The author notes that `disc_only_copies` avoids the memory cost but makes searches slower, since disk access is the slowest part.

## Examples

**Example** (Chapter 29, "Installing the Database"): `mnesia:create_table(mafiapp_friends, [..., {disc_copies, Nodes}])` stores the friends table in both RAM and on disk on every node.

## Relationships

## Builds Upon

- **Mnesia** — Storage type is set when creating an Mnesia table

## Related

- **Mnesia schema** — A disk schema is a prerequisite for disk-based storage types
- **Mnesia replication** — The node list in each storage option determines where copies are placed
- **Mnesia table type** — A separate, orthogonal choice (set/bag/ordered_set)

## Contrasts With

- **Mnesia table type** — Storage type governs where data physically lives; table type governs key/record semantics

## Common Errors

- **Error**: Creating a `disc_copies` table with only an in-memory schema
  **Correction**: A disk schema must exist first; create it with `mnesia:create_schema/1`

## Common Confusions

- **Confusion**: Thinking `disc_copies` is limited to DETS's 2GB ceiling
  **Clarification**: `disc_copies` is not bound by the DETS limit — Mnesia uses transaction logs and checkpoints; only `disc_only_copies` has the 2GB limit

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, sections "From Record to Table" and "Of Mnesia Schemas and Tables."

## Verification Notes

- Definition: Direct adaptation from "From Record to Table"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — the three options are explicitly enumerated and explained
- Cross-references: `ets-table` is a shared slug from Agent 4
