---
# === CORE IDENTIFICATION ===
concept: Creating an ETS Table
slug: ets-creation

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
section: "Creating an ETS Table"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ets:new"
  - "ETS table options"
  - "{keypos, K}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
extends: []
related:
  - ets-table-types
  - ets-table-visibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an ETS table?"
  - "What options does ets:new take?"
  - "What is the default ETS table configuration?"
---

# Quick Definition

An ETS table is created with `ets:new(Name, [Opt])`, which returns a table identifier. The option list fixes the table's type, visibility, and key position; these options cannot be changed afterward.

# Core Definition

"You create ETS tables by calling `ets:new`. The process that creates the table is called the owner of the table. When you create the table, it has a set of options that cannot be changed" ("Creating an ETS Table"). The spec is `ets:new(Name, [Opt]) -> TableId` where `Name` is an atom. Options come from: the type (`set | ordered_set | bag | duplicate_bag`); the visibility (`private | public | protected`); `named_table`, which lets `Name` itself be used in subsequent table operations; and `{keypos, K}`, which uses position `K` as the key (normally position 1). "Opening an ETS table with zero options is the same as opening it with the options `[set, protected, {keypos,1}]`." If the owner process dies, the table's space is automatically deallocated; a table can also be removed with `ets:delete`.

# Prerequisites

- **ETS** — Creation produces an ETS table; understanding ETS is required first.

# Key Properties

1. `ets:new(Name, [Opt])` returns a table identifier; `Name` is an atom.
2. Options chosen at creation cannot be changed afterward.
3. Default options (empty list) are `[set, protected, {keypos, 1}]`.
4. `named_table` allows the atom `Name` to be used directly in later operations.
5. `{keypos, K}` sets the key to tuple position `K` (default 1) — useful for records, where position 1 is the record name.
6. The creating process is the table's owner; the table is freed when the owner dies or `ets:delete` is called.

# Construction / Recognition

## To create an ETS table:
1. Choose a `Name` atom.
2. Build the option list: a type, optionally a visibility, optionally `named_table`, optionally `{keypos, K}`.
3. Call `TableId = ets:new(Name, [Opt])`.
4. Use the returned `TableId` (or `Name`, if `named_table`) for inserts and lookups.

# Context & Application

- **Typical contexts**: The first step in any ETS-based program.
- **Common applications**: `ets:new(test, [Mode])` in the table-types example; `ets:new(table, [Type])` in the trigram builder.
- **Historical/stylistic notes**: `{keypos, K}` is mainly used when storing records, since a record's first element is the record name rather than a useful key.

# Examples

**Example 1** ("Types of Table"): `TableId = ets:new(test, [Mode])` creates a table of one of the four types.

**Example 2** ("Build the Tables"): `Tab = ets:new(table, [Type])` creates the trigram table.

# Relationships

## Builds Upon
- **ETS** — Creation instantiates an ETS table.

## Related
- **ETS table types** — The type option chosen at creation.
- **ETS table visibility** — The private/protected/public option chosen at creation.

# Common Errors

- **Error**: Trying to change a table's type or visibility after creation.
  **Correction**: These options are fixed at creation time; choose them correctly up front.

- **Error**: Storing records without `{keypos, K}` and getting the record name as the key.
  **Correction**: Use `{keypos, K}` so a meaningful field becomes the key.

# Common Confusions

- **Confusion**: Thinking an ETS table created with no options is unprotected.
  **Clarification**: Zero options means `[set, protected, {keypos, 1}]` — protected by default.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", section "Creating an ETS Table".

# Verification Notes

- Definition source: Direct quotes from "Creating an ETS Table".
- Confidence rationale: HIGH — `ets:new` and all its options are explicitly documented.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slug `ets` used.
- Re-extraction notes: Fresh extraction.
