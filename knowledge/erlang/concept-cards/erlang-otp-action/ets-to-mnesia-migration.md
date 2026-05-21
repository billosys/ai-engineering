---
# === CORE IDENTIFICATION ===
concept: Switching from ETS to Mnesia
slug: ets-to-mnesia-migration

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
section: "9.3.1 Switching from ETS to Mnesia"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ETS to Mnesia conversion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - ets
extends: []
related:
  - mnesia-index
  - mnesia-dirty-operation
  - distributed-cache
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I switch a storage module from ETS to Mnesia?"
  - "Why does encapsulating the store make the migration easy?"
  - "What complication arises when looking up pids in a distributed Mnesia store?"
---

# Quick Definition

Switching from ETS to Mnesia means re-implementing a storage module's `init`, `insert`, `lookup`, and `delete` functions on Mnesia instead of ETS — possible without touching the rest of the codebase because the store is encapsulated behind that module.

# Core Definition

Switching from ETS to Mnesia is the conversion of a storage module from ETS-backed tables to Mnesia-backed tables. In the book the `sc_store` module encapsulates the cache's key-to-pid table, hiding the storage implementation from the rest of the code; this encapsulation means the data storage can be completely re-implemented with no changes outside `sc_store`. The four key functions are converted: `init/0` calls `mnesia:start()` and `mnesia:create_table/2` (with an index on `pid`); `insert/2` uses `mnesia:dirty_write/1`; `lookup/1` uses `mnesia:dirty_read/2`; and `delete/1` uses the index-aware `mnesia:dirty_index_read/3`. A distributed-setting complication arises in `lookup/1`: the pid stored in Mnesia could refer to a process on a node that has since died, so the lookup must check whether the pid is still alive (with a helper `is_pid_alive/1` that uses `is_process_alive` locally or `rpc:call` remotely) and treat a stale pid as `not_found` (Ch. 9, Section 9.3.1).

# Prerequisites

- **mnesia** — The migration moves the store onto Mnesia.
- **ets** — The store originally used ETS.

# Key Properties

1. Re-implements `init`, `insert`, `lookup`, `delete` on Mnesia.
2. Possible without changing code outside the encapsulating storage module.
3. `init/0` starts Mnesia and creates the table; `insert`/`lookup` use dirty operations.
4. `delete/1` uses `dirty_index_read/3` to find an entry by pid.
5. The Mnesia table is a RAM-only `set` with unique keys.
6. Distributed lookups must guard against pids referring to dead processes.

# Construction / Recognition

## To Switch a Store from ETS to Mnesia:
1. Confirm the store is encapsulated behind a module with `init`/`insert`/`lookup`/`delete`.
2. Rewrite `init/0` to `mnesia:start()` and `mnesia:create_table/2`.
3. Rewrite `insert`/`lookup`/`delete` using `dirty_write`, `dirty_read`, `dirty_index_read`.
4. Add a liveness check in `lookup` so stale pids return `not_found`.

## To Recognize:
1. A storage module whose four functions were swapped from `ets:*` to `mnesia:*` calls.

# Context & Application

- **Typical contexts**: Making a single-node store distributable.
- **Common applications**: Converting the Simple Cache's `sc_store` to Mnesia.
- **Historical/stylistic notes**: The encapsulation introduced in chapter 6 is what makes the migration painless.

# Examples

**Example 1** (Section 9.3.1): The ETS `init/0` (`ets:new(?TABLE_ID, [public, named_table])`) becomes a Mnesia `init/0` calling `mnesia:start()` and `mnesia:create_table(key_to_pid, [{index, [pid]}, {attributes, record_info(fields, key_to_pid)}])`.

**Example 2** (Section 9.3.1): `lookup/1` adds an `is_pid_alive(Pid)` check so a pid for a process on a now-dead node is treated as `{error, not_found}`.

# Relationships

## Builds Upon
- **mnesia** — The store is moved onto Mnesia.
- **ets** — The starting point of the migration.

## Enables
- None.

## Related
- **mnesia-index** — `delete/1` relies on a pid index.
- **mnesia-dirty-operation** — The converted functions use dirty operations.
- **distributed-cache** — The migration is step one of distributing the cache.

## Contrasts With
- None.

# Common Errors

- **Error**: Returning a looked-up pid without checking it is alive in a distributed setting.
  **Correction**: Verify the pid (e.g., `is_pid_alive/1`); treat a stale pid as `not_found`.

# Common Confusions

- **Confusion**: Thinking switching storage backends requires changes throughout the codebase.
  **Clarification**: If the store is properly encapsulated, only the storage module changes.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.3.1 "Switching from ETS to Mnesia."

# Verification Notes

- Definition source: Directly adapted from Section 9.3.1.
- Confidence rationale: HIGH — the book walks through each function's conversion.
- Uncertainties: None.
- Cross-reference status: Verified; `ets` owned by Agent 2.
