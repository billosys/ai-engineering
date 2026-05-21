---
concept: Dict Module
slug: dict-module
category: data-types
subcategory: associative-structures
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Larger Dictionaries: Dicts and GB Trees"
extraction_confidence: high
aliases:
  - "dict"
  - "dictionary"
prerequisites: []
extends:
  - key-value-store
related:
  - orddict
  - gb-trees
contrasts_with:
  - orddict
  - gb-trees
answers_questions:
  - "What is the dict module?"
  - "When should I use a dict instead of an orddict or a GB tree?"
---

# Dict Module

## Quick Definition

The `dict` module provides a key-value store for larger amounts of data, sharing the same interface as `orddict` but scaling far better. It offers the best read speeds among the standard key-value structures.

## Core Definition

Dicts are one of the two key-value structures the chapter recommends "to deal with larger amounts of data" (the other being GB trees). A dict has "the same interface as orddicts" — `dict:store/3`, `dict:find/2`, `dict:fetch/2`, `dict:erase/2` — plus every other `orddict` function, including `dict:map/2` and `dict:fold/2`, which makes a dict "a very good choice for scaling up orddicts." The chapter's benchmark notes that dicts have the best read speeds of the structures compared, while GB trees are a little quicker on other operations. A dict does not keep keys in order (Hébert, ch. 9, "Larger Dictionaries: Dicts and GB Trees").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. Designed for larger key-value data sets than orddicts handle well
2. Shares the orddict interface — drop-in scaling from an orddict
3. Provides `dict:map/2` and `dict:fold/2` for operating on the whole structure
4. Has the best read speeds of the standard key-value structures
5. Does not preserve key ordering — no min/max or ordered traversal

## Construction / Recognition

## To Use a Dict

1. Create it: `dict:new()` or `dict:from_list/1`
2. Insert/update: `dict:store(Key, Value, D)`
3. Read: `dict:find(Key, D)` or `dict:fetch(Key, D)`
4. Delete: `dict:erase(Key, D)`
5. Operate over all entries: `dict:map/2`, `dict:fold/2`

## Examples

> **Same interface as orddict** (ch. 9): `dict:store/3`, `dict:find/2`, `dict:fetch/2`, `dict:erase/2`.
>
> **Whole-structure operations** (ch. 9): `dict:map/2` and `dict:fold/2`, "pretty useful to work on the whole data structure."

## Relationships

## Builds Upon

- **Key-value store** — Dict is the scalable read-optimized member of the family

## Related

- **Orddict** — A dict has the same interface; you scale up from orddict to dict
- **GB trees** — The ordered alternative for large data

## Contrasts With

- **Orddict** — Orddict suits small data (~75 elements); dict scales to large data
- **GB trees** — A dict has better read speed and a fold; GB trees preserve order and have faster non-read operations but only an iterator, no fold

## Common Errors

- **Error**: Relying on a dict for ordered traversal or min/max
  **Correction**: Use a GB tree if you need ordering; a dict does not maintain key order

## Common Confusions

- **Confusion**: Confusing the `dict` module with the process dictionary
  **Clarification**: `dict` is an immutable functional data structure; the process dictionary is per-process mutable state

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores," subsection "Larger Dictionaries: Dicts and GB Trees."

## Verification Notes

- Definition, interface, benchmark notes: directly from ch. 9
- Confidence: HIGH — explicitly described
