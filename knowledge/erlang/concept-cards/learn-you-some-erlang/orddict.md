---
concept: Orddict
slug: orddict
category: data-types
subcategory: associative-structures
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Stores for Small Amounts of Data"
extraction_confidence: high
aliases:
  - "ordered dictionary"
  - "orddict module"
prerequisites: []
extends:
  - key-value-store
related:
  - proplist
  - dict-module
contrasts_with:
  - proplist
  - dict-module
answers_questions:
  - "What is an orddict?"
  - "When should I use an orddict over a proplist or a dict?"
---

# Orddict

## Quick Definition

An orddict is an ordered dictionary — a sorted list of `{Key, Value}` pairs with unique keys, accessed only through the `orddict` module's functional interface. It is the recommended key-value store for small amounts of data.

## Core Definition

The chapter describes orddicts as "proplists with a taste for formality." Each key appears only once, the whole list is kept sorted (so average lookups are faster), and entries must respect a strict `{Key, Value}` structure. Unlike proplists, you are not expected to edit an orddict as a raw list — you must use the `orddict` module's functional interface for every operation. Orddicts are "a good compromise between complexity and efficiency for up to about 75 elements," after which a dict or GB tree is preferable (Hébert, ch. 9, "Orddicts").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. Internally a sorted list of `{Key, Value}` tuples
2. Each key is unique
3. Entries must respect the strict `{Key, Value}` shape
4. All operations go through the `orddict` module — never edit it as a raw list
5. CRUD functions: `store/3`, `find/2` (key may be absent), `fetch/2` (key must be present), `erase/2`
6. Created with `orddict:new/0` or `orddict:from_list/1`
7. Good for up to roughly 75 elements; switch to dict/GB tree beyond that

## Construction / Recognition

## To Use an Orddict

1. Create it: `D = orddict:new()` or `orddict:from_list([{a,1},{b,2}])`
2. Insert/update: `orddict:store(Key, Value, D)`
3. Read when the key may be absent: `orddict:find(Key, D)` → `{ok, Value}` or `error`
4. Read when the key must exist: `orddict:fetch(Key, D)`
5. Delete: `orddict:erase(Key, D)`

## Examples

> **CRUD interface** (ch. 9): `orddict:store/3`, `orddict:find/2`, `orddict:fetch/2`, `orddict:erase/2`.
>
> **Event server use** (ch. 13): the reminder app's event server keeps both its clients and events as orddicts because "we're unlikely to have many hundreds of them at once."

## Relationships

## Builds Upon

- **Key-value store** — Orddict is the formal small-data member of the key-value family

## Related

- **Proplist** — The looser small-data alternative
- **Dict module** — The scalable replacement when an orddict grows too large

## Contrasts With

- **Proplist** — Proplists allow duplicate keys and arbitrary elements; orddicts enforce unique sorted strict pairs
- **Dict module** — A dict scales better for large data but does not keep keys ordered

## Common Errors

- **Error**: Manually consing or editing an orddict as a list
  **Correction**: Always use `orddict` functions, or you risk ordering errors that break lookups
- **Error**: Using `fetch/2` on a possibly-missing key
  **Correction**: Use `find/2` when the key may be absent; `fetch/2` crashes if it is not there

## Common Confusions

- **Confusion**: Thinking an orddict and a proplist are interchangeable
  **Clarification**: They share a list-of-tuples shape, but an orddict guarantees sorted unique keys and must be manipulated only through its module

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores," subsection "Orddicts."

## Verification Notes

- Definition, interface, 75-element heuristic: directly from ch. 9
- Event server usage: cross-referenced from ch. 13
- Confidence: HIGH — explicitly defined
