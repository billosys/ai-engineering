---
# === CORE IDENTIFICATION ===
concept: Mnesia Schema
slug: mnesia-schema

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
section: "Creating the Initial Database"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - schema
  - "Mnesia database directory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - node
extends: []
related:
  - mnesia-table
  - distributed-mnesia
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Mnesia schema?"
  - "How do I create an Mnesia database?"
---

# Quick Definition

The Mnesia schema is the on-disk directory structure that defines an Mnesia database on a set of nodes. It is created once with `mnesia:create_schema/1` before any tables can be defined.

# Core Definition

`mnesia:create_schema(NodeList)` "initiates a new Mnesia database on all the nodes in `NodeList` (which must be a list of valid Erlang nodes)" ("Creating the Initial Database"). When given `[node()]`, it creates the schema on the current node. Mnesia is initialized and creates a directory called `Mnesia.<node>` (for example `Mnesia.nonode@nohost` or `Mnesia.joe@doris.myerl.example.com`) to store the database. The schema must be created only once for a given database.

# Prerequisites

- **Mnesia** — The schema is the foundation of an Mnesia database; you must understand what Mnesia is.
- **Node** — `create_schema` takes a list of Erlang nodes; the schema directory is named after the node.

# Key Properties

1. Created by `mnesia:create_schema(NodeList)` where `NodeList` is a list of valid Erlang nodes.
2. Returns `ok` on success.
3. Creates a directory named `Mnesia.<node>` (or at a path given by `erl -mnesia dir`).
4. Created once per database — it is a setup step, not a per-session step.
5. Defines on which nodes the database lives; tables are subsequently placed within it.

# Construction / Recognition

## To Create a Schema:
1. Start an Erlang shell (`erl`, or `erl -name joe` for a named node, or `erl -mnesia dir '...'` for a specific location).
2. Call `mnesia:create_schema([node()])`.
3. Confirm it returns `ok`.
4. Stop the shell with `init:stop()` — the schema persists on disk.

## To Recognize:
1. A `Mnesia.<node>` directory in the working directory or the configured `mnesia dir`.

# Context & Application

Schema creation is the unavoidable first step of using Mnesia.

- **Typical contexts**: One-time database provisioning during deployment or development setup.
- **Common applications**: `mnesia:create_schema([node()])` on a single node; a multi-node list for distributed databases.
- **Historical/stylistic notes**: The directory location can be controlled with the `-mnesia dir` startup flag.

# Examples

**Example 1** ("Creating the Initial Database"): On an unnamed node, the schema directory becomes `Mnesia.nonode@nohost`.

**Example 2** ("Creating the Initial Database"): Pointing to a specific directory at startup.

```erlang
%% started with: erl -mnesia dir '"/home/joe/some/path/to/Mnesia.company"'
1> mnesia:create_schema([node()]).
ok
```

# Relationships

## Builds Upon
- **Mnesia** — The schema is the structural root of an Mnesia database.

## Enables
- **Mnesia table** — Tables can only be created after the schema exists.
- **Distributed Mnesia** — A multi-node node list in the schema enables distribution.

## Related
- **Node** — The schema is bound to a list of nodes.

## Contrasts With
- None.

# Common Errors

- **Error**: Calling `create_schema` every time the application starts.
  **Correction**: Create the schema once; on subsequent starts only call `mnesia:start()`.

- **Error**: Passing node names that are not valid running Erlang nodes.
  **Correction**: `NodeList` must contain valid Erlang nodes.

# Common Confusions

- **Confusion**: Thinking the schema and the tables are the same thing.
  **Clarification**: The schema is the database-level structure on a set of nodes; tables are defined inside it afterward.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Creating the Initial Database".

# Verification Notes

- Definition source: Direct quote from "Creating the Initial Database".
- Confidence rationale: HIGH — the section explicitly defines `create_schema` and its behavior.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
