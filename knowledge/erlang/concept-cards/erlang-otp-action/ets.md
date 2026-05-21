---
# === CORE IDENTIFICATION ===
concept: ETS (Erlang Term Storage)
slug: ets

# === CLASSIFICATION ===
category: performance
subcategory: in-memory-storage
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.4.2 Implementing the sc_store module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ETS
  - "Erlang Term Storage"
  - ets table

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - sc-store
  - ets-match-pattern
  - tv-table-viewer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ETS?"
  - "When should you use an ETS table?"
  - "How do you create and access an ETS table?"
---

# Quick Definition

ETS (Erlang Term Storage) provides fast, in-memory hash tables for Erlang data, implemented in C as part of the runtime system and accessed via built-in functions.

# Core Definition

ETS tables are fast, in-memory hash tables for Erlang data (Ch. 6, Section 6.4.2). They are implemented in C as part of the Erlang Run-Time System (ERTS) and are accessed using a set of built-in Erlang functions. Every entry must be a tuple, where one of the tuple columns (normally the first or second) is the key. ETS tables are particularly useful for data that: does not need to be shared between virtual machines; needs to be persistent only as long as the VM is alive; may need to be shared by several processes on the VM; needs fast access times; and is mainly flat, without foreign-key relationships. A table is created with `ets:new/2`; it can be accessed via the table handle it returns, or — if created with the `named_table` option — by its name. The default table type is a *set*: at most one entry per key, and key lookup is a fast constant-time operation.

# Prerequisites

- **Erlang module** — ETS is used through built-in functions called from modules.

# Key Properties

1. Fast, in-memory hash tables, implemented in C as part of ERTS.
2. Every entry is a tuple; one column is the key.
3. Created with `ets:new/2`; accessed by handle, or by name if `named_table`.
4. The `public` option allows access by any process.
5. The default type is a *set*: one entry per key, constant-time key lookup.
6. Data persists only while the VM is alive; not shared between VMs.

# Construction / Recognition

## To Use ETS:
1. Create a table with `ets:new(Name, Options)` (e.g. `[public, named_table]`).
2. Insert tuples with `ets:insert/2`.
3. Look up by key with `ets:lookup/2`.
4. Delete by pattern with `ets:match_delete/2` or by key with `ets:delete/2`.

# Context & Application

ETS suits in-memory, VM-lifetime data shared across processes — exactly a cache's key-to-pid mapping.

- **Typical contexts**: Caches, registries, shared lookup tables.
- **Common applications**: The `sc_store` module backs the cache's key-to-pid mapping with a `public`, `named_table` ETS table.

# Examples

**Example 1** (Ch. 6, Listing 6.6): `sc_store:init/0` calls `ets:new(?TABLE_ID, [public, named_table])` to create the key-to-pid mapping table.

**Example 2** (Ch. 6): `ets:lookup(?TABLE_ID, Key)` returns a list of matching tuples — one or none, because the table is a set.

# Relationships

## Related
- **sc-store** — `sc_store` is an ETS-backed abstraction layer.
- **ets-match-pattern** — Match patterns are used with ETS functions like `match_delete/2`.
- **tv-table-viewer** — TV can display ETS tables graphically.

## Contrasts With
- This card has no direct contrast within the source's treatment (Mnesia is mentioned but out of scope here).

# Common Errors

- **Error**: Inserting non-tuple values into an ETS table.
  **Correction**: Every ETS entry must be a tuple, with one column serving as the key.

- **Error**: Relying on a non-`named_table` ETS table by name.
  **Correction**: Only tables created with `named_table` can be accessed by name; otherwise use the handle.

# Common Confusions

- **Confusion**: Thinking ETS data persists across VM restarts.
  **Clarification**: ETS data lives only as long as the VM; it is not persistent storage like a database.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.4.2 "Implementing the sc_store module," Listing 6.6. ETS is introduced earlier in Chapter 2, Section 2.14 (out of this chapter group's scope).

# Verification Notes

- Definition source: Direct adaptation of the ETS recap in Section 6.4.2.
- Confidence rationale: HIGH — the chapter explicitly recaps and defines ETS where `sc_store` uses it.
- Uncertainties: Full ETS table types and Chapter 2's deeper treatment are out of this chapter group's scope.
- Cross-reference status: References Agent-1 slug `erlang-module` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed. ETS introduced here per assignment.
