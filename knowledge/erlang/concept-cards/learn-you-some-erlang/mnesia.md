---
concept: Mnesia
slug: mnesia
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "What's Mnesia?"
extraction_confidence: high
aliases:
  - "mnesia database"
prerequisites:
  - ets-table
related:
  - mnesia-schema
  - mnesia-table-type
  - mnesia-transaction
  - mnesia-replication
  - mnesia-table-storage-type
contrasts_with:
  - ets-table
answers_questions:
  - "What is Mnesia?"
  - "How do ETS and Mnesia relate?"
---

# Mnesia

## Quick Definition

Mnesia is a distributed database built into Erlang/OTP, layered on top of ETS and DETS, that natively stores and replicates arbitrary Erlang terms and adds transactions.

## Core Definition

Mnesia is a layer built on top of ETS and DETS that adds functionality many developers would otherwise build themselves: writing to ETS and DETS automatically (gaining DETS's persistence and ETS's performance), replicating the database to many Erlang nodes, and supporting transactions. It is "pretty much the only full-featured database available that will natively store and return any Erlang term out of the box." On the CAP theorem it sits on the CP side — strong consistency, but it reacts badly to netsplits. Mnesia is centered on the idea of using a record to define a table's structure (Chapter 29, "What's Mnesia?").

## Prerequisites

- **ETS table** — Mnesia is built on ETS (and DETS); understanding ETS table types and operations is needed first

## Key Properties

1. A layer over ETS and DETS, combining ETS performance with DETS persistence
2. Supports automatic replication of tables across Erlang nodes
3. Provides transactions — multiple operations acting as a single isolated unit
4. Natively stores any Erlang term (atoms, pids, references, etc.)
5. CP under the CAP theorem: strong consistency, poor netsplit tolerance
6. Inherits DETS limitations in some modes (e.g., the 2GB single-table on-disk limit, bypassable via fragmentation)
7. Suited to smaller data volumes on a limited, fixed number of nodes (practically ~10)
8. Tables are defined from Erlang records

## Context & Application

Mnesia is the right choice when you know it will run on a fixed number of nodes, have an idea of the data volume, and primarily access data from Erlang in ways ETS and DETS already allow. It is not meant to replace a standard SQL database, nor to handle terabytes across many data centers. The chapter builds a Mafia friend-tracking application (`mafiapp`) to demonstrate it.

## Examples

**Example** (Chapter 29, "Meet the Boss"): the `mafiapp` application runs Mnesia across nodes `corleone` and `genco`; `mnesia:system_info()` shows both nodes as running database nodes with `disc_copies` tables and schema.

## Relationships

## Builds Upon

- **ETS table** — Mnesia layers over ETS (and DETS)

## Related

- **Mnesia schema** — The metadata Mnesia needs to store and load tables
- **Mnesia table type**, **Mnesia table storage type** — How tables are structured and stored
- **Mnesia transaction** — The activity context giving isolation and consistency
- **Mnesia replication** — Automatic copying of tables across nodes

## Contrasts With

- **ETS table** — ETS is a single-node in-memory store with no transactions; Mnesia adds persistence, replication, and transactions on top

## Common Errors

- **Error**: Choosing Mnesia for terabyte-scale, many-data-center workloads
  **Correction**: Mnesia targets smaller data on a limited, fixed node count; use another database for large NoSQL-style scale

## Common Confusions

- **Confusion**: Treating Mnesia as an eventually consistent (AP) datastore
  **Clarification**: Mnesia is CP — it gives strong consistency but reacts badly to netsplits

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "What's Mnesia?" and the closing "Remember Mnesia."

## Verification Notes

- Definition: Direct adaptation from "What's Mnesia?"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined and characterized
- Cross-references: `ets-table` is a shared slug from Agent 4
