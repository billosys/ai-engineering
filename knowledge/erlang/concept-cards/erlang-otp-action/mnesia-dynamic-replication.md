---
# === CORE IDENTIFICATION ===
concept: Mnesia Dynamic Table Replication
slug: mnesia-dynamic-replication

# === CLASSIFICATION ===
category: distribution
subcategory: mnesia
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.3.4 Bringing the Mnesia tables into dynamic replication"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dynamic table replication"
  - "mnesia:change_config"
  - "mnesia:add_table_copy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - resource-discovery
extends: []
related:
  - distributed-cache
  - mnesia-schema
  - cluster-contact-node
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Mnesia dynamically replicate tables across discovered nodes?"
  - "How does a new node connect to and copy from an existing Mnesia node?"
  - "Why must one Mnesia node be started first?"
---

# Quick Definition

Mnesia dynamic table replication is the runtime process by which a freshly started node — guided by resource discovery — connects to an existing Mnesia node, copies its schema and tables, and joins the replication set.

# Core Definition

Mnesia dynamic table replication is the technique that lets discovered cache instances replicate data across one another with almost no static configuration (Ch. 9, Section 9.3.4). The cache's `sc_store:init/0`, run after the node is connected to the cluster and resource discovery has populated its cache, fetches the list of `simple_cache` instances and passes the others to `dynamic_db_init/1`. If no other instances are found, the node simply creates the table and an implicit RAM-only schema — it becomes a working instance ready to replicate to others that join later. If other instances are found, `add_extra_nodes/1` loops over them: it calls `mnesia:change_config/2` to add an extra node to the database (Mnesia, like Erlang nodes, informs all members of each other when one connects), then copies the remote schema to the local node (replacing the temporary empty one), copies the `key_to_pid` table, and calls `mnesia:wait_for_tables/2` to await full synchronization. An important caveat: the initial node must be started alone, or two nodes starting simultaneously create a race where neither creates the initial schema.

# Prerequisites

- **mnesia** — Replication is a Mnesia feature.
- **mnesia-table** — Tables are the unit being replicated.
- **resource-discovery** — Discovery supplies the list of nodes to replicate with.

# Key Properties

1. Brings discovered nodes into a shared Mnesia replication set at runtime.
2. A lone node creates its own table and implicit RAM-only schema.
3. A joining node uses `mnesia:change_config/2` to add an existing node.
4. The joining node copies the remote schema and tables locally.
5. `mnesia:wait_for_tables/2` awaits synchronization before proceeding.
6. The initial node must start alone to avoid a schema-creation race.

# Construction / Recognition

## To Set Up Dynamic Replication:
1. After joining the cluster, fetch peer instances via resource discovery.
2. If alone, create the table and rely on an implicit RAM-only schema.
3. If peers exist, `mnesia:change_config(extra_db_nodes, [Node])` to connect to one.
4. Copy the schema and target table to the local node.
5. `mnesia:wait_for_tables/2` to await full synchronization.

## To Recognize:
1. Startup code calling `mnesia:change_config/2` and copying schema/tables from discovered nodes.

# Context & Application

- **Typical contexts**: Dynamically scaling a replicated Mnesia-backed service.
- **Common applications**: The distributed cache replicating its `key_to_pid` table across instances.
- **Historical/stylistic notes**: If connecting to a peer fails, the code tries the next; running out of nodes crashes startup — a deliberate "let it crash."

# Examples

**Example 1** (Section 9.3.4, Listing 9.7): `dynamic_db_init([])` creates the `key_to_pid` table when alone; `dynamic_db_init(CacheNodes)` calls `add_extra_nodes/1` to replicate when peers exist.

**Example 2** (Section 9.3.4, Listing 9.8): `add_extra_nodes/1` calls `mnesia:change_config/2` to add a node, copies the remote schema and `key_to_pid` table locally, then calls `mnesia:wait_for_tables/2`.

# Relationships

## Builds Upon
- **mnesia** — Replication is a Mnesia capability.
- **mnesia-table** — Tables are replicated across nodes.
- **resource-discovery** — Discovery provides the nodes to replicate with.

## Enables
- None.

## Related
- **distributed-cache** — Dynamic replication is the final step in distributing the cache.
- **mnesia-schema** — A new node copies the remote schema, replacing its empty one.
- **cluster-contact-node** — The node first joins the cluster via contact nodes.

## Contrasts With
- None.

# Common Errors

- **Error**: Starting two fresh `simple_cache` nodes simultaneously.
  **Correction**: Start the initial node alone; simultaneous starts race so that no initial schema is ever created.

# Common Confusions

- **Confusion**: Thinking the new node must already hold data to connect.
  **Clarification**: A new, empty RAM-based node with an empty schema initiates the connection and then copies the existing node's schema and tables.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.3.4 "Bringing the Mnesia tables into dynamic replication," Listings 9.7 and 9.8, and the "One node must be started first" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 9.3.4.
- Confidence rationale: HIGH — the book walks through the replication code in detail.
- Uncertainties: None.
- Cross-reference status: Verified.
