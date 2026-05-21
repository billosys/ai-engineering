---
concept: ETS Table Type
slug: ets-table-type
category: performance
subcategory: in-memory-storage
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "The Concepts of ETS"
extraction_confidence: high
aliases:
  - "set"
  - "ordered_set"
  - "bag"
  - "duplicate_bag"
  - "ETS table types"
prerequisites:
  - ets-table
extends: []
related:
  - ets-select-and-match
contrasts_with: []
answers_questions:
  - "What are the four ETS table types?"
  - "What is the difference between set, ordered_set, bag, and duplicate_bag?"
  - "Which ETS table type should I use for ranges?"
---

# ETS Table Type

## Quick Definition

An ETS table's type determines how keys and duplicate tuples behave. The four types are `set`, `ordered_set`, `bag`, and `duplicate_bag`; `set` is the default.

## Core Definition

When creating a table with `ets:new/2`, the `Type` option selects one of four ways to store data (Ch. 25, "The Concepts of ETS"). `set` requires unique keys with constant-time access. `ordered_set` also requires unique keys but keeps elements ordered and supports range traversal, at the cost of `O(log N)` access. `bag` allows multiple entries with the same key as long as the tuples differ. `duplicate_bag` allows entirely identical tuples to be stored multiple times.

## Prerequisites

- **Ets-table** — Table type is an option chosen at table creation

## Key Properties

1. `set` — each key value must be unique; constant-time access; the default type
2. `ordered_set` — unique keys, elements kept in sorted order, supports range/iteration; `O(log N)` access
3. `bag` — multiple entries with the same key allowed, provided the whole tuples differ
4. `duplicate_bag` — like `bag` but allows entirely identical tuples stored multiple times
5. Inserting a duplicate key overwrites in `set` and `ordered_set`, but not in `bag`/`duplicate_bag`
6. `ordered_set` treats `1` and `1.0` as identical; other types treat them as different
7. `ordered_set` supports `first/1`, `next/2`, `last/1`, `prev/2` traversal, returning `'$end_of_table'` at boundaries

## Construction / Recognition

### To choose a type

1. Standard key/value store with fastest access → `set`
2. Need ordered traversal or range queries → `ordered_set`
3. Need several distinct tuples sharing one key → `bag`
4. Need identical tuples stored repeatedly → `duplicate_bag`

## Context & Application

`ordered_set` is best when you frequently operate on ranges (e.g. "entries 12 to 50") or iterate elements in order. The book notes restricting return values to integers *or* floats avoids `1` vs `1.0` surprises in `ordered_set`.

## Examples

**Example** (Ch. 25): A `bag` table keeps `{bacon, fat}` only once even after two inserts, but allows a second distinct `bacon` entry:

```erlang
13> ets:lookup(TabId, bacon).
[{bacon,delicious},{bacon,fat}]
```

**Example** (Ch. 25): An `ordered_set` traversal — `ets:first/1`, `ets:next/2`, `ets:last/1`, `ets:prev/2` walk entries in sorting order, both forward and backward.

## Relationships

### Builds Upon

- **Ets-table** — Type is one of the `ets:new/2` options

### Related

- **Ets-select-and-match** — `select_reverse` ordering matters for `ordered_set`

## Common Errors

- **Error**: Expecting a `set` table to keep elements in insertion or sorted order.
  **Correction**: Only `ordered_set` keeps elements sorted.
- **Error**: Expecting `bag` to deduplicate distinct tuples sharing a key.
  **Correction**: `bag` keeps all distinct tuples per key; only fully identical tuples are deduplicated.

## Common Confusions

- **Confusion**: Thinking `bag` and `duplicate_bag` are the same.
  **Clarification**: `duplicate_bag` allows entirely identical tuples; `bag` does not.
- **Confusion**: Assuming `ordered_set` distinguishes `1` and `1.0`.
  **Clarification**: `ordered_set` treats them as identical; other table types treat them as different.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", sections "The Concepts of ETS" and "Creating and Deleting Tables."

## Verification Notes

- Definition: Direct adaptation from the table-type variable list
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines all four types precisely
- Cross-references: `ets-table`, `ets-select-and-match` planned this chapter
