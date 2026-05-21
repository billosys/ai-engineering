---
# === CORE IDENTIFICATION ===
concept: Mnesia Storage Type
slug: mnesia-storage-type

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
  - "ram_copies"
  - "disc_copies"
  - "disc_only_copies"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia-table
extends: []
related:
  - mnesia-table-type
  - mnesia-schema
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What storage types can a Mnesia table have?"
  - "What is the difference between ram_copies, disc_copies, and disc_only_copies?"
  - "Can a table have different storage types on different nodes?"
---

# Quick Definition

A Mnesia storage type determines where a table's data is kept: `ram_copies` (memory only), `disc_copies` (disk plus a memory mirror), or `disc_only_copies` (disk only).

# Core Definition

A Mnesia storage type controls where a table's data resides (Ch. 9, Section 9.2.3). The three types are: `ram_copies` — the table is stored only in memory, offering the highest performance, but the data is not persistent and is lost on a crash or restart (this is the default); `disc_copies` — the table is written to disk for persistence and survives restarts, and is also fully mirrored in memory for fast read access; `disc_only_copies` — the table is stored only on disk, and accesses are a lot slower than for the other types (the `ordered_set` table type is not supported for disk-only tables). A table can have different storage types on different nodes — for example kept on disk on one node but in RAM on the others — and this configuration can be altered at runtime without stopping the system, though typically the storage type is decided when tables are created.

# Prerequisites

- **mnesia-table** — The storage type is a per-table, per-node setting.

# Key Properties

1. `ram_copies`: memory only; fastest; not persistent (the default).
2. `disc_copies`: disk-backed and memory-mirrored; survives restarts.
3. `disc_only_copies`: disk only; slowest; no `ordered_set` support.
4. A table may use different storage types on different nodes.
5. The storage type can be changed at runtime without stopping the system.

# Construction / Recognition

## To Choose a Storage Type:
1. Use `ram_copies` for fast, non-persistent runtime data (the default).
2. Use `disc_copies` for persistent data that still needs fast reads.
3. Use `disc_only_copies` for large data where memory is constrained and slower access is acceptable.

## To Recognize:
1. `mnesia:info()` lists which tables are `ram_copies`, `disc_copies`, or `disc_only_copies`.

# Context & Application

- **Typical contexts**: Deciding persistence vs. performance for each table.
- **Common applications**: RAM-only cache tables; disk-backed project databases.
- **Historical/stylistic notes**: The schema itself has a storage type — typically `disc_copies` for a persistent database, but RAM-only for the cache.

# Examples

**Example 1** (Section 9.2.3): After `init_tables()`, `mnesia:info()` shows the application's tables as `ram_copies` (memory only) and the schema as `disc_copies` (disk plus memory mirror).

**Example 2** (Section 9.3.4): The distributed cache keeps all its data — including the schema — as `ram_copies`.

# Relationships

## Builds Upon
- **mnesia-table** — Storage type is a property of a table on a node.

## Enables
- None.

## Related
- **mnesia-table-type** — An orthogonal table property (set/ordered_set/bag).
- **mnesia-schema** — The schema also has a storage type.

## Contrasts With
- None.

# Common Errors

- **Error**: Relying on `ram_copies` data surviving a node restart.
  **Correction**: `ram_copies` data is lost on crash/restart; use `disc_copies` for persistence.

# Common Confusions

- **Confusion**: Thinking storage type must be the same on every node.
  **Clarification**: A table can have different storage types per node, and the type can change at runtime.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2.3 "Creating the tables," subsection "Storage types for tables."

# Verification Notes

- Definition source: Directly adapted from Section 9.2.3.
- Confidence rationale: HIGH — the book explicitly defines all three storage types.
- Uncertainties: None.
- Cross-reference status: Verified.
