---
# === CORE IDENTIFICATION ===
concept: ETS (Erlang Term Storage)
slug: ets

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
section: "Storing Data with ETS and DETS"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang term storage"
  - ets
  - "ETS table"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - tuple
extends: []
related:
  - ets-table-types
  - ets-table-visibility
  - ets-performance
  - ets-creation
  - mnesia
contrasts_with:
  - dets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ETS (Erlang Term Storage)?"
  - "How do I store and query data with ETS and DETS?"
  - "When should I use ETS?"
---

# Quick Definition

ETS (Erlang Term Storage) is a system module providing large, efficient, memory-resident key-value lookup tables of Erlang tuples, with constant- or logarithmic-time lookups and no garbage collection overhead.

# Core Definition

"ETS is short for Erlang term storage" — `ets` is a system module "you can use for the efficient storage of large numbers of Erlang terms" ("Storing Data with ETS and DETS"). ETS provides "large key-value lookup tables" that are memory resident: "using ETS, you can store colossal amounts of data (if you have enough memory) and perform lookups in constant (or in some cases logarithmic) time." An ETS table "is just a collection of Erlang tuples." Data in an ETS table "is stored in RAM and is transient. The data will be deleted when the ETS table is disposed of or the owning Erlang process terminates." ETS tables "look as if they were implemented in Erlang, but in fact they are implemented in the underlying runtime system" and "are not garbage collected", so very large tables incur no garbage-collection penalty. Tables "can be shared by several processes, making interprocess access to common data highly efficient."

# Prerequisites

- **Process** — An ETS table is owned by the process that created it and dies with it.
- **Tuple** — Every entry in an ETS table is a tuple; one element (by default the first) is the key.

# Key Properties

1. Memory resident (RAM); data is transient and lost when the table or its owner dies.
2. Stores collections of Erlang tuples; one element (default: position 1) is the key.
3. Lookups run in constant time (hash tables) or logarithmic time (ordered sets).
4. Implemented in the runtime system, not in Erlang itself.
5. Not garbage collected — huge tables incur no GC penalty.
6. Tables can be shared by several processes for efficient interprocess data access.
7. The four basic operations are: create/open, insert, lookup, dispose.

# Construction / Recognition

## The four basic operations:
1. **Create** a table with `ets:new(Name, [Opt])`, returning a table identifier.
2. **Insert** tuples with `ets:insert(TableId, X)`, where `X` is a tuple or list of tuples.
3. **Look up** tuples with `ets:lookup(TableId, Key)`, returning a list of matching tuples (empty list if none).
4. **Dispose** of the table with `ets:delete(TableId)`.

## To recognize ETS use:
1. Calls to the `ets` module create and operate on tables.
2. Data persists only while the owning process is alive.

# Context & Application

- **Typical contexts**: Applications that "manipulate large amounts of data in an efficient manner and where it is too costly to program with nondestructive assignment and 'pure' Erlang data structures."
- **Common applications**: The chapter builds an ETS-based trigram table to predict whether a string is an English word.
- **Historical/stylistic notes**: Mnesia is implemented using ETS and DETS; many `ets` routines are intended for internal use by Mnesia.

# Examples

**Example 1** ("Types of Table", `ets_test.erl`): `test_ets/1` creates a table with `ets:new(test, [Mode])`, inserts `{a,1}`, `{b,2}`, `{a,1}`, `{a,3}`, and dumps it with `ets:tab2list`.

**Example 2** ("Example Programs with ETS", `lib_trigrams.erl`): an ETS set stores every English-language trigram as a `{<<"ABC">>}` tuple for fast lookup.

# Relationships

## Enables
- **Mnesia** — Mnesia is built on top of ETS and DETS tables.

## Related
- **ETS table types** — set, ordered_set, bag, duplicate_bag determine key/duplication behavior.
- **ETS table visibility** — private/protected/public control which processes may read/write.
- **ETS performance** — Hash-table vs. tree representation and copy semantics.
- **Creating an ETS table** — `ets:new` and its options.

## Contrasts With
- **DETS** — DETS provides almost the same interface but stores tables on disk (persistent, slower).

# Common Errors

- **Error**: Expecting ETS data to survive after the owning process terminates.
  **Correction**: ETS is transient; use DETS or write the table to a file (`ets:tab2file`) for persistence.

- **Error**: Assuming `ets:lookup` returns a single tuple.
  **Correction**: `lookup` always returns a *list* of tuples (possibly empty), so the same function works for sets and bags.

# Common Confusions

- **Confusion**: Thinking ETS tables are ordinary garbage-collected Erlang terms.
  **Clarification**: ETS tables live in a separate runtime storage area and are not garbage collected.

- **Confusion**: Believing ETS gives a relational database with multi-key indexing.
  **Clarification**: A single ETS table indexes on only one key; for richer querying use Mnesia.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", chapter introduction and section "Types of Table".

# Verification Notes

- Definition source: Direct quotes from the chapter introduction.
- Confidence rationale: HIGH — ETS is explicitly and thoroughly defined.
- Uncertainties: None.
- Cross-reference status: Verified; `mnesia`, `tuple`, `process` are canonical slugs; `ets-creation` referenced as the creation card.
- Re-extraction notes: Fresh extraction; overwrites prior card. This is the canonical `ets` card owned by this extraction.
