---
# === CORE IDENTIFICATION ===
concept: sc_store Key-to-Pid Mapping Module
slug: sc-store

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-design
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
  - sc_store
  - "key-to-pid mapping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - cache-system-design
extends: []
related:
  - sc-element
  - ets-match-pattern
  - application-api-module
  - check-the-borders
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the sc_store module?"
  - "How does the cache map keys to storage processes?"
  - "Why is sc_store an abstraction layer over ETS?"
---

# Quick Definition

`sc_store` is the Simple Cache module that maps keys to storage-process pids. It is an abstraction layer — backed by an ETS table — over whatever storage mechanism the cache uses.

# Core Definition

`sc_store` implements the mapping from keys to process identifiers, so the cache can find the value stored for a given key (Ch. 6, Section 6.4.2). It uses an ETS table, but that fact is hidden from the rest of the system: `sc_store` serves as an abstraction layer over whatever storage mechanism is used (it could equally be a `gen_server`, a file, or a database). Unlike the other cache modules, `sc_store` implements no OTP behaviour and has no associated process — it is just a set of library functions. Its API is `init/0` (creates a `public`, `named_table` ETS table), `insert/2` (creates or updates a mapping via `ets:insert/2`), `lookup/1` (returns `{ok, Pid}` or `{error, not_found}`, hiding the raw ETS return value), and `delete/1` (deletes by pid using `ets:match_delete/2` with the pattern `{'_', Pid}`). `sc_store:init/0` is called from the application behaviour module `sc_app` so the table exists before the supervisor runs.

# Prerequisites

- **ETS** — `sc_store` is backed by an ETS table.
- **Process-per-value cache design** — `sc_store` provides the key-to-pid half of the design.

# Key Properties

1. Maps cache keys to storage-process pids.
2. An abstraction layer hiding the storage mechanism (ETS) from the rest of the system.
3. Implements no OTP behaviour and has no associated process — just library functions.
4. API: `init/0`, `insert/2`, `delete/1`, `lookup/1` (the CRUD operations).
5. `init/0` creates a `public`, `named_table` ETS table named after the module.
6. `init/0` is called from `sc_app` so the table exists before the supervisor starts.
7. `lookup/1` translates ETS results into `{ok, Pid}` / `{error, not_found}`.

# Construction / Recognition

## To Implement sc_store:
1. Write a plain module (no behaviour) exporting `init/0`, `insert/2`, `delete/1`, `lookup/1`.
2. `init/0` calls `ets:new(?TABLE_ID, [public, named_table])`.
3. `insert/2` calls `ets:insert/2` (creates or updates — the table is a set).
4. `lookup/1` calls `ets:lookup/2` and maps the result to `{ok, Pid}` / `{error, not_found}`.
5. `delete/1` calls `ets:match_delete/2` with the pattern `{'_', Pid}`.
6. Call `sc_store:init/0` from `sc_app:start/2`.

# Context & Application

`sc_store` decouples the cache from its storage choice — ETS could be swapped for a database with no change to the rest of the application.

- **Typical contexts**: The lookup layer of the Simple Cache, on the critical path of every cache access.
- **Common applications**: Resolving a URL key to the `sc_element` pid holding the cached listing.

# Examples

**Example 1** (Ch. 6, Listing 6.6): `sc_store:lookup/1` pattern-matches the `ets:lookup/2` result — `[{Key, Pid}]` yields `{ok, Pid}`, `[]` yields `{error, not_found}`.

**Example 2** (Ch. 6): `sc_store:delete/1` calls `ets:match_delete(?TABLE_ID, {'_', Pid})`, deleting the entry by value (pid) rather than by key.

# Relationships

## Related
- **ets** — `sc_store` is backed by an ETS table.
- **ets-match-pattern** — `delete/1` uses an ETS match pattern.
- **sc-element** — `sc_element:terminate/2` calls `sc_store:delete/1`.
- **application-api-module** — `simple_cache` uses `sc_store:lookup/1` to find storage processes.
- **check-the-borders** — `sc_store:insert/2` deliberately does no type checking, trusting internal callers.

## Contrasts With
- This card has no direct contrast within the source's treatment.

# Common Errors

- **Error**: Initializing `sc_store` after starting the supervisor.
  **Correction**: Initialize it in `sc_app:start/2` so the ETS table exists before anything tries to access it.

- **Error**: Leaking raw ETS return values to callers.
  **Correction**: Translate them into `{ok, Pid}` / `{error, not_found}` — the ETS backing is incidental.

# Common Confusions

- **Confusion**: Thinking `sc_store` is a process or a `gen_server`.
  **Clarification**: It is just a set of library functions with no associated process and no behaviour.

# Source Reference

Chapter 6: Implementing a caching system, Section 6.4.2 "Implementing the sc_store module," Listing 6.6 and the "First things first" and "Match patterns" sidebars.

# Verification Notes

- Definition source: Direct adaptation of Section 6.4.2.
- Confidence rationale: HIGH — explicit, worked treatment with full code listing.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
