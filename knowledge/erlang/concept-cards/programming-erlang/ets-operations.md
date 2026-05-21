---
# === CORE IDENTIFICATION ===
concept: ETS and DETS Table Operations
slug: ets-operations

# === CLASSIFICATION ===
category: performance
subcategory: data-storage
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Storing Data with ETS and DETS"
chapter_number: 19
pdf_page: null
section: "Types of Table"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ets:insert"
  - "ets:lookup"
  - "ets:new"
  - "dets:open_file"
  - "table operations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - ets-table-types
extends: []
related:
  - dets
  - ets-table-ownership
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the basic operations on ETS and DETS tables?"
  - "How do I insert and look up data in an ETS table?"
---

# Quick Definition

The four basic operations on ETS and DETS tables are: create/open a table, insert one or more tuples, look up tuples by key, and dispose of the table.

# Core Definition

"There are four basic operations on ETS and DETS tables" ("Types of Table"). **Create or open** a table with `ets:new` or `dets:open_file`. **Insert** a tuple or several tuples with `insert(TableId, X)`, where `X` is a tuple or a list of tuples; `insert` has the same arguments and works the same way in ETS and DETS. **Look up** a tuple with `lookup(TableID, Key)`, defined for both ETS and DETS; the result is always a *list* of tuples matching `Key` — this uniformity lets the same `lookup` work on bags and sets, since a bag may return several tuples while a set returns at most one. If no tuples have the required key, an empty list is returned. **Dispose** of a table with `ets:delete(TableId)` or `dets:close(TableId)`. The chapter notes that matching on a tuple element that is *not* the key is possible but very inefficient, because it must search the whole table.

# Prerequisites

- **ETS (Erlang Term Storage)** — The operations act on ETS (and DETS) tables.
- **ETS table types** — The result of `insert`/`lookup` depends on whether the table is a set or a bag.

# Key Properties

1. Four operations: create/open, insert, lookup, dispose.
2. `ets:new` / `dets:open_file` create or open a table.
3. `insert(TableId, X)` takes a single tuple or a list of tuples; identical in ETS and DETS.
4. `lookup(TableId, Key)` always returns a *list* of tuples (empty list if the key is absent).
5. The list-returning convention lets one `lookup` serve both sets (≤1 result) and bags (≥0 results).
6. `ets:delete` / `dets:close` dispose of a table.
7. Matching on a non-key tuple element is supported but inefficient — it scans the whole table.
8. Helper operations include `ets:tab2list`, `ets:tab2file`, `ets:file2tab`, and `ets:info(Tab, size)`.

# Construction / Recognition

## To perform the basic operations:

1. Create: `TableId = ets:new(Name, [Opts])` (or open a DETS file with `dets:open_file`).
2. Insert: `ets:insert(TableId, {Key, Value})` or `ets:insert(TableId, [Tuple1, Tuple2, ...])`.
3. Lookup: `ets:lookup(TableId, Key)` — match the returned list, e.g. `[]` for absent, `[{K,V}]` for found.
4. Dispose: `ets:delete(TableId)`.

## To recognize correct lookup handling:

1. Always handle the empty-list case for an absent key.
2. For a bag, expect the result list to contain more than one tuple.

# Context & Application

These four operations are everything most ETS/DETS programs need.

- **Typical contexts**: Building and querying in-memory or on-disk lookup tables.
- **Common applications**: The trigram example inserts `{<<"ABC">>}` tuples and tests membership with `ets:lookup`.
- **Historical/stylistic notes**: The book stores `{Key}` (a one-element tuple) when a key needs no value, since every ETS entry must be a tuple.

# Examples

**Example 1** ("Types of Table"): `ets:insert(TableId, {a,1})` followed by `ets:tab2list(TableId)` and `ets:delete(TableId)`.

**Example 2** ("Example Programs with ETS"): `is_this_a_trigram` does `case ets:lookup(Tab, list_to_binary(X)) of [] -> false; _ -> true end`.

## Worked Example

Membership test via lookup (from "And the Winner Is..."):

```erlang
is_this_a_trigram(Tab, X) ->
    case ets:lookup(Tab, list_to_binary(X)) of
        [] -> false;
        _  -> true
    end.
```

# Relationships

## Builds Upon

- **ETS (Erlang Term Storage)** — The operations are the ETS/DETS module API.
- **ETS table types** — `insert`/`lookup` results vary by table type.

## Related

- **DETS** — `insert` and `lookup` are defined identically for DETS; `dets:open_file`/`dets:close` are the create/dispose pair.
- **ETS table ownership and visibility** — Whether a non-owner may `insert` depends on the table's visibility.

# Common Errors

- **Error**: Treating `lookup`'s result as a single tuple rather than a list.
  **Correction**: `lookup` always returns a list — match `[]`, `[Tuple]`, or `[T1, T2, ...]`.

- **Error**: Routinely matching on non-key tuple elements.
  **Correction**: That scans the entire table; design the table so the field you query is the key, or use multiple entries / Mnesia.

# Common Confusions

- **Confusion**: Expecting `lookup` to return one tuple for a set.
  **Clarification**: It returns a *list* even for a set — at most one element, but still wrapped in a list.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS," section "Types of Table" and "Example Programs with ETS." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the "four basic operations" list in "Types of Table."
- Confidence rationale: HIGH — the operations are explicitly enumerated and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
