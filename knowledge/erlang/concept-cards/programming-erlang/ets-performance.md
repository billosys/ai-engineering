---
# === CORE IDENTIFICATION ===
concept: ETS Performance Characteristics
slug: ets-performance

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
section: "ETS Table Efficiency Considerations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ETS efficiency"
  - "ETS table efficiency considerations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
  - ets-table-types
extends:
  - ets
related:
  - binary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the performance characteristics of ETS tables?"
  - "Why is an ordered set slower than a set?"
  - "How is data copied in and out of an ETS table?"
---

# Quick Definition

ETS tables are hash tables (except ordered sets, which are balanced binary trees). Lookups and inserts are fast; data is copied in and out of the table; large binaries are shared rather than copied; and there is no garbage-collection penalty.

# Core Definition

"Internally, ETS tables are represented by hash tables (except ordered sets, which are represented by balanced binary trees). This means there is a slight space penalty for using sets and a time penalty for using ordered sets. Inserting into sets takes place in constant time, but inserting into an ordered set takes place in a time proportional to the log of the number of entries" ("ETS Table Efficiency Considerations"). "Bags are more expensive to use than duplicate bags, since on each insertion all elements with the same key have to be compared for equality." ETS tables live in "a separate storage area that is not associated with normal process memory" and "are not garbage collected." When a tuple is inserted, "all the data structures representing the tuple are copied from the process stack and heap into the ETS table"; on lookup, the resultant tuples are copied back. The exception is large binaries, which "are stored in their own off-heap storage area" shared by processes and tables and managed by a reference-counting garbage collector — making it "very cheap" to insert tuples containing binaries.

# Prerequisites

- **ETS** — These are properties of ETS tables.
- **ETS table types** — The performance differences are tied to set/ordered_set/bag/duplicate_bag.

# Key Properties

1. Sets, bags, and duplicate bags are hash tables; ordered sets are balanced binary trees.
2. Inserting into a set is constant time; inserting into an ordered set is logarithmic time.
3. Sets carry a slight space penalty; ordered sets carry a time penalty.
4. Bags are more expensive than duplicate bags — each insert compares all same-key elements for equality.
5. Inserting copies tuple data from the process stack/heap into the table; lookups copy it back.
6. Large binaries are stored off-heap and shared (reference counted), so inserting tuples with binaries is cheap.
7. ETS tables are not garbage collected — huge tables incur no GC penalty.

# Construction / Recognition

## To make good performance choices:
1. Use a `set` for fast constant-time inserts and lookups; use `ordered_set` only if you need sorted iteration.
2. Prefer `duplicate_bag` over `bag` when many tuples share a key, to avoid per-insert equality comparisons.
3. Represent strings and large untyped blocks as binaries so they are shared, not copied.
4. Measure the most time-consuming operations rather than guessing.

# Context & Application

- **Typical contexts**: Choosing table type and data representation for large, performance-sensitive tables.
- **Common applications**: The trigram benchmark measures build and lookup times for ETS set, ETS ordered_set, and the `sets` module — the ETS set wins.
- **Historical/stylistic notes**: The book recommends timing only the most time-consuming operations and writing the rest in the most beautiful way possible.

# Examples

**Example 1** ("Table-Building Time"): insertion per trigram measured at 2.9 µs (ETS ordered set), 1.5 µs (ETS set), 9.3 µs (`sets` module).

**Example 2** ("Table Access Times"): lookup per trigram measured at 1.8 µs (ETS ordered set), 0.72 µs (ETS set), 1.35 µs (`sets` module) — "the ETS set won by a large margin."

# Relationships

## Builds Upon
- **ETS** — These are the runtime characteristics of ETS tables.

## Related
- **Binary** — Large binaries are stored off-heap and shared, making binary-heavy tuples cheap to store.

# Common Errors

- **Error**: Using an ordered set when sorting is not actually needed.
  **Correction**: Use a plain set for constant-time inserts; reserve ordered_set for when sorted iteration is required.

- **Error**: Using a `bag` for large numbers of same-key tuples.
  **Correction**: Use a `duplicate_bag` to avoid the per-insert equality comparison of all same-key elements.

# Common Confusions

- **Confusion**: Thinking large ETS tables slow the system through garbage collection.
  **Clarification**: ETS tables are not garbage collected; very large tables incur no GC penalty.

- **Confusion**: Believing inserting a large string into ETS copies the whole string.
  **Clarification**: If the string is a binary, it is stored off-heap and shared by reference count, not copied.

# Source Reference

Chapter 19: "Storing Data with ETS and DETS", section "ETS Table Efficiency Considerations" and the trigram timing subsections "Table-Building Time" and "Table Access Times".

# Verification Notes

- Definition source: Direct quotes from "ETS Table Efficiency Considerations".
- Confidence rationale: HIGH — performance characteristics are explicitly stated with measured numbers.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs `ets`, `binary` used.
- Re-extraction notes: Fresh extraction.
