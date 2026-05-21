---
concept: ETS Select and Match
slug: ets-select-and-match
category: performance
subcategory: in-memory-storage
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "Meeting Your Match"
extraction_confidence: high
aliases:
  - "ets:match"
  - "ets:select"
  - "ets:match_object"
  - "ETS querying"
prerequisites:
  - ets-table
extends: []
related:
  - ets-match-specification
contrasts_with: []
answers_questions:
  - "How do I query an ETS table beyond simple key lookup?"
  - "What is the difference between ets:match and ets:select?"
  - "How do I delete ETS entries by pattern?"
---

# ETS Select and Match

## Quick Definition

`ets:match` and `ets:select` query ETS tables with patterns. `match` uses a tuple pattern notation with `'$N'` variables; `select` uses full match specifications with guards.

## Core Definition

To query beyond keys, ETS offers two notations. The simpler is the *match* notation — tuples mixing `'$N'` variables and `'_'` "don't care" variables that act like ordinary pattern matching (Ch. 25, "Meeting Your Match"). `ets:match/2` returns only the pattern variables; `ets:match_object/2` returns whole matching entries; `ets:match_delete/2` deletes by pattern. The more powerful approach is *select*, which uses match specifications with guards (Ch. 25, "You Have Been Selected"): `ets:select/2` fetches results, `ets:select_reverse/2` reverses order for `ordered_set`, `ets:select_count/2` counts matches, and `ets:select_delete/2` deletes matching records.

## Prerequisites

- **Ets-table** — These functions query ETS tables

## Key Properties

1. Match patterns are tuples mixing literals, `'$N'` variables, and `'_'` (don't care)
2. `ets:match/2` returns lists of just the variable bindings, in `'$N'` order
3. `ets:match_object/2` returns the whole matched entries
4. `ets:match_delete/2` deletes entries matching a pattern
5. `ets:select/2` runs a match specification and fetches results
6. `ets:select_reverse/2` returns results in reverse for `ordered_set` (same as `select` otherwise)
7. `ets:select_count/2` returns how many entries match
8. `ets:select_delete/2` deletes matching records; the match spec must return `true` for entries to delete
9. `match` returns only what is needed, which avoids copying large records unnecessarily

## Construction / Recognition

### To query a table

1. Simple structural pattern → build a tuple with `'$N'`/`'_'` and call `ets:match/2` or `ets:match_object/2`
2. Need guards/comparisons → write a match specification (via `fun2ms`) and call `ets:select/2`
3. To delete by pattern → `ets:match_delete/2` (pattern) or `ets:select_delete/2` (match spec returning `true`)

## Context & Application

`match` is convenient for literal-value pattern matching; `select` adds comparisons, ranges, and explicit output formatting. The book uses `select` with `fun2ms` to rewrite `regis_server`'s lookups.

## Examples

**Example** (Ch. 25): `match` vs `match_object` —

```erlang
3> ets:match(table, {items, '$1', '$2', '_', '$1'}).
[[a,b],[1,2]]
5> ets:match_object(table, {items, '$1', '$2', '_', '$1'}).
[{items,a,b,c,a},{items,1,2,3,1}]
```

**Example** (Ch. 25): `select_delete` removing food over $5 — `ets:select_delete(food, ets:fun2ms(fun(#food{price=P}) when P > 5 -> true end))` returns `3`.

## Relationships

### Builds Upon

- **Ets-table** — These are table query functions

### Related

- **Ets-match-specification** — `select` functions consume match specifications

## Common Errors

- **Error**: Returning a value instead of `true` from a `select_delete` match spec.
  **Correction**: `select_delete` requires the pattern to return `true` to delete an entry.
- **Error**: Expecting `match` variable numbers to carry meaning.
  **Correction**: The numbers in `'$N'` only fix output order; their values are arbitrary.

## Common Confusions

- **Confusion**: Thinking `match` and `match_object` return the same thing.
  **Clarification**: `match` returns just the bound variables; `match_object` returns the whole entries.
- **Confusion**: Believing `match` supports guards and comparisons.
  **Clarification**: Only `select` (with match specifications) supports guards; `match` does literal pattern matching only.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", sections "Meeting Your Match" and "You Have Been Selected."

## Verification Notes

- Definition: Direct adaptation from "Meeting Your Match" and "You Have Been Selected"
- Key Properties: All explicit in source
- Confidence: HIGH — the sections demonstrate every function
- Cross-references: `ets-table`, `ets-match-specification` planned this chapter
