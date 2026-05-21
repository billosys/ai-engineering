---
# === CORE IDENTIFICATION ===
concept: Mnesia Table Types and Storage
slug: mnesia-table-types

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
section: "Table Types and Location"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ram_copies"
  - "disc_copies"
  - "disc_only_copies"
  - "table storage types"
  - "RAM and disk tables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - node
extends: []
related:
  - distributed-mnesia
  - mnesia-table-fragmentation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Mnesia table storage types?"
  - "What is the difference between ram_copies, disc_copies, and disc_only_copies?"
  - "How do I make an Mnesia table fault-tolerant?"
---

# Quick Definition

Mnesia tables can be stored in RAM, on disk, or both, and can be placed on one node or replicated across several. The storage options `ram_copies`, `disc_copies`, and `disc_only_copies` control speed, persistence, and fault tolerance.

# Core Definition

"We can configure Mnesia tables in many different ways. First, tables can be in RAM or on disk (or both). Second, tables can be located on a single machine or replicated on several machines" ("Table Types and Location"). RAM tables are very fast but transient — their data is lost on crash or DBMS stop. Disk tables survive a crash: transaction data is first written to a continuously growing disk log, periodically consolidated with the rest of the database; on restart the disk log is checked for consistency and outstanding entries are applied. The storage type is chosen via `create_table` options:

- `{ram_copies, NodeList}` — RAM copies on the listed nodes.
- `{disc_copies, NodeList}` — disk copies on the listed nodes; the system also creates a RAM copy on the node where the operation is performed.
- `{disc_only_copies, NodeList}` — disk-only copies with no RAM replica; slower to access.

# Prerequisites

- **Mnesia** — Storage types are an Mnesia configuration concept.
- **Mnesia table** — These options are passed when creating a table.
- **Node** — Each storage option takes a list of nodes where copies are stored.

# Key Properties

1. RAM tables are the fastest but transient — they must fit in physical memory.
2. `disc_copies` keeps both a RAM copy and a disk copy: fast reads, slower writes, recoverable after a crash.
3. `disc_only_copies` has no RAM replica: used for tables too large to fit in memory; slower access.
4. The table `{type, Type}` is one of `set`, `ordered_set`, or `bag` (same meaning as ETS table types).
5. Tables can be replicated on multiple nodes by listing several nodes in the storage option.
6. A table can be `disc_copies` on one node and a different storage type on another.
7. When a replicated table's node crashes, the system keeps working with fewer replicas; the node resynchronizes when it returns.

# Construction / Recognition

## To Choose a Storage Type:
1. Decide whether data must survive a crash — if not, `ram_copies` is fastest.
2. Decide whether the whole table fits in memory — if not, use `disc_only_copies`.
3. For fast reads plus persistence, use `disc_copies` (RAM + disk).
4. For fault tolerance, list multiple nodes in the chosen storage option.
5. Pass the option to `mnesia:create_table/2`, e.g. `{disc_copies, [node()]}`.

## To Recognize:
1. Look at the `create_table` option list for `ram_copies`, `disc_copies`, or `disc_only_copies` tuples.

# Context & Application

Storage-type selection is the central design decision for an Mnesia table.

- **Typical contexts**: Tuning a table for speed (RAM), durability (disk), or size (disk-only).
- **Common applications**: A single-node RAM table for transient cache data; `disc_copies` on multiple nodes for fault-tolerant persistent data.
- **Historical/stylistic notes**: For a fault-tolerant application, a RAM table should be replicated onto disk or onto a second machine.

# Examples

**Example 1** ("Common Combinations of Table Attributes"): A RAM-resident table on a single node — fastest, lost on crash, must fit in memory.

```erlang
mnesia:create_table(shop, [Attrs])
```

**Example 2** ("Common Combinations of Table Attributes"): Disk copies on several nodes — survives failure of all nodes.

```erlang
mnesia:create_table(shop, [Attrs, {disc_copies, [node(), someOtherNode()]}])
```

## Worked Example

From "Common Combinations of Table Attributes", a single-node RAM + disk table:

```erlang
mnesia:create_table(shop, [Attrs, {disc_copies, [node()]}])
```

This makes a RAM-resident table plus a disk copy on one node: recovered from disk after a crash, fast reads, slower writes, and the table should fit in memory.

# Relationships

## Builds Upon
- **Mnesia table** — Storage types are options applied when a table is created.

## Enables
- **Distributed Mnesia** — Replicating storage across multiple nodes is what makes Mnesia distributed.
- **Mnesia table fragmentation** — Fragments are themselves tables with their own storage types.

## Related
- **Node** — Storage options are lists of nodes.

## Contrasts With
- None — the three storage types are complementary points on a speed/persistence trade-off.

# Common Errors

- **Error**: Using a RAM table for data that must survive a crash.
  **Correction**: Use `disc_copies` or replicate the RAM table onto disk or another machine.

- **Error**: Loading a huge `ram_copies` table that does not fit in physical memory.
  **Correction**: Experiment first; if the table will not fit, use `disc_only_copies`, otherwise the system pages heavily and performance suffers.

# Common Confusions

- **Confusion**: Believing `disc_copies` stores data only on disk.
  **Clarification**: `disc_copies` keeps both a RAM copy and a disk copy; only `disc_only_copies` has no RAM replica.

- **Confusion**: Thinking a replicated table is unavailable if one node crashes.
  **Clarification**: The system keeps working with fewer replicas and resynchronizes the crashed node when it returns.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Table Types and Location", including "Creating Tables", "Common Combinations of Table Attributes", and "Table Behavior".

# Verification Notes

- Definition source: Direct quotes from "Table Types and Location" and "Creating Tables".
- Confidence rationale: HIGH — the three storage types and their trade-offs are explicitly enumerated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
