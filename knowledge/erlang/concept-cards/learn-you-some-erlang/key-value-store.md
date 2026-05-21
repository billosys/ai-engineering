---
concept: Key-Value Store
slug: key-value-store
category: data-types
subcategory: associative-structures
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Key/Value Stores"
extraction_confidence: high
aliases:
  - "key/value store"
  - "associative store"
  - "dictionary"
prerequisites:
  - pattern-matching
extends: []
related:
  - proplist
  - orddict
  - dict-module
  - gb-trees
contrasts_with: []
answers_questions:
  - "What is a map (associative key-value store)?"
  - "Which key-value store should I choose in Erlang?"
---

# Key-Value Store

## Quick Definition

A key-value store associates values with keys for lookup. Erlang's standard library offers several implementations — proplists, orddicts, dicts, and GB trees — each with different size and performance trade-offs.

## Core Definition

Chapter 9 surveys the data structures Erlang provides for storing data under a key. Rather than a single map type, Erlang gives a family of modules, and the right choice depends on the amount of data and the operations needed. For small amounts of data, use a proplist or an orddict. For larger amounts, use a dict or a GB tree. The chapter's recurring advice is to "measure, profile, and benchmark" rather than guess (Hébert, ch. 9, "Key/Value Stores").

The chapter notes that orddicts are a good compromise up to roughly 75 elements, after which a dict or GB tree should be used. Larger, process-related stores — ETS, DETS, and Mnesia — are deferred to later chapters.

## Prerequisites

- **Pattern matching** — Lookup results are typically `{ok, Value}` / `error` tuples matched by callers

## Key Properties

1. Erlang has no single canonical map type in this chapter; it offers a family of modules
2. Proplist — loosest, just a list of `{Key, Value}` tuples; best for small config-style data
3. Orddict — a sorted, strict `{Key, Value}` list with a functional CRUD interface; good up to ~75 elements
4. Dict — scales beyond orddict; best read speed; has `map/2` and `fold/2`
5. GB tree — balanced tree; quick min/max access and ordered traversal; faster than dict on non-read operations
6. The best choice depends on data size and access pattern — benchmark to decide

## Construction / Recognition

## To Choose a Key-Value Store

1. Small, loose, config-like data → proplist (`proplists` + `lists` modules)
2. Small, strict, needing a full CRUD interface → orddict (up to ~75 elements)
3. Larger data, read-intensive → dict
4. Larger data needing ordering, min/max, or non-read speed → GB tree
5. When unsure, benchmark with realistic data

## Examples

> **Proplist as properties** (ch. 9): `[{name, buddy}, {race, husky}, friendly]` describes a dog.
>
> **Orddict CRUD** (ch. 9): `orddict:store/3`, `orddict:find/2`, `orddict:fetch/2`, `orddict:erase/2`.
>
> **Choosing by size** (ch. 9): orddicts "are generally a good compromise... for up to about 75 elements," after which you switch to dicts or GB trees.

## Relationships

## Related

- **Proplist** — The loosest key-value store, for small config-style data
- **Orddict** — A sorted strict key-value store for small data
- **Dict module** — Scalable key-value store for larger data
- **GB trees** — Ordered balanced-tree key-value store

## Common Errors

- **Error**: Using an orddict for many thousands of elements
  **Correction**: Switch to a dict or GB tree past roughly 75 elements
- **Error**: Picking a store without measuring
  **Correction**: Benchmark with realistic data; performance differences depend on access pattern

## Common Confusions

- **Confusion**: Expecting one universal "map" type
  **Clarification**: In this edition the chapter presents a family of modules, not a single map type; choice is workload-dependent
- **Confusion**: Thinking all these stores have the same equality semantics
  **Clarification**: `sets` uses `=:=` while `gb_sets`/`ordsets` use `==`; the same caution applies across implementations

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores" (subsections "Stores for Small Amounts of Data," "Larger Dictionaries: Dicts and GB Trees").

## Verification Notes

- Definition: synthesized from the chapter's overview of key/value modules
- 75-element heuristic: explicit in the source
- Confidence: HIGH — the chapter explicitly frames the choice as workload-dependent
