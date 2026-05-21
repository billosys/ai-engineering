---
concept: Mnesia Table Operations
slug: mnesia-table-operations
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "Reads, Writes, and More"
extraction_confidence: high
aliases:
  - "mnesia:read"
  - "mnesia:write"
  - "match_object"
prerequisites:
  - mnesia
  - mnesia-transaction
related:
  - query-list-comprehension
  - mnesia-table-type
contrasts_with: []
answers_questions:
  - "How do I read and write records in Mnesia?"
  - "What query operations does Mnesia provide?"
---

# Mnesia Table Operations

## Quick Definition

Mnesia table operations — `write`, `delete`, `read`, `match_object`, and `select` — are the record-level functions used inside an activity context to modify and query Mnesia tables.

## Core Definition

Mnesia's table-modifying functions are mostly similar to what ETS and DETS offer, and all must be run inside an activity access context. The core operations are: `mnesia:write(Record)` (insert a record, the record name being the table name); `mnesia:delete(TableName, Key)` (remove records sharing a key); `mnesia:read({TableName, Key})` (return a list of records matching a primary key); `mnesia:match_object(Pattern)` (return records matching an ETS-style pattern); and `mnesia:select(TableName, MatchSpec)` (query via match specifications or `ets:fun2ms`). Each returns `ok` or a result list on success, and throws an exception on failure — which aborts the enclosing transaction (Chapter 29, "Reads, Writes, and More").

## Prerequisites

- **Mnesia** — These are Mnesia's table-access functions
- **Mnesia transaction** — Operations must run inside an activity context

## Key Properties

1. `write/1`: inserts a record; for `set`/`ordered_set` an existing primary key is replaced, for `bag` the whole record must match to be a duplicate; returns `ok`
2. `delete/2`: removes record(s) sharing a key; returns `ok`
3. `read/1`: returns a list of records matching the primary key (empty list if none) — always a list, even for `set` tables
4. `match_object/1`: returns whole records matching an ETS-style pattern; `_ = '_'` is needed to make unspecified fields match-all
5. `select/2`: queries using match specifications, often built with `ets:fun2ms/1`
6. All operations throw an exception on failure, aborting the transaction
7. Other operations exist: `first`/`last`/`next`/`prev` for iteration, `foldl`/`foldr` for folds, `transform_table` and `add_table_index` for table manipulation

## Construction / Recognition

## To Operate on a Table

1. Write the operation call (e.g., `mnesia:read({mafiapp_friends, Name})`) inside a `fun`
2. Execute the `fun` with `mnesia:activity(transaction, Fun)`
3. For pattern queries use `match_object/1` with a record pattern, or `select/2` with a match spec from `ets:fun2ms/1`

## Context & Application

`read/1` is best when querying by primary key — `friend_by_name/1` in `mafiapp` uses a single `mnesia:read`. `match_object/1` suits matching on one non-key field — `friend_by_expertise/1` uses it with an `expertise` pattern. `select/2` with `ets:fun2ms/1` handles queries that must match multiple fields or compute results — `find_services/1` and `debts/1` use it. Nested transactions are possible but often pointless, so a helper like `find_services/1` called only from inside another transaction need not start its own.

## Examples

**Example** (Chapter 29, "Tests for Lookups"): `find_services/1` uses `ets:fun2ms` to build a two-clause match specification and runs `mnesia:select(mafiapp_services, Match)`.

**Example** (Chapter 29): `friend_by_expertise/1` builds `Pattern = #mafiapp_friends{_ = '_', expertise = Expertise}` and calls `mnesia:match_object(Pattern)`.

## Relationships

## Builds Upon

- **Mnesia** — These are Mnesia's record-level access functions
- **Mnesia transaction** — Operations run inside an activity context

## Related

- **Query list comprehension** — A more Erlang-natural alternative to `match_object`/`select`
- **Mnesia table type** — `write` behaves differently for `set`/`ordered_set` vs. `bag` tables

## Common Errors

- **Error**: Using `match_object` with a record pattern that omits `_ = '_'`
  **Correction**: Without `_ = '_'`, unspecified fields are treated as the atom `undefined`; add it to match all

- **Error**: Calling Mnesia operations outside an activity context
  **Correction**: All reads and writes must run inside `mnesia:activity/2`

## Common Confusions

- **Confusion**: Expecting `read/1` on a `set` table to return a bare record
  **Clarification**: `read/1` always returns a list, even for `set` tables that can hold at most one match

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "Reads, Writes, and More" and the request implementations in "Implementing the First Requests."

## Verification Notes

- Definition: Direct adaptation from "Reads, Writes, and More"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — each operation explicitly described with `mafiapp` usage
- Cross-references: verified against planned cards in this extraction
