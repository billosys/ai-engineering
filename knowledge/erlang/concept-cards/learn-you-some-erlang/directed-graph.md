---
concept: Directed Graph
slug: directed-graph
category: data-types
subcategory: collections
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Directed Graphs"
extraction_confidence: medium
aliases:
  - "digraph"
  - "graph"
prerequisites: []
extends: []
related:
  - set-data-structure
contrasts_with: []
answers_questions:
  - "What is a directed graph in Erlang?"
  - "Which modules implement directed graphs?"
---

# Directed Graph

## Quick Definition

A directed graph in Erlang is a data structure of vertices and directed edges, implemented by the `digraph` and `digraph_utils` modules for construction, modification, and navigation.

## Core Definition

Directed graphs are "intimately related to mathematics" and are implemented as two modules. The `digraph` module "allows the construction and modification of a directed graph — manipulating edges and vertices, finding paths and cycles, and so on." The `digraph_utils` module "allows you to navigate a graph (postorder and preorder); test for cycles, arborescences, and trees; find neighbors; and so on." Because directed graphs are closely related to set theory, the `sofs` module provides functions to convert families to directed graphs and back. The chapter notes the modules "aren't really appropriate without a good basic knowledge of either graphs or set theory" (Hébert, ch. 9, "Directed Graphs").

## Prerequisites

This is a foundational data structure within this chapter; effective use, however, presupposes background in graph or set theory (noted by the source rather than treated as a prerequisite concept).

## Key Properties

1. Implemented by two modules: `digraph` and `digraph_utils`
2. `digraph` builds and modifies graphs — vertices, edges, paths, cycles
3. `digraph_utils` navigates graphs — preorder/postorder traversal, cycle/tree/arborescence tests, neighbors
4. Closely related to set theory; `sofs` converts between families and directed graphs
5. The modules assume the user already understands graphs or set theory

## Construction / Recognition

## To Use a Directed Graph

1. Create the graph: `digraph:new()`
2. Add vertices: `digraph:add_vertex/1,2,3`
3. Add directed edges: `digraph:add_edge/3,4,5`
4. Query structure: `digraph:get_path/3`, `digraph:get_cycle/2`
5. Navigate or test properties via `digraph_utils` (e.g. `digraph_utils:topsort/1`, `digraph_utils:is_acyclic/1`)

## Examples

> The chapter provides no code example for directed graphs, deferring to the standard documentation: "If you know your stuff... you'll have no problem figuring them out by their standard documentation" (ch. 9).

## Relationships

## Related

- **Set data structure** — The `sofs` module converts families to and from directed graphs

## Common Errors

- **Error**: Treating `digraph` data as an immutable value passed around like a list
  **Correction**: `digraph` graphs are mutable structures backed by ETS-style state; they are referenced, not copied

## Common Confusions

- **Confusion**: Expecting the chapter to teach graph algorithms
  **Clarification**: The chapter only raises awareness of the modules; it assumes graph/set-theory background and points to the documentation

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Directed Graphs."

## Verification Notes

- Definition and module roles: directly from ch. 9
- Construction steps: synthesized from standard `digraph` usage since the chapter gives no code
- Confidence: MEDIUM — the chapter describes the modules but provides no worked example
