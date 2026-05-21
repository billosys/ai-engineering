---
# === CORE IDENTIFICATION ===
concept: ETS Table Visibility and Ownership
slug: ets-table-visibility

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
  - "private, public, protected"
  - "ETS table ownership"
  - "ETS blackboard"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - process
extends: []
related:
  - ets-creation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Who can read and write an ETS table?"
  - "What does it mean for a process to own an ETS table?"
  - "What is the difference between private, protected, and public ETS tables?"
---

# Quick Definition

An ETS table is owned by the process that created it and has one of three visibilities — private, protected, or public — which control which other processes may read and write it.

# Core Definition

"An ETS table is said to be owned by the process that created it — when that process dies or when `ets:delete` is called, then the table is deleted" ("ETS Table Efficiency Considerations"). The visibility option set at creation determines access ("Creating an ETS Table"): a **private** table — "only the owner process can read and write this table"; a **public** table — "any process that knows the table identifier can read and write this table"; a **protected** table — "any process that knows the table identifier can read this table, but only the owner process can write to the table." Protected tables "allow data sharing at virtually zero cost" — the book likens a protected table to a "blackboard": "anybody who knows the name of the blackboard can read the blackboard, but only the owner can write on the blackboard." With a public table, "the user must ensure that reads and writes to the table are performed in a consistent manner."

# Prerequisites

- **ETS** — Visibility and ownership are properties of an ETS table.
- **Process** — A table is owned by a process and access is controlled per process.

# Key Properties

1. Every ETS table is owned by the process that created it.
2. When the owner dies (or `ets:delete` is called), the table is deleted.
3. **private** — only the owner can read or write.
4. **protected** — any process knowing the table id can read; only the owner can write (the default).
5. **public** — any process knowing the table id can read and write.
6. With a public table, the application must coordinate concurrent reads and writes itself.

# Construction / Recognition

## To choose a visibility:
1. If only the owner needs access, use `private`.
2. If many readers need cheap shared access but only one writer, use `protected` (the default).
3. If multiple processes must both read and write, use `public` — and add your own consistency control.
4. Pass the choice as an option to `ets:new`.

# Context & Application

- **Typical contexts**: Sharing read-mostly data across processes (caches, lookup tables) at near-zero cost.
- **Common applications**: "All the code in this chapter uses protected ETS tables" — the trigram table is read by many processes after being built by one.
- **Historical/stylistic notes**: The "blackboard system" metaphor — a named board everyone can read but only the owner can write.

# Examples

**Example 1** ("Creating an ETS Table"): protected tables let the trigram table be read by all local processes that know its identifier, while only the owner writes it.

**Example 2** (sidebar "ETS Tables As Blackboards"): a protected table is a named blackboard — readable by all, writable only by the owner.

# Relationships

## Builds Upon
- **ETS** — Visibility is an attribute of an ETS table.

## Related
- **Creating an ETS table** — Visibility is fixed by an option to `ets:new`.

# Common Errors

- **Error**: Using a `public` table and letting multiple processes write without coordination.
  **Correction**: With public tables, the application must ensure reads and writes are consistent.

- **Error**: Expecting a table to persist after its owner process exits.
  **Correction**: The table is deleted when the owner dies; keep the owner alive or transfer ownership.

# Common Confusions

- **Confusion**: Thinking `protected` means no other process can access the table.
  **Clarification**: Protected means other processes can *read* it; only the owner can *write* it.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", sections "Creating an ETS Table" (visibility options) and "ETS Table Efficiency Considerations" (ownership), plus the sidebar "ETS Tables As Blackboards".

# Verification Notes

- Definition source: Direct quotes from "Creating an ETS Table" and the blackboard sidebar.
- Confidence rationale: HIGH — the three visibilities and ownership rule are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs `ets`, `process` used.
- Re-extraction notes: Fresh extraction.
