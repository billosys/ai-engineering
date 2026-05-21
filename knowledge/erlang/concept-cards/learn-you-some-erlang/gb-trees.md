---
concept: GB Trees
slug: gb-trees
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
  - "general balanced trees"
  - "gb_trees"
  - "GB tree"
prerequisites: []
extends:
  - key-value-store
related:
  - dict-module
  - set-data-structure
contrasts_with:
  - dict-module
answers_questions:
  - "What is a GB tree?"
  - "When should I use gb_trees instead of dict?"
---

# GB Trees

## Quick Definition

GB trees (general balanced trees), handled by the `gb_trees` module, are a balanced-tree key-value store for larger data that preserves key order and offers both "smart" and "naive" function modes.

## Core Definition

GB trees are the second large-data key-value structure (alongside dicts). The `gb_trees` module offers more functions giving "more direct control over how the structure is to be used," organized into two modes: a *naive mode* for when you cannot assume much about the structure (`enter/3`, `lookup/2`, `delete_any/2`) and a *smart mode* for when you know the key is present (`insert/3`, `get/2`, `update/3`, `delete/2`). Smart functions skip safety checks and are faster. Because a GB tree is balanced, inserts and deletes may trigger rebalancing, which costs time and memory. Unlike dicts, GB trees have no fold — only an iterator function with `gb_trees:next/1` — but they do provide ordered traversal and quick access to the smallest and largest elements via `gb_trees:smallest/1` and `gb_trees:largest/1` (Hébert, ch. 9, "Larger Dictionaries: Dicts and GB Trees").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. A balanced tree, accessed through the `gb_trees` module
2. Two modes: naive (`enter/3`, `lookup/2`, `delete_any/2`) and smart (`insert/3`, `get/2`, `update/3`, `delete/2`)
3. Smart functions assume the key exists, skip safety checks, and run faster
4. Inserts and deletes may rebalance the tree, costing time and memory
5. Preserves order — supports ordered traversal and `smallest/1` / `largest/1`
6. Has no fold; iteration uses an iterator plus `gb_trees:next/1`
7. Has a `gb_trees:map/2` analogous to `lists:map/2`

## Construction / Recognition

## To Use a GB Tree

1. Create it: `gb_trees:empty()` or `gb_trees:from_orddict/1`
2. Insert when the key is new: `gb_trees:insert(Key, Value, T)` (smart) or `enter/3` (naive)
3. Read: `gb_trees:get(Key, T)` (smart) or `lookup/2` (naive, returns `{value, V}` / `none`)
4. Traverse in order: build an iterator with `gb_trees:iterator/1`, then loop with `gb_trees:next/1`
5. Get extremes: `gb_trees:smallest/1`, `gb_trees:largest/1`

## Examples

> **Smart vs naive functions** (ch. 9): smart `gb_trees:get/2` assumes the key is present; naive `gb_trees:lookup/2` does not.
>
> **Priority mailbox** (ch. 11): the chapter suggests dumping prioritized messages into `gb_trees` (priority first in the key) and pulling the `smallest` or `largest` to handle messages by priority efficiently.

## Relationships

## Builds Upon

- **Key-value store** — GB tree is the ordered large-data member of the family

## Related

- **Dict module** — The unordered large-data alternative
- **Set data structure** — `gb_sets` is built on the same balanced-tree structure

## Contrasts With

- **Dict module** — Dict has better read speed and a fold; GB tree preserves order, gives min/max, and is faster on non-read operations but has only an iterator

## Common Errors

- **Error**: Using a smart function (`get/2`, `insert/3`) on a key that may not exist or already exists
  **Correction**: Use naive functions (`lookup/2`, `enter/3`) when you cannot guarantee the key's state
- **Error**: Expecting a `gb_trees:fold/3`
  **Correction**: GB trees have no fold; use the iterator and `next/1`, or write your own recursion

## Common Confusions

- **Confusion**: Thinking GB trees are always faster than dicts
  **Clarification**: The benchmark shows dicts win on reads; GB trees win on other operations and ordering

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Key/Value Stores," subsection "Larger Dictionaries: Dicts and GB Trees."

## Verification Notes

- Definition, modes, function names: directly from ch. 9
- Priority-mailbox use: cross-referenced from ch. 11
- Confidence: HIGH — explicitly described
