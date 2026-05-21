---
# === CORE IDENTIFICATION ===
concept: Mnesia Schema
slug: mnesia-schema

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
section: "9.2.2 Initializing the database"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "schema"
  - "database schema"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
extends: []
related:
  - mnesia-table
  - mnesia-storage-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Mnesia schema?"
  - "How do I create a Mnesia schema?"
  - "Why must every node have its own copy of the schema?"
---

# Quick Definition

A Mnesia schema is the description of which tables exist and their details; every node in a distributed Mnesia database needs its own copy so all nodes know the data's structure.

# Core Definition

A Mnesia schema is a description of the tables that currently exist plus any necessary details about those tables — it is what Mnesia uses to keep track of its data. For a distributed database, all involved nodes must have their own copies of the schema so they all know the general structure of the data. To survive shutting down Mnesia or the whole node and restarting later without losing the database, the schema is normally stored on disk, in the directory given by the `-mnesia dir "..."` option; it is also possible to keep the schema (and tables) in RAM only. A schema is created with `mnesia:create_schema([Node])` before Mnesia is started; it can fail if a node cannot be contacted, if Mnesia is already running on a node, or if a schema already exists. `mnesia:delete_schema(Nodes)` purges an old schema — but this makes any existing tables unreadable (Ch. 9, Section 9.2.2).

# Prerequisites

- **mnesia** — The schema is part of a Mnesia database.

# Key Properties

1. Describes which tables exist and their details.
2. Every node in a distributed database needs its own copy.
3. Normally stored on disk for persistence across restarts; can be RAM-only.
4. Created with `mnesia:create_schema/1` before starting Mnesia.
5. The schema is itself one of Mnesia's tables.
6. `delete_schema/1` purges it and makes existing tables unreadable.

# Construction / Recognition

## To Create a Schema:
1. Start the node with a `-mnesia dir "..."` directory if disk persistence is wanted.
2. Call `mnesia:create_schema([node()])` (or list all nodes) before starting Mnesia.
3. Then call `mnesia:start()`.

## To Recognize:
1. `mnesia:info()` lists `schema` as an active table; it shows the schema's storage type.

# Context & Application

- **Typical contexts**: The first step of initializing any Mnesia database.
- **Common applications**: Persistent project databases; or RAM-only schemas for caches.
- **Historical/stylistic notes**: For the distributed cache, the schema is deliberately kept RAM-only and freely overwritten.

# Examples

**Example 1** (Section 9.2.2): `mnesia:create_schema([node()])` creates an empty schema on the local node.

**Example 2** (Section 9.2.3): `mnesia:info()` shows the schema as a `disc_copies` table — written to disk and mirrored in memory.

# Relationships

## Builds Upon
- **mnesia** — The schema is the structural backbone of a Mnesia database.

## Enables
- **mnesia-table** — Tables are described by the schema.

## Related
- **mnesia-storage-type** — The schema, like any table, has a storage type.

## Contrasts With
- None.

# Common Errors

- **Error**: Calling `mnesia:delete_schema` casually to fix a startup error.
  **Correction**: Think twice — deleting the schema makes all existing tables unreadable.

- **Error**: Trying to create a schema while Mnesia is already running.
  **Correction**: Create the schema before starting Mnesia.

# Common Confusions

- **Confusion**: Thinking the schema only matters on one node.
  **Clarification**: Every node in a distributed Mnesia database needs its own copy of the schema.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.2 "Initializing the database," subsection "Creating the schema."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.2.
- Confidence rationale: HIGH — the book explicitly defines the schema.
- Uncertainties: None.
- Cross-reference status: Verified.
