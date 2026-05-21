---
# === CORE IDENTIFICATION ===
concept: ETS Table Ownership and Visibility
slug: ets-table-ownership

# === CLASSIFICATION ===
category: performance
subcategory: data-storage
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
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
  - "ETS table owner"
  - "private, protected, public"
  - "named_table"
  - "ETS visibility"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - process
extends: []
related:
  - ets-table-types
  - ets-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Who owns an ETS table?"
  - "What is the difference between a private, protected, and public ETS table?"
---

# Quick Definition

An ETS table is owned by the process that created it and is destroyed when that process dies; its visibility option — private, protected, or public — controls which other processes may read or write it.

# Core Definition

You create ETS tables with `ets:new(Name, [Opt])`, and "the process that creates the table is called the owner of the table" ("Creating an ETS Table"). When the table is created it gets a set of options that cannot afterward be changed; if the owner process dies, the space for the table is automatically deallocated. The owner can also delete the table explicitly with `ets:delete`. The visibility options control access: a **private** table can be read and written only by the owner; a **public** table can be read and written by any process that knows the table identifier; a **protected** table can be read by any process that knows the identifier but written only by the owner. The `named_table` option lets the table's `Name` atom be used in subsequent operations, and `{keypos, K}` changes which tuple position is the key. Opening a table with zero options is the same as opening it with `[set, protected, {keypos, 1}]`.

# Prerequisites

- **ETS (Erlang Term Storage)** — Ownership and visibility are properties of an ETS table.
- **Process** — The owner is a process, and table lifetime is tied to that process.

# Key Properties

1. The creating process is the table's owner.
2. The table's options are fixed at creation and cannot be changed.
3. When the owner process dies, the table's space is automatically deallocated.
4. `private` — only the owner can read or write.
5. `protected` — anyone with the table identifier can read; only the owner can write.
6. `public` — anyone with the table identifier can read and write.
7. `named_table` — the `Name` atom can be used for subsequent table operations.
8. `{keypos, K}` — uses position `K` as the key instead of the default position 1.
9. The default options are `[set, protected, {keypos, 1}]`.

# Construction / Recognition

## To create a table with a given ownership/visibility:

1. Decide the visibility: `private`, `protected`, or `public`.
2. Call `ets:new(Name, [Type, Visibility | Opts])`; the calling process becomes owner.
3. Optionally add `named_table` to address the table by its name atom, or `{keypos, K}` for a non-default key.

## To recognize the access model:

1. A `protected` table acts as a "blackboard" — many readers, one writer.
2. A `public` table requires the application itself to keep reads and writes consistent.

# Context & Application

Visibility choice governs how an ETS table can be shared safely between processes.

- **Typical contexts**: Shared lookup tables, configuration blackboards, shared counters.
- **Common applications**: The chapter uses `protected` tables throughout, calling them a "blackboard system" — many can read, one can write.
- **Historical/stylistic notes**: A `public` table needs the user to ensure consistent reads and writes; a `protected` table gives data sharing "at virtually zero cost."

# Examples

**Example 1** ("Creating an ETS Table"): the chapter lists the options to `ets:new` — `set | ordered_set | bag | duplicate_bag`, `private`, `public`, `protected`, `named_table`, `{keypos, K}`.

**Example 2** ("ETS Tables As Blackboards" sidebar): a `protected` table is described as a named blackboard — anyone who knows the name can read it, but only the owner can write to it.

# Relationships

## Builds Upon

- **ETS (Erlang Term Storage)** — Ownership/visibility specialize how an ETS table is accessed.
- **Process** — The owning process determines the table's lifetime.

## Related

- **ETS table types** — Type and visibility are both fixed at `ets:new` time.
- **ETS operations** — Whether `insert` succeeds for a non-owner depends on visibility.

# Common Errors

- **Error**: Expecting to change a table's options after creation.
  **Correction**: Options are fixed at creation; create a new table if different options are needed.

- **Error**: Writing to a `protected` table from a non-owner process.
  **Correction**: Only the owner may write a `protected` table; use `public` if multiple writers are required.

# Common Confusions

- **Confusion**: Thinking a table outlives the process that created it.
  **Clarification**: When the owner process dies, the table is automatically deallocated.

- **Confusion**: Believing `public` tables provide concurrency safety.
  **Clarification**: With a `public` table the user must ensure reads and writes are performed consistently.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS," section "Creating an ETS Table" and the "ETS Tables As Blackboards" sidebar. EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of "Creating an ETS Table."
- Confidence rationale: HIGH — ownership and the three visibility options are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
