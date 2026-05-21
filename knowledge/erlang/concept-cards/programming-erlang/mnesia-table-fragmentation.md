---
# === CORE IDENTIFICATION ===
concept: Mnesia Table Fragmentation
slug: mnesia-table-fragmentation

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Table Types and Location (Fragmented Tables sidebar)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "fragmented tables"
  - "horizontal partitioning"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - mnesia-table-types
extends:
  - mnesia-table
related:
  - distributed-mnesia
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Mnesia table fragmentation?"
  - "How do I store an extremely large Mnesia table?"
---

# Quick Definition

Mnesia table fragmentation splits one very large logical table into multiple fragment tables stored on different machines. It is Mnesia's form of horizontal partitioning.

# Core Definition

"Mnesia supports 'fragmented' tables (horizontal partitioning in database terminology). This is designed for implementing extremely large tables. The tables are split into fragments that are stored on different machines. The fragments are themselves Mnesia tables. The fragments can be replicated, have indexes, and so on, like any other table" ("Fragmented Tables" sidebar). The book directs readers to the Mnesia User's Guide for full details.

# Prerequisites

- **Mnesia** — Fragmentation is an Mnesia feature.
- **Mnesia table** — A fragmented table is a set of fragment tables.
- **Mnesia table types** — Each fragment has its own storage configuration, so the storage types apply per fragment.

# Key Properties

1. A fragmented table is one logical table split into multiple fragments.
2. It is horizontal partitioning — rows are distributed across fragments.
3. Each fragment is itself an ordinary Mnesia table.
4. Fragments are stored on different machines.
5. Fragments can be replicated and indexed like any other table.
6. Designed for implementing extremely large tables.

# Construction / Recognition

## To Use Fragmented Tables:
1. Determine that a table is too large for a single (even disk-only) table on one machine.
2. Configure the table as fragmented, with fragments distributed across machines.
3. Configure replication and indexes per fragment as needed.
4. Consult the Mnesia User's Guide for the exact API and options.

## To Recognize:
1. A logical table backed by multiple fragment tables spread across nodes.

# Context & Application

Fragmentation addresses the scale ceiling of a single Mnesia table.

- **Typical contexts**: Extremely large datasets that exceed what one machine can hold.
- **Common applications**: Spreading a huge table across a cluster of machines.
- **Historical/stylistic notes**: The book covers fragmentation only in a brief sidebar and refers to the Mnesia User's Guide for the rest.

# Examples

The chapter provides no worked code example; the "Fragmented Tables" sidebar describes the concept and points to the Mnesia User's Guide for details.

# Relationships

## Builds Upon
- **Mnesia table** — A fragmented table is composed of ordinary Mnesia tables as fragments.

## Enables
- (No card depends on this concept.)

## Related
- **Distributed Mnesia** — Fragments are spread across nodes, extending Mnesia's distribution model.
- **Mnesia table types** — Each fragment chooses its own storage type.

## Contrasts With
- None.

# Common Errors

- **Error**: Trying to fit an extremely large table into a single table on one machine.
  **Correction**: Use a fragmented table to spread the data across machines.

# Common Confusions

- **Confusion**: Thinking fragments are an internal detail invisible to Mnesia.
  **Clarification**: Each fragment is itself a real Mnesia table that can be replicated and indexed.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Table Types and Location", "Fragmented Tables" sidebar.

# Verification Notes

- Definition source: Direct quote from the "Fragmented Tables" sidebar.
- Confidence rationale: MEDIUM — explicitly described but only in a short sidebar, with no example and an explicit referral to the Mnesia User's Guide.
- Uncertainties: The configuration API for fragmented tables is not given in the book.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
