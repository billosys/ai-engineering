---
# === CORE IDENTIFICATION ===
concept: ETS Table Types
slug: ets-table-types

# === CLASSIFICATION ===
category: performance
subcategory: term-storage
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Storing Data with ETS and DETS"
chapter_number: 19
pdf_page: null
section: "Types of Table"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "set, ordered_set, bag, duplicate_bag"
  - "ETS set and bag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
extends:
  - ets
related:
  - ets-performance
  - ets-creation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the ETS table types?"
  - "What is the difference between a set and a bag?"
  - "Which ETS table type should I choose?"
---

# Quick Definition

ETS and DETS tables come in four types — set, ordered_set, bag, and duplicate_bag — which differ in whether keys must be unique and whether identical tuples may be duplicated.

# Core Definition

"Each of the basic set and bag table types has two variants, making for a total of four types of table: sets, ordered sets, bags, and duplicate bags" ("Types of Table"). In a **set**, "all the keys in the different tuples in the table must be unique." In an **ordered set**, the tuples are also sorted (by key). In a **bag** "there can be more than one tuple with the same key, but no two tuples in the bag can be identical." In a **duplicate bag** "several tuples can have the same key, and the same tuple can occur many times in the same table." "Choosing the correct type of table has important consequences for the performance of your applications."

# Prerequisites

- **ETS** — Table types are an attribute of ETS (and DETS) tables.

# Key Properties

1. **set** — keys are unique; one tuple per key; inserting a new tuple with an existing key replaces it.
2. **ordered_set** — like set, but tuples are kept sorted by key.
3. **bag** — multiple tuples may share a key, but no two tuples may be identical.
4. **duplicate_bag** — multiple tuples may share a key, and identical tuples may be repeated.
5. The type is fixed when the table is created (passed as an option to `ets:new`).
6. The choice affects performance and the result of inserting duplicate or same-key tuples.

# Construction / Recognition

## To choose a table type:
1. If keys must be unique, use `set`; if you also need sorted iteration, use `ordered_set`.
2. If several tuples may share a key (but should not be identical), use `bag`.
3. If identical tuples should be allowed to repeat, use `duplicate_bag`.
4. Pass the chosen type as an option to `ets:new(Name, [Type])`.

## To recognize behavior on insert:
1. `set`/`ordered_set`: inserting `{a,1}` then `{a,3}` leaves only `{a,3}`.
2. `bag`: inserting `{a,1}` then `{a,3}` leaves both; inserting `{a,1}` twice leaves one copy.
3. `duplicate_bag`: inserting `{a,1}` twice leaves two copies of `{a,1}`.

# Context & Application

- **Typical contexts**: Deciding how a table should handle keys and duplicates.
- **Common applications**: The trigram example uses a `set` because trigrams are unique keys with no value.
- **Historical/stylistic notes**: The chapter tests all four types with the same insertions to show the differences.

# Examples

**Example 1** ("Types of Table"): inserting `{a,1}`, `{b,2}`, `{a,1}`, `{a,3}` yields:
- `set => [{b,2},{a,3}]`
- `ordered_set => [{a,3},{b,2}]`
- `bag => [{b,2},{a,1},{a,3}]`
- `duplicate_bag => [{b,2},{a,1},{a,1},{a,3}]`

# Relationships

## Builds Upon
- **ETS** — Table types are a property of an ETS table.

## Related
- **ETS performance** — Type choice affects time and space cost (e.g., ordered_set vs. set).
- **Creating an ETS table** — The type is given as an option to `ets:new`.

# Common Errors

- **Error**: Using a `bag` when identical duplicate tuples must be kept.
  **Correction**: Use a `duplicate_bag`; a regular bag keeps only one copy of identical tuples.

- **Error**: Expecting a `set` to keep both `{a,1}` and `{a,3}`.
  **Correction**: A set keys uniquely; the later insert replaces the earlier tuple.

# Common Confusions

- **Confusion**: Thinking `ordered_set` orders by insertion order.
  **Clarification**: An ordered set is sorted by the *key*, not by insertion order.

- **Confusion**: Believing a `bag` allows identical duplicate tuples.
  **Clarification**: A bag allows multiple tuples per key but no two *identical* tuples; only a duplicate_bag allows that.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", section "Types of Table".

# Verification Notes

- Definition source: Direct quotes from "Types of Table".
- Confidence rationale: HIGH — the four types are explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slug `ets` used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
