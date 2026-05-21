---
concept: ETS Table
slug: ets-table
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
  - "ETS"
  - "Erlang Term Storage"
  - "ETS table"
  - "ets module"
prerequisites:
  - process
  - tuple
extends: []
related:
  - ets-table-type
  - ets-concurrency-option
  - ets-select-and-match
  - dets
contrasts_with:
  - dets
answers_questions:
  - "What is an ETS table?"
  - "Why use ETS instead of holding data in a process?"
  - "How do I create and use an ETS table?"
---

# ETS Table

## Quick Definition

An ETS (Erlang Term Storage) table is an efficient in-memory database built into the Erlang VM. It stores tuples with constant-time access and allows limited concurrent reads and writes across processes.

## Core Definition

ETS tables are "an efficient in-memory database included with the Erlang VM" (Ch. 25, "Why ETS"). The database "sits in a part of the VM where destructive updates are allowed and where garbage collection dares not approach, in a part of memory not shared by processes." ETS was designed to store large amounts of data with constant access time (vs. the logarithmic time of functional data structures) and to look as if implemented as processes — keeping use simple and idiomatic. ETS tables natively store Erlang tuples and only tuples. They allow limited concurrency in reads and writes, but using them throws away most of the concepts that make Erlang concurrency safe.

## Prerequisites

- **Process** — A table is owned by the process that creates it and dies with it
- **Tuple** — ETS stores only tuples; one element acts as the primary key

## Key Properties

1. ETS is an in-memory database; the `ets` module's functions are BIFs
2. Tables store only Erlang tuples; one tuple position is the primary key (default position 1)
3. Created with `ets:new(Name, Options)`, which returns a table identifier
4. Deleted with `ets:delete(Table)`; a single entry with `ets:delete(Table, Key)`
5. Basic operations: `ets:insert/2` and `ets:lookup/2` (lookup always returns a list)
6. A table is owned by the process that created it; if that process dies, the table and its contents disappear
7. Permission levels: `protected` (default — owner writes, all read), `public` (all read/write), `private` (owner only)
8. A table can be given away (`ets:give_away/3`) or assigned an `heir` to survive owner death
9. By default the VM allows about 1,400 ETS tables (`ERL_MAX_ETS_TABLES` raises it)

## Construction / Recognition

### To create and use a table

1. `Tid = ets:new(name, [set, named_table])`
2. Insert: `ets:insert(Tid, {key, value})` (one tuple or a list of tuples)
3. Look up: `ets:lookup(Tid, key)` returns a list of matching tuples
4. Delete an entry: `ets:delete(Tid, key)`; drop the table: `ets:delete(Tid)`

## Context & Application

ETS is the right choice when a process holds a data structure mainly to share it with other processes — a central process answering messages one by one becomes a bottleneck. The book rewrites the `regis` registry to use ETS for parallel, concurrent access.

## Examples

**Example** (Ch. 25): Basic key/value use —

```erlang
1> ets:new(ingredients, [set, named_table]).
ingredients
2> ets:insert(ingredients, {bacon, great}).
true
3> ets:lookup(ingredients, bacon).
[{bacon,great}]
```

## Relationships

### Related

- **Ets-table-type** — `set`, `ordered_set`, `bag`, `duplicate_bag` choose key/duplication semantics
- **Ets-concurrency-option** — `read_concurrency`/`write_concurrency` tune concurrent access
- **Ets-select-and-match** — Querying beyond simple key lookup
- **Dets** — The disk-based counterpart

### Contrasts With

- **Dets** — Disk-based, no `ordered_set`, 2GB limit

## Common Errors

- **Error**: Letting the shell or owning process crash and being surprised the table is gone.
  **Correction**: Tables die with their owner; use an `heir` or `give_away` to preserve data.
- **Error**: Treating `lookup` as returning a single value.
  **Correction**: `lookup` always returns a list, even for `set` tables.

## Common Confusions

- **Confusion**: Thinking ETS tables are processes you can link to or spawn.
  **Clarification**: They only behave like processes (nothing shared, functional interface, optional names); you cannot link to or spawn them, though an heir mechanism exists.
- **Confusion**: Believing ETS preserves Erlang's concurrency safety.
  **Clarification**: ETS allows destructive shared updates and discards much of that safety; use it with care.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", sections "Why ETS," "The Concepts of ETS," and "ETS Phone Home."

## Verification Notes

- Definition: Direct adaptation from "Why ETS" and "The Concepts of ETS"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter is dedicated to ETS
- Cross-references: `ets-table-type`, `ets-concurrency-option`, `ets-select-and-match`, `dets` planned this chapter; `process`, `tuple` shared slugs
