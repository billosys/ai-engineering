---
concept: Proplist
slug: proplist
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
  - "property list"
  - "proplists"
prerequisites: []
extends:
  - key-value-store
related:
  - orddict
contrasts_with:
  - orddict
  - record
answers_questions:
  - "What is a proplist?"
  - "When should I use a proplist instead of an orddict?"
---

# Proplist

## Quick Definition

A proplist (property list) is any list of `{Key, Value}` tuples — a loosely defined key-value structure most appropriate for configuration data and lists of properties.

## Core Definition

A proplist is "any list of tuples of the form `[{Key, Value}]`." The chapter calls it "a weird kind of structure because that's the only rule that applies to them" — the rules are so relaxed the list may also contain bare Boolean values, integers, and other terms. The `proplists` module supplies reading functions (`get_value/2`, `get_all_values/2`, `lookup/2`, `lookup_all/2`, `delete/2`) but notably no add or update function. To add, you cons manually: `NewList = [NewElement|OldList]`. Because the `proplists` module scans in order and stops at the first match, prepending also serves as an update (Hébert, ch. 9, "Proplists").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. A proplist is just a list of `{Key, Value}` tuples — the only structural rule
2. The list may also contain bare values; a bare `friendly` is equivalent to `{friendly, true}`
3. The `proplists` module provides lookups but no add/update functions
4. Add an element by consing it onto the front; this also acts as an update due to first-match semantics
5. `lists:keyreplace/4` can update in place to avoid the list growing over time
6. Best suited to configuration lists and lists of properties

## Construction / Recognition

## To Use a Proplist

1. Build it as a literal list of tuples: `[{name, buddy}, {race, husky}, friendly]`
2. Read a value: `proplists:get_value(name, List)`
3. Add or update by consing: `[{name, rex} | List]`
4. Update in place to avoid growth: `lists:keyreplace(name, 1, List, {name, rex})`

## Examples

> **Describing a dog** (ch. 9): `[{name, buddy}, {race, husky}, friendly]`, where `friendly` is shorthand for `{friendly, true}`.
>
> **Reading functions** (ch. 9): `proplists:get_value/2`, `proplists:lookup/2`, `proplists:get_all_values/2`.

## Relationships

## Builds Upon

- **Key-value store** — A proplist is the loosest member of the key-value store family

## Related

- **Orddict** — The "more formal" small-data alternative to a proplist

## Contrasts With

- **Orddict** — An orddict enforces unique sorted keys and a strict `{Key, Value}` shape; a proplist enforces nothing
- **Record** — A record has fixed compile-time field names; a proplist has dynamic runtime keys

## Common Errors

- **Error**: Repeatedly consing updates so the proplist grows unboundedly
  **Correction**: Use `lists:keyreplace/4` for frequent updates
- **Error**: Expecting a `proplists:store/3` function
  **Correction**: There is no add/update function; add by consing manually

## Common Confusions

- **Confusion**: Treating a proplist as a strict map with unique keys
  **Clarification**: A proplist may contain duplicate keys and non-tuple elements; only first-match lookup makes it usable as a store

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores," subsection "Proplists."

## Verification Notes

- Definition and module functions: directly from ch. 9
- Confidence: HIGH — explicitly defined with examples
