---
concept: Set Data Structure
slug: set-data-structure
category: data-types
subcategory: collections
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "A Set of Sets"
extraction_confidence: high
aliases:
  - "set"
  - "ordsets"
  - "gb_sets"
  - "sofs"
prerequisites: []
extends: []
related:
  - gb-trees
  - directed-graph
contrasts_with: []
answers_questions:
  - "What is a set in Erlang?"
  - "Which set module should I use?"
---

# Set Data Structure

## Quick Definition

A set is a group of unique elements supporting comparison and combination (union, intersection, difference). Erlang offers four set modules — `ordsets`, `sets`, `gb_sets`, and `sofs` — because there is no single "best" implementation.

## Core Definition

Sets are "groups of unique elements that you can compare and operate on." Because the implementers agreed there is no single best way to build a set, Erlang ships four modules: `ordsets` (sorted lists — simplest and most readable representation, slowest, for small sets); `sets` (built on a dict-like structure — scales well, good for read-intensive use); `gb_sets` (built on a GB tree — faster than `sets` for non-read operations, with smart/naive functions, iterators, and min/max access); and `sofs` (sets of sets — sorted lists in a tuple with metadata, for the mathematical theory of sets, relations, and families). Björn Gustavsson's advice, cited in the chapter, is to use `gb_sets` in most cases, `ordsets` when you want a readable representation to process yourself, and `sets` when you need the `=:=` operator (Hébert, ch. 9, "A Set of Sets").

## Prerequisites

This is a foundational data structure with no prerequisites within this chapter.

## Key Properties

1. A set holds only unique elements
2. Four modules — `ordsets`, `sets`, `gb_sets`, `sofs` — share a common core interface
3. `ordsets` are sorted lists: simplest, most readable, slowest, for small sets
4. `sets` are dict-backed: scale well, good for read-intensive checks like membership
5. `gb_sets` are GB-tree-backed: faster on non-read operations, with smart/naive functions and min/max
6. `sofs` (sets of sets) supports the mathematical theory of relations and families
7. Equality differs: `sets` uses `=:=`; `gb_sets`, `ordsets`, and `sofs` use `==` (so `2` and `2.0` compare equal)

## Construction / Recognition

## To Use a Set

1. Choose a module: `gb_sets` for most cases, `ordsets` for a readable small set, `sets` when `=:=` semantics are required
2. Create: `gb_sets:new()` / `ordsets:new()` / `sets:new()`
3. Add an element: `Module:add_element(E, Set)`
4. Test membership: `Module:is_element(E, Set)`
5. Combine sets: `Module:union/1`, `Module:intersection/1`

## Examples

> **Common functions** (ch. 9): `ordsets:new/0`, `ordsets:is_element/2`, `ordsets:add_element/2`, `ordsets:union/1`, `ordsets:intersection/1`.
>
> **Selection advice** (ch. 9): Björn Gustavsson recommends `gb_sets` "in most circumstances," `ordsets` for a clear self-processed representation, and `sets` when you need `=:=`.

## Relationships

## Related

- **GB trees** — `gb_sets` is built on the same balanced-tree structure
- **Directed graph** — The `sofs` module converts between families and directed graphs

## Common Errors

- **Error**: Assuming you can freely swap set implementations
  **Correction**: `sets` uses `=:=` while the others use `==`; switching can change behavior for numbers like `2` vs `2.0`
- **Error**: Using `ordsets` for large sets
  **Correction**: `ordsets` are the slowest; use `gb_sets` or `sets` as the set grows

## Common Confusions

- **Confusion**: Thinking `sofs` is just another general-purpose set
  **Clarification**: `sofs` is for the mathematical concept of sets — relations, families, set types — not merely groups of unique elements

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "A Set of Sets."

## Verification Notes

- Definition, four modules, equality caveat: directly from ch. 9
- Selection advice: attributed to Björn Gustavsson in the source
- Confidence: HIGH — explicitly described
