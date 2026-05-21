---
# === CORE IDENTIFICATION ===
concept: ETS vs DETS
slug: ets-vs-dets

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
  - "ETS versus DETS"
  - "memory vs disk term storage"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - dets
extends: []
related:
  - ets-table-types
  - mnesia
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ETS relate to DETS?"
  - "What is the difference between ETS and DETS?"
  - "When should I use ETS instead of DETS?"
---

# Quick Definition

ETS and DETS perform the same task — large key-value tables of Erlang tuples — but ETS is memory resident and transient while DETS is disk resident and persistent; ETS is far faster, DETS uses far less memory.

# Core Definition

"ETS and DETS perform basically the same task: they provide large key-value lookup tables. ETS is memory resident, while DETS is disk resident" ("Storing Data with ETS and DETS"). "ETS is highly efficient — using ETS, you can ... perform lookups in constant (or in some cases logarithmic) time. DETS provides almost the same interface as ETS but stores the tables on disk. Because DETS uses disk storage, it is far slower than ETS but will have a much smaller memory footprint when running." Data in an ETS table "is stored in RAM and is transient" — deleted when the table or its owning process dies. Data in DETS tables "is persistent and should survive an entire system crash." Both store collections of tuples, both support the same core operations, and both can be shared between processes — but with different sharing semantics (ETS by table identifier and ownership; DETS by global name with reference-counted opening).

# Prerequisites

- **ETS** — One side of the comparison.
- **DETS** — The other side of the comparison.

# Key Properties

1. Both provide large key-value lookup tables of Erlang tuples.
2. ETS is memory resident; DETS is disk resident.
3. ETS data is transient (lost when the table/owner dies); DETS data is persistent (survives a system crash).
4. ETS is far faster; DETS is far slower but has a much smaller memory footprint.
5. DETS files are limited to 2 GB; ETS is limited only by available memory.
6. Both share almost the same interface — `insert`, `lookup`, the four table types.
7. DETS files must be explicitly opened and closed; ETS tables are created and deleted.

# Construction / Recognition

## To choose between ETS and DETS:
1. If the data must persist across runs or survive a crash, use DETS.
2. If speed is critical and the data is transient (or can be rebuilt), use ETS.
3. If memory footprint must stay small, favor DETS.
4. For richer querying (multi-key indexing, transactions), use Mnesia, which is built on both.

# Context & Application

- **Typical contexts**: Deciding where to store large volumes of Erlang terms.
- **Common applications**: The chapter uses ETS for the (rebuildable) trigram table and DETS for the (persistent) filename index.
- **Historical/stylistic notes**: Mnesia uses ETS and DETS internally; many of their exported routines are intended for Mnesia's internal use.

# Examples

**Example 1** ("Example Programs with ETS"): the trigram table is held in ETS — it is fast and can be rebuilt or saved with `ets:tab2file`.

**Example 2** ("Example: A Filename Index"): the filename-to-index mapping is held in DETS so it persists across application runs.

# Relationships

## Related
- **ETS table types** — Both ETS and DETS support set, ordered_set, bag, duplicate_bag.
- **Mnesia** — A higher-level database built on top of both ETS and DETS.

# Common Errors

- **Error**: Using ETS for data that must survive a restart.
  **Correction**: Use DETS (or persist the ETS table with `ets:tab2file`) for data that must be durable.

- **Error**: Using DETS for hot-path lookups where latency matters.
  **Correction**: Use ETS; DETS is far slower because it goes to disk.

# Common Confusions

- **Confusion**: Thinking ETS and DETS have entirely different APIs.
  **Clarification**: DETS provides almost the same interface as ETS — `insert` and `lookup` behave identically.

- **Confusion**: Believing either ETS or DETS gives database features like multi-key indexing.
  **Clarification**: A single ETS/DETS table indexes one key; for relational-style features use Mnesia.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", chapter introduction; comparison reinforced in "Storing Tuples on Disk" and "What Haven't We Talked About?".

# Verification Notes

- Definition source: Direct quotes from the chapter introduction.
- Confidence rationale: HIGH — the comparison is explicitly drawn in the chapter intro.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs `ets`, `dets`, `mnesia` used.
- Re-extraction notes: Fresh extraction.
