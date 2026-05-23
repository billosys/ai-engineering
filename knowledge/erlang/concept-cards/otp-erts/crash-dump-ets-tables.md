---
concept: Crash Dump ETS and Distribution Info
slug: crash-dump-ets-tables
category: production-ops
subcategory: crash-dumps
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Interpret the Erlang Crash Dumps"
chapter_number: null
pdf_page: null
section: "ETS Tables"
extraction_confidence: high
aliases:
  - "crash dump ETS section"
  - "crash dump distribution section"
prerequisites:
  - crash-dump
extends:
  - crash-dump
related:
  - crash-dump-process-info
  - crash-dump-slogans
contrasts_with: []
answers_questions:
  - "How do I interpret an Erlang crash dump?"
  - "How do I find ETS table information in a crash dump?"
  - "How do I interpret distribution information in a crash dump?"
---

# Quick Definition

The ETS tables and distribution sections of a crash dump reveal the state of all ETS tables (owners, sizes, types, concurrency settings) and all distributed Erlang connections (visible/hidden nodes, monitors, links) at the time of the crash. Large ETS tables are a common cause of memory exhaustion crashes.

# Core Definition

## ETS Tables Section

Each ETS table is listed under the tag `=ets:<owner>`, where `<owner>` is the owning process identifier. Key fields include (Ericsson AB, "How to Interpret the Erlang Crash Dumps," section "ETS Tables"):

- **Table**: The table identifier; if it is a `named_table`, this is the name
- **Name**: The table name regardless of `named_table` setting
- **Objects**: The number of objects in the table
- **Words**: The number of words allocated to data in the table
- **Type**: `set`, `bag`, `duplicate_bag`, or `ordered_set`
- **Hash table, Buckets**: Present for hash tables (not `ordered_set`)
- **Hash table, Chain Length**: Statistics including max, min, and average chain length. A maximum much larger than the average with a high standard deviation indicates poor hashing behavior
- **Ordered set (AVL tree), Elements**: Present for `ordered_set` tables
- **Fixed**: Whether the table is fixed via `ets:safe_fixtable/2`
- **Compressed**: Whether the table was compressed
- **Protection**: The table's protection level
- **Write Concurrency / Read Concurrency**: Whether these options were enabled

## Distribution Section

If the node was distributed, this section lists active connections:

- `=visible_node:<channel>`: A connected visible node
- `=hidden_node:<channel>`: A connected hidden node (started with `-hidden`)
- `=not_connected:<channel>`: A previously connected node with remaining references
- Fields include: **Name**, **Controller** (port), **Creation** (1-3, with node name identifies a specific instance)
- Monitor and link information: `Remote monitoring`, `Remotely monitored by`, and `Remote link` entries with local and remote process identifiers

# Prerequisites

- **crash-dump** -- Understanding crash dump structure and navigation

# Key Properties

1. ETS tables are indexed by owner pid in the crash dump
2. The `Words` field indicates memory consumption per table
3. High `Objects` counts combined with high `Words` values indicate memory-heavy tables
4. Hash table chain length statistics can reveal pathological hashing behavior
5. `Fixed` tables retain deleted objects until unfixed, which can cause unexpected memory growth
6. Distribution information is only present if the node was distributed (alive)
7. `not_connected` entries indicate nodes that were previously connected but references (pids, ports) still exist
8. The `Creation` field (1-3) disambiguates different incarnations of the same node name

# Construction / Recognition

## Finding Memory-Heavy ETS Tables

1. Look for `=ets:` tags in the crash dump
2. Check the `Words` field -- this is the most direct measure of memory consumed by table data
3. Compare `Objects` count with expected table sizes
4. Check `Type` -- `duplicate_bag` tables can grow unexpectedly
5. Check `Fixed` -- fixed tables accumulate deleted objects

## Diagnosing Distribution Issues

1. Look for `=node:` to confirm the node was distributed
2. Check `=visible_node:` and `=hidden_node:` for active connections at crash time
3. Check `=not_connected:` for stale references that may indicate connection problems
4. Review `Remote monitoring` and `Remote link` entries for cross-node dependency failures

# Context & Application

ETS table analysis is critical when the crash dump slogan indicates memory exhaustion. Common scenarios:

- A table accumulating data without cleanup (growing `Objects` and `Words`)
- A fixed table that was never unfixed, retaining all deleted objects
- Poor hash distribution causing performance degradation (chain length anomalies)
- Application-specific caches or state tables growing without bounds

Distribution information is important when investigating:

- Node name conflicts (common cause of `Kernel pid terminated` slogans)
- Network partitions and their effects on monitors/links
- Orphaned references to disconnected nodes

# Examples

**ETS table fields in a crash dump** (source: "How to Interpret the Erlang Crash Dumps," section "ETS Tables"):

A hash table entry might show:
- `Hash table, Buckets`: The number of hash buckets
- `Hash table, Chain Length`: max, min, average, standard deviation
- Having a maximum chain length "much larger than the average, and a standard deviation much larger than the expected standard deviation is a sign that the hashing of the terms behaves badly"

**Distribution node types** (source: section "Distribution Information"):

- `=visible_node:3` -- A visible connected node on channel 3
- `=hidden_node:5` -- A hidden connected node on channel 5 (started with `-hidden`)
- `=not_connected:7` -- A previously connected node whose references (pids/ports) still exist

# Relationships

## Extends

- **crash-dump** -- ETS and distribution sections are specific parts of the crash dump

## Related

- **crash-dump-process-info** -- ETS table owners can be correlated with process information to understand which processes are responsible for table growth
- **crash-dump-slogans** -- Memory allocation slogans often point to ETS table issues

# Common Errors

- **Error**: Only checking process memory and ignoring ETS tables in memory exhaustion crashes
  **Correction**: ETS tables can consume significant memory independently of process heaps; always check the ETS section

- **Error**: Ignoring the `Fixed` field
  **Correction**: Fixed tables retain deleted objects, which can cause memory to grow even when the application believes it is cleaning up

# Common Confusions

- **Confusion**: The `Table` and `Name` fields are always the same
  **Clarification**: They differ when the table is not a `named_table` -- `Table` shows the identifier (a reference), while `Name` shows the name passed to `ets:new/2`

- **Confusion**: `not_connected` nodes indicate an error
  **Clarification**: They simply indicate that references (pids, ports) to a previously connected node still exist in the system, which is normal during or after disconnection

# Source Reference

"How to Interpret the Erlang Crash Dumps," sections "ETS Tables" and "Distribution Information." The source lists all ETS table fields including hash statistics and concurrency settings, and all distribution fields including node types, controller ports, creation values, and remote monitor/link entries.

# Verification Notes

- All ETS fields: Directly listed and described in source section "ETS Tables"
- Hash chain length pathology sign: Directly quoted from source
- All distribution node types (visible, hidden, not_connected): Directly from source
- Creation field range (1-3): Directly stated in source
- Remote monitoring/link format: Directly from source
- Confidence: HIGH -- all content directly from official ERTS documentation
