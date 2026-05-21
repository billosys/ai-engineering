---
# === CORE IDENTIFICATION ===
concept: Distributed Mnesia
slug: distributed-mnesia

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Table Types and Location (Table Behavior)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "replicated Mnesia"
  - "Mnesia replication"
  - "fault-tolerant Mnesia"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table-types
  - node
extends:
  - mnesia
related:
  - mnesia-schema
  - mnesia-table-fragmentation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make Mnesia fault-tolerant?"
  - "How does Mnesia replicate tables across nodes?"
  - "How do I write a distributed Mnesia program?"
---

# Quick Definition

Distributed Mnesia replicates tables across multiple Erlang nodes so the database keeps working when a node crashes. Replicas resynchronize automatically when a crashed node comes back online.

# Core Definition

Mnesia tables can be "replicated on different machines to provide fault-tolerant behavior" (chapter introduction), and can be "configured with RAM replicates on two physically separated nodes to provide a fast fault-tolerant data store". A table is replicated by listing several nodes in a storage option such as `{disc_copies, [node(), someOtherNode()]}`. "When a table is replicated across several Erlang nodes, it is synchronized as far as possible. If one node crashes, the system will still work, but the number of replicas will be reduced. When the crashed node comes back online, it will resynchronize with the other nodes where the replicas are kept" ("Table Behavior").

# Prerequisites

- **Mnesia** — Distributed Mnesia is Mnesia configured across nodes.
- **Mnesia table types** — Replication is expressed through `ram_copies`/`disc_copies`/`disc_only_copies` node lists.
- **Node** — Replicas live on multiple Erlang nodes.

# Key Properties

1. A table is replicated by listing multiple nodes in its storage option.
2. Replicas are synchronized as far as possible across nodes.
3. If a node crashes, the system keeps working with a reduced number of replicas.
4. A returning crashed node resynchronizes with the remaining replicas.
5. A table can use one storage type on one node and a different type on another (e.g. `disc_copies` on one, `ram_copies` on another).
6. RAM replicates on two physically separated nodes give a fast, fault-tolerant store.
7. Disk copies on several nodes survive failure of all nodes.

# Construction / Recognition

## To Build a Distributed Mnesia Database:
1. Create the schema across all participating nodes via `mnesia:create_schema(NodeList)`.
2. Start Mnesia on each node.
3. Create each table with a storage option listing the nodes that should hold replicas, e.g. `{disc_copies, [node(), someOtherNode()]}`.
4. Choose per-node storage types to balance read speed and persistence.
5. Operate normally — replication and resynchronization are handled by Mnesia.

## To Recognize:
1. Look for `create_table` storage options with multiple nodes in the node list.
2. Look for a schema created across more than one node.

# Context & Application

Distributed Mnesia is how Erlang systems get a database that survives machine failure.

- **Typical contexts**: Fault-tolerant data stores for telecom and other always-on systems.
- **Common applications**: RAM replicates on two separated nodes for a fast fault-tolerant store; disk copies on several nodes to survive total node failure.
- **Historical/stylistic notes**: Mnesia may become temporarily overloaded if nodes stop functioning (e.g. a laptop sleeping); the resulting warning messages can be ignored.

# Examples

**Example 1** ("Common Combinations of Table Attributes"): A RAM-resident table on two nodes — lost only if both nodes crash, accessible on either.

```erlang
mnesia:create_table(shop, [Attrs, {ram_copies, [node(), someOtherNode()]}])
```

**Example 2** ("Common Combinations of Table Attributes"): Disk copies on several nodes — survives failure of all nodes.

```erlang
mnesia:create_table(shop, [Attrs, {disc_copies, [node(), someOtherNode()]}])
```

# Relationships

## Builds Upon
- **Mnesia** — Distribution extends a single-node Mnesia database across nodes.

## Enables
- (No card depends on this concept.)

## Related
- **Mnesia schema** — A distributed database has its schema created across multiple nodes.
- **Mnesia table fragmentation** — Fragmentation distributes a single table's fragments across machines.

## Contrasts With
- None.

# Common Errors

- **Error**: Replicating a RAM table on only one node and expecting fault tolerance.
  **Correction**: For fault tolerance, replicate the table on disk or on a second machine.

- **Error**: Treating overload warnings after a node sleep/restart as fatal.
  **Correction**: Mnesia may be temporarily overloaded when nodes stop functioning; those warning messages can be ignored.

# Common Confusions

- **Confusion**: Thinking a crashed node permanently desynchronizes the table.
  **Clarification**: When the node returns, it automatically resynchronizes with the surviving replicas.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", chapter introduction and section "Table Types and Location" ("Common Combinations of Table Attributes" and "Table Behavior").

# Verification Notes

- Definition source: Direct quotes from the chapter introduction and "Table Behavior".
- Confidence rationale: HIGH — replication behavior, crash handling, and resynchronization are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
