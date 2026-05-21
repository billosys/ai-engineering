---
concept: Query List Comprehension
slug: query-list-comprehension
category: distribution
subcategory: mnesia
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Mnesia and the Art of Remembering"
chapter_number: 29
pdf_page: null
section: "Query List Comprehensions"
extraction_confidence: high
aliases:
  - "QLC"
  - "qlc"
prerequisites:
  - mnesia
related:
  - mnesia-transaction
contrasts_with: []
answers_questions:
  - "What are query list comprehensions (QLC)?"
  - "How do I query Mnesia tables with list comprehensions?"
---

# Query List Comprehension

## Quick Definition

Query list comprehensions (QLCs) are a compiler trick that lets you use ordinary list comprehension syntax to query any iterable data structure, including Mnesia, DETS, and ETS tables.

## Core Definition

Query list comprehensions (QLCs) are a compiler trick using parse transforms that let you use list comprehensions for any data structure that can be searched and iterated through. They are implemented for Mnesia, DETS, and ETS, and can be implemented for structures like `gb_trees`. After adding `-include_lib("stdlib/include/qlc.hrl").` to a module, you use a *query handle* as a generator — for Mnesia, `mnesia:table(TableName)` — and wrap the list comprehension in `qlc:q(...)`, which returns a modified query handle. That handle can be further refined (e.g., `qlc:sort/1-2`) and evaluated with `qlc:eval/1` or folded with `qlc:fold/1` (Chapter 29, "Query List Comprehensions").

## Prerequisites

- **Mnesia** — In this chapter QLCs are used to query Mnesia tables (though they also work for ETS/DETS)

## Key Properties

1. Implemented via parse transforms; requires `-include_lib("stdlib/include/qlc.hrl").`
2. Works over any iterable data structure that provides a query handle (Mnesia, DETS, ETS, `gb_trees`)
3. `mnesia:table(TableName)` provides a query handle usable as a comprehension generator
4. `qlc:q(...)` wraps a list comprehension and returns a refined query handle
5. Query handles are evaluated with `qlc:eval/1` or folded with `qlc:fold/1`
6. Handles can be transformed further, e.g., sorted with `qlc:sort/1-2`
7. Provides a more natural, Erlang-like alternative to match specifications for database queries

## Construction / Recognition

## To Query with a QLC

1. Add `-include_lib("stdlib/include/qlc.hrl").` to the module
2. Write a list comprehension whose generator is `mnesia:table(TableName)`, wrapped in `qlc:q(...)`
3. Evaluate it with `qlc:eval/1`, or pass the handle to `qlc:fold/1`
4. Run the whole thing inside an `mnesia:activity(transaction, Fun)`

## Context & Application

QLCs are an alternative to `match_object` and match specifications, making database queries read like ordinary Erlang list comprehensions. The chapter rewrites `mafiapp`'s `friend_by_expertise/1` (previously using `mnesia:match_object/1`) and `debts/1` (previously using a match specification plus a fold) as QLCs. The author notes you could even write QLC selectors for SQL databases or any other iterable storage.

## Examples

**Example** (Chapter 29, "Query List Comprehensions"): `friend_by_expertise/1` becomes
`qlc:eval(qlc:q([{Name,C,I,E,find_services(Name)} || #mafiapp_friends{name=Name, contact=C, info=I, expertise=E} <- mnesia:table(mafiapp_friends), E =:= Expertise]))` inside a transaction.

**Example** (Chapter 29): `debts/1` builds a query handle `QH` with `qlc:q(...)` and evaluates it with `qlc:fold/3`, replacing the earlier match specification.

## Relationships

## Builds Upon

- **Mnesia** — The chapter uses QLCs to query Mnesia tables

## Related

- **Mnesia transaction** — QLC queries against Mnesia are run inside an activity context

## Common Errors

- **Error**: Using QLC syntax without including `qlc.hrl`
  **Correction**: Add `-include_lib("stdlib/include/qlc.hrl").` so the parse transform is applied

## Common Confusions

- **Confusion**: Thinking a `qlc:q/1` expression is evaluated like a normal list comprehension
  **Clarification**: `qlc:q/1` produces a query handle; it must be explicitly evaluated with `qlc:eval/1` or `qlc:fold/1`

## Source Reference

Chapter 29: Mnesia and the Art of Remembering, section "Query List Comprehensions."

## Verification Notes

- Definition: Direct adaptation from "Query List Comprehensions"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with two rewritten `mafiapp` examples
- Cross-references: verified against planned cards in this extraction
