---
# === CORE IDENTIFICATION ===
concept: Integrating HBase with the Simple Cache
slug: cache-hbase-integration

# === CLASSIFICATION ===
category: distribution
subcategory: foreign-integration
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Communication between Erlang and Java via Jinterface"
chapter_number: 13
pdf_page: null
section: "13.4. Integrating HBase with Simple Cache"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cache write-through to HBase"
  - "cache-aside with HBase"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-hbase-bridge
  - sc-hbase-protocol
extends: []
related:
  - hbase-integration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are the cache's lookup, insert, and delete functions changed to use HBase?"
  - "Why does ordering matter when integrating the cache with HBase?"
  - "How does a cache miss fall back to HBase?"
---

# Quick Definition

The Simple Cache is integrated with HBase by modifying only `simple_cache.erl`: `lookup` falls back to HBase on a miss, while `insert` and `delete` write through to HBase as well.

# Core Definition

To make the Simple Cache use the Erlang-HBase bridge, only the front-end module `simple_cache.erl` needs changing, because the cache code is well-structured. `lookup/1` is modified to look the key up in HBase only when it cannot be found locally; if HBase has it, the entry is inserted into the cache to speed up the next lookup, using `try`/`catch` to report `not_found` on failure. `insert/2` adds a call to `sc_hbase:put/2` so each inserted entry is also written to HBase. `delete/1` adds a call to `sc_hbase:delete/2`. The HBase node name is fixed once via `-define(HBASE_NODE, 'hbase@localhost')`. Operation ordering matters to avoid race conditions with concurrent operations (Chapter 13, Section 13.4, Listing 13.5).

# Prerequisites

- **Erlang-HBase bridge** — Provides `sc_hbase:put/get/delete` used by the cache.
- **sc_hbase protocol** — Defines how those calls reach HBase.

# Key Properties

1. Only `simple_cache.erl` changes; the rest of the cache is untouched.
2. The HBase node name is centralized in the `HBASE_NODE` macro.
3. `lookup/1`: try local store first; on a miss, query HBase; if found, insert into the cache and return; uses `try`/`catch` for `not_found`.
4. `insert/2`: add the cache entry, then call `sc_hbase:put/2` — write-through ordering.
5. `delete/1`: call `sc_hbase:delete/2` before removing the entry from the cache.
6. Ordering rules prevent a concurrent lookup from re-populating a value that is being deleted, or finding a stale miss.

# Construction / Recognition

## To Construct/Create:
1. Add `-define(HBASE_NODE, 'hbase@localhost').` after the export declaration.
2. Modify `lookup/1` to query HBase on a local miss and cache the result.
3. Modify `insert/2` to call `sc_hbase:put/2` after creating the cache entry.
4. Modify `delete/1` to call `sc_hbase:delete/2` before removing the cache entry.

# Context & Application

- **Typical contexts**: Adding a durable backing store to an existing in-memory cache.
- **Common applications**: The Simple Cache becomes a fast front end to HBase; lookups read only the cache when possible, writes always reach HBase.
- **Historical/stylistic notes**: The book leaves making `HBASE_NODE` a proper configurable parameter as an exercise.

# Examples

**Example 1** (Listing 13.5): The new `simple_cache:lookup/1` falls back to HBase when the local lookup fails and inserts the found value into the cache.

**Example 2** (Section 13.5): A shell session shows key `17` inserted directly into HBase; a later cache lookup finds it in HBase and stores it in the cache, so the next lookup hits the cache.

# Relationships

## Related
- **HBase as a backing store** — The store the cache reads from and writes through to.

# Common Errors

- **Error**: Calling `sc_hbase:put/2` before creating the cache entry on insert.
  **Correction**: Insert into the cache first; otherwise a concurrent lookup could miss the cache but find HBase, creating a race.

- **Error**: Removing the cache entry before deleting from HBase.
  **Correction**: Delete from HBase first; otherwise a concurrent lookup could re-populate the cache from HBase before the HBase delete completes.

# Common Confusions

- **Confusion**: Thinking lookups always hit HBase.
  **Clarification**: Lookups consult HBase only on a local cache miss; writes always touch HBase.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.4 "Integrating HBase with Simple Cache" (13.4.1-13.4.3), Listing 13.5; running example in Section 13.5.

# Verification Notes

- Definition source: Direct adaptation of Section 13.4 and Listing 13.5.
- Confidence rationale: HIGH — the integration steps and ordering rationale are explicit.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
