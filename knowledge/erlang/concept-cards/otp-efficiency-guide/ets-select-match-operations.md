---
concept: ETS Select/Match Operations
slug: ets-select-match-operations
category: performance
subcategory: ets
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Select/Match Operations"
extraction_confidence: high
aliases:
  - "ets:select"
  - "ets:match"
  - "ETS pattern matching"
  - "match specification"
prerequisites:
  - ets-key-usage-and-indexing
extends: []
related:
  - ets-tab2list-avoidance
  - ordered-set-tables
  - mnesia-secondary-index
contrasts_with: []
answers_questions:
  - "How does `ets:select/2` compare to `ets:tab2list/1` for data retrieval?"
  - "What distinguishes `ets:select/2` from `ets:match/2`?"
  - "How do I use `ets:select/2` instead of `ets:tab2list/1`?"
---

# Quick Definition

Select/match operations on ETS tables can be expensive as they usually scan the complete table. However, `ets:select/2` is preferred over `ets:match/2` and `ets:match_object/2`, and all are more efficient than `ets:tab2list/1` followed by list processing.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Select/Match Operations" section): "Select/match operations on Ets and Mnesia tables can become very expensive operations. They usually need to scan the complete table. Try to structure the data to minimize the need for select/match operations. However, if you require a select/match operation, it is still more efficient than using `tab2list`."

The preference ordering is: "The functions `ets:select/2` and `mnesia:select/3` are to be preferred over `ets:match/2`, `ets:match_object/2`, and `mnesia:match_object/3`."

There are cases where select/match does not scan the complete table:
1. Part of the key is bound when searching an `ordered_set` table
2. The table is a Mnesia table with a secondary index on the matched field
3. The key is fully bound (though a direct lookup is better unless it is a bag table with subset interest)

# Prerequisites

- **ets-key-usage-and-indexing** -- Understanding key-based lookups explains why select/match is a fallback

# Key Properties

1. Select/match operations usually require a full table scan
2. `ets:select/2` is preferred over `ets:match/2` and `ets:match_object/2`
3. All select/match operations are more efficient than `ets:tab2list/1` plus list processing
4. Partial key binding on `ordered_set` tables avoids full scan
5. Mnesia secondary indexes avoid full scan for indexed fields
6. For fully bound keys, use `ets:lookup/2` instead of select/match (unless bag table with subset interest)
7. The `_ = '_'` shorthand efficiently creates wildcard records for match specifications

# Construction / Recognition

## Creating Match Specifications

1. Use the record wildcard shorthand for match patterns:
   ```erlang
   #person{age = 42, _ = '_'}.
   ```
2. This is "the easiest and fastest way" to create a record with most fields as wildcards

## Choosing the Right Operation

1. If the key is known: use `ets:lookup/2` (constant time for `set`, O(log N) for `ordered_set`)
2. If searching on a non-key field: use `ets:select/2` with a match specification
3. If searching on a partially bound key in an `ordered_set`: select/match benefits from key ordering
4. Prefer `ets:select/2` over `ets:match/2` and `ets:match_object/2`

# Context & Application

Match specifications in ETS are a powerful but potentially expensive mechanism. They use a pattern-matching language compiled into the ETS engine, avoiding the overhead of extracting all data to the Erlang process heap (as `tab2list` does). The preference for `ets:select/2` over `ets:match/2` reflects that `select` supports a richer specification language with guards and result transformations.

The select/match operations apply equally to Dets tables, which share the same API.

# Examples

**Record wildcard pattern** (Tables and Databases chapter):
```erlang
#person{age = 42, _ = '_'}.
```
This creates a match pattern where age is 42 and all other fields are wildcards.

**Select vs. tab2list** -- see the `ets-tab2list-avoidance` card for detailed DO/DO NOT examples showing `ets:select/2` as the preferred alternative to `ets:tab2list/1` plus list processing.

# Relationships

## Related

- **ets-tab2list-avoidance** -- Detailed examples of replacing tab2list with select
- **ordered-set-tables** -- Ordered sets enable partial key optimization for select/match
- **mnesia-secondary-index** -- Secondary indexes enable efficient select on non-key fields

# Common Errors

- **Error**: Using `ets:match/2` when `ets:select/2` would work
  **Correction**: Prefer `ets:select/2` -- it has a richer specification language and is the recommended function

- **Error**: Using select/match when a key lookup would suffice
  **Correction**: Always use `ets:lookup/2` when the key is known; it is significantly faster (no table scan)

- **Error**: Manually constructing wildcard records field by field
  **Correction**: Use `#record{matched_field = Value, _ = '_'}` for the fastest wildcard construction

# Common Confusions

- **Confusion**: Thinking `ets:select/2` always scans the complete table
  **Clarification**: It does not need a full scan when part of the key is bound on an `ordered_set`, or when using Mnesia with a secondary index

- **Confusion**: Believing `ets:match/2` and `ets:select/2` are equivalent
  **Clarification**: `ets:select/2` is preferred because it supports match specifications with guards and result transformations; `ets:match/2` only supports simple pattern matching

- **Confusion**: Thinking select/match on a fully bound key is useful
  **Clarification**: If the key is fully bound, `ets:lookup/2` is more efficient; select/match on a fully bound key is only useful for bag tables when interested in a subset of elements with that key

# Source Reference

Tables and Databases chapter, "Select/Match Operations" section. Includes the record wildcard shorthand example and the preference ordering for select vs. match functions.

# Verification Notes

- Definition: Directly extracted from the source section text
- Preference ordering: Quoted from source
- Exceptions to full scan: All three cases explicitly listed in source
- Record wildcard: Directly from source code example
- Confidence: HIGH -- explicit guidance with clear preference ordering in official documentation
