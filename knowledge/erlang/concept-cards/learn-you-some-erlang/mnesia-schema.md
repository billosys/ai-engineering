---
concept: Mnesia Schema
slug: mnesia-schema
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
  - "schema"
prerequisites:
  - mnesia
related:
  - mnesia-table-storage-type
  - mnesia-replication
contrasts_with: []
answers_questions:
  - "What is an Mnesia schema?"
  - "How do I set up an Mnesia database?"
---

# Mnesia Schema

## Quick Definition

The Mnesia schema is the metadata describing how Mnesia stores tables on disk, loads them, and which nodes they are synchronized with; it must be created before Mnesia starts if you want disk-based tables.

## Core Definition

To know how to store tables on disk, how to load them, and which other nodes they should be synchronized with, Mnesia needs a *schema* holding all that information. By default Mnesia creates a schema directly in memory when started — fine for RAM-only tables — but a schema that must survive VM restarts on every node of the cluster must be created on disk. This creates a chicken-and-egg situation: Mnesia depends on the schema, yet Mnesia creates it. The resolution is `mnesia:create_schema(ListOfNodes)`, which must be called *before* starting Mnesia; it writes schema files on each listed node (Chapter 29, "Of Mnesia Schemas and Tables").

## Prerequisites

- **Mnesia** — The schema is Mnesia's own metadata structure

## Key Properties

1. Holds information on table storage, loading, and node synchronization
2. By default an in-memory schema is created when Mnesia starts — adequate only for `ram_copies` tables
3. A persistent (disk) schema must be created before Mnesia starts, via `mnesia:create_schema(Nodes)`
4. The listed nodes must be running (but not necessarily connected) when `create_schema` is called
5. Schema location is controlled by the Mnesia `dir` variable (`erl -mnesia dir ...` or `application:set_env(mnesia, dir, ...)`)
6. Schema creation can fail if one already exists, Mnesia is running on a target node, or the directory is not writable
7. An existing RAM schema can be converted to disk via `mnesia:change_table_copy_type(schema, node(), disc_copies)`
8. Tables can only be created while Mnesia is running, but the disk schema must be created while it is stopped

## Construction / Recognition

## To Set Up an Mnesia Schema

1. Optionally set the storage location with `application:set_env(mnesia, dir, Path)` or `erl -mnesia dir Path`
2. With Mnesia stopped on all target nodes, call `mnesia:create_schema(Nodes)`
3. Start Mnesia
4. Create tables with `mnesia:create_table/2`

## Context & Application

The schema's ordering constraints drive the standard Mnesia install function: create the schema (Mnesia stopped), start Mnesia on all nodes, create tables, stop Mnesia. Multi-node installs use `rpc:multicall/4` to start and stop Mnesia remotely so the schema is created with Mnesia stopped everywhere and tables are created with Mnesia running everywhere.

## Examples

**Example** (Chapter 29, "Installing the Database"): `install(Nodes) -> ok = mnesia:create_schema(Nodes), rpc:multicall(Nodes, application, start, [mnesia]), mnesia:create_table(...), rpc:multicall(Nodes, application, stop, [mnesia]).`

## Relationships

## Builds Upon

- **Mnesia** — The schema is part of Mnesia's machinery

## Related

- **Mnesia table storage type** — The schema records whether tables live in RAM, on disk, or both
- **Mnesia replication** — The schema records which nodes a table is synchronized with

## Common Errors

- **Error**: Calling `mnesia:create_schema/1` while Mnesia is running on a target node
  **Correction**: Stop Mnesia on all nodes first; the disk schema must be created with Mnesia not running

- **Error**: Expecting disk tables to work with the default in-memory schema
  **Correction**: Create a disk schema explicitly, or convert it with `change_table_copy_type`

## Common Confusions

- **Confusion**: Thinking the schema is created automatically for disk use
  **Clarification**: Only an in-memory schema is automatic; a persistent schema requires an explicit `create_schema` call before startup

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "Of Mnesia Schemas and Tables" and "Creating Tables" / "Installing the Database."

## Verification Notes

- Definition: Direct adaptation from "Of Mnesia Schemas and Tables"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with the chicken-and-egg discussion and code
- Cross-references: verified against planned cards in this extraction
