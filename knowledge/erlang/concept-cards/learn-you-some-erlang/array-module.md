---
concept: Array Module
slug: array-module
category: data-types
subcategory: collections
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Larger Dictionaries: Dicts and GB Trees"
extraction_confidence: medium
aliases:
  - "array"
  - "Erlang array"
prerequisites: []
extends: []
related:
  - queue-module
contrasts_with: []
answers_questions:
  - "What is an Erlang array?"
  - "Why are arrays rarely used in Erlang?"
---

# Array Module

## Quick Definition

The `array` module provides a data structure with numeric integer indices. Unlike imperative arrays it is persistent (no destructive updates), so it lacks constant-time access and is rarely used in Erlang.

## Core Definition

The chapter introduces arrays in a "Don't Drink Too Much Kool-Aid" sidebar. Erlang arrays "allow you to access elements with numeric indices and to fold over the whole structure while possibly ignoring undefined slots. However, very few people use them." Unlike their imperative counterparts, Erlang arrays "do not have such things as constant-time insertion or lookup. Instead, they are said to be *persistent*, as they allow no destructive updates," which makes them slower than arrays in languages with destructive assignment. Programmers needing real matrix-style array work tend to use ports, C nodes, linked-in drivers, or NIFs to let other languages do the heavy lifting (Hébert, ch. 9, sidebar).

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. Provides numeric (integer) index access to elements
2. Supports folding over the whole structure, optionally ignoring undefined slots
3. Persistent — no destructive updates — so no constant-time insertion or lookup
4. Slower than imperative arrays; rarely used in idiomatic Erlang
5. Heavy numeric/matrix work is usually delegated via ports, C nodes, linked-in drivers, or NIFs

## Construction / Recognition

## To Use an Array

1. Create: `array:new()` or `array:new(Size)`
2. Set an element: `array:set(Index, Value, A)`
3. Read an element: `array:get(Index, A)`
4. Fold over it: `array:foldl/3`

## Examples

> The chapter gives no code example for arrays; it presents them only in a cautionary sidebar describing why they "tend to sit in a dark corner, alone" (ch. 9).

## Relationships

## Related

- **Queue module** — Another specialized standard data structure covered in the same chapter

## Common Errors

- **Error**: Expecting array reads/writes to be constant time
  **Correction**: Erlang arrays are persistent; access is not constant-time, unlike imperative arrays

## Common Confusions

- **Confusion**: Choosing an array because other languages use arrays for everything
  **Clarification**: Idiomatic Erlang rarely uses arrays; lists, dicts, or GB trees are usually better fits

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores," "Don't Drink Too Much Kool-Aid" sidebar.

## Verification Notes

- Definition and persistence note: directly from the ch. 9 sidebar
- Construction steps: synthesized from standard `array` usage since the chapter gives no code
- Confidence: MEDIUM — the chapter discusses arrays only briefly in a sidebar with no example
