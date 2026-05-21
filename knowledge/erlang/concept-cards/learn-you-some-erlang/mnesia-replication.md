---
concept: Mnesia Replication
slug: mnesia-replication
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "Of Mnesia Schemas and Tables"
extraction_confidence: high
aliases:
  - "table replication"
  - "local_content"
prerequisites:
  - mnesia
  - mnesia-schema
  - mnesia-table-storage-type
related:
  - mnesia-transaction
contrasts_with: []
answers_questions:
  - "How does Mnesia replicate tables across nodes?"
  - "What does the local_content table option do?"
---

# Mnesia Replication

## Quick Definition

Mnesia replication is the automatic copying of a table's data across the nodes listed in its storage options, so every replica node holds the same data; `local_content` opts a table out of replication.

## Core Definition

Mnesia supports distribution and replication of tables to many nodes. Where a table is replicated is determined by the node lists given in its storage options (`disc_copies`, `disc_only_copies`, `ram_copies`) to `mnesia:create_table/2` — and these are recorded in the schema. By default every Mnesia table has `{local_content, false}`, meaning the table and its data are replicated on all nodes that are part of the schema. Setting `{local_content, true}` instead creates the table on all nodes but keeps each node's content local and unshared — Mnesia then merely acts as an engine to initialize similar empty tables on many nodes (Chapter 29, "Of Mnesia Schemas and Tables" and "Deleting Stuff, Demonstrated").

## Prerequisites

- **Mnesia** — Replication is a built-in Mnesia capability
- **Mnesia schema** — The schema records which nodes a table is synchronized with
- **Mnesia table storage type** — The storage options' node lists determine replica placement

## Key Properties

1. Replication targets are the nodes named in the table's storage-option lists
2. The schema must include the target nodes for replication to occur
3. `{local_content, false}` (the default) replicates the table and its data across all schema nodes
4. `{local_content, true}` creates the table on all nodes but keeps content node-local and unshared
5. With `local_content`, Mnesia initializes empty tables everywhere but shares nothing
6. Transactions commit coordinated across all replica nodes; data written on one node becomes visible on the others
7. `mnesia:system_info()` shows running database nodes and which tables/schema are replicated where

## Construction / Recognition

## To Replicate (or Not Replicate) a Table

1. To replicate: list all desired nodes in the table's `disc_copies`/`disc_only_copies`/`ram_copies` option
2. To keep a table node-private: add `{local_content, true}` to the `create_table` options
3. Verify with `mnesia:system_info()`

## Context & Application

In `mafiapp`, the `mafiapp_friends` and `mafiapp_services` tables are replicated across nodes — adding a friend on the `corleone` node makes it visible on `genco`. The `mafiapp_enemies` table uses `{local_content, true}` because personal enemies are private to each node: an enemy added on `corleone` is not visible on `genco` (though `rpc` could trivially circumvent the privacy).

## Examples

**Example** (Chapter 29, "Meet the Boss"): a friend added on the `corleone` node is immediately queryable on `genco` via `mafiapp:friend_by_expertise/1`, and survives a node restart because the data is replicated and persisted.

**Example** (Chapter 29, "Deleting Stuff, Demonstrated"): `mnesia:create_table(mafiapp_enemies, [..., {local_content, true}])` — `find_enemy("Some Guy")` returns the record on `corleone` but `undefined` on `genco`.

## Relationships

## Builds Upon

- **Mnesia** — Replication is a core Mnesia feature
- **Mnesia schema** — The schema tracks replica node membership
- **Mnesia table storage type** — Storage-option node lists place the replicas

## Related

- **Mnesia transaction** — Transactions coordinate commits across replica nodes

## Common Errors

- **Error**: Expecting a table to replicate to a node not in the schema
  **Correction**: The schema must include the node; `create_schema` must cover all replica nodes

## Common Confusions

- **Confusion**: Thinking `local_content` tables share nothing structurally
  **Clarification**: A `local_content` table's *structure* is created on every node; only its *data* is node-local

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, sections "Of Mnesia Schemas and Tables" (the `local_content` option) and "Deleting Stuff, Demonstrated."

## Verification Notes

- Definition: Synthesized from the `local_content` discussion and the multi-node demonstrations
- Key Properties: All explicit in the chapter
- Confidence: HIGH — replication behavior is explicitly described and demonstrated on two nodes
- Cross-references: verified against planned cards in this extraction
