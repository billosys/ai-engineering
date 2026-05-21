---
# === CORE IDENTIFICATION ===
concept: Mnesia
slug: mnesia

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
section: "Mnesia: The Erlang Database (chapter introduction)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "the Erlang database"
  - "Amnesia (original name)"
  - DBMS

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record
  - process
  - node
extends:
  - ets
related:
  - mnesia-schema
  - mnesia-table
  - mnesia-transaction
  - mnesia-query-qlc
  - distributed-mnesia
contrasts_with:
  - ets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Mnesia?"
  - "What distinguishes ETS from Mnesia?"
  - "When should I use Mnesia?"
---

# Quick Definition

Mnesia is a distributed database management system written in Erlang and bundled with the standard Erlang distribution. It stores any Erlang data structure, supports transactions, comes with its own query language, and can replicate tables in RAM or on disk across multiple nodes.

# Core Definition

Mnesia is "a database written in Erlang for demanding telecommunications applications, and it is part of the standard Erlang distribution. It can be configured with RAM replicates on two physically separated nodes to provide a fast fault-tolerant data store. It provides transactions and comes with its own query language" (chapter introduction). Mnesia is extremely fast and highly configurable: database tables can be stored in RAM for speed or on disk for persistence, and tables can be replicated across machines for fault tolerance. Because Mnesia stores native Erlang terms, there is no impedance mismatch between database data and program data. (The name derives from "Amnesia" with the leading "A" dropped.)

# Prerequisites

- **Record** — Mnesia table rows are Erlang records; column definitions come from record definitions and `record_info(fields, ...)`.
- **Process** — Transactions guard against concurrent access by multiple processes; Mnesia runs as an OTP application.
- **Node** — Mnesia is configured per-node; the schema and table replicas are placed on lists of Erlang nodes.

# Key Properties

1. Part of the standard Erlang/OTP distribution; started as the `mnesia` application.
2. Stores any Erlang data structure (atoms, tuples, lists, nested terms) as table values — no impedance mismatch.
3. Tables can be RAM-resident (fast, transient), disk-resident (persistent), or disk-only; tables can be replicated across nodes.
4. Provides ACID transactions via `mnesia:transaction/1` using pessimistic locking.
5. Comes with QLC (query list comprehensions) for SQL-like querying.
6. Supports dirty operations for performance when transactional guarantees are not needed.
7. Originally built for demanding telecom applications; in production use at Ericsson since 1998.

# Construction / Recognition

## To Use Mnesia:
1. Create a schema once with `mnesia:create_schema([node()])` — this creates the `Mnesia.<node>` directory.
2. Start Mnesia with `mnesia:start()`.
3. Create tables with `mnesia:create_table/2`, supplying attributes from record definitions.
4. Read and write data inside transactions using `mnesia:transaction/1`.
5. Query data with QLC.
6. Stop Mnesia with `mnesia:stop()`.

## To Recognize Mnesia Usage:
1. Look for `mnesia:` module calls (`create_schema`, `create_table`, `transaction`, `write`, `read`, `delete`).
2. Look for a `Mnesia.<node>` directory holding the database files.

# Context & Application

Mnesia is the go-to embedded database for Erlang systems that need to keep state without an external DBMS process. It is used for multiuser games, websites, online payment systems, and telecom control data.

- **Typical contexts**: Fault-tolerant data stores, configuration data, session state, telecom applications.
- **Common applications**: RAM-replicated tables on two separated nodes for fast fault-tolerant storage.
- **Historical/stylistic notes**: Developed at Ericsson; in demanding telecom production use since 1998. The book covers only common usage; the definitive reference is the Mnesia User's Guide.

# Examples

**Example 1** ("Creating the Initial Database"): A one-time schema creation in the shell.

```erlang
1> mnesia:create_schema([node()]).
ok
2> init:stop().
```

**Example 2** ("Database Queries"): The `shop` and `cost` tables are defined by record definitions in `test_mnesia.erl`.

```erlang
-record(shop, {item, quantity, cost}).
-record(cost, {name, price}).
```

## Worked Example

From "Database Queries", the one-time setup that creates the schema and tables:

```erlang
do_this_once() ->
    mnesia:create_schema([node()]),
    mnesia:start(),
    mnesia:create_table(shop, [{attributes, record_info(fields, shop)}]),
    mnesia:create_table(cost, [{attributes, record_info(fields, cost)}]),
    mnesia:create_table(design, [{attributes, record_info(fields, design)}]),
    mnesia:stop().
```

# Relationships

## Builds Upon
- **ETS** — Mnesia builds on the same in-memory storage concepts as ETS and can use ETS-style table types.

## Enables
- **Mnesia schema** — The schema must exist before any tables.
- **Mnesia table** — Tables hold the actual data as records.
- **Mnesia transaction** — Transactions are the safe access mechanism.
- **Distributed Mnesia** — Replicating tables across nodes builds on Mnesia.

## Related
- **Mnesia query (QLC)** — The query mechanism for reading data.
- **Record** — Table rows are records.

## Contrasts With
- **ETS** — ETS is a single-node in-memory term store with no transactions, queries, or persistence; Mnesia adds transactions, QLC, disk storage, and distribution on top.

# Common Errors

- **Error**: Calling `mnesia:create_schema/1` repeatedly on each startup.
  **Correction**: The schema is created only once; subsequent runs just call `mnesia:start()`.

- **Error**: Calling `mnesia:write/1` or `mnesia:delete/1` outside a transaction fun.
  **Correction**: These should be called only inside a fun processed by `mnesia:transaction/1`.

# Common Confusions

- **Confusion**: Believing Mnesia is a replacement for SQL databases in every situation.
  **Clarification**: Mnesia is excellent for Erlang-native data and telecom-style workloads, but it is purpose-built rather than a general-purpose SQL DBMS; the book deliberately covers only common usage.

- **Confusion**: Thinking the name "Mnesia" relates to memory.
  **Clarification**: It was originally "Amnesia"; a manager objected that a database cannot forget things, so the leading "A" was dropped.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", chapter introduction and "Digging Deeper" section. Sidebar "Why Is the DBMS Called Mnesia?"

# Verification Notes

- Definition source: Direct quote from the chapter introduction.
- Confidence rationale: HIGH — the chapter explicitly and clearly defines Mnesia and its capabilities.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned cards for this chapter and canonical shared slugs.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
