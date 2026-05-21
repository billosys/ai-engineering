---
concept: Ordered Set Tables
slug: ordered-set-tables
category: data-structures
subcategory: ets
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "`ordered_set` Tables"
extraction_confidence: high
aliases:
  - "ordered_set"
  - "ETS ordered set"
  - "ordered ETS table"
prerequisites:
  - ets-key-usage-and-indexing
extends: []
related:
  - ets-select-match-operations
contrasts_with: []
answers_questions:
  - "When should I use ordered_set instead of set for ETS tables?"
  - "How does ordered_set affect select and match operations?"
---

# Quick Definition

The `ordered_set` table type maintains keys in Erlang term order, making results from `select`, `match_object`, and `foldl` ordered by key. It also enables partial key optimization for select/match operations, avoiding full table scans in some cases.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "`ordered_set` Tables" section): "If the data in the table is to be accessed so that the order of the keys in the table is significant, the table type `ordered_set` can be used instead of the more usual `set` table type."

Key characteristics:
- "An `ordered_set` is always traversed in Erlang term order regarding the key field"
- Return values from `select`, `match_object`, and `foldl` are ordered by key values
- Traversal with `first` and `next` returns keys in order
- "An `ordered_set` only guarantees that objects are processed in _key_ order. Results from functions such as `ets:select/2` appear in _key_ order even if the key is not included in the result."

The `ordered_set` also enables an optimization noted in the Select/Match section: when part of the key is bound during a search on an `ordered_set`, the select/match operation does not need to scan the complete table.

# Prerequisites

- **ets-key-usage-and-indexing** -- Understanding ETS table types and key usage

# Key Properties

1. Keys are maintained in Erlang term order
2. `select`, `match_object`, and `foldl` return results in key order
3. `first`/`next` traversal returns keys in order
4. Results are in key order even when the key is not included in the result
5. Partial key binding during select/match avoids full table scan
6. Key lookup is O(log N) (tree-based) vs. O(1) for `set` (hash-based)
7. The `ordered_set` type replaces the more usual `set` type

# Construction / Recognition

## When to Use ordered_set

1. Application logic requires keys in sorted order
2. Range queries on keys are common (partial key binding optimization)
3. Ordered traversal is needed (e.g., iterating from smallest to largest key)

## When to Prefer set

1. Key order does not matter
2. Maximum lookup speed is needed (O(1) hash vs. O(log N) tree)
3. The table is very large and only exact-key lookups are performed

# Context & Application

The `ordered_set` table type is backed by a balanced tree (AVL tree in the BEAM implementation), providing O(log N) lookups and ordered traversal. This is in contrast to the `set` type which uses a hash table for O(1) lookups but unordered storage.

The partial key optimization is particularly valuable: if the key is a tuple and the first element(s) are bound in a match specification, the `ordered_set` can use the tree structure to narrow the search range, avoiding a full table scan.

# Examples

**Ordered traversal** (Tables and Databases chapter): "Traversing an `ordered_set` with the `first` and `next` operations also returns the keys ordered."

**Key-order guarantee** (Tables and Databases chapter): "Results from functions such as `ets:select/2` appear in _key_ order even if the key is not included in the result."

**Partial key optimization** (Select/Match section): "if part of the key is bound when searching an `ordered_set` table" the select/match operation does not need to scan the complete table.

# Relationships

## Related

- **ets-select-match-operations** -- Select/match can be optimized on ordered_set with partial key binding

# Common Errors

- **Error**: Using `ordered_set` when key order is never needed, paying the O(log N) lookup cost
  **Correction**: Use `set` for hash-based O(1) lookups when ordering is not required

- **Error**: Assuming `ordered_set` sorts by values, not keys
  **Correction**: Only key order is guaranteed; values have no guaranteed ordering

# Common Confusions

- **Confusion**: Thinking `ordered_set` results are ordered by insertion time
  **Clarification**: Results are ordered by Erlang term order of the key, not by insertion order

- **Confusion**: Believing that select/match on `ordered_set` always avoids full table scan
  **Clarification**: The optimization only applies when part of the key is bound; a fully unbound key still requires a full scan

- **Confusion**: Thinking ordered results require sorting after retrieval
  **Clarification**: Results from `ordered_set` tables are already in key order; no `lists:sort/1` is needed

# Source Reference

Tables and Databases chapter, "`ordered_set` Tables" section. Also references the "Select/Match Operations" section for the partial key optimization.

# Verification Notes

- Definition: Directly quoted from source text
- Key order guarantee: Directly quoted, including the note about results being in key order even without the key in results
- Partial key optimization: Cross-referenced from the Select/Match section
- Confidence: HIGH -- explicit descriptions and an info note in official documentation
